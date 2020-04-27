const axios = require('axios');
const cheerio = require('cheerio')

const instance = axios.create({
	baseURL: 'http://www.hzau.edu.cn',
	timeout: 1000,
	headers: {
		'X-Custom-Header': 'foobar'
	}
});

const hdygUrl = '/hdyg.htm'
const selectPath = 'div.zy-mainxrx ul li'

// function requestUrl() {
// 	instance.get('http://www.hzau.edu.cn/hdyg.htm')
// 	.then(function (response) {
// 		// console.log(response.data)
// 		let $ = cheerio.load(response, {
// 			ignoreWhitespace: true,
// 			xmlMode: true,
// 			lowerCaseTags: true
// 		})
// 		console.log($('ul li').text())
// 		// let active = $('ul li')
// 		// console.log(active)
// 		// getActivity($)
// 	})
// 	.catch(function (error) {
// 		// handle error
// 		console.log(error);
// 	})
// 	.then(function () {
// 		console.log()
// 	});
// }

// function getActivity($){
// 	console.log($)
// 	// console.log($(selectPath))
// }

// requestUrl()

instance.get('http://www.hzau.edu.cn/hdyg.htm')
	.then(response => {
		let $ = cheerio.load(response.data, {
			decodeEntities: false
		});
		// console.log($(selectPath).text())
		let sponsor = $(`${selectPath} span`).text()
		// let title = $(`${selectPath} a`).attr('title').text()
		// let time = $(`${selectPath} a`).attr('href').text()
		console.log($(`${selectPath} a`).attr('title'))
	})