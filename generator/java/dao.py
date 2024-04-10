from . import config
import Saver
import pretty
import utils
import globalConfig




CRUD_FUNCTIONS="""
    public void create({CLASS_NAME} data){{
        Session s=this.sf.openSession();
        try{{
            Transaction tx=s.beginTransaction();
            s.save(data);
            tx.commit();

        }}finally{{
            s.close();
        }}
    }}
    
    public {CLASS_NAME} readFromId(long id){{
        Session s=this.sf.openSession();
        {CLASS_NAME} tmp=null;
        try{{
            Transaction tx=s.beginTransaction();
            tmp=s.<{CLASS_NAME}>get({CLASS_NAME}.class,id);
            tx.commit();
        }}finally{{
            s.close();
        }}
        return tmp;

    }}
 
 public {CLASS_NAME} read({CLASS_NAME} obj){{
        Session s=this.sf.openSession();
        {CLASS_NAME} tmp=null;
        try{{
            Transaction tx=s.beginTransaction();
            tmp=s.<{CLASS_NAME}>get({CLASS_NAME}.class,obj.getId());
            tx.commit();
        }}finally{{
            s.close();
        }}
        return tmp;

    }}

    public void update({CLASS_NAME} data) {{
	    Session s=this.sf.openSession();
        try{{
            Transaction t=s.beginTransaction();
            s.persist(data);
            t.commit();

        }}finally{{
            s.close();
        }}
    }}

	public void delete({CLASS_NAME} data) {{
	    Session s=this.sf.openSession();
        try{{
            Transaction t=s.beginTransaction();
            s.remove(data);
            t.commit();
        
            
        }}finally{{
            s.close();
        }}
    }}

"""





DAO_CLASS="""

package dao;
import bean.{CLASS_NAME};

import org.springframework.stereotype.Component;

import org.hibernate.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;

import org.springframework.context.annotation.PropertySource;

//@PropertySource("classpath:sql/{CLASS_NAME}.properties")
@Component()
public class {CLASS_NAME}Dao{{
    @Autowired()
    SessionFactory sf;


    {CRUD_FUNCTIONS}

}}

"""
# use to create the list of getter of given 
#def call_getter_as_args(instance_var_name,var_list):
#    get_args=""
#    for a in var_list:
#        get_args += instance_var_name+".get"+a[0].capitalize()+"(),"
#    return get_args[0:-1];
#1:33 / 2:56


def generate_crud(tokens):
    functions=""
    variables=""
    #check is the variable premitive        instance var name  ,   list of variable 
    #variables=call_getter_as_args("data",[a for a in bc["VARIABLES"] if  and not a[2] and not a[3]] )
    functions += CRUD_FUNCTIONS.format(CLASS_NAME=tokens["CLASS"],VAR_ARGS=variables)

    return functions







def generate(tokens):
    crud_functions=""
    output=""

    #create the crud functions
    crud_functions=generate_crud(tokens)

    #generate source code
    output=DAO_CLASS.format(
        CLASS_NAME=tokens["CLASS"],
        CRUD_FUNCTIONS=crud_functions
            )

    dir="/dao"
    name=tokens.get("CLASS")+"Dao"
    Saver.save(dir,name,config.postfix,output)





