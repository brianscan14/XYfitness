# XYfitness

[![Build Status](https://travis-ci.org/brianscan14/XYfitness.svg?branch=master)](https://travis-ci.org/brianscan14/XYfitness)

This Django website was created as a means for an aspiring personal fitness or "PT" trainer to display their talents or capabilities to the general public, and potentially attract new clients. Whether this results in them purchasing a plan for exercise or routine to follow, or even if they purchase an item of clothing. This results in a revenue stream for the PT and means of getting their product out on the market and their clientele growing in stature. 

Users are encouraged to sign up to the website in order to create a profile, this will allow them to purchase products, leave reviews and the usual profile features by being able to edit their picture, password and add additional details such as first name, email, etc. However the user can still browse many parts of the page freely without needing an account, this is the encourage freedom of the site and to get the user to browse it more and get a feel for it, without being put off by having to sign in straight away. In order to purchase any products the user will then need to create an account. 

## UX

The main goal of the website is to convince customers that this is the PT that they need, and that his plans are the best ones to get on the market. This is accomplished by a combination of a sleek, professional design and many reviews and testimonials from current customers to persuade the user to use this PT. The pages are kept sleek and interactive so as to allow the user to easily navigate around the site.  The navbar at the top enkeeps with this theme and allows the users to navigate to each page with ease, decreasing to a menu icon on smaller screen sizes.

The hero image on the index page take up the entire and lets the user know the purpose of the site straight away, grabbing their attention. If the user just wants to search a product quickly then they can utilise the search icon in the nav bar which calls an overlay that has a search bar, which searches the DB for names matching the string inputted by the user. The user can also easily navigate to the about or contact page, if they want to find out more about the PT. All products also have a review rating from customers, if they have left one. And the testimonials page shows previous customers experiences and even before and after pics if they have left one.

### User Stories

1. As a new visitor to the website, I want to be easily navigate the site and find information I was looking for in one or two clicks.
2. As a new visitor, when browsing the site I want the site to be coherent and responsive, whether I am using a laptop, tablet or phone.
3. As a new visitor, when filling out forms or entering data I want reasonable feedback to tell me whether I was either successful, or unsuccessful, and what the error is. 
4. As a new visitor, when browsing the website  want it to have a professional feel and make me want to use this PT.
5. As a new visitor, when searching the site I want to know from other customers whether this PT is a good one or not.
6. As a new visitor, when browsing the products I want them to be presented to me in a tidy and easily readable/viewable manner.
7. As a new visitor, when viewing products, I want to get as much information from them as possible to see what the exercise plan may entail or incorporate.
8. As a new visitor, when browsing the products I want to be able to filter them by their types and sort them by features such as price or name.
9. As a new visitor, when browsing the site I want to be able to find out more information about the PT in an easy manner without having to go through a myriad of pages or open new browser sessions.
10. As a potential customer, when browsing the site I want to get a feel of the content that this PT offers, and the information that they offer so that I know the product will be the same.
11. As a potential customer, when purchasing the product I want to be able to change my mind in the cart if I want a different size or product.
12. As a potential customer, when purchasing a product I want the user experience to be slick and to flow in the correct, logical manner when putting in my details.
13. As a potential customer, when purchasing a product, I want my cart items to be viewable when I am filling out my checkout details.
14. As a returning customer, I want to be able to leave a testimonial or review for a product that I used, and rate it, whether it was good or bad.
15. As a returning customer, I want to be able to alter or delete my review if I change my mind on the product.
16. As a returning site user, i want to be able to edit my profile settings or details as I please.

## Wireframes



## Technologies

### Front End

- This project uses Html, JavaScript, Python & CSS programming languages.
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
- [PostgreSQL](https://www.postgresql.org/)
  - Open Source Relational Database for Heroku.
- [SQlite](https://www.sqlite.org/index.html)
  - In-process library used when developing the website.
- [Sweetify](https://github.com/Atrox/sweetify)
  - To return html alerts from user site interactions.
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
  - To process img files stored in DB.

## Features

#### *Elements common to all pages*

##### Navbar:

The navbar can be divided into two type, small screen sizes and screen sizes above small. The pages consist of; home, about, contact, shop, testimonials, cart and depending on whether the user is signed in or not, login, signup, log out or view profile. There is a search icon on both screens for easier interaction with the user, when hovered all pages will change colour to signify it is a clickable option. The nav header is the short name of the page and this is in bolder and larger font to notify the users of this fact, when clicked it will bring them back to the home page. It is positioned at the top of the page for better recipe viewing experience. The user can easily be returned to the navbar's location by clicking the up arrow which brings them to the top of the page.

*Small screen*:

The navbar is a burger icon with a vertical collapsible list of the pages when clicked to easily navigate the website. The pages pop down in a list form under the header as a collapsible list and the user can can click one of these and they are brought to said page. The shopping bag and search icons here are just words, so as to not disturb the uniformity of the collapsible content list. The shopping bag title has the number of items currently in the bag in brackets after the title.

*Larger screen:*

For bigger screens the navbar is displayed as a list of titles of the pages in a horizontal fashion. Again, the overlay for searching can be called by clicking the search icon. In larger screens this and the shopping bag icon are pushed to the right side of the nav, along with the user's profile name if signed in. If not signed in the the profile is replaced by register or login titles. The shopping bag icon attached a green badge to it when an item is added to the cart to signify how many items are currently in it.

##### Footer:



**Scroll Top button**

This button appears on all screen sizes but is mainly for use with the smaller screens as a handy means for the user to scroll to the top of the screen when clicked. It will appear after 80px of scrolling as an 'up' directional arrow which will allow the user to know its function. Once clicked it bring you back to the start of the page. It also changes colour on hover to notify the user that it is clickable and uses CSS to position itself at the bottom right of the screen, with a higher z-index to make sure it isn't covered by any html content.

**Search Icon**

The navbar uses a search icon in the shape of a magnifying glass which when clicked will call an overlay that covers the whole page. This overlay has less opacity to still show the user the page they were on, but in the 'background'. The overlay itself keeps to the pages colour scheme and consists of a search bar with a simple search button. This search bar searches the DB for products that match the sting searched.

**Color Scheme**

The site conforms to a very uniform colour scheme across the entire page, there are slight variations on buttons or icons hover but mainly just opacity changes. The vibrant colour variations stem from that of the weight plates on a barbell, these can be red, blue, green or yellow. The green and yellow has been implemented on this site, green for use on success buttons, yellow for the review stars and also the cart update button. The scheme mainly stems from the following [Bootstrap theme](https://bootswatch.com/lux/), which gives the page the intended professional/cool design desired, convincing the customers to us this page. [Coolors](https://coolors.co/) website was used for the varying background colours, seen in the [about](https://xyfitness.herokuapp.com/page/about/) and [home](https://xyfitness.herokuapp.com/) pages, for example. This scheme is employed throughout the website and gives the user a more pleasant and immersive viewing experience. 

![Weight Plates](https://github.com/brianscan14/XYfitness/blob/master/media/images/readme/gym-plates.jpg?raw=true)

#### Home Page

##### Hero Image

The user is first presented when the y load the page by a hero image which consists of a darkened brick wall and some hero text as well. The image is taken from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/) and is fixed, it also ties in very well with the sub-text, telling the user to "build a better foundation". It serves a purpose as the user immediately knows what the purpose of this site is from their initial arrival. The button to learn more then scrolls the user down to the section on the page which tells them what this page offers, and how this PT works.

##### Info Section

The next section to scroll to then is what gives the user more of an insight in to how the PT works. This is achieved by stating the 3 pillars of how he operates to improve you on; physically, mentally and eating habits. Each pillar has a little paragraph describing what he means by them and how he plans on improving you in that category. The user is then encouraged to start their journey and click on the button which will then redirect them to the products page.

##### Testimonials slideshow

The user is then presented with a series of testimonials from previous clients in a slideshow fashion. Each of these slides will move on themselves after 6 seconds unless clicked by the user to do otherwise. The background image again enkeeps with the theme of the page and is a greyed picture of dumbbells, which is again fixed in order to keep that professional feel. These testimonials act as a means of shoring up any reservations the potential customer may have had about using this PT, and (providing the testimonials are good) will entice them to use this PT and purchases one of the products. In the event of there being no testimonials on the page an inspiration quote with the same background will be used instead.

##### Social Media

The three pillars of an aspiring fitness trainer's social media platform are then linked in the next section with a grey background. These icons send the user to their respective browsers in a new tab and will open up their platform there, where they can explore instructional videos etc. When the user hovers over any of these icons then they will slowly transition to their respective company colours, adding a bit of colour and also denoting to the user the icon is clickable and they are on it. 

##### Mission Statement

This gives the user a quick synopsis of the values and goals of our company. It is an honest statement of what you will get if you work with this PT and tries to give the user a more personal note. Again, this is trying to solidify the user;s trust in this PT and eventually going on to use his services. 

#### About page

The about page enkeeps with the previously mentioned home page with the dark background to begin with containing information about what XY is. This is because if the user is a new user to the site, the next logical step is to browse the about section to find out more about this PT and what they stand for. The user is given a quick synopsis of what the company is and how they operate. 

Next is a more personal section giving the user a little bit more background on what the PT's origins are and where they originate from. This would be accompanied by a picture of the actual person if it were put into production. This gives the user a little bit more knowledge the type of person they could potentially be working with.

The 3 means of operation section is next then which gives the user an insight in to how the plans work, and how this PT operates. It lets them know that changes won't be instant and it also ties in with the 3 pillars previously seen on the home page.

The next section then tells the user why our results last, as was previously explained in how the plans work, it is about giving them a fishing rod as opposed to a fish. If the user buys in to this mode of training or thinking then they will know that this is definitely the PT for them. Again, encouraging them to purchases the products.

#### All products page

The products page features a plane background and all the products in rows of three, the background is so that the customer can see the product easier. This allows for a better viewing experience. The products themselves are displayed as a picture showing it, with a title and rating, if it has one, underneath it, and the price. The picture has a slight shadow to stand out form the background which gradually but very slightly increases to denote to the user that they are hovering over the product. The picture and title themselves are clickable links which brings you to the <u>product page</u>.

The reviews are dependent on whether the product itself has been reviewed by customers on its page. The value returned is an average of all the reviews accumulated for this product. The stars themselves are gotten from [FA's](https://fontawesome.com/start) site, using a conditional statement to determine to number of full / half stars returned. The price is a set price for the respective and is not dependent on product size, only on the product being offered.

The items can then whittled down to their categories, showing them in a different view. These categories consist of "Apparel" or "Plan",  which are the two types of product being offered. The Apparel currently only consists of a training jumper, as the PT's brand expands this offering could turn into a plethora of different branded offerings. The items can then be sorted in these views using the 'sort' button. This button calls a view to sort the contents of the page either, alphabetically a-z and vice versa, or by prices, high to low / low to high.

#### Single product view

This page consists of more information on the product that the user will have clicked into to find out. Firstly the user is presented with a a slideshow of pictures of the product and some summary information about it. These include the title, description which is truncated and contains a link to the more info section, its reviews rating if it has been reviewed and then its price.

Since the items for sale on this site have two variations, apparel or plan, the design and layout subtly differs depending on this factor. The add to cart button is then below this info. If item is apparel the user is presented with a size selection choice and a numeric input value, if a plan then just the button. If the user tries to add the same plan twice they will be notified by [sweetify](https://github.com/Atrox/sweetify) and it won't be re-added to the cart. If it is apparel and the item of the same size is already in the cart then the quantity will just be updated, if different size then it is added as a new key / value pair to the product id's dictionary in  the cart. 

The more info section makes use of [Bootstrap's](https://getbootstrap.com/docs/4.3/components/navs/) tabs and depending on the product category it displays varying data for the product's fields. it consists of an info section, reviews tab, shipping information and/or size information. The info is the full product description, and if it is a plan then "equipment needed" is added here also.  Shipping then just tells the customer how they will receiver the product, if it is a plan then its in PDF format via email, if its apparel then it will be deliver within 10 working days. If the item is apparel then an extra tab for size info will be displayed.

Since the clothing item is unisex it will not need a size selection and they are made to order so there is no need for stock counts at this moment in time, see <u>features to implement section</u>. All items will also have a reviews tab, if there are any reviews for the product then they will be in here. Users can easily add a review if they wish here, and give it a rating out of 5, their post will then appear in this section. If they already had a review, then they will be notified of this by [sweetify](https://github.com/Atrox/sweetify) and redirected to the product's page. They can then edit or delete their review if they want to, but it can only be done if their account is the author. The product's rating is then accumulated form these reviews and the average is taken and reflected by the [star](https://fontawesome.com/icons/star?style=solid) icons.

#### Testimonials

##### *All Testimonials*

This is where customers leave their experiences on the page for others to view, whether good or bad, and give their experience for others to see. The content is kept short and sweet and gives a quick synopsis of how they found it. This is a way for potential customers to see how good the PT is and see what they are getting themselves in for. 

The page itself is kept relatively simple with a bright background to ensure the content is as readable as possible for the user. The testimonials consist of a title, the user who posted it, their user image, the date posted (only month and year used here in Django templates) and also if the user has posted a before and after a link to see the review in full is shown. Only is both pictures are included will this link show up. Also if the user viewing the page is the author, a little extra message saying "you!" is put in brackets beside their name. This just means a little more interaction between the page and the user. There is also a button to add a new review at the bottom of the page which calls the add review form. If they already had a review, then they will be notified of this by [sweetify](https://github.com/Atrox/sweetify) and redirected to the all testimonials page.

##### *Single Testimonial*

The full view of the testimonial consists of the same format for the previous page of all the testimonials, except this time the before and after pics are included. These are shown first, as the user has already seen the message content and has clicked this link to see the pictures, the pictures should then be seen first. The pics are separated by a little border on bigger screens. The author name, which is their username in brackets followed by their first name if they put in one, is floated to the right this time. If the current user is the author of the review then they will see links to either edit the review or just delete it.

#### Contact

The contact page is kept relatively simple as it only serves a purpose as a means for the user to get in contact with the PT if they have a query. This is because if they find themselves on this page in the first place then they do not want to be distracted by more text etc. They merely want to send the PT a message, so this page fits that purpose. Is the user is signed in then the form's initial data will have their email in the email field already.  

The message currently gets sent to the backend, being printed in the terminal window, and also gets added to the admin page. This could be set up in settings to send to my Gmail account but it means changing Gmail settings to less secure ones. If this website were to be fully deployed and used as a business then this would be altered and a work email utlised to take full advantage of this feature, and the Django settings altered. 

#### Profile

The user's profile page, if they create one is kept relatively simple with just their picture they used on registration displayed, their username, first name if they added it, email, and then links to update these fields in the center of the page. The user can easily update their email, first name, username,  password or indeed profile picture on this page if they desire. These links redirect the user to the respective form's pages to alter these fields, and they are waterfalled appropriately.

#### Cart

The shopping cart uses a context file in order to have its data available on each page. The user will add items to it from the products page and these will the be added to the cart dictionary, for that product's id. When an item is added the badge will appear on the cart icon in the navbar, or for smaller screens the numeric value is returned. If the item being added is a plan then this will not be added twice. If the item id is already in the cart then it will either; update item's quantity in the dictionary if the size is the same, or add another key value pair in the item's dictionary along with the previous one, if the size is different.

In terms of the cart page itself then the products are presented in rows, as most normal shopping carts would be. If the same product (of differing sizes) is in the cart then the different sizes will be presented as another product row to the user. The user is free to update their cart items from this view as they please. they can update the quantity of items if it is a clothes item, or the size either. If the size they are changing it to is already in the cart then the quantity will just just be added to the size they are changing it to, and the previous item deleted form the cart.

If the user wants to just remove an item form the cart then they can do this by just clicking the 'X' button and the cart is updated with the item removed from the dictionary. All these interactions are confirmed to the user by custom [sweetify](https://github.com/Atrox/sweetify) responses, depending on what they have done. The user can then click checkout, which bring them to next step step in the purchase process of filling out delivery details. If there are no items in the cart then this button is disabled and this next step is prevented. The view also determines what type of items are in the cart and if any of the contents contains an 'Apparel' item then the delivery fee of €5 is also added to the total.

#### Checkout

The checkout sequence is then divided into two main sections for better user experience. The first being entering the user's delivery details and the second is entering the user's payment card information. On both pages the cart items can be seen with a similar assembly to the previous <u>cart page</u>, only a more summarised version. The user can edit these details at any stage and return to the cart with the edit link provided. 

The delivery page then consists of a form of which the user fills out in order to proceed to next step. These details are the standard ones of which a user fills out in most online stores to purchases an item. They consist of delivery address, phone number and name. Having these details will allow the site owner know where they will have to deliver the items. Once the user confirms their details they proceed to the next step of payment card information.

The payment page then will show the user a summary of their address details, and gives them an opportunity to go back and change them. If they are happy with them then they can fill out the card form. This card form sends the information to stripe which will then take the payment form the user for the products. If there are any errors on the credit card form then they will be reflected as a message below the form's legend. There will also be notification from [sweetify](https://github.com/Atrox/sweetify) for these card errors.  

If the card is filled out successfully the info is sent to stripe, the cart is emptied and the user returned to the thank you with a thank you message and a paragraph telling them to check their emails for the order confirmation. If for some reason the user decides to use the history tab on this page and go back to the previous pages, the confirm details button for delivery and submit payment will be disabled as there are no items in the cart now.

## Features to implement



## Information Architecture



## Credits

### Content

All text on XYfitness was written by me.

### Media

All images on this site were sourced from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/)

### Code

The overlay for the search icon click was originally found [here](https://www.w3schools.com/howto/howto_js_fullscreen_overlay.asp) and heavily modified for my page.

### Acknowledgments

I would like to thank the CI tutors for all of their help throughout the course of this project, and my mentor, Simen.

### Disclaimer

This website and its content are for educational purposes only