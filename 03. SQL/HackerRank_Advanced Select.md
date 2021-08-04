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
-- MAX여도 상관 없음.
SELECT MIN(DECODE(Occupation, 'Doctor', Name)) Doctor,
       MIN(DECODE(Occupation, 'Professor', Name)) Professor,
       MIN(DECODE(Occupation, 'Singer', Name)) Singer,
       MIN(DECODE(Occupation, 'Actor', Name)) Actor
FROM (
    SELECT Occupation, Name
             , ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY Name) RN
    FROM OCCUPATIONS
    ORDER BY RN
)
GROUP BY RN
ORDER BY 1,2,3,4
;
```

```sql
-- PIVOT 함수 사용
SELECT Doctor, Professor, Singer, Actor
FROM (
    SELECT Occupation, Name, ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY Name) RN
    FROM OCCUPATIONS
)
PIVOT (
    MIN(NAME) FOR OCCUPATION IN ('Doctor' as Doctor, 'Professor' as Professor, 'Singer' as Singer, 'Actor' as Actor)
)
ORDER BY 1,2,3,4
;
```



### Binary Tree Nodes

```sql
SELECT N,
	CASE
	WHEN P IS NULL THEN 'Root'
	WHEN N IN (SELECT P FROM BST) THEN 'Inner'
	ELSE 'Leaf'
	END
FROM BST
ORDER BY N;
```





### New Companies

```sql
-- USING을 사용하면 테이블을 결합할 때 사용한 중복 컬럼에 별칭을 사용할 수 없어 GROUP BY나 ORDER BY 등에서 그 컬럼을 사용할 때 ambigous column으로 처리되어 오류 발생
SELECT C.company_code, C.founder, 
    COUNT(DISTINCT(L.lead_manager_code)), 
    COUNT(DISTINCT(S.senior_manager_code)), 
    COUNT(DISTINCT(M.manager_code)),
    COUNT(DISTINCT(E.employee_code))
FROM Company C INNER JOIN Lead_Manager L ON(C.company_code=L.company_code)
INNER JOIN Senior_Manager S ON(L.lead_manager_code=S.lead_manager_code)
INNER JOIN Manager M ON(S.senior_manager_code=M.senior_manager_code)
INNER JOIN Employee E ON(M.manager_code=E.manager_code)
GROUP BY C.company_code, C.founder
ORDER BY C.company_code;
```

