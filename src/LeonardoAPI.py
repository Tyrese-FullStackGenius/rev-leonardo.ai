import requests
import time
from src.GetAllAccessTokens import HeadlessSaver

class LeoREVAPI:
    def __init__(self):
        self.webAPI = "https://api.leonardo.ai/v1/graphql"
        self.api_key = ""
        self.sub_id = ""
        self.user_id = ""

    def process_request(self, settings_obj):
        headless_server = HeadlessSaver()
        account_check = headless_server.confirm_account_is_good()
        self.api_key = account_check["access_token"]
        self.sub_id = account_check["sub_id"]
        self.get_user_details()
        self.generate_image(settings_obj["prompt"], settings_obj["negative_prompt"], True, 4, settings_obj['width'], settings_obj['height'], settings_obj['model'])
        print("+ Generating Image")
        self.generate_image(settings_obj["prompt"], settings_obj["negative_prompt"], True, 4, settings_obj['width'], settings_obj['height'], settings_obj['model'])
        image_urls = []
        for image in self.get_images():
            image_urls.append(image["url"])
        final_response = {"settings": settings_obj, "images": image_urls}
        return final_response

    def generate_image(
        self,
        postive_propt,
        negative_prompt,
        nsfw=True,
        num_images=4,
        width=512,
        height=768,
        model_id="d69c8273-6b17-4a30-a13e-d6637ae1c644",
    ):
        headers = {
            "authority": "api.leonardo.ai",
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": f"Bearer {self.api_key}",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://app.leonardo.ai",
            "pragma": "no-cache",
            "referer": "https://app.leonardo.ai/",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        }

        data = {
            "operationName": "CreateSDGenerationJob",
            "variables": {
                "arg1": {
                    "prompt": postive_propt,
                    "negative_prompt": negative_prompt,
                    "nsfw": nsfw,
                    "num_images": num_images,
                    "width": width,
                    "height": height,
                    "num_inference_steps": 10,
                    "guidance_scale": 7,
                    "init_strength": 0.4,
                    "sd_version": "v1_5",
                    "modelId": model_id,
                    "presetStyle": "LEONARDO",
                    "scheduler": "LEONARDO",
                    "public": True,
                    "tiling": False,
                    "leonardoMagic": True,
                    "imagePrompts": [],
                    "imagePromptWeight": 0.45,
                    "poseToImage": False,
                    "poseToImageType": "POSE",
                    "weighting": 1,
                    "highContrast": True,
                    "leonardoMagicVersion": "v2",
                }
            },
            "query": "mutation CreateSDGenerationJob($arg1: SDGenerationInput!) {\n  sdGenerationJob(arg1: $arg1) {\n    generationId\n    __typename\n  }\n}",
        }
        response = requests.post(self.webAPI, headers=headers, json=data).json()
        return response

    def get_user_details(self):
        headers = {
            "authority": "api.leonardo.ai",
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": f"Bearer {self.api_key}",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://app.leonardo.ai",
            "pragma": "no-cache",
            "referer": "https://app.leonardo.ai/",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        }
        sub = self.sub_id
        data = (
            f'{{"operationName":"GetUserDetails","variables":{{"userSub":"{sub}"}},'
            f'"query":"query GetUserDetails($userSub: String) {{\\n users(where: {{user_details: {{cognitoId: {{_eq: $userSub}}}}}}) {{\\n id\\n username\\n user_details {{\\n auth0Email\\n plan\\n paidTokens\\n apiCredit\\n subscriptionTokens\\n subscriptionModelTokens\\n subscriptionGptTokens\\n interests\\n interestsRoles\\n interestsRolesOther\\n showNsfw\\n tokenRenewalDate\\n planSubscribeFrequency\\n __typename\\n }}\\n __typename\\n }}\\n}}"}}'
        )

        response = requests.post(
            "https://api.leonardo.ai/v1/graphql", headers=headers, data=data
        ).json()

        if response["data"]["users"][0]["user_details"][0]["subscriptionTokens"] > 5:
            self.user_id = response["data"]["users"][0]["id"]
        else:
            self.process_request()

    def get_images(self, draw_amount=4):
        headers = {
            "authority": "api.leonardo.ai",
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": f"Bearer {self.api_key}",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://app.leonardo.ai",
            "pragma": "no-cache",
            "referer": "https://app.leonardo.ai/",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        }
        query = """
        query GetAIGenerationFeed($where: generations_bool_exp, $userId: uuid!, $limit: Int, $offset: Int = 0) {
        generations(
            limit: $limit
            offset: $offset
            order_by: [{createdAt: desc}]
            where: $where
        ) {
            alchemy
            contrastRatio
            highResolution
            guidanceScale
            inferenceSteps
            modelId
            scheduler
            coreModel
            sdVersion
            prompt
            negativePrompt
            id
            status
            quantity
            createdAt
            imageHeight
            imageWidth
            presetStyle
            sdVersion
            public
            seed
            tiling
            initStrength
            highContrast
            promptMagic
            imagePromptStrength
            user {
            username
            id
            __typename
            }
            custom_model {
            id
            userId
            name
            modelHeight
            modelWidth
            __typename
            }
            init_image {
            id
            url
            __typename
            }
            generated_images(order_by: [{url: desc}]) {
            id
            url
            likeCount
            generated_image_variation_generics(order_by: [{createdAt: desc}]) {
                url
                status
                createdAt
                id
                transformType
                upscale_details {
                oneClicktype
                isOneClick
                id
                variationId
                __typename
                }
                __typename
            }
            user_liked_generated_images(limit: 1, where: {userId: {_eq: $userId}}) {
                generatedImageId
                __typename
            }
            __typename
            }
            __typename
        }
        }
        """

        data = {
            "operationName": "GetAIGenerationFeed",
            "variables": {
                "where": {
                    "userId": {"_eq": self.user_id},
                    "canvasRequest": {"_eq": False},
                },
                "offset": 0,
                "userId": self.user_id,
                "limit": draw_amount,
            },
            "query": query,
        }
        time.sleep(15)
        print('+ Waiting for response.')
        response = requests.post(self.webAPI, headers=headers, json=data).json()
        images_array = response["data"]["generations"][0]["generated_images"]
        if len(images_array) < 1:
            self.get_images()
            return "No Images Found"
        else:
            return images_array
