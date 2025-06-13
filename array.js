let arr = new Array(5);
let sum = 0;


for(let i = 0; i<arr.length;i++){
    arr[i] = Number(prompt("Enter your number: "))
    sum = sum + arr[i]

    }
    console.log(arr)
console.log("Sum of all elements is: " + sum);

let arr1 = [2,3,4,5,6,7,8]

let min = arr1[0];

for(i=1;i<arr1.length;i++){
    if(arr[i]< min){
        min = arr1[i];
    }
}
    console.log("Minimum element is: " + min)