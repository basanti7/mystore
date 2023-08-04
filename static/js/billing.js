
// js code for modal

// end of js code for modal
function addPurchase() {
    let product_name_el = document.getElementById('product_name');
    let product_price_el = document.getElementById('product_price');
    let product_quantity_el = document.getElementById('product_quantity');

    // validation 
    if (product_name_el.value.trim() === "") {
        alert("You must enter product name to save.");
        return;
    }
    if (product_price_el.value.trim() === "") {
        alert("Price should not be empty or zero.");
        return;
    }
    if (product_quantity_el.value.trim() === "") {
        alert("Please enter at least one quantity.");
        return;
    }

    let purchase = {
        serial: 1,
        product: product_name_el.value,
        price: parseFloat(product_price_el.value),
        quantity: parseFloat(product_quantity_el.value)
    };
    purchase.total = purchase.price * purchase.quantity;

    // Find a <table> element with id="myTable":
    let table = document.getElementById("purchase_table");
    let number_of_rows = table.rows.length;

    console.log(number_of_rows);

    // Create an empty <tr> element and add it to the 1st position of the table:
    let row = table.insertRow(number_of_rows);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    let sl_cell = row.insertCell(0);
    sl_cell.innerHTML = number_of_rows;

    let name_cell = row.insertCell(1);
    name_cell.innerHTML = purchase.product;

    let price_cell = row.insertCell(2);
    price_cell.innerHTML = purchase.price;

    let quantity_cell = row.insertCell(3);
    quantity_cell.innerHTML = purchase.quantity;
    let total_cell = row.insertCell(4);
    total_cell.innerHTML = purchase.total;

    product_name_el.value = "";
    product_price_el.value = "";
    product_quantity_el.value = "";

}


console.log(purchase);

function clicked() {
    alert('clicked!');
    //some code
}
document.onkeydown = function (e) {
    var keyCode = e.keyCode;
    if (keyCode == 90) {
        clicked();
    }
};






// Array to store the list of products
const productList = [];

// Function to dynamically add a product to the list
function addProduct() {
    const productName = prompt("Enter the product name:");
    const productPrice = parseFloat(prompt("Enter the product price:"));

    if (!productName || isNaN(productPrice)) {
        alert("Invalid input. Please try again.");
        return;
    }

    // Create the product object
    const product = {
        name: productName,
        price: productPrice
    };

    // Add the product to the list
    productList.push(product);

    // Update the product list displayed on the page
    const productListElement = document.getElementById('productList');
    const productListItem = document.createElement('li');
    productListItem.textContent = `${productName} - $${productPrice.toFixed(2)}`;
    productListElement.appendChild(productListItem);

    // Update the hidden input field with the updated list of products
    document.getElementById('products').value = JSON.stringify(productList);
}
