import re

RE_EMAIL = re.compile(r'^[a-z0-9A-Z-_%!#$%&*+^_{|}~]+([.,]*[a-z0-9A-Z-_%!#$%&*+^_`{|}~])*@'
                      r'([A-Za-z0-9]+[a-zA-Z0-9-]*[A-Za-z0-9]+\.)+[a-zA-Z]{2,4}$')


def email_parse(email):
    try:
        assert RE_EMAIL.match(email)
    except AssertionError:
        raise ValueError(f'wrong email: {email}')
    else:
        m = re.match(r"(?P<username>^[a-z0-9A-Z-_%!#$%&*+^_{|}~]+([.,]*[a-z0-9A-Z-_%!#$%&*+^_`{|}~])*)@"
                     r"(?P<domain>([A-Za-z0-9]+[a-zA-Z0-9-]*[A-Za-z0-9]+\.)+[a-zA-Z]{2,4}$)", email)
        email_dict = m.groupdict()
        return email_dict


print(email_parse("som.e_stuff@li-st.ru.ru"))