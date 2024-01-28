#Restaurant
#	name,email,address,phone,openTime,closeTime,manager
{
    "PACKAGE"       :   "",
    "CLASS"         :   "Eample",
    "EXTENDS"       :   "",
    "IMPLEMENTS"    :   [],
    "ANNOTATIONS"   :{
            "BEAN"  :{
                "java"  :   ["@Entity()","@Table()"]
            }
        },
    "IMPORTS"       :   {
            "BEAN" :{
                "java"  : [
                    "jakarta.persistence.*",
                        ],
                "*"     : [
                    "bean.Restaurant"
                ]
            }
        },
    
    "VARIABLES"     :[
        {
            "NAME"      :   "id",
            "TYPE"      :   "long",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@Id()","@GeneratedValue()"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
                    "*"  : "1"
                }
            }
         },
    ],
    "FUNCTIONS"     :{
        "BEAN"      :{
            "java"  :""
            }
    }
}
