from pylatex import Document, Section, Subsection, MiniPage, LargeText, LineBreak, MediumText, HugeText, Command
from pylatex.utils import italic, NoEscape, bold, escape_latex
import uuid

TEMPLATE1_FORMAT=    '''inp={"basic_details":{"name":"<name>","email":"<email>"},
            "experience":   {"exp1":"details","exp2":"details"},
            "education" :   {"ed1":"details","ed1":"details"},
            "projects"  :   {"pro1":"details","pro2":"details"},
            "link"      :   {"Facebook": "www.faacebook.com"}
            }'''

def template1(inp):
    geometry_options = {"margin": "0.7in"}
    doc=Document(geometry_options=geometry_options)

    doc.preamble.append(NoEscape("\\usepackage{indentfirst}"))
    doc.packages.append(NoEscape("\\usepackage{hyperref}"))

    def hyperlink(url,text):
        text = escape_latex(text)
        if url[0:3]!="www.":
            url="www."+url
        return NoEscape(r'\href{' + url + '}{' + text + '}')

    with doc.create(MiniPage(align='r')):
        doc.append(HugeText(bold(inp["basic_details"]["name"])))
        doc.append(LineBreak())
        doc.append(MediumText(bold(inp["basic_details"]["email"])))
    if not inp["experience"]=={}:
        with doc.create(Section("EXPERIENCE: ")):
            for i in inp["experience"].keys():
                with doc.create(Subsection(i)):
                    doc.append(inp["experience"][i])
    if not inp["education"]=={}:
        with doc.create(Section("EDUCATION: ")):
            for i in inp["education"].keys():
                with doc.create(Subsection(i)):
                    doc.append(inp["education"][i])
    if not inp["projects"]=={}:
        with doc.create(Section("PROJECTS: ")):
            for i in inp["projects"].keys():
                with doc.create(Subsection(i)):
                    doc.append(inp["projects"][i])
    if not inp["link"]=={}:
        with doc.create(Section("LINKS: ")):
            for i in inp["link"].keys():
                doc.append(MediumText(hyperlink(inp["link"][i],i)))
    

    filename=str(uuid.uuid1())
    doc.generate_pdf("payloads/"+filename)
    return "payloads/"+filename+".pdf"

'''testdata={"basic_details":{"name":"<name>","email":"<email>"},
            "experience":   {"exp1":"details","exp2":"details"},
            "education" :   {"ed1":"details","ed1":"details"},
            "projects"  :   {"pro1":"details","pro2":"details"},
            }

template1(testdata)'''