# MicroServices

1. Установить docker и docker-compose
2. Чтобы запустить в тервинале нужно ввести 

```bash
-- Run all services
$> docker-compose up -d
```

3. В браузере открыть http://localhost:8000/
4. В поле ввести текст на Английском
5. При нажатии на кнопку отправляется POST запрос, его обрабатывает fastapi
6. FastApi обращается к микросервису torch-serve для получения сентимента предложения

7. Чтобы отключить контейнеры и удалить images 

```bash
-- Stop all services
$> docker-compose down

-- Stop and remove all services and images
$> docker-compose down -v --rmi all

-- Remove all unused containers, networks and images
$> docker system prune
```
