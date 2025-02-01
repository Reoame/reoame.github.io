import os
import subprocess

def deploy():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "update"], check=True)
    subprocess.run(["git", "push", "origin", "master"], check=True)

def deploy_first():
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "first commit"], check=True)
    print("------------------------------请在github上新建一个仓库，并将远程仓库地址填入------------------------------")
    url = input("请输入远程仓库地址：")
    subprocess.run(["git", "remote", "add", "origin", url], check=True)
    print("------------------------------请查看Github仓库的分支------------------------------")
    branch = input("请输入分支名称（master 或 main）：")
    if branch in ["master", "main"]:
        subprocess.run(["git", "push", "-u", "origin", branch], check=True)
        with open('1.txt', 'w') as f:
            f.write('1')
    else:
        print("分支名称输入错误，请重新输入！")

print('------------------------------欢迎使用自动部署工具------------------------------')
print('------------------------------请确认部署工具和1.txt是否存在于同一目录下-------------------------------')

try:
    with open('1.txt', 'r') as f:
        if f.read().strip() == '1':
            print('检测到您已经自动部署过第一次')
            print("请问是否需要重新部署？\n1. 重新部署\n2. 退出")
            choice = input("请输入选项：")
            if choice == "1":
                deploy()
            else:
                print("退出部署工具")
        else:
            print('检测到您没有自动部署过第一次')
            deploy_first()
except FileNotFoundError:
    print('检测到您没有自动部署过第一次')
    deploy_first()
