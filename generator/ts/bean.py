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
    return "";

def generate_imports(tokens):
    IMPORT_FORMAT="import {CLASS} from \"{IMPORT}\";"
    output=""
#   specific import
#    for a in tokens.get("IMPORTS",{}).get("BEAN",{}).get(config.postfix,[]):
#        output+=a

    for a in tokens.get("IMPORTS",{}).get("BEAN",{}).get(globalConfig.all,[]):
        IMPORT=globalConfig.replacements.get("@")+a.replace(".","/")
        CLASS=a.split(".")[-1]
        output+=IMPORT_FORMAT.format(IMPORT=IMPORT,CLASS=CLASS)
    return output

def generate_class(tokens):
    CLASS_FORMAT="{ANNOTATIONS}export class {CLASS} {IS_THERE_EXTENDS} {EXTENDS} {IS_THERE_IMPLEMENTS} {IMPLEMENTS} {{{CLASS_BODY}}}"
    ANNOTATIONS="".join(tokens.get("ANNOTATIONS",{}).get("BEAN",{}).get(config.postfix,[]))
    
    EXTENDS               = tokens.get("EXTENDS")
    IS_THERE_EXTENDS = "extends" if EXTENDS!="" else "";
    
    IMPLEMENTS             = "" 
    for a in tokens.get("IMPLEMENTS"):
        IMPLEMENTS += ","+a
    IS_THERE_IMPLEMENTS = "implements" if IMPLEMENTS!="" else "";
    CLASS_BODY          =""
    CLASS_BODY          +=generate_variables(tokens)   
    CLASS_BODY          +=generate_getters_and_setters(tokens)
    CLASS_BODY          +=generate_toJson(tokens)
    CLASS_BODY          +=generate_fromJson(tokens)
    CLASS_BODY          +=generate_equals(tokens)
    CLASS_BODY          +=generate_clone(tokens)
    output              =CLASS_FORMAT.format(ANNOTATIONS=ANNOTATIONS,CLASS=tokens.get("CLASS"),CLASS_BODY=CLASS_BODY , IMPLEMENTS =IMPLEMENTS , EXTENDS=EXTENDS , IS_THERE_EXTENDS=IS_THERE_EXTENDS,IS_THERE_IMPLEMENTS=IMPLEMENTS)
    return output;
   


def generate_variables(tokens):
    VARIABLE_FORMAT="{ANNOTATIONS}private  {NAME}{HAVE_DEFAULT}:{TYPE}{IS_ARR}{DEFAULT};"
    output=""
    for a in tokens.get("VARIABLES"):
        ANNOTATIONS="".join(a.get("ANNOTATIONS",{}).get("BEAN",{}).get(config.postfix,[]))
        
        NAME=a.get("NAME");
        
        TYPE=a.get("TYPE");
        TYPE=config.TRANS.get(TYPE,TYPE)
        IS_ARR="[]" if a.get("IS_ARR") else ""
        
        DEFAULT=a.get("DEFAULT",{}).get("BEAN",{}).get(globalConfig.all,"")
        DEFAULT=a.get("DEFAULT",{}).get("BEAN",{}).get(config.postfix,DEFAULT)

        DEFAULT="="+DEFAULT if DEFAULT!="" else ""
        HAVE_DEFAULT="" if DEFAULT!="" else "!"
        output+=VARIABLE_FORMAT.format(ANNOTATIONS=ANNOTATIONS,NAME=NAME,TYPE=TYPE,IS_ARR=IS_ARR,DEFAULT=DEFAULT,HAVE_DEFAULT=HAVE_DEFAULT)
    return output

def generate_getters_and_setters(tokens):
    GETTER_FORMAT="public  get{FUNC_NAME}():{TYPE}{IS_ARR}{{return this.{NAME};}}"
    SETTER_FORMAT="public set{FUNC_NAME}({NAME}:{TYPE}{IS_ARR}):void {{this.{NAME}={NAME};}}"
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
    TOJSON_FORMAT="public toJson():string{{return JSON.stringify(this);}}"
    return TOJSON_FORMAT.format();
    

def generate_fromJson(tokens):
    FROMJSON_FORMAT="public static fromJson(json_obj:object):{CLASS}{{return Object.assign(new {CLASS}(), json_obj)}}"
    output=""
    output+=FROMJSON_FORMAT.format(CLASS=tokens.get("CLASS"));
    return output


def generate_equals(tokens):
    COMPARISONS_PRIMITIVE_FORMAT = "if(this.get{COMPARE_VAR}()!=obj1.get{COMPARE_VAR}()){{return false;}}"
    COMPARISONS_FORMAT = "if(!this.get{COMPARE_VAR}().equals(obj1.get{COMPARE_VAR}())){{return false;}}"
    COMPARISONS=f"if (obj == null) {{return false; }}final {tokens.get('CLASS')} obj1 = ({tokens.get('CLASS')}) Obj;"
    output=""
    for a in tokens.get("VARIABLES"):
        COMPARISONS+=COMPARISONS_PRIMITIVE_FORMAT.format(COMPARE_VAR=utils.makeFuncCase(a.get("NAME")))

    output+=EQUALS_FORMAT.format(COMPARISONS=COMPARISONS)
    return output



def generate_clone(tokens):
    CLONE_FORMAT="@Override()public {CLASS} clone(){{{CLASS} obj=({CLASS})super.clone();return obj;}}"
    output=""
    output=CLONE_FORMAT.format(CLASS=tokens.get("CLASS"))
    return output;


