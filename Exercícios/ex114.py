import urllib.request
import urllib

site = str(input("Vericar site: "))
try:
    sitet = urllib.request.urlopen(f'https://www.{site}')
except:
    print("\033[1;31mNão foi possível acessar o site informado!\033[m")
else:
    print("\033[1;32mSite acessado com sucesso!\033[m")