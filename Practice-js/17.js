function cleanSentence(str) {
  let strArr = str.split(" ");
  const badWords = ['bad', 'ugly'];
  return strArr.map(x=>{
    if(badWords.includes(x)){
        return '***'
    } else {
        return x;
    }
  }).join(" ");
}
console.log(cleanSentence("That was a bad and ugly day.")); // "That was a *** and *** day."
