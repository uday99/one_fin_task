# one_fin_task



python version
3.9.9


Create a virtual enviroment for the project

python -m env venv

install requirements.txt

pip install -r requirements.txt



Make the changes for the settings.py  for the DAtabase for your local




create migrations for your project

python manage.py makemigrations 
python manage.py migrate





Changes reflect in the database and created tables


Count model table create a record with id =1 and count=0


this is used to count the middle when each every request is made by the server

http://127.0.0.1:8000/register/

payload

========

{
    "username":"ravan2",
    "email":"ravan@gmail.com",
    "password":"ravan33@@"

}

response
=======

{
    "message": "User Register successfully",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxOCwidXNlcm5hbWUiOiJyYXZhbjIiLCJleHAiOjE2OTM5MDczMjgsImVtYWlsIjoicmF2YW5AZ21haWwuY29tIiwib3JpZ19pYXQiOjE2OTM4MjA5Mjh9.Y3ZFtRzRtH27M89wL0tHQWGtpaw215gwwLQ0-9aWwzo"
}




 
TO Get the list of collection And to create the collection pass the jwt token in bearer using postman
http://127.0.0.1:8000/collection/

	To POst creat the list of collection
	
	payload
	=========
           

             {
    
    "title":"prabhas collection",
    "description":"We provide  collection of movies for prabhas",
    "movies":[
        {
            "title":"Bahuballii",
            "description":"got describes the war and the power of a king",
            "genres":"bhaubali",
            "uuid":"8d0ba7b0-d974-45f1-a999c24-e8950975a539"
            
        },
        {
            "title":"sahoo",
            "description":"the revenge of father by son",
            "genres":"gangstar and busineess man",'
            "uuid":"8d0ba7b0-d974-45f1-a999c24-e8950975a539"
            
        },
        {
            "title":"radhyashyyam",
            "description":"the love story of engergitic person",
            "genres":"palmist",
            "uuid":"8d0ba7b0-d974-45f1-a999c24-e8950975a539"
            
        }
        

    ]
}

{
"collection_uuid": c66a7eda-dd6c-4434-9e3c-384964b783c1
}


To get the specific collection data ,update and delete use one url
http://127.0.0.1:8000/collection_uuid/


put payload
==============

{
    "id": 10,
    "title": "Netflix tey",
    "description": "We provide  a series of  different stories",
    "movies": [
        {
            "title": "Game of thrones-ggot",
            "genres": "John snow",
            "description": "got describes the war and the power of a king",
            "uuid":"8d0ba7b0-d974-45f1-ac24-e8950975a539"
        },
        {
            "title": "Never Have I ever",
            "genres": "Devi",
            "description": "webseries of child",
            "uuid":"8d0ba7b0-d974-45f1-ac24-e895097599779"
        },
        {
            "title": "lucifer",
            "genres": "lucifer",
            "description": "lucifer a devil and the fallen angel",
            "uuid":"8d0ba7b0-d974-45f1-a999c24-e8950975a539"
        }
    ]
    
}






GET:
http://127.0.0.1:8000/movies/

It call the third party api 



GEt:
http://127.0.0.1:8000/request-count/
middle per request

POST
http://localhost:8000/request-count/reset/







