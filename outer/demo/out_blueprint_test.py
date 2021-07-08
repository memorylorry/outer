"""
A sample to cover
"""
from BluePrintSample import BluePrintSample

# composite blueprint
blueprint = BluePrintSample('1')
# touch file or dir
out = blueprint.TRAIN_IMG_OUTPUT.touch_(2)
# std out
print(out)
