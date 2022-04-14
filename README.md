# Pokedex Starter

## Installation

Make sure you have Python and Pipenv installed on your computer.

Download the repo and save it to your code folder in the class repo. *make sure you download it, don't clone it or it won't upload to the class repo correctly*

If you are not running Python 3.8, edit the last line of the `Pipfile` to refer to your version instead.

Navigate to the pokedex folder in the terminal and do the following:

- `pipenv install` Create the virtual enviroment and install dependencies.
- `pipenv shell` Enter the new virtual enviroment.
- `python manage.py migrate users` Migrate the user model. *this django project uses a custom user model, you MUST migrate the users app before migrating the rest!*
- `python manage.py migrate` Migrate all other models.
- `python manage.py createsuperuser` Create yourself a super user.
- `python manage.py load_pokemon` Load Pokemon into the database.

You're good to go! This Django project comes with a database full of Pokemon, login/logout/registration pages, and a `home.html` template for you to create your Vue app.

# Project Name - Articulate Me

## Project Overview

- Description = A Scholarly Article Website designed for Authors to write and post, articles they wish to share with other like-minded people.
  
## Major Features:
-   User Registration/Account Creation
-   Account Verification
-	Author Login
-	Articles Search 
-	Article submission
-   Article Update
-   Article Deletion
-	Comments submission
-	Article Draft or Publish Status
-	Restful API for Clients
-	Responsive display
-   Gradient Image Background Display
## Future Features:
-	Article Tags
-	Articles Search (Published Articles only)
-	Category List
-	New Category Submission
-	Category Article List
-	Pagination
-	Article Number of Words
-	Article Number of Views
-	Article Social Media Share
-	Markdown Support

## User Stories
- `As a writer, I want a secure web site that allows me to draft and finely publish articles with peers, scholars and students interested in my area of expertise.`

- Tasks:
- register and authenticate new site members
- set up a draft , publish field so draft publications are not visible to other site members.
- setup functionality to submit articles
- store articles, in model/db table.
- retrieve articles, from model/db.
- display articles retrieved from model/db.
- delete owned articles in the db model
- setup functionality to add comments to articles by any valid member of the site.
 
`As a scholar, I would like access to a secure web site of current articles, written by peers and well penned writers, in categories related to my scope of study. I would like to be able to review articles, make comments to articles of interest as well as publishing any of my own work.`

- Tasks:
- register and authenticate new site members
- set up a draft , publish field so draft publications are not visible to other site members.
- setup functionality to submit articles
- store articles, in model/db table.
- retrieve articles, from model/db.
- display articles retrieved from model/db.
- delete owned articles in the db model
- setup functionality to add comments to articles by any valid member of the site. 

`As a student, I would like to have access to a secure, well organized article web site containing published articles I could review relating to my studies.`

- Tasks:
- register and authenticate new site members
- retrieve articles, from model/db.
- display articles retrieved from model/db.
- setup functionality to add comments to articles by any valid member of the site.

`As a developer, I want to create a secure platform where writers and readers can securely draft, publish, modify content, list and retrieve articles, list categories, and submit comments. Additionally I want to provide an API for use by the Administrator and any approved 3rd party interested in the Application.

- Tasks:
- set up application.
- setup SuperUser access and functionality
- register and authenticate new site members
- set up a draft , publish field so draft publications are not visible to other site members.
- setup functionality to submit articles
- store articles, in model/db table.
- retrieve articles, from model/db.
- display articles retrieved from model/db.
- setup functionality to add comments to articles by any valid member of the site.
- SuperUser(Admin) level delete articles in the db model
- SuperUser(Admin) level delete comments in the db model
- set up RestAPI

## Technologies:
-	Python 3.10
-	Django 3
-	VueJS
-	Ajax
-	HTML5
-	CSS
-	Bootstrap 
-	Font awesome
-	SQLite
-	PostgreSQL

### APP Data Model

`Status’ = (
    (0, “Draft”),
    (1, Publish))

‘Article’

- `title` (Charfield)
- `slug` (SlugField)
- `author` (ForeignKey)User)
- `updated` (DateTimeField)(auto_now_add=True) 
- `content` (TextField)
- `created` (DateTimeField)(auto_now_add=True) 
- `status (IntegerField)
- `def__str__(self)

`Comment`

- `article` (ForeignKey(Article))
- `comment_author’ (Charfield)
- `comment_date` (DateTimeField)(auto_now_add=True)
- `def__str__(self)
-`return self.comment_content`

`Categories`

