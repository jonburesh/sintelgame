import bpy


class showSlider(bpy.types.Panel):
    bl_label = "Staff Parent"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    @classmethod
    def poll(self, context):
        
        staffBones = ["sintel_staff", "ribs", "hand.R", "hand_ik.R", "hand.L", "hand_ik.L"]
        
        return(bpy.context.active_object.type == 'ARMATURE' and bpy.context.active_bone.name in staffBones)
    
    def draw(self, context):
        layout = self.layout
        
       
       
        row = layout.row()
        row.prop(context.active_object.data, '["Staff-ribs"]', slider=True, text="Ribs")
        
        row = layout.row()
        row.prop(context.active_object.data, '["Staff-ik.L"]', slider=True, text="Left IK")
        
        row = layout.row()
        row.prop(context.active_object.data, '["Staff-ik.r"]', slider=True, text="Right IK")

        row = layout.row()
        row.prop(context.active_object.data, '["Staff-fk.l"]', slider=True, text="Left FK")

        row = layout.row()
        row.prop(context.active_object.data, '["Staff-fk.r"]', slider=True, text="Right FK")

bpy.utils.register_class(showSlider)