# W7_4

Structure timestamp data in program.

This task uses datasets A7_T4_D1.csv, A7_T4_D2.csv and A7_T4_D3.csv.

The dataset had four different values separated by a semicolon ;

* Weekday
* Hour
* Consumption(kWh)
* Price(€/kWh)
The goal is to print each timestamp from a file and also calculate the total of consumption and price. Below is the output format for a single record.

````
Electiricity usages:
- Monday 12:00, price 0.20 €, consumption 15.00 kWh, total 3.00 €
- ...
````
To keep the code maintainable, define a named datastructure for the different values. Once defined, specify a way to read the timestamps into a list. This can be done by reading a file line by line, skipping empty lines, trimming line endings, and then splitting each line by the delimiter.

Code example of the operations:

````
# Constants
DELIMITER = ";"
  # iterate over lines
    ...
    Row = Line.rstrip()                 # Remove newline
    Columns = Row.split(DELIMITER)      # Splits the row into a list
    Timestamp = TIMESTAMP()             # Create object
    Timestamp.weekday = Columns[0]      # Collect the first column
    ...                                 # Collect rest of the columns...
    Timestamp.price = float(Columns[3]) # Collect the fourth column and convert datatype
    Columns.clear()
````

Preferred datastructures:

Timestamps: list[TIMESTAMP]

Run 1
````
Program starting.
Insert filename: A7_T4_D1.csv
Reading file "A7_T4_D1.csv".
Electricity usage:
 - Monday 00:00, price 0.09, consumption 154.00 kWh, total 13.86 €
 - Monday 01:00, price 0.07, consumption 125.00 kWh, total 8.75 €
 - Monday 02:00, price 0.13, consumption 158.00 kWh, total 20.54 €
 - Monday 03:00, price 0.12, consumption 61.00 kWh, total 7.32 €
 - Monday 04:00, price 0.15, consumption 149.00 kWh, total 22.35 €
 - Monday 05:00, price 0.09, consumption 69.00 kWh, total 6.21 €
 - Monday 06:00, price 0.08, consumption 77.00 kWh, total 6.16 €
 - Monday 07:00, price 0.07, consumption 141.00 kWh, total 9.87 €
 - Monday 08:00, price 0.08, consumption 148.00 kWh, total 11.84 €
 - Monday 09:00, price 0.13, consumption 90.00 kWh, total 11.70 €
 - Monday 10:00, price 0.11, consumption 93.00 kWh, total 10.23 €
 - Monday 11:00, price 0.05, consumption 47.00 kWh, total 2.35 €
 - Monday 12:00, price 0.08, consumption 66.00 kWh, total 5.28 €
 - Monday 13:00, price 0.08, consumption 66.00 kWh, total 5.28 €
 - Monday 14:00, price 0.15, consumption 137.00 kWh, total 20.55 €
 - Monday 15:00, price 0.15, consumption 60.00 kWh, total 9.00 €
 - Monday 16:00, price 0.07, consumption 69.00 kWh, total 4.83 €
 - Monday 17:00, price 0.19, consumption 136.00 kWh, total 25.84 €
 - Monday 18:00, price 0.09, consumption 67.00 kWh, total 6.03 €
 - Monday 19:00, price 0.19, consumption 150.00 kWh, total 28.50 €
 - Monday 20:00, price 0.11, consumption 103.00 kWh, total 11.33 €
 - Monday 21:00, price 0.05, consumption 136.00 kWh, total 6.80 €
 - Monday 22:00, price 0.10, consumption 108.00 kWh, total 10.80 €
 - Monday 23:00, price 0.14, consumption 100.00 kWh, total 14.00 €
 - Tuesday 00:00, price 0.15, consumption 87.00 kWh, total 13.05 €
 - Tuesday 01:00, price 0.12, consumption 58.00 kWh, total 6.96 €
 - Tuesday 02:00, price 0.11, consumption 43.00 kWh, total 4.73 €
 - Tuesday 03:00, price 0.13, consumption 74.00 kWh, total 9.62 €
 - Tuesday 04:00, price 0.13, consumption 103.00 kWh, total 13.39 €
 - Tuesday 05:00, price 0.06, consumption 88.00 kWh, total 5.46 €
 - Tuesday 06:00, price 0.10, consumption 56.00 kWh, total 5.60 €
 - Tuesday 07:00, price 0.08, consumption 83.00 kWh, total 6.64 €
 - Tuesday 08:00, price 0.17, consumption 131.00 kWh, total 22.27 €
 - Tuesday 09:00, price 0.12, consumption 69.00 kWh, total 8.28 €
 - Tuesday 10:00, price 0.19, consumption 132.00 kWh, total 25.08 €
 - Tuesday 11:00, price 0.10, consumption 85.00 kWh, total 8.50 €
 - Tuesday 12:00, price 0.17, consumption 156.00 kWh, total 26.52 €
 - Tuesday 13:00, price 0.16, consumption 45.00 kWh, total 7.20 €
 - Tuesday 14:00, price 0.07, consumption 138.00 kWh, total 9.66 €
 - Tuesday 15:00, price 0.12, consumption 144.00 kWh, total 17.28 €
 - Tuesday 16:00, price 0.15, consumption 76.00 kWh, total 11.40 €
 - Tuesday 17:00, price 0.17, consumption 63.00 kWh, total 10.71 €
 - Tuesday 18:00, price 0.09, consumption 132.00 kWh, total 11.88 €
 - Tuesday 19:00, price 0.08, consumption 152.00 kWh, total 12.16 €
 - Tuesday 20:00, price 0.15, consumption 85.00 kWh, total 12.75 €
 - Tuesday 21:00, price 0.17, consumption 92.00 kWh, total 15.64 €
 - Tuesday 22:00, price 0.10, consumption 134.00 kWh, total 13.40 €
 - Tuesday 23:00, price 0.06, consumption 138.00 kWh, total 8.28 €
