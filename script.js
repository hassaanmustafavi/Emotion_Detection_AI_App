document.getElementById('emotionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const textInput = document.getElementById('textInput').value;
    try {
      const response = await fetch('/predict-emotion', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textInput })
      });
      const data = await response.json();
      document.getElementById('output').innerText = `Predicted Emotion: ${data.predictedEmotion}`;
    } catch (error) {
      console.error('Error:', error);
    }
  });
  