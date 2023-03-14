import bpy 
import struct 
 
from bpy_extras.io_utils import ( 
    ImportHelper 
) 
  
class CustomDrawOperator(bpy.types.Operator, ImportHelper): 
    bl_idname = "object.custom_draw" 
    bl_label = "Import" 
  
    filepath = bpy.props.StringProperty(subtype="FILE_PATH") 
  
    def execute(self, context): 
        print(self.filepath) 
 
        encoding = "cp1251" 
        ipl_path = self.filepath #r"F:\gta sa models\arzamas_N.IPL" 
 
 
        ipl_objects = {} 
 
        with open(ipl_path, "r", encoding=encoding) as f: 
            for line in f: 
 
                elements = [elem.strip() for elem in line.split(",")] 
 
#[0//'4000', 1//'road_tran_01', 2//'0', 3//x'-318.924', 4//y'971.001', 5//z'11.001', 6//rotx'0', 7//roty'0', 8//rotz'0.707108', 9//rotw'-0.707105', '1'] 
 
                #print("   ", elements) 
 
                if len(elements) >= 4 and elements[1] in bpy.data.objects.keys(): 
                    x, y, z, rotx, roty, rotz, rotw = map(float, elements[3:10]) 
                    ipl_objects[elements[1]] = (x, y, z, rotx, roty, rotz, rotw) 
 
        print(ipl_objects.items()) 
 
        for obj_name, coords_rot in ipl_objects.items(): 
            if obj_name in bpy.data.objects: 
                obj = bpy.data.objects[obj_name] 
                obj.location = coords_rot[:3] 
                obj.rotation_mode = 'QUATERNION' 
                obj.rotation_quaternion = (coords_rot[6], coords_rot[3], coords_rot[4], coords_rot[5]) 
            else: 
                print(f"hui {obj_name}") 
 
        return {'FINISHED'} 
 
bpy.utils.register_class(CustomDrawOperator) 
 
# test call 
bpy.ops.object.custom_draw('INVOKE_DEFAULT') 
 
#bpy.utils.unregister_class(CustomDrawOperator)
