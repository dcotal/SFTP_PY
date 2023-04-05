import pysftp

myHostname = "url_server"
myUsername = "user"
myPassword = "pass"
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  


def conectar():
    try:
        cnx = pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts)
        print(" OK! Conexión a FTP exitosa.")
        return cnx
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)