import globalConfig

def prettify(code,type):
    match type:
        case "java" | "ts":
            return java(code)
        


def java(code):
    result=""
    no_of_indent=0
    #code = code . split (" ")
    #code = [a for a in code if a != ""]
    #code = " ".join(code)
    #code = code . split ("\n")
    #code = [a for a in code if a != ""]
    #code = " ".join(code)
    #code = code . split ("\t")
    #code = [a for a in code if a != ""]
    #code = " ".join(code)
    
    code = code . split ("\n")
    code = [a.strip() for a in code if a != ""]
    code = "".join(code)
    annotation_start = "@"
    bracket_start=['(','{','[']
    bracket_end=[')','}',']']
    bracket_count=0
    is_pass = False
    b_start=False
    for a in code:
        if is_pass==True:
            if a in bracket_start :
                b_start=True
                bracket_count+=1

            elif a in bracket_end :
                bracket_count-=1
    
            if bracket_count == 0 and b_start==True:
                result+=a+"\n"+"\t"*no_of_indent
                is_pass=False
                b_start=False
            else:
                result+=a

        elif a == annotation_start and is_pass==False:
            is_pass=True
            result+="\n"+("\t"*no_of_indent)+a

        elif is_pass:
            result +=a

        elif a == "{":
            no_of_indent+=1
            result += a+"\n"+("\t"*no_of_indent)

        elif a== "}":
            no_of_indent-=1
            result += "\n"+("\t"*no_of_indent)+a+"\n"+("\t"*no_of_indent)

        elif a== ";":
            result += a+"\n"+("\t"*no_of_indent)

        else:
            result +=a
    for a in globalConfig.replacements:
        result=result.replace(globalConfig.replacements.get(a),a)
    return result
        



        


