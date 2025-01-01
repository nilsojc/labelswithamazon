import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageSequence
from io import BytesIO

def detect_labels_in_gif(photo, bucket):
    """Detect labels for each frame of a GIF already stored in an S3 bucket."""
    try:
        # Load the GIF from S3
        s3 = boto3.resource('s3')
        gif_data = s3.Object(bucket, photo).get()['Body'].read()
        gif = Image.open(BytesIO(gif_data))

        # Process each frame
        for frame_count, frame in enumerate(ImageSequence.Iterator(gif), start=1):
            print(f"Processing frame {frame_count}...")

            # Save the frame as a PNG in memory
            buffer = BytesIO()
            frame.save(buffer, format="PNG")
            buffer.seek(0)

            # Call Rekognition for the frame
            client = boto3.client('rekognition')
            response = client.detect_labels(
                Image={'Bytes': buffer.read()},
                MaxLabels=10
            )

            # Display results and draw bounding boxes
            display_frame_with_labels(frame, response, frame_count)

    except Exception as e:
        print(f"Error processing GIF: {e}")

def display_frame_with_labels(frame, rekognition_response, frame_number):
    """Display a single GIF frame with bounding boxes and labels."""
    plt.imshow(frame)
    ax = plt.gca()

    for label in rekognition_response['Labels']:
        for instance in label.get('Instances', []):
            bbox = instance['BoundingBox']
            left = bbox['Left'] * frame.width
            top = bbox['Top'] * frame.height
            width = bbox['Width'] * frame.width
            height = bbox['Height'] * frame.height

            rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            label_text = f"{label['Name']} ({label['Confidence']:.2f}%)"
            plt.text(left, top - 2, label_text, color='r', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

    plt.axis('off')
    plt.title(f"Frame {frame_number}")
    plt.show()

def main():
    photo = 'orlando.gif'  # The GIF file already in the bucket
    bucket = 'imagelabelgenerator'

    detect_labels_in_gif(photo, bucket)

if __name__ == "__main__":
    main()

