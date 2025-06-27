let arr = [4, 5, 6, 7, 0, 1, 2, 3];
let min = arr[0];
let index = 0;

for (let i = 1; i < arr.length; i++) {
  if (arr[i] < min) {
    min = arr[i];
    index = i;
  }
}

console.log("Array is rotated", index, "times.");