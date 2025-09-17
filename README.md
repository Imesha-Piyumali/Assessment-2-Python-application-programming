Case Study 1 — Campus Café Checkout
Scenario. Build a simple point-of-sale console to add items to a cart and print a receipt.

Learning goals
Use a dict for prices, a list as a cart, a set for unique categories
Practice while menus, for loops, floats, Booleans, and functions
Requirements
Menu (dict). Provide ≥6 items with prices and a category (e.g., drink/food).
Looping menu (while). 1) Show menu 2) Add item 3) View cart 4) Checkout 5) Exit.
Receipt. Show line items, subtotal, tax (10%), and total. Ask for student discount (5%).
Functions (≥4). Suggested: show_menu(), add_item(cart), view_cart(cart), checkout(cart).
Stretch (optional. will give you extra marks if needed)
Quantities (e.g., “2x muffin”).
Show unique categories using a set.
Apply a simple meal deal if both food+drink present.
Case Study 2 — Smart Classroom Monitor
Scenario. Monitor a classroom: check-ins, equipment status, and temperature logs.

Learning goals
Combine Booleans, ints/floats/strings, sets, lists, tuples, and dicts
Use if, for/while, and functions
Requirements
Room state (dict). Track: {"projector_on": bool, "capacity": int, "topic": str}
Attendance (set). Add/remove student names; show count vs capacity.
Temperature log (list of floats). Add readings; compute (min, max, avg) in a helper function returning a tuple.
Alerts (if). Over capacity → “ROOM FULL”; out-of-range temp (<16 or >28) → warning; topic set but projector off at exit → reminder.
Menu (while) & Functions (≥5). Suggested: toggle_projector, set_topic, add_student, remove_student, add_temp, stats, report.

Case Study 3 — A Boolean Circuit Equivalence
Scenario. Given a Boolean circuit, work out its Python equivalent code.

Learning goals
Translate a logic problem into its Python code equivalent.
Propose a suitable solution for the logic given using Python-based code.
Requirements
From the Boolean circuits given, obtain the corresponding Boolean expression (one for each circuit a) and b). Be sure showing EACH step marked as a) to j) in both circuits.
Create a code in Python that simulates the behavior of each circuit. That is, your code should accept inputs A, B, and C, and print out the corresponding outputs X and Y.
Write the truth tables for each circuit and test that your circuits behave as expected.
Check that both circuits are equivalent. To do this, use your truth tables in step 3 above.
