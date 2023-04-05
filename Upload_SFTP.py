import ConnectSFTP
import sys
import Logs
import os

#Subir archivo
def upload_file(localFilePath, remoteFilePath):
    try:        
        Logs.file_log().info("******* INIT ***********")
        Logs.file_log().info("localFilePath In: "+str(localFilePath))
        Logs.file_log().info("remoteFilePath In: "+str(remoteFilePath))

        if(localFilePath == "" or localFilePath is None):
            print("Ruta localFilePath debe ser distinto a vacio")
            return
        if(remoteFilePath == "" or remoteFilePath is None):
            print("Ruta remoteFilePath debe ser distinto a vacio")
            return

        # file name with extension
        file_name = os.path.basename(localFilePath)
        remoteFilePath = remoteFilePath +"/"+file_name
        
        Logs.file_log().info("file_name: "+str(file_name))
        Logs.file_log().info("remoteFilePath proc: "+str(remoteFilePath))

        with ConnectSFTP.conectar() as sftp:
            sftp.put(localFilePath, remoteFilePath)
    except Exception as e:
        Logs.file_log().error("Error "+str(e))

        
upload_file(str(sys.argv[1]),str(sys.argv[2]))