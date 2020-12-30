# Online Hosted site link [https://rr-cloth.herokuapp.com/]
# R-Ryan Clothes

1. Ronal Ryan Clothing is designed for online shopping for clothes. RR-Clothes offers a wide range 
   of clothing products for different adult age groups.
2. RR Clothes is designed to look simple, elegant and easy to navigate. Home page is designed with 
   a big search box in the centre of hero section to make search easy and accessible for user. 
   There is a product scroller which works on all screen sizes and user can just look at product 
   with just a click or slide over. There is a big jumbotron which leads to google maps so user can 
   easily find store locations. Users are provided with animated images of most watched product categories. 
   In ‘discount section’ users are given the ability to explore all products with discount offers. 
   The ‘selected items’ displays product information and its images. In the ‘footer’ section, 
   form fields are provided for the costumers to make contact with admins for any further information 
   or queries. Social links are provided to allow costumers to follow store promotions and other news 
   on social media.
3. RR-Clothes has a fully functional Django admin panel, where administrator can manage all database 
   activities and entries. Admin users are provided with on-site CRUD (create, read, update & delete) 
   functionality for product and its variants. Admins require super user credentials to access these 
   features.

# UX

1. RR-Clothes is designed and built to satisfy needs of following kind of user

 * As a buyer I want to view products to checkout if I like something.
 * As a buyer I want to see product in its category so I can selectively compare similar products.
 * As a buyer I want to search product with its name to find out all available options for me.
 * As a buyer I want to checkout different product categories.
 * As a buyer I want to see products with discount.
 * As a buyer before buying products, I want to find out about available colour, sizes and see product images so I can decide what I want to buy.
 * As a buyer I want to check product ratings and other user reviews who have bought that product so I can make a better choice.
 * As a buyer I always want to keep an eye on how much I am spending.
 * As a web browser I want to look at products images and click and scroll to look at available choices.
 * As a customer with complaint, I want to have simple way to complain or write to store owners.
 * As a customer I want to give my reviews and rating to product to help others.
 * As a regular buyer and user of site, I want to have my own account where I can login and logout.
 * As a regular buyer I want to save records of all order that I am making.
 * As an account holder I want to have an ability to recover my password if I forget it.
 * As an account holder I want to have my personalised user profile.
 * As a store owner I want to add new products and delete old products so user don’t see them any more.
 * As store owner I want to have product management section where I can review product and its variant.

 2. Designed wireframes are added in workspace directory
 2. Database models designs are added in directory
 3. Fixtures in Json format are added to workspace directoy.
 4. All images are on workspace directory accessible once fixtures are installed.

# Features

1.	Website is designed with modern navigation bar with collapsible view on different mobile devices.
2.	Website is fully responsive on both mobile and tablets (common models and screen sizes) with changing its design and orientation on screen rotation.
3.	Website displays products and its variants for users to choose from – offering different sizes and colours.
4.	Website is provided with simple form to message store owners.
5.	Website is provided with google maps to find store locations.
6.	Website is provided search box where user can search product they want to buy.
7.	Website is provided with different sorting criteria’s so user can set their preferences.
8.	Website is provided with functionality where user can register user-account/profile, maintain it and view his order history.
9.	Website is provided with functionality to update user password in case if user forget it.
10.	Website is provided with bootstrap toasts to notify user with ‘success, error, warning and info’ pop-up messages.
11.	Website is provided with ability where user can add reviews to product and rate product, so other user can know what they are buying. 
12.	Website is provided with admin site, where store owner can view, add, update and delete product and its variant.
13.	Store owner are provided with AJAX form to view, add, delete, update product colours and sizes.

# Features Left to Implement

1.	Currently, if items are added to the ‘shopping cart’, the cart resets itself when/if the user logs out of the user account. In future update site is going to update with cart database model which is going to hold user ‘add to bag’ information. Shopping cart is related to almost every part of code directly or indirectly and requires time for implementing and testing. 
2.	Ckeditor is used to implement rich text box functionality where user can add images and add text data in html tags. At the moment rich-text box are only implemented on site admin panel but in future development this feature is going to be implemented on ‘add new product’ form. This implementation will allow site-admins to directly add images to product description, with ability to give size details for the added image. 
3.	There is JavaScript error on product detail page which has no visible impact on functioning of product detail page. I am aware of that error and suppose to correct in update release of software.
4.	Favicon error is still not resolved, I have decided to resolve it in future release of RR-Cloth.
5.	I want to write JavaScript/jQuery code where first item in product variant is selected automatically when its size changes on product details, I didn’t have enough time to write and test code. For current use, a message has been added for the users to ensure that the product is selected. 
6.  Size guide is last minute addition to RR-Clothes this part of site is in development. In future update sizes guides are going to be displayed more dynamically and appropriately with updated styling.
7.  At the adding product catergory has no impact on site. If new category is added by site admin, it will not visible on site, unless it is progrmatically added to code. In future I am update, I am 
    planning to update in a way, that when admin adds new category to site, there will be a choice for admin to that what heading of navigation bar that category belongs.

