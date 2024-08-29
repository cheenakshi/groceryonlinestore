var productListApiUrl = "http://localhost:5000/getProducts"
var uomListApiUrl = "http://127.0.0.1:5000/getUOM"
var saveProductListApiUrl = "http://127.0.0.1:5000/insertProduct"
var deleteProductListApiUrl = "http://127.0.0.1:5000/deleteProduct"
document.addEventListener('DOMContentLoaded', function () {
    // JSON data by API call
    fetch(productListApiUrl)
        .then(response => response.json())
        .then(response => {
            if (response) {
                let table = '';
                response.forEach(product => {
                    table += `<tr data-id="${product.product_id}" data-name="${product.name}" data-unit="${product.uom_id}" data-price="${product.price_per_unit}">
                                <td>${product.name}</td>
                                <td>${product.uom_name}</td>
                                <td>${product.price_per_unit}</td>
                                <td><span class="btn btn-xs btn-danger delete-product" id="actionDeleteBtn">Delete</span></td>
                              </tr>`;
                });
                document.querySelector("table tbody").innerHTML = table;
            }
        
        });
    const productModal = document.getElementById('productModal');

});

// document.addEventListener('click', function(event) {
//     if (event.target.classList.contains('delete-product')) {
//         const tr = event.target.closest('tr');
//         const data = {
//             "product_id": Number(tr.dataset.id)
//         };
//         console.log(data); 
//         const isDelete = confirm(`Are you sure to delete ${tr.dataset.name} item?`);
//         if (isDelete) {
//             fetch(deleteProductListApiUrl, {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     // 'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
//                 },
//                 body:JSON.stringify(
//                     data
//                 ),
//                 // body: data
//             })
//             .then(response => response.json())
//             // .then(data => {
//             //     // Handle response here
//             // });
//         }
//     }
// });
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('delete-product')) {
        const tr = event.target.closest('tr');
        const productId = Number(tr.dataset.id);
        const productName = tr.dataset.name;

        // Confirm deletion
        const isDelete = confirm(`Are you sure you want to delete ${productName}?`);
        if (isDelete) {
            // Construct the payload
            const data = {
                product_id: productId
            };
            console.log(JSON.stringify(data));
            

            fetch(deleteProductListApiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // Uncomment if CSRF protection is used
                    // 'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(responseData => {
                // Handle the response data
                console.log('Delete successful:', responseData);
                // Optionally remove the row or update the UI
                tr.remove(); // Example: Remove the row from the DOM
            })
            .catch(error => {
                // Handle any errors
                console.error('Error:', error);
            });
        }
    }
});





// MODAL JS(ADD PRODUCT)
const addProductBtn = document.getElementById('addProductBtn');
const productModal = document.getElementById('productModal');
const uoms = document.getElementById('uoms');
const closeProductModal = document.getElementById('closeProductModal');
const saveProductListBtn = document.getElementById('saveProduct');

closeProductModal.addEventListener('click', () => {
    productModal.style.display = 'none';
}
)

productModal.style.display = 'none'
addProductBtn.addEventListener('click', (e) => {
    e.preventDefault();
    productModal.style.display = productModal.style.display === 'none' ? 'block' : 'none';
    const fetchapi = async () => {
        try {
            const response = await fetch(uomListApiUrl);
            const data = await response.json();
            console.log(data);
            let options = '<option value="">--Select--</option>';
            data.forEach(uom => {
                options += `<option value="${uom.uom_id}">${uom.uom_name}</option>`;
            });
            document.getElementById('uoms').innerHTML = options;
        } catch (error) {
            console.error('Fetch error:', error);
        }
    }
    fetchapi();

})

// Assuming saveProductListBtn is the form element
saveProductListBtn.addEventListener('click', () => {
    // e.preventDefault();

    // Create FormData and requestPayload inside the event listener
    const data = new FormData(document.getElementById('productForm'));
    const requestPayload = {
        product_name: data.get('name'),
        uom_id: data.get('uoms'),
        price_per_unit: data.get('price'),
        category: data.get('category'),
        image_url : data.get('img-link')
    };

    fetch(`${saveProductListApiUrl}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestPayload)
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response data if needed
            console.log('Success:', data);
            location.reload()
        })
        .catch(error => {
            // Handle any errors
            console.error('Error:', error);
        });
});

