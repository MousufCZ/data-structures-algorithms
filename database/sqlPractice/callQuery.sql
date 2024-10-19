-- Returns table with employees on both tables
SELECT * FROM ProjectStar
INTERSECT
SELECT * FROM ProjectMoon;


SELECT * FROM ProjectMoon
RIGHT JOIN ProjectStar
    on ProjectMoon.EmpId = ProjectStar.EmpId;


SELECT * FROM ProjectMoon
WHERE EmpId IN (SELECT EmpId FROM ProjectStar);