postfix = "ts"
primitive_types = ["byte", "short", "int", "long", "float", "double", "char", "boolean"]


def variableTypeParser(var):
    output = ""
    if ("<" not in var) and (">" not in var):
        output = TRANS.get(var, var)
    else:
        b = ""
        for a in var:
            if a == "<":
                output += TRANS.get(b, b) + "<"
                b = ""
            elif a == ">":
                output += TRANS.get(b, b) + ">"
                b = ""

            elif a == ",":
                output += TRANS.get(b, b) + ","
                b = ""

            else:
                b += a
    return output


TRANS = {
    "byte": "number",
    "short": "number",
    "int": "number",
    "long": "number",
    "float": "number",
    "double": "number",
    "char": "string",
    "String": "string",
    "boolean": "boolean",
    "java.sql.Timestamp": "Date",
    "java.util.List": "Array",
    "java.util.LinkedList": "Array",
}
