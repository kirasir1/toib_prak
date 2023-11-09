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
Устанавливаем Grafana Loki<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/a72e6f42-91b9-430e-ae0e-e4cee6deec2a)<br /><br />
На клиенте настроили promtail для отправки логов<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/a26db8b7-02ca-4601-abd9-cc407e645602)<br /><br />
Loki работает исправно<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/d3933da7-c479-40ab-bb8b-604c115aa352)<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/ace526e6-ee7f-450f-bf6b-20a32f79e0b9)<br /><br />
На сервере поднимается сервер Signoz<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/66c039b5-ad06-4b55-a693-df7d89d4f42c)<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/218ec804-89b3-492f-86ab-c821ddb0db08)<br /><br />
На клиенте - приложение на nodejs из репозитория Signoz<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/f6a20329-ee56-4501-9f62-1a6dfa88b031)<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/e71724cd-cc5c-4ea5-bea6-08558a4c9b15)<br /><br />
Телеметрия отображается в Signoz<br /><br />
![изображение](https://github.com/kirasir1/toib_prak/assets/13931629/714a92ce-d8fc-470b-8359-8147bacd9860)<br /><br />
