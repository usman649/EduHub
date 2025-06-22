# 🎓 EduHub

**EduHub** — bu onlayn ta'lim platformasi bo‘lib, o‘qituvchilar kurs yaratadi, talabalar esa kurslarga yozilib darslarni o‘rganadilar va testlar orqali bilimlarini tekshiradilar.

---

## 🚀 Asosiy imkoniyatlar

- 👨‍🏫 O‘qituvchilar kurs yaratadi, video darslar, fayllar va testlar qo‘shadi
- 👨‍🎓 Talabalar kursga obuna bo‘lishadi va o‘zlariga tegishli darslarni ko‘rishadi
- 🎥 Har bir darsda video, fayl va CKEditor bilan matnli kontent bo‘ladi
- 📝 Har bir dars uchun test mavjud bo‘ladi (vaqti o‘qituvchi tomonidan belgilanadi)
- ✅ Talaba testni **faqat bir marta** topshira oladi
- ⏳ Agar testga ajratilgan vaqt (masalan 2 daqiqa) tugasa, test avtomatik **noto‘g‘ri** deb baholanadi
- 📊 Kurs tugaganidan so‘ng, foydalanuvchining testdagi **umumiy foizli natijasi** hisoblanadi

---

## 🔐 Rollar va ruxsatlar

- `role = 1` — Teacher
- `role = 2` — Student

### 🎯 Custom Permissions:
- `IsTeacher`: faqat teacher o‘ziga obuna bo‘lgan studentlar natijalarini ko‘ra oladi
- `IsStudent`: student faqat o‘zi obuna bo‘lgan kurslar, darslar va testlarni ko‘ra oladi

---

## 🧩 Arxitektura

### 📚 Model struktura (qisqacha)
- `Course` — kurs (yaratuvchi, nomi, holati)
- `Lesson` — kursga tegishli dars (video, matn, fayl)
- `Test` — darsga bog‘langan testlar (vaqt bilan cheklangan)
- `Follow` — talabalar kursga obuna bo‘lishi
- `TestBasicModel` — foydalanuvchi test natijasi

### 🔁 Nested serializers
- Kurs → Darslar → Testlar — barcha bog‘liq ma’lumotlar **nested** ko‘rinishda yuboriladi (DRF serializers orqali)

---

## 📁 Media qo‘llab-quvvatlash

- Video fayllar: `FileField` orqali yuklanadi (`upload_to="course/video"`)
- CKEditor 5 yordamida matnli darslar (RichTextField)
- Testlar, darslar, kurslar bilan bog‘langan fayllar to‘liq qo‘llab-quvvatlanadi

---

## ⏱ Throttling va test cheklovlari

- Har bir test uchun `start_date` va `end_date` belgilanishi mumkin
- Test topshirish vaqti **o‘qituvchi tomonidan belgilangan** bo‘ladi (masalan, 2 daqiqa)
- Agar test belgilangan vaqtdan ko‘proq vaqt olsa, **noto‘g‘ri (`result=False`)** deb baholanadi
- Talaba **har bir testni faqat bir marta** topshira oladi

---

## 📊 Statistik hisoblash

- Kurs **yakunlangandan** so‘ng `is_finished=True` bo‘lsa:
  - Talabaning barcha test natijalari olinadi
  - `result=True` bo‘lgan testlar foizga hisoblanadi:
    ```
    foiz = (to‘g‘ri testlar soni / jami testlar soni) * 100
    ```
- Bu statistikani API orqali olish mumkin (`/course/<id>/statistic/`)

---

## 🛠 Texnologiyalar

- **Backend:** Django, Django REST Framework
- **Ma'lumotlar bazasi:** PostgreSQL
- **Media:** CKEditor 5, video/fayl yuklash
- **Avtorizatsiya:** Session yoki JWT (tanlangan usulga qarab)
- **Permissions:** Custom `IsTeacher`, `IsStudent`
- **Test throttling:** vaqt va bir martalik cheklov

---

## ▶️ Ishga tushirish

```bash
# Virtual muhit yaratish
python -m venv venv
source venv/bin/activate

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# Migratsiyalar
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Serverni ishga tushirish
python manage.py runserver