Program ending.
````

Run 2
````
Program starting.
Insert filename: A7_T4_D2.csv
Reading file "A7_T4_D2.csv".
Electricity usage:
 - Monday 00:00, price 0.09, consumption 154.00 kWh, total 13.86 €
 - Monday 01:00, price 0.07, consumption 125.00 kWh, total 8.75 €
 - Monday 02:00, price 0.13, consumption 158.00 kWh, total 20.54 €
 - Monday 03:00, price 0.12, consumption 61.00 kWh, total 7.32 €
 - Monday 04:00, price 0.15, consumption 149.00 kWh, total 22.35 €
 - Monday 05:00, price 0.09, consumption 69.00 kWh, total 6.21 €
 - Monday 06:00, price 0.08, consumption 77.00 kWh, total 6.16 €
 - Monday 07:00, price 0.07, consumption 141.00 kWh, total 9.87 €
 - Monday 08:00, price 0.08, consumption 148.00 kWh, total 11.84 €
 - Monday 09:00, price 0.13, consumption 90.00 kWh, total 11.70 €
 - Monday 10:00, price 0.11, consumption 93.00 kWh, total 10.23 €
 - Monday 11:00, price 0.05, consumption 47.00 kWh, total 2.35 €
 - Monday 12:00, price 0.08, consumption 66.00 kWh, total 5.28 €
 - Monday 13:00, price 0.08, consumption 66.00 kWh, total 5.28 €
 - Monday 14:00, price 0.15, consumption 137.00 kWh, total 20.55 €
 - Monday 15:00, price 0.15, consumption 60.00 kWh, total 9.00 €
 - Monday 16:00, price 0.07, consumption 69.00 kWh, total 4.83 €
 - Monday 17:00, price 0.19, consumption 136.00 kWh, total 25.84 €
 - Monday 18:00, price 0.09, consumption 67.00 kWh, total 6.03 €
 - Monday 19:00, price 0.19, consumption 150.00 kWh, total 28.50 €
 - Monday 20:00, price 0.11, consumption 103.00 kWh, total 11.33 €
 - Monday 21:00, price 0.05, consumption 136.00 kWh, total 6.80 €
 - Monday 22:00, price 0.10, consumption 108.00 kWh, total 10.80 €
 - Monday 23:00, price 0.14, consumption 100.00 kWh, total 14.00 €
 - Tuesday 00:00, price 0.15, consumption 87.00 kWh, total 13.05 €
 - Tuesday 01:00, price 0.12, consumption 58.00 kWh, total 6.96 €
 - Tuesday 02:00, price 0.11, consumption 43.00 kWh, total 4.73 €
 - Tuesday 03:00, price 0.13, consumption 74.00 kWh, total 9.62 €
 - Tuesday 04:00, price 0.13, consumption 103.00 kWh, total 13.39 €
 - Tuesday 05:00, price 0.06, consumption 88.00 kWh, total 5.46 €
 - Tuesday 06:00, price 0.10, consumption 56.00 kWh, total 5.60 €
 - Tuesday 07:00, price 0.08, consumption 83.00 kWh, total 6.64 €
 - Tuesday 08:00, price 0.17, consumption 131.00 kWh, total 22.27 €
 - Tuesday 09:00, price 0.12, consumption 69.00 kWh, total 8.28 €
 - Tuesday 10:00, price 0.19, consumption 132.00 kWh, total 25.08 €
 - Tuesday 11:00, price 0.10, consumption 85.00 kWh, total 8.50 €
 - Tuesday 12:00, price 0.17, consumption 156.00 kWh, total 26.52 €
 - Tuesday 13:00, price 0.16, consumption 45.00 kWh, total 7.20 €
 - Tuesday 14:00, price 0.07, consumption 138.00 kWh, total 9.66 €
 - Tuesday 15:00, price 0.12, consumption 144.00 kWh, total 17.28 €
 - Tuesday 16:00, price 0.15, consumption 76.00 kWh, total 11.40 €
 - Tuesday 17:00, price 0.17, consumption 63.00 kWh, total 10.71 €
 - Tuesday 18:00, price 0.09, consumption 132.00 kWh, total 11.88 €
 - Tuesday 19:00, price 0.08, consumption 152.00 kWh, total 12.16 €
 - Tuesday 20:00, price 0.15, consumption 85.00 kWh, total 12.75 €
 - Tuesday 21:00, price 0.17, consumption 92.00 kWh, total 15.64 €
 - Tuesday 22:00, price 0.10, consumption 134.00 kWh, total 13.40 €
 - Tuesday 23:00, price 0.06, consumption 138.00 kWh, total 8.28 €
 - Wednesday 00:00, price 0.19, consumption 99.00 kWh, total 18.81 €
 - Wednesday 01:00, price 0.10, consumption 136.00 kWh, total 13.60 €
 - Wednesday 02:00, price 0.12, consumption 155.00 kWh, total 18.60 €
 - Wednesday 03:00, price 0.17, consumption 102.00 kWh, total 17.34 €
 - Wednesday 04:00, price 0.15, consumption 124.00 kWh, total 18.60 €
 - Wednesday 05:00, price 0.16, consumption 71.00 kWh, total 11.36 €
 - Wednesday 06:00, price 0.08, consumption 126.00 kWh, total 10.08 €
 - Wednesday 07:00, price 0.13, consumption 72.00 kWh, total 9.36 €
 - Wednesday 08:00, price 0.15, consumption 106.00 kWh, total 15.90 €
 - Wednesday 09:00, price 0.08, consumption 57.00 kWh, total 4.56 €
 - Wednesday 10:00, price 0.07, consumption 64.00 kWh, total 4.48 €
 - Wednesday 11:00, price 0.19, consumption 145.00 kWh, total 27.55 €
 - Wednesday 12:00, price 0.12, consumption 134.00 kWh, total 16.08 €
 - Wednesday 13:00, price 0.08, consumption 93.00 kWh, total 7.44 €
 - Wednesday 14:00, price 0.19, consumption 97.00 kWh, total 18.43 €
 - Wednesday 15:00, price 0.19, consumption 106.00 kWh, total 20.14 €
 - Wednesday 16:00, price 0.13, consumption 143.00 kWh, total 18.59 €
 - Wednesday 17:00, price 0.18, consumption 85.00 kWh, total 15.30 €
 - Wednesday 18:00, price 0.07, consumption 63.00 kWh, total 4.41 €
 - Wednesday 19:00, price 0.09, consumption 153.00 kWh, total 13.77 €
 - Wednesday 20:00, price 0.15, consumption 71.00 kWh, total 10.65 €
 - Wednesday 21:00, price 0.17, consumption 86.00 kWh, total 14.62 €
 - Wednesday 22:00, price 0.17, consumption 125.00 kWh, total 21.25 €
 - Wednesday 23:00, price 0.11, consumption 62.00 kWh, total 6.82 €
 - Thursday 00:00, price 0.10, consumption 80.00 kWh, total 8.00 €
 - Thursday 01:00, price 0.17, consumption 9.00 kWh, total 1.53 €
 - Thursday 02:00, price 0.19, consumption 26.00 kWh, total 4.94 €
 - Thursday 03:00, price 0.16, consumption 79.00 kWh, total 12.64 €
 - Thursday 04:00, price 0.15, consumption 36.00 kWh, total 5.40 €
 - Thursday 05:00, price 0.13, consumption 5.00 kWh, total 0.65 €
 - Thursday 06:00, price 0.10, consumption 37.00 kWh, total 3.70 €
 - Thursday 07:00, price 0.19, consumption 19.00 kWh, total 3.61 €
 - Thursday 08:00, price 0.19, consumption 58.00 kWh, total 11.02 €
 - Thursday 09:00, price 0.09, consumption 28.00 kWh, total 2.52 €
 - Thursday 10:00, price 0.09, consumption 47.00 kWh, total 4.23 €
 - Thursday 11:00, price 0.10, consumption 85.00 kWh, total 8.50 €
 - Thursday 12:00, price 0.11, consumption 99.00 kWh, total 10.89 €
 - Thursday 13:00, price 0.19, consumption 39.00 kWh, total 7.41 €
 - Thursday 14:00, price 0.07, consumption 11.00 kWh, total 0.77 €
 - Thursday 15:00, price 0.05, consumption 4.00 kWh, total 0.20 €
 - Thursday 16:00, price 0.12, consumption 64.00 kWh, total 7.68 €
 - Thursday 17:00, price 0.18, consumption 59.00 kWh, total 10.62 €
 - Thursday 18:00, price 0.07, consumption 29.00 kWh, total 2.03 €
 - Thursday 19:00, price 0.09, consumption 45.00 kWh, total 4.05 €
 - Thursday 20:00, price 0.15, consumption 15.00 kWh, total 2.25 €
 - Thursday 21:00, price 0.17, consumption 6.00 kWh, total 1.02 €
 - Thursday 22:00, price 0.17, consumption 71.00 kWh, total 12.07 €
 - Thursday 23:00, price 0.11, consumption 3.00 kWh, total 0.33 €
 - Friday 00:00, price 0.89, consumption 99.00 kWh, total 88.11 €
 - Friday 01:00, price 0.80, consumption 136.00 kWh, total 108.80 €
 - Friday 02:00, price 0.82, consumption 155.00 kWh, total 127.10 €
 - Friday 03:00, price 0.76, consumption 102.00 kWh, total 77.52 €
 - Friday 04:00, price 0.03, consumption 124.00 kWh, total 3.72 €
 - Friday 05:00, price 0.58, consumption 71.00 kWh, total 41.18 €
 - Friday 06:00, price 0.41, consumption 126.00 kWh, total 51.66 €
 - Friday 07:00, price 0.30, consumption 72.00 kWh, total 21.60 €
 - Friday 08:00, price 0.60, consumption 106.00 kWh, total 63.60 €
 - Friday 09:00, price 0.38, consumption 57.00 kWh, total 21.66 €
 - Friday 10:00, price 0.78, consumption 64.00 kWh, total 49.92 €
 - Friday 11:00, price 0.44, consumption 145.00 kWh, total 63.80 €
 - Friday 12:00, price 0.52, consumption 134.00 kWh, total 69.68 €
 - Friday 13:00, price 0.61, consumption 93.00 kWh, total 56.73 €
 - Friday 14:00, price 0.99, consumption 97.00 kWh, total 96.03 €
 - Friday 15:00, price 0.87, consumption 106.00 kWh, total 92.22 €
 - Friday 16:00, price 0.48, consumption 143.00 kWh, total 68.64 €
 - Friday 17:00, price 0.65, consumption 85.00 kWh, total 55.25 €
 - Friday 18:00, price 0.14, consumption 63.00 kWh, total 8.82 €
 - Friday 19:00, price 0.94, consumption 153.00 kWh, total 143.82 €
 - Friday 20:00, price 0.34, consumption 71.00 kWh, total 24.14 €
 - Friday 21:00, price 0.93, consumption 86.00 kWh, total 79.98 €
 - Friday 22:00, price 0.90, consumption 125.00 kWh, total 112.50 €
 - Friday 23:00, price 0.66, consumption 62.00 kWh, total 40.92 €
 - Saturnday 00:00, price 0.77, consumption 18.00 kWh, total 13.86 €
 - Saturnday 01:00, price 0.06, consumption 30.00 kWh, total 1.80 €
 - Saturnday 02:00, price 0.29, consumption 24.00 kWh, total 6.96 €
 - Saturnday 03:00, price 0.35, consumption 95.00 kWh, total 33.25 €
 - Saturnday 04:00, price 0.02, consumption 48.00 kWh, total 0.96 €
 - Saturnday 05:00, price 0.79, consumption 7.00 kWh, total 5.53 €
 - Saturnday 06:00, price 0.63, consumption 65.00 kWh, total 40.95 €
 - Saturnday 07:00, price 0.49, consumption 87.00 kWh, total 42.63 €
 - Saturnday 08:00, price 0.81, consumption 51.00 kWh, total 41.31 €
 - Saturnday 09:00, price 0.72, consumption 2.00 kWh, total 1.44 €
 - Saturnday 10:00, price 0.04, consumption 55.00 kWh, total 2.20 €
 - Saturnday 11:00, price 0.85, consumption 89.00 kWh, total 75.65 €
 - Saturnday 12:00, price 0.42, consumption 49.00 kWh, total 20.58 €
 - Saturnday 13:00, price 0.88, consumption 17.00 kWh, total 14.96 €
 - Saturnday 14:00, price 0.07, consumption 67.00 kWh, total 4.69 €
 - Saturnday 15:00, price 0.33, consumption 8.00 kWh, total 2.64 €
 - Saturnday 16:00, price 0.01, consumption 50.00 kWh, total 0.50 €
 - Saturnday 17:00, price 0.64, consumption 14.00 kWh, total 8.96 €
 - Saturnday 18:00, price 0.54, consumption 32.00 kWh, total 17.28 €
 - Saturnday 19:00, price 0.26, consumption 16.00 kWh, total 4.16 €
 - Saturnday 20:00, price 0.09, consumption 42.00 kWh, total 3.78 €
 - Saturnday 21:00, price 0.69, consumption 84.00 kWh, total 57.96 €
 - Saturnday 22:00, price 0.74, consumption 75.00 kWh, total 55.50 €
 - Saturnday 23:00, price 0.19, consumption 52.00 kWh, total 9.88 €
 - Sunday 00:00, price 0.39, consumption 67.00 kWh, total 26.13 €
 - Sunday 01:00, price 0.55, consumption 84.00 kWh, total 46.20 €
 - Sunday 02:00, price 0.08, consumption 27.00 kWh, total 2.16 €
 - Sunday 03:00, price 0.32, consumption 46.00 kWh, total 14.72 €
 - Sunday 04:00, price 0.20, consumption 16.00 kWh, total 3.20 €
 - Sunday 05:00, price 0.51, consumption 81.00 kWh, total 41.31 €
 - Sunday 06:00, price 0.92, consumption 93.00 kWh, total 85.56 €
 - Sunday 07:00, price 0.21, consumption 46.00 kWh, total 9.66 €
 - Sunday 08:00, price 0.98, consumption 91.00 kWh, total 89.18 €
 - Sunday 09:00, price 0.11, consumption 69.00 kWh, total 7.59 €
 - Sunday 10:00, price 0.10, consumption 57.00 kWh, total 5.70 €
 - Sunday 11:00, price 0.47, consumption 96.00 kWh, total 45.12 €
 - Sunday 12:00, price 0.25, consumption 62.00 kWh, total 15.50 €
 - Sunday 13:00, price 0.17, consumption 31.00 kWh, total 5.27 €
 - Sunday 14:00, price 0.95, consumption 72.00 kWh, total 68.40 €
 - Sunday 15:00, price 0.96, consumption 77.00 kWh, total 73.92 €
 - Sunday 16:00, price 0.12, consumption 94.00 kWh, total 11.28 €
 - Sunday 17:00, price 0.23, consumption 61.00 kWh, total 14.03 €
 - Sunday 18:00, price 0.15, consumption 13.00 kWh, total 1.95 €
 - Sunday 19:00, price 0.56, consumption 21.00 kWh, total 11.76 €
 - Sunday 20:00, price 0.37, consumption 54.00 kWh, total 19.98 €
 - Sunday 21:00, price 0.68, consumption 12.00 kWh, total 8.16 €
 - Sunday 22:00, price 0.70, consumption 10.00 kWh, total 7.00 €
 - Sunday 23:00, price 0.75, consumption 20.00 kWh, total 15.00 €
