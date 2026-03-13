CREATE TABLE Students (Name VARCHAR(250), Marks INT);

INSERT INTO Students (Name, Marks)
VALUES ('Sahil', 95), ('Kaushik', 97), ('John', 95), ('Kara', 87), ('Simpson', 97);

SELECT Name, Marks FROM Students
ORDER BY Marks DESC
LIMIT 1 OFFSET 1;

SELECT Name, Marks FROM Students
ORDER BY Marks DESC, Name ASC
LIMIT 1 OFFSET 1;

SELECT Name, Marks
FROM (
    SELECT Name, Marks,
           DENSE_RANK() OVER (ORDER BY Marks DESC) as rnk
    FROM Students
) as RankedStudents
WHERE rnk = 2;