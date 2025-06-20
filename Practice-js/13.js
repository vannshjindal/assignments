function isPalindrome(str) {
 let rev = str.toLowerCase().split("").reverse().join("")
 if(str === rev){
    return "Palindrome"
 }else return "Not a palindrome";
 
}
console.log(isPalindrome("vaav"));
