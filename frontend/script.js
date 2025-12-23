const video = document.getElementById('webcam');
const resultText = document.getElementById('result-text');
const detectBtn = document.getElementById('detect-btn');

async function setupWebcam() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
  } catch (err) {
    alert('Could not access webcam. Please allow camera permissions.');
    console.error(err);
  }
}

setupWebcam();

detectBtn.addEventListener('click', async () => {
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const imageDataURL = canvas.toDataURL('image/jpeg');

  resultText.innerText = 'Detecting...';

  try {
    const response = await fetch('http://localhost:5000/detect', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ image: imageDataURL }),
    });

    const result = await response.json();
    resultText.innerText = `🧠 Face Emotion: ${result.face_emotion}\n✋ Hand Gesture: ${result.hand_gesture}`;
  } catch (error) {
    resultText.innerText = '❌ Detection failed. Is the backend running?';
    console.error(error);
  }
});
