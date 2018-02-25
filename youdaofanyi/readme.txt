记得填写cookie！


sign的计算过程：

打开网页，在Sources里面找到fanyi.min.js文件（文件名可能会改），格式化里面的js代码，搜索sign：
找到sign: o,
再找到o = n.md5("fanyideskweb" + t + i + "ebSeFb%=XZ%T[KZ)c(sy!");这是计算sign，其中t为输入的内容
再找到i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),这是计算salt