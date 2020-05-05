const rp = require('request-promise')
const cheerio = require('cheerio')
const selectActivePath = 'div.zy-mainxrx ul li'
const imgBaseUrl = 'http://www.hzau.edu.cn/'

// 请求活动数据
async function reqActivity(lastNumber) {
  let activityData = []
  let html = await rp('http://www.hzau.edu.cn/hdyg.htm')
  $ = cheerio.load(html)
  $(selectActivePath).each(async function (index, elem) {
    elemLink = $('a', $(elem)).attr('href')
    elemNumber = parseInt(elemLink.match(/\d+/g)[1])
    if (elemNumber > lastNumber) {
      let activityLink = imgBaseUrl + elemLink.replace("../", "").replace("../", "")
      let activityTitle = $('a', $(elem)).text()
      let activityTime = $('small', $(elem)).text()
      let activitySponsor = $('span', $(elem)).text()
      let activityNumber = elemNumber;
      let imgHtml = await rp(activityLink)
      let soup = cheerio.load(imgHtml)
      activityImg = soup('div.v_news_content p img').attr('src')
      console.log({activityTitle, activityTime, activitySponsor, activityNumber})
    }
  })
}

reqActivity(10819)
console.log("hello world")
