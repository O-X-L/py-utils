import re as regex

# source: https://validators.readthedocs.io/en/latest/_modules/validators/email.html
EMAIL_REGEX_USER = regex.compile(
    # dot-atom
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+"
    r"(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"
    # quoted-string
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|'
    r"""\\[\001-\011\013\014\016-\177])*"$)""",
    regex.IGNORECASE
)
EMAIL_REGEX_DOMAIN = regex.compile(
    # domain
    r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?$)'
    # literal form, ipv4 address (SMTP 4.1.3)
    r'|^\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)'
    r'(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$',
    regex.IGNORECASE
)


def valid_email(email: str) -> bool:
    if not email or '@' not in email:
        return False

    user_part, domain_part = email.rsplit('@', 1)

    if not EMAIL_REGEX_USER.match(user_part):
        return False

    if not EMAIL_REGEX_DOMAIN.match(domain_part):
        # Try for possible IDN domain-part
        try:
            domain_part = domain_part.encode('idna').decode('ascii')
            return EMAIL_REGEX_DOMAIN.match(domain_part)

        except UnicodeError:
            return False

    return True