Program ending.
````

Run 3
````
Program starting.
Insert filename: A7_T4_D3.csv
Reading file "A7_T4_D3.csv".
Electricity usage:
 - Monday 00:00, price 0.09, consumption 154.00 kWh, total 13.86 €
 - Monday 01:00, price 0.07, consumption 125.00 kWh, total 8.75 €
 - Monday 02:00, price 0.13, consumption 158.00 kWh, total 20.54 €
 - Monday 03:00, price 0.12, consumption 61.00 kWh, total 7.32 €
 - Monday 04:00, price 0.15, consumption 149.00 kWh, total 22.35 €
 - Monday 05:00, price 0.09, consumption 69.00 kWh, total 6.21 €
 - Monday 07:00, price 0.07, consumption 141.00 kWh, total 9.87 €
 - Monday 08:00, price 0.08, consumption 148.00 kWh, total 11.84 €
 - Monday 09:00, price 0.13, consumption 90.00 kWh, total 11.70 €
 - Monday 10:00, price 0.11, consumption 93.00 kWh, total 10.23 €
 - Monday 11:00, price 0.05, consumption 47.00 kWh, total 2.35 €
 - Monday 12:00, price 0.08, consumption 66.00 kWh, total 5.28 €
 - Monday 13:00, price 0.08, consumption 66.00 kWh, total 5.28 €
 - Monday 14:00, price 0.15, consumption 137.00 kWh, total 20.55 €
 - Monday 15:00, price 0.15, consumption 60.00 kWh, total 9.00 €
 - Monday 16:00, price 0.07, consumption 69.00 kWh, total 4.83 €
 - Monday 17:00, price 0.19, consumption 136.00 kWh, total 25.84 €
 - Monday 18:00, price 0.09, consumption 67.00 kWh, total 6.03 €
 - Monday 19:00, price 0.19, consumption 150.00 kWh, total 28.50 €
 - Monday 20:00, price 0.11, consumption 103.00 kWh, total 11.33 €
 - Monday 21:00, price 0.05, consumption 136.00 kWh, total 6.80 €
 - Monday 22:00, price 0.10, consumption 108.00 kWh, total 10.80 €
 - Monday 23:00, price 0.14, consumption 100.00 kWh, total 14.00 €
 - Tuesday 00:00, price 0.15, consumption 87.00 kWh, total 13.05 €
 - Tuesday 01:00, price 0.12, consumption 58.00 kWh, total 6.96 €
 - Tuesday 02:00, price 0.11, consumption 43.00 kWh, total 4.73 €
 - Tuesday 03:00, price 0.13, consumption 74.00 kWh, total 9.62 €
 - Tuesday 04:00, price 0.13, consumption 103.00 kWh, total 13.39 €
 - Tuesday 05:00, price 0.06, consumption 88.00 kWh, total 5.46 €
 - Tuesday 06:00, price 0.10, consumption 56.00 kWh, total 5.60 €
 - Tuesday 07:00, price 0.08, consumption 83.00 kWh, total 6.64 €
 - Tuesday 08:00, price 0.17, consumption 131.00 kWh, total 22.27 €
 - Tuesday 09:00, price 0.12, consumption 69.00 kWh, total 8.28 €
 - Tuesday 10:00, price 0.19, consumption 132.00 kWh, total 25.08 €
 - Tuesday 11:00, price 0.10, consumption 85.00 kWh, total 8.50 €
 - Tuesday 12:00, price 0.17, consumption 156.00 kWh, total 26.52 €
 - Tuesday 13:00, price 0.16, consumption 45.00 kWh, total 7.20 €
 - Tuesday 14:00, price 0.07, consumption 138.00 kWh, total 9.66 €
 - Tuesday 15:00, price 0.12, consumption 144.00 kWh, total 17.28 €
 - Tuesday 16:00, price 0.15, consumption 76.00 kWh, total 11.40 €
 - Tuesday 17:00, price 0.17, consumption 63.00 kWh, total 10.71 €
 - Tuesday 18:00, price 0.09, consumption 132.00 kWh, total 11.88 €
 - Tuesday 19:00, price 0.08, consumption 152.00 kWh, total 12.16 €
 - Tuesday 20:00, price 0.15, consumption 85.00 kWh, total 12.75 €
 - Tuesday 21:00, price 0.17, consumption 92.00 kWh, total 15.64 €
 - Tuesday 22:00, price 0.10, consumption 134.00 kWh, total 13.40 €
 - Tuesday 23:00, price 0.06, consumption 138.00 kWh, total 8.28 €
 - Wednesday 00:00, price 0.19, consumption 99.00 kWh, total 18.81 €
 - Wednesday 01:00, price 0.10, consumption 136.00 kWh, total 13.60 €
 - Wednesday 02:00, price 0.12, consumption 155.00 kWh, total 18.60 €
 - Wednesday 03:00, price 0.17, consumption 102.00 kWh, total 17.34 €
 - Wednesday 04:00, price 0.15, consumption 124.00 kWh, total 18.60 €
 - Wednesday 05:00, price 0.16, consumption 71.00 kWh, total 11.36 €
 - Wednesday 06:00, price 0.08, consumption 126.00 kWh, total 10.08 €
 - Wednesday 07:00, price 0.13, consumption 72.00 kWh, total 9.36 €
 - Wednesday 08:00, price 0.15, consumption 106.00 kWh, total 15.90 €
 - Wednesday 09:00, price 0.08, consumption 57.00 kWh, total 4.56 €
 - Wednesday 10:00, price 0.07, consumption 64.00 kWh, total 4.48 €
 - Wednesday 11:00, price 0.19, consumption 145.00 kWh, total 27.55 €
 - Wednesday 12:00, price 0.12, consumption 134.00 kWh, total 16.08 €
 - Wednesday 13:00, price 0.08, consumption 93.00 kWh, total 7.44 €
 - Wednesday 14:00, price 0.19, consumption 97.00 kWh, total 18.43 €
 - Wednesday 17:00, price 0.18, consumption 85.00 kWh, total 15.30 €
 - Wednesday 18:00, price 0.07, consumption 63.00 kWh, total 4.41 €
 - Wednesday 19:00, price 0.09, consumption 153.00 kWh, total 13.77 €
 - Wednesday 20:00, price 0.15, consumption 71.00 kWh, total 10.65 €
 - Wednesday 21:00, price 0.17, consumption 86.00 kWh, total 14.62 €
 - Wednesday 22:00, price 0.17, consumption 125.00 kWh, total 21.25 €
 - Wednesday 23:00, price 0.11, consumption 62.00 kWh, total 6.82 €
 - Thursday 00:00, price 0.10, consumption 80.00 kWh, total 8.00 €
 - Thursday 01:00, price 0.17, consumption 9.00 kWh, total 1.53 €
 - Thursday 02:00, price 0.19, consumption 26.00 kWh, total 4.94 €
 - Thursday 03:00, price 0.16, consumption 79.00 kWh, total 12.64 €
 - Thursday 04:00, price 0.15, consumption 36.00 kWh, total 5.40 €
 - Thursday 05:00, price 0.13, consumption 5.00 kWh, total 0.65 €
 - Thursday 06:00, price 0.10, consumption 37.00 kWh, total 3.70 €
 - Thursday 07:00, price 0.19, consumption 19.00 kWh, total 3.61 €
 - Thursday 08:00, price 0.19, consumption 58.00 kWh, total 11.02 €
 - Thursday 09:00, price 0.09, consumption 28.00 kWh, total 2.52 €
 - Thursday 10:00, price 0.09, consumption 47.00 kWh, total 4.23 €
 - Thursday 11:00, price 0.10, consumption 85.00 kWh, total 8.50 €
 - Thursday 12:00, price 0.11, consumption 99.00 kWh, total 10.89 €
 - Thursday 13:00, price 0.19, consumption 39.00 kWh, total 7.41 €
 - Thursday 14:00, price 0.07, consumption 11.00 kWh, total 0.77 €
 - Thursday 15:00, price 0.05, consumption 4.00 kWh, total 0.20 €
 - Thursday 19:00, price 0.09, consumption 45.00 kWh, total 4.05 €
 - Thursday 20:00, price 0.15, consumption 15.00 kWh, total 2.25 €
 - Thursday 21:00, price 0.17, consumption 6.00 kWh, total 1.02 €
 - Thursday 22:00, price 0.17, consumption 71.00 kWh, total 12.07 €
 - Thursday 23:00, price 0.11, consumption 3.00 kWh, total 0.33 €
 - Saturnday 00:00, price 0.77, consumption 18.00 kWh, total 13.86 €
 - Saturnday 01:00, price 0.06, consumption 30.00 kWh, total 1.80 €
 - Saturnday 02:00, price 0.29, consumption 24.00 kWh, total 6.96 €
 - Saturnday 03:00, price 0.35, consumption 95.00 kWh, total 33.25 €
 - Saturnday 04:00, price 0.02, consumption 48.00 kWh, total 0.96 €
 - Saturnday 05:00, price 0.79, consumption 7.00 kWh, total 5.53 €
 - Saturnday 06:00, price 0.63, consumption 65.00 kWh, total 40.95 €
 - Saturnday 07:00, price 0.49, consumption 87.00 kWh, total 42.63 €
 - Saturnday 08:00, price 0.81, consumption 51.00 kWh, total 41.31 €
 - Saturnday 09:00, price 0.72, consumption 2.00 kWh, total 1.44 €
 - Saturnday 10:00, price 0.04, consumption 55.00 kWh, total 2.20 €
 - Saturnday 11:00, price 0.85, consumption 89.00 kWh, total 75.65 €
 - Saturnday 12:00, price 0.42, consumption 49.00 kWh, total 20.58 €
 - Saturnday 13:00, price 0.88, consumption 17.00 kWh, total 14.96 €
 - Saturnday 14:00, price 0.07, consumption 67.00 kWh, total 4.69 €
 - Saturnday 15:00, price 0.33, consumption 8.00 kWh, total 2.64 €
 - Saturnday 16:00, price 0.01, consumption 50.00 kWh, total 0.50 €
 - Saturnday 17:00, price 0.64, consumption 14.00 kWh, total 8.96 €
 - Saturnday 18:00, price 0.54, consumption 32.00 kWh, total 17.28 €
 - Saturnday 19:00, price 0.26, consumption 16.00 kWh, total 4.16 €
 - Saturnday 23:00, price 0.19, consumption 52.00 kWh, total 9.88 €
 - Sunday 00:00, price 0.39, consumption 67.00 kWh, total 26.13 €
 - Sunday 01:00, price 0.55, consumption 84.00 kWh, total 46.20 €
 - Sunday 02:00, price 0.08, consumption 27.00 kWh, total 2.16 €
 - Sunday 03:00, price 0.32, consumption 46.00 kWh, total 14.72 €
 - Sunday 06:00, price 0.92, consumption 93.00 kWh, total 85.56 €
 - Sunday 07:00, price 0.21, consumption 46.00 kWh, total 9.66 €
 - Sunday 08:00, price 0.98, consumption 91.00 kWh, total 89.18 €
 - Sunday 09:00, price 0.11, consumption 69.00 kWh, total 7.59 €
 - Sunday 10:00, price 0.10, consumption 57.00 kWh, total 5.70 €
 - Sunday 11:00, price 0.47, consumption 96.00 kWh, total 45.12 €
 - Sunday 12:00, price 0.25, consumption 62.00 kWh, total 15.50 €
 - Sunday 13:00, price 0.17, consumption 31.00 kWh, total 5.27 €
 - Sunday 14:00, price 0.95, consumption 72.00 kWh, total 68.40 €
 - Sunday 15:00, price 0.96, consumption 77.00 kWh, total 73.92 €
 - Sunday 16:00, price 0.12, consumption 94.00 kWh, total 11.28 €
 - Sunday 17:00, price 0.23, consumption 61.00 kWh, total 14.03 €
 - Sunday 18:00, price 0.15, consumption 13.00 kWh, total 1.95 €
 - Sunday 22:00, price 0.70, consumption 10.00 kWh, total 7.00 €
 - Sunday 23:00, price 0.75, consumption 20.00 kWh, total 15.00 €
Program ending.
````
