from graphene import ObjectType, String, Int, NonNull

class Operator(ObjectType):
    id = NonNull(Int)
    operator = String()
    describtion = String()

operators = {
    Operator(id = 1, operator = "addition", describtion = "Adds to values together"),
    Operator(id = 2, operator = "substraction", describtion = "Substracts a value from another value"),
    Operator(id = 3, operator = "multiplication", describtion = "Multiplies two values"),
    Operator(id = 4, operator = "division", describtion = "Dives a value by a second given value")
}
    