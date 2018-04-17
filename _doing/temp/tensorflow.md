## tensorflow 설치

### osx
[맥 OS X에 텐서플로우(tensorflow) 설치하는 방법 - CPU, virtualenv(가상환경), Python 3.n 버전](http://rfriend.tistory.com/325)

[맥 OSX에 텐서플로우(TensorFlow) 설치하기](https://meisteruser.net/devflow/1863)

[Installing TensorFlow on macOS](https://www.tensorflow.org/install/install_mac)

- virtualenv(가상환경)
- Native pip
- [Docker](https://www.docker.com/)
- [installing from sources](https://www.tensorflow.org/install/install_sources)

#### CPU 지원 환경, virtualenv, Python 3.n

```shell

$ sudo easy_install pip

$ sudo pip install --upgrade virtualenv


$ cd ~/Apps
$ mkdir ML
$ cd ML
$ mkdir tensorflow


$ virtualenv --system-site-packages ~/Apps/ML/tensorflow
_$ virtualenv --system-site-packages <디렉토리명>


$ source ~/Apps/ML/tensorflow/bin/activate # bash, sh, ksh 혹은 zsh 를 사용하는 경우
_$ source ~/tensorflow/bin/activate.csh # csh 혹은 tcsh를 사용하는 경우

_$ pip install --upgrade TF_BINARY_URL # Python 2.7
_$ pip3 install --upgrade TF_BINARY_URL # Python 3.N
$ pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.6.0-py3-none-any.whl

_$ pip install --upgrade tensorflow # for Python 2.7
$ pip3 install --upgrade tensorflow # for Python 3.n
_$ pip install --upgrade tensorflow-gpu # for Python 2.7 & GPU
_$ pip3 install --upgrade tensorflow-gpu # for Python 3.n & GPU
```


#### zsh 환경 설정
[python -- Mac 에서 pyenv, virtualenv 설치하기](http://freeprog.tistory.com/281)

```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc


// 저장한 zsh 환경을 적용하기
$ source .zshrc

// shell 다시 실행하기
$ exec $SHELL
```




#### Jupyter Notebook

```
$ pip3 install jupyter

$ jupyter notebook

```


$ pip3 show jupyter

Name: jupyter
Version: 1.0.0
Summary: Jupyter metapackage. Install all the Jupyter components in one go.
Home-page: http://jupyter.org
Author: Jupyter Development Team
Author-email: jupyter@googlegroups.org
License: BSD
Location: /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages
Requires: qtconsole, ipykernel, notebook, jupyter-console, ipywidgets, nbconvert


* 가상환경에 Python, tensorflow를 설치했으므로 Anaconda 에서 Jupyter notebook 실행시켜서 사용하면 안됩니다. 가상환경에 jupyter notebook 설치하고 가상환경에서 jupyter notebook 실행해서 tensorflow importing 해야 제대로 인식을 합니다.


localhost:8888 로 Jupyter Notebook 열고 나서 => import tensorflow as tf로 텐서플로우를 불어와서 사용하면 됩니다.


### tensorflow 비활성화/삭제

```
//tensorflow 비활성화
$ deactivate

//tensorflow 삭제
$rm -r ~/tensorflow

```


### pycharm

[PyCharm에서 TensorFlow를 위한 새 프로젝트 생성](http://agiantmind.tistory.com/178)
