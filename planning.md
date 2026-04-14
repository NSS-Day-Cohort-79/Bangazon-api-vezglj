# Bangazon Ticket Priority Plan

## Overview

| Sprint | Days | Focus |
|--------|------|-------|
| **Sprint 1** | Days 1–5 | Fix all critical bugs + start learning spikes |
| **Sprint 2** | Days 6–10 | Write tests + build core features |
| **Sprint 3** | Days 11–15 | Dependent features + UI fixes + reports (stretch) |

> **How to read this plan:** Tickets are grouped into waves by dependency order. Within each sprint, different team members can work on different tickets at the same time. You do not have to finish every ticket — the waves and sprints tell you what matters most.

---

## Sprint 1 — Days 1–5
### Goal: Get the app working. Nothing else can be built on top of broken code.

---

### Day 1 — Team Setup + Learning Spikes

Before anyone writes a single line of code, spend Day 1 getting oriented. This is not wasted time — it prevents confusion and duplicate work later.

**Whole team:**
- [ ] Clone both repos and confirm they run locally (`./seed_data.sh` → `python manage.py runserver` and `npm run dev`)
- [ ] Log in with a test user and poke around the app to see what's broken
- [ ] Read through `planning.md` together and assign Wave 1 bugs (see assignments below)

**Dedicated research tickets — assign to 1 person each:**

| Ticket # | Title | Notes |
|----------|-------|-------|
| **#1** | Learning Spike: Introduction to TypeScript | Work through the linked resources. Goal: understand what TypeScript is and why it's used. You'll apply it in Sprint 2+. |
| **#2** | Learning Spike: TanStack Query | Work through the linked resources. Goal: understand what it is and demo a simple example to the team by end of Sprint 1. |

> **Tip:** The person on #1 and the person on #2 should share what they learned at the start of Day 2 (a 10-minute standup demo). The rest of the team needs this context.

---

### Days 2–5 — Fix All Critical Bugs (Wave 1)

These 7 bugs break the most fundamental parts of the app. Work on them in parallel — each person takes a bug (or pair of bugs) and owns it to completion.

| Ticket # | Title | What's broken | Est. Days |
|----------|-------|--------------|-----------|
| **#5** | Bug: Same user profile always returned | The API ignores the auth token and always returns the same user's data to everyone — profile, cart, orders are all wrong until this is fixed | 1–2 days |
| **#6** | Bug: Division by zero error on products | `/products` crashes with a 500 error when a product has no ratings yet — the average rating calculation tries to divide by zero | 1 day |
| **#4** | Bug: Products keep getting added to the last, closed order | After completing an order, new cart items get added to the old completed order instead of starting a fresh one | 1–2 days |
| **#3** | Bug: Cart resource has duplicate line items | `/profile/cart` returns both `lineitems` and `line_items` keys — the `line_items` key needs to be removed | half a day |
| **#8** | Bug: Can't remove an item from the cart | DELETE to `/lineitems/:id` is not deleting the item | 1 day |
| **#10** | Bug: All payment types are being returned | `/paymenttypes` returns every user's payment methods instead of just the logged-in user's | 1 day |
| **#9** | Bug: Payment type info is incorrect | Expiration dates on payment types are showing the wrong value | half a day |

**Suggested team split for Days 2–5:**

| Person | Tickets | Notes |
|--------|---------|-------|
| Dev 1 | #5 | Most impactful bug — touches auth/profile logic |
| Dev 2 | #6 + #9 | Both are in the products/payments views, smaller fixes |
| Dev 3 | #4 + #3 | Both are cart/order logic, they're related |
| Dev 4 | #8 + #10 | Both are delete/filter operations |
| Dev 5 | #1 or #2 spike + help where needed | Finish the learning spike, then pair with whoever is stuck |

> **Note for beginners:** It is totally normal if a bug takes longer than expected. If you're stuck for more than 2 hours, ask a teammate or instructor. Do not spin alone.

