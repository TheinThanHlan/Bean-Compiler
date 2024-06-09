#User
#	name,email,phone,address,marsta,gender,userName,password,userType
{
    "PACKAGE"       :   "",
    "CLASS"         :   "Category",
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
                    "bean.MenuTemplate",
                    "bean.UserGroup",
                    "bean.Type"
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
                        "java"  :   ["@Column(nullable=false)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "type",
            "TYPE"      :   "Type",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@ManyToOne(fetch=FetchType.EAGER)","@Column(unique=false,nullable=false)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "subCategories",
            "TYPE"      :   "java.util.LinkedList<Category>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToMany(fetch=FetchType.EAGER,mappedBy="category")']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "category",
            "TYPE"      :   "Category",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@ManyToOne(fetch=FetchType.LAZY)"]
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
