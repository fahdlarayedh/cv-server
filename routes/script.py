import load_model

data = load_model.json.load(load_model.sys.stdin)
image_convert_fromb64 = load_model.convert_to_image(str(data['image']))
val = load_model.launch(image_convert_fromb64)

#print('done.')

res = {
  "evaxData":load_model.evaxData,
  "qrCodeData":load_model.qrCodeData,
}

print(load_model.json.dumps(res))

#sys.stdout.flush()