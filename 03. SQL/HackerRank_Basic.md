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



### Weather Observation Station 4

```sql
SELECT COUNT(CITY) - COUNT(DISTINCT(CITY))
FROM STATION;
```



### Weather Observation Station 5

```sql
(SELECT CITY, LENGTH(CITY)
FROM    (SELECT CITY, LENGTH(CITY)
        FROM STATION
        ORDER BY LENGTH(CITY), CITY)
WHERE ROWNUM = 1
)
UNION
(SELECT CITY, LENGTH(CITY)
FROM    (SELECT CITY, LENGTH(CITY)
        FROM STATION
        ORDER BY LENGTH(CITY) DESC, CITY)
WHERE ROWNUM = 1
);
```



*다른 풀이*

```sql
SELECT CITY, LEN
FROM (SELECT CITY, LENGTH(CITY) LEN,
     		 ROW_NUMBER() OVER(ORDER BY LENGTH(CITY), CITY) RN_MIN,
      		 ROW_NUMBER() OVER(ORDER BY LENGTH(CITY) DESC, CITY) RN_MAX
      FROM STATION
     )
WHERE (RN_MIN = 1 OR RN_MAX =1)
ORDER BY LEN;
```



### Weather Observation Station 6

```sql
# 1)
SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTR(CITY,1,1) IN ('A','E','O','I','U');

# 2)
SELECT DISTINCT(CITY)
FROM STATION
WHERE REGEXP_LIKE(CITY,'^[AEIOU]');
```



### Weather Observation Station 7

```sql
# 1)
SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTR(CITY,-1,1) IN ('a','e','o','i','u');

# 2)
SELECT DISTINCT(CITY)
FROM STATION
WHERE REGEXP_LIKE(CITY,'[aeiou]$');
```

