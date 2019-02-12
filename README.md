## One Minute Pitch
## Picth is a web application meant to help hard workers on the current affairs
### 01 February 2019
#### By **[Francis T Karagu]**

## Description
News Highlight is a web application that is meant to catch up hard workers on current affairs happening all over the world. The website has the home page, that has a list of all sources of news sorted in categories. A user will have to click on New Sources in order to get a list of news sources and content.

## Specifications
### Who is the target User?
* Anyone who wants to catch up on current affairs happening all over the world

### Front-end/User Interface Logic Objectives
* By default the page will load and provide three options
* Home: This is the current landing page
* News Article: This will contain news articles from different source.
* News Source: This will contain news source from different news platforms.

### Back-end/Business logic Objectives
* The application is using API links to pick data.
* Once a link is clicked i.e. News Article or News Sources routing is done and a specific web page is loaded.
* The pages are automatically linked to API links and API key is passed and data is then loaded on the page.

### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View Home | Click on the Home | Loads the home page. |
| View Article | Click on the New Article | Scrolls the select article and click view details to read articles. |
| View Source | Click on the New Source | Scrolls the select the source and click view details to read articles from that source. |

## Prerequiites
    - Python 3.6 required

## Application link
Here is a live working link https://newshighlightapi.herokuapp.com

## Set-up and Installation
    - Install python 3.6
    - Run chmod a+x start.py
    - Run ./start.py

    Incase you need to access / improve the application please follow the below steps
    1.  Use this command $ git clone <https://github.com/Fkaragu/NewsHighlight.git>
        This will clone the projects repository into a local folder on your device.
    2.  Open the files with an editor( preferably Atom. )
    3.  Study the code. learn from it. Improve on it.

## Known bugs
No known errors.

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap
    - JavaScript

## Support and contact details
In case of any problems reach me through my email:fkaragu@gmail.com

### License
Copyright (c) {2019} **{Francis Thande Karagu}**
Permission is hereby granted, free of charge, to any person willing to obtain a copy of this program for personal use. However if the program will be used for commercial gain then a royalty fee will have to be paid to the author of the program.
