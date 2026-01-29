
CREATE TABLE users(
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);
CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
);


ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);


CREATE INDEX idx_users_email
ON users(email);


CREATE OR ALTER VIEW user_order_summary AS
SELECT
    u.user_id,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o 
ON u.user_id = o.user_id
GROUP BY u.user_id, u.email;
 

INSERT INTO users (user_id, email,  password) VALUES
(1, 'ptlkrish@gmail.com', 'Krish@252'),
(2, 'ptlyash@gmaiil.com', 'Yash@287'),
(3, 'taksh@gmail.com', 'tak1004'),
(4, 'aryan12@gmail.com', 'ayan253'),
(5, 'tndel@gmail.com', 'tndl857');

INSERT INTO orders (order_id, user_id, order_date, amount) VALUES
(101, 1, '2024-01-15', 250.75),
(102, 2, '2024-02-20', 450.00),
(103, 1, '2024-03-05', 125.50),
(104, 3, '2024-03-15', 300.00),
(105, 4, '2024-04-10', 600.25),
(106, 2, '2024-04-12', 150.00);

SELECT * FROM user_order_summary;