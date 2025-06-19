function retrieve(arr, n = 1) {
  if (n < arr.length) {
    for (i = 0; i < n; i++) {
      console.log(arr[i]);
    }
  }
}

retrieve([1, 2, 3, 4, 5], 2);
