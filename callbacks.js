const calculate = (a,b,operation) => {
return operation (a,b);
}

const addition = (3,4,function (num1,num2){
    return (num1 + num2);
}) 

console.log(addition);
