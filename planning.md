# Bangazon Ticket Priority Plan

## Overview

| Sprint | Days | Focus |
|--------|------|-------|
| **Sprint 1** | Days 1–5 | Fix all critical bugs + complete learning spikes |
| **Sprint 2** | Days 6–10 | Write tests + build core features |
| **Sprint 3** | Days 11–15 | Dependent features + UI fixes + reports (stretch) |

> **How to read this plan:** Tickets are grouped into waves by dependency order. Within each sprint, different team members can work on different tickets at the same time. You do not have to finish every ticket — the waves and sprints tell you what matters most.

---

## Sprint 1 — Days 1–5
### Goal: Get the app working. Nothing else can be built on top of broken code.

---

### Day 1 — Learning Spikes (Whole Team, Split Into Two Groups)

Before writing any code, everyone spends Day 1 on research. Split the team into two groups. Each group works through their spike and prepares a 10-minute summary to present to the rest of the team at the **end of Day 1**.

| Group | Ticket # | Topic | Who |
|-------|----------|-------|-----|
| **Group A** (2–3 people) | **#1** | Learning Spike: Introduction to TypeScript | Devs 1, 2, 3 |
| **Group B** (2 people) | **#2** | Learning Spike: TanStack Query | Devs 4, 5 |

**End of Day 1:** Each group presents their findings to the whole team (~10 min each). Goal is for everyone to have a basic understanding of both topics before Sprint 2+.

