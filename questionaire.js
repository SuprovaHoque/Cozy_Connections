const userInputsList = [];
function submitForm(){
    const numItems = document.getElementById('amountToDonate').value;
    const genderItems = document.getElementById('genderAmount').value;
    const ageItems = document.getElementById('ageRange').value;
    const boroughItem = document.getElementById('borough').value;

    if (!numItems || !genderItems ||!ageItems ||!boroughItem) {
        alert('Please fill out all fields');
        return;
    }

    const userInput={
        numItems:numItems,
        genderItems:genderItems,
        ageItems:ageItems,
        boroughItem:boroughItem,
    };
    userInputsList.push(userInput);
}
