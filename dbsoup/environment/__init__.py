from jinja2 import Environment, PackageLoader, Template, FileSystemLoader


class TemplateLoader:
    def __init__(self) -> None:
        self.jina_env = self.get_jinja_environment()

    def get_template(self, template_name: str) -> Template:
        return self.jina_env.get_template(template_name)

    @staticmethod
    def get_jinja_environment() -> Environment:
        """
        used to get a jinja2 templating environment.
        Returns: Jinja2 Environment
        """
        loader = PackageLoader(package_name="dbsoup", package_path="core/database/dialects")
        return Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
