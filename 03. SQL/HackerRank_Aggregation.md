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
SELECT ROUND(A.ACTUAL-B.MC)
FROM
	(SELECT AVG(SALARY) ACTUAL
    FROM EMPLOYEES A,
    SELECT AVG(REPLACE(SALARY,'0','')) MC
    FROM EMPLOYEES B);
```

