import bpy

class print_selected_objects_operator(bpy.types.Operator):
   
    bl_idname = "object.print_selected_objects_operator"
    bl_label = "console format lines"
    
    def execute(self, context):
        selected_objects = context.selected_objects

        print("\n" * 3)

        for obj in selected_objects:

            obj.rotation_mode = 'QUATERNION'
            coord = obj.location
            rot = obj.rotation_quaternion

            if "." in obj.name:
                object_name = obj.name.split(".")[0]

            else:
                object_name = obj.name        

            obj_id = bpy.data.objects[obj.name_full].get('id', None)

            if obj_id is None:
                obj_id = "0000"

            if obj.type == "EMPTY":
                obj_id = bpy.data.objects[object_name].get('id', None)
                
            rot_x = 0 if rot.x > -0.001 and rot.x < 0.001 else f"{rot.x:.3f}"
            rot_y = 0 if rot.y > -0.001 and rot.x < 0.001 else f"{rot.y:.3f}"
            rot_z = 0 if rot.z > -0.001 and rot.x < 0.001 else f"{rot.z:.3f}"
            rot_w = 0 if rot.w > -0.001 and rot.x < 0.001 else f"{-rot.w:.3f}"

            print(f"{obj_id}, {object_name}, 0, {coord.x:.3f}, {coord.y:.3f}, {coord.z:.3f}, {rot_x}, {rot_y}, {rot_z}, {rot_w}, -1")

        return {'FINISHED'}

