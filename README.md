## 실행순서
1. /webapp 으로 이동

2. 라이브러리 설치
   ``` 
   pip install -r requirements.txt
   ``` 

3. 마이그레이션 파일 생성
   ```
   python manage.py makemigrations
   ```

4. 마이그레이션 파일 적용
   ```
   python manage.py migrate
   ```

5. 슈퍼유저 생성
   ```
   python manage.py createsuperuser
   ```

6. 슈퍼유저 아이디, 비밀번호 입력
   ```
   a@a.com
   123
   y
   ```

7. 개발 서버 실행
   ```
   python manage.py runserver
   ```

8. api 명세서 확인 및 테스트
  
