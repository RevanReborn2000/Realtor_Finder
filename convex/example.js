// convex/exampleFunction.js

// An example Convex function to fetch data
export default async function exampleFunction({ db }, args) {
    const items = await db.query("your_table_name").collect();
    return items;
  }
  