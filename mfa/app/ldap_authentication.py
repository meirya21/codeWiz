from time import pthread_getcpuclockid
from ldap3 import Server, Connection, ALL


def ldap_authentication(user_name, user_pass):

    ldap_server = "ldap://openldap:1389"
    root_dn = "dc=example,dc=org"
    user = f'cn={user_name},{root_dn}'

    server = Server(ldap_server, get_info=ALL)

    try:
        connection = Connection(server, user=user,
                                password=user_pass)
        if not connection.bind():
            l_faild_msg = f' ** Failed Authentication: {connection.last_error}'
            return l_faild_msg
        else:
            l_success_msg = 'Success'
            return l_success_msg
            
    except Exception as e:
        return e