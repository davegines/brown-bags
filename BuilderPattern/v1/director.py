class Director:
    def construct(self, builder):
        builder.build_header()
        builder.build_body()
        builder.build_footer()
