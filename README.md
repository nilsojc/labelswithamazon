<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>
  
##  Building an image labels generator using Amazon Rekognition

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

`aws --version`

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
-  `pip install boto3`
-  `pip install matplotlib`

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
 ---

<h2>Conclusion</h2>
This projects demostrates a real-world scenario where we can create a website hosted with an S3 bucket utilizing AWS. In this example we also utilized .HTML and .CSS files to load our resume file into the bucket. By utilizing secure dns protocols and traffic through Route 53 and Cloudfront, we made sure that our website is fully compliant and accessible, as well as providing our own custom domain. This project was made with AWS free tier on all tools except for Route 53, where creating hosted zones has a cost as well. You can add a CNAME to a Cloudfront endpoint address using godaddy instead if you wish to cut on costs. Note that CNAMEs are not available at the root (apex) of the domain, so unless godaddy provides a CNAME flattening service (equivalent to Alias) you can only set it on a subdomain. There is also a cost in purchasing a third party domain or inside AWS. With this feature, you can utilize both without issues.
☁️
