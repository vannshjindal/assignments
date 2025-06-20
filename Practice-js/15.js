function countWords(str) {
    let count = 0;
  str.split(" ").forEach(x=>{
    count ++;
  })
  return count;
}
console.log(countWords("Hello, I am learning JS")); 
