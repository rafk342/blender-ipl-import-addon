import bpy 
import struct 
 
from bpy_extras.io_utils import ( 
    ImportHelper 
) 
  
print(" ===================================================== ")
class CustomDrawOperator(bpy.types.Operator, ImportHelper): 
    bl_idname = "object.custom_draw" 
    bl_label = "Import" 
  
    filepath = bpy.props.StringProperty(subtype="FILE_PATH") 
  
    def execute(self, context): 
        print(self.filepath) 
 
        encoding = "cp1251" 
        ipl_path = self.filepath 
 
        ipl_objects = {} 
 
 
        with open(ipl_path, "r", encoding=encoding) as f: 
            for line in f: 
                elements = [elem.strip() for elem in line.split(",")] 
                if len(elements) >= 4: 
                    obj_name = elements[1]
                    x, y, z, rotx, roty, rotz, rotw = map(float, elements[3:10]) 
                    if obj_name not in ipl_objects:
                        ipl_objects[obj_name] = {"coords_rot_list": [], "check": 0}
                        
                    ipl_objects[obj_name]["coords_rot_list"].append((x, y, z, rotx, roty, rotz, rotw))
                    ipl_objects[obj_name]["check"] += 1
        
        print("\n\n")
        
        for obj_name, data in ipl_objects.items():
            obj = bpy.data.objects.get(obj_name)
            if obj is None:
                #print(f" {obj_name} not found.")
                continue
            
            coords_rot_list = data['coords_rot_list']
            check = data['check']
            
            if check > 1:
                collection_name = obj_name + "_collection"
                if collection_name not in bpy.data.collections:
                    new_collection = bpy.data.collections.new(collection_name)
                    bpy.context.scene.collection.children.link(new_collection)
                    
                for i, coords_rot in enumerate(coords_rot_list):
                    new_obj = obj.copy()
                    new_obj.data = obj.data.copy()
                    new_obj.location = coords_rot[0:3] 
                    new_obj.rotation_mode = 'QUATERNION'
                    new_obj.rotation_quaternion = (-(coords_rot[6]), coords_rot[3], coords_rot[4], coords_rot[5])
                    new_obj.name = f"{obj_name}_{i}"
                    bpy.data.collections[collection_name].objects.link(new_obj)
                    print(f"{new_obj.name} location: {new_obj.location} rotation: (x = {coords_rot[3]}, y = {coords_rot[4]}, z = {coords_rot[5]}, w = {coords_rot[6]})")
                    print("\n")
            else:
                coords_rot = coords_rot_list[0]
                obj.location = coords_rot[0:3] 
                obj.rotation_mode = 'QUATERNION'
                obj.rotation_quaternion = (-(coords_rot[6]), coords_rot[3], coords_rot[4], coords_rot[5])
                print(f"{obj_name} location: {obj.location} rotation: (x = {coords_rot[3]}, y = {coords_rot[4]}, z = {coords_rot[5]}, w = {coords_rot[6]})")
                print("\n")
                
        return {'FINISHED'} 
 
bpy.utils.register_class(CustomDrawOperator) 
 
# test call 
bpy.ops.object.custom_draw('INVOKE_DEFAULT') 
 
#bpy.utils.unregister_class(CustomDrawOperator)
