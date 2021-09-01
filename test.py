import yaml
from clases.push import PushRootLeft
from ruamel.yaml import YAML  
import ruamel.yaml 
import yaml



with open('home_dir/nginx/templates/deployment.yaml', 'r+' ) as file:
    docs = file.read().rsplit('\n')
    with open('home_dir/nginx/templates/deployment.yaml', 'a+' ) as file:
        docs[3] = (" refael ")
        file.write(str(docs[3]))




# file = open("nginx.env","r+")
# for lines in open("nginx.env"):
#     line = lines.split(':')[0] 
#     test=('{}: {{.Values.env.{}}}'.format(line,line))
#     with open('home_dir/nginx/templates/deployment.yaml', 'a' ) as file:
#         docs = yaml.load(test,  transform=PushRootLeft(12))
#         yaml.dump(docs, file)
        



# with open('home_dir/nginx/templates/deployment.yaml', 'a' ) as file:
#     docs = yaml.load(deploymentName)
#     yaml.dump(docs, file)