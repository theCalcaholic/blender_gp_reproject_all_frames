bl_info = {
    "name": "GreasePencil: Project to View for all Frames",
    "blender": (4, 0, 2),
    "category": ""
}
import bpy


class GpReprojectAllFramesOperator(bpy.types.Operator):
    """Project to view for all frames"""
    bl_idname = "gpencil.reproject_all_frames"
    bl_label = "Reproject for all Frames"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object

    def execute(self, context):
        scene = context.scene

        bpy.ops.screen.frame_jump(end=False)

        i = 0
        while scene.frame_current <= scene.frame_end and i < 1000:
            bpy.ops.gpencil.select_all(action='SELECT')
            bpy.ops.gpencil.reproject(type='VIEW', keep_original=False, offset=0.0)
            bpy.ops.screen.frame_offset(delta=1)
            i += 1
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(GpReprojectAllFramesOperator.bl_idname,
                         text=GpReprojectAllFramesOperator.bl_label)


def register():
    bpy.utils.register_class(GpReprojectAllFramesOperator)
    bpy.types.VIEW3D_MT_edit_gpencil.append(menu_func)


def unregister():
    bpy.utils.unregister_class(GpReprojectAllFramesOperator)
    bpy.types.VIEW3D_MT_edit_gpencil.remove(menu_func)


if __name__ == "__main__":
    register()
