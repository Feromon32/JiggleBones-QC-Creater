import bpy
context = bpy.context
obj = context.object

namelist = [
"ValveBiped.Bip01_Pelvis",
"ValveBiped.Bip01_L_Thigh",
"ValveBiped.Bip01_L_Calf",
"ValveBiped.Bip01_L_Foot",
"ValveBiped.Bip01_L_Toe0",
"ValveBiped.Bip01_R_Thigh",
"ValveBiped.Bip01_R_Calf",
"ValveBiped.Bip01_R_Foot",
"ValveBiped.Bip01_R_Toe0",
"ValveBiped.Bip01_Spine",
"ValveBiped.Bip01_Spine1",
"ValveBiped.Bip01_Spine2",
"ValveBiped.Bip01_Spine4",
"ValveBiped.Bip01_Neck1",
"ValveBiped.Bip01_Head1",
"ValveBiped.Bip01_L_Clavicle",
"ValveBiped.Bip01_L_UpperArm",
"ValveBiped.Bip01_L_Forearm",
"ValveBiped.Bip01_L_Hand",
"ValveBiped.Bip01_L_Finger0",
"ValveBiped.Bip01_L_Finger01",
"ValveBiped.Bip01_L_Finger02",
"ValveBiped.Bip01_L_Finger1",
"ValveBiped.Bip01_L_Finger11",
"ValveBiped.Bip01_L_Finger12",
"ValveBiped.Bip01_L_Finger2",
"ValveBiped.Bip01_L_Finger21",
"ValveBiped.Bip01_L_Finger22",
"ValveBiped.Bip01_L_Finger3",
"ValveBiped.Bip01_L_Finger31",
"ValveBiped.Bip01_L_Finger32",
"ValveBiped.Bip01_L_Finger4",
"ValveBiped.Bip01_L_Finger41",
"ValveBiped.Bip01_L_Finger42",
"ValveBiped.Bip01_R_Clavicle",
"ValveBiped.Bip01_R_UpperArm",
"ValveBiped.Bip01_R_Forearm",
"ValveBiped.Bip01_R_Hand",
"ValveBiped.Bip01_R_Finger0",
"ValveBiped.Bip01_R_Finger01",
"ValveBiped.Bip01_R_Finger02",
"ValveBiped.Bip01_R_Finger1",
"ValveBiped.Bip01_R_Finger11",
"ValveBiped.Bip01_R_Finger12",
"ValveBiped.Bip01_R_Finger2",
"ValveBiped.Bip01_R_Finger21",
"ValveBiped.Bip01_R_Finger22",
"ValveBiped.Bip01_R_Finger3",
"ValveBiped.Bip01_R_Finger31",
"ValveBiped.Bip01_R_Finger32",
"ValveBiped.Bip01_R_Finger4",
"ValveBiped.Bip01_R_Finger41",
"ValveBiped.Bip01_R_Finger42"
]

ob = bpy.context.object
armaturebones = []
if ob.type == 'ARMATURE':
    armature = ob.data

    for bone in armature.bones:
        armaturebones.append(bone.name)
        

for item in namelist:
    if item in armaturebones:
        armaturebones.remove(item)


for v in armaturebones:
    print("$jigglebone " + "'" + v + "'")
    print("{")
    print("    is_flexible")
    print("    {")
    print("        length 10")
    print("        tip_mass 200")
    print("        pitch_stiffness 75")
    print("        pitch_damping 6")
    print("        yaw_stiffness 75")
    print("        yaw_damping 6")
    print("        along_stiffness 100")
    print("        along_damping 0")
    print("        angle_constraint 10")
    print("    }")
    print("}")
        