---

## Sprint 2 — Days 6–10
### Goal: Confirm the fixes work with tests, then build the core features everything else depends on.

---

### Days 6–7 — Write Tests (Wave 3)

Now that the Wave 1 bugs are fixed, write tests that prove they're fixed and will stay fixed. These tests live in the `tests/` folder.

| Ticket # | Title | File to edit | Est. Days |
|----------|-------|-------------|-----------|
| **#21** | TEST: Delete product | `tests/product.py` | half a day |
| **#22** | TEST: Product can be rated; assert avg_rating exists | `tests/product.py` | half a day |
| **#20** | TEST: Delete payment type | `tests/payments.py` | half a day |
| **#18** | TEST: Complete order by adding payment type | `tests/order.py` | 1 day |
| **#19** | TEST: New line item is not added to closed order | `tests/order.py` | 1 day |

> **Tip:** Look at the existing tests in `tests/product.py` and `tests/order.py` for examples. Each test follows the same pattern: create a user, log in, make a request, assert the response is correct.

---

### Days 7–10 — Core Features (Wave 4)

These three features are the foundation for everything in Sprint 3. Get them done before the sprint ends.

| Ticket # | Title | What to build | Est. Days |
|----------|-------|--------------|-----------|
| **#14** | Feature: Increase max price to $17,500 | Change the price validator in `bangazonapi/models/product.py` from 10000 to 17500. This is literally one number. Do this first. | 1 hour |
| **#23** | Feature: Users can create a store | Add a POST endpoint so users can create a store (store name + description). This is the most important feature of Sprint 2 — everything store-related depends on it. | 2 days |
| **#24** | Feature: Sellers should have a Store view | After #23 is done, build the "My Store" view that shows a seller's active products and sold products. Needs #23 to exist first. | 1–2 days |

> **Suggested split:** Two people pair on #23 together (it's the hardest), one person handles #14 + starts #24 solo once #23 is merged.

---

### Sprint 2 Stretch — Start Wave 5 If Time Allows

If your team finishes Wave 4 with time to spare in Sprint 2, start these. They're independent enough to pick up early:

| Ticket # | Title | Est. Days |
|----------|-------|-----------|
| **#17** | Feature: Users can like/dislike products | 1 day |
| **#15** | Feature: Get products by location (`?location=`) | half a day |
| **#7** | Bug: Incorrect result for minimum products sold (`?number_sold=`) | half a day |

---

## Sprint 3 — Days 11–15
### Goal: Finish dependent features, fix frontend bugs, and complete reports as stretch goals.

---

### Days 11–12 — Dependent Features (Wave 5)

These features all require Sprint 1 bugs and Sprint 2 features to be done first.

| Ticket # | Title | Depends on | Est. Days |
|----------|-------|------------|-----------|
| **#17** | Feature: Users can like/dislike products | Wave 1 (products not crashing) | 1 day |
| **#29** | Feature: Add recommended products to user profile | #5 fixed (correct profile returned) | 1–2 days |
| **#16** | Feature: Users can favorite a store | #23 (stores must exist) | 1 day |
| **#12** | Feature: Get products over a specified price (`?min_price=`) | #14 (max price updated) | half a day |
| **#11** | Feature: Initial product view — 5 most recent per category | Wave 1 (products working) | 1–2 days |
| **#15** | Feature: Get products by location (`?location=`) | Wave 1 | half a day |
| **#7** | Bug: Incorrect result for minimum products sold | Wave 1 | half a day |

> **Skip any of these already done during Sprint 2 stretch time.**

---

### Days 12–14 — Frontend + Cart/Order Bug Fixes (Wave 6)

These are mostly frontend fixes that require the backend bugs from Sprint 1 to already be resolved.

