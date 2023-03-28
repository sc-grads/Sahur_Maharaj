SELECT system_type_id, column_id, system_type_id * 1.00 / column_id AS Calculation
FROM sys.all_columns
-- all types are ints should be decimal
SELECT system_type_id, column_id, FLOOR(system_type_id * 1.00 / column_id) AS Calculation
FROM sys.all_columns

SELECT system_type_id, column_id, CEILING(system_type_id * 1.00 / column_id) AS Calculation
FROM sys.all_columns

SELECT system_type_id, column_id, ROUND(system_type_id * 1.00 / column_id, 1) AS Calculation
FROM sys.all_columns

SELECT system_type_id, column_id, TRY_CONVERT(TINYINT, system_type_id * 2) AS Calculation
FROM sys.all_columns