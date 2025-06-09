const express = require('express');
const app = express();


app.get("/", function(req,res){
    res.send("Hello World");
});

app.get("/profile", function(req,res){
    res.send("Hello world!");
});

app.get("/profile/:username", function(req,res){
    res.send(`Welcome ${req.params.username} to your profile`);
});



app.listen(3000, function(){
    console.log("Server is running on port 3000");
});