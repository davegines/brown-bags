from BuilderPattern.v1.builder_abc import BuilderAbc


class EquifaxBuilder(BuilderAbc):
    def build_header(self):
        self.full_file_contents = 'Equifax|Pipe|Delimited|Header\n'

    def build_body(self):
        self.full_file_contents += 'Contents|Here\n'

    def build_footer(self):
        self.full_file_contents += 'Footer|Here'
