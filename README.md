# deployment-automater
automates the deployments of apps to azure


# How to use this
1. You will need to grab copies of the yaml files from the https://amuniversal.atlassian.net/wiki/spaces/DEVOps/pages/2096496727/Preparing+an+App+to+Deploy+to+Kubernetes
2. Put them in a directory and set the first path in each function to that absolute path
3. Change the target directory to the local path of your github repos that you check out
4. Run the script, and you should be able to have those files copied over and use this over and over again for the future

# Planned enhancements
1. Run github commands to commit and push
2. Creating the files with the templates and the correct changes to completely automate this with a button press
3. Possible GUI development
