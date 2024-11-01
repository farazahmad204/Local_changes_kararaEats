document.addEventListener("DOMContentLoaded", function() {
    

    // Get all anchor tags
    const links = document.getElementsByTagName("a");

    // Current URL for comparison
    const currentUrl = window.location.href;

    // Log the menu object
    console.log("Menu object is ", menu);

        console.log("menu.classList");
        // Loop through each link
        for (let link of links) {
            // Check if the link's href matches the current URL
            if (link.href === currentUrl) {

                if (! (link.classList.contains("navbar-brand")))
            {
                link.classList.add('active'); // Add active class to the link
            }
                
            }
        }
    
});



function showMenu(menuName) {
    const menus = document.querySelectorAll('.menu-section');
    const buttons = document.querySelectorAll('.tab-button');

    menus.forEach(menu => {
        menu.style.display = 'none';
    });

    buttons.forEach(button => {
        button.classList.remove('active');
    });

    document.getElementById(menuName).style.display = 'block';
    const activeButton = Array.from(buttons).find(button => button.textContent.includes(menuName));
    activeButton.classList.add('active');
}



function saveQuantitiesToLocalStorage(quantities) {
    const values = {};
    quantities.forEach((input, index) => {
        values[index] = input.value;
    });
    localStorage.setItem('quantities', JSON.stringify(values));
}

function loadQuantitiesFromLocalStorage() {
    const quantities = JSON.parse(localStorage.getItem('quantities'));
    console.log("quantities",quantities);
    if (quantities) {
        Object.keys(quantities).forEach(key => {
            const input = document.querySelector(`.item-quantity:nth-of-type(${parseInt(key) + 1})`);
            if (input) {
                input.value = quantities[key];
                console.log("input.value",input.value);
            }
        });
    }
}