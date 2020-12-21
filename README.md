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
        - [](#)
        - [](#)
        - [](#)
        - [](#)
        - [](#)
        - [](#)
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

### Brand Identity
- Vision: Beautiful life surrounded by natures and flowers with your creativities.
- Mission: Provide a wide range of bouquets and flower arrangements that suit special occasion and moments in life which can be purchased with one click online. Be a wholesaler of individual flower bunches so the customers can enjoy flower arrangements themselves, without hassle to go to a physical shops.
- Values: 1.Happiness - Improve your happiness with the power of natures, 2.Elegance - Appreciate everything around you in everyday life, 3.Nature - Inspired by the natural world and its beauty, 4.Creative - Express your creativity in flower arrangements

### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below. 

<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/readme_materials/Colorpalette.png" width=900></p>

This pallet collects the earthy tones with luxuary shades, which the shop aims to have their brand image for. The `Twilight Lavender` and `Popster` colors give the site an elegant and vibrant atmosphere with keeping harmonies with the flowers. The `Champagne Pink` fills the gap between white and the other vivid colors, while giving the calm shades.

### Typography
To refrect the flower shop's brand identity, the typeface `Playfair Display` by Claus Eggers Sørensen that falls under serif font family was chosen for the website unless there is any additional specific font setting. `Playfair Display` falls under a classic typography called 'serif' font family which is great to be used when you want your brand to appear trustworthy and traditional. `Playfair Display` font has a mood of Elegance, Vintage, Classy and Stylish which matches the shop's branding. [This article](https://medium.com/@manahabibian/playfair-display-a-typographic-specimen-b311856700bd) by Mana Habibian says “Playfair Display is a classical typeface with a modern feeling that will give designs the elegance they need.”

- Icon: [FontAwesome]() is used for the main icon library accross the site.
- Favicon: I got the favicon by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Brand Logo
Logo design is the cornerstone in your brand identity and logo presents a company's name, product and brand. I used [Canva](https://www.canva.com/en_gb/) to create brand logo file. The font represents the brand value `elegance` and the image of a branch at the top was added to represent `Nature` brand value. 
<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/static/img/home/logo_flowery_days.png"></p>

<div "text-align: right;"><a href="#table-of-contents">Back to top</a></div>

# Features

## Existing Features
Flowery Days website is composed of 6 application: `home`, `blog`, `cart`, `checkout`, `products`, `profiles`.

## Landing Page (Home)
Landing Page is designed as a single page website to provide with enough information for the site visitor to understand what the business is about on this site. This page has minimal amount of information to make the site visitors make decisions and take next actions. The page compose of `Navbar`, `Carousel`, `About`, `Why Choose Us?`, `testimonials` and `Contact Form` section. As scrolling down on thie page, the elements are smoothly being placed by [Animate.css](https://animate.style/) and [wow.js](https://wowjs.uk/docs) animation effects to give a dynamic and sophisticated experience to the site visitors.

### Navbar
When site visitors landed on the page, the hight of the navbar is set as "165 px". I wanted to make the whole brand logo visible to make it memorable because the first view of the page is important that gives the first impressions of the site to the users. If you scroll down the navbar shrinks to the height of "100 px" and sticks at the top of the view, for easy navigations and wider views of content on the landing page. The brand logo which is placed at the left top also becomes the branch icon. 

Navbar contains a site menu, a `Search Box`, `Login button`, `Sign Up button`, `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `descriotion` field of Product Model, `name` field of Color Model and `name` field of Flower Model.(Details of these models will be described at the [Information Architecture](#information-architecture)) This function uses "OR" condition not "AND" when searching the keywords, meaning, if the search query was "Tulip Rose", the search result shows the product found using the keyword "Tulip" OR "Rose". Searching with "OR" condition is chosen in order not to limit the possibilities for the products the potential customers want to purchase.


### Carousel
At the top of the landing page, I placed carousels with beautiful photos of the flowers and the messages. This area is called "Above the fold" area and site visitors engage more with the content in "Above the fold".

### About Us & Why Choose Us?
`About Us` section explains what the business is and the history of the shop briefly to the site visitor.
`Why Choose Us?` section showcases three sales points of the shop presenting with icons.
Those two sections use the color of `Popstrat` and `Champagne Pink` from the color pallete for its background color that seamlessly matches the next section's background.

### Testimonial
A customer testimonial section can contribute to building the trust of potential customers and also explain the benefits of your products or services. This section displays different customer's testimonials with smooth carousel auto-animation effects.

### Contact Form
A simple contact form is placed at the end of the landing page. Site visitors fill out (name, email, subject, message) when submitting the form. An email with the inquery from the form will be sent to the admin of the website (handling by django send_mail() functionality).

### Footer
The footer section consists of two parts: 1. General information of the Shop and Quick Link, 2. Social Media icons and credit
1. The first footer section includes the shop address and its opening hours and quick links to the pages within the site.
2. In this milestone project, Social Media icons are linked to my personal social media accounts, but in real settting they should be linked to business pages on social media, such as Facebook, Instragram, Twitter, Pinterest etc, for social media marketing purposes.

## Product Page
### Online Shop Page
By clicking 'Online Shop' on the site menu, you can go to the online shop page. This page is filtered with 'Bouquet' category as a default as the shop owner wants to promote products that fall uner Bouquet category that has higher profit. However, the site visitor can adjust the filter condition very easily.  
- `Filter Function`: There is a filter section at the left side of the online shop page, and you can filter products with `categories`, `color`, `flower` and `occasion/use`. You can also select multiple choices within the filter option same and use several filters to get the results.(e.g. you can choose white and red for the color option and choose tulip and rose for the flower option. In this case, the result will show the products that fall under (white OR red color) AND (tulip OR rose).) I designed the filter to this way in order not to narrow down the products the potential customers are looking for.
- `Result Number`: It's shown above the product cards. Customers can see how many results were found in total at a glance.
- `Product Card`: The products are displayed in cards that have `Product Name`, `Price`, `Unit`, `Add to Card` button and `View Details` button when hoverovering the product image. If the user is logged in as a superuser, Edit / Delete option is also shown on each card. 
- `Pagination Bar`: At the bottom of this online shop page, I've set a pagination bar for easy navigation when there are many results to show. Setting up a pagination bar and limiting the number of the products reduce the loading time and make the site look more organized, which is crutial for a site like online shop which offers many products. 

### Product Detail Page
- `Breadcrumb` navigation is added at the top of the product detail page, which allows customers to keep track their locations in the onlineshop.
`Product Image`: On the left side of the product detail page (single_product.html), the product images are shown. When there are several images for the product , for example, some products have color options such as Carnation, the options will be shown under the main image.
- `Product Information`: On the right side of the product detail page, there is `Product Name`, `Price`, `Description`, `Color` option, `Quantity`, `Add to Cart` button. `Color` option is only visible when the product has the options. Also for superuser, Edit / Delete option will be shown.
- `Product Review Section`: Customers can see the product scores and review messages by the other customers. The users can leave a score from 1 to 5, and the average of the scores by the customers is shown on the product page. To leave product review, the user is asked to log in their account. Also, to delete a review, the customer who left the review needs to log in and the delete option will be visible next to the review after logging in. At the moment, regardless of the history of purchasing the product the user wants to review for, the user is able to leave a review. This is one of the features left to implement to limit only the user who actually purchased the product to be allowed to review.

## Cart Page
- The left side of this cart page shows the products added to the cart. Customers are able to change the quantity or remove the product from the cart in this cart page. 
- On the right side of this cart page, there is Order Summary section that shows `Cart Total`, `Delivery` and `Grand Total`. This way, customers are able to check the order summary at first glance even if they have added a lot of products to the shopping cart.

## Checkout Page
### Checkout Page
- On checkout page, customers are asked to fill out delivery details. The customer also can select if they want gift wrapping to the product or not. At the moment, this shop does not collect user's billing information to the User Profile model or Order model.(However, the billing data is recorded in Stripe from the billing information added by the customer.) One of the features left to implement is add the billing details on Checkout page.
- Thought the customer can complete the checkout process without having an account, if the customer hasn't logged in, the message "Create an account or login to save this information" is shown at the checkout page.

### Checkout Success Page
- Thank you message will be displayed after the checkout process as well as the table that holds the order details.
- `Keep Shopping` button is placed at the end of the page, and if the customer has been logged into their account `Back to Profile` will be shown.

## Blog Page
### Blog Feed Page
- After clicking `Blog` on the site menu at the top, Blog Feed page is loaded. On this page, blog posts will be displayed in decending order by the posted date. To display the blog posts beautifully, the layout that shows posts in 2-1-2 order was chosen. `Pagination Bar` is also added at the end of the page.
- On the left side of this page, I create categories of blog posts so the site visitors can navigate the blog posts easily. The number of posted blogs in the categories is also shown in the round brackets. 

### Blog Post Detail Page
- `Breadcrumb` navigation is added at the top of the blog post detail page, for the easy navagation.
- `Leave Comment` function: Site visitors are able to leave comments to the blog posts. It requirs the visitors to log into their account to do so. Also, after logging in, they can delete comments they left in the past with the delete option shown next to the past comment.
- To post a new blog article, the admin has to go to the Django Admin site. One of the features left to implement is add a page in the site itself where the admin is able to post a new article without accessing Django Admin site.

## Profiles Page
`My Profile` page is available for authenticated users and will be shown in the `My Account` Dropdown menu at the navbar which appears when you log into your account.
### My Profile Page
- In Profile Page, authenticated users can 1. edit `Delivery Information` and 2. see `Order History`. 

## Admin product managment

## Django-allauth features

## Features Left to Implement
There are some of features left to implement in the future which I could not add to this project this time due to the time constraints. These features are great to be added for more complete online shop service for gaining higher customer satisfactions in the site. 
### 1. Limit the user who can leave product review
At the moment, all the authenticated users can leave reviews to any products if they are logged in. It should be limited to those who actually purchased the product for the validity of the reviews.
### 2. Add an option to let the customer add their billing information
With the current checkout process, the user is asked to fill out delivery information. Billing information is required when the customer wants a receipt or when a billing address is different from a delivery address.
### 3. Post Blog article through the site
At the moment, the site owner/admin has to use Django Admin to post a new blog article. However, it would be better usability if they could post them on the site.
### 4. When a color was selected on a product page, the product image also changes accordingly
At the moment, even though the color options and images for each color are shown on its product page, these two are not changed if the other is changed. It will be more ideal the action of those two elements is synced.
### 5. Social Account Login
This function allows users to sign up / log into their account of the site, using the existing account such as Google and Facebook. This is beneficial to users and the site ownwers. For users, it's hassle free from remembering a password for the site and it gives the users a smooth registration process. For the site owners, there are many benefits gained by social login - such as increasing user's sign up, reducing bounce rate and gaining user's information for social account which is beneficial for marketing purpose.

## Defensive Design
### Error views (404 and 500 error)
If 404 and 500 error occured within the site, a page that has the message of the error and 'Back to Home' button so that the user would not be lost. The templates of 404.html and 500.html are added to [the root template directory].(https://docs.djangoproject.com/en/3.1/ref/views/))

### Form Validation
- Django Form Validation

### Product Quantity Counter Validation


# Information Architecture
## Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

## Data Modeling
Following is Entity Relationship Diagram of this project. I created this diagram with [dbdiagram.io](https://dbdiagram.io/home).
<p align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/Entity_Relationship_Diagrams.png?raw=true" width=900></p>

### Product App
A bouquet could have several types of flowers and multiple colors. For example, below the product 'Floral Fantasy' has `Delphinium`, `Rose`, `Tulip` and `Tistle` for its flowers and it can be categorized as `Red` and `Orange`. To give customers a better search experience, meaning not to narrow down the search results with the search keyword, I wanted to enable customers to search/filter bouquets with their flower type(name) or their color. For example, if a customer uses a filter `tulip`, bouquets that contains `tulip` (such as the 'Floral Fantasy') and also individual tulip flower product (not bouquet) will be shown. Therefore, separated models `Product`, `Flower`, `Color` are created and connected inbetween. `Image` model is connected to `Product` model because some products could have several product images. Also `Image` model is connected to `Color` model, because each product image should a product that could have mutiple colors. There might have been a better implementation than this scheme, but at the time, this was the best idea I had.
<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/readme_materials/Product_model.png" width=900></p>

### Order App
`Order` model collects the delivery information, stripe_pid and order information. All the fields except `user_profile` field have `null=false`. The reason why `user_profile` does not have `null=false` is that guest customers (not authenticated users) can also purchase products and complete the checkout process without creating an account. `Order` model is connected to `OrderLineItem` model which collects information of purchased products.

### Blog App
`BlogPost` model has the essential information for blog post, such as a title, author, content, created date. This model is connected to `User`, `BlogImage` and `BlogComment`.

### Profile App
`Profile` is used for my profile page where the authenticated users can see their delivery details and their order history.


# Technologies Used
The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Django.

## Languages
- HTML, CSS, JavaScript, Python

## Libraries and Packages
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v4.4.1)](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [JQuery-UI](https://jqueryui.com/)
- [Popper.js](https://popper.js.org/)
- [Font Awesome](https://fontawesome.com/)
- [Animate.css](https://animate.style/)
- [Wow.js](https://www.delac.io/wow/)
- [Stripe](https://stripe.com/ie)
- [Google Fonts](https://fonts.google.com/)

## Tools
- Git/GitHub
- Gitpod
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [dbdiagram.io](https://dbdiagram.io/home)
- [coolors.co](https://coolors.co/)

## Databases
- [SQlite3](https://www.sqlite.org/index.html)- database used for development.
- [PostgreSQL](https://www.postgresql.org/) - database used for production.

# Testing
Manual Testing and Automated Testing can be found in [this article]().

## Code Valication and Formatting 
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

# Deployment
## Heroku Deployment
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Create a `requirements.txt` file using the command `web: gunicorn flowery_days.wsgi:application` in the terminal.
2. Create a `Procfile` using the commant `echo web: python app.py > Procfile` in the terminal.
3. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
4. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
5. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Provision** button to add it to your project.
6. In the heroku dashboard for the application, click on "Setting" > "Reveal Config Vars" and set the values as follows:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
SECRET_KEY | `<your_secret_key>`

## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS

1. In the IDE you are using, copy and paste the following commane into the terminal
    `git clone https://github.com/AsunaMasuda/FloweryDays.git`
The other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
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

# Credits

### Content
- All text within this project was written by the developer.

### Code
- 
- 

### Icons
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).
- Favicon is made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Images
- The favicon for this site is provided by [flaticon](https://www.flaticon.com/)

### UX
- 

### Acknowledgements
- Thanks to: my Code Institute Mentor Guido Cecilio Garcia Bernal for his advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.

### Disclaimer
This website is created for educational purpose only.