> **What to cover in your presentation:**
> - Group A (#1): What is TypeScript? How is it different from JavaScript? Show one example of a typed function.
> - Group B (#2): What is TanStack Query? What problem does it solve? Show one example of a `useQuery` call.

Also use Day 1 to:
- [ ] Clone both repos and confirm they run locally (`./seed_data.sh` → `python manage.py runserver` + `npm run dev`)
- [ ] Log in with a test user and poke around the broken app together so everyone understands what's wrong
- [ ] Assign bug tickets for Days 2–5 (see below)

---

### Days 2–5 — Fix All Critical Bugs (Wave 1)

Everyone codes. Each person owns their bug(s) from start to finish — read the ticket, find the broken code, fix it, and manually test it before marking done.

| Person | Ticket(s) | What's broken | Est. Days |
|--------|-----------|--------------|-----------|
| **Dev 1** | **#5** | Bug: Same user profile always returned — the API ignores the auth token and returns the same user's data to everyone | 1–2 days |
| **Dev 2** | **#6** | Bug: Division by zero error on products — `/products` crashes when a product has no ratings, the average calculation divides by zero | 1 day |
| **Dev 3** | **#4** | Bug: Products keep getting added to the last closed order — new cart items go into a completed order instead of opening a fresh one | 1–2 days |
| **Dev 4** | **#8** + **#3** | Bug: Can't remove item from cart (DELETE not working) + Cart has duplicate `line_items` / `lineitems` keys in response | 1–2 days |
| **Dev 5** | **#10** + **#9** | Bug: All payment types returned (should filter by logged-in user) + Payment expiration dates are incorrect | 1–2 days |

**Notes:**
- `#3` and `#9` are smaller fixes (half a day each) — Dev 4 and Dev 5 may finish early and can help a stuck teammate
- If you finish your bug before Day 5, pick up a test ticket from Wave 3 early (see Sprint 2 below)
- Pair up if you're stuck — two sets of eyes on a bug is always better than one person spinning alone for hours

---

## Sprint 2 — Days 6–10
### Goal: Confirm fixes work with tests, then build the features everything else depends on.

---

### Days 6–7 — Write Tests (Wave 3)

Now that bugs are fixed, write tests that prove the fixes work and will stay fixed. These live in the `tests/` folder. Look at the existing tests as examples — they all follow the same pattern: create a user, log in, make a request, check the response.

| Person | Ticket # | Test to write | File | Est. Days |
|--------|----------|--------------|------|-----------|
| **Dev 1** | **#19** | New line item is NOT added to a closed order | `tests/order.py` | 1 day |
| **Dev 2** | **#22** | Product can be rated; assert `avg_rating` key exists with correct value | `tests/product.py` | 1 day |
| **Dev 3** | **#18** | Complete order by adding a payment type | `tests/order.py` | 1 day |
| **Dev 4** | **#20** | Delete payment type | `tests/payments.py` | half a day |
| **Dev 5** | **#21** | Delete product (verify it no longer appears) | `tests/product.py` | half a day |

> Dev 4 and Dev 5 finish tests early — use the remaining time to start on Wave 4 features below.

---

### Days 7–10 — Core Features (Wave 4)

These three features are the foundation for everything in Sprint 3. #23 is the most important one — stores must exist before any other store-related features can be built.

| Person | Ticket # | What to build | Est. Days |
|--------|----------|--------------|-----------|
| **Dev 1 + Dev 2** (pair) | **#23** | Feature: Users can create a store — add a POST endpoint for store name + description. This unlocks #16, #24, #36. Pair on this one — it's the most complex feature of Sprint 2. | 2 days |
| **Dev 3** | **#24** | Feature: Sellers should have a Store view — "My Store" page showing active listings and sold products. Depends on #23 being merged first. | 1–2 days |
| **Dev 4** | **#14** | Feature: Increase max price from $10,000 to $17,500 — change one number in the model validator. Do this first, it takes 1 hour. Then move on to helping with #23 or starting Wave 5. | 1 hour |
| **Dev 5** | Help with **#23** or start Wave 5 | Once tests (#21) are done, join Dev 1 + Dev 2 on store creation or start an early Wave 5 ticket (#17, #15, or #7) | — |

---

### Sprint 2 Stretch — Start Wave 5 If Time Allows

If anyone finishes their Sprint 2 work early, pick up one of these:

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

All of these require Sprint 1 bugs and Sprint 2 features to be done first. Skip any already completed during Sprint 2 stretch time.

| Person | Ticket # | What to build | Depends on | Est. Days |
|--------|----------|--------------|------------|-----------|
| **Dev 1** | **#29** | Feature: Add recommended products to user profile | #5 fixed (correct profile returned) | 1–2 days |
| **Dev 2** | **#17** | Feature: Users can like/dislike products | Wave 1 bugs fixed | 1 day |
| **Dev 3** | **#16** | Feature: Users can favorite a store | #23 done | 1 day |
| **Dev 4** | **#11** | Feature: Initial product view — 5 most recent items per category | Wave 1 bugs fixed | 1–2 days |
| **Dev 5** | **#12** + **#7** + **#15** | Get products over min price + fix number_sold filter + get products by location | #14 done, Wave 1 bugs fixed | 1–2 days |

---

### Days 12–14 — Frontend + Cart/Order Fixes (Wave 6)

Mostly frontend fixes that require the backend bugs from Sprint 1 to already be resolved.

| Person | Ticket # | What to fix | Depends on | Est. Days |
|--------|----------|------------|------------|-----------|
| **Dev 1** | **#33** | Bug: Completing an order doesn't work (frontend checkout flow) | #4, #9, #10 fixed | 1–2 days |
| **Dev 2** | **#34** + **#35** | Bug: Can't remove cart items (frontend) + Past orders not displaying | #8 fixed, #33 done | 1–2 days |
| **Dev 3** | **#32** | Feature: Delete all items in cart ("Delete Order" button) | Wave 1 cart bugs fixed | 1 day |
| **Dev 4** | **#30** | Feature: Filter products by category (fix dropdown to use real categories) | #11 done | half a day |
| **Dev 5** | **#31** | Feature: Filter products by price (wire up min price UI to API) | #12 done | half a day |

---

### Days 14–15 — Reports (Wave 7, Stretch Goals)

These are HTML reports using Django templates — a new concept for most beginners. Only tackle these if Wave 6 is done. The first one will take the longest as you learn the pattern; the rest go faster.

| Person | Ticket # | Report | Depends on | Est. Days |
|--------|----------|--------|------------|-----------|
| **Dev 1** | **#36** | Feature: List of stores with items currently listed | #23, #24 done | 1 day |
| **Dev 2** | **#26** + **#25** | Inexpensive products report (≤$999) + Expensive products report (≥$1,000) | #14 done | half a day each |
| **Dev 3** | **#13** | REPORT: Incomplete orders | Wave 1 done | half a day |
| **Dev 4** | **#27** | REPORT: Completed orders | #33 working | half a day |
| **Dev 5** | **#28** | REPORT: Favorited sellers by customer | #16 done | half a day |

> Reports are **stretch goals** — if your team runs out of time here, that is okay. Focus on getting Waves 1–6 solid first.

---

## Full Sprint Summary

### Sprint 1 (Days 1–5)
```
Day 1     — All 5 devs: learning spikes in 2 groups (#1 TypeScript, #2 TanStack Query), end-of-day presentations
Days 2–5  — Dev 1: #5 | Dev 2: #6 | Dev 3: #4 | Dev 4: #8+#3 | Dev 5: #10+#9
```

### Sprint 2 (Days 6–10)
```
Days 6–7  — Dev 1: #19 | Dev 2: #22 | Dev 3: #18 | Dev 4: #20 | Dev 5: #21
Days 7–10 — Devs 1+2 pair on #23 | Dev 3: #24 | Dev 4: #14 then help | Dev 5: help #23 or early Wave 5
```

### Sprint 3 (Days 11–15)
```
Days 11–12 — Dev 1: #29 | Dev 2: #17 | Dev 3: #16 | Dev 4: #11 | Dev 5: #12+#7+#15
Days 12–14 — Dev 1: #33 | Dev 2: #34+#35 | Dev 3: #32 | Dev 4: #30 | Dev 5: #31
Days 14–15 — Dev 1: #36 | Dev 2: #26+#25 | Dev 3: #13 | Dev 4: #27 | Dev 5: #28 (all stretch)
```

---

## Dependency Map

```
Wave 1 Bugs (#3, #4, #5, #6, #8, #9, #10)  ← Sprint 1
  ├──> Wave 2 Learning Spikes (#1, #2)       ← Sprint 1 Day 1 (all 5 devs)
  └──> Wave 3 Tests (#18, #19, #20, #21, #22) ← Sprint 2
       └──> Wave 4 Core Features (#14, #23, #24) ← Sprint 2
            └──> Wave 5 Features (#7, #11, #12, #15, #16, #17, #29) ← Sprint 3
                 └──> Wave 6 UI + Cart Flow (#30, #31, #32, #33, #34, #35) ← Sprint 3
                      └──> Wave 7 Reports (#13, #25, #26, #27, #28, #36) ← Sprint 3 stretch
```

---

## Team Tips for Beginners

- **Daily standup:** Start each day with a 10-minute check-in. Each person answers: *What did I finish? What am I working on today? Am I blocked on anything?*
- **Don't spin alone:** If you've been stuck on the same problem for more than 2 hours, ask a teammate. Everyone is learning.
- **Commit small and often:** Make a git commit every time something works — even if it's small. Losing a whole day of work because you didn't commit is painful.
- **Read the error messages:** Django and the browser console give surprisingly helpful error messages. Read the full message before asking for help.
- **Test as you go:** After fixing a bug, manually test it in the browser or Postman before marking the ticket done.
- **One ticket per branch:** Create a new git branch for each ticket (`git checkout -b ticket-5-profile-bug`). This keeps work separate and makes code reviews easier.
- **Ask for a code review:** Before merging a branch, have at least one teammate read through your changes. Two sets of eyes catch bugs the author misses.