# Technologies used

1.	HTMI5 to implement website project.
2.	CSS3 to implement website project.
3.	GIT POD online web workspace for HTML, CSS, JavaScript, jQuery and python (Django) coding.
4.	Git Hub hosting services and data storage services.
5.	Google Chrome to run GIT POD workspace for development process.
6.	Google chrome Git extension button to log into Git Pod workspace.
7.	Google Chrome Developer tools.
8.	Firefox browser latest version for testing purposes.
9.	Opera latest version for testing purposes.
10.	Safari unknown version for testing.
11.	EDGE latest version for testing purposes.
12.	Bootstrap to design website.
13.	Font awesome free version.
14.	Balsamiq Mock-ups 3 for designing wireframes.
15.	Stripe for payment system.
16.	Different addons and other requirements for site to work information is available on requirements.txt file in workspace folder. 
17.	Slick for showing images on webpage.
18.	Light slider and jQuery zoom for product detail page.
19.	AWS amazon web services
20.	Heroku web hosting services
21. All auth Django packages

# Testing

Following is the list of crucial errors that were discovered while testing application. 

1.	Django admin site is implemented with a feature to show image tag for images and, not to show image URL links. In models image fields were set to take blank values. If there is no image then image tag function will have no image to show and will cause a server error. I have updated model and set it to not take blank values in an add image field. Later same error has repeated itself when image widgets code was added to show images on edit product web page rather than showing image URL. Widget was forcing form to accept empty value in image field and it caused server error. I have updated widget in a similar way to not take blank values for image field. This now has an impact that user must have to add an image when adding a new product to database. In future development I am planning to remove image field from products model. Product can get all its images from image gallery where product foreign field is added to image gallery model. I am still planning and evaluating impact of this change on whole site. Once it understood that it’s an effective change, I will implement it. 
2.	CRUD functionality for size and colour management is implemented with AJAX. There were 3 errors of different nature on both of these pages. First error was with ‘edit form’, which appears on page in form of modal when users clicks edit button. Value which was added to code input field was not updating in database. It was a naming error with input box ID attribute and it is corrected. Second error was with modal, it was not disappearing when ‘save changes’ was clicked to submit values. I discovered that modal attribute is required to target separately in JavaScript code to hide modal when ‘save changes’ is clicked. Third error was with ‘edit and add’ functionality. Edit button on webpage which was added using JavaScript. It was completely white and not readable. For some reason bootstrap form formatting class, added using JavaScript code, was cause of the error. I have removed that class from JavaScript code and it has resolved error. There is a consistency issues with edit and delete buttons, they are not dark grey and green as edit and delete button on product management page. I am aware of this and planning to correct them in update version.
3.	If site registered user adds products to cart and then later login to account using different machine, there will be no information available for cart items as information is saved in browser sessions and cookies. Add to bag functionality required updating with database model where registered user can save information about cart at server side in database. It is complex part of site and it has direct or indirect involvement with all other parts of site. I am planning to update this part of site in future release version.
4.	Stripe webhooks were implemented to control scenarios like where user has made payments but for some reason their order history in not updated to database. Stripe payment intent will have all order information in it and can be update to order database using webhook handlers in case if they were missing. While testing it was discovered that webhook payment intents on Stripe site were failed. First it was understood that the problem was with given endpoints on Stripe site. Error was solved by deleting and adding new end point at Stripe end. This solved initial problem but later it was discovered that on every order that was made there were two emails sent out to customer, one from boutique ado server and other from RR-cloth server confirming that order is received. Environment variables in settings for Stripe API keys were save with same names and causing conflicts. To solve error, I have changed all boutique ado environment variable names and there were no more conflicts since confirmation emails are sent by servers where orders are made. 
5.	Django SQL raw query was used to distinct size so only one of each size appears in select box on product detail page. Postgres databases are not compatible with Django raw SQL queries. Alternatively, distinct () Django query is not compatible with db.sqlite3. To solve this issue so that the both databases will work. I created variable in database section of setting.py to identify which database is used and with help of that variable I updated product view that each query gets select in respect to its compatible database engine.
6.	Home page is implemented with customer support form where site user can easily contact and send messages to site administrators. During development of this feature there was console error that user id is required. User Id was provided in JavaScript code, later it was discovered that provided CDN link was not compatible with code that was written. After changing CDN link, form was successfully sending emails.
7.	Google maps were not visible on home page and there were no browser console errors. After careful evaluation it was discovered that google maps are printed outside of browser viewing error. To solve this error, google map div was updated with height styling to make google maps visible in browser screen area.
8.	Site is tested on different machines and browsers; it was discovered that page headings were hiding behind navbar on full screen size. To fix error different media queries are given and margin tops are added to page title div to give extra spacing. 
9.	There is no inventory system to track available quantity of products. In future update I am planning to implement inventory system for products. Quantity of products in order is going to subtracted from total quantity of products – currently, the website has the capacity to 

