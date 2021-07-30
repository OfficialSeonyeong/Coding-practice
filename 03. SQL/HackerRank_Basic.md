# HackerRank_Basic



## Select

### Revising the Select Query 2

```sql
SELECT NAME
FROM CITY
WHERE POPULATION > 120000 and COUNTRYCODE = 'USA';
```



### Select ALL

```sql
SELECT *
FROM CITY;
```



### Select By ID

```sql
SELECT *
FROM CITY
WHERE ID = 1661;
```



### Japanese Cities' Attributes

```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'JPN';
```



### Japanese Cities' Names

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';
```



### Revising the Select Query 1

```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA' and POPULATION > 100000;
```



### Weather Observation Station 1

```sql
SELECT CITY, STATE
FROM STATION;
```



### Weather Observation Station 3

```sql
SELECT DISTINCT(CITY)
FROM STATION
WHERE MOD(ID, 2) = 0;
```



### Weather Obervation Station 4

```sql
SELECT COUNT(CITY) - COUNT(DISTINCT(CITY))
FROM STATION;
```

