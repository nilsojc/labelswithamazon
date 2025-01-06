<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>
  
## ☁️  Building an image labels generator using Amazon Rekognition ☁️

In this project, I created an image labels generator using Amazon Rekognition. With this tool, we can easily identify individual parts of an image and assign a label. For instance, if you have a photo of a high traffic environment, Amazon Recognition will be able to identify what it is, and label the image with it's parts.


<h2>Environments and Technologies Used</h2>

  - Amazon Web Services (AWS)
  - S3 
  - AWS CLI
  - Python
  - Amazon Rekognition
  - IAM
  - Visual Code
  - boto3
  
  
<h2>How to Build</h2>

1. **Create a S3 Bucket and upload files**  

![image](/assets/image1.png)
![image](/assets/image2.png)

For this project, we will use a sample image from Orlando city.

![image](/assets/orlando.jpg)

2. **Install and configure AWS CLI**  
Open the terminal for your operating system and use these commands accordingly:

To check if the AWS CLI (Command Line Interface) was installed successfully on your system, you can run the following command in your terminal or command prompt:

```
`aws --version`
```

Next, we will need to configure AWS CLI with command `AWS configure`. For this, we will need to set up a user in IAM with an access key and secret access key through the console so that we can execute actions and commands with our AWS account:
![image](/assets/image5.png)

After searching `IAM` in the AWS console we start creating a user:
![image](/assets/image6.png)
![image](/assets/image7.png)

Next, after assigning a name we create permissions for our new user:
![image](/assets/image8.png)

NOTE: The permission policies that we are assigning to this user will be giving access to all AWS services. It is generally not recommended if the user will be used by someone else.

Then, we click on the user and create an access key:
![image](/assets/image9.png)

When prompted, choose CLI and check on the confirmation box as well as next.
![image](/assets/image10.png)
It will then generate an access key and secret key. These keys can be used to access your AWS services so make sure these are kept confidential. Then, we go back to the terminal to input the keys:
![image](/assets/image11.png)
NOTE: Make sure the region of the S3 bucket and the CLI region on terminal matches.

---

3. **Importing Libraries from Python**
   In this step, we will write the python code for extracting pictures from S3 bucket and applying detect_labels operation from Rekognition to generate the labels with their confidence score.

   We first begin utilizing Visual Code (or any IDE of your liking) in order to create a .py file so that we can perform our coding.

   ![image](/assets/image12.png)

   On our terminal, we will install the libraries needed for the project:
   ```
.-  `pip install boto3`
-  `pip install matplotlib`
   ```
   
For our code, we will need to import the following libraries:
- boto3 for interacting with AWS services.
- matplotlib for visualization.
- PIL (Python Imaging Library) for handling image data.
- BytesIO from the io module to work with image data.

We proceed by adding our code to the .py that we created:

![image](/assets/image13.png)


5. **Define Functions**

In this step we will define a function called detect_labels. This function takes a photo and bucket name as input parameters.

Within the function we will create a Rekognition client using boto3.

![image](/assets/image14.png)

Then, we will use the detect_labels function from the Rekognition client to detect labels in the given photo.

![image](/assets/image15.png)

Our detected labels will be printed along with their confidence levels, along with loading the image that we uploaded from the S3 bucket using boto3 and PIL. 

![image](/assets/image16.png)
![image](/assets/image17.png)

Finally, we use matplolib to display the image and draw bounding boxes around the detected objects.

![image](/assets/image18.png)

6. **Final code with results**

We deploy a main funtion to test our detected_labels function.

![image](/assets/image19.png)

NOTE: Make sure that your photo and bucket string in the main function is renamed by the photo and bucket you are using. 

Final code should look like this:

![image](/assets/image20.png)
![image](/assets/image21.png)

Then, we open the terminal in the directory where the python file is present and run the command `python code.py`

![image](/assets/image22.png)

Note: Alternatively, .py file can be also opened within the python 3.12 (as of writing) framework.

![image](/assets/image23.png)

Lastly, it will display our desired result!

![image](/assets/image24.png)

**(Optional) Side Project**

I wanted to keep dabbling into Amazon Rekognition to make it detect the labels with either videos or .gif files. For videos, you can use Amazon Kinesis to point out a stream and create them in real time, though I suspect it is not Free tier. However, you can make it upload a gif to the bucket and create image labels frame by frame on a .gif file, with dependency `OpenCV`. code file was:

```
`def detect_labels_per_frame(photo, bucket):
    """Detect labels for each frame of a GIF."""
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, photo)
    gif_data = obj.get()['Body'].read()`
```

As a sample you can find the other .py file on the repository, as there are other changes to this file. The result for this instance will be as it follows:

![image](/assets/gif1.png)
![image](/assets/gif2.png)
![image](/assets/gif3.png)
    
 ---

<h2>Conclusion</h2>
This project made use of an image label generator by calling boto3 API into images uploaded with a S3 bucket combined with Amazon Rekognition. With this feature, you can identify individual parts of an object along with it's closest (defined by confident percentage) label definition. Alternatively, this tool can be used for Labels on Video Streams (Amazon Kinesis) or generated frame by frame with a gif file. 
☁️
