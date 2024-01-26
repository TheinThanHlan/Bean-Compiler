import os

def save(dir,name,postfix,source_code):
    dir="output/"+postfix+"/"+dir
    if not os.path.exists(dir): 
        os.makedirs(dir)
    with open(dir+"/"+name+"."+postfix,"w+") as f:
        f.write(source_code)
