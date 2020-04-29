# XYfitness

![Hero Image](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/hero.PNG?raw=true)

[![Build Status](https://travis-ci.org/brianscan14/XYfitness.svg?branch=master)](https://travis-ci.org/brianscan14/XYfitness)

XYfitness acts as a portal for an aspiring personal fitness or **"PT"** trainer to display their talents or capabilities to the general public, and potentially attract new clients. Whether this results in them purchasing a plan for exercise or routine to follow, or even if they purchase an item of clothing. This results in a revenue stream for the PT and means of getting their product out on the market and their clientele growing in stature. It is  means of them showing off their talents, their results and their approach for all to see.

Users are encouraged to sign up to the website in order to create a profile, this will allow them to purchase products, leave reviews and the usual profile features by being able to edit their picture, password and add additional details such as first name, email, etc. However the user can still browse many parts of the page freely without needing an account, this is the encourage freedom of the site and to get the user to browse it more and get a feel for it, without being put off by having to sign in straight away. In order to purchase any products the user will then need to create an account. 

## Table of Contents

- [UX](#ux)
  * [User Stories](#user-stories)
  * [Color Scheme](#color-scheme)
- [Wireframes](#wireframes)
- [Technologies](#technologies)
  * [Languages Used](#languages-used)
  * [Databases](#databases)
  * [Front End](#front-end)
  * [Back End](#back-end)
- [Features](#features)
  * [*Elements common to all pages*](#-elements-common-to-all-pages)
    + [Navbar:](#navbar)
    + [Footer:](#footer)
    + [Scroll Top button:](#scroll-top-button)
    + [Search Overlay:](#search-overlay)
  * [Home Page](#home-page)
    + [Hero Image](#hero-image)
    + [Info Section](#info-section)
    + [Testimonials slideshow](#testimonials-slideshow)
    + [Social Media](#social-media)
    + [Mission Statement](#mission-statement)
  * [About page](#about-page)
  * [All products page](#all-products-page)
  * [Single product view](#single-product-view)
  * [All Testimonials](#all-testimonials)
  * [Single Testimonial View](#single-testimonial-view)
  * [Contact](#contact)
  * [Profile](#profile)
  * [Cart](#cart)
  * [Checkout](#checkout)
    + [Delivery Details:](#delivery-details)
    + [Payment Card Details:](#payment-card-details)
    + [Order Confirmation:](#order-confirmation)
  * [Account](#account)
  * [Login / Logout](#login---logout)
  * [Register](#register)
- [Features to implement](#features-to-implement)
- [Information Architecture](#information-architecture)
  * [Database](#database)
  * [Data Structure](#data-structure)
    + [Accounts](#accounts)
    + [Checkout](#checkout-1)
    + [Pages](#pages)
    + [Products](#products)
    + [Testimonials](#testimonials)
- [Testing](#testing)
- [Deployment](#deployment)
  * [*Run project locally:*](#-run-project-locally)
  * [*Heroku Deployment:*](#-heroku-deployment)
- [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
  * [Acknowledgments](#acknowledgments)
  * [Disclaimer](#disclaimer)

## UX

The main goal of the website is to convince customers that this is the PT that they need, and that his plans are the best ones to get on the market. This is accomplished by a combination of a sleek, professional design and many reviews and testimonials from current customers to persuade the user to use this PT. The pages are kept sleek and interactive so as to allow the user to easily navigate around the site.  The navbar at the top enkeeps with this theme and allows the users to navigate to each page with ease, decreasing to a menu icon on smaller screen sizes.

The **hero image** on the index page take up the entire and lets the user know the purpose of the site straight away, grabbing their attention. If the user just wants to search a product quickly then they can utilise the **search icon** in the navbar which calls an overlay that has a search bar, which searches the DB for names matching the string inputted by the user. The user can also easily navigate to the **about** or **contact** page, if they want to find out more about the PT. All products also have a review rating from customers, if they have left one. And the testimonials page shows previous customers experiences and even before and after pics if they have left one.

### User Stories

- As a new visitor to the website, I want to be easily navigate the site and find information I was looking for in one or two clicks.
- As a new visitor, when browsing the site I want the site to be coherent and responsive, whether I am using a laptop, tablet or phone.
- As a new visitor, when filling out forms or entering data I want reasonable feedback to tell me whether I was either successful, or unsuccessful, and what the error is. 
- As a new visitor, when browsing the website  want it to have a professional feel and make me want to use this PT.
- As a new visitor, when searching the site I want to know from other customers whether this PT is a good one or not.
- As a new visitor, when browsing the products I want them to be presented to me in a tidy and easily readable/viewable manner.
- As a new visitor, when viewing products, I want to get as much information from them as possible to see what the exercise plan may entail or incorporate.
- As a new visitor, when browsing the products I want to be able to filter them by their types and sort them by features such as price or name.
- As a new visitor, when browsing the site I want to be able to find out more information about the PT in an easy manner without having to go through a myriad of pages or open new browser sessions.
- As a potential customer, when browsing the site I want to get a feel of the content that this PT offers, and the information that they offer so that I know the product will be the same.
- As a potential customer, when purchasing the product I want to be able to change my mind in the cart if I want a different size or product.
- As a potential customer, when purchasing a product I want the user experience to be slick and to flow in the correct, logical manner when putting in my details.
- As a potential customer, when purchasing a product, I want my cart items to be viewable when I am filling out my checkout details.
- As a returning customer, I want to be able to leave a testimonial or review for a product that I used, and rate it, whether it was good or bad.
- As a returning customer, I want to be able to alter or delete my review if I change my mind on the product.
- As a returning site user, i want to be able to edit my profile settings or details as I please.

### Color Scheme

![Colour Scheme](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/xy-scheme.png?raw=true)

The site conforms to a very uniform colour scheme across the entire page, there are slight variations on buttons or icons hover but mainly just opacity changes. The vibrant colour variations stem from that of the weight plates on a barbell, these can be red, blue, green or yellow. The green and yellow has been implemented on this site, green for use on success buttons, yellow for the review stars and also the cart update button. The scheme mainly stems from the following [Bootstrap theme](https://bootswatch.com/lux/), which gives the page the intended professional/cool design desired, convincing the customers to us this page. [Coolors](https://coolors.co/) website was used for the varying background colours, seen in the [about](https://xyfitness.herokuapp.com/page/about/) and [home](https://xyfitness.herokuapp.com/) pages, for example. This scheme is employed throughout the website and gives the user a more pleasant and immersive viewing experience.

![Weight Plates](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/gym-plates.jpg?raw=true)

## Wireframes

- [About](https://github.com/brianscan14/XYfitness/blob/master/wireframes/about.jpg?raw=true)
- [Testimonials](https://github.com/brianscan14/XYfitness/blob/master/wireframes/testimonials.jpg?raw=true)
  - [Add / edit testimonial](https://github.com/brianscan14/XYfitness/blob/master/wireframes/add-testimonial.jpg?raw=true)
  - [Single testimonial](https://github.com/brianscan14/XYfitness/blob/master/wireframes/single-testimonial.jpg?raw=true)
- Cart
  - [xs-md](https://github.com/brianscan14/XYfitness/blob/master/wireframes/cart-xs.jpg?raw=true)
  - [lg-xl](https://github.com/brianscan14/XYfitness/blob/master/wireframes/cart-lg.jpg?raw=true)
- Checkout
  - [Delivery Details](https://github.com/brianscan14/XYfitness/blob/master/wireframes/delivery-details.jpg?raw=true)
  - [Card Details](https://github.com/brianscan14/XYfitness/blob/master/wireframes/checkout.jpg?raw=true)
  - [Order Confirmed](https://github.com/brianscan14/XYfitness/blob/master/wireframes/order-confirmed.jpg?raw=true)
- [Index](https://github.com/brianscan14/XYfitness/blob/master/wireframes/index.jpg?raw=true)
- Account
  - [Login](https://github.com/brianscan14/XYfitness/blob/master/wireframes/login.jpg?raw=true)
  - [Register](https://github.com/brianscan14/XYfitness/blob/master/wireframes/register.jpg?raw=true)
- Navbar
  - [xs-md](https://github.com/brianscan14/XYfitness/blob/master/wireframes/navbar-xs.jpg?raw=true)
  - [lg-xl](https://github.com/brianscan14/XYfitness/blob/master/wireframes/navbar-lg.jpg?raw=true)
- Products
  - [All products](https://github.com/brianscan14/XYfitness/blob/master/wireframes/products.jpg?raw=true)
  - Single product
    - [Apparel product](https://github.com/brianscan14/XYfitness/blob/master/wireframes/product-apparel.jpg?raw=true)
    - [Plan product](https://github.com/brianscan14/XYfitness/blob/master/wireframes/product-plan.jpg?raw=true)
    - [Product info](https://github.com/brianscan14/XYfitness/blob/master/wireframes/product-info.jpg?raw=true)
  - [Product review](https://github.com/brianscan14/XYfitness/blob/master/wireframes/prod-review.jpg?raw=true)
- [Profile](https://github.com/brianscan14/XYfitness/blob/master/wireframes/profile.jpg?raw=true)
  - [Password change](https://github.com/brianscan14/XYfitness/blob/master/wireframes/profile-password.jpg?raw=true)
  - [Name / email change](https://github.com/brianscan14/XYfitness/blob/master/wireframes/profile-update-details.jpg?raw=true)
  - [Picture change](https://github.com/brianscan14/XYfitness/blob/master/wireframes/profile-pic.jpg?raw=true)
- [Search](https://github.com/brianscan14/XYfitness/blob/master/wireframes/search.jpg?raw=true)

## Technologies

### Languages Used

This project uses the below languages:

-  Html
-  JavaScript
-  Python 
-  CSS

### Databases

- [PostgreSQL](https://www.postgresql.org/docs/)
  - Open source relational DB used for production in Heroku.
- [SQLite](https://www.sqlite.org/docs.html)
  - SQL DB engine used while developing the site in Django.

### Front End

- [Bootstrap](https://getbootstrap.com/)
  - Used to make the website more responsive and streamline the grid layout.
- [jQuery](https://jquery.com/)
  - Used for the navbar, also the modal and to simplify DOM manipulation.
- [Popper.js](https://popper.js.org/)
  - A reference JS needed for the navbar & modal.
- [FontAwesome](https://fontawesome.com/)
  - The site used BootstrapCDN to provide icons from FontAwesome.
- [Autoprefixer](https://autoprefixer.github.io/)
  - Used to validate the CSS code for all browsers.
- [Jasmine](https://jasmine.github.io/)
  - To run automated tests for the JS code.

### Back End

- [Django](https://www.djangoproject.com/)
  - Django framework used to build the app.
- [PIP](https://pip.pypa.io/en/stable/installing/)
  - To install tools used in the project.
- [Travis](https://travis-ci.org/)
  - To verify build.
- [Stripe](https://stripe.com/ie)
  - Online payment platform for taking payments.
- [AWS S3 Bucket](https://aws.amazon.com/s3/)
  - To store static files and media content from the site on a server.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
  - It enables Python developers to create, configure, and manage AWS services.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
  - django-storages is a collection of custom storage backends for Django.
- [Gunicorn](https://gunicorn.org/)
  - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX, to deploy to Heroku.
- [Psycog2](https://pypi.org/project/psycopg2/)
  - PostgreSQL database adapter for Heroku.
- [Sweetify](https://github.com/Atrox/sweetify)
  - To return html alerts from user site interactions.
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
  - To process img files stored in DB.

## Features

### *Elements common to all pages*

#### Navbar:

The navbar can be divided into two type, small screen sizes and screen sizes above small. The pages consist of; home, about, contact, shop, testimonials, cart and depending on whether the user is signed in or not, login, signup, log out or view profile. There is a search icon on both screens for easier interaction with the user, when hovered all pages will change colour to signify it is a clickable option. The nav header is the short name of the page and this is in bolder and larger font to notify the users of this fact, when clicked it will bring them back to the home page. It is positioned at the top of the page for better viewing experience. The user can easily be returned to the navbar's location by clicking the up arrow which brings them to the top of the page.

*Small screen*:

![Nav Smaller Screens](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/smallnav.PNG?raw=true)

The navbar is a burger icon with a vertical collapsible list of the pages when clicked to easily navigate the website. The pages pop down in a list form under the header as a collapsible list and the user can can click one of these and they are brought to said page. The shopping bag and search icons here are just words, so as to not disturb the uniformity of the collapsible content list. The shopping bag title has the number of items currently in the bag in brackets after the title.

*Larger screen:*

![Nav](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/nav.PNG?raw=true)

![Nav Logged Out](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/nav-logged-out.PNG?raw=true)

For bigger screens the navbar is displayed as a list of titles of the pages in a horizontal fashion. Again, the overlay for searching can be called by clicking the search icon. In larger screens this and the shopping bag icon are pushed to the right side of the nav, along with the user's profile name if signed in. If not signed in the the profile is replaced by register or login titles. The shopping bag icon attached a green badge to it when an item is added to the cart to signify how many items are currently in it.

#### Footer:

![Footer](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/footer.PNG?raw=true)

The footer is a simple line of muted text alogn with a symbol for the site at the bottom of the page that signifies to the users who the page was created by. It is fixed to the bottom of the page with CSS positioning. If this page were to be used in production and as the popularity grows in stature then more links would be added to it, such as FAQs, contact links, contat details etc, for now it uses Django's templates to pull in the current date and just show the year. The image was created on [Canva](https://www.canva.com/).

### Scroll Top button:

This button appears on all screen sizes but is mainly for use with the smaller screens as a handy means for the user to scroll to the top of the screen when clicked. It will appear after 80px of scrolling as an 'up' directional arrow which will allow the user to know its function. Once clicked it bring you back to the start of the page. It also changes colour on hover to notify the user that it is clickable and uses CSS to position itself at the bottom right of the screen, with a higher z-index to make sure it isn't covered by any html content.

### Search Overlay:

![Overlay](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/overlay.PNG?raw=true)

The navbar uses a search icon in the shape of a magnifying glass which when clicked will call an overlay that covers the whole page. This overlay has less opacity to still show the user the page they were on, but in the 'background'. The overlay itself keeps to the pages colour scheme and consists of a search bar with a simple search button. This search bar searches the DB for products that match the string searched.

### Home Page

![Home Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/index.PNG?raw=true)

#### Hero Image

The user is first presented when they load the page by a hero image which consists of a darkened brick wall and some hero text as well stating the name of the site. The image is taken from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/) and is fixed, it also ties in very well with the sub-text, telling the user to "build a better foundation". It serves a purpose as the user immediately knows what the purpose of this site is from their initial arrival. The button to learn more then scrolls the user down to the section on the page which tells them what this page offers, and how this PT works.

#### Info Section

![Info](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/indexinfo.PNG?raw=true)

The next section to scroll to then is what gives the user more of an insight in to how the PT works. This is achieved by stating the 3 pillars of how he operates to improve you on; physically, mentally and eating habits. Each pillar has a little paragraph describing what he means by them and how he plans on improving you in that category. The user is then encouraged to start their journey and click on the button which will then redirect them to the products page.

#### Testimonials slideshow

![Testimonials](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/indextestimonials.PNG?raw=true)

The user is then presented with a series of five of the first testimonials from previous clients in a slideshow fashion. Each of these slides will move on themselves after 6 seconds unless clicked by the user to do otherwise. The background image again enkeeps with the theme of the page and is a greyed picture of dumbbells, which is again fixed in order to keep that professional feel. These testimonials act as a means of shoring up any reservations the potential customer may have had about using this PT, and (providing the testimonials are good) will entice them to use this PT and purchases one of the products. In the event of there being no testimonials on the page an inspiration quote with the same background will be used instead.

#### Social Media

![Social](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/indexsocial.PNG?raw=true)

The three pillars of an aspiring fitness trainer's social media platform are then linked in the next section with a grey background. These icons send the user to their respective browsers in a new tab and will open up their platform there, where they can explore instructional videos etc. When the user hovers over any of these icons then they will slowly transition to their respective company colours, adding a bit of colour and also denoting to the user the icon is clickable and they are on it. 

#### Mission Statement

![Mission](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/indexmission.PNG?raw=true)

This gives the user a quick synopsis of the values and goals of our company. It is an honest statement of what you will get if you work with this PT and tries to give the user a more personal note. Again, this is trying to solidify the user;s trust in this PT and eventually going on to use his services. 

### About page

![About Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/about.PNG?raw=true)

The about page enkeeps with the previously mentioned home page with the dark background to begin with containing information about what XY is. This is because if the user is a new user to the site, the next logical step is to browse the about section to find out more about this PT and what they stand for. The user is given a quick synopsis of what the company is and how they operate. 

Next is a more personal section giving the user a little bit more background on what the PT's origins are and where they originate from. This would be accompanied by a picture of the actual person if it were put into production. This gives the user a little bit more knowledge the type of person they could potentially be working with.

The 3 means of operation section is next then which gives the user an insight in to how the plans work, and how this PT operates. It lets them know that changes won't be instant and it also ties in with the 3 pillars previously seen on the home page.

The next section then tells the user why our results last, as was previously explained in how the plans work, it is about giving them a fishing rod as opposed to a fish. If the user buys in to this mode of training or thinking then they will know that this is definitely the PT for them. Again, encouraging them to purchases the products.

### All products page

![All Products](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/products.PNG?raw=true)

The products page features a plane background and all the products in rows of three, the background is so that the customer can see the product easier. This allows for a better viewing experience. The products themselves are displayed as a picture showing it, with a title and rating, if it has one, underneath it, and the price. The picture has a slight shadow to stand out form the background which gradually but very slightly increases to denote to the user that they are hovering over the product. The picture and title themselves are clickable links which brings you to the [product page](#single-product-view).

The reviews are dependent on whether the product itself has been reviewed by customers on its page. The value returned is an average of all the reviews accumulated for this product. The stars themselves are gotten from [FA's](https://fontawesome.com/start) site, using a conditional statement to determine to number of full / half stars returned. The price is a set price for the respective and is not dependent on product size, only on the product being offered.

The items can then whittled down to their categories, showing them in a different view. These categories consist of "Apparel" or "Plan",  which are the two types of product being offered. The Apparel currently only consists of a training jumper, as the PT's brand expands this offering could turn into a plethora of different branded offerings. The items can then be sorted in these views using the 'sort' button. This button calls a view to sort the contents of the page either, alphabetically a-z and vice versa, or by prices, high to low / low to high.

### Single product view

![A Product](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/aproduct.PNG?raw=true)

This page consists of more information on the product that the user will have clicked into to find out. Firstly the user is presented with a a slideshow of pictures of the product and some summary information about it. These include the title, description which is truncated and contains a link to the more info section, its reviews rating if it has been reviewed and then its price.

Since the items for sale on this site have two variations, apparel or plan, the design and layout subtly differs depending on this factor. The add to cart button is then below this info. If item is apparel the user is presented with a size selection choice and a numeric input value, if a plan then just the button. If the user tries to add the same plan twice they will be notified by [sweetify](https://github.com/Atrox/sweetify) and it won't be re-added to the cart. If it is apparel and the item of the same size is already in the cart then the quantity will just be updated, if different size then it is added as a new key / value pair to the product id's dictionary in  the cart. 

The more info section makes use of [Bootstrap's](https://getbootstrap.com/docs/4.3/components/navs/) tabs and depending on the product category it displays varying data for the product's fields. it consists of an info section, reviews tab, shipping information and/or size information. The info is the full product description, and if it is a plan then "equipment needed" is added here also.  Shipping then just tells the customer how they will receiver the product, if it is a plan then its in PDF format via email, if its apparel then it will be deliver within 10 working days. If the item is apparel then an extra tab for size info will be displayed.

Since the clothing item is unisex it will not need a size selection and they are made to order so there is no need for stock counts at this moment in time, see [features to implement section](#features-to-implement). All items will also have a reviews tab, if there are any reviews for the product then they will be in here. Users can easily add a review if they wish here, and give it a rating out of 5, their post will then appear in this section. If they already had a review, then they will be notified of this by [sweetify](https://github.com/Atrox/sweetify) and redirected to the product's page. They can then edit or delete their review if they want to, but it can only be done if their account is the author. The product's rating is then accumulated form these reviews and the average is taken and reflected by the [star](https://fontawesome.com/icons/star?style=solid) icons.

### All Testimonials

![All Testimonials](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/testimonials.PNG?raw=true)

This is where customers leave their experiences on the page for others to view, whether good or bad, and give their experience for others to see. The content is kept short and sweet and gives a quick synopsis of how they found it. This is a way for potential customers to see how good the PT is and see what they are getting themselves in for. 

The page itself is kept relatively simple with a bright background to ensure the content is as readable as possible for the user. The testimonials consist of a title, the user who posted it, their user image, the date posted (only month and year used here in Django templates) and also if the user has posted a before and after a link to see the review in full is shown. Only is both pictures are included will this link show up. Also if the user viewing the page is the author, a little extra message saying "you!" is put in brackets beside their name. This just means a little more interaction between the page and the user. There is also a button to add a new review at the bottom of the page which calls the add review form. If they already had a review, then they will be notified of this by [sweetify](https://github.com/Atrox/sweetify) and redirected to the all testimonials page.

### Single Testimonial View

![Single Testimonial](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/this-testimonial.PNG?raw=true)

The full view of the testimonial consists of the same format for the previous page of all the testimonials, except this time the before and after pics are included. These are shown first, as the user has already seen the message content and has clicked this link to see the pictures, the pictures should then be seen first. The pics are separated by a little border on bigger screens. The author name, which is their username in brackets followed by their first name if they put in one, is floated to the right this time. If the current user is the author of the review then they will see links to either edit the review or just delete it.

### Contact

![Contact Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/contact.PNG?raw=true)

The contact page is kept relatively simple as it only serves a purpose as a means for the user to get in contact with the PT if they have a query. This is because if they find themselves on this page in the first place then they do not want to be distracted by more text etc. They merely want to send the PT a message, so this page fits that purpose. Is the user is signed in then the form's initial data will have their email in the email field already.  

The message currently gets sent to the backend, being printed in the terminal window, and also gets added to the admin page. This could be set up in settings to send to my Gmail account but it means changing Gmail settings to less secure ones. If this website were to be fully deployed and used as a business then this would be altered and a work email utlised to take full advantage of this feature, and the Django settings altered. 

### Profile

![Profile Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/profile.PNG?raw=true)

The user's profile page, if they create one is kept relatively simple with just their picture they used on registration displayed, their username, first name if they added it, email, and then links to update these fields in the center of the page. The user can easily update their email, first name, username,  password or indeed profile picture on this page if they desire. The Django [password change](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/) form is used here for simplicity. These links redirect the user to the respective form's pages to alter these fields, and they are waterfalled appropriately.

### Cart

![Cart Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/cart.PNG?raw=true)

The shopping cart uses a context file in order to have its data available on each page. The user will add items to it from the products page and these will the be added to the cart dictionary, for that product's id. When an item is added the badge will appear on the cart icon in the navbar, or for smaller screens the numeric value is returned. If the item being added is a plan then this will not be added twice. If the item id is already in the cart then it will either; update item's quantity in the dictionary if the size is the same, or add another key value pair in the item's dictionary along with the previous one, if the size is different.

In terms of the cart page itself then the products are presented in rows, as most normal shopping carts would be. If the same product (of differing sizes) is in the cart then the different sizes will be presented as another product row to the user. The user is free to update their cart items from this view as they please. they can update the quantity of items if it is a clothes item, or the size either. If the size they are changing it to is already in the cart then the quantity will just just be added to the size they are changing it to, and the previous item deleted form the cart.

If the user wants to just remove an item form the cart then they can do this by just clicking the 'X' button and the cart is updated with the item removed from the dictionary. All these interactions are confirmed to the user by custom [sweetify](https://github.com/Atrox/sweetify) responses, depending on what they have done. The user can then click checkout, which bring them to next step step in the purchase process of filling out delivery details. If there are no items in the cart then this button is disabled and this next step is prevented. The view also determines what type of items are in the cart and if any of the contents contains an 'Apparel' item then the delivery fee of €5 is also added to the total.

### Checkout

The checkout sequence is then divided into two main sections for better user experience. The first being entering the user's delivery details and the second is entering the user's payment card information. On both pages the cart items can be seen with a similar assembly to the previous [cart page](#cart), only a more summarised version. The user can edit these details at any stage and return to the cart with the edit link provided. Throughout the checkout process there is breadcrumb of icons denoting to the user what stage they are at, depending on the stage they can use these to go back and forth.

#### Delivery Details:

![Delivery Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/delivery.PNG?raw=true)

The delivery page then consists of a form of which the user fills out in order to proceed to next step. These details are the standard ones of which a user fills out in most online stores to purchases an item. They consist of delivery address, phone number and name. Having these details will allow the site owner know where they will have to deliver the items. Once the user confirms their details they proceed to the next step of payment card information. If these details are not filled out or the cart items are empty then the button to continue to the next step will be disabled and the user unable to proceed.

#### Payment Card Details:

![Payment Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/checkout.PNG?raw=true)

The payment page then will show the user a summary of their address details, and gives them an opportunity to go back and change them. If they are happy with them then they can fill out the card form, which also has the current month pre-selected, this is done in the forms file to grab the current date, then month, then set that as initial value. This card form sends the information to stripe which will then take the payment form the user for the products. If there are any errors on the credit card form then they will be reflected as a message below the form's legend. There will also be notification from [sweetify](https://github.com/Atrox/sweetify) for these card errors. If the user has managed to get to this page with no items in the cart or the previous delivery page not filled out, then the 'pay' button will be disabled and the user won't be able to select it to make an incorrect payment.

#### Order Confirmation:

![Confirm Page](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/confirmation.PNG?raw=true)

If the card is filled out successfully the info is sent to stripe, the cart is emptied and the user returned to the thank you with a thank you message and a paragraph telling them to check their emails for the order confirmation, the 'tick' icon will also be coloured green now in the breadcrumb. If for some reason the user decides to use the history tab on this page and go back to the previous pages, the confirm details button for delivery and submit payment will be disabled as there are no items in the cart now. The user will also be sent an email upon successful order with their order number, as explained previously in [Contact](#contact) features, this is sent to the backend as this site is not in production, I did not want to change my Gmail settings to less secure ones for now.

### Account

### Login / Logout

![Login / Register Pages](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/login-register.PNG?raw=true)

The user can effectively login or logout from wherever they are on the site. If they choose to logout they are simply returned to the home page after doing so, with a [sweetify](https://github.com/Atrox/sweetify) alert telling them they what they are after doing. If they choose to login then they will be redirected to a login form where they enter either their username or email and their password. If successful they are either redirected to a page they needed to login to view or else to the home page if not.  A [sweetify](https://github.com/Atrox/sweetify) again greets them with their username in it this time telling them they logged in successfully. 

If there was an error with the login form then they will be shown the error message and they can try again, or reset their password if they forgot. The user can also login using their email if it matches the password/username, if they are already logged in and manage to access this page they are returned to the home screen with a [sweetify](https://github.com/Atrox/sweetify) message telling them this. If the user forgets their password then they can use the Django templates to do so.

### Register

If a user wishes to make an account, they will be presented with the registration form and its fields; username, email, password (twice) and profile picture for the site. The Django [user creation](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/) form is used here to create a user, with the given details. Password is entered twice so they can be checked for correctness in the backend. If the email entered or the username is taken then the form will return an error stating this, any other others are returned at the top of the form. Upon successful registration the user will also have created a profile, which uses the form pic as their profile pic, and be logged in. These details can be altered in the [Profile](#profile) page, if a user is already logged in and gets this page they are returned to the home screen with a [sweetify](https://github.com/Atrox/sweetify) message telling them they already have an account. They will also be encouraged upon successful registration to edit their profile page, in another [sweetify](https://github.com/Atrox/sweetify) message. If they needed to register an account to checkout then they will be redirected to the cart using the document.referrer and slice method to check if the url matches the 'next' one seen in the login page url.

## Features to implement

If this website were to be put into production, and as it becomes more popular, and in turn the PT becoming more popular, I would add more apparel items to the site. these items would tend to be branded, an I would also give the user more options when purchasing them, such as colour and gender filters too. This would mean the cart view and context file would need updating, along with the checkout view for payment and also another model added for these options, referencing the product as its key.

As the site grows and clientele increases, more plans would need to be offered to cover all shapes and sizes, regimes and goals. This would be done in time as the ones currently there are only a few offerings of what it could potentially be. As the number of items in the shop increases also I would implement a pagination system to help with the viewing process of all these products, it is not needed now as there are very little items on offer.

Since there is only one item in the shop currently that is "Apparel", and this item is made to order from the [oneills](https://www.oneills.com/) website (example of what I would use if it were in production). None of them kept in stock by me, but if there were more items on offer this would change, again another model would need to be added with a relationship to the main product one  giving feedback to the customer and letting them know whether the size of their chosen item is in stock or not.

Currently the user gets sent an email upon successful order, however it only a random number which is generated from Django. If this site were in full production and these plans were actual PDF files then this would need to be automated to send out these files to the user for download. Also the items order would be added to it, and a 'view status' tracker to let them know the progress of their items if they were apparels.

If this website were to be put into product then content would need to be added to these PDF files of exercises, diets etc. A sneak peek of these PDFs would then be added to the page to give the customer even more of an insight into what the workouts entail.

## Information Architecture

### Database

During the development phases of this project I worked with the [sqlite](https://www.sqlite.org/index.html) DB that Django uses. When the project is deployed it uses the [PostgreSQL](https://www.postgresql.org/) DB in Heroku.

### Data Structure 

Below is the data base collection:

#### Accounts

##### *Profile*

| Title       | DB Key      | Field Validation                         | Type          |
| ----------- | ----------- | ---------------------------------------- | ------------- |
| User        | user        | on_delete=models.CASCADE                 | OneToOneField |
| Username    | username    | max_length=30, default='User'            | CharField     |
| Profile Pic | profile_pic | upload_to='images', default='avatar.jpg' | ImageField    |

#### Checkout

##### *Order*

| Title     | DB Key          | Field Validation                                             | Type         |
| --------- | --------------- | ------------------------------------------------------------ | ------------ |
| Full Name | full_name       | max_length=50, blank=False                                   | CharField    |
| Number    | phone_number    | blank=False                                                  | IntegerField |
| Country   | country         | max_length=40, blank=False                                   | CharField    |
| Postcode  | postcode        | max_length=20, blank=True                                    | CharField    |
| Town      | town_or_city    | max_length=40, blank=Falsea                                  | CharField    |
| House No. | street_address1 | max_length=40, verbose_name=u'House name / apartment no.', blank=True | CharField    |
| Townland  | street_address2 | max_length=40, verbose_name=u'Townland', blank=False         | CharField    |
| County    | county          | max_length=40, blank=False                                   | CharField    |
| Date      | date            |                                                              | DateField    |

##### *OrderLineItem*

| Title    | DB Key   | Field Validation    | Type         |
| -------- | -------- | ------------------- | ------------ |
| Order    | order    | Order, null=False   | ForeignKey   |
| Product  | product  | Product, null=False | ForeignKey   |
| Quantity | quantity | blank=False         | IntegerField |

#### Pages

##### *Query*

| Title     | DB Key  | Field Validation               | Type      |
| --------- | ------- | ------------------------------ | --------- |
| Title*    | title   | max_length=30, default='Query' | CharField |
| Email     | email   | max_length=30, default='User'  | CharField |
| Message** | message | max_length=400                 | TextField |

**Title given following attributes in forms.py file: min_length=5*

***Message given a placeholder from a widget attribute in forms.py file and also: min_length=30*

#### Products

##### *Product*

| Title       | DB Key      | Field Validation                                             | Type         |
| ----------- | ----------- | ------------------------------------------------------------ | ------------ |
| Image one   | image1      | upload_to='images', default='images/item.jpg'                | ImageField   |
| Image two   | image2      | upload_to='images', blank=True                               | ImageField   |
| Image three | image3      | upload_to='images', blank=True                               | ImageField   |
| Name        | name        | name = models.CharField(max_length=100, default='XYfitness Product') | CharField    |
| Description | description | max_length=400                                               | TextField    |
| Price       | price       | max_digits=4, decimal_places=2                               | DecimalField |
| Category*   | category    | max_length=30, choices=cats, default='P'                     | CharField    |
| Size**      | size        | max_length=10, choices=sizes, default='D', verbose_name="size" | CharField    |
| Equipment   | equipment   | max_length=200                                               | TextField    |

**Category choices are either "Plan" or "Apparel".*

***Size choices are either "Default" for a plan, or range from "XS-XL" for apparel items.*

##### *Product Review*

| Title     | DB Key  | Field Validation                     | Type          |
| --------- | ------- | ------------------------------------ | ------------- |
| Product   | product | Product, on_delete=models.CASCADE    | ForeignKey    |
| Title*    | title   | max_length=30, default='User Review' | CharField     |
| User      | user    | Product, on_delete=models.CASCADE    | ForeignKey    |
| Content** | content | max_length=250                       | TextField     |
| Date      | date    | default=timezone.now                 | DateTimeField |
| Rating*** | rating  | choices=ratings, default='5'         | IntegerField  |

**Title  given a placeholder from a widget attribute in forms.py, and: min_length=5*

***Message given a placeholder from a widget attribute in forms.py file, and: min_length=20*

****Rating choices range from values 1-5.*

#### Testimonials

##### *Review*

| Title        | DB Key         | Field Validation                                             | Type          |
| ------------ | -------------- | ------------------------------------------------------------ | ------------- |
| Title*       | title          | max_length=30, default='Review Title'                        | CharField     |
| Image        | image          | upload_to='images', default='avatar.jpg'                     | ImageField    |
| Author       | author         | User, on_delete=models.CASCADE, unique=True                  | OneToOneField |
| Content**    | content        | max_length=250                                               | TextField     |
| Date         | date           | default=timezone.now                                         | DateTimeField |
| Before Pic   | before_picture | upload_to='images', blank=True, verbose_name=u"Before pic (only add these if you want to)." | ImageField    |
| After Pic    | after_picture  | upload_to='images', blank=True                               | ImageField    |

**Title  given a placeholder from a widget attribute in forms.py, and: min_length=5*

***Message given a placeholder from a widget attribute in forms.py file, and: min_length=40*

## Testing

[Link to the testing file for this project](https://github.com/brianscan14/XYfitness/blob/master/testing/TESTING.md)

## Deployment

### *Run project locally:*

Using a suitable IDE (this project used Gitpod), the below requirements are what are needed for running this project:

**[PIP](https://pip.pypa.io/en/stable/installing/), [Python 3](https://www.python.org/downloads/), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)**

To enable full use of the site locally, ensure that accounts are created with the following:

**[Stripe](https://stripe.com/docs/api)**, **[AWS](https://docs.aws.amazon.com/index.html)**

On the **Stripe** site the user is given a secret key and a publishable key, make sure to take note of these as they will be needed.

On the **AWS** website after [setting up](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html) the bucket the user is given a secret key and a secret key id, these won't be sent twice so make sure to save them correctly when given them.

1. Clone a copy of the [Github repo](https://github.com/brianscan14/XYfitness) by clicking the "clone" button, this will open the contents of the repo in a new workspace in the IDE. If Git is installed on your system, clone the repo with the following command: 

   `git clone https://github.com/brianscan14/XYfitness.git`

2. Use the python virtual environment (VI) for the interpreter by entering the below command:

   `pip install virtualenv`

3. Specify a path, for example one being created in the local directory called 'montypython' is:

   `virtualenv mypython`

4. Activate the VI by running the following command:

   1. Mac OS / Linus:
      `source montypython/bin/activate`
   2. Windows:
      `montypython\Scripts\activate`

   *Note: your commands may differ, depends on IDE used, check [python](https://docs.python.org/3/library/venv.html) docs if you are running into issues*

5. Upgrade pip if it is needed:

   `pip install --upgrade pip`

6. Install all the required modules with the command: 

   `pip -r requirements.txt`

   *This will also later be needed to setup the **heroku** app*

7. In your local IDE create a file called env.py.

8. Setup the following variables in your env.py file:

```python
"GIT_HOSTNAME": "local site hostname"

"HEROKU_HOSTNAME": "heroku site url"

"SECRET_KEY": "Django app secret key in settings"

"STRIPE_PUBLISHABLE": "general key gotten from stripe site"

"STRIPE_SECRET": "secret key gotten from stripe site"

"DATABASE_URL": "postgress url gotten form heroku app"

"AWS_SECRET_ACCESS_KEY": "AWS S3 secret key"

"AWS_SECRET_KEY_ID": "AWS secret key id"
```

9. Restart machine to active env variables.

10. Run below command in sequence to migrate the DB models:

    `python3 manage.py makemigrations`

    *Packages up your model changes into individual migration files*

    `python3 manage.py migrate`

    *Applies these changes to the DB*

11. You can now run the app with the command:

    `python3 manage.py runserver`

12. You can visit the site at:

    http://127.0.0.1:8000/

13. Create a superuser to then be able to access the admin functions of this website, and add content to it: 

    `python3 manage.py createsuperuser`

    *Add /admin to the site's url to access this admin page, and add/edit content on the site*

### *Heroku Deployment:*

Follow the below instructions to deploy XYfitness to Heroku:

1. In bash, create requirements file with:

   `pip3 freeze --local > requirements.txt`

2. Create a Procfile in the terminal with the command:

   `web: gunicorn "app name".wsgi:application`

   *Make sure gunicorn is installed with the below command for this to work:*

   `pip3 install gunicorn`

   *Update requirements.txt file again if this is not already installed*

3. If you ever use pip3 to install more packages after an initial deploy, you must re-generate the requirements.txt and commit/push to **heroku**

4. Using bash, commit everything:

   `git add .`

   `git commit -m "<Commit Message>"`

5. In bash, push to GitHub using: 

   `git push -u origin master`

6. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Make sure to set the region to Europe when naming it.

7. From the heroku dashboard of your new app, click on "Deploy" and then "Deployment method" and select GitHub, from there a popup will  appear and you select the appropriate repo.

8. Go to your Heroku account, find the app and open it. Click on setting and then "reveal config vars", set the following config vars:

```console
"DISABLE_COLLECTSTATIC": "1"

"SECRET_KEY": "Django app secret key in settings"

"STRIPE_PUBLISHABLE": "general key gotten from stripe site"

"STRIPE_SECRET": "secret key gotten from stripe site"

"DATABASE_URL": "postgress url gotten form heroku app"

"AWS_SECRET_ACCESS_KEY": "AWS S3 secret key"

"AWS_SECRET_KEY_ID": "AWS secret key id"
```

9. In the dashboard, click "Deploy", go to "manual" and make sure the master branch is selected and click "Deploy", and the build will begin.

10. Click on "view app" to see the app once this build is complete, this will  bring you to the site.

11. Same as in [local](#run-project-locally), add /admin to the end of the **site's url** and access the admin content on the page.

## Credits

### Content

All text on XYfitness was written by me.

### Media

All images on this site were sourced from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/) and [Pixaby](https://pixabay.com/)

### Code

The overlay for the search icon click was originally found [here](https://www.w3schools.com/howto/howto_js_fullscreen_overlay.asp) and heavily modified for my page.

The counter used in the cart view originated form this [example](https://bootsnipp.com/snippets/2eKOz).

The following **stack** [example](https://stackoverflow.com/questions/39576016/django-1-9-using-django-sessions-in-two-page-forms) helped with figuring out how to use session data for the delivery form in the ckecout process.

**Django** emails were used on the site are from the [docs](https://docs.djangoproject.com/en/3.0/topics/email/).

This **stack** [post](https://stackoverflow.com/questions/46617375/how-do-i-show-an-active-link-in-a-django-navigation-bar-dropdown-list) helped to get the *active* class added to the navbar links when on the page.

The following [example](https://stackoverflow.com/questions/45969679/get-average-of-user-input-ratings-for-different-model-instances-django) from **stack** helped with getting the **average ratings** used on the page for product reviews.

Using this **stack** [post](https://stackoverflow.com/questions/38431166/redirect-to-next-after-login-in-django) I was able to setup the redirect after login seen on the site.

Update user's password uses the Django [form](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/) to update the user's password, along with a tutorial from this [site](https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html).

The **Accounts, Cart, Reviews & Checkout** apps were initilally setup by following CI's tutorials, then changed to suit the purposes of the website.

### Acknowledgments

I would like to thank the CI tutors for all of their help throughout the course of this project. 

A special thanks would go to my mentor Simen, who has helped me throughout the course of not just this project, but the entire CI course. 

### Disclaimer

This website and its content are for educational purposes only