#// Zip Cracker Cracking Tutorial
## Don't forget to hit SUBSCRIBE, LIKE, COMMENT, and LEARN :) ... it's good to learn.




'''imports'''
import zipfile


count = 1

with open('darkweb2017-top10000.txt','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('locked1.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass


