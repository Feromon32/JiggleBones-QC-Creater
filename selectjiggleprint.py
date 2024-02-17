import bpy

obj = bpy.context.object

selected_bones = [bone.name for bone in obj.data.bones if bone.select]

output_text = '\n'.join([
    f'$jigglebone "{bone}"\n'
    '{\n'
    '    is_flexible\n'
    '    {\n'
    '        length 10\n'
    '        tip_mass 10\n'
    '        pitch_stiffness 40\n'
    '        pitch_constraint -70 0\n'
    '        pitch_damping 6\n'
    '        yaw_stiffness 75\n'
    '        yaw_damping 6\n'
    '        along_stiffness 100\n'
    '        along_damping 0\n'
    '        angle_constraint 10\n'
    '    }\n'
    '}'
    for bone in selected_bones
])

bpy.context.window_manager.clipboard = output_text
print("Done, press 'Ctrl + V' in your qc file.")
