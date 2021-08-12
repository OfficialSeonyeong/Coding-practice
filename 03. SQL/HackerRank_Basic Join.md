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

-- 틀림...수정해야하는데 너무 복잡하다.

```SQL
SELECT hacker_id, H.name, COUNT(C.challenge_id) created
FROM Hackers H JOIN Challenges C ON (H.hacker_id=C.hacker_id)
WHERE created != (SELECT COUNT(B.challenge_id)
                        FROM Hackers A JOIN Challenges B ON (A.hacker_id=B.hacker_id)
                        WHERE A.hacker_id != H.hacker_id
                 		GROUP BY hacker_id
                 		HAVING COUNT(B.challenge_id)!=(SELECT MAX(COUNT(change_id)
                                                       FROM Hackers JOIN Challenges USING (hacker_id)
                                                       GROUP BY hacker_id)))
GROUP BY hacker_id, H.name
ORDER BY created DESC, hacker_id
```

