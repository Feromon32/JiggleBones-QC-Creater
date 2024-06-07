import bpy

obj = bpy.context.object

selected_bones = [bone.name for bone in obj.data.bones if bone.select]

# just change this settings, if need that
jigglebone_template = '''
$jigglebone "{bone}"
{{
    is_flexible
    {{
        length 10
        tip_mass 10
        pitch_stiffness 40
        pitch_constraint -70 0
        pitch_damping 6
        yaw_stiffness 75
        yaw_damping 6
        along_stiffness 100
        along_damping 0
        angle_constraint 10
    }}
}}
'''

output_text = '\n'.join([jigglebone_template.format(bone=bone) for bone in selected_bones])


bpy.context.window_manager.clipboard = output_text

print("Done, press 'Ctrl + V' in your qc file.")
