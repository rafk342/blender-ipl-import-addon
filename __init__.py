import struct 

if "bpy" in locals():
   
    import importlib
    importlib.reload(format_lines)
    importlib.reload(ipl_importer)
    importlib.reload(ui_panel)

else:
   
    import bpy
    from bpy_extras.io_utils import ImportHelper

    from .ipl_importer import *
    from .format_lines import *
    from .ui_panel import *



bl_info = {
	"name": "ipl tools",
	"description": "",
	"author": "swapfr",
	"version": (0, 0, 1),
	"blender": (5, 5, 1),
	"location": "3D View > Tools",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Development"
}
 


classes_array = [
    import_ipl_file, 
    print_selected_objects_operator, 
    ipl_panel, 
    set_object_id,
    show_console
    ]   

def register():
    for _class in classes_array:
        bpy.utils.register_class(_class)

    print(" \n\n register ipl \n\n ")

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.Scene.object_id = bpy.props.IntProperty(name="Object ID", default= 0000)

def unregister(): 
    for _class in classes_array:
        bpy.utils.unregister_class(_class)
    
    print(" \n\n unregister ipl \n\n ")
    
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    del bpy.types.Scene.object_id
    
if __name__ == "__main__":
	register()
    
