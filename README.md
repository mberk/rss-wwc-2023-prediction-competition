# Welcome to the RSS Women's World Cup 2023 Prediction Competition!

# Entries are now closed! The live leaderboard can be viewed [here](leaderboard.csv)

The organisers are grateful to [Smartodds](https://www.smartodds.co.uk/) for their continued support in sponsoring this competition and its previous editions

## Rules

1. The goal of the competition is to make probabilistic predictions of the outcome of every game in the Women's World Cup 2023 tournament
2. Entrants are free to use any data they wish, _provided it is publicly available_. This includes data scraped from public websites
3. Predictions are to be made for all group games and _every possible_ knockout game
4. Submissions must be made before kick-off of the first game, 08:00 BST on 20th July 2023
5. Code and data (or links to the data if the data sets are large) used to generate the predictions must be included in a submission so that the judging panel can reproduce the results
6. Participants are free to enter either as individuals or as teams
7. Entrants may update their predictions at any point before the start of the tournament by submitting a new entry but only the most recent submission will be scored
8. There are three prizes available ([see Prizes below](#prizes)):
    1. **Overall Winner** - the entry with the best log-score ([see Scoring below](#scoring))
    2. **Methodology Prize** - chosen by the judging panel, based on the methodology used
    3. **Student Prize** - awarded by the judging panel (based on the log-score/methodology used) to an entry where at least one team member has e-Student Membership of the RSS

## Scoring

* Entries will be scored according to the log-score
* Each group stage game will receive the score:
```
-(log(p_team1_win)*I(team1_win) + log(p_draw)*I(draw) + log(p_team2_win)*I(team2_win))
```
where  `I(.)` is the indicator function and e.g. `p_team1_win` is the entrant's estimate of the probability that team 1 wins the match
* For knockout games, the outcome is based on the score after extra-time/penalties if relevant and the contribution is:
```
-(log(p_team1_win)*I(team1_win) + log(p_team2_win)*I(team2_win))
```
* The individual scores for all games that actually take place will be summed to provide an overall score for the entry
* The lower the score, the better (note the minus signs!)

## Prizes

All winners will be invited to present their work at the [2023 RSS conference](https://rss.org.uk/training-events/conference-2023/) with reasonable expenses paid (courtesy of [Smartodds](https://www.smartodds.co.uk/), the sponsors of the competition)

## Making a Submission

* An example submission file can be found here: [submission-template.csv](submission-template.csv)
* Entrants should email a zip file to statisticsinsport@rss.org.uk that contains the submission file along with the code and data used to generate it
* If the zip file exceeds 10 megabytes then please do not submit the data but instead clearly comment the code with what data was used and where it can be obtained from. If the submission relies on scraped data and this is too large to be included then the scraping code must be included instead
* When making a submission please indicate whether entering as a team or individual and your name or team name and team members' names as appropriate

## Getting Started

To help you get started, we have added an [IPython Notebook](getting-started.ipynb) that describes fitting a model to a publicly available data set and producing some predictions in the correct format

## Questions?

Any questions can be emailed to statisticsinsport@rss.org.uk or asked by creating a GitHub issue

## Suggested Resources

### Women's International Football Results

* [Mart Jürisoo](https://martj42.github.io/) maintains an easy to consume [CSV file](https://raw.githubusercontent.com/martj42/womens-international-results/ae285e00fa19c7edc4b986a01d135ae6f6545fb8/results.csv) of Women's international football results
* This consists of 5,595 matches going back to 1969
* It's an ideal place to get started

### StatsBomb Free Data

* This is a very detailed data set that spans a range of competitions including some mens matches but of particular interest to competitors will be their women's World Cup 2019 and Euro 2022 data
* Available [here](https://github.com/statsbomb/open-data)
* Comprehensively explained along with tutorials [here](https://statsbomb.com/what-we-do/hub/free-data/)
* Supporting software packages [StatsBombR](https://github.com/statsbomb/StatsBombR) and [StatsBombPy](https://github.com/statsbomb/statsbombpy) are available depending on your programming language of choice

### Oddsportal.com

* Bookmaker odds have been valuable datasets in past editions of this competition
* At [oddsportal.com](https://www.oddsportal.com) you can find:
    * [Odds for the first round of matches](https://www.oddsportal.com/football/world/world-cup-women/)
    * [Odds for each team to win the tournament](https://www.oddsportal.com/football/world/world-cup-women/outrights/)
    * [Odds for qualifying matches and from historic editions of the Women's World Cup](https://www.oddsportal.com/football/world/world-cup-women/results/)

### Previous Competition Editions

* The RSS Statistics in Sport Section has previously run prediction competitions for [Men's Euro 2020](https://github.com/mberk/rss-euro-2020-prediction-competition) and [Wimbledon 2022](https://github.com/jam13g/rss-Wimbledon-2022-prediction-competition)
* To kick off the Wimbledon 2022 competition the Section hosted an online event where the winners of the Euro 2020 competition presented their methods. This is [available to view on YouTube](https://www.youtube.com/watch?v=sYk1ASDCBrc) and may provide some inspiration
