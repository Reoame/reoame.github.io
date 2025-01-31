import os

def deploy():
    os.system("git add .")
    os.system("git commit -m 'update'")
    os.system("git push origin master")

if __name__ == '__main__':
    deploy()