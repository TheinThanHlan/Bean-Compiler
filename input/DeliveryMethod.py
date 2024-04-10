{
    "PACKAGE"       :   "",
    "CLASS"         :   "DeliveryMethod",
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
                    "bean.Restaurant",
                    "bean.Delivery"
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
            "NAME"      :   "user",
            "TYPE"      :   "User",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ["@OneToOne()"]
                    }
                },
            "DEFAULT"   :   {
                "BEAN"  : {}
            }
         },
        {
            "NAME"      :   "deliveries",
            "TYPE"      :   "java.util.List<Delivery>",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                    "BEAN"  :{
                        "java"  :   ['@ManyToMany(mappedBy="deliveryMethods")']
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
