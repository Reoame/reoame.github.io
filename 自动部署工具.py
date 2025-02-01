
import os


def first_deploy():
    print('开始部署')
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "first commit"')
    url = input('请输入远程仓库地址：')
    os.system('git remote add origin'+ url)
    branch = os.system('git branch -r')
    print('你的远程仓库分支是：',branch)
    branch_name = input('请输入你要推送的分支名称：')
    os.system('git push -u origin'+ branch_name)
    print('部署完成')

def update():

    print('开始更新')
    os.system('git add .')
    os.system('git commit -m "update"')
    branch_name = input('请输入你要推送的分支名称：')
    os.system('git push -u origin'+ branch_name)
    print('更新完成')

if __name__ == '__main__':
    deploy_type = input('请输入部署类型：1.首次部署 2.更新：')
    if deploy_type == '1':
        first_deploy()
    elif deploy_type == '2':
        update()
    else:
        print('输入错误')