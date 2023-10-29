# Cakes Cookies and Crumbles

## Contents

- [**Model Relationship Diagram**](#model-relationship-diagram)
- [**Local Development**](#local-development)
- [**Linting**](#linting)
- [**Testing**](#testing)
- [**Deployment to Heroku**](#deployment-to-heroku)




## Model Relationship Diagram
This is a diagram I created on what the relationship looks like between the models on my backend.
![image](assets/readme-images/model-relationship-diagram.png)

### User
This table is supplied by Django it is used to hold user information such as email address and password.
The userID will be used to create relations on models that the user owns. 
### Recipes
This model stores the recipe information such as the title, ingredients and instructions etc. The recipe will belong to a user.
### Categories
This model stores the filter categories that help the user find a specific recipe that they desire. (Cakes, Cookies and Categories). The user can assign more than one category to a recipe.
### Ratings
Ratings has a relation to the user and the recipe and has the value for the recipe's rating (1-5).
This is later used to calculate the recipes average rating.
### Favourites
This is used to mark a specific recipes as favourited by the user this is so the user can find their favourites using the relationship.
## Local Development
To run the application locally, I used the below command to start the server in the terminal.
```
$ python3 manage.py runserver
```

## Linting
I installed a PyLint extention for VSCode that listed problems with linting. I then had to fix manually.
See below for examples of pylinting issues that I have fixed.
![image](assets/readme-images/readme-linting.png)
![image](assets/readme-images/readme-linting2.png)

The image below shows some issues that I couldn't fix.
![image](assets/readme-images/readme-linting3.png)


## Testing
### Create Recipe
I made an API request on the recipes end point and this returned back a 400 bad request. This is because there are validation errors. In the example below, you can see the errors from the server.
![image](assets/readme-images/reademe-tesing-validation-error.png)  

I made an API request on the recipes end point and this returned back a 201 success. In the response is my recipe in JSON
![image](assets/readme-images/readme-testing-create-recipe-success.png)


### Edit Recipe
I made a PUT API request to the recipes/29/ end point where 29 is the ID of the created test recipe from the last example.
It has returned back a 200 and make a note that I have changed the ingredients from "milk" to "custard and bread crumbs".
![image](assets/readme-images/readme-testing-edit-recipe.png)

### Delete Recipe
I made a DELETE API request on the recipes end point and this returned back a  204 no content. This means that the recipe I created, was deleted sucessfully.
![image](assets/readme-images/readme-testing-delete-recipe.png)
### Favourite Recipe        
### Paginate Recipe
I made an API request to the recipes end point and this returned back a paginated result where I had a count property for the total amount of recipes, next and previous properties for next and previous page URLS and a results property for the array of recipes. 
![image](assets/readme-images/backend-testing-pagination.png)

### Recipe Filters
I made an API request to the recipes end point with a query parameter for categories with the category `Cakes`.
This returned a paginated response where all recipes had a `Cakes` category. 
![image](assets/readme-images/backend-testing-category-filter.png)

### Recipe Favourite Pagination.
I made an API request to the recipes end point with a query parameter for `isFavourited` set to True. This returned a paginated response where all recipes returned contained a favourite relationship for the signed in user.

![image](assets/readme-images/backend-testing-favourtes-filter.png)
### Recipe Rating
I made POST API request to the ratings end point with a payload for recipe with ID 4 and my rating of 7. This returned back a 400 response which is to be expected as my rating value is higher than the maximum.

![image](assets/readme-images/backend-testing-ratings.png)

I made a POST API request to the ratings end point with the same payload as above and changed the value to 4, within the validation rules. This returned back a 201 status code and the body of my rating model.

![image](assets/readme-images/backend-testing-ratings-2.png)

I tried to make the same request as above but received a 400 response because I cannot create duplicates.

![image](assets/readme-images/backend-testing-rating-duplicate.png)

## Deployment to Heroku 
1. First, I clone the repository from GitHub.
![image](assets/readme-images/clone_backend_readme.png)<br>
2. Then I copied the SSH link.
![image](assets/readme-images/copied-readme.png)<br>
3. I then used the git clone command to clone to my local machine.
![image](assets/readme-images/clone_link_readme.png)<br>


This is how I deployed the backend of this site to Heroku
4. I Created a new app on Heroku
![image](assets/readme-images/deploy-to-heroku1.png)<br>
5. I gave the app a unique name and chosen the region where I am from.
![image](assets/readme-images/deploy-to-heroku2.png)<br>
6. I then linked my Github backend repository to Heroku.
![image](assets/readme-images/deploy-to-heroku3.png)<br>
7. I then inputted all the necessary config vars to Heroku.
![image](assets/readme-images/deploy-to-heroku4.png)<br>
8. I input the Python buildback.
![image](assets/readme-images/deploy-to-heroku5.png)<br>
9. I created the Procfile that so Heroku knows what profile to run? 
![image](assets/readme-images/deploy-to-heroku6.png)<br>
10. I chosen to deploy the main branch.
![image](assets/readme-images/deploy-to-heroku7.png)<br>
11. I added the Heroku app host to my origins for CORS.
![image](assets/readme-images/deploy-to-heroku8.png)<br>