### Instructions to Use Site

1.	Site is tested on different scenarios and it works well. There are errors that can be made by site admin, which can cause the site to behave abnormally. I have added cautioning code for those errors to make sure that the site doesn’t break and give server error. 
    But there are some, I have discovered when I was adding product information and making obvious mistake to check if the site breaks. 
    Following are the results of impact that site can have with due to admin mistakes.

* If admin adds a new product and then set it to ‘has variants’ and then forgets to add variant information to product. This was causing site to break and show server error on product detail page. To solve error, I have added if-else logic to check if product has variants and if there is no variant information then site will inform user that its an admin error and contact the admin. And if admin logins with superuser and click same product to view, admin will be directed to product management page with instructions that add variant information and it has cause user inconvenience. 
* For testing I changed ‘product has variant’ value to false from true. This particular product has 9 different variants with information about different size and colour. I have checked its impact on product detail and product management pages. There was no impact on either of the pages, only variant information was not available any more.
* In second attempt I have changed same product variant from size-colour to only colour and set ‘has variant’ value to true. It has no impact on product management page all information was displayed but on product detail page there was only one colour visible. To solve that error, site admin has to delete size information manually from all variants. In future update I am planning to add caution for this sort of errors.
* In future upgrade I am planning to add cautioning for all these scenarios where site admin can make mistakes. When I was developing site, I was only testing for coding errors, I never assumed what when site admin is going to make mistakes. I don’t have enough time to add all cautioning’s and then go thorough testing. 

2. In earlier version of evolving site I was not giving user full cotrol on updating variant information. There were different django forms for add and edit variant information, 
   for example. variant-color form, size-color-form and form where all size-color information can be added. My mentor suggested me to give user ability to choose variant image in add/edit 
   forms. Now in variant form admin user has ablity to choose from product image gallery that belongs to the variant. Since these new forms are updated admin user is required to follow 
   below given rules:
   * If product "has-Size is true" then admin should not leave product "varaints" to None. In future update I am adding code to force this rule.
   * Admin add varaint information correctly so there will be no inconvinence to shopper and site owners. 
   * As a programmer I have made sure that none of these mistakes break site and show server error. In future update I am going to force these rules.   


# Deployment

###### Important Note:
        All-important packages that are required to run RR-Cloths are included in requirements.txt file inside project directory folder. Python command (pip3 install -r requirements.txt) can be used to install these requirements.

## Environment Variables:

1.	To host site on local server or web server Django secret key and other API keys values are required in environment variables. These API keys are obtainable if AWS and STRIPE sites. To use services of AWS (amazon web services) their accounts are required. Links for creating Stripe and AWS are provided respectively ( [https://dashboard.stripe.com/] ) , ([https://aws.amazon.com/] ). Please make sure to read AWS service charges information before registering your account. Please read information manual before using these services.
2.	 List of these secret is given below:
* SECRET_KEY: This is application secret key required to run application.
* Stripe API (Application Programming Interface) Keys are required for payment system to work, checking out and webhooks handler’s functionality. Stripe account is required in order to get these API keys.
* a)	STRIPE_PUBLIC_KEY
* b)	STRIPE_SECRET_KEY
* c)	STRIPE_WH_SECRET_MS4
* Static and media files are stored using amazon webservices (AWS) for online hosted application. Products images and static files are located on GitHub workspace as well. If you are connected to db.sqlite3 database all image files are going to be fully functional. If it is required to host application on webserver to store static and media files webhosting services are required. To use site default settings following API keys are required from amazon web services. To get these keys AWS account is required.
* a)	AWS_ACCESS_KEY_ID
* b)	AWS_SECRET_ACCESS_KEY
* c)	USE_AWS (set USE_AWS to true in order to site logic to work using amazon web services)

# Deploying Site on Heroku:

1. Site is hosted using Heroku web services all above variables values are set and saved in heroku app 
   settings inside config vars section. For online database RR-Cloth is using heroku postgres database. 
   URL value of heroku postgres is saved in config vars similar to all above config vars with variable 
   name DATABASE_URL. Site logic is set in a way if value of this variable is given site will use 
   online postgres database and if not, site will use db.sqlite3 database available in workspace.
