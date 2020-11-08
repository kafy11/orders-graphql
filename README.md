Small graphQL project made with Python using Flask, Graphene and SQLite. I made it with docker to make it easy to run in any computer.

## Getting Started 

To run the project, first you need to have Docker installed, then you just need to clone it and run the command bellow to start the server: 

```
docker-compose up
```

After starting it, you can open [http://localhost:5000/graphql](http://localhost:5000/graphql) to run some queries. 

## Available Mutations

### Creating a product

```
mutation{
  createProduct(name: "Product 1",price: 10.00){
    product{
      name
    }
  }
}
```

### Creating an order

```
mutation{
  createOrder(productId: 1,qty: 1){
    order{
      qty
    }
  }
}
```

### Updating a product

```
mutation{
  updateProduct(productId: 1, name: 'New name', price: 2.0){
    product{
      name
    }
  }
}
```

### Updating an order

```
mutation{
  updateOrder(orderId: 1, productId: 2, qty: 2){
    order{
      qty
    }
  }
}
```

### Deleting a product

```
mutation{
  deleteProduct(productId: 1){
    ok
  }
}
```

### Deleting an order

```
mutation{
  deleteOrder(orderId: 1){
    ok
  }
}
```

## Available Queries

### Fetching all products

```
{
  allRowsProduct{
    edges{
      node{
        name
      }
    }
  }
}
```

### Fetching all orders

```
{
  allRowsOrder{
    edges{
      node{
        qty
        product{
          name
        }
      }
    }
  }
}
```