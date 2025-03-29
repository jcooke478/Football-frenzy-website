# Football-Frenzy-Website
PROJECT IDEA:
My goal for this project is create a webpage in which you can find the names of football players who have played for any particular combination of teams you might be interested in. i.e. which players have played for both manchester united and arsenal? 

To do this i need to scrape player data from a site which contains information on all football players in the top 5 leagues with all the teams they played for, the seasons they played for those teams and how many appearances they made. i plan to then store this data in a table within a database and query this database when the user makes a request to search for a player. 

PROJECT IMPLEMENTATION:
Understanding github codespaced - 
At first i had to familiarise myself with github as this is where i planned to do my coding. This actually took up alot more time than i expected in order to understand how to set up a repository, project structure, installing relevant packages, use of virtual environments and importance of file organisation for code sharing and accesability and finally learning new terminal commands for commiting and pushing changes in a way that also followed conventions. 

Writing data-scarping script - 


Web-design using HTML, bootstrap, CSS and python - 
As my project was user based i needed to build an interface that could accomodate user input and display relevant results correctly and aesthetically. i first started by inspecting the html of similar sites to get an idea of the basic struture and layout i would need. i then read through relevant bootstraps documents to understand the different components i could use specific to bootstrap and the conventions around using these supported components. it was then just a process of implementing my design one step at a time starting with the homepage and navigation bar and working my way down.







    # add a list to keep track of the players we have already scraped
    scraped_players = []

    # loop through list to check player hasnt already been scraped