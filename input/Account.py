{
    "PACKAGE"       :   "",
    "CLASS"         :   "Account",
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
                    "bean.AccountTransaction"
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
            "NAME"      :   "name",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@Column(unique=true,nullable=false)']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "number",
            "TYPE"      :   "int",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@Column(unique=true,nullable=false)']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "normal",
            "TYPE"      :   "int",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@Column(nullable=false)']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "transactions",
            "TYPE"      :   "java.util.LinkedList<AccountTransaction>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToMany(mappedBy="account")']
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
