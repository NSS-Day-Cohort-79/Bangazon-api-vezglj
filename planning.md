Bangazon Ticket Priority Plan
How to Read This Plan
Tickets are grouped into "waves." A wave must be largely complete before starting the next, because later waves depend on earlier ones being stable. Within each wave, tickets can be worked in parallel by different team members.

WAVE 1 — Fix Critical Bugs First
These bugs break the most fundamental parts of the app. Nothing can be properly tested or built until these are fixed. Start here.

#	Ticket	Why it must go first
#5	Bug: Same user profile always returned	Every feature that shows user-specific data (cart, orders, profile, favorites, recommendations) is wrong until this is fixed. The API ignores the auth token and returns the same person's data to everyone.
#6	Bug: Division by zero error on products	The /products endpoint completely crashes with a 500 error. Nothing involving products works until this is fixed. Caused by the average rating calculation dividing by zero when no ratings exist.
#4	Bug: Products keep getting added to the last, closed order	After a user completes an order, new items go into the old completed order instead of a new cart. The cart is fundamentally broken until this is fixed.
#3	Bug: Cart resource has duplicate line items	The /profile/cart response has two redundant keys (lineitems and line_items). The line_items key needs to be removed. This confuses the frontend.
#8	Bug: Can't remove an item from the cart (backend)	DELETE to /lineitems/:id is not working. Removing items from the cart is impossible until this is fixed.
#10	Bug: All payment types are being returned	The /paymenttypes endpoint returns every payment type in the database, not just the logged-in user's. Checkout shows the wrong (or other users') payment methods.
#9	Bug: Payment type info is incorrect	Expiration dates on payment types are wrong. Users see incorrect data at checkout.
WAVE 2 — Learning Spikes (Do Alongside Wave 1)
These are not coding tasks — they are research assignments. Team members not working on Wave 1 bugs should tackle these now so the whole team has the knowledge needed for later waves.

#	Ticket	Why now
#1	Learning Spike: Introduction to TypeScript	TypeScript knowledge will be needed when refactoring or adding new features. Start learning now so you're ready to apply it in Wave 4+.
#2	Learning Spike: TanStack Query	TanStack Query will replace the current fetch() + useEffect pattern. Understanding it now prepares you to refactor state management as you build features.
WAVE 3 — Write Tests for Fixed Functionality
Once Wave 1 bugs are fixed, write tests to confirm the fixes actually work and prevent regressions. These tests also cover existing features that have no tests yet.

#	Ticket	Depends on
#18	TEST: Complete order by adding payment type	Needs #4 and #9/#10 fixed so cart + payment work correctly
#19	TEST: New line item is not added to closed order	Needs #4 fixed — test verifies the bug stays fixed
#20	TEST: Delete payment type	Write after #10 is fixed (ensures user's own types are deletable)
#21	TEST: Delete product	Can be written now — tests soft-delete behavior
#22	TEST: Product can be rated; assert avg_rating exists	Needs #6 fixed (division by zero bug was in the rating calc)
WAVE 4 — Core Features That Unlock Others
These features are building blocks that other tickets depend on. Complete them before moving to Wave 5.

#	Ticket	Why it must go before others
#14	Feature: Increase max price to $17,500	A one-line change in the model validator. Needed before the expensive products report (#25) makes sense, and before sellers can list high-value items.
#23	Feature: Users can create a store	The Store model must exist and be creatable before any other store features (Store view, favorites, store listing) can be built.
#24	Feature: Sellers should have a Store view	Depends on #23. Shows a seller's active listings and sold items. Needed before the public store list (#36) makes sense.
WAVE 5 — Dependent Features
These all require Wave 4 to be done, or depend on other Wave 5 items in a clear order.

