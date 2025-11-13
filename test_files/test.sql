CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

INSERT INTO users VALUES (1, 'test_user', 'test@example.com');
INSERT INTO users VALUES (2, 'test_admin', 'admin@test.com');
SELECT * FROM users WHERE name LIKE '%test%';