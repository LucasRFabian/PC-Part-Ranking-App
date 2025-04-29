## Description
This web app is meant to evaluate the relative computing power of your system using ranking data from [TechPowerUp](https://www.techpowerup.com/gpu-specs/) and [GeekBench](https://browser.geekbench.com/processor-benchmarks). The app will also give the user a score grading their overall configuration. The app uses Flask to run the site and the data is stored in a SQLite database. The data was scraped using BeautifulSoup.

## Total System Score Calculation
The basic calculations looks something like this:
- (CPU rank $\div$ total number of CPUs in database) + (GPU rank $\div$ total number of GPUs in database)

The grade is then decided based on the result.
| Raw Score     | Grade     |
| ------------- | ------------- |
| < .1 | S |
| \geq .1, < .2 | A |
| \geq .2, < .3 | B |
| \geq .3, < .4 | C |
| \geq .4, < .5 | D |
| \geq .5 | F |
