function countA(str) {
  
    let count = 0;
    str.toLowerCase().split("").forEach(x=>{
        if(x==="a"){
           count ++;
           
        }
        
        
    })
    return count;
}
console.log(countA("An amazing apple")); 



function hidePhone(phone) {
  return phone.replace("987654","******")
}
console.log(hidePhone("9876543210")); 
