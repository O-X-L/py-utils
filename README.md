# Utils Collection

## Data States

```python3
from oxl_utils.state import is_set
from oxl_utils.state import is_null
```

## Network interactions

```python3
# dnspython wrapper
from oxl_utils.net import resolve_dns

# get first IP
from oxl_utils.net import resolve_first_ip

# check if a remote port is reachable
from oxl_utils.net import is_port_open
```

## Validators

```python3
# validate email format
from oxl_utils.valid.email import valid_email

# also check for valid MX record of e-mail domain
from oxl_utils.valid.email import valid_email_dns

# ips and networks
from oxl_utils.valid.net import valid_ip
from oxl_utils.valid.net import valid_ip4
from oxl_utils.valid.net import valid_ip6
from oxl_utils.valid.net import valid_net4
from oxl_utils.valid.net import valid_net6
from oxl_utils.valid.net import valid_public_ip
from oxl_utils.valid.net import valid_asn

from oxl_utils.valid.dns import valid_domain
from oxl_utils.valid.email import valid_email
from oxl_utils.valid.email import has_mailserver

```

## Django

```python3
# fix datetime timezone
from oxl_utils.dj.dt import datetime_from_db
```
