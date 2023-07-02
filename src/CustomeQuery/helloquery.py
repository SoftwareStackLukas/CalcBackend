from graphene import ObjectType, Argument, String, Int, Schema

class HelloQuery(ObjectType):
    hello = String(name = Argument(String, default_value = "World"))
    amazing = String()
    
    # resolve function
    def resolve_hello(self, info, name):
        print("Which name is set: " + name)
        return 'Hello ' + name
    def resolve_amazing(self, info):
        return "This world is amazing"
    
helloSchema = Schema(query = HelloQuery)
