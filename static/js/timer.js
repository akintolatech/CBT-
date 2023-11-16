


var time = document.querySelector('#time');


//Prevent Data
history.pushState(null, null, );
window.addEventListener('popstate', function(event) {
  history.pushState(null, null, );
});


function startTimer(duration, display) {
    var timer = duration;
	var minutes, seconds;
	var warning = 60;
//	var ok=false;
	var form=document.forms.test;

   var interval = setInterval(function () {


        //store current time state in local storage
        window.localStorage.setItem("seconds",seconds);
        window.localStorage.setItem("minutes",minutes);

        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

       if(timer <= 60) {
            document.querySelector('#time').style.color = "red"
        }



        if(--timer < 0) {
            timer = duration;
            clearInterval(interval);
            form.submit();
            window.localStorage.clear();

        }


        }, 1000);
}


window.onload = function() {
    var sec  = parseInt(window.localStorage.getItem("seconds"));
    var min = parseInt(window.localStorage.getItem("minutes"));

    if (isNaN(sec) || isNaN(min)) { // check if sec or min is NaN
        var examTime = 60 * 10; // set default exam time to 50 minutes
    } else {
        var examTime = parseInt((min * 60) + sec); // convert minutes and seconds to seconds
    }


    var display = document.querySelector('#time');
    display.style.color = "green";
//    console.log(display)
    startTimer(examTime, display);

};









