# HackerRank_Basic Join

### Population Census

```sql
SELECT SUM(CITY.POPULATION)
FROM CITY INNER JOIN COUNTRY ON(CITY.COUNTRYCODE = COUNTRY.CODE)
WHERE COUNTRY.CONTINENT='Asia';
```



### African Cities

```sql
SELECT CITY.NAME
FROM CITY INNER JOIN COUNTRY ON(CITY.COUNTRYCODE=COUNTRY.CODE)
WHERE CONTINENT='Africa';
```



### Average Population of Each Continent

```sql
SELECT B.CONTINENT, FLOOR(AVG(A.POPULATION))
FROM CITY A INNER JOIN COUNTRY B ON(A.COUNTRYCODE=B.CODE)
GROUP BY B.CONTINENT;
```



### The Report

```sql
SELECT CASE
        WHEN G.GRADE<8 THEN 'NULL'
        ELSE S.NAME
        END AS N,
        G.GRADE, S.MARKS
FROM STUDENTS S JOIN GRADES G ON (S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK)
ORDER BY G.GRADE DESC, N, S.MARKS;
```



### Top Competitors

```sql
 SELECT A, B
 FROM  (SELECT H.hacker_id A, H.name B, COUNT(H.hacker_id) TN
        FROM Submissions S JOIN Challenges C ON (S.challenge_id=C.challenge_id)
           JOIN Difficulty D ON (D.difficulty_level=C.difficulty_level)
           JOIN Hackers H ON (H.hacker_id=S.hacker_id)
        WHERE D.score = S.score
        GROUP BY H.hacker_id, H.name)
 WHERE TN > 1
 ORDER BY TN DESC, A;
```
