from src.LeonardoAPI import LeoREVAPI

leo_gen = LeoREVAPI()

model_map = {
    "default": "d69c8273-6b17-4a30-a13e-d6637ae1c644",
    "DreamShaper":"e316348f-7773-490e-adcd-46757c738eb7"
}

leonado_settings = {
    "prompt": input('Input Prompt:'),
    "negative_prompt": "out of frame, cropped, bad proportions, out of frame, bad anatomy, poorly drawn face, morbid, mutilated,((extra eyes)), ((extra arms)), ((extra legs)), ((extra fingers)), ((extra headphones)), ((two headphones)), ((extra heads)), ((extra eyes)) (((2 heads))), duplicate, man, men, blurry, abstract, disfigured, deformed, cartoon, animated, toy, figure, framed, 3d, cartoon, 3d, disfigured, bad art, deformed, poorly drawn, extra limbs, close up, b&w, weird colors, blurry, watermark, blur haze, 2 heads, long neck, watermark, elongated body, cropped image,out of frame,draft,deformed hands, twisted fingers, double image, malformed hands, multiple heads, extra limb, ugly, poorly drawn hands, missing limb, cut-off, over satured, grain, lowères, bad anatomy, poorly drawn face, mutation, mutated, floating limbs, disconnected limbs, out of focus, long body, disgusting, extra fingers, groos proportions, missing arms, mutated hands, cloned face, missing legs",
    "num_images": 4,
    "width": 512,
    "height": 768,
    "model": model_map['DreamShaper']
}

print(leo_gen.process_request(leonado_settings))