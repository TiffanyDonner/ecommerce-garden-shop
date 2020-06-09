![Garden Shop Site Header Image](static/readme/readme-header-screens-01.jpg)
# Garden Shop
The Garden Shop is a full stack ecommmerce website built with the neighborhood garden store in mind. 

[![Build Status](https://travis-ci.com/TiffanyDonner/ecommerce-garden-shop.svg?branch=master)](https://travis-ci.com/TiffanyDonner/ecommerce-garden-shop)

## Table of Contents

1. [Demo](#Demo)
2. [Project Purpose](#Project-purpose)
3. [UX](#ux)
    - [User Stories](#User-stories)
4. [Features](#Features)    
5. [Technology Used](#Technology-Used)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)

## Demo
A live demo of the website can be found [here](https://ecommerce-garden-shop.herokuapp.com/).

## Project Purpose
To build a fullstack web application, using HTML, CSS, JavaScript, Python+Django with a relational database.
That can take payments through Stripe.

## UX
The strategy of designing this website was to give the user a very structed way to shop online by using 
a typlical ecommerce store feel without all the clutter. The use of bright and vibirant colors and high quality 
images is meant to each users visit a happy one. 

### The ideal Garden Shop User is:
- Reading and Speaking English
- Like or would like to garden
- Located in and around a neighborhood AoE (Anywhere on Earth)
- Would like to find inspration for their their garden

### Features
- 


Wireframes designed in Adobe Illistraitor. [Wireframes](https://lh3.googleusercontent.com/L66DA5NrPD_CTLQ1ytZsl2Ywbk4LUaF7R0C1x-D2QhugF17I_jtJO0d-tjH_1ureV0gtvXt4degp1EW-mkC8Q-PRwzuLeClvLvAS9haZvsF6P7thf_Nsmocxm2MaE_RlW3RNZiWBA0s=w2400)

### User Stories
#### Magnus
Magnus is a landscape designer with a large client base. He enjoys neighborhood garden centers for their personal touch
and individualized attention.
- Features he needs:
    - An easy way to search specific plants for his clients.
    - A place he can ask questions and get knowable answers.
    - An area to review his order history.
    - Fast delivery to his job sites

#### Lina
Lina is retired and enjoys having flowers in her garden. She doesn't drive anymore so having a store that 
delivers is a prioty for her.
- Features she needs:
    - To be able to shop and pay for her products online.
    - An easy way to contact the store if she has any questions.
    - Product discriptions in order for her to make decistions on what to purchase.

### Design


## Features
### Home Page
- Includes a full width, jumbotron, image that is static and adds depth to the page.
- Features products
- A quotes carousal with store reviews.
- A responsive navigation bar and footer with easy to navigate links to pages and user account.

### Account Page
- Site users can register, login or logout. This information is then stored in the database.
- Users can view order history dates.
- The navigation bar updates to the user staus (Logged in or out).
- Logged-in users can add, update, delete account information in the database.
- Users can update their password when logged in.
- User can get an email notification to reset a forgotten paswords.
- Messages in breadcrums are used to help the user know where they are in different processes.

### Shop
- The search bar is always located at the top of the page. It can filter by words in product names and discriptions.
- Products can be filtered by categories in the navigation bar and footer.
- Users can add items from the products page or product description view.
- The cart displays an image of the product, it's name and price.
- Product quanities can be adjusted at the product or inthe cart.

### Checkout
- Users must be logged in to checkout. Orders are then same in their account.
- Products being purchased with totals display in checkout.
- Use cardnumber 4242424242424242 to check out with Stripe testing.

### Contact Page
- Allows the user to easily contact the store with confirmation.

## Features Left To Implement
- Add a backend system to keep track of product quanities.
- Add Favorites as a filter to populate automatically to home page in Favorite Products instead of being hard coded.
- Add a blog to populate featured posts on home page.
- Add size, weight and features to product details.
- Redirect user during checkout to payment information instead of backto the homepage.
- Add product reviews
- Add product preorder to store.
- User favorites.
- Order details in the user account.
- Social Media

### Technology Used
|  |  |
|----------------------------------|----------------------------------|
| [HTML](https://www.w3.org/html/) | To provide the structure of the webiste |
| [CSS](https://www.w3.org/Style/CSS/Overview.en.html) | To make the website look better visually. | 
| [jQuery](https://jquery.com/) | JavaScript library | 
| [Python](https://www.python.org/) | To manage the database | 
| [Django](https://www.djangoproject.com/)| Python web framework  |
| [Heroku](https://heroku.com)  | PostgreSQL database service |
| [SQlite3](https://www.sqlite.org/index.html) | provided by django |
| [AWS S3](https://aws.amazon.com/s3/) | Object storage service  |
| [Stripe](https://stripe.com/en-se) | Online payments |
| [Github](https://github.com/) | File hosting |
| [Gitpod](https://gitpod.io/) | Code editor and version control |
| [Google Fonts](https://fonts.google.com/) | 'Montserrat', 'Esteban' | 
| [Bootstrap](https://getbootstrap.com/) | Front-end open source toolkit |
| [Font Awesome](https://fontawesome.com/6?next=%2F) | Icons |
|  |  | 

## Testing
- Manual Testing: All aspects of the website were tested throughout the process.
    - Navigation and dropdowns, Search, Adding and editing cart, Password Resets, Checkout forms, Database, Regiter, Sign, Logout, Update Profile...
- W3C Markup Validation for validating the HTML.
- W3C CSS validation was used for validating the CSS.
- JS Hint for JavaScript validation.
- Python Testing through manage.py
- Travis CI continuous integration.

## User Testing
### Questions and Answers
(Each Tester was asked to send a screenshot of the home page and the user profile page.)

#### When you clicked on the [link provided](https://ecommerce-garden-shop.herokuapp.com/), was the website purpose clear?
- User A, "Yes, it was clear. I was able to add items to my cart and checkout very easily."
- User B, "Yes, good choice on coloring. Really brings you in."

#### After you filled in the registration form, were you able to intuitively know what your next step was?
- User A, "Yes! Go Shopping!"
- User B, "Yes, I used the navigation menu to tofind products.

#### When you add a product to the cart, is it easy to update your quanity and find your next step?
- User A, "Yes. continue shoping."
- User B, "Yes, but I wasn't able to view what products I purchased. Just the order date."
    - Update: These features will be added in the next update.

#### Would you visit this website again?
- User A, "Yes, if you got more products."
- User B, "I mean... yeah. If I was into plants."

Any suggestions given by users have been added above in [Features Left To Implement](#Features-Left-To-Implement)

### Devices Tested and Reponsiveness
✓ The site is accessible to everyone on all devices.<br/>
✓ Both Windows and Apple computers in:<br/>
    - Chrome<br/>
    - Firefox<br/>
    - Microsoft Edge<br/>
✓ Samsung:<br/>
    - Galaxy S9<br/>
    - Galaxy S9 Plus<br/>
    - Galaxy S5 Note<br/>
✓ Caterpillar Android Device<br/>
✓ Apple:<br/>
    -iPhone 11<br/>
    -iPhone 10<br/>

## Deployment

#### 1. Create a new [repository](https://github.com/TiffanyDonner/paw-purfect-planner) in GitHub
1. In the upper right corner use the + to bring down the menu. And select Repository.
2. Select your account from the owner dropdown menu.
3. Give your repository a name and optional description.
4. Choose the repository's visibility and initialize this repository with a README.
5. Click Create Repository

#### 2. Create Your Website
1. In GitHub navigate to your repository.
2. Click on the green Gitpod button to open your development environment.

#### 3. Create a New Project
1. Start a new project in Django
2. Add your allowed hosts to the settings.py to run manage.py
3. Push your files and folders while updating git by adding files with commit messages to keep you organized through development.

#### Local Deploy
1. In the command line: *pip3 -r requirements.txt*
2. Create an *env.py* file, add it to a .gitinore file, and add you Secret Keys.

#### 4. Create an App in Heroku
1. Sign in to your [Heroku Account](https://heroku.com/) and create a unique app.
2. Navigate to Deploy and choose GitHub as your deployment method.
3. Navigate to App connected to GitHub and connect your GitHub Repository.
4. Then Enable Automatic Deploys.
5. Now your Heroku app will update every time you push GitHub (git add ., git commit -m "", git push)
6. Navigate to the setting tab and your environment varible to Congig Vars.
7. 

## Credits
- Code Institue, [Ecommerce Project](https://youtu.be/Cy6BDyfs7DM)
- My mentor Brian Macharia, Code Institute Tutors, and Slack Group!
- Logo Created with Adobe Illistraitor. Plant image in logo anf favicon from: [YAWD](https://ya-webdesign.com/imgdownload.html)
- Quotes Carousal Code from [BootStrapious] (https://bootstrapious.com/p/bootstrap-carousel-with-quotes)
- Reduced Image Sizes with [TinyPNG](https://tinypng.com/)
- Max Goodridge [Django Tutorial](https://www.youtube.com/watch?v=JmaxoPBvp1M&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=18)
- MDB [Bootstrap Templates](https://mdbootstrap.com/docs/jquery/forms/contact/)
- Codemy.com [Contact Pages](https://www.youtube.com/watch?v=w4ilq6Zk-08)
- Product discriptions are from Wikipedia
- Django Tests [Help Code](https://www.valentinog.com/blog/testing-django/)
- Shadow Effect on home page from, [codesdope.](https://www.codesdope.com/blog/article/25-creative-css3-text-shadow-effects-you-cant-miss/)

### Image Credits
- Jumbo Photo on index.html - Image by [Kerstin Riemer](https://pixabay.com/users/kriemer-932379/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4357409) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4357409)
- Cherry Photo from [Free Photos](https://pixabay.com/photos/cherries-fruit-tree-harvest-839864/)
- Pumkin Photo [Public Domain Pictures](https://www.publicdomainpictures.net/en/view-image.php?image=195241&picture=pumpkin-patch)
- Pineapple Plant Photo Image by [振鐸 李](https://pixabay.com/photos/pineapple-%E9%B3%B3-pear-potted-plants-%E9%A0%82-816527/) from Pixabay
- Blue Gloves photo [S. Laiba Ali, UnSplash](https://unsplash.com/photos/95d6vqxarpM)
- Cafe Table Image [PXHERE](https://pxhere.com/en/photo/114095)
- Wheelbarrow Image [PXHERE](https://c.pxhere.com/photos/d9/97/barrow_cart_equipment_flower_garden_gardening_grass_green-1159034.jpg!d)
- Clippers [Pixabay-Bru-nO](https://pixabay.com/photos/autumn-scissors-pruning-shears-tool-2759887/)
- Basil [Pixabay-tookapic](https://pixabay.com/photos/basil-herbs-food-fresh-cooking-932079/)
- Coffee and cake [Pixabay-Pexels](https://pixabay.com/photos/cake-cappuccino-ceramic-coffee-cup-1839134/)
- Dahlia [Pixabay-hansbenn](https://pixabay.com/photos/flower-blossom-bloom-dahlia-2019061/)
- Lilac Bush [Pixabay-Didgeman](https://pixabay.com/photos/lilac-purple-flowers-violet-4181712/)
- Landscape Design(Man Holding Flowers) [Pixabay-suetot](https://pixabay.com/photos/gardener-gardening-flower-gerbera-4186301/)
- Wild Flowers [Pixabay-pasja1000](https://pixabay.com/photos/flowers-meadows-grass-plant-nature-3571119/)
- Profile Photos [Unsplash](https://images.unsplash.com/)
- Conifer [Pixabay-Pexels](https://pixabay.com/photos/conifer-evergreen-green-environment-1867371/)
- Bird Feeder [PXhere] (https://pxhere.com/en/photo/562747)
