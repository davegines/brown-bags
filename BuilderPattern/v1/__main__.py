from BuilderPattern.v1.director import Director
from BuilderPattern.v1.concrete_builder import ConcreteBuilder

concrete_builder = ConcreteBuilder()
director = Director()
director.construct(concrete_builder)
product = concrete_builder.product
