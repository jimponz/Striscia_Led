import requests

## http://87.3.186.82:86/?r8g57b255&

contAV = 0
contIN = 255

def PWMmagenta():
    print("MAGENTA")
    cont = 0
    contMax = 255
    Max = 255
    while (cont<Max):
        requests.get("http://192.168.1.81/?r"+str(cont)+"g0"+"b"+str(contMax)+"&")
        print("R"+str(cont)+" G0"+" B"+str(contMax))
        cont +=1
        contMax -=1
        if(cont == Max):
            contMax= Max
            while(contMax > 10):
                requests.get("http://192.168.1.81/?r"+str(contMax)+"g0"+"b"+str(Max-contMax)+"&")
                print("r"+str(contMax)+" g0"+" b"+str(Max-contMax))
                contMax -=1
def PWMgiallo():
    print("GIALLO")
    cont = 0
    contMax = 255
    Max = 255
    while (cont<Max):
        requests.get("http://192.168.1.81/?r"+str(cont)+"g"+str(cont)+"b"+str(contMax)+"&")
        print("R"+str(cont)+" G"+str(cont)+" B"+str(contMax))
        cont +=1
        contMax -=1
        if(cont == Max):
            contMax= Max
            while(contMax > 10):
                requests.get("http://192.168.1.81/?r"+str(contMax)+"g"+str(contMax)+"b"+str(Max-contMax)+"&")
                print("r"+str(contMax)+" g"+str(contMax)+" b"+str(Max-contMax))
                contMax -=1

def PWMciano():
    print("CIANO")
    cont = 0
    contMax = 255
    Max = 255
    while (cont<Max):
        requests.get("http://192.168.1.81/?r0"+"g"+str(cont)+"b"+str(contMax)+"&")
        print("R0"+" G"+str(cont)+" B"+str(contMax))
        cont +=1
        contMax -=1
        if(cont == Max):
            contMax= Max
            while(contMax > 10):
                requests.get("http://192.168.1.81/?r0"+"g"+str(contMax)+"b"+str(Max-contMax)+"&")
                print("r0"+" g"+str(contMax)+" b"+str(Max-contMax))
                contMax -=1

while (True):
    PWMmagenta()
    PWMgiallo()
    PWMciano()

    
##while (contAV<255*6):
##    
##    if (contAV <= 255):
##        print("1 transizione: aumento il rosso")
##        requests.get("http://87.3.186.82:86/?r"+str(contAV)+"g0"+"b0"+"&")
##
##    if (contAV > 255 and contAV <= 255*2):
##        print("2 transizione: diminuisco il rosso e aumento il blu")
##        requests.get("http://87.3.186.82:86/?r"+str(contIN)+"g0"+"b"+str(contAV-255)+"&")
##        
##    if (contAV >255*2 and contAV < 255*3):
##        print("3 transizione: PWM VIOLA")
##        PWMviola()
##        
##    if (contAV >255*3 and contAV < 255*4):
##        print("4 transizione: aumento il rosso e diminuisco il verde e aumento il blu")
##        requests.get("http://87.3.186.82:86/?r"+str(contAV-255*3)+"g"+str(contIN)+"b"+str(contAV-255*3)+"&")
##        
##    if (contAV >255*4 and contAV < 255*5):
##        print("5 transizione: diminuisco il rosso e diminuisco il verde e diminuisco il blu")
##        requests.get("http://87.3.186.82:86/?r"+str(contIN)+"g"+str(contIN)+"b"+str(contIN)+"&")
##        
##    if (contAV >255*5 and contAV < 255*6):
##        print("5 transizione: AZZERO il rosso e aumento il verde e diminuisco il blu")
##        requests.get("http://87.3.186.82:86/?r0"+"g"+str(contAV-255*5)+"b"+str(contIN)+"&")        
##    if (contAV == 255):
##        contIN = 255
##    if (contAV == (255*6)-1):
##        contAV =0;
##        contIN = 255
##        
##    contAV += 1
##    contIN -= 1
    
        
