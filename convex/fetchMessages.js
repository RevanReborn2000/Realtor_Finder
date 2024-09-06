// convex/fetchMessages.js
import { query } from "./_generated/server";

export default query(async ({ db }) => {
  const messages = await db.query("Sample_Data").collect();
  return messages;
});