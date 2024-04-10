{
    "PACKAGE"       :   "",
    "CLASS"         :   "Stock",
    "EXTENDS"       :   "",
    "IMPLEMENTS"    :   [],
    "ANNOTATIONS"   :{
            "BEAN"  :{
                "java"  :   [
                    "@Entity()",]
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
                    "bean.Restaurant",
                    "bean.StockSupplier"
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
            "NAME"      :   "stockSupplier",
            "TYPE"      :   "java.util.List<StockSupplier>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@ManyToMany(fetch=FetchType.LAZY,mappedBy=\"stock\")"]
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
