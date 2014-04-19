def enum(**enums):
    return type('Enum', (), enums)

tag = enum(pos=1,neg=2,neu=3)