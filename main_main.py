print('hello')

'''
Github 처음 코드 업로드 하기

>> 터미널 >> bash 선택

1. 초기화
git init

2. 추가할 파일 더하기 (파일종류 선택)
.(점) 은 모든 파일이라는 뜻, 선택적으로 올리고 싶으면
add뒤에 파일 이름 붙여주면 됨 (예. git add index.html)

git add .

3. 상태확인

git status

4. 히스토리작성 (작업물 인덱싱.1,2,3~ 최종, 최종의 최종...)

git commit -m "first commit"

5. Github repository 와 로컬 연결

git remote add origin 깃허브링크

6 연결확인

git remote -v

7. Github로 올리기

git push origin master




Github 업데이트 하는법
1. 추가할 파일더하기
git add .

2. 히스토리 만들기
git commit -m "first commit"

3. Github로 올리기
git push origin main




Github 팀프로젝트
1. github에서 소스코드 다운로드
git clone 주소 폴더이름

2. Github에서 내 branch 만들기
git checkout -b 브랜치이름

3. 내 브랜치에 소스코드 업데이트
git add .
git commit -m "first commit"
git push origin 브랜치이름

4. 마스터 브랜치에 소스 가져오기(pull)
git pull origin master
(pull을 하기전에는 기존에 소스코드들을 commit을 먼저 해놔야 한다)


'''