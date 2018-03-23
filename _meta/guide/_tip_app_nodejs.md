## String

### replace()
[String.prototype.replace() 한글](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

[String.prototype.replace() 영어](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

### 문법(Syntax)
```
str.replace(regexp|substr, newSubStr|function)
```

#### 인자(Parameters)
- regexp (pattern)
정규식(RegExp) 객체 또는 리터럴. 이 정규식에 매칭되는 부분들은 두번째 파라미터의 반환값으로 교체되어 집니다.
- substr (pattern)
새로운 문자열에 의해서 교체당할 문자열(String).  정규식이 아닌 글자 그대로의 문자열로 처리된다. 오직 첫 번째 일치되는 문자열만이 교체된다.
- newSubStr (replacement)
첫번째 파라미터를 대신할 문자열(String). 여러가지 대체 패턴들이 지원됩니다. 아래의 "매개변수가 string으로 지정되었을 때" 섹션을 참고하세요.
- function (replacement)
첫번째 파라미터를 대신할 새로운 문자열을 생성하기 위해 호출될 function. 이 function에 제공되는 인자들은 아래  "매개변수가 function으로 지정되었을 때" 섹션에 기술되어 있습니다.

#### 반환값(Return value)
어떤 패턴에 일치하는 일부 또는 모든 부분이 교체된 새로운 문자열

### 설명(Description)
이 메서드는 호출된 String 객체를 바꾸지 않습니다. 단순히 새로운 문자열을 리턴합니다.

모든 문자열에 대해 검색하고 바꾸려면 정규표현식의 g플래그를 포함하세요.

#### 매개변수가 string으로 지정되었을 때
replacement 문자열은 다음과 같은 특수 교체 패턴을 포함할 수 있습니다.

Pattern	Inserts
$$	 "$" 기호
$&	매치된 문자열
$`	매치된 문자열 앞쪽의 문자열
$'	매치된 문자열 뒷쪽의 문자열
$n	n이 1이상 99이하의 정수라면, 첫번째 매개변수로 넘겨진 RegExp객체에서 소괄호로 묶인 n번째의 부분 표현식으로 매치된 문자열

#### 매개변수가 function으로 지정되었을 때
두번째 매개변수로 함수를 지정할 수 있습니다. 이 경우, 함수는 정규표현식 매치가 수행된 후 호출될 것입니다. 함수의 반환값은 교체될 문자열이 됩니다. (참고: 윗쪽에서 언급된 특수 교체 패턴은 반환값에 적용되지 않습니다.) 만약 정규표현식의 플래그로 글로벌(g)이 오는 경우, 함수는 매치될 때마다 계속 호출될 것입니다. 

함수의 매개변수들은 다음과 같습니다.

Possible name	Supplied value
match	매치된 문자열. (윗쪽의 $& 표현식으로 매치된 경우와 동일합니다.)
p1, p2, ...	윗쪽의 $n 표현식과 동일합니다. ($1은 p1, $2는 p2...) 예를 들어, 만약 정규표현식 /(\a+)(\b+)/ 이 주어진다면 p1은 \a+와 매치되고 p2는 \b+와 매치됩니다.
offset	조사된 전체 문자열 중에서 매치된 문자열의 index.(예를 들어, 조사될 전체 문자열이 abcd이고, 매치된 문자열이 bc면 이 매개변수의 값은 1이 됩니다.)
string	조사된 전체 문자열 (replace를 호출한 string)
(p1, p2...의 성격상 함수의 매개변수 갯수는 replace 메서드의 첫번째 매개변수로 넘겨지는 정규표현식 객체에서 소괄호로 묶이는 부분표현식의 갯수에 따라 달라집니다.

다음 예제는 newString을 'abc - 12345 - #$*%'로 교체합니다;

```
function replacer(match, p1, p2, p3, offset, string) {
  // p1 is nondigits, p2 digits, and p3 non-alphanumerics
  return [p1, p2, p3].join(' - ');
}
var newString = 'abc12345#$*%'.replace(/([^\d]*)(\d*)([^\w]*)/, replacer);
```

### 예시(Examples)

replace()의 정규표현식 정의
다음 예제에 따르면, 대소문자를 구분하지 않는 정규표현식을 replace()에 정의했습니다.

var str = 'Twas the night before Xmas...';
var newstr = str.replace(/xmas/i, 'Christmas');
console.log(newstr);  // Twas the night before Christmas...
'Twas the night before Christmas...'로 출력됩니다.

global과 ignore를 사용한 replace()
Global replace can only be done with a regular expression. In the following example, the regular expression includes the global and ignore case flags which permits replace() to replace each occurrence of 'apples' in the string with 'oranges'.

var re = /apples/gi;
var str = 'Apples are round, and apples are juicy.';
var newstr = str.replace(re, 'oranges');
console.log(newstr);  // oranges are round, and oranges are juicy.
This logs 'oranges are round, and oranges are juicy'.

Switching words in a string
The following script switches the words in the string. For the replacement text, the script uses the $1 and $2 replacement patterns.

var re = /(\w+)\s(\w+)/;
var str = 'John Smith';
var newstr = str.replace(re, '$2, $1');
console.log(newstr);  // Smith, John
This logs 'Smith, John'.

Using an inline function that modifies the matched characters
In this example, all occurrences of capital letters in the string are converted to lower case, and a hyphen is inserted just before the match location. The important thing here is that additional operations are needed on the matched item before it is given back as a replacement.

The replacement function accepts the matched snippet as its parameter, and uses it to transform the case and concatenate the hyphen before returning.

function styleHyphenFormat(propertyName) {
  function upperToHyphenLower(match) {
    return '-' + match.toLowerCase();
  }
  return propertyName.replace(/[A-Z]/g, upperToHyphenLower);
}
Given styleHyphenFormat('borderTop'), this returns 'border-top'.

Because we want to further transform the result of the match before the final substitution is made, we must use a function. This forces the evaluation of the match prior to the toLowerCase() method. If we had tried to do this using the match without a function, the toLowerCase() would have no effect.

var newString = propertyName.replace(/[A-Z]/g, '-' + '$&'.toLowerCase());  // won't work
This is because '$&'.toLowerCase() would be evaluated first as a string literal (resulting in the same '$&') before using the characters as a pattern.

Replacing a Fahrenheit degree with its Celsius equivalent
The following example replaces a Fahrenheit degree with its equivalent Celsius degree. The Fahrenheit degree should be a number ending with F. The function returns the Celsius number ending with C. For example, if the input number is 212F, the function returns 100C. If the number is 0F, the function returns -17.77777777777778C.

The regular expression test checks for any number that ends with F. The number of Fahrenheit degree is accessible to the function through its second parameter, p1. The function sets the Celsius number based on the Fahrenheit degree passed in a string to the f2c() function. f2c() then returns the Celsius number. This function approximates Perl's s///e flag.

function f2c(x) {
  function convert(str, p1, offset, s) {
    return ((p1 - 32) * 5/9) + 'C';
  }
  var s = String(x);
  var test = /(-?\d+(?:\.\d*)?)F\b/g;
  return s.replace(test, convert);
}
Use an inline function with a regular expression to avoid for loops
The following example takes a string pattern and converts it into an array of objects.

Input:

A string made out of the characters x, - and _

x-x_
x---x---x---x---
x-xxx-xx-x-
x_x_x___x___x___
Output:

An array of objects. An 'x' denotes an 'on' state, a '-' (hyphen) denotes an 'off' state and an '_' (underscore) denotes the length of an 'on' state.

[
  { on: true, length: 1 },
  { on: false, length: 1 },
  { on: true, length: 2 }
  ...
]
Snippet:

var str = 'x-x_';
var retArr = [];
str.replace(/(x_*)|(-)/g, function(match, p1, p2) {
  if (p1) { retArr.push({ on: true, length: p1.length }); }
  if (p2) { retArr.push({ on: false, length: 1 }); }
});

console.log(retArr);
This snippet generates an array of 3 objects in the desired format without using a for loop.
### 명세서(Specifications)


