from . import config
import Saver
import pretty
import utils
import globalConfig
def generate(tokens):
    output=""
    output+=generate_service(tokens)
    #output=pretty.prettify(output,config.postfix)
    dir="/service"
    name=tokens.get("CLASS")+".service"
    Saver.save(dir,name,config.postfix,output)


SERVICE_CLASS_TEMPLATE="""
import {{ HttpClient ,HttpHeaders}} from '@angular/common/http';
import {{ Injectable }} from '@angular/core';
import {{ AppConfigService }} from '@service/app-config.service';
import {{ Observable }} from 'rxjs';

import {{ {CLASS_NAME} }} from '@bean/{CLASS_NAME}';

@Injectable({{
  providedIn: 'root'
}})
export class {CLASS_NAME}Service {{

  constructor(private http:HttpClient) {{
  }}

  read{CLASS_NAME}FromId(id:number):Observable<{CLASS_NAME}>{{
    return this.http.post<{CLASS_NAME}>(AppConfigService.BASE_URL+"read{CLASS_NAME}FromId",id);
  }}
  read{CLASS_NAME}(obj:{CLASS_NAME}):Observable<{CLASS_NAME}>{{
    return this.http.post<{CLASS_NAME}>(AppConfigService.BASE_URL+"read{CLASS_NAME}",obj);
  }}
  create{CLASS_NAME}(obj:{CLASS_NAME}){{
    return this.http.post<{CLASS_NAME}>(AppConfigService.BASE_URL+"create{CLASS_NAME}",obj)
  }}
  update{CLASS_NAME}(obj:{CLASS_NAME}){{
    return this.http.post<{CLASS_NAME}>(AppConfigService.BASE_URL+"update{CLASS_NAME}",obj)
  }}
  delete{CLASS_NAME}(id:number){{
    return this.http.post<boolean>(AppConfigService.BASE_URL+"delete{CLASS_NAME}",id);
  }}
}}



"""



def generate_service(tokens):
    services=""
    services+=SERVICE_CLASS_TEMPLATE.format(CLASS_NAME=tokens.get("CLASS"))
    return services
