# jupyter-lde

1) Generate password token:
python generate_token.py -p 123456

2) update token in .env file

3) docker-compose up -d

4) Get port mapping
docker ps
(to get contaiter name)
docker port containerNameOrId 8888

5) In order to get token execute:
docker exec jupyter jupyter notebook list

6) Run
http://127.0.0.1:port

