
const userInputsList = [];
function updateTextInput(val) {
    document.getElementById('textInput').value=val; 
  }
function submitForm(){
    const numItems = document.getElementById('amountToDonateInput').value;
    const boroughItem = document.querySelector('input[name="area"]:checked').value;    const genderCheckboxes = document.querySelectorAll('input[name="gender"]:checked');
    const selectedGenders = [];

    // Iterate through checkboxes and add checked ones to the array
    genderCheckboxes.forEach(checkbox => {
        selectedGenders.push(checkbox.value);
    });
    document.write(numItems,selectedGenders.length, boroughItem);
    if (!numItems || selectedGenders.length == 0 || !boroughItem) {
        alert('Please fill out all fields');
        return;
    }

    const userInput={
        numItems:numItems,
        boroughItem:boroughItem,
        selectedGenders:selectedGenders,
    };
    userInputsList.push(userInput);
}
