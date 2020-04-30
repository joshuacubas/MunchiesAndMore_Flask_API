# Munchies and More !
#
#####  Flask Backend Api
#
##### Project 3 @ GA
#
###### Creator : Joshua Cubas
#
#
[Imgur](https://i.imgur.com/YCCtiwm.jpg)
### App Basic Info:

 - There will be site that lets users upload and view recipe ideas 
 - each user will be able to  create a personal login
 - each user can create edit and delete THEIR OWN recipes 


### Backend

- will handle authentification and control users being able to login with flask-login
- models in python will be created for 'creator' and 'recipe'
- model for "creator" is {username: String type}
- model for "recipe" is { name: Strign type, ingredients: String type, directions: String type, vegan: Boolean type, gluten_free: Boolean type, creator: ForeignKey to creator of recipe }
- 'creator' and 'recipe' databases will be configured with sqlite3 tables
- the back-end flask api will be connected to the react front-end
- will have create, edit, update and delete routes for 'recipes'
- will have create route for 'creators'
- 'creator' password data will be encrypted with bcrypt
- only the 'creator' associated as the creator of a given recipe can edit or delete that recipe