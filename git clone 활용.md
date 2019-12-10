# git `clone` 활용

## 처음 `clone` 만들기

```bash
student@M160414 MINGW64 ~/Desktop/집
$ git clone https://github.com/High-Bee/multicamp-home.git
Cloning into 'multicamp-home'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.

student@M160414 MINGW64 ~/Desktop/집
$ cd multicamp-home/

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ git log
commit 0121f019021b655712a44fcac65ac2e2fa01a7d8 (HEAD -> master, origin/master, origin/HEAD)
Author: High-Bee <ko.yb112@gmail.com>
Date:   Tue Dec 10 11:14:59 2019 +0900

    멀캠 index 파일 생성

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ git remote -v
origin  https://github.com/High-Bee/multicamp-home.git (fetch)
origin  https://github.com/High-Bee/multicamp-home.git (push)

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ touch main.html

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ git add .

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ git commit -m "집 - html 만들기"
[master 35ccad1] 집 - html 만들기
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 main.html

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ git log
commit 35ccad123ad01495855a28f4a063c380036e94b4 (HEAD -> master)
Author: High-Bee <ko.yb112@gmail.com>
Date:   Tue Dec 10 11:21:34 2019 +0900

    집 - html 만들기

commit 0121f019021b655712a44fcac65ac2e2fa01a7d8 (origin/master, origin/HEAD)
Author: High-Bee <ko.yb112@gmail.com>
Date:   Tue Dec 10 11:14:59 2019 +0900

    멀캠 index 파일 생성

student@M160414 MINGW64 ~/Desktop/집/multicamp-home (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 265 bytes | 265.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0)
To https://github.com/High-Bee/multicamp-home.git
   0121f01..35ccad1  master -> master

```





## 집에서 한것 당겨오기

```bash

student@M160414 MINGW64 ~/Desktop/멀캠/web (master)
$ git pull origin master
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 2 (delta 0), reused 2 (delta 0), pack-reused 0
Unpacking objects: 100% (2/2), done.
From https://github.com/High-Bee/multicamp-home
 * branch            master     -> FETCH_HEAD
   0121f01..35ccad1  master     -> origin/master
Updating 0121f01..35ccad1
Fast-forward
 main.html | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 main.html


```

