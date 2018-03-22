class Director:
    def __init__(self):
        self.builder = None

    def construct(self, builder):
        self.builder = builder
        self.builder.build_header()
        self.builder.build_body()
        self.builder.build_footer()
