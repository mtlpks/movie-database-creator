Movie Database Creator

The purpose of this project is to train creating databases from websites through Python. The project itself takes the Top 250 Movies from IMDB, parses it through BeautifulSoup, creates the database using mysql and displays it with pandas.

So, we begin by using requests on the link provided. With the html file contents, we BeautifulSoup through it and use find_all to find our needed parts and append it to a list.
Then, we create a loop that will use regex to find just the information we need, and create a dict entry with it.

With the dict ready, what we have left is to create a database with our info. We create it through mysql, and then loop through the dict using a INSERT INTO statement to fill our database.
Having used SELECT on the tables, we display it in the screen by using pandas.

To run, simply download the files and run database_creator.py.
