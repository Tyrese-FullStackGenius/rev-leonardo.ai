from src.LeonardoAPI import LeoREVAPI

leo_gen = LeoREVAPI()

model_map = {
    "default": "d69c8273-6b17-4a30-a13e-d6637ae1c644"
}

leonado_settings = {
    "prompt": "Tim Burton Style Donald Duck",
    "negative_prompt": "",
    "num_images": 4,
    "width": 512,
    "height": 768,
    "model": model_map['default']
}

print(leo_gen.process_request(leonado_settings))