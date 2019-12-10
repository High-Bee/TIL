# Git 기초

> Git은 분산형버전관리시스템(DVCS)이다.
>
> 소스코드의 이력을 확인하고, 협업단계에서 활용 가능하다.

## 0. 기본설정

윈도우에서 git을 활용하기 위해서는 `git bash`가 필요하다. [설치링크](https://gitforwindows.org/)

설치 이후에 `commit`을 작성하는 `author`설정이 필요하다.

```bash
$ git config --global user.name High-Bee
$ git config --global user.email ko.yb112@gmail.com
```

설정내용을 확인하기 위해서는 아래의 명령어를 입력한다

```bash
$ git config --global -l
user.name=High-Bee
user.email=ko.yb112@gmail.com

```

## gitignore

프로젝트를 진행할 때,  `git` 으로 관리하지 않을 파일 혹은 폴더들을 설정할 수 있다.

> `*.xlsx` 				# 확장자가 xlsx인 파일
>
> `a.txt` 				  # a.txt 파일
>
> `.ipynb_checkpoints/` #`.ipynynb_checkpoints`폴더



## 로컬저장소 활용하기

### 1. Git 저장소 설정

특정 프로젝트 폴더에서 `git`을 활용하기 위해서는 아래의 명령어를 입력한다.

```bash
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/pract/.git/

```

* 해당 디렉토리내에 `.git`이라는 숨김 폴도가 생성되며, 

  모든 `git`과 관련된 동작은 해당 폴더에 기록된다.

* `git basg`에서 `(master)`라는 브랜치 정보가 표기된다.

### 2. add

`git`에서 커밋할 대상 파일을 `staging area`로 이동시키는 명령어 이다.

```bash
$ git add a.txt # 특정 파일을 stage
$ git add images/ # 특정 폴더를 stage
$ git add . # 모든 디렉도리 파일 및 폴더를 stage
```

* `add` 전 상태

  ```bash
  $ git status
  On branch master
  
  No commits yet
  
  Untracked files: # git 이력에 담기지 않은 파일 생성
    (use "git add <file>..." to include in what will be committed)
    # git add 명령어를 통해서 commit될 곳에 추가
          a.txt
          b.txt
  
  nothing added to commit but untracked files present (use "git add" to track)
  ```

* `add` 후 상태

  ```bash
  $ git status
  On branch master
  
  No commits yet
  
  Changes to be committed: # commit 될 변경 사항
    (use "git rm --cached <file>..." to unstage)
          new file:   a.txt # a.txt 새로운 파일 생성
  
  Untracked files: # 트래킹 되고 있지 않은 파일들
    (use "git add <file>..." to include in what will be committed)
          b.txt
  ```

**항상 `git status` 명령어를 통해 현재 상태를 확인하는 것이 중요하다!!**

### 3. commit

`git` 에서 이력을 남기기 위해서는 항상 `commit` 을 통해서 진행한다.

`commit` 을 남길 때에는 항상 `commit` 메세지를 작성한다.

메세지는 해당 이력에 대한 정보를 담는다.

```bash
$ git commit -m "Add File"
[master (root-commit) 17fdf48] Add File
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
 create mode 100644 b.txt

```

`commit` 이력을 확인하기 위해서는 아래의 명령어를 활용한다.

```bash
$ git log
commit 17fdf48f985a25fde3e98778d88e82c056eb74ad (HEAD -> master)
Author: High-Bee <ko.yb112@gmail.com>
Date:   Mon Dec 9 14:25:57 2019 +0900

    Add File
    
$ git status
On branch master
nothing to commit, working tree clean # 모든 이력을 저장했기 때문에 clean
```

이후 변경 사항이 발생하게 된다면, `add` ->  `commit` 을 한다.

`add` :  `commit` 할 대상 파일 선정

`commit` : 이력의 확정

## 원격 저장소(remote repository) 활용하기

> 원격 저장소를 제공해주는 서비스는 다양하다.
>
> 우리는 github을 기준으로 활용 해보자.

### 0. 기본 설정

Github에 비어있는 저장소 생성

### 1. 원격 저장소 설정

```bash
$ git remote add origin https://~
```

원격 저장소`(remote)`를 `origin` 이라는 이름으로 `https://~` 로 설정한다.

아래의 명령어를 통해 저장된 원격 저장소 목록을 확인할 수 있다.

```bash
$ git remote -v
origin  https://github.com/High-Bee/gittest.git (fetch)
origin  https://github.com/High-Bee/gittest.git (push)
```

혹시 잘못 설정되었다면 아래의 명령어를 통해 삭제가 가능하다.

```bash
$ git remote rm origin
$ git remote -v
```

## 2. push

원격 저장소에 업로드 하기 위해서는 `push` 명령어가 필요하다.

```bash
$ git push -u origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 212 bytes | 212.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/High-Bee/gittest.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

`origin` 으로 설정된 원격 저장소에 `push` 한다.

이후에 변경된 사항(`commit`)이 발생하였을 때, `git push origin master`명령어를 통해서 매번 업로드 해줄 수 있다.









