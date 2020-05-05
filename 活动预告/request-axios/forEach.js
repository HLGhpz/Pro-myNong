const rp = require('request-promise')
const array1 = ['a', 'b', 'c'];

array1.forEach(element => consoleElement(element));
console.log("hello world3")

// element => console.log(element)

async function consoleElement(element) {
  console.log(element)
  await rp('http://www.hzau.edu.cn/hdyg.htm')
  console.log("hello world2")
  return "hello world"
}