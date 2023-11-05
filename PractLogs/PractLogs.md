# Практическая работа №3
## Логирование
Были созданы две виртуальные машины в одной подсети<br />
Машина 1:<br /><br />![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/57b715f2-ba07-4222-be21-f16b56cbed78)<br /><br />
Машина 2:<br /><br />![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/eeeb7897-d6bf-4847-b43c-a57fbd5c4af6)<br /><br />
Установлен rsyslog<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/58189a6c-34cb-4818-bd73-f5a825e3d94a)<br /><br />
На машине 2 раскомментированы строки в конфигурации для настройки серверной стороны по протоколу UDP<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/afadb461-9d7a-4ef8-9f98-a0e11f1ae87d)<br /><br />
После настройки директории для сохранения файлов перезагрузили сервис и проверили, открыт ли сокет на сервере:<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/3b926466-397c-424d-86bc-ed95225d56b8)<br /><br />
Папка с логами доступна на сервере:<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/b86fc4d0-d814-417d-9594-81452757c622)<br /><br />
