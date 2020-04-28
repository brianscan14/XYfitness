### XYfitness Testing

#### Manual Testing

###### **Planning**

------

The main goal of this website is to offer a means for a PT to get their brand out on the market and obtain new customers by encouraging them to purchase one of their products. This testing will be carried out using developer tools audit tests, different browsers and also different screen sizes to check responsiveness. Validation tools and automated tests will also be carried out to check the code's validity, as outlined in the "Automated testing" section below. The main means of testing the intended purpose of this website will also be to go through each client story and check if their outcome was achieved.

###### **Implementation**

------

###### Manual Tests

###### *Methodology used*

*This site was tested across the below browsers:*

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

###### *Manual tests carried out*

**Common elements:**

<u>Navbar</u>:

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

<u>Footer:</u>

1. Confirm the footer content stays centered and at the bottom of the page on all screen sizes and pages.
2. Confirm footer logo adjusts width appropriately for differing screen sizes. 

<u>Float Top Button:</u>

1. Confirm button only appears on bottom right of screen when user has scrolled down the page
2. Confirm that the icon changes colour when hovered over
3. Confirm that the user is brought to the top of the page when button is clicked
4. Confirm that the action of scrolling to the top is  slowed down and not a sudden jolt
5. Confirm icon is above any content that is on the page and doesn't have a lower z-index

**Index/Home Page:**

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

**About Page**

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

**Shop**

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

**Single Product Page**

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

**Contact Page**

1. Confirm that the breadcrumb is pointing correctly to this page
2. Confirm if the user is signed in then the forms email field is populated with their email
3. Confirm that the minimum / max lengths used in the forms.py and model file throw up a notification to the user if they are not adhered to and the placeholder text is correct
4. Confirm that all content on the contact page is centered and margined appropriately
5. Confirm that on clicking 'send mail' an email is sent to the python terminal with the sender's email, subject and message content
6. Confirm that this content is also sent to the admin site for the site admin to look at there
7. Confirm that the user receives a **sweetify** success alert telling them their email was sent and they are redirect to the home page

**Testimonials**

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

**Single Testimonial Page**

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

**Login / logout**

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

**Register**

1. Confirm that all content on the register page is margined appropriately and in the center of the page on all screen sizes
2. Confirm that if the user is already logged in and tries to register, they are redirected to home page with an alert form **sweetify** telling them they are already registered
3. Confirm that any form errors are communicated to the user in their respective fields, and not altogether all at once above the form
4. Confirm that if the user tries to use a username or email that is currently on the site, that they are notified of this in the form and a duplicate isn't created
5. Confirm that upon successful registration the user is redirected to the home page with a **sweetify** telling them this and giving them a link to their profile to update it
6. Confirm that if the user chooses not to user a picture on sign up, that the default avatar image is given to them instead
7. Confirm that if the user needed to register to checkout their items in the cart, then they'll be redirected to the delivery details step in the checkout process after successful register, with no **sweetify**

**Profile**

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

**Cart** 

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

**Checkout Page**

*Delivery Steps*

1. Confirm that this page is only accessible if  the user is logged in
2. Confirm that all content on the page is margined appropriately, with the delivery details on the left side, and the cart content on the right side of a centered page, and on smaller screen sizes these cart contents are pushed to the bottom of the page with all content centered correctly
3. Confirm that the forms validations and max inputs are adhered to when entering data and the user is notified appropriately
4. Confirm that total indicated in the cart items summary are correct, and that the edit link points towards the cart view and delivery fee is only charged if there is an apparel item in the cart
5. Confirm that the correct stage in the checkout process is highlighted in the breadcrumb, and changes colour on hover
6. Confirm that the user can only click on the credit card stage of the checkout process icon in the breadcrumb, and that it only changes colour on hover, if they have both entered data on the delivery form already, and there is content in the cart items
7. Confirm that if the user has already filled out this delivery form in their session then the form will be pre-filed with this data upon loading of the page
8. Confirm that the confirm details button is centered to the delivery form and that it changes colour on hover, bringing the user to the next stage of the checkout process if they have items in the cart and the form is filled out correctly
9. Confirm that the confirm details button is disabled if there are no items in the cart and prevents an empty checkout if the user used the back in history tab to get back to this step

*Card Details step*

1. Confirm that this page is only accessible if  the user is logged in
2. Confirm that all content on the page is margined appropriately, with the previous delivery details on the left side with the card form underneath, and the cart content on the right side of a centered page, and on smaller screen sizes these cart contents are pushed to the bottom of the page with all content centered correctly
3. Confirm that the forms validations and max inputs are adhered to when entering data and the user is notified appropriately if they are incorrect, also if the card details have issues that the user is notified with a danger alert div showing them the error
4. Confirm that total indicated in the cart items summary are correct, and that the edit link points towards the cart view, and delivery fee is only charged if there is an apparel item in the cart
5. Confirm that the correct stage in the checkout process is highlighted in the breadcrumb, and changes colour on hover
6. Confirm that the delivery icon now also changes colour on hover, and can be clicked to go back to the delivery form
7. Confirm that the delivery details shown are correct and are what the user entered previously, and that clicking the edit link will bring the user back to the previous delivery page
8. Confirm that the submit payment button is disabled if there are no items in the cart, preventing an empty checkout and incorrect customer charge
9. Confirm that the submit payment button changes colour on hover and is centered, when clicked it redirects you to the thank you page confirming your order, and an email is sent to the terminal, thanking the customer

*Thank You page*

1. Confirm that upon successful order of products on the site, the user is redirected to the thank you page, which thanks them for their order
2. Confirm that all content on this page is centered, and the back to website button points correctly to the home page
3. Confirm that the user's email mentioned in the thank you message is correct
4. Confirm that if the user goes back in history from this page, all of the content from the previous pages is now empty, and none of the confirm details or submit payment buttons are active