import json
from PIL import Image
import os
import glob


path = './traffic/image'
files = glob.glob(path+'/*')
make_path = './cropped/image/'




for idx, file in enumerate(files):
  im = Image.open(file)
  w, h = im.size
  index = file.split('\\')[1].split('.')[0]
  with open('./traffic/label/'+index+'.json') as f:
    json_data = json.load(f)
  
  label = {}
  print(len(json_data['annotation']))
  i = 0
  for dic in json_data['annotation']:
    if dic['class'] == 'traffic_sign':
      if 'type' in dic.keys():
        label['type'] = dic['type']
      if 'shape' in dic.keys():
        label['shape'] = dic['shape']
      if 'color' in dic.keys():
        label['color'] = dic['color']
      if 'text' in dic.keys():
        label['text'] = dic['text']
        class_path = label['type']+'_'+label['shape']+'_'+label['color']+'/'
      try: 
        crop_image = im.crop(tuple(dic['box']))
      except ValueError:
        break
      else: 
        #crop_image.show()
        try:
          crop_image.save(make_path+class_path+str(index)+'_'+str(i)+'.jpg')
        except FileNotFoundError:
          break
        else:
          with open('./cropped/label/'+str(index)+'_'+str(i)+'.json','w') as l:
            json.dump(label,l)
          i = i+1
