
// js code for modal

// end of js code for modal

const purchase_list = [];
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
    // Find a <table> element with id="myTable":
    let table = document.getElementById("purchase_table");
    let number_of_rows = table.rows.length;

    let purchase = {
        serial: number_of_rows,
        item: product_name_el.value,
        price: parseFloat(product_price_el.value),
        quantity: parseFloat(product_quantity_el.value)
    };
    purchase.total = purchase.price * purchase.quantity;

    purchase_list.push(purchase);




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


    document.getElementById('products').value = JSON.stringify(purchase_list);
    // console.log('purchase list')
    // console.log(JSON.stringify(purchase_list))
    console.log(document.getElementById('products').value)
}
function handlePurchaseSubmit() {
    // Find the form by its ID
    const form = document.getElementById('purchase_form');

    // Trigger the form's submit event
    form.submit();
}

// console.log(purchase);

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

function getCurrentDate() {
    // Get the current date
    const currentDate = new Date();

    // Format the date as "YYYY-MM-DD" (required by the input type="date" field)
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0');
    const day = String(currentDate.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;
    // Set the default value of the input field to the current date
    document.getElementById('date_input').value = formattedDate

}
function handleDiscount(){
    let dis = document.getElementById('discount_input').value
    document.getElementById('discount').value = dis
}
function handleDateInput(){
    let changedDate = document.getElementById('date_input').value
    document.getElementById('date').value = changedDate
    console.log('changed date is : ' + changedDate)
}
getCurrentDate()