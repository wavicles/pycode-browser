from random import choice
import string

def gen_password(length=8,chars=string.letters+string.digits):
	newpasswd=[]
	for i in range(length):
		newpasswd.append(choice(chars))
	return string.join(newpasswd,"")

print __name__

if __name__=='__main__':
	print gen_password()
