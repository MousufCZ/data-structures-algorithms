

-- CREATE TABLE ProjectStar(EmpId INTEGER NOT NULL PRIMARY KEY, Name TEXT NOT NULL);
-- INSERT INTO ProjectStar(EmpId, Name)
-- VALUES
-- (6, 'Byron Romo'),
-- (1, 'John Brooks'),
-- (7, 'Mary Wilson'),
-- (3, 'Richard Chambers'),
-- (4, 'Samuel Taylor');
ATTACH DATABASE 'ProjectMoon.db' AS pm

SELECT * FROM ProjectStar
INTERSECT
SELECT * FROM pm.ProjectMoon;
