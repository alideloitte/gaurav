// script.js


document.addEventListener('DOMContentLoaded', function() {
    var dropdownOptions = document.querySelectorAll('.dropdown-option');
    dropdownOptions.forEach(function(option) {
        option.addEventListener('click', function(event) {
            event.preventDefault();
            var inputId = option.closest('.input-group').querySelector('input').id;
            var inputField = document.getElementById(inputId);
            inputField.value = option.textContent;
            inputField.removeAttribute('placeholder');
            // toggleDropdown(inputId);
        });
    });
});

function fetchCalculateUserSelectedUtilisationBarChart(data){
    fetch('/fetchCalculateUserSelectedUtilisationBarChart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({user_selected_graph_dict: data.user_selected_graph_dict }),
    })
    .then(response => {
        if (response.ok) {
            console.log("response is ok")
            // Create an img element for the bar chart
            const barChartImg = document.createElement('img');
            barChartImg.src = 'static/calculated_suggested_utilisation_bar_chart.png';  // Path to the saved bar chart image
            barChartImg.alt = 'Bar Chart';

            // Display the bar chart image inside right-content-div
            const rightContentDiv = document.querySelector('.user-suggested-utilisation-graph');
            rightContentDiv.innerHTML = '';  // Clear the div
            rightContentDiv.appendChild(barChartImg);  // Append the bar chart image
        } else {
            console.error('Failed to fetch bar chart.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function calculate() {
    // Get the values of all input fields
    const cycle1 = document.getElementById('cycle1Input').value;
    const cycle2 = document.getElementById('cycle2Input').value;
    const cycle3 = document.getElementById('cycle3Input').value;
    const cycle4 = document.getElementById('cycle4Input').value;

    // Check if all fields are filled
    if (cycle1 && cycle2 && cycle3 && cycle4) {
        // Construct an object with selected options
        const selectedOptions = {
            Cycle1: cycle1,
            Cycle2: cycle2,
            Cycle3: cycle3,
            Cycle4: cycle4
        };

        // Send the selected options to the backend
        fetch('/your_backend_endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(selectedOptions)
        })
        .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        if (data.error) {
            alert(data.error); // Display error message if vehicle not found
        } else {
            const divElement = document.querySelector('.user-suggested-utilisation-graph');
            divElement.innerHTML = '';
            // Clear vin-input and hide vin-input and submit button
            console.log(data)
            // Display vehicle details as rounded unclickable fields
            fetchCalculateUserSelectedUtilisationBarChart(data)
            const mainContentDiv = document.querySelector('.main-content');
            mainContentDiv.style.display = 'flex'; // or 'block' if you prefer
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
}


function toggleDropdown(inputId) {
    var dropdown = document.getElementById('dropdown-' + inputId);
    dropdown.classList.toggle('show');
}

function selectOption(option, inputField) {
    alert(option)
    alert(inputField)
    inputField.value = option;
    alert('inputField.value', inputField.value)
    alert('inputField.id', inputField.id)
    toggleDropdown(inputField.id);
}

function fetchComparisionData(data){
    if (data.error) {
        alert(data.error); // Display error message if vehicle not found
    } else {
        const priceByCycleDict = data.price_by_cycle_dict;
        console.log(priceByCycleDict)
        // Update price by cycle values in the HTML
        const priceByCycleDiv = document.getElementById('price-by-cycle-values');
        const revenueValuesDiv = document.getElementById('revenue-values');
        const profitValuesDiv = document.getElementById('profit-values');

        
        let priceByCycleHtmlContent = '';
        // Iterate over each cycle and add content
        for (const cycle in priceByCycleDict) {
            if (priceByCycleDict.hasOwnProperty(cycle)) {
                const cycleData = priceByCycleDict[cycle];
                priceByCycleHtmlContent += `
                    <div class="cycle-values">
                        <p class="cycle-revenue-amount">${cycleData.price_difference}</p>
                        <p class="cycle-revenue-percentage">${cycleData.profit_percentage}</p>
                        <h4>${cycle}</h4>
                    </div>
                `;
            }
        }
        const revenueAmount = data.revenue_dict.revenue_amount;
        const revenuePercentage = data.revenue_dict.revenue_percentage;

        // Create HTML content with customized styling
        const htmlContentRevenue = `
            <p class="profit-amount">${revenueAmount}</p>
            <p class="profit-percentage">${revenuePercentage}</p>
        `;

        // Extract profit values
        const profitAmount = data.profit_dict.profit_amount;
        const profitPercentage = data.profit_dict.profit_percentage;
        //Create HTML content with customized styling
        const htmlContentProfit = `
            <p class="profit-amount">${profitAmount}</p>
            <p class="profit-percentage">${profitPercentage}</p>
        `;

        priceByCycleDiv.innerHTML = priceByCycleHtmlContent;
        revenueValuesDiv.innerHTML = htmlContentRevenue;
        profitValuesDiv.innerHTML = htmlContentProfit;

    }
}
//     fetch('/fetchComparisionData')
//     .then(response => response.json())
//         .then(data => {
//             const profitValuesDiv = document.getElementById('profit-values');
//             const revenueValuesDiv = document.getElementById('revenue-values');

//             // Extract profit values
//             const profitAmount = data.profit_dict.profit_amount;
//             const profitPercentage = data.profit_dict.profit_percentage;
//             const revenueAmount = data.profit_dict.revenue_amount;
//             const revenuePercentage = data.profit_dict.revenue_percentage;
//             const priceByCycleDict = data.price_by_cycle_dict;



//             // Create HTML content with customized styling
//             const htmlContentProfit = `
//                 <p class="profit-amount">${profitAmount}</p>
//                 <p class="profit-percentage">${profitPercentage}</p>
//             `;
//             // Create HTML content with customized styling
//             const htmlContentRevenue = `
//                 <p class="profit-amount">${profitAmount}</p>
//                 <p class="profit-percentage">${profitPercentage}</p>
//             `;

            
//             // Set the HTML content of the div
//             profitValuesDiv.innerHTML = htmlContentProfit;
//             revenueValuesDiv.innerHTML = htmlContentRevenue;
//             // priceByCycleDiv.innerHTML = priceByCycleHtmlContent;


//         })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// function fetchComparisionData_2(){
//     fetch('/fetchComparisionData_2')
//     .then(response => {
//         if (response.ok) {
//             // Create an img element for the bar chart
//             // const barChartImg = document.createElement('img');
//             // barChartImg.src = 'static/comparision_suggested_vs_traditional.png';  // Path to the saved bar chart image
//             // barChartImg.alt = 'Bar Chart';

//             // Display the bar chart image inside right-content-div
//             // const rightContentDiv = document.querySelector('.content-comparision-graph');
//             // rightContentDiv.innerHTML = '';  // Clear the div
//             // rightContentDiv.appendChild(barChartImg);  // Append the bar chart image
//         } else {
//             console.error('Failed to fetch bar chart.');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }
function fetchTraditionalUtilisationBarChart(){
    fetch('/fetchTraditionalUtilisationBarChart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (response.ok) {
            // Create an img element for the bar chart
            const barChartImg = document.createElement('img');
            barChartImg.src = 'static/traditional_utilisation_bar_chart.png';  // Path to the saved bar chart image
            barChartImg.alt = 'Bar Chart';

            // Display the bar chart image inside right-content-div
            const rightContentDiv = document.querySelector('.traditional-utilisation-graph');
            rightContentDiv.innerHTML = '';  // Clear the div
            rightContentDiv.appendChild(barChartImg);  // Append the bar chart image
        } else {
            console.error('Failed to fetch bar chart.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function fetchUserSelectedUtilisationBarChart(data){
    fetch('/fetchUserSelectedUtilisationBarChart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_selected_graph_dict: data.user_selected_graph_dict }),
    })
    .then(response => {
        if (response.ok) {
            // Create an img element for the bar chart
            const barChartImg = document.createElement('img');
            barChartImg.src = 'static/user_suggested_utilisation_bar_chart.png';  // Path to the saved bar chart image
            barChartImg.alt = 'Bar Chart';

            // Display the bar chart image inside right-content-div
            const rightContentDiv = document.querySelector('.user-suggested-utilisation-graph');
            rightContentDiv.innerHTML = '';  // Clear the div
            rightContentDiv.appendChild(barChartImg);  // Append the bar chart image
        } else {
            console.error('Failed to fetch bar chart.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayCompetitorPrice(data) {
    if (data.error) {
        alert(data.error); // Display error message if vehicle not found
    } else {
        const competitorPriceDict = data.competitor_pricing;
        console.log(competitorPriceDict)
        // alert(suggestedPriceDict)
        const cpLabels = document.querySelectorAll('.cp-label'); // Select all elements with class 'cp-label'

        // Loop through the cp-label elements and set their innerHTML from suggested_price_dict
        cpLabels.forEach((label, index) => {
            const cycleKey = `Cycle${index + 1}`;
            console.log(cycleKey)
            if (competitorPriceDict[cycleKey] !== undefined) {
                console.log("competitorPriceDict[cycleKey]",competitorPriceDict[cycleKey])
                label.innerHTML = `$${competitorPriceDict[cycleKey].toFixed(2)}`; // Format to 2 decimal places
            } else {
                label.innerHTML = '$N/A'; // Set to N/A if the cycle key is not found
            }
        });
    }
}
function displayPotentialPrice(data){
    if (data.error) {
        alert(data.error); // Display error message if vehicle not found
    } else {
        const potentialPriceDict = data.potential_price_dict;
        console.log(potentialPriceDict)
        // alert(suggestedPriceDict)
        const spLabels = document.querySelectorAll('.tp-label'); // Select all elements with class 'sp-label'

        // Loop through the sp-label elements and set their innerHTML from suggested_price_dict
        spLabels.forEach((label, index) => {
            const cycleKey = `Cycle${index + 1}`;
            console.log(cycleKey)
            if (potentialPriceDict[cycleKey] !== undefined) {
                console.log("potentialPriceDict[cycleKey]",potentialPriceDict[cycleKey])
                label.innerHTML = `$${potentialPriceDict[cycleKey].toFixed(2)}`; // Format to 2 decimal places
            } else {
                label.innerHTML = '$N/A'; // Set to N/A if the cycle key is not found
            }
        });
    }
}

function displaySuggestedPrice(data) {
    if (data.error) {
        alert(data.error); // Display error message if vehicle not found
    } else {
        const suggestedPriceDict = data.suggested_price_dict;
        console.log(suggestedPriceDict)
        // alert(suggestedPriceDict)
        const spLabels = document.querySelectorAll('.sp-label'); // Select all elements with class 'sp-label'

        // Loop through the sp-label elements and set their innerHTML from suggested_price_dict
        spLabels.forEach((label, index) => {
            const cycleKey = `Cycle${index + 1}`;
            console.log(cycleKey)
            if (suggestedPriceDict[cycleKey] !== undefined) {
                console.log("suggestedPriceDict[cycleKey]",suggestedPriceDict[cycleKey])
                label.innerHTML = `$${suggestedPriceDict[cycleKey].toFixed(2)}`; // Format to 2 decimal places
            } else {
                label.innerHTML = '$N/A'; // Set to N/A if the cycle key is not found
            }
        });
    }
}

function fetchSuggestedUtilisationBarChart(data) {
    fetch('/fetchSuggestedUtilisationBarChart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ graph_data: data.graph_dict }),
    })
    .then(response => {
        if (response.ok) {
            // Create an img element for the bar chart
            const barChartImg = document.createElement('img');
            barChartImg.src = 'static/suggested_utilisation_bar_chart.png';  // Path to the saved bar chart image
            barChartImg.alt = 'Bar Chart';

            // Display the bar chart image inside right-content-div
            const rightContentDiv = document.querySelector('.suggested-utilisation-graph');
            rightContentDiv.innerHTML = '';  // Clear the div
            rightContentDiv.appendChild(barChartImg);  // Append the bar chart image
        } else {
            console.error('Failed to fetch bar chart.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function submitData() {
    const vinInput = document.getElementById('vin-input');
    const submitButton = document.querySelector('.submit-button');
    const vinNumber = vinInput.value.trim();

    // Check if vinNumber is not empty before sending to the backend
    if (vinNumber === '') {
        alert('Please enter a VIN number.');
        return;
    }

    // Send the VIN number to the Python backend using Fetch API
    fetch('/get_vehicle_details', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ vin: vinNumber })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        if (data.error) {
            alert(data.error); // Display error message if vehicle not found
        } else {
            // Clear vin-input and hide vin-input and submit button
            vinInput.value = '';
            vinInput.style.display = 'none';
            submitButton.style.display = 'none';
            console.log(data)
            // Display vehicle details as rounded unclickable fields
            displayResponseFields(data);
            displayRightHeaderFields(data);
            // displayLeftDivFields(data);
            displaySuggestedPrice(data)
            displayCompetitorPrice(data)
            fetchSuggestedUtilisationBarChart(data)
            fetchUserSelectedUtilisationBarChart(data)
            fetchTraditionalUtilisationBarChart()
            displayPotentialPrice(data)
            fetchComparisionData(data)
            // Show the main-content div
            const mainContentDiv = document.querySelector('.main-content');
            mainContentDiv.style.display = 'flex'; // or 'block' if you prefer
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayResponseFields(data) {
    const subHeaderRow = document.querySelector('.sub-header-row');

    // Clear any existing rounded fields
    subHeaderRow.innerHTML = '';

    // Iterate through the first 6 key-value pairs in the vehicle_info object
    const vehicleInfo = data.vehicle_info;
    const keys = Object.keys(vehicleInfo);
    for (let i = 0; i < 6 && i < keys.length; i++) {
        const key = keys[i];
        const value = vehicleInfo[key];

        // Create a rounded field container
        const fieldElement = document.createElement('div');
        fieldElement.className = 'rounded-field';

        // Create separate HTML elements for key and value, applying different styles
        const keyElement = document.createElement('span');
        keyElement.className = 'field-key';
        keyElement.textContent = key + ': ';
        const valueElement = document.createElement('span');
        valueElement.className = 'field-value';
        valueElement.textContent = value;

        // Append key and value elements to the field container
        fieldElement.appendChild(keyElement);
        fieldElement.appendChild(valueElement);

        // Append the field to the sub-header-row
        subHeaderRow.appendChild(fieldElement);
    }

    // Show the sub-header-row
    subHeaderRow.style.display = 'flex';
}

function displayRightHeaderFields(data) {
    const rightHeader = document.querySelector('.right-header');
    const suggestedUtilization = data.suggested_vehicle_lifecycle_utilization;

    // Clear existing content
    rightHeader.innerHTML = '';

    // Append static text
    const staticText = document.createElement('div');
    staticText.className = 'right-header-text';
    staticText.textContent = 'Suggested Vehicle Lifecycle Utilization:';
    rightHeader.appendChild(staticText);

    // Append dynamic rounded fields
    const utilizationKeys = Object.keys(suggestedUtilization);
    for (let i = 0; i < utilizationKeys.length; i++) {
        const key = utilizationKeys[i];
        const value = suggestedUtilization[key];

        // Create a rounded field for each key-value pair
        const fieldElement = document.createElement('div');
        fieldElement.className = 'right-header-rounded-field';
        fieldElement.textContent = `${key}: ${value}`;

        // Append the field to the right header
        rightHeader.appendChild(fieldElement);
    }

    // Show the right header
    rightHeader.style.display = 'flex';
}


// function displayRightHeaderFields(data) {
//     const rightHeader = document.querySelector('.right-header');

//     // Clear any existing rounded fields
//     rightHeader.innerHTML = '';

//     // Create and populate the four rounded fields in the right header
//     const suggestedUtilization = data.suggested_vehicle_lifecycle_utilization;
//     const utilizationKeys = Object.keys(suggestedUtilization);
//     for (let i = 0; i < 4 && i < utilizationKeys.length; i++) {
//         const key = utilizationKeys[i];
//         const value = suggestedUtilization[key];

//         // Create a rounded field for each key-value pair
//         const fieldElement = document.createElement('div');
//         fieldElement.className = 'right-header-rounded-field';
//         fieldElement.textContent = `${key}: ${value}`;

//         // Append the field to the right header
//         rightHeader.appendChild(fieldElement);
//     }

//     // Show the right header
//     rightHeader.style.display = 'flex';
// }


function displayLeftDivFields(data) {
    // const leftDiv = document.querySelector('.left-div');
    const leftresponseContainer = document.getElementById('left-response-container');

    leftresponseContainer.innerHTML = ''; // Clear the left div content
    // Iterate over the data fields and create content for the left div
    for (const field in data) {
        if (data.hasOwnProperty(field)) {
            const fieldValue = data[field];
            const fieldElement = document.createElement('div');
            fieldElement.className = 'left-rounded-field';
            fieldElement.textContent = `${field}: ${fieldValue}`;
            leftresponseContainer.appendChild(fieldElement);
        }
    }
}

