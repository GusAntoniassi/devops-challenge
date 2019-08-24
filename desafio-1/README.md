## Executar a aplicação
Aplicação sobe por default na porta 5000
```sh
$ pip install -r requirements.txt
$ python main.py
```

### Testar a aplicação
Teste GET
```sh
$ curl http://localhost:5000/characters
```
Teste POST
```sh
$ curl -X POST -H "Content-Type: application/json" -d '{
  "Race": "Hobbit",
  "age": "589",
  "name": "Gollum"
}' http://localhost:5000/characters
```