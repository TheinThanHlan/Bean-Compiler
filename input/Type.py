#User
#	name,email,phone,address,marsta,gender,userName,password,userType
{
    "PACKAGE"       :   "",
    "CLASS"         :   "Type",
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
                      "org.hibernate.annotations.CreationTimestamp"
                        ],
                "*"     : [
                    "bean.Category",
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
                    "*"  : ""
                }
            }
         },
        {
            "NAME"      :   "name",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@Column(unique=true,nullable=false)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "categories",
            "TYPE"      :   "java.util.List<Category>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToMany(fetch=FetchType.LAZY,mappedBy="type")']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },


    ],
    "FUNCTIONS"     :{
        "BEAN"      :{
            "java"  :""
            }
    }
}