2. When new database is set then migrations are required to execute again. (Python3 manage.py showmigrations) 
   can be used to see migrations required to migrating. To migrate all migrations python3 manage.py migrate 
   (python command) is required. Database data is saved in json format inside fixtures folder. 
   Python command (python3 manage.py loaddata db.json) can be used to load data. 
   Without loading these fixtures site will not be functional.
3. To host site using heroku hosting services heroku account is required please visit heroku website to 
   create an account please use link in brackets to create account ( [https://signup.heroku.com/] ). Procfile and requirements.txt are already available in workspace directory these files are required by heroku to host project on world web services. If files are missing you can take following steps: 

* pip3 freeze –local > requirements.txt, this command will create requirements file, 
  this file is required by heroku to install requirements before deploying project.
* To install these requirements use following command (pip3 install -r requirements.txt)
* Create file with name Procfile in your workspace. Procfile is required by Heroku to know 
  entry point for project. And add following code to it, please make sure don’t to leave empty 
  line under the code. (“web: gunicorn RR_Clothes.wsgi:application”)
* Heroku platform was installed on my workspace with help of code institute template called 
  Code-Institute-Org/gitpod-full-template. To install heroku platform on workspace 
  please follow the link.([https://devcenter.heroku.com/articles/heroku-cli#download-and-install]), 
  On same link instructions to login to heroku from workspace terminal are given. Once login with user name 
  password then git push heroku master command can be used to push workspace and built online hosting server.
*  For automatic Deployments use following steps. 
    a. From deploy tab on heroku web page, in deployment method section, click option “GitHub connect” to select GitHub.
    b. Then search repository to connect to details were provided which includes ac-count details and repository name.
    c. When repo is found use button below connect to this app.

#  Deploying Site using GITHUB – GITPOD
Any appropriate development environment can be used for example sublime, PyCharm, visual code etc. 
After downloading project files from GitHub repository following steps are required to deploy site on local web server.

1.	Python command (pip3 install -r requirements.txt) to install all requirements.
2.	Run database migrations using following commands. Please be aware if you haven’t given any online database address then site is going to use default db.sqlite3 database built-in on workspace.
    a.	python3 manage.py makemigrations
    b.	Python3 manage.py migrate
3.	Install database fixtures from file provided in workspace directory in folder fixtures. Use command given in brackets. (“python3 manage.py loaddata db.json”) to install all fixtures.
4.	Create superuser to access Django admin panel, use command in bracket to create super user (python3 manage.py createsuperuser).
5.	Once all setup use command “python3 manage.py runserver” to start your local web server.
6.	Use superuser credentials to login to Django admin panel.
7.  Please use all informaiton about environment variable give above under enviornamnt varibale heading. 
    Without enviornment variables site is not fully functional.

# Content 

1. Google maps API is used on home page.
2. Footer form with ability to send email is implemented using send Email functionality provided by www.emailjs.com.
3. Product prices and ratings are given randomly.
4. Text on home page is developed from marketing promo lines and written by myself to fill in appropriate content. 

# Media

1.	All product images are taken from Kaggle.com.
2.	Images on homepage are taken from Unsplash.com, pixabay.com and pexels.com 

# Acknowledgements and Crediting to other developers

1.	To learn more about programming and get additional knowledge, I have followed along following video tutorials and coded these projects. 
    Coding that I learnt from below mention projects, has helped me to design and program RR-Clothes.   
    •	Boutique ado (Code Institute).
    •	YouTube videos made by channel called Professional Cipher ([https://www.youtube.com/watch?v=uQtIqh9mEgM&t=660s]). 
    •	YouTube videos from “Yuksel CELIK, PhD” ([https://www.youtube.com/watch?v=UByiPW2zRy4&list=PLIUezwWmVtFXaHcJ63ZM6uOJdhMrnZFFk]).
2.	For image slider functionality I have taken code from following site. ( [http://sachinchoolur.github.io/lightslider/examples.html] )
3.	For product and category hover effect I have taken code from following site. ([https://miketricking.github.io/bootstrap-image-hover])
4.	For Image carousel, image slides, image zoom effects and other frontend image representations I have used libraires provided by slick and jQuery-zoom 
5.	I have heavily relied on Django documentation, stack overflow, css tricks and some other sites which appeared in my search results for error troubleshooting.
6.	I want to thanks to code institute tutors who helped me emotionally and technically in development of my project.
7.	I want to thanks my Mentor Dick Vlaanderen who helped me emotionally, and technically during the development process.

