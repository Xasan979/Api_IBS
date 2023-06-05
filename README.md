# Api_IBS

## Как запустить:
   Создайте venv и установите требования
   
       cd (путь к папки с проектом)
       
       Mac OS
          python3 -m venv env
          source env/bin/activate - for Unix or MacOS
          pip install -r requirements.txt
  
       Windows
          py -m venv venv
          venv\Scripts\activate
          py -m pip install -r requirements.txt

          
## Получение отчетов: 
   Установка allure 
   
       В командной строке
   
       Mac OS
          brew install allure

       Windows 
          scoop install allure


## Провести тест:
       В командной строке
   
       API
          python -m pytest --alluredir=reports/test_results_api_web api/tests/test_api.py

       WEB
          python -m pytest --alluredir=reports/test_results_api_web web/tests/test_web.py  


## Сгенерировать отчет:
       В командной строке 
   
          cd (путь к папки с проектом)  
          allure serve reports/test_results_api_web


```
███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░
   
             ██╗░░░██╗███████╗██╗░░██╗
             ██║░░░██║██╔════╝██║░██╔╝
             ╚██╗░██╔╝█████╗░░█████═╝░
             ░╚████╔╝░██╔══╝░░██╔═██╗░
             ░░╚██╔╝░░███████╗██║░╚██╗
             ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
```