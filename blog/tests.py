from django.test import TestCase

""""

O‘qituvchilar kurs yaratadi, talabalar kursga obuna bo‘ladi. Har bir kursda videolar, testlar, fayllar.
- Nested serializers (kurs → darslar → testlar)
- Custom permissions (`IsTeacher`, `IsStudent`) teachr la oziga obuna bolgan student va natijalani  : studentla ozi obuna bolgan  video darsla va kursla
- Media uploads (video va fayllar)
- Throttling (test topshirishni cheklash) testlarni vaqti bu vaqti teacher belgilid 2 minut dan oshsa test natijasi notogri bolsin va boshqa testga kirmasin
student faqat bir marta test topshirad

userni  umumiy statistika kursni tugatgandan keyin 
dars tugagandan keyin test ishlaand

























- Custom permissions (`IsTeacher`, `IsStudent`) teachr la oziga obuna bolgan student va natijalani  : studentla ozi obuna bolgan  video darsla va kursla:1ta kursda kop darsla
- Media uploads (video va fayllar)
- Throttling (test topshirishni cheklash) testlarni vaqti bu vaqti teacher belgilid 2 minut dan oshsa test natijasi notogri bolsin va boshqa testga kirmasin


umumiy statistika kursni tugatgandan keyin
student faqat bir marta test topshirad
dars tugagandan keyin test ishlaand










- Custom permissions (`IsTeacher`, `IsStudent`)
- Media uploads (video va fayllar)
- Throttling (test topshirishni cheklash)





"""
