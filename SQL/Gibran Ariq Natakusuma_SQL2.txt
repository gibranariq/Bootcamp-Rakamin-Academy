--soal 1
SELECT nama, email, bulan_lahir, tanggal_registrasi FROM rakafood.rakamin_customer
WHERE 
	(email LIKE '%yahoo.com' OR email LIKE '%roketmail.com')
	AND tanggal_registrasi BETWEEN DATE '2012-01-01' AND DATE '2012-03-31' 
	AND bulan_lahir IN ('Januari', 'Februari', 'Maret');

--soal 2
SELECT id_order, id_pelanggan, harga, (harga + (0.1 * harga)) AS harga_setelah_ppn,
    CASE
        WHEN (harga + (0.1 * harga)) <= 20000 THEN 'LOW'
        WHEN (harga + (0.1 * harga)) > 20000 AND (harga + (0.1 * harga)) <= 50000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS spending_bucket
FROM
    rakafood.rakamin_order
ORDER BY
    harga_setelah_ppn DESC;
	
--soal 3
SELECT 
	id_merchant, 
	COUNT (id_order) AS jumlah_order, 
	SUM (harga) AS jumlah_pendapatan_sebelum_ppn
FROM rakafood.rakamin_order
GROUP BY id_merchant
ORDER BY jumlah_pendapatan_sebelum_ppn DESC;

--soal 4
SELECT 
	metode_bayar, 
	COUNT (metode_bayar) AS jumlah_penggunaan FROM rakafood.rakamin_order
GROUP BY metode_bayar
HAVING COUNT(metode_bayar) > 10
ORDER BY jumlah_penggunaan DESC

--soal 5
SELECT
	MIN(jumlah_pelanggan) AS jumlah_pelanggan_terkecil,
	MAX(jumlah_pelanggan) AS jumlah_pelanggan_terbesar
FROM (
	SELECT
		kota,
		COUNT (id_pelanggan) AS jumlah_pelanggan FROM rakafood.rakamin_customer_address
GROUP BY kota
) AS subquery;

--soal 6
SELECT 
	rakamin_merchant.nama_merchant,
	rakamin_order.metode_bayar,
	COUNT(rakamin_order.id_order) AS jumlah_penggunaan
FROM rakafood.rakamin_merchant
JOIN rakafood.rakamin_order ON rakamin_merchant.id_merchant = rakamin_order.id_merchant
GROUP BY 
	rakamin_merchant.nama_merchant,
	rakamin_order.metode_bayar
ORDER BY
	rakamin_merchant.nama_merchant,
	jumlah_penggunaan DESC;

--soal 7
WITH pelanggan_total_kuantitas AS (
    SELECT 
        o.id_pelanggan,
        SUM(o.kuantitas) AS total_kuantitas
    FROM 
        rakamin_order AS o
    GROUP BY 
        o.id_pelanggan
    HAVING 
        SUM(o.kuantitas) > 5
)
SELECT 
    p.id_pelanggan,
    ptk.total_kuantitas,
    p.nama,
    p.email
FROM 
    rakamin_customer AS p
JOIN 
    pelanggan_total_kuantitas AS ptk ON p.id_pelanggan = ptk.id_pelanggan;









