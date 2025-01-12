# WhatsApp Message Scheduler

This project demonstrates how to schedule and send WhatsApp messages using Python and the Twilio API. Follow the steps below to set up and execute the script.

---

## Description
The **WhatsApp Message Scheduler** is a Python-based tool that allows users to send scheduled WhatsApp messages automatically. By leveraging the Twilio API, this script ensures reliable message delivery at a user-specified date and time. It takes user inputs for recipient details, the message content, and the schedule, calculates the time difference, and sends the message at the exact scheduled time.

This project is ideal for:
- Automating reminders.
- Sending scheduled updates to contacts.
- Experimenting with Python's integration with APIs.

---

## Libraries Used

1. **twilio.rest.Client**:
   - Provides functionality to interact with the Twilio API.
   - Used to send WhatsApp messages through Twilio's messaging service.

2. **datetime**:
   - Used for managing and calculating dates and times.
   - Converts and manipulates user-provided scheduling details.

3. **time**:
   - Allows the program to pause execution until the specified message-sending time.

---

## Code Explanation

### Twilio Account Setup
Before running the code, you need to create a Twilio account and gather the following credentials:

1. **Account SID (`acc_id`)**:
   - Unique identifier for your Twilio account.
   - Found in the Twilio Console dashboard.

2. **Auth Token (`aut_id`)**:
   - Secret key for authenticating API requests.
   - Found in the Twilio Console under your account settings.

3. **Sender Number**:
   - Twilio provides a sandbox WhatsApp number for testing (`+14155238886`).
   - You need to configure your recipient number to interact with this number through the Twilio Console.

### Script Walkthrough

1. **Input Fields**:
   - User inputs:
     - Recipient's full name.
     - WhatsApp number.
     - Message to send.
     - Scheduled time (`HH:MM` format).
     - Scheduled date (`DD/MM/YYYY` format).

2. **Date and Time Parsing**:
   - The `datetime.strptime` function converts user input into a `datetime` object.
   - The current date and time (`curr_datetime`) is retrieved using `datetime.now()`.

3. **Time Delay Calculation**:
   - The difference between the scheduled time and the current time is calculated.
   - If the scheduled time has already passed, the script alerts the user.

4. **Delay Execution**:
   - The script uses `time.sleep(delay)` to pause execution until the scheduled time.

5. **Message Sending**:
   - The `send_whatsapp_message` function sends the WhatsApp message via the Twilio API.
   - Handles errors using a `try-except` block.

6. **Message Parameters**:
   - **Body**: The message text to send.
   - **From**: The Twilio sandbox number (`whatsapp:+14155238886`).
   - **To**: The recipient's WhatsApp number in the format `whatsapp:+<country_code><number>`.

---

## Setting Up Twilio Account

1. **Sign Up**:
   - Go to [Twilio Sign Up](https://www.twilio.com/try-twilio).
   - Create a new account.

2. **Verify Your Number**:
   - Add your phone number to Twilio's WhatsApp sandbox.
   - Follow instructions to send a WhatsApp message to Twilio's sandbox number.

3. **Gather Credentials**:
   - Locate `Account SID` and `Auth Token` in the Twilio Console.

4. **Set Up Messaging Service**:
   - Enable the WhatsApp sandbox in your Twilio account.
   - Use the sandbox number `+14155238886` for testing.

---

## How to Run

1. Install the Twilio library:
   ```bash
   pip install twilio
   ```

2. Save the code in a file (e.g., `whatsapp_scheduler.py`).

3. Run the script:
   ```bash
   python whatsapp_scheduler.py
   ```

4. Enter the required inputs when prompted.

---

## Example Execution

1. **Input**:
   ```
   Enter recipient full name: John Doe
   Enter recipient number: 9876543210
   Enter message: Hello, this is a test message.
   Enter time in HH:MM format: 14:30
   Enter date in DD/MM/YYYY format: 12/01/2025
   ```

2. **Output**:
   ```
   Time left: 3600.0 seconds
   SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

   Here, `SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` is the unique message SID returned by Twilio upon successful delivery.

---

## Notes

- Ensure your recipient's WhatsApp number is verified in the Twilio sandbox.
- Test the script thoroughly before deploying it in production.
- Be cautious with the `Auth Token` as it is a sensitive credential.

---

## License
This project is open-source and available under the MIT License.
