const exampleCameraData = require('../data/basicdata/examplecameras.cjs');
const { User } = require('../models/user');
const { logMessage, logError } = require('./logger');

/**
 * Add base data to the database, including subscription plans and test cameras.
 * @param {string} userId - The ID of the user for whom the data is added.
 */
const addBaseData = async (userId) => {
    try {
        await addTestCameras(userId);
    } catch (error) {
        console.error(error);
    }
}

/**
 * Add test cameras to the user's cameras list.
 * @param {string} userId - The ID of the user for whom test cameras are added.
 */
const addTestCameras = async (userId) => {
    for (const cameraData of exampleCameraData) {
        const { cameraUrl } = cameraData;
        await addCameraUrl(cameraUrl, userId);
    }
}

/**
 * Add a camera URL to the user's cameras list.
 * @param {string} camera - The camera URL to be added.
 * @param {string} userId - The ID of the user to whom the camera URL is added.
 */
const addCameraUrl = async (camera, userId) => {
    await User.findOneAndUpdate(
        { _id: userId },
        { $addToSet: { cameras: camera } },
        { new: true }
    );
}

/**
 * Add the first two cameras to the user's cameras list.
 * @param {User} user - The user to whom the cameras are added.
 * @param {Express.Request} req - The Express request object.
 */
const addFirstTwoCameras = async (user, req) => {
    // Add logic to add the first two cameras here
}

module.exports = { addBaseData, addFirstTwoCameras };
