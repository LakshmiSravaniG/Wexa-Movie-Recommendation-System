// Display welcome message
console.log("Movie Recommendation System Loaded");

// Search Validation
function validateSearch() {

    let keyword = document.querySelector("input[name='keyword']").value;

    if(keyword.trim() === ""){

        alert("Please enter a movie name.");

        return false;
    }

    return true;
}

// Confirm recommendation
function recommendMovie(name){

    alert("Generating recommendations based on " + name);

}