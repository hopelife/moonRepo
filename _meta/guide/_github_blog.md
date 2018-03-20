
## github blog 만들기
### ref
- ![깃허브 블로그 만들기](http://recoveryman.tistory.com/321)
- ![GitHub 블로그 빠르게 시작하기!](http://thdev.net/653)
- ![jekyll 블로그](https://jekyllrb-ko.github.io/)
- ![git 다운로드](https://git-scm.com/)

### github 계정 만들기
- ![github](https://github.com/)

- userName : hopelife
- password : deverlife@gmail.com

hopelife -> __hopelife
deverlife@gmail.com -> __deverlife@gmail.com

### install git
https://git-scm.com/

#### user 설정
- Git Bash 실행

```bash
git config --global user.name "__hopelife"
git config --global user.email "__deverlife@gmail.com"
```

https://github.com/__hopelife

### install jekyll theme to my github blog[https://hopelife.github.io/]
![jekyll theme](http://jekyllthemes.org/)


#### 테마 선택

#### fork 테마

#### repository name 변경
- 'Settings' 클릭
- 'Repository name'란에 '__hopelife.github.io' 입력
- 'Rename' 클릭

### clone remote blog to local repository

https://rogerdudler.github.io/git-guide/index.ko.html

#### make local repository
- D:\dev\web\project\github\blog
- 'shift + click'


#### clone

```
D:\dev\web\project\github\blog> git clone https://github.com/hopelife/hopelife.github.io
```

### git push(파일 변경 / 포스팅)

#### 설정 file 변경/삭제

##### _config.yml
```
# Site settings
title: 'hopelife'
description: 'IT & Korean medicine'
keyword: 'nodejs, web crawling, korean medicine'
url: 'https://hopelife.github.io/' # your host

# if you don't need baseurl, you should leave this value blank.
baseurl: ''

# Navigation links
nav:
  home: '/'
  tags: '/tags.html'

# Footer
footer:
  since: 2017

# Author
author: '문정삼'
nickname: 'monwater'
bio: '전직 프로그래머, 현직 한의사'
avatar: '/assets/img/profile.png'

# Search
search: true

# Night mode
nightMode: true

# Comments 
#   default_hidden： by Ray-Eldath
comments:
  default_hidden: false
  disqus: true
  disqus_url: 'https://hopelife.github.io/'

#  livere: true
#  livere_uid: MTAyMC8yODEwMC80Njcz

# Reward by Ray-Eldath
#reward:
#  enable: true
#  reward_comment: ''
#  wechatpay: 'http://ray-eldath.image.alimmdn.com/basic/wechatpay.jpg'
#  alipay: 'http://ray-eldath.image.alimmdn.com/basic/alipay.jpg'

# b2t by Ray-Eldath
#b2t: true

# MathJax by Ray-Eldath
#mathjax: true

# Share
social-share: true
social-share-items: ['twitter']

# theme color
theme-color: 'default'  # pink or default

# Post header background patterns (when the post no cover): circuitBoard, overlappingCircles, food, glamorous, ticTacToe, seaOfClouds
postPatterns: 'circuitBoard'

# SNS settings url: email, weibo, zhihu, twitter, instagram, juejin, github, douban, facebook, dribble, uicn, jianshu, medium, linkedin
sns:
  email: 'mailto:hopelife@gmail.com'
  facebook: 'monwater@gmail.com'
  twitter: 'monwater@gmail.com'
  github: '//github.com/hopelife'

# Tags
recommend-tags: true # whether or not display recommend-tags on the sidebar
recommend-condition-size: 12 # a tag will be recommended if the size of it is more than this value

# Build settings
paginate: 6
paginate_path: 'page:num'
exclude: ['node_modules', 'dev', 'package.json', 'gulpfile.js', '.gitignore', 'README.md']

# Markdown
markdown: kramdown
highlighter: rouge
kramdown:
  input: GFM

# RSS
RSS: false

# Permalink
# See: https://github.com/kaeyleo/jekyll-theme-H2O/issues/35
permalink: /:year/:month/:day/:title.html

# Plugins
plugins: [jekyll-paginate]
```

##### 댓글(disqus) 기능 추가
![Github Blog에 댓글(disqus) 기능 추가하기](https://devminjun.github.io/blog/addComments)
![disqus](https://disqus.com/)

- disqus 계정 만들기
- Settings
- 설정 > Add Disqus To Site > I want to install Disqus on my site



#### posting 파일 삭제 / 추가 / 편집


#### 