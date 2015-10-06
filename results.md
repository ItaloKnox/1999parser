http://www.1999.co.jp/eng/10345145

NAME: Super Fumina
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam Build Fighters Try
RELEASE DATE:			*release date pattern bug*
----------------------------------------------------
http://www.1999.co.jp/eng/10334868

ID: 10334868
NAME: Kamiki Burning Gundam
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam Build Fighters Try
RELEASE DATE: Sep, 2015
----------------------------------------------------
http://www.1999.co.jp/eng/10350033

ID: 10350033
NAME: V2 Gundam Ver.Ka
MANUFACTURE: Bandai
SCALE: Master Grade
SERIES: 1/100
RELEASE DATE: Gundam			*release date pattern bug*
----------------------------------------------------
http://www.1999.co.jp/eng/10345143

ID: 10345143
NAME: Gundam MK-II
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Z Gundam
RELEASE DATE:			*release date pattern bug*
----------------------------------------------------
http://www.1999.co.jp/eng/10338476

ID: 10338476
NAME: Gundam Barbatos
MANUFACTURE: Bandai
SCALE: 1/100
SERIES: Gundam Iron-Blooded Orphans
RELEASE DATE:			*release date pattern bug*
----------------------------------------------------
http://www.1999.co.jp/eng/10295035

ID: 10295035
NAME: LED Unit for RX-0 Unicorn Gundam
MANUFACTURE: Bandai
SCALE: 1/60
SERIES: Gundam UC
RELEASE DATE: Dec, 2014
----------------------------------------------------
http://www.1999.co.jp/eng/10127944

ID: 10127944
NAME: Strike Freedom Gundam
MANUFACTURE: Bandai
SCALE: 1/60
SERIES: Gundam SEED Destiny
RELEASE DATE: Dec, 2010
----------------------------------------------------
http://www.1999.co.jp/eng/10057482

ID: 10057482
NAME: XXXG-00W0 W-Gundam Zero Custom Special Ver.
MANUFACTURE: Bandai
SCALE: 1/60
SERIES: Gundam W -Endless Waltz-
RELEASE DATE: Jun, 2007
----------------------------------------------------
http://www.1999.co.jp/eng/10044621

ID: 10044621
NAME: Strike Rouge + Sky Grasper
MANUFACTURE: Bandai
SCALE: 1/60
SERIES: Gundam SEED
RELEASE DATE: Aug, 2005
----------------------------------------------------
http://www.1999.co.jp/eng/10334498

ID: 10334498
NAME: Metal Build Strike Freedom Gundam
MANUFACTURE: Bandai
SCALE: Non		*no-scale test
SERIES: Gundam SEED Destiny
RELEASE DATE:
----------------------------------------------------
http://www.1999.co.jp/eng/10329542

ID: 10329542
NAME: Red Warrior Amazing
MANUFACTURE: Bandai
SCALE: Non
SERIES: Gundam Build Fighters Try
RELEASE DATE: Aug, 2015
----------------------------------------------------
http://www.1999.co.jp/eng/10306423

ID: 10306423
NAME: Star Winning Gundam
MANUFACTURE: Bandai
SCALE: Non
SERIES: Gundam Build Fighters Try
RELEASE DATE: Feb, 2015
----------------------------------------------------
http://www.1999.co.jp/eng/10306422

ID: 10306422
NAME: Lightning Back Weapon System Mk-II
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam Build Fighters Try
RELEASE DATE: Feb, 2015
----------------------------------------------------
http://www.1999.co.jp/eng/10303609 	
*release date is Mid Feb., 2015*
*doesn't work because there are two originals listed*
*commenting self.release_date_code pushes the second original to the release date space

ID: 10303609
NAME: Hi-Nu Gundam Vrabe
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam Build Fighters A
RELEASE DATE: Build Fighters D 			*release date pattern bug*
----------------------------------------------------
http://www.1999.co.jp/eng/10295060

ID: 10295060
NAME: XXXG-00W0 Wing Gundam Zero EW
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam W -Endless Waltz-
RELEASE DATE: Dec, 2014
----------------------------------------------------
http://www.1999.co.jp/eng/10267266

ID: 10267266
NAME: MSM-07S Char`s Z`Gok
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam (First)
RELEASE DATE: Jul, 2014
----------------------------------------------------
http://www.1999.co.jp/eng/10146341

ID: 10146341
NAME: MS-06F Zaku II
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam (First)
RELEASE DATE: Jul, 2011
----------------------------------------------------
http://www.1999.co.jp/eng/10138068

ID: 10138068
NAME: GAT-X105 Aile Strike Gundam
MANUFACTURE: Bandai
SCALE: 1/144
SERIES: Gundam SEED
RELEASE DATE: Apr, 2011
----------------------------------------------------
http://www.1999.co.jp/eng/10011577

```Traceback (most recent call last):
  File "parse1999.py", line 69, in <module>
    gunpla = Gunpla(gunpla_id, lst)
  File "C:\1999parser\gunpla.py", line 11, in __init__
    self.release_date = re.sub(r'^\W*\w+\W*', '', lst[4]).replace('.', '')
IndexError: list index out of range```

***No release date = date error***
----------------------------------------------------
http://www.1999.co.jp/eng/10291243

```Traceback (most recent call last):
  File "parse1999.py", line 69, in <module>
    gunpla = Gunpla(gunpla_id, lst)
  File "C:\1999parser\gunpla.py", line 14, in __init__
    '%b, %Y')
  File "C:\Python27\lib\_strptime.py", line 325, in _strptime
    (data_string, format))
ValueError: time data 'SEED Destiny Astray B' does not match format '%b, %Y'```

Comment the self.release_date_code, then:

ID: 10291243
NAME: Gundam Astray Blue Frame D
MANUFACTURE: Bandai
SCALE: Master Grade
SERIES: 1/100
RELEASE DATE: SEED Destiny Astray B 		*release date pattern bug*
