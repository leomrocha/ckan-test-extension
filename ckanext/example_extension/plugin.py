import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from flask import Blueprint, render_template


def hello_plugin():
    u'''A simple view function'''
    return u'Hello World, this is served from an extension'


class Example_ExtensionPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)  # This is to add the Flask Blueprint support 

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'example_extension')

    # IBlueprint

    def get_blueprint(self):
        u'''Return a Flask Blueprint object to be registered by the app.'''
        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        # Add plugin url rules to Blueprint object
        # this adds a path to the API as /hello_plugin using the hello_plugin function 
        blueprint.add_url_rule('/hello_plugin', '/hello_plugin', hello_plugin)
        return blueprint