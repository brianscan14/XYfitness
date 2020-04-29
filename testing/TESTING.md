# XYfitness Testing

[link to view the website on Heroku](https://xyfitness.herokuapp.com/)

## Table of contents

- [Manual Testing](#manual-testing)
  * [Planning](#planning)
  * [Implementation](#implementation)
    + [*Methodology used*](#methodology-used)
    + [*Manual testing completed*](#manual-testing-undertaken-on-features)
    + [*User Stories tests*](#user-stories-tests)
  * [Results](#results)
    + [*Results of Google Audits*](#results-of-google-audits)
    + [*Bugs fixed*](#bugs-fixed)
    + [*Bugs still an issue*](#bugs-still-an-issue)
  * [*Further Manual Tests*](#further-manual-tests)
- [Automated Testing](#automated-testing)
  * [Validation](#validation)
  * [Jasmine](#jasmine)
  * [Travis](#travis)

## Manual Testing

### Planning

------

The main goal of this website is to offer a means for a PT to get their brand out on the market and obtain new customers by encouraging them to purchase one of their products. This testing will be carried out using developer tools audit tests, different browsers and also different screen sizes to check responsiveness. Validation tools and automated tests will also be carried out to check the code's validity, as outlined in the "Automated testing" section below. The main means of testing the intended purpose of this website will also be to go through each client story and check if their outcome was achieved.

### Implementation

------

#### *Methodology used*

*This manual tests below were carried out on the following browsers:*

- Chrome
- Safari
- IE
- Firefox

*And devices:*

- Laptops (windows & mac)
- Desktop (windows & mac)
- iPhones 6 & 7
- iPad & iPad mini
- Samsung's 6, 8 & 10e

The audit tool from google inspect was also used in order to improve on three aspects:

- Performance
- Best Practices
- Accessibility

#### *Manual testing undertaken on features:*

#### Common elements

##### Navbar:

1. Confirm nav is a list of the different pages on lg-xl screens
2. Confirm nav is a burger icon with collapsible menu on xs-md screens
3. Confirm current page is highlighted in the nav menu
4. Confirm nav items and nav search icon changes colour when hovered over
5. Confirm user is brought to correct page for each nav item
6. Confirm that when clicked the nav search icon calls an overlay covering the screen
7. Confirm that the form searches for the entered string when button is clicked or 'enter' typed
8. Confirm that incorrect spelling is highlighted 
9. Confirm user is redirected to page of the results with the matching products
10. Confirm user is redirected to all products page if no matches
11. Confirm if user is signed in their username appears on the nav as a link, and a logout link too
12. Confirm if the site viewer has no profile or is signed out then the sign in or register links are shown instead

##### Footer:

1. Confirm the footer content stays centered and at the bottom of the page on all screen sizes and pages.
2. Confirm footer logo adjusts width appropriately for differing screen sizes. 

##### Float Top Button:

1. Confirm button only appears on bottom right of screen when user has scrolled down the page
2. Confirm that the icon changes colour when hovered over
3. Confirm that the user is brought to the top of the page when button is clicked
4. Confirm that the action of scrolling to the top is  slowed down and not a sudden jolt
5. Confirm icon is above any content that is on the page and doesn't have a lower z-index

#### Index/Home Page:

1. Confirm that the page content is margined correctly on all screen sizes.
2. Confirm that hero text, subheading and find out more button resizes and stays centered on all screen sizes.
3. Confirm that find out more button scrolls user down to the more info section in a smooth fashion.
4. Confirm that the more button changes colour on hover.
5. Confirm that info section title and sub-content stay centered on all screen sizes.
6. Confirms the 3 columns of information take up the full width to themselves and act as rows on smaller screen sizes.
7. Confirm that clicking the start your journey button redirects the user to the products page on click.
8. Confirm on hover the start your journey button changes colour.
9. Confirm that Testimonials section title stays centered on all screen sizes.
10. Confirm the text content of a user's testimonial stays centered on all screen sizes, and an appropriate margin from the heading.
11. Confirm that clicking the next or previous arrows will show the appropriate slideshow div.
12. Confirm that on xs screen sizes if the text overflows then it is hidden.
13. Confirm that if there are no testimonials in the DB then a quote appears on this div instead.
14. Confirm that Mission statement section title stays centered on all screen sizes.
15. Confirm that the mission statement content stays centered on all screen sizes.
16.  Confirm that Social section title stays centered on all screen sizes.
17. Confirm that the social media icons stays divided in thirds on all screen sizes.
18. Confirm that on hover the social media icon changes colour to their respective signature colours.
19. Confirm that when clicked this icon will redirect the user to a new tab for this social media link.

#### About Page

1. Confirm that the page content is margined correctly on all screen sizes
2. Confirm that the '**Why XY?**' heading, its subtext and get started button resizes and stays centered on all screen sizes
3. Confirm that 'get started' button redirects the user to the products page on click
4. Confirm that the more button changes colour on hover
5. Confirm that 'A bit about me' section's content is centered as a unit, with the picture slightly to the left of the text
6. Confirm that the picture is centered and a row by itself and the same with the text, on smaller screens
7. Confirm that the picture resizes appropriately for differing screen sizes and the aspect ration is maintained
8. Confirm that clicking on the results link will bring the user to the testimonials page
9. Confirm that clicking on the contact button will bring the user to the contact page
10. Confirm that on hover the contact button changes colour
11. Confirm the the 'How we work' section's content remains centered and margined appropriately on all screen sizes
12. Confirm the the 'Our work lasts' section's content remains centered and margined appropriately on all screen sizes
13. Confirm that the 'get in touch' button redirects the user to the contact page
14. Confirm that on hover the 'get in touch' button changes colour

#### Shop

1. Confirm the breadcrumb for this page is pointing correctly
2. Confirm that the page title adds 'Shop' to it
3. Confirm links for apparel/plan redirect user to the correct pages
4. Confirm the title for all products view is "all products"
5. Confirm the Sort by form is floated to the right on bigger screens and centered on smaller ones
6. Confirm the sort function works correctly on the page, by sorting the items on this page in the manner that the user selected
7. Confirm that the products on the page are margined correctly from left-right on larger screens, but centered on smaller screen sizes, including their text
8. Confirm that the product's image shadow increases slightly when hovered over
9. Confirm the image's aspect ratio is maintained on all screen sizes
10. Confirm that either clicking on the image or the product name brings you to this product
11. Confirm the ratings shown are for the correct product, and if it has no ratings then no stars show.
12. Confirm that if you alter the rating on a product that the pages updates the average reviews value from this rating correctly
13. Confirm if the user selects the sort by function when in the apparel or plan category view, that only the products matching this category are sorted appropriately

#### Single Product Page

1. Confirm that the page content is margined correctly on all screen sizes
2. Confirm that the breadcrumb points to the correct product
3. Confirm that product image is on left side correctly on larger screen, with some product details on the right, but on smaller screens these are their own rows which are centered
4. Confirm that on clicking the arrows in the product image that the different images are cycled through
5. Confirm that clicking the 'see info' link in the truncated description brings the user down to the more information section for this product
6. Confirm that if this product is a plan that only the 'add to cart' button is shown, and not one for selecting sizes or quantity
7. Confirm that adding this product calls a **sweetify** response telling the user they have done so and that the cart icon now has a green badge at the top of it with the count of the number of items in the cart, or if on smaller screen, the number in numerical format beside the checkout link
8. Confirm that if the product is a plan and the item is already in the cart then the user will be notified of this with **sweetify** and the item is not duplicated in the cart
9. Confirm that if this item is an apparel item then the size option select appears and the quantity option also is available beside the add to cart button, with a max input of 50
10. Confirm that if this item is apparel and the size the user is adding is already in the cart then the user gets a **sweetify** alert saying "cart updated" instead of "item added to cart"
11. Confirm that if this item is an apparel one then if the user adds a different size of it to the cart, the cart will have a new row in it, acting as a different item
12. Confirm that if this item is a plan then the 'equipment needed' field is also included in the more information section below the product
13. Confirm that if this item is an apparel item then the 'size' tab is also added to the more information section
14. Confirm that differing information is displayed in the 'shipping' tab in the more information section depending on what category the product is
15. Confirm that all content on the product review form is centered
16. Confirm the cancel button brings the user back to the product's page they were on
17. Confirm that upon adding a product review that it appears in the reviews section tab for this product
18. Confirm that the minimum / max lengths used in the forms.py and model file throw up a notification to the user if they are not adhered to and the placeholder text is correct
19. Confirm that the average product review updates appropriately if the product rating is changed
20. Confirm if the current user is the reviews author then links to edit or delete that review will appear beside it, but only for that review
21. Confirm values saying number of reviews update correctly and the text with it if reviews are added / deleted
22. Confirm clicking on edit review brings up the correct previous review for this user, and adding it doesn't add another review for the user, and the model relationship is maintained
23. Confirm is user tries to add a review straight but they already have a review then they will be redirected to the product's page and told this with **sweetify**, and the duplicate review not added
24. Confirm that the act of deleting a review removes it from the DB and the page, and the average reviews are updated correctly, with a **sweetify** message to confirm this action

#### Contact Page

1. Confirm that the breadcrumb is pointing correctly to this page
2. Confirm if the user is signed in then the forms email field is populated with their email
3. Confirm that the minimum / max lengths used in the forms.py and model file throw up a notification to the user if they are not adhered to and the placeholder text is correct
4. Confirm that all content on the contact page is centered and margined appropriately
5. Confirm that on clicking 'send mail' an email is sent to the python terminal with the sender's email, subject and message content
6. Confirm that this content is also sent to the admin site for the site admin to look at there
7. Confirm that the user receives a **sweetify** success alert telling them their email was sent and they are redirect to the home page

#### Testimonials

1. Confirm the breadcrumb for this page is pointing to the correct url
2. Confirm that the rows of testimonials content remains in the center of the screen for all screen sizes
3. Confirm that the title and the content of each review remain centered on all screen sizes
4. Confirm that the date is floated to the right side under the content, and if the current user is the testimonial author, that an edit button appears under the date.
5. Confirm user name and picture appears on the left side under the content
6. Confirm that only if both a before and after pictures are included, that the link to view the testimonial in full is under the username on the left side
7. Confirm if the testimonial author is the current user, then a little note in brackets saying "(you!)" appears beside their name
8. Confirm that the add your experience button only appears when a user is logged in to their account
9. Confirm the add experience button changes colour when it is hovered over
10. Confirm when this button is clicked that it brings the user to the 'add experience' page to fill out a form
11. Confirm the form pages content is centered on all screen sizes
12. Confirm the placeholder text and the min / max values used in the forms.py and model are adhered to and correct, giving the user a notification if incorrect
13. confirm add testimonial button changes colour on hover and add a testimonial to the page & updates DB as it should 
14. Confirm clicking cancel button brings user back to the previous page of all the testimonials
15. Confirm that if a user already has a testimonial on the page that they will be redirected to the previous page and given a **sweetify** notification saying this, and a duplicate testimonial isn't added to the site

#### Single Testimonial Page

1. Confirm all content on the page is margined / appropriately on all screen sizes
2. Confirm the breadcrumb is pointing towards the correct testimonials name
3. Confirm on larger screens the pictures are side by side partitioned by a border, but on smaller screen sizes this border disappears and the two photos are now rows with their content centered
4. Confirm the title is centered and the review content is centered on all screen sizes, with the username floated to the right
5. Confirm if the testimonial author is the current user, then a little note in brackets saying "(you!)" appears beside their name
6. Confirm that if the current user is the original author then they will see links to edit or delete the review
7. Confirm that if they choose to edit the review, their previous review with all its contents, including the pictures, is pulled correctly and the form page content is centered
8. Confirm that min and max lengths from the forms.py / model files are still adhered to and the user is again notified of these if they are incorrect
9. Confirm clicking on the delete button will remove the testimonial from the site and also the DB
10. Confirm clicking on the back button will bring the user back to the previous page of all the testimonials

#### Login / logout

1. Confirm that if the user is already logged in and tries to do so again, they are redirected to home page with an alert form **sweetify** telling them they are already logged in
2. Confirm that all content on the page is margined correctly and the form content is all centered on all screen sizes
3. Confirm that if the user enters some details incorrectly, and clicks the login button they are notified of it in and alert above the form, and can try again
4. Confirm that if the user uses their email to sign in instead of the username, that this will also work if the  field is correctly inputted
5. Confirm the user's password remains hidden on the form
6. Confirm that the link to sign up if they do not have an account brings the user to the registration page
7. Confirm that if they choose to reset their password they are brought through the **Django** site password reset process, and that this password now works as their new password, and not the old one too
8. Confirm that if a user enters their details successfully and clicks the login button they will be redirected to the home page with a welcoming **sweetify** message including their username to greet them
9. Confirm that if the user needed to login to access a page on a site, that they are then redirected to that page after logging in, and no notification is sent to them this time
10. Confirm that if the user previously changed their username or email in their settings then that these new fields log in successfully, and not the old ones, they are now obsolete

#### Register

1. Confirm that all content on the register page is margined appropriately and in the center of the page on all screen sizes
2. Confirm that if the user is already logged in and tries to register, they are redirected to home page with an alert form **sweetify** telling them they are already registered
3. Confirm that any form errors are communicated to the user in their respective fields, and not altogether all at once above the form
4. Confirm that if the user tries to use a username or email that is currently on the site, that they are notified of this in the form and a duplicate isn't created
5. Confirm that upon successful registration the user is redirected to the home page with a **sweetify** telling them this and giving them a link to their profile to update it
6. Confirm that if the user chooses not to user a picture on sign up, that the default avatar image is given to them instead
7. Confirm that if the user needed to register to checkout their items in the cart, then they'll be redirected to the delivery details step in the checkout process after successful register, with no **sweetify**

#### Profile

1. Confirm that all content on the profile page is centered correctly on all screen sizes
2. Confirm that the breadcrumb is pulling the username correctly
3. Confirm that the details shown about the user are correct, and that only the first and second name will show if they are both there, or the first name by itself will show, but not not the second name by itself 
4. Confirm the links on the page point towards the correct URLs respectively
5. Confirm that the update details form's content is centered and the current details in there are correct
6. Confirm that updating details here are reverberated across the page, making the old ones obsolete
7. Confirm the change password link works, and the back top profile link is centered and brings the user back to the previous profile page
8. Confirm add details button is centered and changes colour on hover, and updates your profile details when clicked
9. Confirm that the update password form's content is centered, and raises errors if the old password is entered incorrectly
10. Confirm add details button is centered and changes colour on hover, and updates your password details when clicked
11. Confirm cancel button will bring you back to the profile page
12. Confirm that the update picture page's content is centered and the update picture button changes colour on hover, and updates your picture when clicked
13. Confirm the cancel button brings you back to the profile page
14. Confirm that upon successful update on either the picture, password or details update pages, the user is returned to the profile page with a **sweetify** message telling them they were successful and a varying message depending on what page they just came form

#### Cart

1. Confirm that the all products link is displayed on the left hand side on all screen sizes, and that it brings the user back to the all products page
2. Confirm the total items and checkout button at the top are floated to the right correctly on all screen sizes, and the total of items updates appropriately when they are changed
3. Confirm that if there are no items in the cart, then the button is disabled and unclickable, preventing the user from going to the checkout process with an empty bag
4. Confirm that the shopping bag title is centered on all screen sizes and resizes appropriately
5. Confirm that the subtotal updates correctly and iterates through all the items in the basket to get the precise amount for all the items
6. Confirm that the delivery fee is only applied to the total fee if the user has an 'apparel' item in the basket, and that if the apparel item is removed, this delivery fee is also removed
7. Confirm that clicking on the product's name or image will bring the user back to that product's page
8. Confirm that if the product is a plan, that the note telling them they will be emailed a pdf is added to it, instead of the size and quantity fields
9. Confirm that the total for this particular item is correct, and if it is an apparel item, and it has more than one in quantity, that these are tallied correctly
10. Confirm that if the quantity is changed, for an apparel item, then this updates correctly and the new quantity is shown in the input field and the total is correct
11. Confirm that the update button changes colour on hover
12. Confirm that if the user decides to change the size of the product in the cart, that the previous size instance of the product is removed, and the new one is added with the correct quanity
13. Confirm that if the size is changed in the cart and there is already an instance of this new size in the cart, that the old one is removed as before and the existing size instance's quantity gets updated with the selected quantity from the user's selection
14. Confirm that if there are more than one instance of a product in the cart, and the user decides to update either the sizes or the quantity of one of them, that unless the new size is the same as the other product, it remains untouched from changing something with the same product id but different size
15. Confirm that the user is aware of a successful action by an **sweetify** alert telling them
16. Confirm that deleting an item from the cart will remove it from the session dict and the cart totals will be updated appropriately, with a **sweetify** alert telling them the item was removed
17. Confirm that the cart items reconfigure appropriately on smaller screens, and that the update or note section, depending on the product's category, is pushed to a new row for better viewing
18. Confirm that the checkout button changes colour on hover
19. Confirm that clicking on the checkout button will bring the user to begin the checkout process if they are signed in, or tell them they need an account to do so

#### Checkout Page

##### *Delivery Steps*

1. Confirm that this page is only accessible if  the user is logged in
2. Confirm that all content on the page is margined appropriately, with the delivery details on the left side, and the cart content on the right side of a centered page, and on smaller screen sizes these cart contents are pushed to the bottom of the page with all content centered correctly
3. Confirm that the forms validations and max inputs are adhered to when entering data and the user is notified appropriately
4. Confirm that total indicated in the cart items summary are correct, and that the edit link points towards the cart view and delivery fee is only charged if there is an apparel item in the cart
5. Confirm that the correct stage in the checkout process is highlighted in the breadcrumb, and changes colour on hover
6. Confirm that the user can only click on the credit card stage of the checkout process icon in the breadcrumb, and that it only changes colour on hover, if they have both entered data on the delivery form already, and there is content in the cart items
7. Confirm that if the user has already filled out this delivery form in their session then the form will be pre-filed with this data upon loading of the page
8. Confirm that the confirm details button is centered to the delivery form and that it changes colour on hover, bringing the user to the next stage of the checkout process if they have items in the cart and the form is filled out correctly
9. Confirm that the confirm details button is disabled if there are no items in the cart and prevents an empty checkout if the user used the back in history tab to get back to this step

##### *Card Details step*

1. Confirm that this page is only accessible if  the user is logged in
2. Confirm that all content on the page is margined appropriately, with the previous delivery details on the left side with the card form underneath, and the cart content on the right side of a centered page, and on smaller screen sizes these cart contents are pushed to the bottom of the page with all content centered correctly
3. Confirm that the forms validations and max inputs are adhered to when entering data and the user is notified appropriately if they are incorrect, also if the card details have issues that the user is notified with a danger alert div showing them the error
4. Confirm that total indicated in the cart items summary are correct, and that the edit link points towards the cart view, and delivery fee is only charged if there is an apparel item in the cart
5. Confirm that the correct stage in the checkout process is highlighted in the breadcrumb, and changes colour on hover
6. Confirm that the delivery icon now also changes colour on hover, and can be clicked to go back to the delivery form
7. Confirm that the delivery details shown are correct and are what the user entered previously, and that clicking the edit link will bring the user back to the previous delivery page
8. Confirm that the submit payment button is disabled if there are no items in the cart, preventing an empty checkout and incorrect customer charge
9. Confirm that the submit payment button changes colour on hover and is centered, when clicked it redirects you to the thank you page confirming your order, and an email is sent to the terminal, thanking the customer

##### *Thank You page*

1. Confirm that upon successful order of products on the site, the user is redirected to the thank you page, which thanks them for their order
2. Confirm that all content on this page is centered, and the back to website button points correctly to the home page
3. Confirm that the user's email mentioned in the thank you message is correct
4. Confirm that if the user goes back in history from this page, all of the content from the previous pages is now empty, and none of the confirm details or submit payment buttons are active

#### *User Stories tests*

- As a new visitor to the website, I want to be easily navigate the site and find information I was looking for in one or two clicks.
  - The navbar is very simple to use and brings the user to any part of the page when clicked.
  - There are also buttons all over the page linking intuitively to different parts of it.
  - The search icon can be clicked from any page and lets the user search for any product in two clicks.
  - Shop items can be searched by their categories either if the user wishes from the navbar.
- As a new visitor, when browsing the site I want the site to be coherent and responsive, whether I am using a laptop, tablet or phone.
  - The **BS4** classes and layout were utilised in this project to have the layout responsive to different configurations etc.
  - Media queries were used for heading font sizes on smaller screens and positions of items. **CSS** such as 'text-overflow' was also used to hide any text that goes over its div.
  - Images were given **BS4** class "img-fluid" were customer classes were not used to determine their sizes and ensure aspect ratios were adhered to.
- As a new visitor, when filling out forms or entering data I want reasonable feedback to tell me whether I was either successful, or unsuccessful, and what the error is. 
  - **Sweetify** alerts are utilised throughout this page to give a level of feedback to the user about an interaction they have just completed or attempted, such as logging in or adding an item to the cart.
  - If filling out forms the user is redirected to a new page telling them they were either successful or if not, giving them the reason for it with **sweetify**.
- As a new user, when browsing the website  want it to have a professional feel and make me want to use this PT.
  - A simple, slick colour scheme is adhered to at all times with this website, these colours were utilised to give the customer that sense that this is a professional site.
  - Background photos in the [index](https://xyfitness.herokuapp.com/) page are fixed on scroll which help aid the qualified persona of this expert PT.
  - Paragraphs are kept concise and to the point in order to not lose the customer's attention span.
  - The site is kept relatively simple but with enough information so that the user is well informed but at the same time not distracted by unbeneficial content for the PT.
- As a new user, when searching the site I want to know from other customers whether this PT is a good one or not.
  - A testimonials section is added to the site whereby a past customer can add their experience with this PT to the site, whether good or bad, and also add before or after pics if they wish.
  - Reviews can be added to the products on the site and these can be seen both while browsing all products, which gives the average rating, or when viewing a single product, which gives the average but also a list of all the reviews.
- As a new user, when browsing the products I want them to be presented to me in a tidy and easily readable/viewable manner.
  - In the 'all products' view the products are laid out in rows of columns of 3, currently there are 6 products on the page which doesn't take up too much screen space on mobile or desktop.
  - I the 'all products view' the items can be sorted either alphabetically or by price by the user.
  - Products can be filtered and searched by their category either if the user wishes.
  - Single product view displays all the information about this product in a tidy and readable manner, with differing views for screen sizes.
- As a new user, when viewing products, I want to get as much information from them as possible to see what the exercise plan may entail or incorporate.
  - All products have an information tab which differs depending on their category type, giving the user more information about the product.
  - If the product is a plan then information such as 'equipment needed' is added to its info, and also the description gives a brief summary of what the plan entails.
- As a new user, when browsing the products I want to be able to filter them by their types and sort them by features such as price or name.
  - Items in the shop can be filtered down to either be of the 'apparel' type, or a 'plan'.
  - These filtered options can then be sorted accordingly by their features.
- As a new user, when browsing the site I want to be able to find out more information about the PT in an easy manner without having to go through a myriad of pages or open new browser sessions.
  - The about section gives the user a very good synopsis of this PT's methodology in training an also their ethos in how they work.
  - Information such as mission statements are given in the index, and the 3 pillars of the PT's mentality also.
  - Users can easily contact the PT by filling out a quick and easy contact form in the [contact](https://xyfitness.herokuapp.com/xy/contact/) page, they don't need an account to do this.
- As a potential customer, when browsing the site I want to get a feel of the content that this PT offers, and the information that they offer so that I know the product will be the same.
  - Social media links are provided on the [home page](https://xyfitness.herokuapp.com/) which will link a user to this PT's social media platform, as all good PTs have.
- As a potential customer, when purchasing the product I want to be able to change my mind in the cart if I want a different size or product.
  - Forms are included in the cart to update the items there and then, user can select a different size or quantity and the product will update to this new selection.
  - There is also a delete button which offers quick and simple removable of an item from the shopping cart for a potential customer.
- As a potential customer, when purchasing a product I want the user experience to be slick and to flow in the correct, logical manner when putting in my details.
  - The customer is progressed through the checkout process in logical manner,enter delivery details, then enter card details, then place the order and redirect to the confirmation page when successful.
  - Customers can ramble between these checkout stages (only if the forms were filled out) and edit the previously entered details if they wish.
  - The user is presented with a breadcrumb which denote to them which stage of the checkout process they are on, these are clickable but pull the session data to determine whether the user has completed previous step to get onto the next stage.
- As a potential customer, when purchasing a product, I want my cart items to be viewable when I am filling out my checkout details.
  - The customer is presented with a list of their checkout items in a tidy and presentable manner at the side of the page during all stages of the checkout.
  - The customer can click on this 'bag' and edit their items if they wish.
- As a returning customer, I want to be able to leave a testimonial or review for a product that I used, and rate it, whether it was good or bad.
  - Users can easily add a testimonial by clicking the 'add testimonial' button on the '[testimonials](https://xyfitness.herokuapp.com/testimonials/all/)' page which brings them to a form they can fill out with their experience.
  - Users can also easily add product reviews by clicking on the 'add review' link in the product info section, and give it a rating.
- As a returning customer, I want to be able to alter or delete my review if I change my mind on the product.
  - User can easily view their reviews and if they change their mind, edit them, as ad 'edit' option will appear on the reviews or testimonial if the current user is the original author.
  - A user can also simply delete their review as a 'delete' option will also appear beside the aforementioned 'edit' link if they are the original author.
- As a returning site user, i want to be able to edit my profile settings or details as I please.
  - Users can access their profile easily by clicking on their username in the navbar and here they will be directed to their profile page showing a summary of all their details.
  - Users can change their password from the profile page.
  - Users can also change their profile picture if they wish from the like on the profile page.
  - Users can also add a bit more detail about themselves like their actual names on the profile page, and edit their usernames or emails which then cascades across the site.

### Results

------

#### *Results of Google Audits*

This let me realise where aria-labels were missing and alt tags, along with labels for forms and if CDN library version was vulnerable. Where loading times can be reduced and colour's opacities needed to be changed to improve performance. The pictures were gotten from [Pexels](https://www.pexels.com/) and were large in file size so these were either condensed on [TinyPNG](https://tinypng.com/) or changed for a smaller sized picture. From these audits on the site each page scored over 90% or over in the three aspects aforementioned.

#### *Bugs fixed*

1. When in the plan or apparel view in the shop and trying to sort the products all product types would be called:
   - This was due to an error both in my urls file, view and the fix for it stemmed from using the templating language. Django templating was used to determine which url was currently being viewed by the user, and this would then feed back to the view. Depending on the url, the view would pick up a different value for the sort value; general, apparel or plans. This would then filter back to the view and there it would filter the results which only matched those in the sort's value, and then sort them appropriately.
2. When browsing the testimonials, there was no way of the user accessing their own one if they wanted to edit / delete it:
   - This was corrected with django templating, the only way a testimonial was previously viewable was if a before and after picture was included. This was remedied by checking in the template if the current user was the author, and if this is the case then they would see and edit link appear which brings them to the testimonial in full.
3. When user tries to login or register, but is already logged in on another page, they were still able to go through the whole sign in / sing up process before realising:
   - To fix this, a quick check was added to the views of these function to check if the user is already authenticated, and if this is the case then they are redirected to the home page and notified with a custom **sweetify** message for each.
   - Also when redirecting after login to the next page, these alerts were being shown at the wrong stages in the process. If the user was to be redirected to the cart they shouldn't be seeing a welcome back message, if the login was incorrect they shouldn't see a welcome back message, this was also corrected.
4. When an apparel item was added to the cart, the delivery fee was added on correctly, but if it was removed and there were no apparel items in the cart the delivery fee stayed there:
   - This was an issue with where the delivery total was being added in the context file, and the conditional checking if there was an apparel item in the cart already. At first I thought the delivery total needed to be added to the for loop checking each item, but this just added it on every time. 
   - The correct way to do it to add a filter for where a product matches its id, and the category is apparel in the cart items, if this exists at all in the for loop checking all items, then the del total is 5. Then this is added to the the total value outside the for loop, and this was checked and verified to be correct when there was more than just one apparel item in the shop.
5. For the all products page, and showing the average reviews for each one, there was an issue where all average reviews for all products, showed on each product:
   - This was remedied by using Django templating to check within the for loop if this rating id from the view, matched the product id, and if that was true then show the rating for this product. To make sure the id was matching the product correctly I reviewed them and gave them different ratings and checked if the average updated correctly, which it did for that product.
6. In the cart when a user added the same item to the cart but with a different size it was replacing the previous item, and also duplicates were being added:
   - Firstly a check was implemented in the cart add view to see if the item was a plan, if this plan was already in the cart then it couldn't be added again, as it was merely a PDF and could just be downloaded again after purchase.
   - Secondly, a conditional was also added in the cart add and update functions where it wopuld check if the if was in the cart. If the size was already i nthe cart, then it would just add the quantity on to it. If the size was not already in the cart but the id was, then it would add a new kv pair for the quantity added and the size selected for this id. If neither were in the cat then it would just create a new item in the cart dict for this product id. If the same product had differing sizes in the cart then they would be shown as separate rows.
7. When a user was logging in, there was no option to register and also if they were redirected here from the cart because they needed an account they were not redirected back to where they came from:
   - A register option was added to the login form which would redirect the user to the register page when clicked if they didn't have an account.
   - If the user was redirected to login and they had an account, then templating was used to pull the 'next' value form the url used in django apps an the user was either directed back to here if this was the case, or to he home page if not.
   - If the user was redirected to login and needed an account to proceed, then javascript was utilised to pull the previous url at the register form page, this was then sliced to the last 24 characters and if this matched the characters for a 'next' url that would trigger a hidden value on the register form. Which the view file then pulled if there and redirected the user to the cart page also, and to the home page if this was not the case.
8. When browsing the site and pages of lesser content were there, the footer would be further up the page than it should be:
   - This was corrected by using css to position the footer at the bottom of the page height at all times, and a class was created which gave the containers of these pages a minimum viewport height, therefore keeping the footer at the bottom of the page as it should be.
9. When testing the checkout with [stripe's](https://stripe.com/docs/testing) test numbers, and using the card declined code, an error occurred where the customer paid check was being referenced too early:
   - This led me to realise the check for cusotmer.paid was being referenced to early in the view function in the event of this error happening. The paid check and subsequent email send and was added to inside the 'try' part of the function for charging the customer in stripe, else telling them their card was declined with a **sweetify** alert.
10. When trying to edit a testimonial on the page, the previously written content was not being pulled and the form was blank:
    - This led to a lot of troubleshooting and failed attempts at fixing the issue, even trying the make a new edit view function purely for editing the previous form. Eventually I realised that the regex in the testimonials urls file was incorrect, and therefore was not routing correctly to pull the previous testimonial, this was altered and it is working correctly now.
11. Wheel entering the credit card details at the checkout, there were no form errors being shown clearly to the user.
    - The first issue was that there were no validations added to the credit card form's fields used in the forms file, these were added and the notifications were shown to the user.
    - Secondly an alert div was added which made use of [BS4](https://getbootstrap.com/docs/4.0/components/alerts/)'s alert-danger class to highlight the area in red and make the card error clear to the user.
12. While testing registering on a phone, it became clear a user could not do this as they couldn't added the photo required for the profile picture field:
    - The field on the forms file was given 'required=False' attribute to firstly stop errors coming up and preventing the user from registering because the picture was missing. Then a default profile picture was added to the account in the view if this field was left empty by the user on sign up.

#### *Bugs still an issue*

There was an bug in IE where the JQuery used doesn't work, I looked up [Can i use](https://caniuse.com/#search=jquery) and unfortunately it isn't available in any forms of IE.

### *Further Manual Tests*

Asked family and friends working in the field to view the site and run through all aspects of it and report back any potential issues they came across

## Automated Testing

### Validation

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate JavaScript.

No major errors were observed, the only one to note was with CSS and this relates to a known BS problem.

### Jasmine

The main functions were tested in this project with Jasmine as a means of ensuring they were working as planned. The way I approached the testing method was to start small and make sure it is implemented correctly in the first place and work from there. The files for testing are below:

- [Jasmine HTML](https://github.com/brianscan14/XYfitness/blob/master/testing/jasmine/jasmine.html)
- [Jasmine JS specs](https://github.com/brianscan14/XYfitness/blob/master/testing/jasmine/jasmine.spec.js)
- [JS](https://github.com/brianscan14/XYfitness/blob/master/static/js/script.js)

#### *Running the tests*

Firstly make sure the the project is cloned from the GitHub repo and running on your own IDE as outlined in the [README.md](https://github.com/brianscan14/Gourmet_Grub/blob/master/README.md) file. Then:

1. Open the Jasmine HTML file.
2. Run it to see the results in your browser.

To create Jasmine tests of your own:

1. Open the Jasmine spec file.
2. Write the tests using Jasmine's framework.
3. Save the spec and refresh the HTML file.

### Travis

Throughout the course of the project [Travis](https://travis-ci.org/) was used as a means of keeping continuous integration with the Heroku site. If the build was not successful at any stage then there was an issue with the code and this was remedied to ensure the site was deployed successfully.