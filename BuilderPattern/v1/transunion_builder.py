from BuilderPattern.v1.builder_abc import BuilderAbc


class TransUnionBuilder(BuilderAbc):
    def build_header(self):
        self.rentplus_filing = 'TransUnion Fixed Width Header\n'

    def build_body(self):
        self.rentplus_filing += 'Contents  Here\n'

    def build_footer(self):
        self.rentplus_filing += 'Footer  Here'
