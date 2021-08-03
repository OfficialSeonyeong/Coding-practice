# HackerRank_Advanced Select



### Type of Triangle

```sql
SELECT
    CASE
        WHEN (A+B<=C) OR (B+C<=A) OR (A+C<=B) THEN 'Not A Triangle'
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN A!=B AND A!=C AND B!=C THEN 'Scalene'
        ELSE 'Isosceles'
        END
FROM TRIANGLES;
```



### The PADS

```sql
SELECT Name||'('||SUBSTR(Occupation,1,1)||')'
FROM OCCUPATIONS
ORDER BY Name;

SELECT 'There are a total of '||COUNT(Occupation)||' '||LOWER(Occupation)||'s.'
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;
```



### Occupations

```sql
SELECT DECODE(Occupation, 'Doctor', Name) Doctor,
	   DECODE(Occupation, 'Professor', Name) Professor,
	   DECODE(Occupation, 'Singer', Name) Singer,
	   DECODE(Occupation, 'Actor', Name) Actor
FROM (
	SELECT Occupation, Name
  		   , ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY Name) RN
    FROM OCCUPATIONS
    ORDER BY RN
)       
```

