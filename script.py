import itertools
import numpy as np
import mujoco
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


model_path = 'model1.xml'
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)


joint_ranges = []
for i in range(model.njnt):
    joint_limited = model.jnt_limited[i]
    if joint_limited:
        joint_range = np.linspace(model.jnt_range[i][0], model.jnt_range[i][1], 10)
    else:
        joint_range = np.linspace(-np.pi, np.pi, 10)  
    joint_ranges.append(joint_range)


configurations = itertools.product(*joint_ranges)
results = []


for config in configurations:
    data.qpos[:] = config
    data.qvel[:] = np.zeros(model.nv)
    data.qacc[:] = np.zeros(model.nv)

    mujoco.mj_fwdActuation(model, data)
    mujoco.mj_inverse(model, data)

    result = {
        'config': config,
        'torques': data.qfrc_inverse.copy()
    }
    results.append(result)


records = []
for result in results:
    for joint_index in range(model.njnt):
        records.append({
            'joint': mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, joint_index),
            'angle': result['config'][joint_index],
            'torque': result['torques'][joint_index]
        })

df = pd.DataFrame(records)
df.to_csv('data.csv', index=False)

plt.figure(figsize=(12, 6))
ax = sns.violinplot(x='joint', y='torque', data=df, inner='quart')
ax.set_title('Torques distribution in different joints')
ax.set_xlabel('Joint')
ax.set_ylabel('Torque')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
