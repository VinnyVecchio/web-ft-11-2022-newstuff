function tipAmount(ammount,service){
if (service=== "good") {
    console.log(ammount * .2)
}
else if (service=== "fair") {
    console.log(ammount * .1)
}
else if (service=== "bad") {
    console.log(ammount * 0)
}
}
tipAmount(100,"fair")