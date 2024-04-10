#User
#	name,email,phone,address,marsta,gender,userName,password,userType
{
    "PACKAGE"       :   "",
    "CLASS"         :   "User",
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
                    "bean.Marsta",
                    "bean.Gender",
                    "bean.Restaurant",
                    "bean.AccountTransaction",
                    "bean.UserGroup"
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
                        "java"  :   ["@Column(nullable=false)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "email",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@Column(unique=true)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "phone",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@Column(unique=true)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "address",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@Column()"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "userName",
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
            "NAME"      :   "password",
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
            "NAME"      :   "loginableStatus",
            "TYPE"      :   "boolean",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   []
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
                    "*" : "false"
                }
            }
         },

        {
            "NAME"      :   "marsta",
            "TYPE"      :   "Marsta",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@ManyToOne()"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
                }
            }
         },

        
        {
            "NAME"      :   "gender",
            "TYPE"      :   "Gender",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                "BEAN"  :{ "java"  :   ["@ManyToOne()"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        








        {
            "NAME"      :   "restaurant",
            "TYPE"      :   "java.util.List<Restaurant>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@ManyToMany(fetch=FetchType.LAZY)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
                }
            }
         },
        





        {
            "NAME"      :   "userGroup",
            "TYPE"      :   "UserGroup",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@ManyToOne(fetch=FetchType.EAGER)"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
                }
            }
         },
        

        {
            "NAME"      :   "recievedAccountTransactions",
            "TYPE"      :   "java.util.List<AccountTransaction>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@OneToMany(mappedBy=\"reciever\")"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
                }
            }
         },
        
        {
            "NAME"      :   "paidAccountTransactions",
            "TYPE"      :   "java.util.List<AccountTransaction>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@OneToMany(mappedBy=\"payer\")"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {
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
