function checkPal(str){
  let revpal =   str.split("").reverse().join("")
   if(revpal === str){
    return true;
   } else{
    return false;
   }
}

console.log(checkPal("cooc"));
console.log(checkPal("loop"));