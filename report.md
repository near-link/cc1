![](data:image/png;base64...)

**KULLIYYAH OF INFORMATION AND COMMUNICATION TECHNOLOGY**

**DEPARTMENT OF INFORMATION SYSTEMS**

**BIIT 2301 – User Experience Design (UXD)**

**Group Project**

**(Part 3)**

**CafeClick – Campus Cafe & Mart Pre-Order System**

**Section <<X>>**

**Group Name:** PawerPoint

**Group Members**

**Team Leader:**

Danial <<MatricNo>>

**Members:**

Iman <<MatricNo>>

Irfan <<MatricNo>>

Johan <<MatricNo>>

Lecturer's Name:

<<Lecturer's Name>>

Submission Date:

<<Date of Submission>>

---

## Contents

- [1.0 Introduction](#10-introduction)
- [2.0 Prototype Development](#20-prototype-development)
  - [2.1 Visual Design and Explanation](#21-visual-design-and-explanation)
- [3.0 User Testing](#30-user-testing)
  - [3.1 Testing Plan and Procedure](#31-testing-plan-and-procedure)
  - [3.2 Analysis of Results](#32-analysis-of-results)
  - [3.3 Recommendations and Refinements](#33-recommendations-and-refinements)
- [4.0 Summary and Conclusion](#40-summary-and-conclusion)
- [APPENDIX](#appendix)

---

# 1.0 Introduction

CafeClick is a mobile-first web application designed to solve the daily food-ordering frustrations faced by students at the International Islamic University Malaysia (IIUM). Through observation and user interviews conducted during the Empathise phase (Part 1), the team identified that existing delivery platforms such as GrabFood and FoodPanda do not support the small, individual stalls found inside Mahallah cafeterias and campus marts. This gap leaves students without any digital means to check whether a stall is open, whether a specific menu item is still available, or how long the current queue is.

The core problems identified are:

1. **Lack of support for small campus stalls** – Major apps only list official merchants and ignore individual Mahallah cafe stalls and local marts.
2. **No information on item availability** – Students walk to a stall or mart only to discover that the item they want is sold out.
3. **No real-time open/closed status** – Stalls may close unexpectedly for prayer times (e.g., Maghrib) or other reasons, but students have no way of knowing in advance.
4. **No queue status** – Students cannot gauge how busy a stall is before committing to walk there, often resulting in long wait times that make them late for class.

Based on the user persona "Ridhwan" — a time-crunched 2nd-year student with back-to-back lectures — and the user journey map developed in Part 2, the project addresses these pain points with two key solutions:

- **Solution 1: The Real-Time Stall Dashboard** – Providing live open/closed status, queue-level indicators, and item availability so students can make informed decisions before leaving their Mahallah.
- **Solution 2: QR & Pickup Notification** – Enabling students to pre-order and pay via the app, then receive a notification and present a QR code when the food is ready for pickup, eliminating wait times and ensuring order integrity.

These solutions were selected for their high impact on student productivity, low barrier to entry (no delivery logistics required), and feasibility for small vendors (operable from a standard mobile phone with no specialised hardware).

The prototype was developed as an interactive, high-fidelity HTML/CSS/JavaScript web application designed in a mobile-first approach, simulating a full end-to-end ordering flow from login to order collection.

---

# 2.0 Prototype Development

The CafeClick prototype was built as a collection of interconnected HTML pages styled with Tailwind CSS and using a Material Design 3 (M3) dark theme colour palette. The prototype is fully interactive — users can register, log in, browse locations, view menus, customise orders, check out, track order status in real time, and leave reviews. A separate staff-facing dashboard allows vendors to manage stall status, view incoming orders, update the menu, and scan customer QR codes for pickup verification.

The design follows a mobile-first approach using a 390px-wide layout to simulate an iPhone-sized screen, and includes PWA meta tags for full-screen behaviour when added to a home screen.

---

## 2.1 Visual Design and Explanation

### Screen 1: Login Screen

*Figure 2.1: Login Screen – The entry point for user authentication*

**Purpose:** The entry point to the application. It authenticates users and routes them to the appropriate interface based on their role (customer → location selection; staff → staff dashboard).

**How it functions:** Users enter their IIUM email, matric number, or staff number along with their password. The system validates credentials against locally stored user data. Upon successful authentication, customers are directed to the location selection screen, while staff members are directed to the staff dashboard. The form includes a loading spinner animation during the sign-in process to provide visual feedback.

**Key design decisions:**
- A clean, centred layout with a gradient-purple icon establishes the brand identity immediately.
- Input fields use the M3 dark surface colour with subtle border highlights on focus.
- Demo credentials are displayed at the bottom for testing convenience.

---

### Screen 2: Registration Screen

*Figure 2.2: Registration Screen – New user account creation form*

**Purpose:** Allows new users to create a CafeClick account.

**How it functions:** The form collects full name, IIUM email, matric/staff number, password, and password confirmation. Client-side validation checks for empty fields, password match, and minimum password length. Upon successful registration, a success screen with a checkmark animation is shown before auto-redirecting to the login page.

**Key design decisions:**
- Inline error messages appear in a red-toned container that is consistent with the M3 error colour palette.
- The success screen uses a green checkmark icon to provide clear positive feedback.

---

### Screen 3: Location Selection Screen

*Figure 2.3: Location Selection Screen – Outlet selection with live status, queue, and distance indicators*

**Purpose:** Allows students to select which Mahallah cafe or campus mart they want to order from. This is the first screen a customer sees after login and directly addresses the "uncertainty" problem.

**How it functions:** The screen displays a scrollable list of all available campus outlets — both cafes (indicated by a map-pin icon) and marts (indicated by a store icon). Each outlet card shows:
- **Open/Closed status** — colour-coded green badge for open, grey for closed.
- **Live queue level** — 🟢 Low, 🟡 Medium, or 🔴 High.
- **Distance** — the approximate distance from the student's current location in kilometres, also colour-coded for quick reading.

A search bar at the top lets users filter outlets by name. Tapping on an outlet stores the selection and navigates to the home screen.

**Islamic/Ethical element:** The real-time status system respects prayer-time closures. Outlets that close for Maghrib or other prayers are clearly displayed as "Closed," preventing students from making wasted trips and respecting the vendor's right to observe prayer.

---

### Screen 4: Home Screen

*Figure 2.4: Home Screen – Main hub with categories, popular items, and full menu grid*

**Purpose:** The main hub of the customer experience. It displays the selected outlet's menu, promotions, and provides navigation to other sections of the app.

**How it functions:** The home screen is contextually dynamic — it adapts based on whether the selected outlet is a cafe or a mart:
- **For cafes:** Categories include Rice 🍚, Noodles 🍜, Western 🍔, and Drinks 🥤.
- **For marts:** Categories switch to Snacks 🍿, Drinks 🥤, Instant 🍜, and Essentials ✏️.

The screen is divided into three sections:
1. **Welcome Banner** — A gradient card displaying the outlet name and today's special offer.
2. **Categories** — An emoji-based filter grid that lets users filter the menu by category.
3. **Popular Now / All Menu** — Lists of menu items with images, names, and prices.

A persistent bottom navigation bar provides tabs for Home, Menu, Cart, and Profile. If an active order exists, a floating widget appears above the nav bar showing the current order status with a tap-to-track affordance.

---

### Screen 5: Menu Customisation Screen

*Figure 2.5: Menu Customisation Screen – Item detail with quantity, add-ons, and spicy level selectors*

**Purpose:** Allows users to customise their selected food item before adding it to the cart.

**How it functions:** When a user taps on a menu item from the home screen, this bottom-sheet-style overlay appears with:
- A large image of the item and its base price.
- **Quantity selector** — Plus/minus buttons with a minimum of 1.
- **Add-ons** (cafe items only) — A toggleable "Add Egg (+RM 1.00)" option with a checkbox-style indicator.
- **Spicy Level** (rice/noodle items only) — Three options: Mild 🌶️, Medium 🌶️🌶️, Hot 🌶️🌶️🌶️.

The "Add to Cart" button at the bottom updates dynamically to reflect the total price including all customisations.

**Context-awareness:** When browsing a Mart, the Add-ons and Spicy Level sections are hidden entirely, since mart items (e.g., packaged snacks, stationery) do not have these customisation options.

---

### Screen 6: Cart & Checkout Screen

*Figure 2.6: Cart & Checkout Screen – Order review, payment method, and order summary*

**Purpose:** Displays the user's selected items, allows payment method selection, and initiates the order.

**How it functions:** The cart tab shows:
1. **Pickup Location** — A highlighted card confirming the selected outlet.
2. **Order Items** — Each item with its image, customisations (e.g., "• Add Egg", "• mild spicy"), quantity, and calculated price. Items can be removed via the ✕ button.
3. **Payment Method** — Two radio-style options: "Online Banking / QR" (default) and "Cash on Pickup."
4. **Order Summary** — Subtotal, service fee (RM 0.50), and total.
5. **Place Order** button — Disabled when the cart is empty, enabled with the total price when items are present.

Upon placing an order, a loading spinner with "Processing Payment..." text appears. After a simulated payment delay, the order is saved, the cart is cleared, and the user is navigated to the tracking screen.

---

### Screen 7: Order Tracking Screen

*Figure 2.7: Order Tracking Screen – Three-step progress tracker with geofencing and QR code*

**Purpose:** Provides real-time order status tracking from placement to pickup, including a geofencing-based proximity feature and QR code generation.

**How it functions:** The tracking screen uses a three-step progress indicator:
1. **Order Sent** ✅ — Immediately complete upon arrival.
2. **Preparing** ⏳ — Shows an animated progress bar, estimated time ("10-15 minutes"), and a pulsing clock icon.
3. **Ready for Pickup** 📦 — The header changes to "Order Ready!" with a package-check icon.

**Geofencing:** Once the order is "Ready," a proximity alert appears. The system simulates the student walking towards the outlet. Once within 500m, the alert turns green with "✓ Within pickup range" and reveals the "I'm Here – Show QR Code" button.

**QR Code Pickup:** Tapping the button opens a full-screen modal displaying a QR code and a text-based verification code (e.g., `PICKUP-9560-1781346598123`). Staff scan this code to verify the correct customer.

**Islamic/Ethical elements:**
- **'Adl (Fairness):** The digital queue is strictly first-come, first-served. Orders go straight to the kitchen dashboard, and nobody can cut the line.
- **Hifz al-Mal (Protection of Wealth):** The QR code acts as a digital check to ensure that the exact person who paid collects their food, protecting the student's money (mal) and fulfilling the trust (amanah).

---

### Screen 8: Review Screen

*Figure 2.8: Review Screen – Post-order star rating and feedback form*

**Purpose:** Collects post-order feedback from the user to improve service quality.

**How it functions:** After collecting their order, students are presented with:
- An order summary showing all items from the completed order.
- A **5-star rating component** with interactive hover effects and descriptive labels (Poor → Excellent).
- An **optional text feedback area** for detailed comments.
- A "Submit Review" button (requires a rating) and a "Skip for now" option.

Upon submission, a "Thank You!" success screen appears before redirecting back to the home screen.

---

### Screen 9: Staff Dashboard

*Figure 2.9: Staff Dashboard – Outlet status toggle, QR scanner button, and order queue*

**Purpose:** The primary interface for cafe/mart staff to manage their outlet in real time.

**How it functions:** The dashboard provides:
1. **Outlet Status Toggle** — A switch to set the stall as Open or Closed. When open, a green "✓ Accepting new orders" badge is displayed.
2. **QR Code Scanner** — A prominent gradient button that navigates to the scanner screen for verifying customer pickups.
3. **Order Queue** — A live list of incoming orders with order number, customer name, itemised details, payment method, total, and action buttons ("Mark Ready" → "Mark Collected").
4. **Menu Management** — Staff can toggle item availability, edit names and prices inline, delete items, and add new items.
5. **Today's Summary** — Total orders and revenue at a glance.

---

### Screen 10: QR Scanner Screen

*Figure 2.10: QR Scanner Screen – Camera viewfinder with scanning frame and manual code entry*

**Purpose:** Allows staff to scan a customer's QR code to verify and complete the pickup.

**How it functions:** The screen presents:
- A simulated camera view with an animated scanning frame (corner brackets and a sweeping scan line).
- A "Simulate Scan (Demo)" button for prototype testing.
- An "Enter code manually" option that reveals a text input for the verification code.
- Upon successful scan/verification, a bouncing green checkmark animation confirms "Scan Successful!" and auto-returns to the staff dashboard.

---

### Navigation Flow

The complete user flow across all screens:

```
Login → Location Selection → Home (Browse Menu)
                                    ↓
                        Menu Customisation → Cart & Checkout
                                                   ↓
                                          Order Tracking (with QR)
                                                   ↓
                                             Review → Home

Staff Login → Staff Dashboard (Toggle Status, View Queue, Manage Menu)
                     ↓
              QR Scanner → Dashboard
```

---

# 3.0 User Testing

## 3.1 Testing Plan and Procedure

### Testing Methodology

The usability testing was conducted with **3 users** who are IIUM students — the primary target audience for CafeClick. Each session was structured as follows:

1. **Pre-test briefing:** The participant was introduced to CafeClick's concept without detailed instructions on how to use it.
2. **Task-based testing:** Each participant was asked to complete a set of specific tasks using the interactive prototype.
3. **Post-test questionnaire:** A 5-question Likert-scale questionnaire (1–5) was administered.
4. **Short feedback interview:** Two open-ended questions were asked to capture qualitative insights.
5. **Observation:** The facilitator observed the participant's behaviour, noting any hesitations, confusion, or errors.

### Participants

| No. | Name | Description |
|-----|------|-------------|
| 1 | Shaifful | IIUM student, regular user of campus cafes |
| 2 | Ridhwan | IIUM student, frequent campus cafe visitor with back-to-back schedule |
| 3 | Shahab | IIUM student, uses campus marts regularly |

### Tasks Given to Users

1. **Log in** to the app using the demo credentials.
2. **Select a Mahallah cafe** and browse the menu.
3. **Add a food item** to the cart with customisations (add egg, choose spicy level).
4. **Proceed to checkout** and place the order.
5. **Track the order** and observe the status updates.
6. **Show the QR code** when the order is marked as ready.
7. **Submit a review** after completing the order.

### Testing Methods

- **Questionnaire:** A standardised 5-point Likert scale questionnaire.
- **Interview:** "What do you like most about the prototype?" and "What part of the app should we improve?"
- **Observation:** Notes on user behaviour, navigation patterns, hesitations, and points of confusion.

### Recording

The testing sessions were recorded. *(Link to testing video: <<Insert Link>>)*

---

## 3.2 Analysis of Results

### Questionnaire Results

| Question | Shaifful | Ridhwan | Shahab | Average |
|----------|----------|---------|--------|---------|
| 1. It was easy to find the food I wanted from the menu | 5/5 | 5/5 | 5/5 | **5.00** |
| 2. Adding food to the cart and checking out was simple | 4/5 | 5/5 | 5/5 | **4.67** |
| 3. The live order status was easy to understand | 4/5 | 4/5 | 5/5 | **4.33** |
| 4. The QR code pickup feature is useful and clear | 4/5 | 4/5 | 5/5 | **4.33** |
| 5. Overall, I am satisfied with this app | 5/5 | 5/5 | 5/5 | **5.00** |
| **Average per user** | **4.40** | **4.60** | **5.00** | **4.67** |

**Overall average score: 4.67 / 5.00 (93.4%)**

### Key Findings

- **Menu discoverability** scored a perfect 5.00, confirming the category-based filtering with emoji icons made it very easy for users to find items.
- **Cart and checkout simplicity** scored 4.67. Shaifful gave it a 4, suggesting minor friction in the checkout flow.
- **Order status clarity** and **QR pickup usefulness** both scored 4.33, suggesting the order progress visualisation and QR workflow could be made slightly clearer.
- **Overall satisfaction** was a perfect 5.00 across all three users.

### Qualitative Feedback (Interview)

| Student | What do you like most? | What should be improved? |
|---------|----------------------|--------------------------|
| **Shaifful** | "I like that I can track my food from my room. No more waiting in long lines at the cafe." | "You should put categories like Drinks and Rice at the top of the menu so I don't have to scroll so much." |
| **Ridhwan** | "The QR code feature is very cool. It makes picking up the food feel fast and safe." | "Maybe make the cart button a little bit bigger." |
| **Shahab** | "I really like that it shows when the cafe is closed for Maghrib. Very helpful." | "It is already good, but maybe add a sound notification when the food is ready." |

### Observation Notes

1. **All three users** completed the end-to-end flow without requiring assistance, demonstrating intuitive navigation.
2. **Shaifful** scrolled past the categories section and went straight to "All Menu," suggesting the categories need more visual prominence or a sticky position.
3. **Ridhwan** initially hesitated when looking for the cart icon in the bottom navigation, indicating it should be more visually distinct.
4. **Shahab** navigated the fastest and specifically appreciated the "Closed" status for Mahallah Uthman during prayer times.
5. **All users** were impressed by the order tracking animation and geofencing proximity feature.
6. **Two users** (Shaifful and Ridhwan) mentioned a sound or vibration notification when food is ready would be beneficial.

---

## 3.3 Recommendations and Refinements

Based on the feedback collected, the following refinements were identified:

| # | User Issue / Feedback | Source | Refinement |
|---|----------------------|--------|------------|
| 1 | Categories should be more prominent at the top of the menu to reduce scrolling. | Shaifful (Interview) | **Implemented:** Categories are now rendered as a sticky filter bar at the top. Users can tap a category to instantly filter the menu. |
| 2 | The cart button should be bigger or more visually distinct. | Ridhwan (Interview) | **Planned:** Increase the cart icon size in the bottom navigation and add a more prominent badge counter with a bounce animation when items are added. |
| 3 | Add a sound notification when the food is ready. | Shahab (Interview), Shaifful (Observation) | **Planned:** Integrate the Web Audio API or Notification API to play an audible alert when the order status transitions to "Ready for Pickup." |
| 4 | Order tracking progress could be slightly clearer. | Questionnaire (Avg: 4.33) | **Implemented:** Added a linear progress bar with percentage animation during the "Preparing" phase, along with estimated time text ("10-15 minutes"). |
| 5 | QR code workflow could be more self-explanatory. | Questionnaire (Avg: 4.33) | **Implemented:** Added descriptive text beneath the QR code and explicit geofencing messages ("Get within 500m to enable pickup" → "✓ Within pickup range"). |

---

# 4.0 Summary and Conclusion

### Design Process Recap

The CafeClick project followed a structured UX design process across three phases:

- **Part 1 (Empathise):** Through observation and user interviews, the team identified four core problems: lack of support for small stalls, no item availability, no real-time status, and no queue visibility. An empathy map was created capturing what students say, do, think, and feel.
- **Part 2 (Define & Ideate):** A user persona (Ridhwan) and user journey map were developed. Six solutions were brainstormed, and two were selected: a Real-Time Stall Dashboard and a QR & Pickup Notification system.
- **Part 3 (Prototype & Test):** A high-fidelity interactive prototype was built with 10 interconnected screens covering both customer and staff workflows. Usability testing with 3 IIUM students yielded an overall satisfaction score of **4.67/5.00 (93.4%)**.

### What Was Successful

1. **End-to-end usability:** All three test users completed the full ordering flow without assistance, validating the navigation architecture.
2. **Menu discoverability:** The category-based filtering system achieved a perfect 5/5 score.
3. **Real-time status concept:** The open/closed status, queue-level indicators, and order tracking were universally praised.
4. **QR pickup verification:** Described as "very cool" and "fast and safe," confirming it addresses the trust (amanah) concern.
5. **Islamic values integration:** 'Adl (fairness) through the FIFO digital queue and Hifz al-Mal (protection of wealth) through QR-verified pickups were well-received and organically embedded.

### What Could Be Improved

1. **Notification system:** The prototype currently lacks audio/push notifications.
2. **Cart visibility:** The bottom navigation cart icon could be more prominent.
3. **Category persistence:** The category filter could be made sticky to reduce scrolling.
4. **Actual geolocation:** The current geofencing uses simulated distance; integration with the Geolocation API would make it functional.

### Potential Impact

If deployed at IIUM, CafeClick could:
- **Reduce student wait times** by enabling pre-ordering and scheduled pickups.
- **Eliminate wasted trips** by providing real-time stall status and item availability.
- **Support small campus vendors** excluded from major delivery platforms.
- **Promote fairness and trust** through Islamic value-integrated features.

### Future Plans

1. **Backend integration** with a real database (e.g., Firebase or Supabase) for persistent, multi-user data.
2. **Payment gateway** integration with Malaysian gateways (e.g., FPX, Touch 'n Go eWallet).
3. **Push notifications** via the Notifications API and service workers.
4. **Vendor onboarding** with a self-registration flow for new stall owners.
5. **Analytics dashboard** providing vendors with sales data and peak-hour insights.
6. **Cross-platform deployment** as a PWA or native app using Flutter.

---

# APPENDIX

### A. Usability Questionnaire

| # | Question | Scale |
|---|----------|-------|
| 1 | It was easy to find the food I wanted from the menu. | 1 (Strongly Disagree) – 5 (Strongly Agree) |
| 2 | Adding food to the cart and checking out was simple. | 1 – 5 |
| 3 | The live order status was easy to understand. | 1 – 5 |
| 4 | The QR code pickup feature is useful and clear. | 1 – 5 |
| 5 | Overall, I am satisfied with this app. | 1 – 5 |

### B. Interview Questions

1. What do you like most about the prototype?
2. What part of the app should we improve?

### C. Screen Inventory

| # | Screen | File | Purpose |
|---|--------|------|---------|
| 1 | Login | `login.html` | User authentication |
| 2 | Register | `register.html` | New user registration |
| 3 | Location Selection | `location.html` | Outlet selection with live status |
| 4 | Home | `home.html` | Menu browsing with categories |
| 5 | Menu Customisation | `menu.html` | Item add-ons and quantity |
| 6 | Cart & Checkout | `home.html?tab=cart` | Order review and payment |
| 7 | Order Tracking | `tracking.html` | Real-time order status and geofencing |
| 8 | Review | `review.html` | Post-order feedback |
| 9 | Staff Dashboard | `staff.html` | Vendor management interface |
| 10 | QR Scanner | `scanner.html` | Pickup verification |

### D. Links

- **Figma Mockup:** <<Insert Figma Link>>
- **Testing Recording:** <<Insert Recording Link>>
- **Live Prototype:** <<Insert Hosted URL or instructions>>

### E. Observation Notes

| User | Task | Observed Behaviour | Notes |
|------|------|--------------------|-------|
| Shaifful | Browse menu | Scrolled past categories directly to "All Menu" grid | Categories need more visual prominence |
| Ridhwan | Find cart | Hesitated before finding the cart icon in bottom nav | Cart icon needs to be more visually distinct |
| Shahab | Full flow | Completed all tasks fastest, no hesitation | Praised the prayer-time closure status feature |
