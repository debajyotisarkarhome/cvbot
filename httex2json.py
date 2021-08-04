import re

ERROR_CODES='''0x001 : No Name
0x002 : No Email'''

def httex2json(data):
    response={"basic_details":{},"experience":{},"education":{},"projects":{},"link":{},"error":[]}
    name_start_index=data.find("<name>")
    if name_start_index!=-1:
        name=data[name_start_index+6:data.find("</name>")]
        name=name.replace("{","")
        response["basic_details"]["name"]=name.replace("}","")
    else:
        response["errors"].append("0x002")

    email_start_index=data.find("<email>")
    if email_start_index!=-1:
        email=data[email_start_index+7:data.find("</email>")]
        email=email.replace("{","")
        response["basic_details"]["email"]=email.replace("}","")
    else:
        response["errors"].append("0x002")

    for exp in re.findall("<exp>(.*?)</exp>",data):
        exp_undecoded=re.findall("{(.*?)}",exp)
        response["experience"][exp_undecoded[0]]=exp_undecoded[1]

    for edu in re.findall("<edu>(.*?)</edu>",data):
        edu_undecoded=re.findall("{(.*?)}",edu)
        response["education"][edu_undecoded[0]]=edu_undecoded[1]

    for pro in re.findall("<pro>(.*?)</pro>",data):
        pro_undecoded=re.findall("{(.*?)}",pro)
        response["projects"][pro_undecoded[0]]=pro_undecoded[1]

    for link in re.findall("<link>(.*?)</link>",data):
        link_undecoded=re.findall("{(.*?)}",link)
        response["link"][link_undecoded[0]]=link_undecoded[1]

    return response