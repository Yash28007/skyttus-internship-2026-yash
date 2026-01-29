CREATE TABLE accounts1(
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance INT
)

BEGIN TRANSACTION;

INSERT INTO accounts1 (account_id, account_name, balance)
VALUES (101, 'Krish', 10000);

ROLLBACK;

BEGIN TRANSACTION;

INSERT INTO accounts1 (account_id, account_name, balance)
VALUES (102, 'Yash', 15000);

COMMIT;

BEGIN TRANSACTION;

-- Deduct from Krish
UPDATE accounts1
SET balance = balance - 2000
WHERE account_name = 'Krish';

-- Add to Yash
UPDATE accounts1
SET balance = balance + 2000
WHERE account_name = 'Yash';

COMMIT;

SELECT * FROM accounts1;