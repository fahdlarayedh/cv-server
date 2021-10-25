import load_model

data = load_model.json.load(load_model.sys.stdin)
image_convert_fromb64 = load_model.convert_to_image(str(data['image']))
#load_model.show_inference(load_model.detection_model,image_convert_fromb64)

#print('done.')

res = {
  "test":load_model.test,
  "detection":load_model.detection,
}

print(load_model.json.dumps(res))

#sys.stdout.flush()