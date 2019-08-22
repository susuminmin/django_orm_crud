# Django ORM

## Create

### 기초설정

* Shell

```bash
$ python manage.py shell
```



* import model

```python
from articles.models import Article
```



* 

```python
>>> Article.objects.all()
<QuerySet []>
```

objects는 db 접근해서 명령 내리게하는 객체 





---

#### 데이터를 저장하는 3가지 방법

1. **첫번째 방법**

   * ORM 을 쓰는 이유는? => DB 를 조작하는 것을 객체지향 프로그래밍 (클래스) 처럼 하기 위해서

   ```python
   >>> article = Article()
   >>> article
   <Article: Article object (None)>
   >>> article.title = 'First article'
   >>> article.content = 'Hello article??'
   >>> article.save()
   >>> article
   <Article: Article object (1)>
   ```

   ```
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>]>
   ```

   

2. **두번째 방법**

   * 함수에서 keyword 인자 넘기기 방식과 동일

   ```python
   >>> article = Article(title='Second article', content='HiHi')
   >>> article.save()
   >>> article
   <Article: Article object (2)>
   ```

   

3. **세번째 방법**

   * create 를 사용하면 쿼리 셋 객체를 생성하고 저장하는 로직이 한번의 스텝 

   ```python
   >>> Article.objects.create(title='Third article', content='Django! Good')
   <Article: Article object (3)>
   ```

   

*c.f. 모든 objects 확인하기*

```bash
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```







---

#### 검증

full_clean()` 함수

```bash
>>> article.title = 'Python is good'
>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\development\django\django_rom_crud\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
```





---

## READ

### 모든 객체

```bash
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
```



##### 객체 표현 변경

* 함수 정의

```python
# articles./models.py
class Article(models.Model):
    ...
    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'
```



* `exit()` 으로 나갔다가 다시 들어오기

```bash
$ python manage.py shell
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from articles.models import Article
>>> Article.objects.all()
<QuerySet [<Article: 1번 글 - First article : Hello article??>, <Article: 2번 글 - Second article : HiHi>, <Article: 3번 글 - Third article : Django! Good>, <Article: 4번
 글 - title : >]>
```



##### DB에 저장된 글 중에서 title이 'Second article' 인 글만 가지고 오기 (filter)

```python
>>> Article.objects.filter(title='Second article')
<QuerySet [<Article: 2번 글 - Second article : HiHi>]>
```



* 복수인 경우에 

```python
>>> Article.objects.create(title='Second article', content='content')
<Article: 5번 글 - Second article : content>
>>> Article.objects.filter(title='Second article')
<QuerySet [<Article: 2번 글 - Second article : HiHi>, <Article: 5번 글 - Second article : content>]>
```



```bash
>>> querySet = Article.objects.filter(title='Second title')
>>> querySet.first()
```



````
filter.first() 도 가능
````

 

##### DB에 저장된 글 중에서 pk 가 1인 글만 가지고 오기

* PK만 `get()`으로 가지고 올 수 있다. 

```bash
>>> Article.objects.get(pk=1)
<Article: 1번 글 - First article: Hello article??>
```



* pk 없으면 오류

```
article.models.Article.DoesNotExist: Article matching query does not exist.
```



* filter는 가능

```bash
>>> Article.objects.filter(pk=10)
<QuerySet []>
```



* 오름차순

````bash
>>> articles = Article.objects.order_by('pk')
````



* 내림차순 

```bash
>>> articles = Article.objects.order_by('-pk')
```



* index 접근 가능

```
>>> article = articles[2]
```



##### Like - 문자열을 포함하고 있는 값을 가지고 옴

장고 ORM 은 이름(title) 과 필터(contains) 를 더블 언더스코어로 구분한다. 



##### startswith/endswith

```bash
>>> articles = Article.objects.filter(content__endswith='Good')
>>> articles
<QuerySet [<Article: 3번 글 - Third article: Django! Good>]>
```



---

### Delete

article 인스턴스 호출 후 `.delete()` 함수를 실행한다. 

```bash
>>> article = Article.objects.get(pk=7)
>>> article.delete()
(1, {'articles.Article': 1})
```



### Update

article 인스턴스 호출 후 값 변경하여 `.save()` 함수를 실행한다. 

```bash
>>> article = Article.objects.get(pk=4)
>>> article.content = 'new contents'
>>> article.save()
```



---

