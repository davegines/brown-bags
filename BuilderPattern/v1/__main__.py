from BuilderPattern.v1.director import Director
from BuilderPattern.v1.transunion_builder import TransUnionBuilder
from BuilderPattern.v1.equifax_builder import EquifaxBuilder

director = Director()

transunion_builder = TransUnionBuilder()
director.construct(transunion_builder)
transunion_file = transunion_builder.full_file_contents

print(transunion_file, '\n')

equifax_builder = EquifaxBuilder()
director.construct(equifax_builder)
equifax_file = equifax_builder.full_file_contents

print(equifax_file)
