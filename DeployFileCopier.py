#this file is to automate creation of files for kubernetes workflows
from distutils.dir_util import copy_tree
import shutil

#copies helm files over to a project
def helmcopy(projectname):
    fromdirectory = "C:\\Users\\mfaber\\Documents\\github\\deployment-automater\\helm"
    todirectory = "C:\\Users\\mfaber\\Documents\\GitHub\\" + projectname +"\\deployments\\charts"
    copy_tree(fromdirectory,todirectory)

#copies k8 files over to project
def k8scopy(projectname):
    fromdirectory = "C:\\Users\\mfaber\\Documents\\github\\deployment-automater\\k8"
    todirectory = "C:\\users\mfaber\\documents\\github\\" +projectname+ "\\deployments\\k8s"
    copy_tree(fromdirectory,todirectory)

#copies workflows to .github directory
def copygithubworkflows(projectname): 
    fromdirectory = "C:\\Users\\mfaber\\Documents\\github\\deployment-automater\\.github"
    todirectory = "C:\\users\\mfaber\\documents\\github\\"+ projectname + "\\.github\\workflows"
    copy_tree(fromdirectory,todirectory)


copygithubworkflows("spot-the-difference_game")