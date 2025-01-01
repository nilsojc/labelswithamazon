import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageSequence
from io import BytesIO

def upload_file_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to bucket {bucket} as {object_name}.")
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False
    return True

def detect_labels_per_frame(photo, bucket):
    """Detect labels for each frame of a GIF."""
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, photo)
    gif_data = obj.get()['Body'].read()

    # Load the GIF
    gif = Image.open(BytesIO(gif_data))

    frame_count = 0
    for frame in ImageSequence.Iterator(gif):
        frame_count += 1
        print(f"Processing frame {frame_count}...")

        # Save the frame to a temporary buffer
        buffer = BytesIO()
        frame.save(buffer, format="PNG")
        buffer.seek(0)

        # Call Rekognition for the frame
        client = boto3.client('rekognition')
        response = client.detect_labels(
            Image={'Bytes': buffer.read()},
            MaxLabels=10
        )

        print(f"Detected labels for frame {frame_count}:")
        for label in response['Labels']:
            print("Label:", label['Name'])
            print("Confidence:", label['Confidence'])
            print()

        # Display the frame with bounding boxes
        plt.imshow(frame)
        ax = plt.gca()

        for label in response['Labels']:
            for instance in label.get('Instances', []):
                bbox = instance['BoundingBox']
                left = bbox['Left'] * frame.width
                top = bbox['Top'] * frame.height
                width = bbox['Width'] * frame.width
                height = bbox['Height'] * frame.height

                rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)

                label_text = label['Name'] + ' (' + str(round(label['Confidence'], 2)) + '%)'
                plt.text(left, top - 2, label_text, color='r', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

        plt.axis('off')
        plt.title(f"Frame {frame_count}")
        plt.show()

def main():
    photo = 'orlando.gif'
    bucket = 'imagelabelgenerator'

    # Upload the .gif file to S3
    if upload_file_to_s3(photo, bucket):
        detect_labels_per_frame(photo, bucket)
    else:
        print("Failed to upload the file. Exiting.")

if __name__ == "__main__":
    main()



                        