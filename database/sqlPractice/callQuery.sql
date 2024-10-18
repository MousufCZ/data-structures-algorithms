-- ATTACH DATABASE '.database/sqlPractice/projectMoon.db' AS pm;
-- ATTACH DATABASE 'ProjectStar.db' AS ps

-- Verify table exists
-- ATTACH DATABASE 'ProjectMoon.db' AS pm;
-- .tables pm

-- 
SELECT name FROM pm.sqlite_master WHERE type='table';

-- SELECT * FROM ProjectStar
-- INTERSECT
-- SELECT * FROM pm.ProjectMoon;