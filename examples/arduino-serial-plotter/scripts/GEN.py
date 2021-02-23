Import("env")
import shutil
import os

def after_build(source, target, env):
	shutil.copy(firmware_source, './firmware.hex')

env.AddPostAction("buildprog", after_build)

firmware_source = os.path.join(env.subst("$BUILD_DIR"), "firmware.hex")