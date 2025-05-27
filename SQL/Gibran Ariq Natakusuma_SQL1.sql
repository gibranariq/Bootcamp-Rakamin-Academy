-- soal 1
SELECT DISTINCT kota from rakamin_customer_address

-- soal 2
SELECT * from rakamin_order
order by tanggal_pembelian desc
limit 10

-- soal 3
SELECT * from rakamin_customer
WHERE penipu = true

-- soal 4
SELECT * from rakamin_order
WHERE metode_bayar = 'shopeepay' 
ORDER BY harga desc

-- soal 5
CREATE TABLE rakamin_customer_address_tangerang AS(
	SELECT * from rakamin_customer_address WHERE kota = 'Tangerang'
)

-- soal 6
UPDATE rakamin_customer_address_tangerang
SET provinsi = 'Banten'
WHERE kota = 'Tangerang';

UPDATE rakamin_customer_address_tangerang
SET alamat = 'Karawaci'
WHERE id_pelanggan = 10

-- soal 7
INSERT INTO rakamin_customer_address_tangerang
VALUES (101, 70, 'Ciledug', 'Tangerang', 'Banten') 

-- soal 8
DELETE FROM rakamin_customer_address_tangerang
WHERE id_alamat = 54
