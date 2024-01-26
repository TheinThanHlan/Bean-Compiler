{
    "PACKAGE"       :   "something",
    "CLASS"         :   "Example",
    "EXTENDS"       :   "john",
    "IMPLEMENTS"    :   [],
    "ANNOTATIONS"   :{
        "java"  :   "@SOMETHING()"
        },
    "IMPORTS"       :   [],
    
    "VARIABLES"     :[
        {
            "NAME"      :   "id",
            "TYPE"      :   "int",
            "IS_ARR"    :   True,
            "ANNOTATIONS"   :{
                "java"  :   ["@Something()"]
            },
            "DEFAULT"   :   {
                "java"  :   "new int[]"
            }
         },

        {
            "NAME"      :   "phone",
            "TYPE"      :   "String",
            "IS_ARR"    :   False,
            "ANNOTATIONS"   :{
                "java"  :   ["@Something()"]
            },
            "DEFAULT"   :   {
                "java"  :   "null"
            }
         }

    ]
}
