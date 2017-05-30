# OngHerdeirosBackend

This is a service to get itens needed by Ong Herdeiros and all the events.

## Events
To see all the events, make a GET request to this endpoint: http://flaskappteste.azurewebsites.net/api/herdeiros/events/all

example of return:
```json
{
  "events": [
    {
      "date": "2017-06-05 17:00:00", 
      "name": "Noite do Bingo"
    }, 
    {
      "date": "Poker", 
      "name": "2017-06-13 16:00:00"
    }, 
    {
      "date": "Truco", 
      "name": "2017-06-16 18:00:00"
    }
  ]
}
```

## Itens needed
To see all the itens needed, make a GET request to this endpoint: http://flaskappteste.azurewebsites.net/api/herdeiros/itens/all

example of return:
```json
{
  "itens": [
    {
      "description": "Geladeira", 
      "name": "Geladeira"
    }, 
    {
      "description": "Carro", 
      "name": "Carro"
    }, 
    {
      "description": "Fogao", 
      "name": "Fogao"
    }
  ]
}
```
