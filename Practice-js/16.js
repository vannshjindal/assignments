function countVowels(str) {
 let count = 0;
 str.toLowerCase().split("").forEach(x=>{
    if(x=="a"||x=="e"||x=="i"||x=="o"||x=="u"){
        count ++; 

    }

 })
 return count;

}
console.log(countVowels("JaVaSCrIPt")); 