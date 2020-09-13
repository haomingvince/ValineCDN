import os
remotepath = 'https://valinecdn.bili33.top/'
prefix= input("请输入前缀：")
def findAllFile(base):
    files = os.listdir(base)
    #files.sort(key = lambda x : int(x.split('.')[0][7:]))
    for file in files:
        if not os.path.isdir(base + file):
            f_name = str(file)
            yield f_name
    # for root, ds, fs in os.walk(base):
    #     for f in fs:
    #         yield f

def main():
    base = './Collections'
    linklist=[]
    num=1
    print('```json')
    print('{')
    for i in findAllFile(base):
        print('\"{}{}\": \"{}/{}\",'.format("",i,"Collections",i))
        num=num+1
    print('}')
    print('```')
    num=1
    for i in findAllFile(base):
        #print('![{}{}]({}{}/{})'.format(prefix,num,remotepath,prefix,i))
        num=num+1
if __name__ == '__main__':
    main()