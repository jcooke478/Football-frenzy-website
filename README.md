# Football-Frenzy-Website
PROJECT IDEA:
My goal for this project is create a webpage in which you can find the names of football players who have played for any particular combination of teams you might be interested in. i.e. which players have played for both manchester united and arsenal? 

To do this i need to scrape player data from a site which contains information on all football players in the top 5 leagues with all the teams they played for, the seasons they played for those teams and how many appearances they made. i plan to then store this data in a table within a database and query this database when the user makes a request to search for a player. 

PROJECT IMPLEMENTATION:
At first i had to familiarise myself with github as this is where i planned to do my coding due to my having limited access to up-to-date hardware. This actually took up alot more time than i expected in order to understand how to set up a repository, file organisation and commiting and pushing changes. 




    # add a list to keep track of the players we have already scraped
    scraped_players = []

    # loop through list to check player hasnt already been scraped