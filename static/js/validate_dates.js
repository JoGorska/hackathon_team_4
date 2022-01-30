/**
 * function testing if the target date has been set for a day in the past or for today
 * https://stackoverflow.com/questions/1531093/how-do-i-get-the-current-date-in-javascript?rq=1
 * 
 */

 var todayDate = new Date().toISOString().slice(0, 10);

function beforeToday () {
  
  if (targetDate.value <= todayDate) {

    return false;

  } else {
    return true;
  }
}

/**
 * Function to test if the target date is further than a month ahead
 * both dates: today and target date are converted to miliseconds from Unix timestamp is the time elapsed since the 1, Jan 1970 00:00:00 UTC,
 * @returns true or false
 */


function monthLater () {
  let todayInMs = new Date().getTime();
  let targetInMs = targetDate.valueAsNumber;
  let monthInMs = 2629800000;
  
  if ((targetInMs-todayInMs) < monthInMs) {
    return false;
  } else {
    return true;

  }
}
/**
 * function to check if the target year is less than a year from Today
 * @returns 
 */

function lessThanAYear () {
  let todayInMs = new Date().getTime();
  let targetInMs = targetDate.valueAsNumber;
  let monthInMs = 2629800000;

  if ((targetInMs-todayInMs > (12 * monthInMs))) {
    return false;

  } else {
    return true;
  }
}

// functions to add or remove classes copied from Felipe Souza Alarcon_mentor, and explained on mentoring meeting 31.07.2021

/**
 * Function to add class
 * @param {*} className 
 * @param {*} targetNode 
 */
 function addClass(className, targetNode) {
    targetNode.classList.add(className);
  }
  
  /**
   * Function to remove class
   * @param {*} className 
   * @param {*} targetNode 
   */
  
  function removeClass(className, targetNode){
    targetNode.classList.remove(className);
  }
  
  /**
   * Function to set attribute
   * @param {*} className 
   * @param {*} targetNode 
   */
  
  function setAtribute(atributeName, atributeValue, targetNode) {
    targetNode.setAttribute(atributeName, atributeValue);
  }
  /**
   * Function to remove attribute
   * @param {*} atributeName 
   * @param {*} atributeValue 
   * @param {*} targetNode 
   */
  function removeAtribute(atributeName, atributeValue, targetNode) {
    targetNode.removeAttribute(atributeName, atributeValue);
  }
  
  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red, input's border is red and red icon with exclamation mark is displayed in input field
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */
  
  function displayErrorValidation(targetNodeInput, targetNodeHelp) {
  
    addClass("is-invalid",targetNodeInput);
    setAtribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("invalid-feedback", targetNodeHelp);
  
  }
  
  /**
   * Function to remove display Error after validation has been passed
   * makes div with help message invisible, input border comes back to standard and icon with exclamation mark disapears
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */
  
  function removeErrorValidation(targetNodeInput, targetNodeHelp) {
  
    removeClass("is-invalid",targetNodeInput);
    removeAtribute("aria-describedby", "name-help", targetNodeInput);
    addClass("my-invisible", targetNodeHelp);
    removeClass("invalid-feedback", targetNodeHelp);
  }


/**
 * Function to show the result of valiation on target date input field
 * checks first if the radio button has been set to target date, than
 * Returns true or false, if false - changes the look of the input field 
 * and displays line of text with detailed information why it failed validation
 * 
 */

 function validateResultTargetDate() {

    if (radioTargetDate.checked) {
  
      if (targetDate.value === "") {
  
        helpTargetDate.innerHTML = "This field is required";
        displayErrorValidation(targetDate, helpTargetDate);
        return(false);
  
      } else if (targetDate.value.length > 10) {
        helpTargetDate.innerHTML = "Date contains too many digits, please check the date";
        displayErrorValidation(targetDate, helpTargetDate);
        return(false);
      
      } else if (!beforeToday()) {
  
        return (false);
      
      } else if (!monthLater()) {
      
        helpTargetDate.innerHTML = "We can only calculate the results for dates further than month ahead";
        displayErrorValidation(targetDate, helpTargetDate);
        return(false);
  
      } else if (!lessThanAYear()) {
      
        helpTargetDate.innerHTML = "Please set your target within 12 months from today, it is good to plan short term goals and revise once they are acheved";
        displayErrorValidation(targetDate, helpTargetDate);
        return(false);
  
      } else {
        
  
        removeErrorValidation(targetDate, helpTargetDate);
        return(true);
  
      }
  
    } else {
  
      removeErrorValidation(targetDate, helpTargetDate);
      return(true);
    }
  }