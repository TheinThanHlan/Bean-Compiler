from . import config
import Saver
def generate(tokens):
    output=""
    #output+=generate_imports(tokens)
    output+=generate_class(tokens)
    dir="/bean"
    name=tokens.get("CLASS")
    Saver.save(dir,name,config.postfix,output)


"""
def generate_imports(tokens):
    IMPORT_FORMAT="import {IMPORT};"
    output=""
    for a in tokens.get("IMPORTS"):
        output+=IMPORT_FORMAT.format(IMPORT=a)
    return output
"""
def generate_class(tokens):
    CLASS_FORMAT="{ANNOTATIONS}class {CLASS}{{{CLASS_BODY}}}"
    ANNOTATIONS="".join(tokens.get("ANNOTATIONS",{}).get(config.postfix,[]))
    CLASS_BODY          =""
    CLASS_BODY          +=generate_variables(tokens)   
    CLASS_BODY          +=generate_getters_and_setters(tokens)
    output              =CLASS_FORMAT.format(ANNOTATIONS=ANNOTATIONS,CLASS=tokens.get("CLASS"),CLASS_BODY=CLASS_BODY)
    return output;
   


def generate_variables(tokens):
    VARIABLE_FORMAT="{ANNOTATIONS}private {NAME}!:{TYPE} {IS_ARR}{DEFAULT};"
    output=""
    for a in tokens.get("VARIABLES"):
        ANNOTATIONS="".join(a.get("ANNOTATIONS",{}).get(config.postfix,[]))
        
        NAME=a.get("NAME");
        
        TYPE=a.get("TYPE");
        TYPE=config.Keyword.get(TYPE,TYPE)

        IS_ARR="[]" if a.get("IS_ARR") else ""
        
        DEFAULT=a.get("DEFAULT",{}).get(config.postfix,"")
        DEFAULT="="+DEFAULT if DEFAULT!="" else ""
        
        output+=VARIABLE_FORMAT.format(ANNOTATIONS=ANNOTATIONS,NAME=NAME,TYPE=TYPE,IS_ARR=IS_ARR,DEFAULT=DEFAULT)
    return output

def generate_getters_and_setters(tokens):
    GETTER_FORMAT="public  get{FUNC_NAME}():{TYPE}{IS_ARR}{{return this.{NAME};}}"
    SETTER_FORMAT="public set{FUNC_NAME}( {NAME}:{TYPE}{IS_ARR}):void{{this.{NAME}={NAME};}}"
    output=""
    for a in tokens.get("VARIABLES"):
        NAME=a.get("NAME");
        FUNC_NAME=NAME[0].upper()+NAME[1:];

        TYPE=a.get("TYPE");
        TYPE=config.Keyword.get(TYPE,TYPE)
        
        IS_ARR="[]" if a.get("IS_ARR") else ""
        
        output+=GETTER_FORMAT.format(TYPE=TYPE,IS_ARR=IS_ARR,FUNC_NAME=FUNC_NAME,NAME=NAME)
        output+=SETTER_FORMAT.format(TYPE=TYPE,IS_ARR=IS_ARR,FUNC_NAME=FUNC_NAME,NAME=NAME)
    return output
