# Overview of Election Audit
The purpose of this election audit is to understand not only the results of the populus vote, but also where voter turnout is highest.

#Election Audit Results
*  There were 369,711 total votes in this congressional election.
*  There were 38,855 total votes, or 10.5% of all votes in Jefferson County
*  There were 306,055 total votes, or 82.8% of all votes in Denver County
*  There were 24,801 total votes, or 6.7% of all votes in Arapahoe County

*  This means that Denver County had the largest number of votes by county

*  Charles Casper Stockham recieved 85,213 total votes, or 23% of the votes
*  Diana DeGette recieved 272,892 total votes, or 73.8% of the votes
*  Raymon Anthony Doane recieved 11,606 total votes, or 3.1% of the votes

*  The winner of the election was Diana DeGette, with 272,892 votes, or 73.8% of the total votes

#Election Audit Summary
The script could be used for all voting applications with a few modifications. So far, the script only populates 3 lists, the unique voter ID, the county that was voted in, and the candidate that was voted for.
It then counts, through a total count, and a count by county, which candidate was voted for on each ballot.
It then returns a total count of votes, and a percentage by candidate and by county of the toal votes cast.

The script could be modified to add more lists to scroll through, such as state, county, and city to help with location based analytics and results. The only necessary changes would be to the .csv format file to add these colums in the included data, 
and then the addition of the new lists to the script to identify, scan, and populate said lists inside the script.
