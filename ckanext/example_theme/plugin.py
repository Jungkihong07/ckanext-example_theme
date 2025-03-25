import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ExampleThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    

    # IConfigurer
    class ExampleThemePlugin(plugins.SingletonPlugin):
        pass
    # '''An example theme plugin.

    # '''
    # pass

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "example_theme")

    
