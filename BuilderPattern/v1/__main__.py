from BuilderPattern.v1.director import Director
from BuilderPattern.v1.transunion_builder import TransUnionBuilder
from BuilderPattern.v1.equifax_builder import EquifaxBuilder

director = Director()

transunion_builder = TransUnionBuilder()
director.construct(transunion_builder)
transunion_product = transunion_builder.rentplus_filing

print(transunion_product, '\n')

equifax_builder = EquifaxBuilder()
director.construct(equifax_builder)
equifax_product = equifax_builder.rentplus_filing

print(equifax_product)
