# HackerRank_Advanced Join



### Placements

```sql
SELECT Stu.Name
FROM (SELECT * FROM Students JOIN Packages USING (ID)) Stu,
	(SELECT Friends.ID ID, Packages.Salary Salary FROM Friends JOIN Packages ON (Friends.Friend_ID=Packages.ID)) Fri
WHERE Stu.ID=Fri.ID AND Fri.Salary > Stu.Salary
ORDER BY Fri.Salary;
```



### Symmetric Pairs

```sql
-- X != Y
((SELECT B.X, B.Y
FROM Functions A JOIN Functions B ON (A.X=B.Y)
WHERE B.X=A.Y AND B.X < B.Y)
 
UNION

-- X = Y
(SELECT X,Y
FROM Functions
WHERE X=Y
GROUP BY X, Y
HAVING COUNT(*)>1))

ORDER BY X;
```

