## Description
This web app is meant to evaluate the relative computing power of your system using ranking data from [TechPowerUp](https://www.techpowerup.com/gpu-specs/) and [GeekBench](https://browser.geekbench.com/processor-benchmarks). The app will also give the user a score grading their overall configuration. The app uses Flask to run the site and the data is stored in a SQLite database. The data was scraped using BeautifulSoup.

## Total System Score Calculation
The basic calculations looks something like this:
(chosen CPU model rank $\div$ total number of CPUs in database) + (chosen GPU model rank $\div$ total number of GPUs in database)
