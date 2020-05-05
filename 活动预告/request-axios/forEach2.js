const rp = require('request-promise')
const array1 = [1, 2, 3, 4, 5, 6, 7];

array1.forEach(element => {
  if(element<4){
    consoleElement(element)
  }else{
    return 0
  }
});
console.log("hello world3")


async function consoleElement(element) {
  console.log(element)
  await rp('http://www.hzau.edu.cn/hdyg.htm')
  console.log("hello world2")
  return "hello world"
}