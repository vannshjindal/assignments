// function getDomain(email) {
//   // your code here
// }
// console.log(getDomain("hello@example.com")); // "example.com"


let str = 'hello HELLO'

// output needed : {'h':1,'e':1,'l':2,'o':1,'':1,'H':1,'E':1,'L':2,'O':1}
// {'h':1,'e':1,'l':2,'o':1,'H':1,'E':1,'L':2,'O':1}
// {'h':2,'e':2,'l':2,'o':2}
// let count = 0;
let res = {}
const obj = [
    {name: 'jay', state: 'MP'},
     {name: 'peeyush', state: 'raj'},
      {name: 'jaya', state: 'UP'},
       {name: 'vansh', state: 'MP'}
]

obj.forEach(x=>{
if(res[x.state]){
    res[x.state]++
}else{
    res[x.state]=1
}
})
console.log(res)

for(let i =0; i<str.length; i++) {
    if(str[i] === ' ') continue;
    if(res[str[i]]) {
        res[str[i]]++
    } else {
        res[str[i]] = 1
    }
}
 
console.log(res)