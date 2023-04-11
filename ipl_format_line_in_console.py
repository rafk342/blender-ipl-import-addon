import bpy 
import struct 
 
print("\n\n")
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    
    coord = obj.location
    rot = obj.rotation_quaternion
    
    if "." in obj.name:
        string= obj.name.split(".")[0]
        
    else:
        string = obj.name        
    
    rot_x = 0 if rot.x == 0.0 else f"{rot.x:.3f}"
    rot_y = 0 if rot.y == 0.0 else f"{rot.y:.3f}"
    rot_z = 0 if rot.z == 0.0 else f"{rot.z:.3f}"
    rot_w = 0 if rot.w == 0.0 else f"{-rot.w:.3f}"
        
        
    print(f"0000, {string}, 0, {coord.x:.3f}, {coord.y:.3f}, {coord.z:.3f}, {rot_x}, {rot_y}, {rot_z}, {rot_w}, -1")

print("\n\n")
