const rp = require('request-promise')
const cheerio = require('cheerio')
const selectActivePath = 'div.zy-mainxrx ul li'
const imgBaseUrl = 'http://www.hzau.edu.cn/'
// rp(options)
//   .then(data=>{
//     console.log(data)
//   })
//   .catch(err=>{
//     console.log(res)
//   })

// 请求活动数据
async function reqActivity(lastNumber) {
  let activityData = []
  let html = await rp('http://www.hzau.edu.cn/hdyg.htm')
  $ = cheerio.load(html)
  $(selectActivePath).each((index, elem) => {
    elemLink = $('a', $(elem)).attr('href')
    elemNumber = parseInt(elemLink.match(/\d+/g)[1])
    if (elemNumber > lastNumber) {
      getActivityData(elem)
      console.log("reqActivity")
      // activityData = getActivityData(elem)
      // console.log("activityData", activityData)
    }
  })
  // console.log("打印数据", activityData)
}

// 遍历获取活动数据
function getActivityData(elem) {
  let activityImg = []
  let activityLink = imgBaseUrl + elemLink.replace("../", "").replace("../", "")
  // 获得图片数据
  activityImg = getActivityImg(activityLink)
  console.log("getActivityData")
  let activityNumber = elemNumber;
  let activityTitle = $('a', $(elem)).text()
  let activityTime = $('small', $(elem)).text()
  let activitySponsor = $('span', $(elem)).text()
  return {
    activityImg,
    activityNumber,
    activityTitle,
    activityTime,
    activitySponsor
  }
}

// 请求图片数据
async function reqActivityImg(activityLink) {
  return await rp(activityLink)
}

// 获得图片数据
function getActivityImg(activityLink) {

  reqActivityImg(activityLink).then(res => {
    let imgHtml = ""
    let activityImg = []
    imgHtml = res
    let soup = cheerio.load(imgHtml)
    activityImg = soup('div.v_news_content p img').attr('src')
    // if (typeof (activityImg) == "undefined") {
    //   activityImg = []
    // } else {
    //   activityImg.push(imgBaseUrl + $('div.v_news_content p img').attr('src'))
    // }
    console.log("getActivityImg", activityImg)
  })
  console.log("getActivityImg2")
  // return activityImg
}



reqActivity(10819)