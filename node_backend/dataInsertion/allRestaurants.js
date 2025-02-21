import mongoose from "mongoose";
import connectDb from "../config/db.js";
import dotenv from "dotenv";
import AllRestaurantsModal from "../modals/home/allRestaurants.js";
import { allRestaurantsTable } from "../dummyData/allRestaurantsTable.js";
dotenv.config();

// Connect to MongoDB
connectDb();

// Create a default admin user ID (you should replace this with a real admin ID)
const defaultAdminId = new mongoose.Types.ObjectId();

// Add adminUserId to each restaurant
const restaurantsWithAdmin = allRestaurantsTable.map((restaurant) => ({
  ...restaurant,
  adminUserId: defaultAdminId,
}));

// Insert data
AllRestaurantsModal.insertMany(restaurantsWithAdmin)
  .then(() => {
    console.log("Data inserted successfully");
    mongoose.connection.close();
  })
  .catch((error) => {
    console.error("Error inserting data:", error);
    mongoose.connection.close();
  });
