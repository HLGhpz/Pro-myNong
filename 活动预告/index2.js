const axios = require('axios');
const cheerio = require('cheerio')
const fs = require('fs')

const instance = axios.create({
  baseURL: 'http://www.hzau.edu.cn',
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar'
  }
});

const baseUrl = 'http://www.hzau.edu.cn/'
const hdygUrl = '/hdyg.htm'
const selectActivePath = 'div.zy-mainxrx ul li'
const selectImagePath = 'div.v_news_content p img'



function reqHdyg() {
  let url;
  for (let index = 0; index < 30; index++) {
    url = `${baseUrl}hdyg/${index}.htm`
    instance.get(url)
      .then(response => {
        let $ = cheerio.load(response.data, {
          decodeEntities: false
        });
        $(selectActivePath).each(function (i, elem) {
          let sponsor = $('span', $(this)).text()
          let title = $('a', $(this)).attr('title')
          let time = $('small', $(this)).text()
          let link = $('a', $(this)).attr('href')
          console.log(sponsor, title, time, link)
        })
      })
  }

}

reqHdyg()