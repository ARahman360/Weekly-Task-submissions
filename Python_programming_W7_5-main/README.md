# W7_5

Analyse provided CSV data and create a summary of daily power usage and cost. Use the data from the provided csv-files A7_T5_D1.csv, A7_T5_D2.csv and A7_T5_D3.csv.

For the summary, calculate the daily power usage and the cost.

* Daily usage: Sum the consumption for each timestamp at the daily level. Use [gatherer](https://saja.kapsi.fi/var_roles/stud_vers/stud_Python_eng.html#gatherer) variable.
* Daily cost: Multiply the consumption by the daily timestamp’s corresponding price. Then sum the results into an gatherer-type variable.

Preferred datastructures:

* Timestamps: list[TIMESTAMP]
* Analysis helper: list[DAY_USAGE]
* Results: list[str]

Run 1

````
Program starting.
Insert filename: A7_T5_D1.csv
Reading file "A7_T5_D1.csv".
Analysing timestamps.
Displaying results.
### Electricity consumption summary ###
 - Monday usage 2510.00 kWh, cost 279.42 €
 - Tuesday usage 2364.00 kWh, cost 286.46 €
 - Wednesday usage 0.00 kWh, cost 0.00 €
 - Thursday usage 0.00 kWh, cost 0.00 €
 - Friday usage 0.00 kWh, cost 0.00 €
 - Saturnday usage 0.00 kWh, cost 0.00 €
 - Sunday usage 0.00 kWh, cost 0.00 €
### Electricity consumption summary ###
Program ending.
````

Run 2
````
Program starting.
Insert filename: A7_T5_D2.csv
Reading file "A7_T5_D2.csv".
Analysing timestamps.
Displaying results.
### Electricity consumption summary ###
 - Monday usage 2510.00 kWh, cost 279.42 €
 - Tuesday usage 2364.00 kWh, cost 286.46 €
 - Wednesday usage 2475.00 kWh, cost 337.74 €
 - Thursday usage 954.00 kWh, cost 126.06 €
 - Friday usage 2475.00 kWh, cost 1567.40 €
 - Saturnday usage 1077.00 kWh, cost 467.43 €
 - Sunday usage 1300.00 kWh, cost 628.78 €
### Electricity consumption summary ###
Program ending.
````

Run 3
````
Program starting.
Insert filename: A7_T5_D3.csv
Reading file "A7_T5_D3.csv".
Analysing timestamps.
Displaying results.
### Electricity consumption summary ###
 - Monday usage 2433.00 kWh, cost 273.26 €
 - Tuesday usage 2364.00 kWh, cost 286.46 €
 - Wednesday usage 2226.00 kWh, cost 299.01 €
 - Thursday usage 802.00 kWh, cost 105.73 €
 - Friday usage 0.00 kWh, cost 0.00 €
 - Saturnday usage 876.00 kWh, cost 350.19 €
 - Sunday usage 1116.00 kWh, cost 544.37 €
### Electricity consumption summary ###
Program ending.
````
