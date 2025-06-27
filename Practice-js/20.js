const cluster = require("cluster")
const os = require("os");

const TotalCpus = os.cpus().length

console.log(TotalCpus);

