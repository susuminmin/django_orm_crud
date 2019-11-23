from django.db import models

# 순차적으로 3단계!! 잔고의 db에 적용하는 방법은?
# 0. model 을 작성한다.
# 1. python manage.py makemigrations => django 에게 model 작성했음을 알림
# 2. python manage.py migrate => django 에게 실제 DB에 작성하라고 명령


class Article(models.Model):
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)

    # 모든 필드는 기본적으로 NOT NULL => 비어있으면 안 된다.

    # CharField 에서는 max_length가 필수 인자다.
    # 클래스 변수 (DB의 필드), max_length 인자 필수
    title = models.CharField(max_length=20)
    content = models.TextField()  # 클래스 변수 (DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True)  # 자동으로 지금 추가됐을 때
    updated_at = models.DateTimeField(auto_now=True)  # 언제든지

    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'


class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id}번 글 - {self.name} {self.email} {self.birthday} {self.age}'
