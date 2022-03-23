# type hints and annotations.
from vandal.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
)

# makes multiple instances of the object available.
class Meta(type):

    def __call__(
        self, 
        *args, 
        **kwargs,
        ) -> ReturnType:
        instance = super(Meta, self).__call__(*args, **kwargs)

        return instance

    def __init__(
        self, 
        name, 
        base, 
        attr,
        ) -> ReturnType:
        super(Meta, self).__init__(name, base, attr)
