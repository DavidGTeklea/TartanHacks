from roboflow import Roboflow
rf = Roboflow(api_key="c5Ak0Ld4PWZ1PNR0nt23")

# roboflow load model
rf = Roboflow(api_key="c5Ak0Ld4PWZ1PNR0nt23")
mob_project = rf.workspace().project("minecraft-mob-detection")
mob_model = mob_project.version(10).model

tree_project = rf.workspace().project("minecraft-tree-detection")
tree_model = tree_project.version(1).model

# infer on a local image
image_name = "Classifier/output/image11"

# visualize your prediction
print(mob_model.predict(image_name + ".jpg", confidence=40, overlap=20).json().get('predictions'))
print(tree_model.predict(image_name + ".jpg", confidence=55, overlap=20).json().get('predictions'))

# visualize your prediction
mob_model.predict(image_name + ".jpg", confidence=10, overlap=10).save(image_name + "_mob.jpg")
tree_model.predict(image_name + ".jpg", confidence=55, overlap=20).save(image_name + "_tree.jpg")