#	Ticket	Depends on
#17	Feature: Users can like/dislike products	Wave 1 (products must work). Adds like/unlike endpoints + liked products list to profile.
#29	Feature: Add recommended products to user profile	Wave 1 (#5 fixed so correct profile is returned). Adds the "Recommend" button + recipient's profile section.
#16	Feature: Users can favorite a store	Needs #23 (stores must exist). POST to /profile/favoritesellers with {"store_id": n}.
#15	Feature: Get products by location	Wave 1 (products must not crash). Adds ?location= query param using Django's __contains filter.
#12	Feature: Get products over a specified price	Needs #14 first (so max price is correct). Adds ?min_price= query param.
#7	Bug: Incorrect result for minimum products sold	Fix the ?number_sold= filter so it returns products with AT LEAST that many sold, not an incorrect result.
#11	Feature: Initial product view — 5 most recent per category	Needs Wave 1 (products working). When no filters are applied, show the 5 newest products per category with category headers.
WAVE 6 — Filter UI + Cart/Order Flow Features
These require Wave 5 features to exist first and wrap up the core shopping experience.

#	Ticket	Depends on
#30	Feature: Filter products by category	Needs #11 (categories must display). Fix the filter dropdown to show real categories instead of dummy data.
#31	Feature: Filter products by price	Needs #12 (min_price backend param must exist). Wires up the Minimum Price UI field to the API.
#32	Feature: Delete all items in cart	Needs Wave 1 cart bugs fixed. Adds a "Delete Order" button that clears the whole cart.
#33	Bug: Completing an order doesn't work (frontend)	Needs Wave 1 (#4, #9, #10 fixed). The full checkout flow — pick payment → confirm → cart clears → appears in My Orders.
#34	Bug: Cannot remove items from cart (frontend)	Needs #8 fixed (backend DELETE must work). Wire up the trash icon to call the correct endpoint.
#35	Bug: Past orders not displaying	Needs #33 (orders must be completable). Orders table rows are created but empty — fix the data binding.
WAVE 7 — Reports + Store Listing
These are lower-priority reporting features and a final store display feature. None are blocking anything else — do these last.

#	Ticket	Depends on
#36	Feature: List of stores with items currently listed	Needs #23 and #24 (stores must exist and have products). Shows store name, description, seller name, item count, and product list.
#13	REPORT: Incomplete orders	Needs Wave 1 (orders must work). HTML report at /reports/orders?status=incomplete — shows Order ID, customer name, total cost.
#26	REPORT: Inexpensive products	Independent. HTML report at /reports/inexpensiveproducts — all products ≤ $999.
#25	REPORT: Expensive products	Needs #14 (so $17,500 items exist). HTML report at /reports/expensiveproducts — all products ≥ $1,000.
#27	REPORT: Completed orders	Needs #33 (orders must be completable). HTML report at /reports/orders?status=complete — Order ID, customer, total, payment type.
#28	REPORT: Favorited sellers by customer	Needs #16 (favorites must exist). HTML report at /reports/favoritesellers?customer=n — customer name + bulleted list of favorited sellers.
Dependency Map (Visual Summary)
Wave 1 Bugs (#3, #4, #5, #6, #8, #9, #10)
  └──> Wave 2 Learning Spikes (#1, #2) ← do in parallel
  └──> Wave 3 Tests (#18, #19, #20, #21, #22)
       └──> Wave 4 Core Features (#14, #23, #24)
            └──> Wave 5 Features (#7, #11, #12, #15, #16, #17, #29)
                 └──> Wave 6 UI + Cart Flow (#30, #31, #32, #33, #34, #35)
                      └──> Wave 7 Reports (#13, #25, #26, #27, #28, #36)
Quick Assign Suggestions (Team of 5)
Since you have 5 people, here's how you could split Wave 1 immediately:

Person	Tickets
Dev 1	#5 (profile bug) + #10 (payment types filter)
Dev 2	#6 (division by zero) + #9 (payment expiration)
Dev 3	#4 (closed order bug) + #3 (duplicate line items)
Dev 4	#8 (remove from cart) + begin reading #1 (TypeScript spike)
Dev 5	#2 (TanStack Query spike) — research & demo to team