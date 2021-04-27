import fileinput

def fileopener(path, reponame): 
    with open(path, "r") as file: 
        filedata = file.read()
        
        filedata = filedata.replace('placeholder', reponame)

        with open(path, 'w') as file: 
            file.write(filedata)
        
#this changes the placeholder placeholder with the repo name for the 
def filechanger(path, reponame): 
    with fileinput.FileInput as file:
        for line in file:
            print(line.replace("placeholder", reponame), end='')



path = "C:\\Users\\Mfaber\\Documents\\github\\deployment-automater\\.github\\aks-production.yaml"
reponame = 'content-service'
fileopener(path, reponame)
