```python
import cv2
import pyzbar.pyzbar as pyzbar

def scan_qr_code():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read current frame from the camera
        ret, frame = cap.read()

        # Detect and decode QR codes
        decoded_objs = pyzbar.decode(frame)

        # Iterate over all detected QR codes
        for decoded_obj in decoded_objs:
            # Extract the data and type of the QR code
            qr_data = decoded_obj.data.decode("utf-8")
            qr_type = decoded_obj.type

            # Print the data and type
            print("QR Code Type:", qr_type)
            print("QR Code Data:", qr_data)

            # Draw a bounding box around the QR code
            (x, y, w, h) = decoded_obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # Draw the QR code data on the frame
            cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Wait for keypress to exit
        if cv2.waitKey(1) == ord("q"):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
```
