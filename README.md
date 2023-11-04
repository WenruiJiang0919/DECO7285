# 1 Overall Architecture

This system combines frontend (Vue.js), backend (Flask), database (SQLite), and Object-Relational Mapping (ORM) tool (SQLAlchemy) to create a robust recipe website. Here are the key components of the architecture.

## 1.1 Frontend (Vue.js)

Vue.js is a progressive JavaScript framework focused on building user interfaces. It handles the presentation layer of the application, including the user interface, user interactions, and view rendering.

## 1.2 Backend (Flask)

Flask is a lightweight and flexible python web application framework built in Python. It is designed to be minimalistic, allowing developers to build web applications quickly and efficiently.

## 1.3 Database (SQLite)

SQLite is a lightweight and embedded database system used to store, manage, and organize the system's data. Key aspects include:

- **Data Tables**: SQLite tables are used to organize and store user data, recipe information, likes, favorites, and comments.
- **Data Integrity**: SQLite ensures data integrity through structured tables and enforces relationships between data entities.
- **Data Retrieval**: Data is efficiently retrieved from the SQLite database and made available to the Flask backend for processing.

## 1.4 Object-Relational Mapping (SQLAlchemy)

SQLAlchemy is an ORM tool that connects the Python application (Flask) with the database (SQLite). It simplifies database interactions and provides an abstraction layer for data operations.

The combination of these technologies results in a flexible, scalable, and efficient system that separates concerns between frontend, backend, and data storage. Vue.js ensures an interactive user interface, Flask manages server-side logic, SQLAlchemy simplifies data operations, and SQLite provides a lightweight and reliable data store. This architecture allows for the development of a feature-rich recipe website with a user-friendly and responsive interface.

# 2 Module Design

## 2.1 Frontend Module Design

### 2.1.1 User Authentication Module

1. **Registration**: Users can register an account.
2. **Login**: Registered users can log in using their accounts.

### 2.1.2 Recipe Management Module

1. **Upload Recipe**: Users can upload new recipes, including information such as name, ingredients, steps, images, etc.
2. **Edit Recipe**: Previously uploaded recipes can be edited and updated.

### 2.1.3 Recipe Browsing Module

1. **View All Recipes**: Users can browse all the recipes that have been uploaded.
2. **Like, Favorite, Comment**: Users can like, favorite, and comment on recipes.

### 2.1.4 User Profile

1. **Liked Recipes**: Users can view recipes they have liked.
2. **Favorited Recipes**: Users can view recipes they have favorited.
3. **Commented Recipes**: Users can view recipes they have commented on.
4. **Uploaded Recipes**: Users can view all the recipes they have uploaded.

## 2.2 Backend Module Design

### 2.2.1 User Authentication Module

1. **User Registration**: Receive user-provided information, create a user account, and store user data in the database.
2. **User Login**: Authenticate user-provided credentials, create and return an access token.

### 2.2.2 Recipe Management Module

1. **Upload Recipe**: Receive user-uploaded recipe information and store recipe data in the database.
2. **Edit Recipe**: Receive user edit requests and update recipe information in the database.

### 2.2.3 Recipe Data Query Module

1. **Query All Recipes**: Retrieve and return information for all recipes from the database, sortable by different criteria.
2. **Like, Favorite, Comment**: Receive user requests to like, favorite, and comment on recipes, and store information about these actions in the database.

# 3 Database Design

The system involves a total of five tables to organize and store data, as illustrated in Figure 1.

## 3.1 User Table

The User table is used to store user information for the application, including user ID, username, and password.

Stored Field Description:
- **id**: A unique identifier for the user, serving as the primary key.
- **username**: User's username, unique and cannot be null.
- **password**: User's password, cannot be null. Typically stores the hash of the password for security.

## 3.2 Recipe Table

The Recipe table is used to store recipe information, including recipe ID, uploader's username, recipe name, image path, cooking time, cuisine, ingredients, description, and preparation steps.

Stored Field Description:
- **id**: A unique identifier for the recipe, serving as the primary key.
- **username**: Username of the uploader, associated with the username in the User table.
- **recipeName**: Name of the recipe.
- **imgPath**: Path to the recipe's image.
- **LengthOfTime**: Time required to prepare the recipe.
- **Cuisine**: The cuisine category to which the recipe belongs.
- **Ingredients**: List of ingredients, stored in text format.
- **Description**: Description of the recipe, stored in text format.
- **Steps**: Preparation steps for the recipe, stored in text format.

## 3.3 RecipeLike Table

The RecipeLike table is used to track which user liked which recipe.

Stored Field Description:
- **id**: A unique identifier for the like record, serving as the primary key.
- **recipe_id**: Linked to the liked recipe, which corresponds to the ID in the Recipe table.
- **user_id**: Username of the user who liked the recipe, associated with the username in the User table.

## 3.4 RecipeFavorite Table

The RecipeFavorite table is used to track which user favorited which recipe.

Stored Field Description:
- **id**: A unique identifier for the favorite record, serving as the primary key.
- **recipe_id**: Linked to the favorited recipe, which corresponds to the ID in the Recipe table.
- **user_id**: Username of the user who favorited the recipe, associated with the username in the User table.

## 3.5 RecipeComment Table

The RecipeComment table is used to store user comments on recipes.

Stored Field Description:
- **id**: A unique identifier for the comment, serving as the primary key.
- **recipe_id**: Linked to the recipe being commented on, which corresponds to the ID in the Recipe table.
- **user_id**: Username of the user who commented, typically associated with the username in the User table.
- **comment**: The content of the comment, stored in text format.

# 4 Deployment Methods

## 4.1 Frontend Deployment

To deploy the frontend, follow these steps:

1. Navigate to the "vuejs" folder.
2. Open a terminal or command prompt.
3. Execute the command `npm start`.

This will launch the frontend application, making it accessible to end-users.

## 4.2 Backend Deployment

To deploy the backend, perform the following steps:

1. Navigate to the "backend" folder.
2. Open a terminal or command prompt.
3. Run the command `python run.py`.

This will start the backend server, allowing it to serve requests from the frontend.
