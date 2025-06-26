from datetime import timezone
from blog.serialazer import UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import timedelta
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from course.models import Course, Lesson, Test, Follow, TestBasicModel
from course.serialazer import CourseSerializer, FollowSerializer, LessonSerializer, TestSerializer, TestBasicSerializer
from blog.permission import IsStudent, IsTeacher


@swagger_auto_schema(
    method="post",
    responses={200: FollowSerializer(many=True)},
    request_body=FollowSerializer,
    tags=["Follow"],
)
@api_view(['POST'])
@permission_classes([IsStudent])
def follow_student_view(request):
    serializer = FollowSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user,course_id=serializer.validated_data['course_id'])
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="get",
    responses={200: FollowSerializer(many=True)},
    tags=["Follow"],
)
@api_view(['GET'])
@permission_classes([IsTeacher])
def teacher_ability_view(request):
    course = Course.objects.filter(user=request.user)
    student = Follow.objects.filter(course__in=course)

    serializer = FollowSerializer(student, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="get",
    responses={200: CourseSerializer(many=True)},
    tags=["Follow"],
)
@api_view(['GET'])
@permission_classes([IsStudent])
def student_ability_view(request):
    course = Follow.objects.filter(user=request.user).values_list("course_id", flat=True)

    lesson = Course.objects.filter(id__in=course).prefetch_related("lesson")

    serializer = CourseSerializer(lesson, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="get",
    tags=["Follow"],
)
@permission_classes([IsStudent])
@api_view(['GET'])
def statistic_view(request, course_id):
    course = Course.objects.filter(id=course_id).first()
    if not course:
        return Response(data={"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    followed_curs = Follow.objects.filter(user=request.user, course=course).first()
    if not followed_curs:
        return Response(data={"error": "Follow not found"}, status=status.HTTP_400_BAD_REQUEST)
    lessons = course.lesson.all()
    lesson_data = [{"title": lesson.title} for lesson in lessons]
    test = Test.objects.filter(lesson__in=lessons)
    test_data = [{"id": test.id, "title": test.title,"started_date":test.start_date,"end_date":test.end_date} for test in test]


    test_result = TestBasicModel.objects.filter(user=request.user, test__in=test)
    total_tests = test.count()
    success_tests = test_result.filter(result=True).count()

    success_percent = (success_tests / total_tests * 100) if total_tests > 0 else 0
    test_result_data = [{"id": test_result.id, "result": test_result.result,"started_at":test_result.started_at,"test_precent":success_percent} for test_result in test_result]

    if not followed_curs.course.is_finished:
        return Response(data={"error": "Course has not finished"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={"course": followed_curs.course.title, "lesson": lesson_data, "test": test_data,
                          "test_result": test_result_data}, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="post",
    tags=["Follow"],
)
@api_view(['POST'])
@permission_classes([IsStudent])
def exam_view(request, test_id):
    test = Test.objects.filter(id=test_id).first()
    if not test:
        return Response(data={"error": "Test ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    result_obj = TestBasicModel.objects.filter(user=request.user, test=test).first()
    if not result_obj:
        return Response(data={"error": "Student started test not yet "}, status=status.HTTP_400_BAD_REQUEST)

    count = TestBasicModel.objects.filter(user=request.user, test=test).count()
    if count >= 1:
        return Response(data={"error": "Student can examine once "}, status=status.HTTP_400_BAD_REQUEST)

    now = timezone.now()
    time_limit = timedelta(minutes=2)
    time = now - result_obj.started_at

    if time > time_limit:
        result_obj.result = False
        result_obj.save()
        return Response(data={"None": "Time is up  test failed. "}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    tags=["Follow"],
    responses={200: TestBasicSerializer(many=True)},
    request_body=TestBasicSerializer,
)
@api_view(['POST'])
def test_basic_view(request):
    serializer = TestBasicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user, started_at=timezone.now())
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseCreate(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacher]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonCreate(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacher]
    parser_classes = [MultiPartParser, FormParser] #


class TestCreate(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsTeacher]
