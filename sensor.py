import time	#library ini digunakan untuk meng-import modul waktu.
import board	#library ini akan digunakan untuk menentukan dengan pin GPIO mana kita menghubungkan sensor DHT11.
import adafruit_dht	#Pustaka khusus sensor DHT.
import psutil	#perpustakaan untuk mengambil informasi tentang proses yang sedang berjalan.
for proc in psutil.process_iter():	# Kembalikan iterator yang menghasilkan instance kelas Proses untuk semua proses yang berjalan di mesin lokal.
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()	#perintah menghentikan proses.
sensor = adafruit_dht.DHT11(board.D23)	# Di sini kita mendefinisikan jenis sensor dan nomor pin.
while True:	#berjalan tanpa kondisi apapun sampai pernyataan break di eksekusi di dalam loop.
   	try:
        	temp = sensor.temperature	#membaca nilai suhu dari sensor.
        	humidity = sensor.humidity	#membaca nilai kelembaban dari sensor.
        	print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))	#mencetak hasilnya di layar. Mempertimbangkan akurasi sensor yang terbatas, hasilnya diformat tanpa desimal.
    	except RuntimeError as error:	#menangani error apabila terdapat kesalahan waktu proses.
        	print(error.args[0])	#menampilkan output error.
        	time.sleep(2.0)	#tunggu selama 2 detik.
        	continue	#sensor akan terus membaca dan menampilkan hasil.
    	except Exception as error:	#mendeteksi kesalahan selama dieksekusi. 
        	sensor.exit()	#fungsi untuk keluar.
        	raise error	#digunakan untuk membangkitkan ekspesi ketika kondisi error.
    	time.sleep(2.0)	#tunggu selama 2 detik.
import time	#library ini digunakan untuk meng-import modul waktu.
import board	#library ini akan digunakan untuk menentukan dengan pin GPIO mana kita menghubungkan sensor DHT11.
import adafruit_dht	#Pustaka khusus sensor DHT.
import psutil	#perpustakaan untuk mengambil informasi tentang proses yang sedang berjalan.
for proc in psutil.process_iter():	# Kembalikan iterator yang menghasilkan instance kelas Proses untuk semua proses yang berjalan di mesin lokal.
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()	#perintah menghentikan proses.
sensor = adafruit_dht.DHT11(board.D23)	# Di sini kita mendefinisikan jenis sensor dan nomor pin.
while True:	#berjalan tanpa kondisi apapun sampai pernyataan break di eksekusi di dalam loop.
   	try:
        	temp = sensor.temperature	#membaca nilai suhu dari sensor.
        	humidity = sensor.humidity	#membaca nilai kelembaban dari sensor.
        	print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))	#mencetak hasilnya di layar. Mempertimbangkan akurasi sensor yang terbatas, hasilnya diformat tanpa desimal.
    	except RuntimeError as error:	#menangani error apabila terdapat kesalahan waktu proses.
        	print(error.args[0])	#menampilkan output error.
        	time.sleep(2.0)	#tunggu selama 2 detik.
        	continue	#sensor akan terus membaca dan menampilkan hasil.
    	except Exception as error:	#mendeteksi kesalahan selama dieksekusi. 
        	sensor.exit()	#fungsi untuk keluar.
        	raise error	#digunakan untuk membangkitkan ekspesi ketika kondisi error.
    	time.sleep(2.0)	#tunggu selama 2 detik.

