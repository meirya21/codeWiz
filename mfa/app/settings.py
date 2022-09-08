from ldap3 import Server, Connection, ALL

# ldap server hostname and port
ldap_server = 'ldap://openldap:1389'

# dn
root_dn = 'dc=example,dc=org'

# ldap user and password
ldap_user_name = 'admin'
ldap_password = 'adminpassword'

# user
user = f'cn={ldap_user_name},{root_dn}'

server = Server(ldap_server, get_info=ALL)

connection = Connection(server,
                        user=user,
                        password=ldap_password,
                        auto_bind=False)

# logging
print(f" *** ldap bind is \n{connection}")