{
    "PACKAGE"       :   "",
    "CLASS"         :   "UserGroup",
    "EXTENDS"       :   "",
    "IMPLEMENTS"    :   [],
    "ANNOTATIONS"   :{
            "BEAN"  :{
                "java"  :   [
                    "@Entity()",
                    '''@Table(
                              )''']
            }
        },
    "IMPORTS"       :   {
            "BEAN" :{
                "java"  : [
                    "jakarta.persistence.*",
                      "org.hibernate.annotations.CreationTimestamp"
                        ],
                "*"     : [
                    "bean.User",
                    "bean.Authority",
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
            "NAME"      :   "rowCreatedDateTime",
            "TYPE"      :   "java.sql.Timestamp",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@CreationTimestamp()"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "users",
            "TYPE"      :   "java.util.List<User>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToMany(mappedBy="userGroup")']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "authority",
            "TYPE"      :   "Authority",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@ManyToOne()']
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
