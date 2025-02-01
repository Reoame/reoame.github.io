import os
import subprocess

def deploy():
    try:
        # 检查是否有新的更改
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        if not status.stdout.strip():
            print("工作目录已经干净，没有新的更改需要提交。")
            return

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "update"], check=True)
        subprocess.run(["git", "push", "origin", "master"], check=True)
        print("部署成功！")
    except subprocess.CalledProcessError as e:
        print(f"发生异常: {e}")
        print(f"命令 {' '.join(e.cmd)} 返回非零退出状态 {e.returncode}")
        print(f"详细错误信息: {e.output if e.output else '无详细输出'}")
    except Exception as e:
        print(f"发生异常: {e}")

def deploy_first():
    try:
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
            print("第一次部署成功！")
        else:
            print("分支名称输入错误，请重新输入！")
    except subprocess.CalledProcessError as e:
        print(f"发生异常: {e}")
        print(f"命令 {' '.join(e.cmd)} 返回非零退出状态 {e.returncode}")
        print(f"详细错误信息: {e.output if e.output else '无详细输出'}")
    except Exception as e:
        print(f"发生异常: {e}")

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
