### *API service English Teacher*


#### description

- This app is made for learning english

#### author

- Biyaslan Mokaev

#### service run instruction

- run main.py file


## FAST API

- JsonResponse (create response as json, we can specify: status_code, content, media_type) 
  ```from fastapi.responses import JsonResponse```
- BaseModel (base class for validate fields in body) ```from pydantic import BaseModel```
- Field (for validate field in body) ```from pydantic import Field```
- Path (for validate params in endpoint) ```from fastapi import Path```