import yaml
from clases.push import PushRootLeft
from ruamel.yaml import YAML  
import ruamel.yaml 
import yaml 
import os



with open('home_dir/nginx/templates/deployment.yaml', 'r+' ) as file:
    docs = file.readlines()
    # data = (yaml.load(docs, Loader=yaml.FullLoader))
    docs[3] = ("refael")
    print (docs)
    data = yaml.load_all(docs)
    with open('home_dir/nginx/templates/deployment.yaml', 'w+' ) as files:
        yaml.dump(data)






# with open(file_name) as f:
#         doc = yaml.safe_load(f)
#     doc['state'] = state
#     with open(file_name, 'w') as f:# file = 
# open("nginx.env","r+")
#         yaml.safe_dump(doc, f, x y# for lines in 
# open("nginx.env"):
# #     line = lines.split(':')[0] 
# #     test=('{}: {{.Values.env.{}}}'.format(line,line))
# #     with open('home_dir/nginx/templates/deployment.yaml', 'a' ) as file:
#         docs = yaml.load(test,  transform=PushRootLeft(12))
#         yaml.dump(docs, file)
        



# with open('home_dir/nginx/templates/deployment.yaml', 'a' ) as file:
#     docs = yaml.load(deploymentName)
#     yaml.dump(docs, file)
