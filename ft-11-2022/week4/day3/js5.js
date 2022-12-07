function tipAmount(total,tip){
    if(tip === "good"){
        return(total * (20/100))+ total
    }
    if(tip === "fair"){
        return(total * (15/100))+ total
    } else(tip === "bad");
        return(total * (10/100))+ total

}

console.log(tipAmount(100,"good"))
