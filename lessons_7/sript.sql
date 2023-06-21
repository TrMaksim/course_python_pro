CREATE TABLE warehouses(
	id SERIAL NOT NULL PRIMARY KEY,
	name varchar(50) NOT NULL,
	location varchar(100) NOT NULL
);

CREATE TABLE goods(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
  	quantity INTEGER NOT NULL,
  	warehouse_id INTEGER NOT NULL REFERENCES warehouses(id),
  	updated_at TIMESTAMP NOT NULL
);

INSERT INTO warehouses (name, location) VALUES
  	('Central Warehouse', 'London, Baker street, 221b,'),
  	('International Warehouse', 'New York, Lincoln Ave Winnetka, 671'),
  	('Ukranian Warehouse', 'Kiev, Khreshchatyk Street, 13');


 INSERT INTO goods (name, quantity, warehouse_id, updated_at) VALUES
	('Clothing', 500, 3, '2023-06-16 00:30:00'),
	('Medicinal products', 75, 3, '2023-06-16 19:42:25'),
  	('Baby toys', 10, 1, NOW()),
 	('Cheap cars', 50, 2, '2023-06-17 11:48:12'),
  	('Expensive cars(exclusive)', 5, 2, '2023-06-17 13:45:00'),
	('Expensive cars', 15, 2, '2023-06-16 19:34:57'),
 	('Baby toys', 60, 1, NOW()),
	('Military facility', 17, 3, current_timestamp),
  	('Humanitarian aid', 120, 1, '2023-06-20 15:15:00'),
  	('Military facility', 5, 3, current_timestamp);

UPDATE goods SET quantity = 1 WHERE id = 3;
DELETE FROM goods WHERE id = 3;
CREATE INDEX idx_product_name ON goods (n);

