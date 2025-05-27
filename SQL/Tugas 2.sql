SELECT nama, email, bulan_lahir, tanggal_registrasi FROM rakafood.rakamin_customer
WHERE 
	(email LIKE '%yahoo.com' OR email LIKE '%roketmail.com')
	AND tanggal_registrasi BETWEEN DATE '2012-01-01' AND DATE '2012-03-31' 
	AND bulan_lahir IN ('Januari', 'Februari', 'Maret');
	
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

