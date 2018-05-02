/*
crawler ver0.01

usage: node crawler {default = crawl_opts.json}
=> crawl_opts.json은 download폴더에 저장해 두었다가 crawling 시에 crawler.js 폴더에 이동하여 사용

*/

var request = require('request');
var cheerio = require('cheerio');
var Iconv  = require('iconv').Iconv;
var fs = require('fs');
var URL = require('url');
var opts = require('./crawl_opts.json');

var delay_req = opts.delay_req;
var path = opts.path.dir;
var file = path + '/' + opts.path.file;
var path_img = path + '/' + opts.path.img;
var urls = opts.urls;


if (!fs.existsSync(path)){
  fs.mkdirSync(path);
}

if (!fs.existsSync(path_img)){
  fs.mkdirSync(path_img);
}

var data1 = '';
var data = '';
var delay_write = delay_req*(urls.length + 2);

async function run() {
  for(var k in urls) {
    await sleep(delay_req);

    requestOptions  = { method: "GET"
      ,uri: urls[k]
      ,headers: { "User-Agent": "Mozilla/5.0" }
      ,encoding: 'binary'
    };

    request(requestOptions, function(err, res, html) {
      var contentType = res.headers['content-type'];
      var binaryHtml = new Buffer(html, 'binary');
      var $ = cheerio.load(binaryHtml);

      // img 링크 추출하여 각 링크에 대해 함수 수행
      $("img").each(function(idx) {
        var src = $(this).attr('src');
        //console.log('original image url : ', src);

        // 상대경로를 절대경로로 변환
        src = URL.resolve(urls[k], src);

        if (src.match(/\.png|\.gif|\.jpg/)) {
          // 저장 파일 이름 결정
          var arr_path = URL.parse(src).pathname.split('/');
          var fname = arr_path[arr_path.length-1];

          // 다운로드
          request(src).pipe(fs.createWriteStream(fname));
        }

      });

    });
  }
}

run();

/*
setTimeout(write, delay_write);


function sleep(period){
  return new Promise(resolve => setTimeout(() => resolve(), period));
}


function write() {
  fs.writeFile(file, data1, function(err) {
    if (err) {
      console.log('file write err!!!');
    } else {
      //console.log('\nwrited it!!!\n' + data);
    }
  });
}
*/
