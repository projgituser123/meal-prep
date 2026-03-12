function delaycheck(){
    console.log("this msg will be printed after 3 seconds...")
}
//setTimeout(delaycheck, 3000)

function clock(){
    console.log(new Date().toLocaleTimeString())
}
//setInterval(clock, 1000)

//intialize two variable and implement both the variable each time and display the addition of both variable at interval of 1s.
let a1 = 10
let b1= 20
let a2= 10
let b2 =20
function add1(){
        let c = a+b
        console.log(a + " + " + b + " = " +c)
        ++a;
        ++b;
}
//setInterval(add, 1000)

function add2(a2,b2){
    let c2 = a2+b2
    console.log(a2 + " + " + b2 + " = " +c2)
    // to stop the timer, use clearInterval
    if (c2>=40) {
        clearInterval(timer_var)
        console.log("reached the limit...")
    }
}
//setInterval(function (){add2(++a2,++b2)},1000)
timer_var = setInterval(function (){add2(++a2,++b2)},1000) // if want to pass a function that has parameters than you to pass anonymous function to setInterval and inside that you write down your original calling function ..