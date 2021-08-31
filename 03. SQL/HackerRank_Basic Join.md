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



### Ollivander's Inventory

```SQL
SELECT A.ID, B.AGE, A.COINS_NEEDED, A.POWER
FROM WANDS A JOIN WANDS_PROPERTY B USING (CODE)
WHERE B.IS_EVIL=0
AND A.COINS_NEEDED = (SELECT MIN(C.COINS_NEEDED)
                     FROM WANDS C JOIN WANDS_PROPERTY D USING (CODE)
                     WHERE D.IS_EVIL=0
                     AND C.POWER=A.POWER
                     AND D.AGE=B.AGE)
ORDER BY A.POWER DESC, B.AGE DESC;                     
```



### Challenges

```SQL
-- MySQL
SELECT H.hacker_id, H.name, COUNT(*) challenges_created
FROM Hackers H INNER JOIN Challenges C ON (H.hacker_id=C.hacker_id)
GROUP BY H.hacker_id, H.name
HAVING challenges_created IN (SELECT sub1.challenges_created
                              FROM (SELECT hacker_id, COUNT(*) challenges_created
                                    FROM Challenges
                                    GROUP BY hacker_id) sub1
                              GROUP BY sub1.challenges_created
                              HAVING COUNT(*)=1
                              )
       OR challenges_created = (SELECT MAX(sub2.challenges_created)
                                FROM (SELECT COUNT(*) challenges_created
                                      FROM Challenges
                                      GROUP BY hacker_id) sub2)
ORDER BY challenges_created DESC, H.hacker_id                          
```



### Contest Leaderboard

```sql
SELECT hacker_id, name, SUM(score)
FROM Hackers H JOIN (SELECT hacker_id, challenge_id, MAX(score) score
                    FROM Submissions
                    GROUP BY hacker_id, challenge_id) S USING (hacker_id)
GROUP BY hacker_id, name
HAVING SUM(score) != 0
ORDER BY SUM(score) DESC, hacker_id;
```

