# xapo-rest

## API

The API runs currently on flask; for production this should
be be moved to a serious server.

### grab_and_save

Saves a Request Record to the database; by sending
a POST request to the API.

The POST request has to contain the following two fields:
- `currency` with a string as value
- `amount` with a float as value

`currency` has to meet the following conditions:
- has to be a string with exactly three letters [A-Z]
- lower case letters are accepted and transformed to
upper case letters

### last

Returns a array(list) of dictionaries that contains 
the latest Request Records; by sending a GET request
to the API.

usage:
- `<url>/last[/<number>[/<currency>]]` or
- `<url>/last[/<currency>[/<number>]]`

`<number>`:
- queries for last `<number>` integers
- if `<number>` is larger than available entries, 
all entries are returned
- has to be a positive integer
- if `<number>` is omitted, the (single) last Request
Record is returned

`<currency>`:
- queries for the currency provided
- has to be a string with exactly three letters [A-Z]
- lower case letters are accepted and transformed to
upper case letters

curl:
```
curl http://localhost:5000/last
curl http://localhost:5000/last/10
curl http://localhost:5000/last/2
curl http://localhost:5000/last/EUR
curl http://localhost:5000/last/EUR/2
curl http://localhost:5000/last/2/EUR
```