## File structure
    .
    ├── app                     # Application fies
    │   ├── templates           # HTML files for webpage   
    │       ├── base.html       # Base style template for website  
    │       ├── index.html      # Landing page  
    │       └── content.html    # Content page
    │   ├── app.py              # Entry point for flask app w/ routes
    │   ├── config.py           # Application-level config options
    │   ├── grabber.by          # External API scraper
    │   └── requirements.txt    # App requirements file
    └── ...

## Write-up
Hey there,

Thanks for taking the time to review. I've built a relatively simple
application that queries an external API, stores the data in memory,
and displays it as a simple time-series bar graph on a webpage.
For now, it displays population data over time for the United States.
This could be relatively easily extended to capture data from many
countries as well, allowing the user to see many different population
charts. Overall, the logic itself is very simple and thus I didn't
consider the addition of unit tests to be meaningful just yet.

I used some basic Bootstrap for the look and feel, and Jinja templates
to help keep the HTML files relatively clean. CSS and JS features are
written in-line just to keep project structure clean for a small app
like this.

Unfortunately, I ran out of time to build the last bonus feature I wanted to add.
This application should have two or even three docker containers networked together
via docker-compose. One contains the webserver, one contains the API scraper, and
optionally one would contain a database the other two could communicate with.
Instead of using a database, we could have the API scraper simply POST data
to the webapp over an endpoint. However, this has concurrency and security problems.
It makes far more sense to follow a three-container pattern such as:

```
API Grabber --- Writes to ---> Database --- Read by ---> Webapp
```

The database would handle consistency, concurrency, and authentication for us.
This would also be dramatically more efficient in terms of the API use, as we
wouldn't need to query the full dataset every time which would allow us to do things
like add support for many different countries without flooding the API.

That's about everything for now. Have a great day!

## Run

To run with public Docker repo:
```commandline
docker run -d -p 80:80 jtaylorapps/bascom-demo
```

To build and run with Docker:
```commandline
docker build -t bascom-demo:latest .
docker run -d -p 80:80 bascom-demo
```

To run with Python:
```commandline
python3 app/app.py
```

And head on over to http://127.0.0.1/
