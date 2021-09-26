# Election Analysis

## Project Overview
The County Board of Elections has asked us to analyze data from a local election and determine the winner. Here are the questions we are tasked to answer:
1. Calculate the total number of votes cast
2. Compile a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received 
4. Calculate the percentage of the total vote each candidate received 
5. Determine the winner based on the popular vote

## Resources
* Data source: election_results.csv
* Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
Our analysis of the election data provided the following results:
* There were 369,711 total votes cast
* The candidates were:
  * Charles Casper Stickham
  * Diana DeGette
  * Raymon Anthony Doane
* The candidates results were:
  * Charles Casper Stockham recieved **23%** of the vote with **85,213** total votes
  * Diana DeGette received **73.8%** of the vote with **272,892** total votes
  * Raymon Anthony Doane received **3.1%** of the vote with **11,606** total votes
* The winner of the election was:
  * ***Diana DeGette*** who received **73.8%** of the vote with **272,892** total votes

## Challenge Overview
After completing our analysis of the election data and determining that Diana DeGette was the winner, we were tasked with an audit of the data that focused on the turnout in individual counties. 

## Challenge Results
We were able to retool our previous code to determine the percentage of the total vote cast for each county in the election as follows:
* Jefferson County had **10.5%** of the vote with **38,855** votes
* Denver County had **82.8%** of the vote with **306,055** votes
* Arapahoe County had **6.7%** of the vote with **24,801** votes
From this we can conclude that ***Denver County*** had the highest percentage of the total voter turnout. Furthermore, our code can analyze additional input as necessary to be able to provide election results for any future elections held.
