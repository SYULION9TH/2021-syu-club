동아리 박람회를 대체하기 위해 동아리 연합회를 진행할 예정입니다.  

- 백엔드 : 박미란, 박현서, 이지수, 최정은, 함승우, 황한슬
- 프론트엔드 : 김지연, 박세연, 이민주, 이보람, 주미진 (보조: 박미란, 성예지)
- 다자인 : 윤예빈 (보조: 성예지)

# 세팅 방법
git clone을 합니다. 
```bash
git clone https://github.com/SYULION9TH/2021-syu-club.git
```
## github branch 설계 규칙
### Branch 확인 하기
### backend와 frontend로 banch를 나눠놨으니 본인이 해당하는 브랜치에 들어가 본인의 브랜치 생성하기 

1. 현재 내가 위치한 Branch 확인
   - `$git branch`
2. 원격 저장소의 브랜치 확인
   - `$git branch -r`
3. 브랜치의 마지막 커밋 메세지 확인
   - `$git branch -v`

### Branch 생성 및 이동
1. Branch 생성하기
    - git branch 브랜치명
        - `$git branch test`
2. 생성한 Branch로 이동하기
    - git checkout 브랜치명
        - `$git checkout test`

### Branch 삭제
git branch -d 브랜치명  
`$git branch -d test`

### branch 병합 Git Merge
`$git merge 브랜치명`

### master branch로 이동
`$git checkout master`

# 개발 시작합시다.  

`2021-syu-club/onlineclub`폴더가 있는 위치에서 가상환경(`$source myvenv/bin/activate`)을 실행해 줍니다.  
가상환경 실행 후 `requirements.txt`가 있는 위치에서 `$pip install -r requirements.txt`명령어를 입력합니다.  
`$python manage.py runserver` 이후 `127.0.0.1:8000/admin`으로 들어가서 제대로 되는지 확인합니다.

```text
※python manage.py migrate는 하지마세요※  
id : dev  
password : 1234  
```  

## 동아리 앱 폴더:
- 동아리 - 황한슬, 박미란  
    -  박미란 : 모집요강, 활동사진 수정
    -  황한슬 : 동아리 목록 정렬(디데이를 기준으로)
    -  박현서 : 동아리 검색, 사이드바 분과별로 정렬
        - models = ClubTypes, Clubs
- 게시물 - 최정은
    - 게시글 생성, 수정, 삭제
    - models = Posts
- account -함승우
    - 관리자 로그인
    - models - AuthUser

## URL 설계
1. 자원의 컬렉션 이름으로는 복수형을 쓴다. ex) `/Post/1 -> /posts/1`
2. http의 Method가 들어가서는 안된다.
3. 동사표현을 쓰면 안된다. ex) `/posts/show/1 -> GET /posts/1`
4. 경로 중 변하는 값은 유일한 값으로 바꾼다. ex) id가 12인 게시물을 지우는 행위 `DELETE /posts/12`
5. '/'는 계층관계를 나타내는데 사용한다.
6. URI 마지막 문자로 슬래시(/ )를 포함하지 않는다.
7. 대문자는 쓰지 않고 소문자만 쓴다.
8. 하이픈(- )은 URI 가독성을 높이는데 사용 불가피하게 긴 URI경로를 사용하게 된다면 하이픈을 사용해 가독성을 높인다.
9. 밑줄(\_ )은 URI에 사용하지 않는다. 밑줄은 보기 어렵거나 밑줄 때문에 문자가 가려지기도 하므로 가독성을 위해 밑줄은 사용하지 않는다.
10. 리소스 간에 연관 관계가 있는 경우 ex) 리소스명/{리소스ID}/관계가 있는 다른 리소스 명 --> `posts/1/comments`

QnA 예시)

|설명|Method|경로|
|----|-------|----|
|한 동아리의 QnA목록을 나타낸다.|GET|/clubs/:id/qna|
|한 동아리의 QnA상세를 나타낸다.|GET|/clubs/:id/qna/:id|
|한 동아리의 QnA를 수정한다.|PUT|/clubs/:id/qna/:id|
|한 동아리의 QnA를 삭제한다.|DELETE|/clubs/:id/qna/:id|
