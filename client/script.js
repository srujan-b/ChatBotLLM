document.getElementById('analyze-form').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const submitBtn = document.getElementById('submit-btn');
    const loading = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
  
    submitBtn.disabled = true;
    loading.style.display = 'block';
    resultDiv.innerText = '';
  
    const formData = new FormData();
    formData.append('user_answers', document.getElementById('user_answers').value);
    formData.append('image', document.getElementById('image').files[0]);
  
    try {
      const response = await fetch('/v1/analyze', {
        method: 'POST',
        body: formData
      });
  
      if (!response.ok) throw new Error(`Error: ${response.status}`);
  
      const data = await response.json();
  
      resultDiv.innerText = `Based on your Query and Image:\n${data.vision_model_analysis}`;
  
    } catch (error) {
      resultDiv.innerText = `Failed: ${error}`;
    } finally {
      submitBtn.disabled = false;
      loading.style.display = 'none';
    }
  });
  
  // GP Button (Optional functionality)
  document.getElementById('connect-gp-btn').addEventListener('click', () => {
    alert('You will be connected to a GP shortly!');
  });
  