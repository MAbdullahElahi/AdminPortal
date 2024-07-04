let addRecordBtn = document.getElementById("addRecordBtn");
let addRecordForm = document.getElementById("addRecordForm");
let closeRecordBtn = document.getElementById("closeRecordForm");

let updateRecordBtn = document.getElementById("updateRecordBtn");
let updateRecordForm = document.getElementById("updateRecordForm");
let closeUpdateRecordBtn = document.getElementById("closeUpdateRecordFormBtn");

let deleteRecordBtn = document.getElementById("deleteRecordBtn");
let deleteRecordForm = document.getElementById("deleteRecordForm");
let closeDeleteRecordFormBtn = document.getElementById("closeDeleteRecordFormBtn");


function showHideForms(button, form, closeButton) {
    button.addEventListener("click", (e)=> {form.classList.replace("hide", "show");})    
    closeButton.addEventListener("click", (e)=> {form.classList.replace("show", "hide");})
};
showHideForms(button = addRecordBtn, form = addRecordForm, closeButton = closeRecordBtn);
showHideForms(button = updateRecordBtn, form = updateRecordForm, closeButton = closeUpdateRecordBtn);
showHideForms(button = deleteRecordBtn, form = deleteRecordForm, closeButton = closeDeleteRecordFormBtn);




document.addEventListener('DOMContentLoaded', function() {
    const selectField = document.getElementById('record_id');
    const details = {
        name: document.getElementById('record_name'),
        holder: document.getElementById('record_holder_name'),
        contact: document.getElementById('record_contact_num'),
        location: document.getElementById('record_location'),
        assignment: document.getElementById('record_assignment'),
        amount: document.getElementById('record_amount'),
        date: document.getElementById('record_date'),
        dateComplete: document.getElementById('record_date_completed'),
        account: document.getElementById('record_account_num'),
        socials: document.getElementById('record_socials'),
        status: document.getElementById('record_status')
    };

    

    function updateDetails() {
        const selectedOption = selectField.options[selectField.selectedIndex];
        details.name.value = selectedOption.getAttribute('data-name');
        details.holder.value = selectedOption.getAttribute('data-holder');
        details.contact.value = selectedOption.getAttribute('data-contact');
        details.location.value = selectedOption.getAttribute('data-location');
        details.assignment.value = selectedOption.getAttribute('data-assignment');
        details.amount.value = selectedOption.getAttribute('data-amount');
        details.date.value = selectedOption.getAttribute('data-date');
        details.dateComplete.value = selectedOption.getAttribute('data-datecomplete');
        details.account.value = selectedOption.getAttribute('data-account');
        details.socials.value = selectedOption.getAttribute('data-socials');
        details.status.checked = selectedOption.getAttribute('data-status') === 'True';
    }

    // Initialize details on page load
    updateDetails();

    // Update details when selection changes
    selectField.addEventListener('change', updateDetails);
});