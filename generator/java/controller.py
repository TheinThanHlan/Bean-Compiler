from . import config
import Saver
import pretty
import utils
import globalConfig


controller="""
package controller;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.beans.factory.annotation.Autowired;
import dao.*;
import bean.*;
@RestController()
public class {CLASS_NAME}Controller{{
	@Autowired()
    {CLASS_NAME}Dao dao;

	@PostMapping("create{CLASS_NAME}")
	public String create(@RequestBody() {CLASS_NAME} data{CLASS_NAME}){{
	    dao.create(data{CLASS_NAME});
        return data{CLASS_NAME}.toJson();
	}}
    
	@PostMapping("read{CLASS_NAME}FromId")
	public String read{CLASS_NAME}FromId(@RequestBody() int id){{
        try{{
            return dao.readFromId(id).toJson();
        }}
        catch(NullPointerException e){{
            return null;
        }}
	}}
	
    @PostMapping("read{CLASS_NAME}")
	public String read(@RequestBody() {CLASS_NAME} data{CLASS_NAME} ){{
        try{{
	        return dao.read(data{CLASS_NAME}).toJson();
        }}
        catch(NullPointerException e){{
            return null;
        }}
	}}
    

    
	@PostMapping("update{CLASS_NAME}")
	public void update(@RequestBody() {CLASS_NAME} data{CLASS_NAME}){{
        dao.update(data{CLASS_NAME});
	}}
    
	@DeleteMapping("delete{CLASS_NAME}")
	public String delete(@RequestBody() {CLASS_NAME} data){{
        dao.delete(data);
        return "haha";
	}}
    

}}
"""







def generate(tokens):
    output=""
    output+=controller.format(CLASS_NAME=tokens.get("CLASS"))
    output=pretty.prettify(output,config.postfix)
    dir="/controller"
    name=tokens.get("CLASS")+"Controller"
    Saver.save(dir,name,config.postfix,output)
    




