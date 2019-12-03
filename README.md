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