## Description
This web app is meant to evaluate the relative computing power of your system using ranking data from [TechPowerUp](https://www.techpowerup.com/gpu-specs/) and [GeekBench](https://browser.geekbench.com/processor-benchmarks). The app will also give the user a score grading their overall configuration. The app uses Flask to run the site and the data is stored in a SQLite database. You can find the site [here](https://lucasrfabian.site/pcpartrankings/).

The data was scraped using BeautifulSoup. The GPU data is from [TechPowerUp's Relative GPU Performance](https://www.techpowerup.com/gpu-specs/geforce-210.c2020) Database and the CPU data is from [GeekBench's Multi=Core Processor Benchmarks](https://browser.geekbench.com/processor-benchmarks).

## Total System Score Calculation
The basic calculations looks something like this:
- (CPU rank $\div$ total number of CPUs in database) + (GPU rank $\div$ total number of GPUs in database)

The grade is then decided based on the result.
| Raw Score     | Grade     |
| ------------- | ------------- |
| < .1 | S |
| $\geq$ .1, < .2 | A |
| $\geq$ .2, < .3 | B |
| $\geq$ .3, < .4 | C |
| $\geq$ .4, < .5 | D |
| $\geq$ .5 | F |

## How Does It Work?
The main page contains a Flask form where the user inputs their CPU and GPU model names, assisted by a JavaScript autocomplete function that suggests up to 5 possible options. When the user submits the form, the input is then collected by Flask. Flask processes the input, calculates the Total System Score, and then returns a page displaying the results of both the CPU and GPU rankings followed by the calculated score.
