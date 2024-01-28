from . import config
import Saver
import pretty
import utils
import globalConfig
def generate(tokens):
    output=""
    output+=generate_package(tokens)
    output+=generate_imports(tokens)
    output+=generate_class(tokens)
    output=pretty.prettify(output,config.postfix)
    dir="/bean"
    name=tokens.get("CLASS")
    Saver.save(dir,name,config.postfix,output)


def generate_package(tokens):
    output="package bean;"
    return output

def generate_imports(tokens):
    IMPORT_FORMAT="import {IMPORT};"
    output="import com.google.gson.Gson;"
    for a in tokens.get("IMPORTS",{}).get("BEAN",{}).get(config.postfix,[]):
        output+=IMPORT_FORMAT.format(IMPORT=a)
    for a in tokens.get("IMPORTS",{}).get("BEAN",{}).get(globalConfig.all,[]):
        output+=IMPORT_FORMAT.format(IMPORT=a)
    return output

def generate_class(tokens):
    CLASS_FORMAT="{ANNOTATIONS}public class {CLASS} {IS_THERE_EXTENDS} {EXTENDS} implements java.io.Serializable {IMPLEMENTS} {{{CLASS_BODY}}}"
    ANNOTATIONS="".join(tokens.get("ANNOTATIONS",{}).get("BEAN",{}).get(config.postfix,[]))
    
    EXTENDS               = tokens.get("EXTENDS")
    IS_THERE_EXTENDS = "extends" if EXTENDS!="" else "";
    
    IMPLEMENTS             = "" 
    for a in tokens.get("IMPLEMENTS"):
        IMPLEMENTS += ","+a

    CLASS_BODY          =""
    CLASS_BODY          +=generate_variables(tokens)   
    CLASS_BODY          +=generate_getters_and_setters(tokens)
    CLASS_BODY          +=generate_toJson(tokens)
    CLASS_BODY          +=generate_equals(tokens)
    CLASS_BODY          +=generate_clone(tokens)
    output              =CLASS_FORMAT.format(ANNOTATIONS=ANNOTATIONS,CLASS=tokens.get("CLASS"),CLASS_BODY=CLASS_BODY , IMPLEMENTS =IMPLEMENTS , EXTENDS=EXTENDS , IS_THERE_EXTENDS=IS_THERE_EXTENDS)
    return output;
   


def generate_variables(tokens):
    VARIABLE_FORMAT="{ANNOTATIONS}private {TYPE} {NAME}{IS_ARR}{DEFAULT};"
    output=""
    for a in tokens.get("VARIABLES"):
        ANNOTATIONS="".join(a.get("ANNOTATIONS",{}).get("BEAN",{}).get(config.postfix,[]))
        
        NAME=a.get("NAME");
        
        TYPE=a.get("TYPE");
        
        IS_ARR="[]" if a.get("IS_ARR") else ""
        
        DEFAULT=a.get("DEFAULT",{}).get("BEAN",{}).get(config.postfix,"")
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



def generate_toJson(tokens):
    TOJSON_FORMAT="public String toJson(){{return new Gson.toJson(this);}}"
    return TOJSON_FORMAT.format();
    

def generate_equals(tokens):
    EQUALS_FORMAT="@Override()public boolean equals(Object obj){{{COMPARISONS}return true;}}"
    COMPARISONS_PRIMITIVE_FORMAT = "if(this.get{COMPARE_VAR}()!=obj1.get{COMPARE_VAR}()){{return false;}}"
    COMPARISONS_FORMAT = "if(!this.get{COMPARE_VAR}().equals(obj1.get{COMPARE_VAR}())){{return false;}}"
    COMPARISONS=f"if (obj == null) {{return false; }} if (obj.getClass() != this.getClass()){{return false;}}final {tokens.get('CLASS')} obj1 = ({tokens.get('CLASS')}) Obj;"
    output=""
    for a in tokens.get("VARIABLES"):
        if a.get("TYPE") in config.primitive_types:
            COMPARISONS+=COMPARISONS_PRIMITIVE_FORMAT.format(COMPARE_VAR=utils.makeFuncCase(a.get("NAME")))
        else:
            COMPARISONS+=COMPARISONS_FORMAT.format(COMPARE_VAR=utils.makeFuncCase(a.get("NAME")))

    output+=EQUALS_FORMAT.format(COMPARISONS=COMPARISONS)
    return output



def generate_clone(tokens):
    CLONE_FORMAT="@Override()public {CLASS} clone(){{{CLASS} obj=({CLASS})super.clone();return obj;}}"
    output=""
    output=CLONE_FORMAT.format(CLASS=tokens.get("CLASS"))
    return output;


