from openai import AzureOpenAI, OpenAI
import os
import requests
from PIL import Image
import dotenv
import traceback

# import dotenv
dotenv.load_dotenv()


# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
client = AzureOpenAI(
    # this is also the default, it can be omitted
    api_key=os.environ['AZURE_OPENAI_KEY'],
    api_version="2023-05-15",
    azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT']
)

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

model = os.environ['AZURE_OPENAI_DEPLOYMENT']
model = os.environ['OPENAI_IMAGE_MODEL']

try:
    # Create an image by using the image generation API

    prompt = 'Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils'
    prompt = 'A beautiful house next to the mountain with fantastic scenary.'
    prompt = 'Cartoon character from PJ masks named Cat boy playing football with a child. Create a football ground background with lighting effect.'
    prompt = 'Generate an image of a realistic south indian woman taking care of her children. Generate a scenic village background for the image.'
    prompt = 'Generate a super hero image rescuing middle aged children from thieves. The image should look similar to a movie poster.'
    prompt = 'Generate an image of spider man who is a superhero character eating chicken pizza.'
    prompt = 'Generate an image of Iron man who is a superhero character eating an indian dish named dosa along with side dish named coconut chutney.'

    generation_response = client.images.generate(
        model=model,
        # Enter your prompt text here
        prompt=prompt,
        size='1024x1024',
        n=1
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    # extract image URL from response
    print("Response:")
    print(generation_response)
    image_url = generation_response.data[0].url
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except:
    print(traceback.format_exc())

# ---creating variation below---

"""
response = client.Image.create_variation(
    image=open(image_path, "rb"),
    n=1,
    size="1024x1024"
)
"""
# response = openai.Image.create_variation(
#   image=open(image_path, "rb"),
#   n=1,
#   size="1024x1024"
# )

# image_path = os.path.join(image_dir, 'generated_variation.png')

# image_url = response['data'][0]['url']

# generated_image = requests.get(image_url).content  # download the image
# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image)

# # Display the image in the default image viewer
# image = Image.open(image_path)
# image.show()
