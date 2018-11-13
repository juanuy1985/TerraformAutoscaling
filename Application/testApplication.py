#sudo apt-get update
#sudo apt install python-minimal

from time import time

print("Este código se come el procesador")

begin = time()
current = time()
while(current-begin<300):
    current = time()
   
print("Termina :)")