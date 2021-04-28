import fileinput

def fileopener(path, reponame): 
    with open(path, "r") as file: 
        filedata = file.read()
        
        filedata = filedata.replace('placeholder', reponame)

        with open(path, 'w') as file: 
            file.write(filedata)

path = "C:\\Users\\Mfaber\\Documents\\github\\deployment-automater\\.github\\aks-production.yaml"
reponame = 'content-service'
fileopener(path, reponame)
