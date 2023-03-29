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
    
    print(f"0000, {string}, 0, {coord.x:.3f}, {coord.y:.3f}, {coord.z:.3f}, {rot.x:.3f}, {rot.y:.3f}, {rot.z:.3f}, {-(rot.w):.3f}, -1")

print("\n\n")
