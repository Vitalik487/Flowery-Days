# Flowery Days

Ongoing research in the field of botany seems to indicate delightful things about flowers:
- Flowers can help heal the common cold.
- Flowers can help improve mood.
- Flowers improve memory.
- Flowers aid relaxation.
- Flowers increase energy.

[Flowery Days]() is an online flower shop, that offers not only flower bouquets, but also a bunch of individual flowers so that customers can create arrangements by themselves.  
The shop also publishes blog posts about flower arrangements, gardening and flowers/plants, where the site visitors can leave a comment.

<p align="center"><img src = "" width=900></p>

## Table of Contents

1. [UX](#ux)
    - [Project Goals](#goals)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Home page](#home-page)
        - [Page for registering a name and an event key](#page-for-registering-a-name-and-an-event-key)
        - [Page for registering details of the event](#page-for-registering-details-of-the-event)
        - [Page for getting a shareable link](#page-for-getting-a-shareable-link)
        - [Page for participants](#page-for-participants)
        - [Page for restoring an existing plan](#page-for-restoring-an-existing-plan)
    - [Features Left to Implement](#features-left-to-implement)
        - [Delete the data after the event date is passed](#delete-the-data-after-the-event-date-is-passed)
    - [Defensive Design](#defensive-design)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#database-modeling)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Tools](#tools)
    - [Databases](#databases)

5. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)

6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)


# UX
## Project Goals
### Target Audience
- 

### Visitor / User Goals
-

### Business Goals (Site Owner's Goals)
-

## User Goals
The target audience for this website is:
1. The site owner who wants to open an online shop where customers can purchase products safely
2. People who are interested in buying flowers and gardening products
3. People who are interested in gaining flower decoration and gardening tips and inspirations

The user goal is to have:

## User Stories

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper     | Easily see what services are offered | Find the service I want to use |  
| Shopper     | All the important services are accesible from nav bar| Don't need to scroll to find important information | 
| Shopper     | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 

<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Easily register for an account | Have a personal account and be able to view my profile and ability to check order history |  
| Site User | Easily recover my password in case I forget it | Recover access to my account | 
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful | 
| Site Owner | Post a blog about flower arrangement and gardening | Give site visitors interesting information of flowers | 
| Site Owner | Let the site users log in when they leave comments/reviews | Track who left comments/reviews | 
| Site User | Add comments to the blog posts | Write down my thoughts to the post | 

<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Search a product with keywords | Find the most appropriate products |  
| Shopper | Order the search results with the prices | Find the most appropriate products for the target price range | 
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing | 
| Shopper | Filter with a specific category of product | Easily find products in a specific category | 
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular by the other customers | 
| Site Owner | Easity add a new product | Make sure the online site has the latest lineups | 

<br/>

- Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product and the quantity |  
| Shopper | Automatically suggest to log in if I did not log in, when proceeding with checkout | Smoothly proceed with my purchase | 
| Shopper | See the purchase steps | Understand what process I am at in the purchase | 

<br/>

## Design
### Wireframes
Wireframes were created with [balsamiq](https://balsamiq.com/).
You can find the wireframes [here](https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/wireframe.md).

### Brand Identity of The Shop


### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below. 
<img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/readme_materials/Colorpalette.png" width=900>

This pallet collects the earthy tones with luxuary shades, which the shop aims to have their brand image for. The `Twilight Lavender` and `Popster` colors give the site an elegant and vibrant atmosphere with keeping harmonies with the flowers. The `Champagne Pink` fills the gap between white and the other vivid colors, while giving the calm shades.

### Typography
To refrect the flower shop's brand identity, the typeface `Playfair Display` by Claus Eggers Sørensen that falls under serif font family was chosen for the website unless there is any additional specific font setting. `Playfair Display` font has a mood of Elegance, Vintage, Classy and Stylish which matches the shop's branding. As per [this article](https://medium.com/@manahabibian/playfair-display-a-typographic-specimen-b311856700bd) on Medium.com by Mana Habibian, “Playfair Display is a classical typeface with a modern feeling that will give designs the elegance they need.”

### Brand Logo


# Features

## Existing Features
### Home page
- 

### Page for registering a name and an event key
- 

### Page for registering details of the event
- 

### Page for getting a shareable link
- 

### Page for participants
- 
- 

### Page for restoring an existing plan
- 

## Features Left to Implement
### Delete the data after the event date is passed
- 

## Defensive Design
-  
- 


# Information Architecture
## Database Choice
## Data Modeling


# Technologies Used
This application contains key CRUD functionalities and they are used to maximize user's experience in this site. The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Flask.

## Languages 
- HTML, CSS, JavaScript, Python

## Libraries
- Bootstrap (v4.4.1)
- JQuery
- JQuery-UI
- Popper.js
- Font Awesome
- Flask
- Jinja
- PyMongo

## Tools
- Git/GitHub
- Gitpod
- PIP
- MongoDB Atlas

## Databases


# Testing
### Validation Tools
I used these validation tools below for each file.
- HTML: [W3C HTML Validator](https://validator.w3.org/)
- CSS: [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
- JavaScript: [JSHint](https://jshint.com/)
- Python: [PEP8 online](http://pep8online.com/)

### Formatter
- HTML: [HTML Formatter](https://webformatter.com/html)
- CSS: [CSS Formatter](https://webformatter.com/css)
- JavaScript: [Online JavaScript Beautifier](https://beautifier.io/)
- Python:[PEP8 online](http://pep8online.com/)

### Manual Testing

### Bugs
#### Python and Database
- 

#### JavaScript
- 

#### Browser Compatibility
- 
# Deployment
## Local Deployment
For local deployment, you need to have an IDE such as Gitpod and you need to install the following in your IDE:
- Git, Python3, PIP3

1. At the top of this repository, click the green button **Clone or download**.
2. In the Clone with HTTPs section, copy the clone URL for the repository. 
3. Open your favourite terminal (cmd, powershell, bash, git bash, etc.)
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type `git clone`, and then paste the URL you copied in Step 2:
   `git clone https://github.com/AsunaMasuda/MilestoneProject3.git`
6. Press Enter. Your local clone will be created.
7. You can either 
    - Create a virtual environment and create environment variables of IP, PORT, MONGO_URI and SECRET_KEY.
    - Or edit the app.py file like the following variables:
        ```
        'IP', '127.0.0.1'
        ```
        ```
        'PORT', '5000'
        ```
        ```
        'SECRET_KEY', '<somethingsecret>'
        ```
        ```
        'MONGO_URI', 'mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority'
        ```
8. Install all required modules from requirements.txt with the command`pip3 install -r requirements.txt`
9. Now you can run the website with the command `python3 app.py`
10. You can now access the website at **http://127.0.0.1:5000**

## Heroku Deployment
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Create a requirements.txt file using the command `pip3 freeze > requirements.txt` in the terminal.
2. Create a Procfile using the commant `echo web: python app.py > Procfile` in the terminal.
3. Commit and push all the changes to the Github repositoty of this project.
4. Go to Heroku and create a new app. Set a name for this app and select the closest region.
5. Choose Deployment method as GitHub in Heroku Dashboard and link the Github repository to the Heroku app.
6. Go to Settings then Reveal Config Vars in Heroku Dashboard and set the values as follows:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
SECRET_KEY | `<your_secret_key>`


# Credits

## Content
- All text within this project was written by the developer.

## Media
### Icons
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).
- Favicon is made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Images
- The favicon for this site is provided by [flaticon](https://www.flaticon.com/)

### UX
- 

### JavaScript
- 

## Acknowledgements
- Thanks to: my Code Institute Mentor Guido Cecilio Garcia Bernal for his advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.
