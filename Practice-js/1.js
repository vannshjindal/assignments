let str = "Vansh Jindal is cooked!"
let rev =str.split(" ").map(function(x){
    return x.split("").reverse().join("")
})

console.log(rev.join(" "))