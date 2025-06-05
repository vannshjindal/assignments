const fs = require("fs");


fs.writeFile("hey.txt","Hey this is Vansh Jindal", function(err){
    if(err){console.log(err);}
    else{console.log("done");}
})


fs.appendFile("hey.txt"," and I am a Software Engineer", function(err){
    if(err){console.log(err);}
    else{console.log("done");}
})

fs.unlink("hey.txt", function(err){
    if(err){console.log(err);}
    else{console.log("done");}
}
)
