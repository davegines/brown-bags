from BuilderPattern.v1.builder_abc import BuilderAbc


class EquifaxBuilder(BuilderAbc):
    def build_header(self):
        self.rentplus_filing = 'Equifax|Pipe|Delimited|Header\n'

    def build_body(self):
        self.rentplus_filing += 'Contents|Here\n'

    def build_footer(self):
        self.rentplus_filing += 'Footer|Here'
