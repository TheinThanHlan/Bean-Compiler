{
    "PACKAGE"       :   "",
    "CLASS"         :   "AccountTransaction",
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
                    "bean.Account",
                    "bean.Voucher",
                    "bean.EmployeeSalary",
                    "bean.StockOrder"
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
            "NAME"      :   "direction",
            "TYPE"      :   "int",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@Column(unique=false,nullable=false)']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "description",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@Column()']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "reciever",
            "TYPE"      :   "User",
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

        {
            "NAME"      :   "payer",
            "TYPE"      :   "User",
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
        {
            "NAME"      :   "account",
            "TYPE"      :   "Account",
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

        {
            "NAME"      :   "voucher",
            "TYPE"      :   "Voucher",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToOne()']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "employeeSalary",
            "TYPE"      :   "EmployeeSalary",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToOne()']
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },

        {
            "NAME"      :   "stockOrder",
            "TYPE"      :   "StockOrder",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@OneToOne()']
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
