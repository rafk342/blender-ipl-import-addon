import bpy


class set_object_id(bpy.types.Operator):
    
    bl_idname = "object.set_object_id"
    bl_label = "set object id"

    def execute(self, context):
        selected_objects = context.selected_objects

        object_id = context.scene.object_id

        for obj in selected_objects:
            if obj.type == "EMPTY":
                bpy.data.objects[obj.name_full.split(".")[0]]['id'] = object_id
            if obj.type == "MESH":
                bpy.data.objects[obj.name_full]['id'] = object_id
            
        return {'FINISHED'}



class show_console(bpy.types.Operator):
    bl_idname = "object.show_console"
    bl_label = "show console"

    def execute(self, context):
        bpy.ops.wm.console_toggle()
            
        return {'FINISHED'}

class ipl_panel(bpy.types.Panel):
    
    bl_idname = "ipl_panel"
    bl_label = "IPL tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.scale_y = 1.05
        row.operator("object.print_selected_objects_operator", text= "IPL format lines in console")

        row = layout.row()
        row.scale_y = 1.05
        row.operator("object.show_console", text= "Open/Close Console")
        
        row = layout.row(align=True)
        row.scale_y = 1.05
        row.operator("object.set_object_id", text = "Set object ID to selected")
        row.prop(context.scene, "object_id", text="")

        row = layout.row()
        row.scale_y = 1.1
        
        selected_objects = context.selected_objects
        if len(selected_objects) > 0:
            obj = bpy.data.objects[selected_objects[0].name_full]
            
            if obj.type == "EMPTY":
                object_id = bpy.data.objects[selected_objects[0].name_full.split(".")[0]].get('id')
            
            else:
                object_id = obj.get('id')

            if object_id is not None:
                row.label(text="Current Object ID: {}".format(object_id))
            
