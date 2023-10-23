# Cakes Cookies and Crumbles

## Contents

- [**Model Relationship Diagram**](#model-relationship-diagram)
- [**Local Development**](#local-development)
- [**Local Development**](#testing)


## Model Relationship Diagram
This is a diagram I created on what the relationship looks like between the models on my backend.
![image](ccc-backend/assets/readme-images/model-relationship-diagram.png)
## Local Development
To run the application locally, I used the below command to start the server in the terminal.
```
$ python3 manage.py runserver
```

## Testing

### Create Recipe

### Edit Recipe
### Delete Recipe

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


