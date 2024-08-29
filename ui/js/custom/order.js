var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';
var productPrices = {};
var Data
document.addEventListener('DOMContentLoaded', function () {
    // Json data by api call for order table
    fetch(productListApiUrl)
        .then(response => response.json())
        .then(data => {
            productPrices = {0:"0.0"};
            if (data) {
                Data = data
            }
        });
});

// const dropdown = document.getElementById("dropdownProduct")
// updates price on click on select el
document.querySelector("body").addEventListener('click', (e) => {
    if (e.target.id === "dropdownProduct") {
    var item = e.target.closest(".product-item");

        const currOption = item.querySelector("#dropdownProduct").value
        const price = item.querySelector("#product_price")
        const currprice = productPrices[currOption]
        price.value = currprice
        calculateQtyValue(e); 
    }
})

function calculateValue() {
    var total = 0;
    var productItems = document.querySelectorAll(".product-item");

    productItems.forEach(function(item) {
        var qty = parseFloat(item.querySelector('.product-qty').value);
        var price = parseFloat(item.querySelector('#product_price').value);
        var itemTotal = price * qty;
        item.querySelector('#item_total').value = itemTotal.toFixed(2);
        total += itemTotal;
    });

    document.getElementById("product_grand_total").value = total.toFixed(2);
}
function calculateQtyValue(el) {
    var total = 0;
    var item = el.target.closest(".product-item");

        var qty = parseFloat(item.querySelector('.product-qty').value);
        var price = parseFloat(item.querySelector('#product_price').value);
        var itemTotal = price * qty;
        item.querySelector('#item_total').value = itemTotal.toFixed(2);
        total += itemTotal;
    calcTotal()
}

function calcTotal(){
    let total =0;
    
    const totalfields = document.querySelectorAll("#item_total");
    totalfields.forEach((el)=>{
        
        console.log(parseFloat(el.value))
    total = total + parseFloat(el.value)
    })
    const grandTotal = document.querySelector("#product_grand_total")
    grandTotal.value = total
}

document.getElementById("addMoreButton").addEventListener("click", function () {

    const producItem = document.createElement("div")
    producItem.className = 'row product-item'
    let options = '<option value="0">--Select--</option>';
    Data.forEach(product => {
        options += `<option value="${product.product_id}">${product.name}</option>`;
        productPrices[product.product_id] = product.price_per_unit;
    });

    const innerhtml = `       
                    <div class="col-sm-12">
                        <div class="box-info full p-3 mb-3 mt-0">
                            <div class="col-sm-4 selectContainer">
                                <select id="dropdownProduct"  name="product" class="form-control cart-product" style="max-width: 250px">${options}</select>
                            </div>
                            <div class="col-sm-3">
                                <input id="product_price" name="product_price" class="product-price" value="0.0"></input>
                            </div>
                            <div class="col-sm-2">
                                <input name="qty" type="number" min="1" placeholder="" class="form-control product-qty" value="1" style="max-width: 100px">
                            </div>
                            <div class="col-sm-3">
                                <input id="item_total" name="item_total"  value="0" class="product-total"></input><span> Rs</span>
                                <button class="btn btn-sm btn-danger pull-right remove-row" type="button">Remove</button>
                            </div>
                        </div>
                    </div>`
    // newRow.classList.add("row", "product-item");
    // newRow.innerHTML = row;
        
    producItem.innerHTML = innerhtml
    const container = document.querySelector(".product-box")
    container.appendChild(producItem);

    document.querySelectorAll(".product-qty").forEach(function(element) {
        element.addEventListener("change", function(el) {
            calculateQtyValue(el); 
        });
    });
   
    

    // Assuming you want to fetch data from a single product item
function fetchProductData(productItem) {
    const productId = productItem.querySelector('#dropdownProduct').value;
    const productPrice = productItem.querySelector('#product_price').value;
    const quantity = productItem.querySelector('.product-qty').value;
    const itemTotal = productItem.querySelector('#item_total').value;

    return {
        productId: productId,
        productPrice: productPrice,
        quantity: quantity,
        itemTotal: itemTotal
    };
}

// Example usage
document.querySelectorAll('.product-item').forEach(item => {
    const productData = fetchProductData(item);
    console.log(productData);
});


});


document.addEventListener("click", function(event) {
    if (event.target && event.target.matches(".remove-row")) {
        var row = event.target.closest('.row');
        if (row) {
            row.remove();
            calculateValue();
        }
    }
});
// debugger
// document.getElementById("saveOrder").addEventListener("click", function() {
//     // Get form data
//     var formData = new FormData(document.querySelector('.selectContainer'));
    
//     // Initialize request payload
//     var requestPayload = {
//         customer_name: null,
//         grand_total: null,
//         order_details: []
//     };

//     // Process each form data entry
//     formData.forEach(function(value, key) {
//         if (key === 'customerName') {
//             requestPayload.customer_name = value;
//         } else if (key === 'product_grand_total') {
//             requestPayload.grand_total = value;
//         } else if (key === 'product') {
//             requestPayload.order_details.push({
//                 product_id: value,
//                 quantity: null,
//                 total_price: null
//             });
//         } else if (key === 'qty') {
//             var lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
//             if (lastElement) {
//                 lastElement.quantity = value;
//             }
//         } else if (key === 'item_total') {
//             var lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
//             if (lastElement) {
//                 lastElement.total_price = value;
//             }
//         }
//     });
// });