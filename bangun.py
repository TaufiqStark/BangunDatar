#!/usr/bin/python
# Jika kamu ingin merecode code ini, donasi saya di "https://paypal.me/DonateTaufiq" thx :v
import time,os,sys

w = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
u = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
s = "\033[97;1m"

logo = '''
\t\t############################################
\t\t#\033[91;1m Autor  =\033[96;1m  Taufiq Stark\033[92;1m                   #
\t\t#\033[91;1m Github =\033[96;1m  https://github.com/TaufiqStark\033[92;1m #
\t\t#\033[91;1m Donasi =\033[96;1m  https://paypal.me/DonateTaufiq\033[92;1m #
\t\t############################################  
'''

def prsgi():
	lagi = 'y'
	while lagi == 'y':
		p = int(input('\n{}[{}*{}]Panjang:{} '.format(h,m,h,a)))
		l = int(input('{}[{}*{}]Lebar:{} '.format(h,m,h,a)))
		L = p**2
		K = 4 * p
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
		lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))
	
	
def prsgipjg():
	lagi = 'y'
	while lagi == 'y':	
		p = int(input('\n{}[{}*{}]Panjang:{} '.format(h,m,h,a)))
		l = int(input('{}[{}*{}]Lebar:{} '.format(h,m,h,a)))
		L = p*l
		K = 2*(p+l)
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
		lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))
	
	
def jjrgnjng():
	lagi = 'y'
	while lagi == 'y':	
		p = int(input('\n{}[{}*{}]Alas:{} '.format(h,m,h,a)))
		l = int(input('{}[{}*{}]Tinggi:{} '.format(h,m,h,a)))
		L = p*l
		K = 2*(p+l)
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
		lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))
	

def blhktpt():
	lagi = 'y'
	while lagi == 'y':	
		p = int(input('\n{}[{}*{}]Diagonal1:{} '.format(h,m,h,a)))
		l = int(input('{}[{}*{}]Diagonal2:{} '.format(h,m,h,a)))
		L = p*l/2
		K = 4*p
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
			lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))
		
def lyang():
	lagi = 'y'
	while lagi == 'y':	
		p = int(input('\n{}[{}*{}]Diagonal1:{} '.format(h,m,h,a)))
		l = int(input('{}[{}*{}]Diagonal2:{} '.format(h,m,h,a)))
		L = p*l/2
		K = 2*(p+l)
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
			lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))
				
def trpsm():
	lagi = 'y'
	while lagi == 'y':
		e = int(input('\n{}[{}*{}]Sisi AB:{} '.format(h,m,h,a)))
		b = int(input('\n{}[{}*{}]Sisi BC:{} '.format(h,m,h,a)))
		c = int(input('\n{}[{}*{}]Sisi CD:{} '.format(h,m,h,a)))
		d = int(input('\n{}[{}*{}]Sisi DA:{} '.format(h,m,h,a)))
		t = int(input('\n{}[{}*{}]Tinggi:{} '.format(h,m,h,a)))
		
		print(m,'\n#Tulis sisi yang sejajar!')
		p = int(input('\n{}[{}*{}]Sisi1:{} '.format(h,m,h,a)))
		l = int(input('{}[{}*{}]Sisi2:{} '.format(h,m,h,a)))
		L = p+d/2*t
		K = e+b+c+d
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
			lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))

def sgtga():
	lagi = 'y'
	while lagi == 'y':	
		e = int(input('\n{}[{}*{}]Sisi AB:{} '.format(h,m,h,a)))
		b = int(input('{}[{}*{}]Sisi BC:{} '.format(h,m,h,a)))
		c = int(input('{}[{}*{}]Sisi BC:{} '.format(h,m,h,a)))
		al = int(input('{}[{}*{}]Alas:{} '.format(h,m,h,a)))
		t = int(input('{}[{}*{}]Tinggi:{} '.format(h,m,h,a)))
		L = al*t/2
		K = e+b+c
		print('\n{}1. {}Keliling\n{}2. {}Luas\n'.format(m,k,m,k))
		pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
		if pil == 1:
			print('{}[{}#{}]Kelilingnya: '.format(h,m,h),a,K)
		if pil == 2:
			print('{}[{}#{}]Luasnya: '.format(h,m,h),a,L)
			lagi = input('{}[{}*{}]Lagi??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))



lagi = 'y'
while lagi == 'y':
	os.system('pkg install figlet')
	os.system('clear')
	print(u)
	time.sleep(0.2)
	os.system('figlet Bangun Datar')
	time.sleep(0.2)
	print(h,logo)
	time.sleep(0.2)
	print('Luas & Keliling Bangun Datar!\n')
	print('{}1. {}Persegi\n{}2. {}Persegi Panjang\n{}3. {}Jajargenjang\n{}4. {}Belah Ketupat\n{}5. {}Layang - Layang\n{}6. {}Trapesium\n{}7. {}Segitiga\n{}99. {}Exit \n'.format(m,k,m,k,m,k,m,k,m,k,m,k,m,k,m,k))
	pil = int(input('{}[{}*{}]Pilih:{} '.format(h,m,h,a)))
	if pil == 1:
		prsgi()
	if pil == 2:
		prsgipjg()
	if pil == 3:
		jjrgnjng()
	if pil == 4:
		blhktpt()
	if pil == 5:
		lyng()
	if pil == 6:
		trpsm()
	if pil == 7:
		sgtga()
	if pil == 99:
		print('Thanks for use!',u)
		os.system('figlet \'Thanks for use !\'')
		with open('README.md') as r:
			print(s,r.read())
		sys.exit(1)
	elif pil > 7 and pil != 99:
		print(m,'\nERROR: Wrong Input!\n')
	lagi = input('{}[{}*{}]Kembali ke Menu??{}[{}y/n{}]{}:{} '.format(h,m,h,u,m,u,h,a))	
	
	if lagi == 'n':
		print('Thanks for use!',u)
		os.system('figlet \'Thanks for use !\'')
		with open('README.md') as r:
			print(s,r.read())
		sys.exit(1)
		
		
		
	
	