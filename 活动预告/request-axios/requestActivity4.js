const rp = require('request-promise')
const cheerio = require('cheerio')
const selectActivePath = 'div.zy-mainxrx ul li'
const imgBaseUrl = 'http://www.hzau.edu.cn/'

// 请求活动数据
async function reqActivity(lastNumber) {
  let activityData = []
  let html = await rp('http://www.hzau.edu.cn/hdyg.htm')
  $ = cheerio.load(html)
  $(selectActivePath).each((index, elem)=>{
    getData($, elem, lastNumber).then(res=>{
      console.log(res)
    }).catch(err=>{
      console.log(err)
    })
  })
}

async function getData ($, elem, lastNumber) {
  let elemLink = $('a', $(elem)).attr('href')
  let elemNumber = parseInt(elemLink.match(/\d+/g)[1])
  if (elemNumber > lastNumber) {
    let activityLink = imgBaseUrl + elemLink.replace("../", "").replace("../", "")
    let activityTitle = $('a', $(elem)).text()
    let activityTime = $('small', $(elem)).text()
    let activitySponsor = $('span', $(elem)).text()
    let activityNumber = elemNumber;
    let imgHtml = await rp(activityLink)
    let soup = cheerio.load(imgHtml)
    activityImg = soup('div.v_news_content p img').attr('src')
    return {activityTitle, activityTime, activitySponsor, activityNumber}
  }
  throw "hello world"
}

reqActivity(10819)
