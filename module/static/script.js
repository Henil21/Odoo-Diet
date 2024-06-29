document.getElementById('dietForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value,
        height: document.getElementById('height').value,
        weight: document.getElementById('weight').value,
        activity_level: document.getElementById('activity_level').value,
        dietary_preferences: document.getElementById('dietary_preferences').value,
        allergies: document.getElementById('allergies').value,
        goal: document.getElementById('goal').value
    };

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('calories').innerText = `Your daily caloric needs are: ${data.caloric_needs.toFixed(2)} calories`;
        document.getElementById('breakfast').innerText = `Breakfast: ${data.meal_plan.breakfast}`;
        document.getElementById('lunch').innerText = `Lunch: ${data.meal_plan.lunch}`;
        document.getElementById('dinner').innerText = `Dinner: ${data.meal_plan.dinner}`;
        document.getElementById('snacks').innerText = `Snacks: ${data.meal_plan.snacks}`;
    });
});
