import requests
import os
import json
import time
name = "nameofdir"
#from fp.fp import FreeProxy
import requests

tag = 'yuuri_(shoujo_shuumatsu_ryokou)'

pr = False
countoff = 0
headers = {

    "User-Agent":  "gdl/1.24.5",

}
proxies = {}
if(pr == True):
    from fp.fp import FreeProxy
    proxyh = FreeProxy(https=True).get()
    proxy = FreeProxy(https=False).get()
    proxies = {
        'https': proxy,
        'http': proxyh
    }

print(proxies)
ida = 1
md5 = ""
print(os.getcwd())
os.system("mkdir "+os.getcwd()+"/"+name)
#os.system("rm list.txt")
with open("list.txt", "a") as myfile:
    myfile.write("\n\n\n\n")
myfile.close()

f = open("save.txt", "r")
try:
    ida=int(f.read())
except Exception:
    f = open("save.txt", "w")
    f.write(str(ida))
    f.close()
while (True):
    ida = 1+ida
    f = open("save.txt", "w")
    f.write(str(ida))
    f.close()
    
    f = open("save.txt", "r")
    ida=int(f.read())
    
    if (pr ==True):
        response_API = requests.get('https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=1&id='+str(ida)+'&json=1', proxies=proxies,  verify=True)
    else:
        response_API = requests.get('https://safebooru.org/index.php?page=dapi&s=post&q=index&pid=0&limit=9999&json=1&tags=la_pluma_(arknights)', headers=headers)
    status = int(response_API.status_code)    


    if(not int(status) == 200 and not int(status) == 404):
        countoff += 1
        print(countoff)
        time.sleep(60)
    else:
        countoff = 0
    if(countoff == 69):
        exit()
    print(str(response_API.status_code)+"\n")
    data = response_API.text
    print(data +"\n")
    time.sleep(5)
    try:

        parse_json = json.loads(data)
        dirn = parse_json[ida]['directory']
        print(dirn)
        mld = parse_json[ida]['id']
        img = parse_json[ida]['image']
        #url = parse_json['file_url']
        #ext = parse_json['file_ext']
        #md5 = parse_json['md5']
        url = "https://safebooru.org/images/"+dirn+"/"+str(img)

        split_tup = os.path.splitext(url)
        #print(split_tup)

        file_name = split_tup[0]
        ext = split_tup[1]


        with open("list.txt", "a") as myfile:
            pass
            #myfile.write(str("\n\n"+str(ida)+"\n"))
        myfile.close()
        with open("list.txt", "a") as myfile:
            myfile.write("\n"+str(img)+"\n")
        myfile.close()
        with open("list.txt", "a") as myfile:
            myfile.write(str("id: "+str(mld)+"\n"))
        myfile.close()
        with open("list.txt", "a") as myfile:
            myfile.write(str("\n\n"))
        myfile.close()
        #print("url:", url)
        os.system("wget "+str(url)+" -O "+os.getcwd()+"/"+name+"/"+img)
    except Exception as e:
        print(e)
        time.sleep(10)
        pass
    time.sleep(10)


