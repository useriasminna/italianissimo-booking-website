

document.addEventListener("DOMContentLoaded", function(event) { 
  
  // --------------------------ON REFRESH DELETE HASH IF EXISTS AND RELOAD--------------------------
  if (performance.getEntriesByType('navigation')[0].type != 'navigate') {
    if(window.location.hash){
      history.pushState("", document.title, window.location.pathname);
      window.location = history.state;
      sessionStorage.setItem('pageHasBeenLoaded', 'true');
    }
  }

  if (window.location.pathname=='/') {

    // --------------------------ADD EVENT LISTENER FOR BOTTOM TO TOP BUTTON ON INDEX PAGE--------------------------
    //Get the button
    let mybutton = document.getElementById("btn-back-to-top");

    // When the user clicks on the button, scroll to the top of the document
    mybutton.addEventListener("click", backToTop);

    function backToTop() {
      history.pushState("", document.title, window.location.pathname);
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
    const generateStarsContainers = document.getElementsByClassName('ratings-generated');
    for(container of generateStarsContainers){
      const rateHidden = container.previousElementSibling


      for(i=0; i<rateHidden.value; i++){
        let star = document.createElement("button");
        star.textContent = '★'
        star.classList.add('star')
        star.style.color = "yellow"
        container.appendChild(star)
   
       }
   
       for(i=0; i<5-rateHidden.value; i++){
         let star = document.createElement("button");
         star.textContent = '★'
         star.classList.add('star')
         container.appendChild(star)
    
        }
    }

  }
  

  if (window.location.pathname=='/bookings/createbookings/') {
    const user = document.getElementsByClassName('user')[0];
    if(user.value == "authenticated"){
      const datePicker = document.querySelector("#datePicker");
      const startTime = document.querySelector("#startTime");
      const endTime = document.querySelector("#endTime");
      const customer_name = document.querySelector("#fullName");
      const customer_email = document.querySelector("#email");
      const book_auth = document.querySelector("#bookAuthenticate");
      const tableSelect = document.querySelector("#tableCode")
      const tableOptions = document.querySelectorAll('#tableCode > option')
      const findTableButton = document.getElementsByClassName("continue")[0];
      const continueButton = document.getElementsByClassName("continue")[1];
      const restartButtons = document.getElementsByClassName("restart");
      const finishButton = document.getElementsByClassName("continue")[2];
      const flexButtons = document.querySelector("#flexButtons");
      const bookingOverview = document.querySelector("#bookingOverview");
      const noOfPersons = document.querySelector("#tablePersons");
      const formContainer = document.getElementsByClassName("center-container")[0]

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

      // --------------------------RELOAD PAGE ON RESTART BUTTON CLICK--------------------------
      Array.from(restartButtons).forEach(button => {
        button.addEventListener('click', () => {
          window.location = "/bookings/createbookings"
        })
      });
      


      // --------------------------ENABLE/DISABLE CONTACT INPUTS WHEN 'BOOK IT ON MY NAME' IS CHECKED--------------------------
      book_auth.addEventListener('click', manipulateInputs = () => {
        if(book_auth.checked == true){
          customer_name.readOnly = true;
          customer_email.readOnly = true;
        }
        else{
          customer_name.readOnly = false;
          customer_email.readOnly = false;
        }
      })




      const isRequired = value => value === '' ? false : true;

      const isBetween = (length, min, max) => length < min || length > max ? false : true;


      // --------------------------CHECK IF DATE SELECTED IS BEFORE CURRENT DAY--------------------------
      const isDateValueValid = (date) => {

        // get input value date 
        var inputDate = new Date(date);
        inputDate.setHours(0,0,0,0);

        // get current day
        var today = new Date();
        today.setHours(0,0,0,0);

        if( inputDate >= today )
          return true
        else  
          return false
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
          
          if(h < 10)
            if(m < 10)
              var currentTime = "0"+h+":0"+m;
            else
              var currentTime = "0"+h+":"+m;
          else
            if(m < 10)
              var currentTime = h+":0"+m;
            else
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
        let startInMinutes = (parseInt(startTime.split(":")[0]) * 60 + parseInt(startTime.split(":")[1])) 
        let endInMinutes = (parseInt(endTime.split(":")[0]) * 60 + parseInt(endTime.split(":")[1])) 
        let diffInMin = endInMinutes - startInMinutes
        if( diffInMin < 60 )
          return false
        else
          return true  
      }

      // --------------------------CHECK IF STRING HAS A LENGTH GREATER THAN VALUE GIVEN AS ARGUMENT--------------------------
      const isStringLengthValid = (string, value) => {

        if(string.length > value)
          return false
        else
          return true  
      }

      // --------------------------CHECK IF STRING CONTAINS SPECILA CHARACTERS--------------------------
      const containsSpecialChars = (string) => {
        const specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

        return specialChars.test(string);
      }

      // --------------------------CHECK IF EMAIL RESPECTS EMAIL PATTERN--------------------------
      const isEmailValid = (email) => {
        const email_expression = /^(?:[\w\!\#\$\%\&\'\*\+\-\/\=\?\^\`\{\|\}\~]+\.)*[\w\!\#\$\%\&\'\*\+\-\/\=\?\^\`\{\|\}\~]+@(?:(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-](?!\.)){0,61}[a-zA-Z0-9]?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9\-](?!$)){0,61}[a-zA-Z0-9]?)|(?:\[(?:(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])\]))$/;

        if(email_expression.test(email) == false)
        {
          return false;
        }
        return true;

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
        } else if(!isDateValueValid(date)){
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
        } else if(!isBetween(end, "09:00", "23:00")){
            showError(endTime, 'Choose a time between 09:00 and 23:00');
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


      // --------------------------CHECK NAME INPUT AND SET ERROR MESSAGES--------------------------
      const checkCustomerName = () => {

        let valid = false;

        const name = customer_name.value.trim();
      
        if (!isRequired(name)) {
            showError(customer_name, 'Please type a name');
        } else if(!isStringLengthValid(name, 30)){
          showError(customer_name, 'No more than 30 characters');
        } else if(containsSpecialChars(name)){
            showError(customer_name, 'No special characters');
        } else{
            showSuccess(customer_name);
            valid = true;
        }
        return valid;
      } 

      // --------------------------CHECK EMAIL AND SET ERROR MESSAGES--------------------------
      const checkEmail = () => {

        let valid = false;

        const email = customer_email.value.trim();
      
        if (!isRequired(email)) {
            showError(customer_email, 'Please type an email');
        } else if(!isEmailValid(email)){
            showError(customer_email, 'Email is invalid');
        } else{
            showSuccess(customer_email);
            valid = true;
        }
        return valid;
      } 

    
      // -------------------------CHECK FIRST BOOKING SECTION VALIDITY --------------------------
      findTableButton.addEventListener("click", () => {
        formContainer.scrollTop = formContainer.scrollHeight
        let isdateValid = checkDate();
        let isStartValid = checkStartTime();
        let isEndValid = checkEndTime();
  

        let isDetailsSectionValid = isdateValid &&
            isStartValid &&
            isEndValid;


        // display next section if inputs are valid
        if (isDetailsSectionValid) {

          datePicker.readOnly = true;
          startTime.readOnly = true;
          endTime.readOnly = true;
          findTableButton.style.display = "none";
          window.location = "/bookings/createbookings/#tableContentCollapse"
          document.querySelector('#tableContentCollapse').style.display = 'block';


          // get database entries for bookings and tables from html 
          var bookingsData = JSON.parse(JSON.parse(document.getElementById('bookings_data').textContent));
          var tablesData = JSON.parse(JSON.parse(document.getElementById('tables_data').textContent));
          var tablesStatusImages = []
          
          //check if tables are busy for the date and time selected and create another array of objects with tables code and status image
          for(let table of tablesData){

            var free = true;

            for(let booking of bookingsData){
              var bookingStart = booking.fields.start_time;
              var bookingEnd = booking.fields.end_time;
              
              if(booking.fields.date == datePicker.value && booking.fields.table == table.fields.code && (!(endTime.value <= bookingStart) && !(startTime.value >= bookingEnd))){
                free = false;
                break;
              }
            }

            if(free == true){
              tablesStatusImages.push({"code": table.fields.code, "status":"free", "persons":table.fields.no_of_persons, "image_url":table.fields.table_free_img})
            }
            else{
              tablesStatusImages.push({"code": table.fields.code, "status":"busy", "persons":table.fields.no_of_persons, "image_url":table.fields.table_occupied_img})
            }
          }

          // create images elements and append them to html grid container
          let tableList = document.getElementsByClassName('table-container')[0]
          tablesStatusImages.forEach(table => {
            let img = document.createElement('img');
            img.src ='https://res.cloudinary.com/useriasminna/' + table.image_url
            tableList.appendChild(img);
          })

          //remove busy tables from select options
          for(i = 0; i < tablesStatusImages.length; i++){
            if(tablesStatusImages[i].status == 'busy')
              tableOptions[i].remove()
              for(j=i; j< tableOptions.length; j++){
                tableOptions[j] = tableOptions[j+1]
              }
          }

          
          if(tableSelect.options.length == 0){
            tableSelect.options.add(new Option('No table available', 'message'))
            tableSelect.options[0].selected = true;
            tableSelect.disable=true;
            noOfPersons.value = "";
            continueButton.style.display = "none"
          }
          else{
            tableSelect.options[0].selected = true;
            //set default value for number of persons
            for(let table of tablesStatusImages){
              if(table.code == tableOptions[0].innerHTML){
                noOfPersons.value = table.persons;
                break;
              }
            }
          }

          //make number of persons input to update its value on select change
          tableSelect.addEventListener("change", () => {

            for(let table of tablesStatusImages){
              if(table.code == tableSelect.options[tableSelect.selectedIndex].text){
                noOfPersons.value = table.persons;
                break;
              }
            }
          })

          
          
        }
      })

      // -------------------------CHECK SECOND BOOKING SECTION VALIDITY --------------------------
      continueButton.addEventListener("click", () => {


          // display next section
          formContainer.scrollTop = formContainer.scrollHeight
          window.scrollTo(0, document.body.scrollHeight);
          flexButtons.style.display = "none";
          window.location = "/bookings/createbookings/#bookingContactCollapse"  
          document.querySelector('#bookingContactCollapse').style.display = 'block';
  
      })

      // -------------------------CHECK THIRD BOOKING SECTION VALIDITY --------------------------
      finishButton.addEventListener("click", () => {

        window.scrollTo(0, document.body.scrollHeight);
        formContainer.scrollTop = formContainer.scrollHeight
        
        

        // check validity
        if(book_auth.checked == false){
          

          
          // book_auth.style.display = "none"
          let isNameValid = checkCustomerName();
          let isEmailValid = checkEmail();
    
          let isContactSectionValid = isNameValid && isEmailValid;
    
          // display next section if inputs are valid
          if ( isContactSectionValid) {
    
            book_auth.removeEventListener("click", manipulateInputs)
            
            //prevent user from changing checbox state
            book_auth.addEventListener("click", (event)=>{

              setTimeout(function() {
                this.removeAttr('checked');
              }, 0);
    
              event.preventDefault();
              event.stopPropagation();
            })

            customer_name.readOnly = true
            customer_email.readOnly = true
            finishButton.style.display="none";

            // display next section
            document.querySelector('#overviewCollapse').style.display = 'block';
          }
        } else{

          //prevent user from changing checbox state
          book_auth.addEventListener("click", (event)=>{

            setTimeout(function() {
              this.checked = true
            }, 0);
  
            event.preventDefault();
            event.stopPropagation();
          })
              
            customer_name.parentElement.style.display="none";
            customer_email.parentElement.style.display="none";

            // display next section
            finishButton.style.display="none";
            document.querySelector('#overviewCollapse').style.display = 'block';
        }
        
        window.location = "/bookings/createbookings/#overviewCollapse"  

        //set initial overview value
        bookingOverview.textContent = "You have selected a booking on " + datePicker.value + ", from " + startTime.value + " to " + endTime.value +
                                      ", table for " + noOfPersons.value + " persons."   
                                       
        //update overview every time another table is selected before submit
        tableSelect.addEventListener("change", () => {

          bookingOverview.textContent = "You have selected a booking on " + datePicker.value + ", from " + startTime.value + " to " + endTime.value +
          ", table for " + noOfPersons.value + " persons."

        })                              
      })
    }
   
  }

  if (window.location.pathname.includes('/reviews/')) {
    const rating = document.getElementsByClassName('rating')[0];
    const stars = rating.getElementsByTagName('button');
    const rateValue = document.querySelector('#rateValue');
    const generateStarsContainers = document.getElementsByClassName('ratings-generated');
    const displayUpdateForm = document.querySelector('#displayUpdateForm');
    const myReview = document.querySelector('#myReview');
    const reviewExists = document.querySelector('#reviewExists');
    const addReviewForm = document.querySelector('#addReviewForm')

    //add event listeners for rating stars
    stars[0].clicked = true
    for(let i=0; i<stars.length; i++){
      stars[i].addEventListener('mouseover', () => {
        for(let j=0; j<=i; j++){
          stars[j].style.color = "yellow"
      }
      })
      stars[i].addEventListener('mouseleave', () => {
        for(let j=0; j<=i; j++){
          if(!stars[j].clicked)
            stars[j].style.color = "gray"
        }
      })

      stars[i].addEventListener('click', () => {
        rateValue.value = i+1;
        rateValue.innerHTML = i+1;
        for(let j=0; j<=i; j++){
          stars[j].style.color = "yellow"
          stars[j].clicked = true
        }
        if(i != stars.length-1)
          for(let z=i+1; z<stars.length; z++){
            stars[z].style.color = "gray"
            stars[z].clicked = false
          }
      })

    }

    //generate stars for reviews rating after rate value
   
      for(container of generateStarsContainers){
        const rateHidden = container.previousElementSibling
  
  
        for(i=0; i<rateHidden.value; i++){
          let star = document.createElement("button");
          star.textContent = '★'
          star.classList.add('star')
          star.style.color = "yellow"
          container.appendChild(star)
     
         }
     
         for(i=0; i<5-rateHidden.value; i++){
           let star = document.createElement("button");
           star.textContent = '★'
           star.classList.add('star')
           container.appendChild(star)
      
          }
      }


    //on update button click display update form and fill it with existing values of the review coresponding to the authenticated user
    if(displayUpdateForm)
        displayUpdateForm.addEventListener("click", () => {
          const updateReviewForm = document.querySelector('#updateReviewForm');
          const reviewText = document.querySelector('#reviewTextHidden');
          const reviewTextInput = updateReviewForm.querySelector('#reviewText');
          const updateRating = updateReviewForm.querySelectorAll('.rating')[0].querySelectorAll('button')
          const updateRate = updateReviewForm.getElementsByClassName("rate")[0];
          const formRate = updateReviewForm.querySelector('#rateValue');

          myReview.style.display = "none";
          updateReviewForm.style.display = "block";
          displayUpdateForm.style.display = "none";

          formRate.value = updateRate.value
          reviewTextInput.textContent = reviewText.value

          console.log(updateRate)
          for(let i=0; i<updateRate.value; i++){
            updateRating[i].style.color = "yellow"
          }
        
        })

    //don't display add review form if review already exists for authenticated user
    if(reviewExists)
    {
      addReviewForm.style.display = 'none'
    }


    


  }

  

  

});