document.getElementById('review-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var review = document.getElementById('review').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review: review })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sentiment').textContent = data.sentiment;
    })
    .catch(error => console.error('Error:', error));
});
