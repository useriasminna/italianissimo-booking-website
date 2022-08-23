# Italianissimo - Booking Website
<img src="static/italianissimo/media/responsive.jpg" width="60%"><br>
<hr>

## Overview
This is a project designed and developed to create a complete experience for the clients of Italianissimo Restaurant. The users are given the possibility to create a booking, post a review and mark their favourite meals, and the staff members dispose of an online system for managing all the bookings. All these functionalities can be accessed by any user with an account, considering that the staff members have special permissions for controlling the data. <br>
The website was created for real-life situations, but the restaurant name is fictive.<br>
**Italianissimo - booking website** was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
<br><br>
The fully deployed project can be accessed at [this link](https://italianissimo-booking-website.herokuapp.com/).<br><br>

## UX<hr>
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a menu so I can easily navigate through website content |             
|                                       |1B| As a user, I want to see relevant information about the restaurant|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the restaurant's theme|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to logout at any time|
|**BOOKING**                            |  ||
|                                       |3A| As a logged in user, I want to be able to find the available tables for a specific date and time|
|                                       |3B| As a logged in user, I want to be able to select the table that I want to reserve|
|**MENU**                               |  ||
|                                       |4A| As a user, I want to see the restaurant's menu with details about ingredients and price, so that I can be completely aware of everything I want to order|
|                                       |4B| As a logged in user, I want to be able to mark my favorite dishes on the menu|
|**USER PROFILE**                       |  ||
|                                       |5A| As a logged in user, I want to view a list of my upcoming bookings|
|                                       |5B| As a logged in user, I want to be able to  cancel my bookings|
|                                       |5C| As a logged in user, I want to see a list with my favorite dishes of the restaurant|
|**STAFF MANAGE BOOKINGS**              |  ||
|                                       |6A| As a logged in staff member, I want to see the restaurant's upcoming bookings for the current day sorted by time|
|                                       |6B| As a logged in staff member, I want to be able to filter bookings by date|
|                                       |6C| As a logged in staff member, I want to be able to cancel bookings|
|**REVIEWS**                            |  ||
|                                       |7A| As a user, I want to see the restaurant's customer reviews on the website|
|                                       |7B| As a logged in user, I want to be able to post and edit a review|
|**CONTACT**                            |  ||
|                                       |8A| As a user, I want to see the restaurant's opening and closing hours|
|                                       |8B| As a user, I want to see location information on the website|
|                                       |8C| As a user, I want to see contact information on the website|

**Project Goal:**<br>
Create a website for the Italianissimo restaurant that is usefull for clients and staff members as well.

**Project Objectives:**<br> 
* To create a website with a simple and intuitive User Experience;
* To add content that is relevant and helps create a better image of the restaurant;
* To differentiate between client and staff member accounts;
* To implement fully functional features that will ease the staff members' tasks and upgrade clients' experience with the restaurant services;
* To make the website available and functional on every device.<br><br>

### Scope<hr>
**Simple and intuitive User Experience**<br>
* Ensure the navigation menu is visible and functional at every step;
* Ensure every page has a suggestive name that fits its content;
* Ensure the users will get visual feedback when navigating through pages;
* Create a design that matches the restaurant theme and does not confuse the users.

**Relevant content**<br>
* Add information about restaurant name, location and contact data;
* Make a clear and beautiful designed presentation of the menu elements;
* Create a section with the most ordered dishes;
* Create a section with customer reviews for full transparency.

**Features for upgraded experience**<br>
* Create a Booking feature that allows the users to see all the tables available for a specific date and time:
* Create a Menu feature that displays all the menu information and gives the possibility for the user to mark his favourite dishes;
* Create a Review feature that displays all the reviews added and gives the possibility for the user to add and edit his review;
* Create a Profile page for the user to see his upcoming bookings and favourite meals;
* Create a page for the staff member to manage all the bookings for all the users;

**Different client and staff member Accounts**<br>
* Permit the client to add/edit reviews and the staff member only the option to read them;
* Give the client permission to mark favourite meals and remove the option for staff members;
* Allow access to Profile page only for client type of users;
* Allow access to Manage Bookings page only for staff members type of users;

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>

### Structure<hr>
The structure of the website is divided into nine pages but with content depending on authentication and client/staff status <br>
-**Register/Login** pages give the user the possibility to create an account and authenticate for accessing different features.<br>
-**Logout** feature is a modal that helps user exit their current account;<br>
-The **Home** page is visible for both types of users and includes details about the restaurant, most appreciated dishes and top reviews;<br>
-The **Menu** page displays menu details and the "Add to favourite" option only for logged-in clients;<br>
-The **Booking** page is only available for logged-in users, both clients and staff members;<br>
-**Where to find us** contains information visible to all users;<br>
-The **Reviews** page displays all existent reviews and the "Add/Update review" option only for logged-in clients;<br>
-**Profile** page is only visible for the logged-in clients and displays "Upcoming bookings" and "Favourite dishes" sections;<br>
_**Manage Bookings** page gives access only to staff members and displays all the bookings registered, grouped and filtered by day.<br>

* FLOWCHARTS
The Flowchart for my program was created using <b>LucidChart</b> and it visually represents how the system works.<br>
[![N|Solid](static/italianissimo/media/flowchart.png)](static/italianissimo/media/flowchart.png)<br><br>


### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here](static/italianissimo/wireframes/wireframes.pdf)<br>

**Database**<br>
The project uses the PostgreSQL relational database for storing the data.<br>
There were created two diagrams to represent the relation between the tables, the initial one and the final one.
The first one was created before the actual development of the website which led to some changes to the attributes and tables for finding the most relevant and useful ones to be kept.

<details>
  <summary>Initial Schema</summary>
<img src="static/italianissimo/media/initial_db.jpeg" width="80%"><br>
</details>

<details>
  <summary>Final Schema</summary>
<img src="static/italianissimo/media/final_db.jpeg" width="80%"><br>
</details><br><br>

### Surface<hr>
### SURFACE<br>
#### Color Scheme
All the colours were selected with the eyedropper plugin from the website cover, to maintain the chromatic harmony. <br>
* The primary colour scheme was used for most of the text existent on the website, in either dark or bright colours for creating a good contrast.<br> 
<img src="static/italianissimo/media/clr2.png" width="18%">
<img src="static/italianissimo/media/clr3.png" width="18%">
<img src="static/italianissimo/media/clr4.png" width="18%">
<img src="static/italianissimo/media/clr1.png" width="18%"><br>

* The seconday colour scheme was used for buttons, warnings, errors or for highlighting some important information.<br>
<img src="static/italianissimo/media/clr5.png" width="18%">
<img src="static/italianissimo/media/clr6.png" width="18%">
<img src="static/italianissimo/media/clr7.png" width="18%">
<img src="static/italianissimo/media/clr8.png" width="18%">

#### Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
**Body:** Tiro Devanagari Marathi, serif<br>
**Navbar:** Courgette, cursive<br>
**Logo:** Cinzel, serif<br>
**Slogan:** Marck Script, cursive<br>

#### Visual Effects
* Box shadows
Multiple box shadows were used for cover, buttons and images. They were inspired from [css-box-shadow-examples]("https://getcssscan.com/css-box-shadow-examples")<br>
* Animation
Some animations were used for creating a dinamic and atractive design
<details>
  <summary>View Moving arrows animation</summary>
<img src="static/italianissimo/media/arrows-capture.gif"><br>
</details>
<details>
  <summary>View Authentication links Pulse animation</summary>
<img src="static/italianissimo/media/pulse-capture.gif"><br>
</details>

* Hover effects
<details>
  <summary>NavBar elements hover</summary>
<img src="static/italianissimo/media/nav-capture.gif"><br>
</details>
<details>
  <summary>Buttons hover</summary>
<img src="static/italianissimo/media/delete-capture.gif"><br>
</details>
<details>
<summary>Footer elements hover</summary>
<img src="static/italianissimo/media/footer-capture.gif"><br>
</details>




### Agile Methodology<hr>
## Features<hr>
### Existing Features<hr>
### Future Feature Considerations<hr>
## Technologies Used<hr>
## Testing<hr>
## Deployment<hr>
## Credits<hr>
### Content<hr>
### Media<hr>
### Code<hr>
## Acknowledgements<hr>
