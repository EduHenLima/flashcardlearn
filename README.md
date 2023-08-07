> Desenvolvido por: Ademilson & Eduardo

# Flash Cards Learn

## Helpers
- Start the application: uvicorn app.main:app
- Debug application: uvicorn app.main:app --reload

## Docker
- Add docker: docker pull mysql/mysql-server:latest
- Config Docker: docker run -d -p 3306:3306 --name mysql-docker-container -e MYSQL_ROOT_PASSWORD=flashcards -e MYSQL_DATABASE=flashcards -e MYSQL_USER=edu -e MYSQL_PASSWORD=flashcards mysql/mysql-server:latest
- Restar docker: docker restart 0a06f436dc68

#Mysql - Local
- Dash Docker Mysqsl: docker exec -it mysql-docker-container bash
- Open mysql with root: mysql -u root -p
- Create User: CREATE USER 'edu'@'localhost' IDENTIFIED BY '123456';
- All Privileges: GRANT ALL PRIVILEGES ON *.* TO 'edu'@'localhost' WITH GRANT OPTION;
- Flush: FLUSH PRIVILEGES;

## Documentations
- FastAPI: https://fastapi.tiangolo.com/
- Design Pattern Structure: https://levelup.gitconnected.com/structuring-fastapi-project-using-3-tier-design-pattern-4d2e88a55757
