import pandas as pd
import pyarrow.parquet as pq
import os
from PIL import Image
from io import BytesIO
import json

poses_dir = os.path.join('training', 'poses')
if not os.path.isdir(poses_dir):
    os.mkdir(poses_dir)
source_dir = os.path.join(poses_dir, 'source')
if not os.path.isdir(source_dir):
    os.mkdir(source_dir)
target_dir = os.path.join(poses_dir, 'target')
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)


table = pq.read_table('poses.parquet').to_pandas()
a =0

line = {}
counter = 0
prompts = []
for row in table.iterrows():
    line['source'] = 'source/' + str(counter) + '.png'
    line['target'] = 'target/' + str(counter) + '.png'
    line['prompt'] = row[1]['caption']
    image = Image.open(BytesIO(row[1]['original_image']['bytes']))
    image = image.resize(size=(512, 512))
    image.save(os.path.join(source_dir, str(counter)+'.png'), 'PNG')
    image.close()
    image = Image.open(BytesIO(row[1]['condtioning_image']['bytes']))
    image = image.resize(size=(512, 512))
    image.save(os.path.join(target_dir, str(counter)+'.png'), 'PNG')
    image.close()
    prompts.append(line)
    with open(os.path.join(poses_dir, 'prompt.json'), 'a') as f:
        json.dump(line, f)
        f.write('\n')
    counter += 1