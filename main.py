#this file is to automate creation of files for kubernetes workflows
from distutils.dir_util import copy_tree
import shutil

#copies helm files over to a project
def helmcopy(projectname):
    fromdirectory = "C:\\Users\\mfaber\\OneDrive - Andrews McMeel Universal\\Desktop\\deployer-automater\\helm\\"
    todirectory = "C:\\Users\\mfaber\\Documents\\GitHub\\" + projectname +"\\deployments\\charts\\"
    copy_tree(fromdirectory,todirectory)

#copies k8 files over to project
def k8scopy(projectname):
    fromdirectory = "C:\\Users\\mfaber\\OneDrive - Andrews McMeel Universal\\Desktop\\deployer-automater\\k8"
    todirectory = "C:\\users\mfaber\\documents\\github\\" +projectname+ "\\deployments\\k8s"
    copy_tree(fromdirectory,todirectory)

#copies workflows to .github directory
def copygithubworkflows(projectname): 
    fromdirectory = "C:\\Users\\mfaber\\OneDrive - Andrews McMeel Universal\\Desktop\\deployer-automater\\.github"
    todirectory = "C:\\users\\mfaber\\documents\\github\\"+ projectname 
    copy_tree(fromdirectory,todirectory)

projectname = "test"

#call methods
helmcopy(projectname)
k8scopy(projectname)
copygithubworkflows(projectname)