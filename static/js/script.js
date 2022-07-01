

document.addEventListener("DOMContentLoaded", function(event) { 

  if (window.location.pathname=='/') {

    // --------------------------ADD EVENT LISTENER FOR BOTTOM TO TOP BUTTON ON INDEX PAGE--------------------------
    //Get the button
    let mybutton = document.getElementById("btn-back-to-top");

    // When the user clicks on the button, scroll to the top of the document
    mybutton.addEventListener("click", backToTop);

    function backToTop() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }

  }

  if (window.location.pathname=='/%2Fbooking/booking') {
    const datePicker = document.querySelector("#datePicker");
    const startTime = document.querySelector("#startTime");
    const endTime = document.querySelector("#endTime");
    const findTableButton = document.getElementsByClassName("continue")[0];
    const continueButton = document.getElementsByClassName("continue")[1];
    const finishButton = document.getElementsByClassName("continue")[2];

    // --------------------------SET DATE PICKER INPUT MIN VALUE TO TODAY DATE--------------------------
    datePicker.min = new Date().toLocaleDateString('en-ca')


    // --------------------------SET DATE PICKER DEFAULT VALUE TO TODAY DATE--------------------------
    datePicker.min = new Date().toLocaleDateString('en-ca')
    var currentDay = new Date();
    var dd = String(currentDay.getDate()).padStart(2, '0');
    var MM = String(currentDay.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = currentDay.getFullYear();
    currentDay = yyyy + '-' + MM + '-' + dd;
    datePicker.value = currentDay


    // --------------------------SET TIME INPUT VALUE TO :00 FORMAT FOR MINUTES--------------------------
    startTime.addEventListener("change", function(evt) {
      var match = this.value.match(/^(\d{2})/);
      if (match) this.value = match[1] + ":00";
    });

    endTime.addEventListener("change", function(evt) {
      var match = this.value.match(/^(\d{2})/);
      if (match) this.value = match[1] + ":00";
    });

    const isRequired = value => value === '' ? false : true;

    const isBetween = (length, min, max) => length < min || length > max ? false : true;


    // --------------------------CHECK IF DATE SELECTED IS BEFORE CURRENT DAY--------------------------
    const isDateValid = (date) => {

      // get input value date 
      var inputDate = new Date(date);
      inputDate.setHours(0,0,0,0);

      // get current day
      var today = new Date();
      today.setHours(0,0,0,0);

      if( inputDate.getTime() < today.getTime() )
        return false
      else  
        return true
    }

     // --------------------------CHECK IF START TIME IS AFTER CURRENT TIME FOR TODAY BOOKINGS--------------------------
    const isStartTimeTodayValid = (startTime) => {
      

      // get input value date 
      var inputDate = new Date(datePicker.value);
      inputDate.setHours(0,0,0,0);

      // get current day
      var today = new Date();
      today.setHours(0,0,0,0);

      if( inputDate.getTime() == today.getTime() ){

        // get system local time
        var d = new Date();
        var m = d.getMinutes();
        var h = d.getHours();
        if(h == '0') {h = 24}
        
        var currentTime = h+":"+m;

        
        if(startTime <= currentTime)
          return false
        else
          return true  
      }
      else
        return true
    }

    // --------------------------CHECK IF END TIME IS GREATER THAN START TIME--------------------------
    const isTimeIntervalValid = (startTime, endTime) => {
      if(startTime >= endTime)
        return false
      else
        return true  
    }

    // --------------------------CHECK IF BOOKING TIME IS GREATER THAN 60 MIN--------------------------
    const isTimeIntervalCorrect = (startTime, endTime) => {
      let startInMinutes =(parseInt(startTime.split(":")[0]) * 60 + parseInt(startTime.split(":")[1])) 
      let endInMinutes =(parseInt(endTime.split(":")[0]) * 60 + parseInt(endTime.split(":")[1])) 
      let diffInMin = endInMinutes - startInMinutes
      if( diffInMin < 60 )
        return false
      else
        return true  
    }

    // --------------------------DISPLAY ERROR--------------------------
    const showError = (input, message) => {
        // get the form-field element
        const formField = input.parentElement;
    
        // show the error message
        const error = formField.querySelector('small');
        error.textContent = message;
    };

    // --------------------------HIDE ERROR--------------------------
    const showSuccess = (input) => {
      // get the form-field element
      const formField = input.parentElement;

      // hide the error message
      const error = formField.querySelector('small');
      error.textContent = '';
    }

    // --------------------------CHECK DATE AND SET ERROR MESSAGES--------------------------
    const checkDate = () => {

      let valid = false;

      const date = datePicker.value.trim();

      if (!isRequired(date)) {
          showError(datePicker, 'Please choose a date');
      } else if(!isDateValid){
          showError(datePicker, 'A date before current day is not valid');
      } else {
          showSuccess(datePicker);
          valid = true;
      }
      return valid;
    } 

    // --------------------------CHECK START TIME AND SET ERROR MESSAGES--------------------------
    const checkStartTime = () => {

      var currentTime = new Date().toLocaleTimeString(navigator.language, {hour: '2-digit', minute:'2-digit'});

      let valid = false;

      const time = startTime.value.trim();

      if (!isRequired(time)) {
          showError(startTime, 'Please choose a start time');
      } else if(!isBetween(time, "09:00", "23:00")){
          showError(startTime, 'Choose a time between 09:00 and 23:00');
      } else if (!isStartTimeTodayValid(time)){
          showError(startTime, 'Please choose a time after ' + currentTime);
      } else
      {
          showSuccess(startTime);
          valid = true;
      }
      return valid;
    } 

    // --------------------------CHECK END TIME AND SET ERROR MESSAGES--------------------------
    const checkEndTime = () => {

      let valid = false;

      const start = startTime.value.trim();
      const end = endTime.value.trim();

      if (!isRequired(end)) {
          showError(endTime, 'Please choose an end time');
      } else if(!isBetween(end, "10:00", "24:00")){
          showError(endTime, 'Choose a time between 10:00 and 24:00');
      } else if (!isTimeIntervalValid(start, end)){
          showError(endTime, 'End hour must be grater than start hour');
      } else if(!isTimeIntervalCorrect(start, end)){
        showError(endTime, 'Booking must be for at least an hour');
      }else
      {
          showSuccess(endTime);
          valid = true;
      }
      return valid;
    } 


    // -------------------------CHECK FIRST BOOKING SECTION VALIDITY --------------------------
    findTableButton.addEventListener("click", () => {

      let isdateValid = checkDate();
      let isStartValid = checkStartTime();
      let isEndValid = checkEndTime();
 

      let isInputsSection = isdateValid &&
          isStartValid &&
          isEndValid;


      // display next section if inputs are valid
      if (isInputsSection) {
        console.log("VALID")
        datePicker.disabled = true;
        startTime.disabled = true;
        endTime.disabled = true;
        findTableButton.style.display = "none";
        document.querySelector('#tableContentCollapse').style.display = 'block';
        
      }
    })

    // -------------------------CHECK SECOND BOOKING SECTION VALIDITY --------------------------
    continueButton.addEventListener("click", () => {

        // check validity


        // display next section
        continueButton.style.display="none";  
        document.querySelector('#bookingContactCollapse').style.display = 'block';
 
    })

    // -------------------------CHECK THIRD BOOKING SECTION VALIDITY --------------------------
    finishButton.addEventListener("click", () => {

      // check validity


      // display next section
      finishButton.style.display="none";
      document.querySelector('#bookingDetails').style.display = 'none';
      document.querySelector('#tableContentCollapse').style.display = 'none';
      document.querySelector('#bookingContactCollapse').style.display = 'none';
      document.querySelector('#overviewCollapse').style.display = 'block';

    })






   
  }
  

});