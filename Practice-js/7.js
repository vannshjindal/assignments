let arr = ["wrffrfef","ffefefe","fff",1,4,23,44,"dbbff"]

let sum = 0; 
arr.forEach(function (x){
if(typeof x == 'number'){
    sum = sum + x
}
})

console.log(sum);