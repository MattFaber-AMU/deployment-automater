# this changes the elements in the yaml file in order for a successful deploy to happen.
#!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!! RUN THIS AFTER DeployFIleCopier.py

import fileinput

# changes the placeholder for the name of the app, with a -


def fileopener(frompath, reponame):
    with open(frompath, "r") as file:
        filedata = file.read()

        filedata = filedata.replace('placeholder', reponame)

        with open(frompath, 'w') as file:
            file.write(filedata)

# changes the dockername placeholder to the docker file name


def dockernamechange(frompath, reponame):
    with open(frompath, "r") as file:
        filedata = file.read()
        filedata = filedata.replace('dockername', reponame)

        with open(frompath, 'w') as file:
            file.write(filedata)


# change these to the correct names that reflect the app
reponame = 'content-game'
dockername = 'content_game'

# change the path to your local github directory
prodakspath = "C:\\Users\\mfaber\\Documents\\GitHub\\" + \
    reponame+"\\.github\\workflows\\aks-production.yaml"
stagepath = "C:\\Users\\mfaber\\Documents\\GitHub\\" + \
    reponame + "\\.github\\workflows\\aks-staging.yaml"
valuespath = "C:\\users\\mfaber\\documents\\Github\\" + \
    reponame + "\\deployments\\Charts\\values.yaml"
chartpath = "C:\\Users\\mfaber\\documents\\Github\\" + \
    reponame + "\\deployments\\Charts\Chart.yaml"

# method calls
fileopener(prodakspath, reponame)
fileopener(stagepath, reponame)
fileopener(valuespath, reponame)
fileopener(chartpath, reponame)
dockernamechange(stagepath, dockername)
dockernamechange(prodakspath, dockername)
