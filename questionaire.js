const userInputsList = [];
function updateTextInput(val) {
    document.getElementById('textInput').value=val; 
  }
function submitForm(){
    const numItems = document.getElementById('amountToDonate').value;
    const selectedGenders = [];

    // Iterate through checkboxes and add checked ones to the array
    for (let i = 0; i < genderCheckboxes.length; i++) {
        if (genderCheckboxes[i].checked) {
            selectedGenders.push(genderCheckboxes[i].value);
        }
    }
    const boroughItem = document.getElementById('borough').value;

    if (!numItems || selectedGenders.length === 0 ||!boroughItem) {
        alert('Please fill out all fields');
        return;
    }

    const userInput={
        numItems:numItems,
        genderAndAgeItems:genderAndAgeItems,
        boroughItem:boroughItem,
    };
    userInputsList.push(userInput);
}
