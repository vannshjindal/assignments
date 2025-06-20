//check if it contains a substring\
function containsCode(str) {
 return  str.toLowerCase().includes("code")
}
console.log(containsCode("I love coding.")); // false
console.log(containsCode("I write Code daily.")); // true