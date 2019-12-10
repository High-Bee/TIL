### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   ```

   

2. 작업 완료 후 commit

   ```bash
   $ touch test.txt
   $ git add .
   $ git commit -m "test 기능 개발 완료"
   ```


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   ```bash
   $ git log --oneline
   6f90f72 (HEAD -> master, testbranch) testbranch work
   b9b5b36 (origin/master) push pull 연습
   35ccad1 집 - html 만들기
   0121f01 멀캠 index 파일 생성
   ```


4. master에 병합

   ```bash
   $ git merge feature/test
   Updating 6f90f72..97ab2bc
   Fast-forward 
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   ```
   
   


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   97ab2bc (HEAD -> master, feature/test) test 기능개발 완료
   6f90f72 (testbranch) testbranch work
   b9b5b36 (origin/master) push pull 연습
   35ccad1 집 - html 만들기
   0121f01 멀캠 index 파일 생성
   
   ```

   

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   ```
   
   

---

### 상황 2. merge commit

> feature branch에서 작업하고 있는 동안
>
> master branch에서 이력이 

1. feature/signout branch 생성 및 이동

   ```bash
   $ git checkout -b feature/signout
   ```

   

2. 작업 완료 후 commit

   ```bash
   $ touch signout.txt
   $ git add .
   $ git commit -m "complete signout"
   ```

   

3. master 이동

   ```bash
   $ git checkout master
   ```

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   ```bash
   $ touch master.txt
   $ git add .
   $ git commit -m 'Update master'
   ```

   ```bash
   $ git log --oneline
   ee70154 (HEAD -> master) Update master
   de7c1cf test 기능 개발 완료
   f653956 Testbranch -test
   97871d5 (origin/master) 집 - main.html
   c1e3b55 멀캠 - index.html
   ```

   

5. master에 병합

```bash
$ git merge feature/signout 	# master  
Merge made by the 'recursive' strategy.
signout.txt | 0
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 signout.txt

```



1. 결과 -> 자동으로 *merge commit 발생*

   ```bash
   $ git log --oneline
   78134d3 (HEAD -> master) Merge branch 'feature/signout'
   323cca7 update master
   26b048c (feature/signout) complete signout
   97ab2bc test 기능개발 완료
   6f90f72 testbranch work
   b9b5b36 (origin/master) push pull 연습
   35ccad1 집 - html 만들기
   0121f01 멀캠 index 파일 생성
   ```

   

2. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   78134d3 (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * 26b048c (feature/signout) complete signout
   * | 323cca7 update master
   |/
   * 97ab2bc test 기능개발 완료
   * 6f90f72 testbranch work
   * b9b5b36 (origin/master) push pull 연습
   * 35ccad1 집 - html 만들기
   * 0121f01 멀캠 index 파일 생성
   
   ```

   

3. branch 삭제

   ```bash
   $ git branch -d feature/signout
   ```

   

---

### 상황 3. merge commit 충돌

1. feature/board branch 생성 및 이동

   ```bash
   $ git checkout -b  hotfix/test
   ```

   

2. 작업 완료 후 commit

   ```bash
   
   $ git log --oneline
   3a04b3c (HEAD -> hotfix/test) hotfix test
   78134d3 (master) Merge branch 'feature/signout'
   323cca7 update master
   26b048c (feature/signout) complete signout
   97ab2bc test 기능개발 완료
   6f90f72 testbranch work
   b9b5b36 (origin/master) push pull 연습
   35ccad1 집 - html 만들기
   0121f01 멀캠 index 파일 생성
   ```


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # test.txt 수정
   $ git add .
   $ git commit -m 'master test'
   ```

   

5. master에 병합

   ```bash
   $ git merge hotfix/test
   Auto-merging test.txt
   CONFLICT (content): Merge conflict in test.txt
   Automatic merge failed; fix conflicts and then commit the result.
   
   ```
   
   


6. 결과 -> *merge conflict발생*

   


7. 충돌 확인 및 해결

   ```bash
   <<<<<<< HEAD
   마스터 test 긴급수정!
   
   수정 완료!
   =======
   hotfix 브랜치에서 수정
   우아아아아아앙아아한 형제들
   >>>>>>> hotfix/test
   
   ```
   
   
   
   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 6 commits.
     (use "git push" to publish your local commits)
   
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   test.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```
   
   


8. merge commit 진행

    ```bash
    $ git add .
    $ git commit
[master acbc693] Merge branch 'hotfix/test'
   ```
   
   * vim 편집기 화면이 나타납니다.
   
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.
   
9. 그래프 확인하기

    ```bash
   $ git log --oneline --graph
   *   acbc693 (HEAD -> master) Merge branch 'hotfix/test'
   |\
   | * 3a04b3c hotfix test
   * | 3028862 master test
   |/
   *   78134d3 Merge branch 'feature/signout'
   |\
   | * 26b048c (feature/signout) complete signout
   * | 323cca7 update master
   |/
   * 97ab2bc test 기능개발 완료
   * 6f90f72 testbranch work
   * b9b5b36 (origin/master) push pull 연습
   * 35ccad1 집 - html 만들기
   * 0121f01 멀캠 index 파일 생성
    ```
   
   


10. branch 삭제

    ```bash
    $ git branch -d hotfix/test
    ```
    
    