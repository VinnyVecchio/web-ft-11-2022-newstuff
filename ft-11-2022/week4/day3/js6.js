function splitamount(total, service, people){
if(service === "good"){
    return ((total * (20/100)) + total) / people
}
else if(service === "fair"){
    return ((total * (15/100)) + total) / people
}
else if(service === "bad"){
    return ((total * (10/100)) + total) / people 
}
}
console.log(splitamount(100,"good",2))