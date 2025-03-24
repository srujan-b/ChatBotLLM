document.getElementById('analyze-form').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const formData = new FormData();
    formData.append('user_answers', document.getElementById('user_answers').value);
    formData.append('image', document.getElementById('image').files[0]);
  
    document.getElementById('result').innerText = 'Processing...';
  
    try {
      const response = await fetch('http://<YOUR_PUBLIC_IP>:1021/v1/analyze', {
        method: 'POST',
        body: formData
      });
  
      if (!response.ok) throw new Error(`Error: ${response.status}`);
  
      const data = await response.json();
  
      document.getElementById('result').innerText = 
        `Question Model:\n${data.question_model_analysis}\n\nVision Model:\n${data.vision_model_analysis}`;
  
    } catch (error) {
      document.getElementById('result').innerText = `Failed: ${error}`;
    }
  });
  