- `title` (Charfield)
- `slug` (SlugField)
- `updated` (DateTimeField)(auto_now_add=True) 
- `content` (Charfield)
- `def__str__(self)

### Admin Models

`ArticleAdmin`(admin.ModelAdmin):

- `list_display`= (`title’, `slug`, `status`, `created_on`)
- `list_filter`= (‘status’)
- `search_fields` = [‘title’, ‘content`]
- `prepopulated_fields` = {`slug`: (`title`,)}

### App Views

`articleList`

- `queryset` (filter on status and order)
- `template_name` (index or main.html)

`articleDetail`

- `model` = `Article`
- `template_name` (index or main.html)

‘addArticle`
- `form` (Article(request.POST or None (I think))
- `if form’ = True (maybe)
  - `article’ (form.save)
  - `article.slug (slugify)
  - `article.author` = request.user
  - `article.save`()
  - `return.render`

`updateArticle`

- `article = get_object_or_404
- `form` (Article(request.POST or None (I think))
- `if form’ = True (maybe)
- `article’ (form.save)
- `article.slug (slugify)
- `article.author` = request.user
- `article.save`()
- `return.render`

`deleteArticle

- `article = get_object_or_404
- `article.delete()

`addComment`

- `article = get_object_or_404
- `if Post = True`
- `comment.author` = (Post.get comment author)
- `comment.content = (Post.get comment_content)
- `newComment` = (comment_author , comment_content)

- `newComment.Article` = Article
- `newComment.save()
- `return.redirect(reverse(article:detail) ??

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

### User Views

`register_request(request):
- `if request.method == “POST”:’
- `form = NewUserForm(request.POST)
- `if form.is_valid():`
- `user` = form.save()`
- `login(request, user)`
- `messages.success(request, “Registration successful.”)`
- `return render (request=request, template_name=, context ={?`
                       
### User Models

`UserSerializer`(serializers.ModelSerializer):
`Meta`
- `model = User`
- `fields = ['id', 'username']` 


### API Models

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


`ArticleSerializer(serializers.ModelSerializer):`
- `owner = serializers.ReadOnlyField(source='owner.username')`

`Meta:`
- `model = Article`
- `fields = ['id', 'title', 'slug', 'author', 'updated', 'content', 'created', 'status,]`

`UserSerializer(serializers.ModelSerializer):`
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'article']
        
`CommentSerializer(serializers.Serializer):`
- `comment_author' = serializers.User()
- `article`  = serializers.CharField(max_length=200)
- `comment_date` = serializers.DateTimeField()

### API View
`ArticleList(generics.ListCreateAPIView):`
- `queryset = Article.objects.all()`
- `serializer_class = serializers.ArticleSerializer`

`perform_create(self, serializer):`
`serializer.save(owner=self.request.user)`

`ArticleDetail(generics.RetrieveUpdateDestroyAPIView):`
-  `queryset = Article.objects.all()`
-  `serializer_class = serializers.ArticleSerializer`

`UserList(generics.ListAPIView):`
- `queryset = User.objects.all()`
- `serializer_class = serializers.UserSerializer`

`UserDetail(generics.RetrieveAPIView):`
- `queryset = User.objects.all()`
- `serializer_class = serializers.UserSerializer`

`Comment(generics.ListAPIView):`
- `queryset = Comment.objects.all()`
- `serializer_class = serializers.Comment.Serializer

`Comment(generics.RetrieveAPIView):`
- `queryset = Comment.objects.all()`
- `serializer_class = serializers.Comment.Serializer

### User View

`register_request(request):
- `if request.method == “POST”:’
- `form = NewUserForm(request.POST)
- `if form.is_valid():
- `user` = form.save() 
- `login(request, user)
- `messages.success(request, “Registration successful.”)
- `return render (request=request, template_name=, context ={  


### forms.py

`NewUserForm(UserCreationForm):`
- `email = forms.EmailField(required=True)`

`Meta`
-`model = User`
-`fields = ("username", "email", "password1", "password2")`

`save(self, commit=True):`
- `user = super(NewUserForm, self).save(commit=False)`
- `user.email = self.cleaned_data['email']`
- `if commit:`
- `user.save()`
- `return user`

	
### Schedule
Mar 29 - Apr 1 – Create a Base, content post-able Django Article Web application with user authentication.

- Acceptance Criteria - functional Base, content post-able Django Article Web application with user authentication.

Apr 4 – Apr 8 – create and complete setup of RestAPI and begin styling for reactive display.

- Acceptance Criteria - functional RestAPI and styling for reactive display.

Apr 11 – Apr 14 – Deployment, Complete last-minute styling, debugging, and polishing

- Acceptance Criteria - Styled Django Article Web application with all initial Feature functionality and any Time Permitting Features permitted by time constraints. authentication,.

Apr 14: Present Capstone 
