# Francesinhas Proxy

This is a implementation of a proxy for the `francesinhas.com` website.

## Deployment requirements

### Required environment variables
```
ALLOWED_HOSTS: A CSV list with the allowed domains/IPs (e.g. 122.122.333.12)
DEBUG: true
FRANCESINHAS_URL: http://francesinhas.com
FRANCESINHAS_PLACES_API: /api/v1/places
LOG_LEVEL: INFO
```

### Optional environment variables
```
DATABASE_ENABLED: True to enable the PostgreSQL database engine
DATABASE_USER: The user of the database
DATABASE_PASSWORD: The password of the user
DATABASE_HOST: The address of the database
DATABASE_HOST: The port of the database
```

## APIs

### Places

**Endpoint**

```
GET /places/  List of places from francesinhas.com
```

**Params**

```
page: Page number to fetch (e.g. /places?page=5)
```