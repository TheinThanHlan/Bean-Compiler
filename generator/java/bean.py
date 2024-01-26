from . import config
import Saver
def generate(tokens):
    output=""
    output+=generate_package(tokens)
    output+=generate_imports(tokens)
    output+=generate_class(tokens)
    dir="/bean"
    name=tokens.get("CLASS")
    Saver.save(dir,name,config.postfix,output)


def generate_package(tokens):
    output="package bean;"
    return output

def generate_imports(tokens):
    IMPORT_FORMAT="import {IMPORT};"
    output=""
    for a in tokens.get("IMPORTS"):
        output+=IMPORT_FORMAT.format(IMPORT=a)
    return output

def generate_class(tokens):
    CLASS_FORMAT="{ANNOTATIONS}public class {CLASS} {IS_THERE_EXTENDS} {EXTENDS} implements Serializzable {IMPLEMENTS} {{{CLASS_BODY}}}"
    ANNOTATIONS="".join(tokens.get("ANNOTATIONS",{}).get("java",[]))
    
    EXTENDS               = tokens.get("EXTENDS")
    IS_THERE_EXTENDS = "extends" if EXTENDS!="" else "";
    
    IMPLEMENTS             = "" 
    for a in tokens.get("IMPLEMENTS"):
        IMPLEMENTS += ","+a

    CLASS_BODY          =""
    CLASS_BODY          +=generate_variables(tokens)   
    CLASS_BODY          +=generate_getters_and_setters(tokens)
    output              =CLASS_FORMAT.format(ANNOTATIONS=ANNOTATIONS,CLASS=tokens.get("CLASS"),CLASS_BODY=CLASS_BODY , IMPLEMENTS =IMPLEMENTS , EXTENDS=EXTENDS , IS_THERE_EXTENDS=IS_THERE_EXTENDS)
    return output;
   


def generate_variables(tokens):
    VARIABLE_FORMAT="{ANNOTATIONS}private {TYPE} {NAME}{IS_ARR}{DEFAULT};"
    output=""
    for a in tokens.get("VARIABLES"):
        ANNOTATIONS="".join(a.get("ANNOTATIONS",{}).get("java",[]))
        
        NAME=a.get("NAME");
        
        TYPE=a.get("TYPE");
        
        IS_ARR="[]" if a.get("IS_ARR") else ""
        
        DEFAULT=a.get("DEFAULT",{}).get("java")
        DEFAULT="="+DEFAULT if DEFAULT!="" else ""
        
        output+=VARIABLE_FORMAT.format(ANNOTATIONS=ANNOTATIONS,NAME=NAME,TYPE=TYPE,IS_ARR=IS_ARR,DEFAULT=DEFAULT)
    return output

def generate_getters_and_setters(tokens):
    GETTER_FORMAT="public {TYPE}{IS_ARR} get{FUNC_NAME}(){{return this.{NAME};}}"
    SETTER_FORMAT="public void set{FUNC_NAME}({TYPE}{IS_ARR} {NAME}){{this.{NAME}={NAME};}}"
    output=""
    for a in tokens.get("VARIABLES"):
        NAME=a.get("NAME");
        FUNC_NAME=NAME[0].upper()+NAME[1:];

        TYPE=a.get("TYPE");
        
        IS_ARR="[]" if a.get("IS_ARR") else ""
        
        output+=GETTER_FORMAT.format(TYPE=TYPE,IS_ARR=IS_ARR,FUNC_NAME=FUNC_NAME,NAME=NAME)
        output+=SETTER_FORMAT.format(TYPE=TYPE,IS_ARR=IS_ARR,FUNC_NAME=FUNC_NAME,NAME=NAME)
    return output





