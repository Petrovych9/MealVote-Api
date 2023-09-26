# MealVote-Api

## Description

MealVote-Api is a Django project that provides various functionalities related to restaurant management. This README guide will walk you through the steps required to set up and run the system locally.


## Installation

Follow these steps to set up and run MealVote-Api:

1. Clone the repository:

   ```bash
   git clone git@github.com:Petrovych9/MealVote-Api.git
    ```
2. Navigate to the project directory:

   ```bash
   cd MealVote-Api
   ```
3. Create a virtual environment (recommended) and activate it:
     ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```


## Usage

Once the server is running, you can access the MealVote-Api using your web browser or API client. Here are some of the available endpoints and functionalities:

- **Authentication**: MealVote-Api provides authentication using JWT token. You can obtain a token by sending a POST request to `/api/1/token/`. Use the obtained token for authentication in subsequent requests.


- **Creating Restaurant**: To create a new restaurant, send a POST request to `/api/1/restaurants/`.
    
  - before: ![img.png](image/img_2.png)
  - after: ![img.png](image/img_3.png)



- **Creating Employee**: To create a new employee, send a POST request to `/api/1/employee/`.
  - GET all: ![img.png](image/img_3.png)
  - POST create new member:  ![img.png](image/img_6.png)

- **Uploading Menu for Restaurant**: To upload a menu for a restaurant, send a POST request to `/api/1/menu/`.
  - GET all: ![img.png](image/img_7.png)
  - POST create new menu:  ![img.png](image/img_8.png)


- **Getting Current Day Menu**: To retrieve the menu for the current day, send a GET request to `/api/1/restaurants/menus/today/`.
  - result: ![img.png](image/img_4.png)


#### Obtain Authentication Token
To obtain an authentication token, you can send a POST as below:

![img.png](image/img.png)
![img.png](image/img2.png)


### Database

MealVote-Api uses the SQLite3 database by default for local development. 
