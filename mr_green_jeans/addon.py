# Addon utility class for looking up preferences and options
import os
import bpy

def addon_name():
    '''Get the name of the add-on'''
    return os.path.basename(os.path.dirname(os.path.realpath(__file__)))

def preference():
    '''Get the add-on preferences properties'''
    preference = bpy.context.preferences.addons[addon_name()].preferences
    return preference