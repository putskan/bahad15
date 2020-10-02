function showTab(currentTab) {
  // This function will display the specified tab of the form ...
  /* for the user's disclaimer part (last page) responsiveness */
  if (screen.width >= 992) {
    document.getElementById("medical-page-main-wrapper").style.height = "auto";
    document.getElementById("medical-page-main-wrapper-2").style.height = "auto";
  }

  let tabElements = document.getElementsByClassName("tab");
  tabElements[currentTab].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (currentTab == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (currentTab == (tabElements.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "סיים";
    /* for the user's disclaimer part (last page) responsiveness */
    if (screen.width >= 992) {
      document.getElementById("medical-page-main-wrapper").style.height = "100%";
      document.getElementById("medical-page-main-wrapper-2").style.height = "100%";
    }
  } else {
    document.getElementById("nextBtn").innerHTML = "הבא";
  }
}


function nextPrev(n) {
  // This function will figure out which tab to display
  let tabElements = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  tabElements[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= tabElements.length) {
    //...the form gets submitted:
    hasUserSubmitted = true;
    if (confirm("האם אתה בטוח שברצונך לסיים?")) {
      document.getElementById("medical-form").submit();
      return false;
    } else {currentTab = currentTab - n}
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
  window.scrollTo(0, 0);
}


function disableEnableInput(elementNames, action) {
    /* 
    action: "enable" / "disable" 
    elementIdentifiers: Array of element names to enable / disable their input
    */
    let elements = [];
    elementNames.forEach(elementName => {
        elements = elements.concat(Array.from(document.getElementsByName(elementName)));
      });


    if (action === "enable") {
        elements.forEach(e => {
          e.disabled = false;
        })
        return true;

    } if (action === "disable") {
        elements.forEach(e => {
          e.value = "";
          e.checked = false;
          e.disabled = true;
        })
        return true;

    } else {
        console.log(action);
      }
}


function handleRadioButtonInputBoxCorrelation(radioId, inputId) {
  /* 
  Logics:
      * when writing in input box - "check" / "choose" correlating radio button
      * when writing in input box - assign written value to correlating radio's value
      * if radio is checked - make input required, else, drop required & initialize value
  */
  let radioElement = document.getElementById(radioId);
  let inputElement = document.getElementById(inputId);
  let handleRadioToggling = (radioElement, inputElement) => { // function for handling radio toggling (check / uncheck)
    if (radioElement.checked === false) {
      radioElement.value = "";
      inputElement.value = "";
      inputElement.required = false;
    } else {
      inputElement.required = true;
    }
  }

  // handle user input
  inputElement.onkeypress = () => {
    radioElement.checked = true;
    radioElement.value = inputElement.value;
  }

  // handle radio toggling
  let radioElementBrothers = document.getElementsByName(radioElement.name); // including our radioElement itself
  Array.from(radioElementBrothers).forEach((someRadioElement) => {
    someRadioElement.onchange = () => {handleRadioToggling(radioElement, inputElement)};
  })
}


function validateForm() {
  // This function deals with validation of the form fields
  let isFormValid = true;
  tabElements = document.getElementsByClassName("tab");
  requiredElements = tabElements[currentTab].querySelectorAll("[required]");
  // A loop that checks every input field in the current tab:
  for (let i = 0; i < requiredElements.length; i++) {
    // If a field is empty...
    if (requiredElements[i].value === "") {
      // add an "invalid" class to the field:
      requiredElements[i].className += " invalid";
      // remove class after required element (input) is being written to
      requiredElements[i].addEventListener('keydown',() => requiredElements[i].className = requiredElements[i].className.replace(' invalid',''), {once: true});
      // and set the current valid status to false:
      isFormValid = false;
    }
  }
  return isFormValid; // return the valid status
}

/* warn for user refresh / leave page */
window.onbeforeunload = function() {
  if (!hasUserSubmitted) {
    return "";
  }
};

let hasUserSubmitted = false;
let currentTab = 0; // Current tab is set to be the first tab (0)
window.addEventListener('load', () => {
showTab(currentTab);
handleRadioButtonInputBoxCorrelation("missing-ventolin-epipen-type-missing-other-type", "other-inhaler-type-input-box");
});



