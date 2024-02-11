bl_info = {
    "name": "GreasePencil: Project to View for all Keyframes",
    "blender": (4, 0, 2),
    "category": ""
}
import bpy


class GpReprojectAllKeyframesOperator(bpy.types.Operator):
    """Project to view for all keyframes"""
    bl_idname = "gpencil.reproject_all_keyframes"
    bl_label = "Reproject for all Keyframes"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object

    def execute(self, context):
        scene = context.scene

        bpy.ops.screen.frame_jump(end=False)

        i = 0
        while scene.frame_current <= scene.frame_end and i < 1000:
            print("Reprojecting frame " + str(scene.frame_current))
            bpy.ops.gpencil.select_all(action='SELECT')
            bpy.ops.gpencil.reproject(type='VIEW', keep_original=False, offset=0.0)
            #bpy.ops.screen.keyframe_jump(next=True)
            bpy.ops.screen.frame_offset(delta=1)
            i += 1
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(GpReprojectAllKeyframesOperator.bl_idname,
                         text=GpReprojectAllKeyframesOperator.bl_label)


def register():
    bpy.utils.register_class(GpReprojectAllKeyframesOperator)
    bpy.types.VIEW3D_MT_edit_gpencil.append(menu_func)


def unregister():
    bpy.utils.unregister_class(GpReprojectAllKeyframesOperator)
    bpy.types.VIEW3D_MT_edit_gpencil.remove(menu_func)


if __name__ == "__main__":
    register()
