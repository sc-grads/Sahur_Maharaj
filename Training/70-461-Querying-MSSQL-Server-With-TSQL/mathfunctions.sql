DECLARE @varDec AS NUMERIC(7, 2) = 3
SELECT POWER(@varDec,3)
SELECT SQUARE(@varDec)
SELECT SQRT(@varDec)

-- rounding
DECLARE @varDecR AS NUMERIC(7, 2) = 3.3457
SELECT FLOOR(@varDecR) -- round down
SELECT CEILING(@varDecR) -- round up
SELECT ROUND(@varDecR, 0) --nearest recursive

SELECT PI() AS pie
SELECT EXP(1) as e

SELECT ABS(456), SIGN(456)

SELECT RAND(30)