# Testing

Back to [README.MD](README.MD)<br>

## Table of contents
* [User Story and Feature Testing](#user-story-and-feature-testing)
* [Automated View Testing](#automated-view-testing)
* [Browser Testing](#browser-testing)
* [Code Validation](#code-validation)


## User Story and Feature Testing
All the user stories were tested manually, that including all the representative features, and were described bellow with a summary of the steps made for demonstrating the validation of the tests: <br>

### CONTENT AND NAVIGATION<hr>
#### 1A: As a user, I want to see a menu so I can easily navigate through website content  
* **Acceptance Criteria:** A site user should always have access to the navigation menu so he can easily switch between pages at any time.
* **Summary:**<br>
    -When a user visits the website he can easily see the navigation menu at the top of the page;<br>
    -Even if switching the pages, the menu is always present at the top and indicates what page is active at the moment;<br>
    -For the *Home* page, a *Bottom to top* button is present at the end of the content, considering that its size can vary, and redirects the user to the page start where he can access the navigation links;<br>
    -For logged-in clients, the menu contains an additional page, *Profile*, and *Logout* link replaces *Register* and *Login* pages;<br>
    -For logged-in staff members, the navigation includes *Manage Bookings* page, instead of *Profile*.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass
#### 1B: As a user, I want to see relevant information about the restaurant
* **Acceptance Criteria:** A site user should be able to see relevant information that will help him create an idea about the restaurant's services.
* **Summary:**   
    -When a user first visits the website, he is redirected to the *Home* page and a big cover with a pizza background is displayed, suggesting what is the speciality of the restaurant;<br>
    -The cover also displays information about the name, year of opening and slogan of the restaurant;<br>
    -"About us" is a section on the *Home* page that describes the restaurant's mission and contains two images of the place;<br>
    -Another two sections exist on the *Home* page that help the user to make an idea about the quality of the services: *Most Appreciated Dishes* and *Top Reviews*;<br>
    -More information about the restaurant specialities and contact details can be found on the *Menu* and *Where to find us* pages.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass
#### 1C: As a user, I want the website to have a nice and intuitive design that will match the restaurant's theme
* **Acceptance Criteria:**  A site user should be able to access the content through an attractive design that would make him want to return to it anytime.
* **Summary:**<br>
    -When a user first visits the website he is redirected to *Home page* where the first impression is created when noticing the well-chosen fonts chosen for the navbar, title and slogan, as well as the cover image which suggests the restaurant's speciality;<br>
    -The colours of the website were tested to match the contrast requirements and all the colours chosen are derivated from the colours' palette of the background cover;<br>
    -On the website there are elements created to help the user have a better experience when navigating through the content, such as hyperlinks, arrows redirecting to the next section of the page or a button to bring the user back to the top;<br>
    -On the Home, Menu and Reviews page, there are messages that suggest to the user to Register or Login to enjoy all the features of the website;<br>
    -The user gets feedback as alerts every time he performs an action such as Registering, Signing In/Signing Out, adding a booking, posting/updating a review.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass   
### USER REGISTRATION/AUTENTHICATION<hr>
#### 2A: As a user, I want to be able to register on the website
* **Acceptance Criteria:** A site user should be able to create an account by filling in a form on the website.   
* **Summary:**<br>
    -There is a Register page that provides a form with email, first name, last name and password for the user to fill in;<br>
    -When the user submits the form a new entry is created in the Users table;<br>
    -A success alert is displayed with the message "Logged in as..." that confirms to the user that he has been registered successfully.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 
#### 2B: As a user, I want to be able to authenticate using only email and password
* **Acceptance Criteria:** A site user should be able to authenticate at any time with email and password.
* **Summary:**<br>
    -There is a Login page that provides a form with email and password to be filled;<br>
    -The authentication form has a "Remember me" checkbox that will keep the user logged in;<br>
    -A success alert is displayed with the message "Logged in as..." that confirms to the user that he has been logged in successfully.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 2C: As a user, I want to be able to logout at any time
* **Acceptance Criteria:** A site user should be able to exit current account at any time.
* **Summary:**    
    -There is a Logout modal that can be triggered when clicking on the hyperlink in the navbar. The modal is implemented as part of defensive programming;<br>
    -The logout modal asks the user again if he wishes to exit the current account;<br>
    -A success alert is displayed with the message "Logged out" that confirms to the user that he has been successfully logged out.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### BOOKING<hr>
#### 3A: As a logged in user, I want to be able to find the available tables for a specific date and time
* **Acceptance Criteria:** A logged user should be provided a booking system that generates the tables availability.  
* **Summary:**<br> 
    -There is a booking page that can be accessed only by authenticated users, considering that all the booking entries must have the current user as the author;<br>
    -The booking sections appear successive only after the previous ones are validated;<br>
    -The first section contains inputs for Date, Start and End time, for the user to fill in;<br>
    -The validation of these values is very strict to prevent errors when generating the tables section. The following rules are being checked:
    * The Date value should not be less than the current day;<br>
    * For the current day the Start hour can't be less than the current hour;<br>
    * End Hour should be greater than Start hour;<br>
    * Start and End hours must be between 9:00 AM - 11:00;<br><br>

    -When the user clicks the *Find a table* button, if the validation is complete, the next section appears with all the tables in the restaurant;<br>
    -There is a legend with the colours for "Free" and "Busy" status of the tables;<br>
    -If a table is reserved for the date filled in by the user, and the reservation time intersects with the hours in the form, the table appears in grey, as *Busy*, otherwise in bright yellow, as *Free*.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 3B: As a logged in user, I want to be able to select the table that I want to reserve and complete my booking
* **Acceptance Criteria:** A logged in user should be be able to complete his booking by choosing one of the free tables available.
* **Summary:**<br>
    -When the tables' section is displayed, it also contains a dropdown with the tables' codes;<br> 
    -The dropdown values correspond with the status of the tables and only the ones with the status *Free* are included in the list, for preventing errors when submitting the booking;<br> 
    -A read-only input is placed near the dropdown, of which value represents the number of seats on the table, as information for the user;<br> 
    -When the user chooses another value from the tables dropdown list, the value of the input changes accordingly;<br> 
    -After selecting a table there is only one more step for completing the reservation, the contact details, which can be filled in or registered automatically when choosing *Book it on my name*;<br> 
    -If the overview of the booking corresponds with the user's selections, the form can be submitted;<br> 
    -An alert appears to inform the user that the reservation was successful.<br> <br> 

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### MENU<hr>
#### 4A: As a user, I want to see the restaurant's menu with details about ingredients and price, so that I can be completely aware of everything I want to order
* **Acceptance Criteria:** A user should be provided with a list of the menu content, as essential information for a restaurant client.
* **Summary:**<br>
    -There is a *Menu* page that can be accessed by any type of user;<br>
    -A list of meals is displayed and it is visible to any type of user;<br>
    -Every menu item is provided with an image of the meal, name, ingredients and price;<br>
    -All images have the same dimensions, with transparent backgrounds, and prices are highlighted, for better visual impact.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 4B: As a logged in user, I want to be able to mark/unmark my favorite dishes on the menu
* **Acceptance Criteria:** A logged-in user should be provided with a way of marking/unmarking his favourite dishes only when he's authenticated. 
* **Summary:**<br> 
    -In the menu page, there is a feature visible only to users that are authenticated and not staff members, considering that this feature wouldn't make sense for admins;<br>
    -For unauthenticated users, an informative message is displayed for users to log in to be able to mark their favourite meals;<br>  
    -To mark a dish as *favourite*, a form is displayed with an empty heart icon that acts like a button, and a suggestive message, "Add to favourites", that indicates to the user what is its purpose;<br>
    -When the user clicks on the button, the change is visible immediately, as the heart icon changes its shape into a filled heart, and the message is now "Remove from favourites";<br>
    -By clicking on the filled heart, the form comes back to its initial state, and the meal is removed from favourites;<br>
    -It has been tested the removing of the *favourite* entry using the URL and no action is performed. Also when it was tested for another user, the custom 403(forbidden) page appears;<br>
    -The state of the meals is visually represented and constant even if the user reloads the page, that meaning that the database has successfully updated the list that contains the favourite dishes for the current user;<br>
    -The list of *Favourite* meals also influences the elements displayed in the section *Most appreciated dishes* found on the *Home* page. The dishes change their order depending on the number of users that marked them as *favourite*.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 
### USER PROFILE<hr>
#### 5A: As a logged in user, I want to view a list of my upcoming bookings
* **Acceptance Criteria:** A logged in user should be able to see all the upcoming reservations made on his account. 
* **Summary:**<br>
    -There is a *Profile* page that is visible only to authenticated users and is prohibited to staff members;<br>
    -On the *Profile* page there is a section called *Upcoming bookings*;<br>
    -Whenever a user makes a successful reservation on the *Booking* page, the element is immediately added and visible on the *Profile* page;<br> 
    -The section contains all bookings except the ones reserved before the current day, as the older bookings are not considered relevant anymore to be displayed in profile;<br>
    -Every booking is represented as a note with the essential details on it  such as Date, Start/End time, Table code and Customer name, and the list is paginated to display only 2 elements at a time for a better visual impact;<br>
    -As this section contains the list of the bookings made from this account, it includes all the reservations that are created by the current user, whether the customer name was registered as the current name or another name.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 5B: As a logged in user, I want to be able to cancel my bookings
* **Acceptance Criteria:** A logged in user should be provided a way to delete a booking if he no longer wishes to keep it. 
* **Summary:**<br>
    -Every element in the *Upcoming Bookings* section has a "Delete booking" button;<br>
    -When the user clicks on the button a modal is triggered for confirmation;<br>
    -Each modal asks for confirmation by displaying the Date, Start and End time of the reservation in order to prevent an unwanted removal;<br>
    -After confirmation, the output is immediately visible as the element is removed from the list, and if the list becomes empty a suggestive message is displayed;<br>
    -It has been tested the removal of the *booking* entry using the URL and no action is performed. Also when it was tested for another user, the custom 403(forbidden) page appears.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 5C: As a logged in user, I want to see a list with my favorite dishes of the restaurant
* **Acceptance Criteria:** A logged in user should be able to see all the meals added to *Favourite* list displayed in *Profile* page.  
* **Summary:**<br>
    -In *Profile* page there is a section called *Your favourite dishes*;<br>
    -The section displays every meal from the menu added to *Favourite* list;<br>
    -Every element is represented with the meal image and name using a simple and atractive design;<br>
    -When adding a meal to *Favourites* list from the *Menu* page, the change is immediately reflected in the *Profile* page as well.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### STAFF MANAGE BOOKINGS<hr>
#### 6A: As a logged in staff member, I want to see the restaurant's upcoming bookings for the current day sorted by time
* **Acceptance Criteria:** A logged in staff member should be able to see bookings from all the users ordered by time and grouped by date.   
* **Summary:**<br>
    -There is a *Manage Bookings* page visible only for logged-in staff members and prohibited for users that are not staff;<br>
    -The page displays all the bookings for the current day sorted by time, which is very helpful for a staff member that wants to take a look over today's reservations;<br>
    -The bookings are listed in a table and every column represents an important detail such as Date, Time interval, Table code, Customer name and email;<br>
    -There is an informative text that specifies the date and number of the bookings.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 6B: As a logged in staff member, I want to be able to filter bookings by date
* **Acceptance Criteria:** A logged-in staff member should be provided with a way of sorting bookings by date for a clearer way of visualising the reservations.
* **Summary:**<br>
    -Considering that the page displays by default only the bookings for the current day, there is a form that is used for filtering the data by date;<br>
    -On submitting the form the reservations for the selected date appear with the informative text displaying the date and number of bookings;<br>
    -The filter for the bookings can be applied any number of times the user wishes and also for reservations made before the current day.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 6C: As a logged in staff member, I want to be able to cancel bookings
* **Acceptance Criteria:** A logged-in staff member should be able to delete any reservation from the database.
* **Summary:**<br>
    -Every row from the table represents a booking and the last column contains a "Delete booking" button;<br>
    -When a staff member clicks on the button a modal is triggered for confirmation;<br>
    -The modal asking for confirmation also displays the corresponding booking id for preventing an unwanted deletion;<br>
    -When a reservation is removed the corresponding row is immediately deleted from the table and if the list becomes empty, a suggestive message is displayed;<br>
    -When a reservation is removed, the page loads with the last date filter included, if existed one before the deletion. That creates a better user experience when managing the bookings;<br>
    -It has been tested the removal of a *booking* entry using the URL and no action is performed. Also when it was tested from a not-staff account, the custom 403(forbidden) page appears.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### REVIEWS<hr>
#### 7A: As a user, I want to see the restaurant's customer reviews on the website
* **Acceptance Criteria:**  A user should have access to a way of seeing all the reviews added on the website for creating a better idea about the offered services.
* **Summary:**<br>
    -There is a page called "Reviews" that is accessible to all types of users;<br>
    -On the page there is a list of reviews paginated to display only 4 elements at a time for a better user experience;<br>
    -Every review element has an attractive design and contains relevant details such as User name, Review text, Star rating and Date and Time of posting;<br>
    -The reviews are ordered by time in a reverse way so that the last added review is the first on the list.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 7B: As a logged in user, I want to be able to post and edit a review
* **Acceptance Criteria:** A logged in user should be provided a way of adding and editing a review for the restaurant.
* **Summary:**<br>
    -On the *Review* page there is an "Add/Edit review" section only visible for authenticated users that are not staff members, as this action wouldn't make sense for admins to make;<br>
    -For a user that hasn't already added a review to the list, there is a form to fill in for creating one;<br>
    -The form only contains an input  for the review message to be posted, and a star rating functionality was implemented with a default value of 1 star;<br>
    -There is no implementation for approval of the review because a restaurant has to have real and transparent opinions;<br>
    -When the review is posted, an alert is triggered confirming that the review was successfully added to the list;<br>
    -The response is immediate and the review appears as the first on the list;<br>
    -If the current user already added his review, it is displayed in the section "Your review";<br>
    -For editing the review, a form is displayed when the user clicks on the *Update* button;<br>
    -The form already contains the text of the review to be edited, and the Star rating feature has by default the initial value;<br>
    -When the user submits the edited review, an alert is triggered to confirm that the update was successful;<br>
    -The date and time are updated with the current ones and the review becomes first on the list;<br>
    -"Your review" section updates its values as well;<br>
    -It has been tested the updating of the current *review* entry using the URL and no action is performed. Also when it was tested for another user's review, the custom 403(forbidden) page appears;<br>
    -When a user posts a review, it also influences the displaying of the elements in the "From our clients " section on the *Home* page, where there are selected top three reviews with the best rating. <br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### CONTACT<hr>
#### 8A: As a user, I want to see the restaurant's opening and closing hours
* **Acceptance Criteria:** A site user should be provided information about opening and closing hours for every day.
* **Summary:**<br>  
    -There is a page called "Where to find us" visible to any type of user;<br>
    -The page displays a container with the timetable for every day of the week;<br>
    -The timetable has a simple and attractive design and the information is clear.<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 8B: As a user, I want to see location information on the website
* **Acceptance Criteria:** A site user should be provided information about restaurant's location.
* **Summary:**<br>
    -On the "Where to find us" page there is a google map with a marker pointed to the restaurant's location;<br>
    -Also there is an informative text with the address of the restaurant;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 8C: As a user, I want to see contact information on the website
* **Acceptance Criteria:** A site user should be provided the restaurant's contact information.
* **Summary:**<br> 
    -On the "Where to find us" page there is a section with contact information;<br>
    -The section displays the phone number and contact email for the restaurant.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### Aditional Manual Testing
#### Error Handling

* Ensure that **403 HTTP** errors display custom 403.html.
    - **Stress Test:** Input a route in the URL for accessing another user content
* Ensure that **404 HTTP** errors display the custom 404.html.
    - **Stress Test:** Input a random route in the URL that can't be found in the declared paths of the project
* Ensure that **500 HTTP** errors display the custom 500.html.
    - **Stress Test:** Set debug to false and try to access a path that has been breaked intentionally.

#### Interface Interaction

* Ensure all interactive elements respond appropriately:
    - **Desktop:**
        - All navbar elements correctly respond to hovering.
        - All buttons correctly respond to hovering.
        - All authentication links correctly respond to hovering
    - **Mobile:**
        - All navbar elements correctly respond to touch.
        - All buttons correctly respond to touch.
        - All authentication links correctly respond to touch

#### Links

* Ensure the external links to social media present in the footer open up in new tabs.

---

## Automated View Testing
### Test Overview<hr>
* **Home App**<br>
Tests applied for user stories: **1B**<br>
<img src="static/italianissimo/media/tst_home.png"><br><br>

* **Booking App**<br>
Tests applied for user stories: **3A, 3B, 5A, 5B, 6A, 6B, 6C**<br>
<img src="static/italianissimo/media/tst_booking.png"><br><br>

* **Contact App**<br>
Tests applied for user stories: **8A, 8B, 8C**<br>
<img src="static/italianissimo/media/tst_contact.png"><br><br>

* **Menu App**<br>
Tests applied for user stories: **4A, 4B, 5C**<br>
<img src="static/italianissimo/media/tst_menu.png"><br><br>

* **Review App**<br>
Tests applied for user stories: **7A, 7B**<br>
<img src="static/italianissimo/media/tst_review.png"><br><br>

### Test Coverage<hr>
For generating a report with the coverage of the automated tests, [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) module was used.<br>
The full report can be found [here]("static/reports/test_coverage.xlsx").

## Browser Testing
The website was tested on different browser for assuring the features work accordingly.
* Chrome
* Edge
* Safary
* Opera
* Firefox

## Code Validation
### HTML

The html code of the website was validated using [W3 Markup Validator](https://validator.w3.org/).<br>
At the time of deployment the validation have the following outcome:<br><br>

<img src="static/italianissimo/media/html_valid.png"><br><br>

The following pages have been tested:
* Home
* Menu
* Make a booking
* Where to find us
* Reviews
* Profile
* Manage bookings
* Login/Register
* 403/404/500 custom pages

### CSS

The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/)<br>
At the time of deployment the validation for *style.css* has the following outcome:<br><br>

<img src="static/italianissimo/media/css_valid.png" width="40%"><br><br>

### Javascript

The Javascript code was validated using using [JsHint](https://jshint.com/)<br>
At the time of deployment the validation for *script.js* has the following outcome:<br><br>

<img src="static/italianissimo/media/js_valid.png" width="40%"><br><br>

* The warnings appeared because of EventListeners added to elements in a loop.<br>
I tried to solve the issue but no successful method has been found, so I chose to ignore the warning as it is not affecting the way my code works in any way.
* The script for defining the google map present in the *Where to find us page* contains *google* and *map* variables that generate the errors in the linter. As this is a script taken from the [Google Developers Website](https://developers.google.com/maps/documentation/javascript/adding-a-google-map), I choose to ignore this issue as well as there is no fix found for it. 

### Python
The python code was tested using [PEP8](http://pep8online.com/) online validator.<br>

**Pep8 results:**<br>
<details>
<summary>Home app</summary>
* **apps.py**<br>
<img src="static/italianissimo/media/hm_app.png" width="60%"><br><br>

* **tests.py**<br>
<img src="static/italianissimo/media/hm_test.png" width="60%"><br><br>

* **urls.py**<br>
<img src="static/italianissimo/media/hm_url.png" width="60%"><br><br>

* **views.py**<br>
<img src="static/italianissimo/media/hm_view.png" width="60%"><br><br>

</details>
<details>
<summary>Menu app</summary>

* **admin.py**<br>
<img src="static/italianissimo/media/mn_admin.png" width="60%"><br><br>

* **apps.py**<br>
<img src="static/italianissimo/media/mn_app.png" width="60%"><br><br>

* **forms.py**<br>
<img src="static/italianissimo/media/mn_form.png" width="60%"><br><br>

* **models.py**<br>
<img src="static/italianissimo/media/mn_model.png" width="60%"><br><br>

* **tests.py**<br>
<img src="static/italianissimo/media/mn_test.png" width="60%"><br><br>

* **urls.py**<br>
<img src="static/italianissimo/media/mn_url.png" width="60%"><br><br>

* **views.py**<br>
<img src="static/italianissimo/media/mn_view.png" width="60%"><br><br>

</details>
<details>
<summary>Booking app</summary>

* **admin.py**<br>
<img src="static/italianissimo/media/bk_admin.png" width="60%"><br><br>

* **apps.py**<br>
<img src="static/italianissimo/media/bk_app.png" width="60%"><br><br>

* **filters.py**<br>
<img src="static/italianissimo/media/bk_filter.png" width="60%"><br><br>

* **forms.py**<br>
<img src="static/italianissimo/media/bk_form.png" width="60%"><br><br>

* **models.py**<br>
<img src="static/italianissimo/media/bk_model.png" width="60%"><br><br>

* **tests.py**<br>
<img src="static/italianissimo/media/bk_test.png" width="60%"><br><br>

* **urls.py**<br>
<img src="static/italianissimo/media/bk_url.png" width="60%"><br><br>

* **views.py**<br>
<img src="static/italianissimo/media/bk_view.png" width="60%"><br><br>

</details>
<details>
<summary>Contact app</summary>

* **apps.py**<br>
<img src="static/italianissimo/media/ct_app.png" width="60%"><br><br>

* **tests.py**<br>
<img src="static/italianissimo/media/ct_test.png" width="60%"><br><br>

* **urls.py**<br>
<img src="static/italianissimo/media/ct_url.png" width="60%"><br><br>

* **views.py**<br>
<img src="static/italianissimo/media/ct_view.png" width="60%"><br><br>

</details>
<details>
<summary>Review app</summary>

* **admin.py**<br>
<img src="static/italianissimo/media/rv_admin.png" width="60%"><br><br>

* **apps.py**<br>
<img src="static/italianissimo/media/rv_app.png" width="60%"><br><br>

* **forms.py**<br>
<img src="static/italianissimo/media/rv_form.png" width="60%"><br><br>

* **models.py**<br>
<img src="static/italianissimo/media/rv_model.png" width="60%"><br><br>

* **tests.py**<br>
<img src="static/italianissimo/media/rv_test.png" width="60%"><br><br>

* **urls.py**<br>
<img src="static/italianissimo/media/rv_url.png" width="60%"><br><br>

* **views.py**<br>
<img src="static/italianissimo/media/rv_view.png" width="60%"><br><br>

</details>
<details>
<summary>Users app</summary>

* **admin.py**<br>
<img src="static/italianissimo/media/us_admin.png" width="60%"><br><br>

* **apps.py**<br>
<img src="static/italianissimo/media/us_app.png" width="60%"><br><br>

* **models.py**<br>
<img src="static/italianissimo/media/us_model.png" width="60%"><br><br>

</details><br>

* Although there is no code line greater than 100, there are a few errors of type "Line too long" that I decided to ignore because it would mean breaking the code in a way that would make it difficult to read. 

### Accesibility 
The accesibility of the website was tested with [Wave](https://wave.webaim.org/)

**Wave results:**<br>
<details>
<summary>Home page</summary>
<img src="static/italianissimo/media/wv_home.png" width="60%"><br><br>
</details>
<details>
<summary>Menu page</summary>
<img src="static/italianissimo/media/wv_menu.png" width="60%"><br><br>
</details>
<details>
<summary>Where to find us page</summary>

* The error on this page is caused by the "Image map area missing alternative text".<br>
As the google map is built of multiple images without an alt attribute, I didn't find a proper way to add the attribute to all of them, as I also consider the error message to be confusing about which image it is targeted.<br>
<img src="static/italianissimo/media/wv_contact.png" width="60%"><br><br>
</details>
<details>
<summary>Reviews page</summary>
<img src="static/italianissimo/media/wv_reviews.png" width="60%"><br><br>
</details>
<details>
<summary>Profile page</summary>
<img src="static/italianissimo/media/wv_profile.png" width="60%"><br><br>
</details>
<details>
<summary>Manage bookings page</summary>
<img src="static/italianissimo/media/wv_manage.png" width="60%"><br><br>
</details>
<details>
<summary>Login page</summary>
<img src="static/italianissimo/media/wv_login.png" width="60%"><br><br>
</details>
<details>
<summary>Register page</summary>
<img src="static/italianissimo/media/wv_register.png" width="60%"><br><br>
</details><br>

### Performance
The performance of the website was tested with [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)

**Lighthouse reports:**<br>

<details>
<summary>Desktop</summary>

* Home page<br>
<img src="static/italianissimo/media/dsk_home.png" width="60%"><br><br>

* Menu page<br>
<img src="static/italianissimo/media/dsk_menu.png" width="60%"><br><br>

* Booking page<br>
<img src="static/italianissimo/media/dsk_booking.png" width="60%"><br><br>

* Where to find us page<br>
<img src="static/italianissimo/media/dsk_contact.png" width="60%"><br><br>

* Reviews page<br>
<img src="static/italianissimo/media/dsk_reviews.png" width="60%"><br><br>

* Profile page<br>
<img src="static/italianissimo/media/dsk_profile.png" width="60%"><br><br>

* Manage bookings page<br>
<img src="static/italianissimo/media/dsk_manage.png" width="60%"><br><br>

* Login page<br>
<img src="static/italianissimo/media/dsk_login.png" width="60%"><br><br>

* Register page<br>
<img src="static/italianissimo/media/dsk_register.png" width="60%"><br><br>
</details>

<details>
<summary>Mobile</summary>  

* Home page<br>
<img src="static/italianissimo/media/mb_home.png" width="60%"><br><br>

* Menu page<br>
<img src="static/italianissimo/media/mb_menu.png" width="60%"><br><br>

* Booking page<br>
<img src="static/italianissimo/media/mb_booking.png" width="60%"><br><br>

* Where to find us page<br>
<img src="static/italianissimo/media/mb_contact.png" width="60%"><br><br>

* Reviews page<br>
<img src="static/italianissimo/media/mb_reviews.png" width="60%"><br><br>

* Profile page<br>
<img src="static/italianissimo/media/mb_profile.png" width="60%"><br><br>

* Manage bookings page<br>
<img src="static/italianissimo/media/mb_manage.png" width="60%"><br><br>

* Login page<br>
<img src="static/italianissimo/media/mb_login.png" width="60%"><br><br>

* Register page<br>
<img src="static/italianissimo/media/mb_register.png" width="60%"><br><br>
</details><br>

Back to [README.MD](README.MD)<br>
 

