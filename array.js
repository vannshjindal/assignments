// var arr = [1, 2, 3, 4, 5];
// arr.forEach(function(val){
//     console.log(val+"  Hello");
// })


// console.log("start!");




var arr = [1, 2, 3, 4, 5];

var ans = arr.filter(function(val){
    if(val>=2){return true}
    else return false;

})

console.log(ans); 




var obj = {
    name : "Vansh", 
    age : 22,
    designation : "Software Engineer"
}

console.log(obj.name);