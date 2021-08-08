# HackerRank_Aggregation



### Revising Aggregations - The Count Function

```sql
SELECT COUNT(ID)
FROM CITY
WHERE POPULATION > 100000;
```



### Revising Aggregations - The Sum Function

```sql
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT='California';
```



### Revising Aggregations - Averages

```sql
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT='California';
```



### Average Population

```sql
SELECT ROUND(AVG(POPULATION))
FROM CITY
;
```



### Japan Population

```sql
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';
```



### Population Density Difference

```sql
SELECT MAX(POPULATION)-MIN(POPULATION)
FROM CITY;
```



### The Blunder

```sql
SELECT CEIL(A.ACTUAL-B.MC)
FROM
    (SELECT AVG(SALARY) ACTUAL
    FROM EMPLOYEES) A,
    (SELECT AVG(TO_NUMBER(REPLACE(SALARY,'0',''))) MC
    FROM EMPLOYEES) B;
```



### Top Earners

```sql
SELECT MONTHS*SALARY, COUNT(*)
FROM EMPLOYEE
WHERE MONTHS*SALARY = (SELECT MAX(MONTHS*SALARY)
    	 		 	   FROM EMPLOYEE)
GROUP BY MONTHS*SALARY
;
```



### Weather Observation Station 2

```sql
SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2)
FROM STATION;
```



### Weather Observation Station 13

```sql
SELECT TRUNC(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N BETWEEN 38.7880 AND 137.2345;
```



### Weather Observation Station 14

```SQL
SELECT TRUNC(MAX(LAT_N), 4)
FROM STATION
WHERE LAT_N < 137.2345;
```



### Weather Observation Station 15

```SQL
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345)
```



### Weather Observation Station 16

```SQL
SELECT ROUND(MIN(LAT_N),4)
FROM STATION
WHERE LAT_N > 38.7780;
```



### Weather Observation Station 17

```SQL
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);
```



### Weather Observation Station 18

```SQL
SELECT ROUND(ABS(MAX(LAT_N)-MIN(LAT_N)) + ABS(MAX(LONG_W)-MIN(LONG_W)),4)
FROM STATION;
```



### Weather Observation Station 19

```SQL
SELECT TRUNC(SQRT(POWER(B-A,2) + POWER(D-C,2)),4)
FROM    (SELECT MIN(LAT_N) A, MAX(LAT_N) B, MIN(LONG_W) C, MAX(LONG_W) D
         FROM STATION);
```



### Weather Observation Station 20

```SQL
-- oracle
SELECT ROUND(MEDIAN(LAT_N),4)
FROM STATION;
```

```SQL
SELECT ROUND(AVG(LAT_N),4) M
FROM (SELECT LAT_N,ROW_NUMBER() OVER(ORDER BY LAT_N) RN
      FROM COUNT(LAT_N) OVER() CNT)
WHERE RN=CEIL(CNT/2);
```

