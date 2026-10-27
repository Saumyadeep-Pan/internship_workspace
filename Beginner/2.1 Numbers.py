def format_representation(number,format_specifier):
    return "{:{}}".format(number,format_specifier)

output=format_representation(145,"o")

print(f"Output result    :{output}")
print(f"Data type returned:{type(output)}")