| Ticket # | Title | Depends on | Est. Days |
|----------|-------|------------|-----------|
| **#34** | Bug: Cannot remove items from cart (frontend) | #8 fixed in Sprint 1 | half a day |
| **#33** | Bug: Completing an order doesn't work (frontend) | #4, #9, #10 fixed in Sprint 1 | 1–2 days |
| **#35** | Bug: Past orders not displaying | #33 working | 1 day |
| **#32** | Feature: Delete all items in cart | Wave 1 cart bugs fixed | 1 day |
| **#30** | Feature: Filter products by category | #11 (categories display correctly) | half a day |
| **#31** | Feature: Filter products by price | #12 (`?min_price=` working) | half a day |

---

### Days 14–15 — Reports (Wave 7, Stretch Goals)

These are HTML reports built with Django templates. They're lower priority — only tackle them if your team has finished the above and has time left. If you run out of time, that's okay.

| Ticket # | Title | Depends on | Est. Days |
|----------|-------|------------|-----------|
| **#36** | Feature: List of stores with items currently listed | #23, #24 done | 1 day |
| **#26** | REPORT: Inexpensive products (≤ $999) | Independent | half a day |
| **#25** | REPORT: Expensive products (≥ $1,000) | #14 done | half a day |
| **#13** | REPORT: Incomplete orders | Wave 1 done | half a day |
| **#27** | REPORT: Completed orders | #33 working | half a day |
| **#28** | REPORT: Favorited sellers by customer | #16 done | half a day |

> **Tip on reports:** Django templates are new to most beginners. The first one (#26 inexpensive products) will take longer than expected as you learn the pattern. Once you've done one, the rest go faster since they all follow the same structure.

---

## Full Sprint Summary

### Sprint 1 (Days 1–5)
```
Day 1   — Setup, assign tickets, start learning spikes (#1, #2)
Days 2–5 — Fix bugs: #5, #6, #4, #3, #8, #10, #9
```

### Sprint 2 (Days 6–10)
```
Days 6–7  — Write tests: #21, #22, #20, #18, #19
Day 7     — Quick win: #14 (one-line price fix)
Days 7–10 — Build stores: #23, #24
Stretch   — Start early: #17, #15, #7
```

### Sprint 3 (Days 11–15)
```
Days 11–12 — Dependent features: #17, #29, #16, #12, #11, #15, #7
Days 12–14 — Frontend fixes: #34, #33, #35, #32, #30, #31
Days 14–15 — Reports (stretch): #36, #26, #25, #13, #27, #28
```

---

## Dependency Map

```
Wave 1 Bugs (#3, #4, #5, #6, #8, #9, #10)  ← Sprint 1
  ├──> Wave 2 Learning Spikes (#1, #2)       ← Sprint 1 in parallel
  └──> Wave 3 Tests (#18, #19, #20, #21, #22) ← Sprint 2
       └──> Wave 4 Core Features (#14, #23, #24) ← Sprint 2
            └──> Wave 5 Features (#7, #11, #12, #15, #16, #17, #29) ← Sprint 3
                 └──> Wave 6 UI + Cart Flow (#30, #31, #32, #33, #34, #35) ← Sprint 3
                      └──> Wave 7 Reports (#13, #25, #26, #27, #28, #36) ← Sprint 3 stretch
```

---

## Team Tips for Beginners

- **Daily standup:** Start each day with a 10-minute check-in. Each person answers: *What did I finish? What am I working on today? Am I blocked on anything?*
- **Don't spin alone:** If you've been stuck on the same problem for more than 2 hours, ask someone. Everyone is learning.
- **Commit small:** Make a git commit every time something works — even if it's small. You can always undo a small commit. Losing a whole day of work is painful.
- **Read the error messages:** Django and the browser console give surprisingly helpful error messages. Read the full message before asking for help.
- **Test as you go:** After fixing a bug, manually test it in the browser/Postman before marking the ticket done.
- **One ticket per branch:** Create a new git branch for each ticket (`git checkout -b ticket-5-profile-bug`). This keeps work separate and makes PRs easier to review.