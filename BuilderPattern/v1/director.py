class Director:
    def __init__(self):
        self.builder = None

    def construct(self, builder):
        self.builder = builder
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()
