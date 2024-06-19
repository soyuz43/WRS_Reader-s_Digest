```dbml
// Users table
Table users {
  id int PK
  username varchar
  password varchar
  email varchar
  // other fields as needed
}

// Book categories table
Table categories {
  id int PK
  name varchar
}

// Books table
Table books {
  id int PK
  title varchar
  author varchar
  isbn varchar
  cover_image_url varchar
  user_id int FK >- users.id
  created_at timestamp
}

// Intersection table for books and categories with timestamp
Table book_categories {
  book_id int FK >- books.id
  category_id int FK >- categories.id
  created_at timestamp
}

// Reviews table
Table reviews {
  id int PK
  book_id int FK >- books.id
  user_id int FK >- users.id
  rating int // numeric rating from 1-10
  comment text
  created_at timestamp
}

// Relationships
Ref: books.user_id > users.id
Ref: book_categories.book_id > books.id
Ref: book_categories.category_id > categories.id
Ref: reviews.book_id > books.id
Ref: reviews.user_id > users.id

```