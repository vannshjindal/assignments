let api1 = fetch("https://picsum.photos/v2/list")
let api2 = fetch("https://dummyjson.com/users/1")
let api3 = fetch("https://reqres.in/api/users?page=1")
let api4 = fetch("https://reqres.in/api/users/1")


Promise.all([api1,api2,api3,api4])
  .then(allResponses=>{
    return Promise.all(allResponses.map(response=> response.json()));
 })
  .then(allData=>{
    console.log("DATA:",allData)
  })

  .catch(error=>{
    console.log("ERROR:",error)
  });
 