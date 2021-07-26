from pylatex import Document, Section, Subsection, MiniPage, LargeText, LineBreak, MediumText, HugeText
from pylatex.utils import italic, NoEscape, bold
import uuid

TEMPLATE1_FORMAT=    '''inp={"basic_details":{"name":"<name>","email":"<email>"},
            "expirience":   {"exp1":"details","exp2":"details"},
            "education" :   {"ed1":"details","ed1":"details"},
            "projects"  :   {"pro1":"details","pro2":"details"},
            }'''

def template1(inp):
    geometry_options = {"margin": "0.7in"}
    doc=Document(geometry_options=geometry_options)

    with doc.create(MiniPage(align='c')):
        doc.append(HugeText(bold(inp["basic_details"]["name"])))
        doc.append(LineBreak())
        doc.append(MediumText(bold(inp["basic_details"]["email"])))

    with doc.create(Section("EXPERIENCE: ")):
        for i in inp["expirience"].keys():
            with doc.create(Subsection(i)):
                doc.append(inp["expirience"][i])

    with doc.create(Section("EDUCATION: ")):
        for i in inp["education"].keys():
            with doc.create(Subsection(i)):
                doc.append(inp["education"][i])

    with doc.create(Section("PROJECTS: ")):
        for i in inp["projects"].keys():
            with doc.create(Subsection(i)):
                doc.append(inp["projects"][i])

    filename=str(uuid.uuid1())
    doc.generate_pdf("payloads/"+filename)
    return "payloads/"+filename+".pdf"

""" testdata={"basic_details":{"name":"<name>","email":"<email>"},
            "expirience":   {"exp1":"details","exp2":"details"},
            "education" :   {"ed1":"details","ed1":"details"},
            "projects"  :   {"pro1":"details","pro2":"details"},
            }

template1(testdata) """