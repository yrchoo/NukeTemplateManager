"""
This is menu.py read when Nuke launches.
"""

import nuke

import template_manager

# ===========================================
#   Nuke Template Manager Menu
# ===========================================

menu_bar = nuke.menu("Nuke")
ntm_menu = menu_bar.addMenu("NTM")

ntm_menu.addCommand("Load Template", )
ntm_menu.addCommand("Save Template",
                    "t_manager = template_manager.TemplateManager(); t_manager.show()")
ntm_menu.addCommand("Save Template as...", )
ntm_menu.addCommand("Launch Template Manager",
                    "t_manager = template_manager.TemplateManager(); t_manager.show()")
