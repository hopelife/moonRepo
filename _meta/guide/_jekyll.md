# jekyll
[jekyll](https://jekyllrb.com/)

[Static Tools/Jekyll 카테고리](http://namhoon.kim/category/Static%20Tools/Jekyll)



## Quick-start guide
[Quick-start guide](https://jekyllrb.com/docs/quickstart/)


## Installation
[Installation](https://jekyllrb.com/docs/installation/)


## Directory structure
[Directory structure](https://jekyllrb.com/docs/structure/)


## Configuration
[Configuration](https://jekyllrb.com/docs/configuration/)


### jekyll customizing

#### jekyll-theme-basically-basic

```
~/www$ git clone https://github.com/mmistakes/jekyll-theme-basically-basic.git

~/www$ cd jekyll-theme-basically-basic

~/www/jekyll-theme-basically-basic$ cd example

~/www/jekyll-theme-basically-basic/example$

~/www/jekyll-theme-basically-basic/example$ bundle install

~/www/jekyll-theme-basically-basic/example$ bundle exec jekyll serve --detach
```

#### jekyll-material-theme

```
~/www$ git clone https://github.com/jameshamann/jekyll-material-theme.git

~/www$ cd jekyll-material-theme

~/www/jekyll-material-theme$ rvm rvmrc warning ignore allGemfiles

~/www/jekyll-material-theme$ vi Gemfile

------
ruby '2.4.3'  --> ruby '2.4.1'
------


~/www/jekyll-material-theme$ chmod 755 Gem*

~/www/jekyll-material-theme/_sass$ chmod 755 *




~/www/jekyll-material-theme$ bundle install

~/www/jekyll-material-theme$ bundle exec jekyll serve --detach
bundle exec jekyll serve --detach
Configuration file: /home/docMoon/www/jekyll-material-theme/_config.yml
            Source: /home/docMoon/www/jekyll-material-theme
       Destination: /home/docMoon/www/jekyll-material-theme/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
jekyll 3.6.2 | Error:  "\xC2" on US-ASCII




/*
~/www/jekyll-material-theme$ rvm install "ruby-2.4.3"
~/www/jekyll-material-theme$ bundle install
*/

-bash: /mnt/c/tools/ruby25/bin/bundle: C:/tools/ruby25/bin/ruby.exe: bad interpreter: No such file or directory


```


#### jekyll new <site>


```
$ jekyll new site3

Running bundle install in /home/ubuntu/www/site3...
  Bundler: The dependency tzinfo-data (>= 0) will be unused by any of the platforms Bundler is installing for. Bundler is installing for ruby but the dependency is only for x86-mingw32, x86-mswin32, x64-mingw32, java. To add those platforms to the bundle, run `bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java`.
  Bundler: Fetching gem metadata from https://rubygems.org/...........
  Bundler: Fetching gem metadata from https://rubygems.org/.
  Bundler: Resolving dependencies...
  Bundler: Using public_suffix 3.0.2
  Bundler: Using addressable 2.5.2
  Bundler: Using bundler 1.16.1
  Bundler: Using colorator 1.1.0
  Bundler: Using concurrent-ruby 1.0.5
  Bundler: Using eventmachine 1.2.5
  Bundler: Using http_parser.rb 0.6.0
  Bundler: Using em-websocket 0.5.1
  Bundler: Using ffi 1.9.23
  Bundler: Using forwardable-extended 2.6.0
  Bundler: Using i18n 0.9.5
  Bundler: Using rb-fsevent 0.10.3
  Bundler: Using rb-inotify 0.9.10
  Bundler: Using sass-listen 4.0.0
  Bundler: Using sass 3.5.6
  Bundler: Using jekyll-sass-converter 1.5.2
  Bundler: Using ruby_dep 1.5.0
  Bundler: Using listen 3.1.5
  Bundler: Using jekyll-watch 2.0.0
  Bundler: Using kramdown 1.16.2
  Bundler: Using liquid 4.0.0
  Bundler: Using mercenary 0.3.6
  Bundler: Using pathutil 0.16.1
  Bundler: Using rouge 3.1.1
  Bundler: Using safe_yaml 1.0.4
  Bundler: Using jekyll 3.7.3
  Bundler: Using jekyll-feed 0.9.3
  Bundler: Using jekyll-seo-tag 2.4.0
  Bundler: Using minima 2.4.0
  Bundler: Bundle complete! 4 Gemfile dependencies, 29 gems now installed.
  Bundler: Use `bundle info [gemname]` to see where a bundled gem is installed.
New jekyll site installed in /home/ubuntu/www/site3.
```

```
$ ls

404.html  about.md  _config.yml  Gemfile  Gemfile.lock  index.md  _posts  site3
```


```
$ bundle show minima


/home/ubuntu/.rvm/gems/ruby-2.4.1/gems/minima-2.4.0
```


#### _config.yml

```
title: Your awesome title    ->   title: Your awesome title


email: your-email@example.com
description: >- # this means to ignore newlines until "baseurl:"
  Write an awesome description for your new site here. You can edit this
  line in _config.yml. It will appear in your document head meta (for
  Google search results) and in your feed.xml site description.
baseurl: "" # the subpath of your site, e.g. /blog
url: "" # the base hostname & protocol for your site, e.g. http://example.com
twitter_username: jekyllrb
github_username:  jekyll

#### 



#### new-theme
```sh
~/www$ jekyll new-theme site1
             create /home/ubuntu/www/site1/assets
             create /home/ubuntu/www/site1/_layouts
             create /home/ubuntu/www/site1/_includes
             create /home/ubuntu/www/site1/_sass
             create /home/ubuntu/www/site1/_layouts/page.html
             create /home/ubuntu/www/site1/_layouts/post.html
             create /home/ubuntu/www/site1/_layouts/default.html
             create /home/ubuntu/www/site1/Gemfile
             create /home/ubuntu/www/site1/site1.gemspec
             create /home/ubuntu/www/site1/README.md
             create /home/ubuntu/www/site1/LICENSE.txt
         initialize /home/ubuntu/www/site1/.git
             create /home/ubuntu/www/site1/.gitignore
```

- edit Gemfile

```ruby
gem "site1"
```


============================================

## 기본 사용법
[기본 사용법](http://jekyllrb-ko.github.io/docs/usage/)






## directories


## _config.yml


## _layouts

## _



## liquid