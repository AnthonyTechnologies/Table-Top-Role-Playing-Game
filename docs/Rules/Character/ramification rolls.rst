.. _ramification_rolls:

Ramification Rolls
==================

In [Game Name], rolling dice is commonly used to determine the outcomes of events and actions — **Ramification Rolls**. These rolls are categorized by the scope and nature of the challenge being resolved.

.. _action_rolls:

1. Action Rolls
---------------

**Action Rolls** are the bridge between a character's intent and the narrative reality. While characters constantly perform mundane actions through narration and resource expenditure, a roll is required whenever an outcome is hindered by significant risk, opposition, or external complications.


Action resolution is handled through two primary types of rolls, depending on whether the character is facing a static challenge or a direct opponent.

When to Roll
~~~~~~~~~~~~
The GM should only call for an **Action Roll** when any of the following four criteria are met:

*   **Uncertainty:** The outcome of the action is not guaranteed by the character's skill or the simplicity of the task.
*   **Interesting Failure:** Failure would move the story in an interesting (even if negative) direction. If failure simply halts the game or results in a repetitive "try again" loop, no roll should be made.
*   **Immediate Stakes:** There is an urgent consequence or pressure, such as combat, a ticking clock, or a high-stakes social negotiation.
*   **Direct Opposition:** The character is acting directly against another character or entity.

If a character has ample time, lacks immediate danger, and possesses a relevant **Talent** or **Persona Tag**, the GM should allow the action to succeed automatically with a "Standard Success" outcome.

Selecting Attributes
~~~~~~~~~~~~~~~~~~~~
The power behind an **Action Roll** is determined by the character's **Attributes**. The selection of which Attribute to apply follows a specific priority:

*   **Technique-Defined:** If a character is using a specific **Technique**, the Attribute used is defined by that Technique's description.
*   **GM-Defined:** For actions not covered by a Technique, the GM selects the most narratively appropriate Attribute based on the player's description of their intent.
*   **Persona's Edge:** When a player invokes a **Persona Tag** to gain **Persona's Edge**, they gain the right to suggest an alternate Attribute for the roll. If the player can narratively justify how a quality allows them to approach the task using a different strength (e.g., using **Will** instead of **Endurance** for a feat of endurance), the GM may grant the switch.

In **Contested Rolls**, these rules apply to both the attacker and defender. However, a player may only influence the Attribute used for their own character's roll, never for their opponent.

Types of Action Rolls
~~~~~~~~~~~~~~~~~~~~~
Action resolution is divided into two primary categories, depending on the nature of the challenge:

*   **Resolution Rolls:** Used for tasks against the environment, static obstacles, or the internal limits of a character. (See: :ref:`resolution_rolls`)
*   **Contested Rolls:** Used for actions directly opposed by another active agent, such as a clash of wills or physical combat. (See: :ref:`contested_rolls`)

The calculation of these rolls and the result of the resolution can be influenced by four distinct forces. These modifiers represent the different narrative agents acting upon the character's fate:

*   **Favor & Disfavor:** Represents the influence of the environment and situational circumstances acting for or against the character.
*   **Pushing:** Represents a character's raw effort and immediate focus acting upon the present moment.
*   **Persona's Edge:** Represents the weight of a character's background, Expertise, and Identity acting upon their successes.
*   **Intervention:** Represents meta-narrative agency and the collective will of the group acting upon destiny.

See section :ref:`modifying_ramification_rolls` for the detailed rules and tactical hierarchy of these modifiers.


.. _resolution_rolls:

2. Resolution Roll
~~~~~~~~~~~~~~~~~~

When a character attempts a risky action against the environment, a static obstacle, or their own internal limits, the player must make a **Resolution Roll**.

1. **The Roll:** The player must roll two ten-sided dice (2d10) and sum the results. (For non-player forces, the GM may choose to use a static result of 11 rather than rolling.)
2. **The Modifier:** The player must add the score of their character's most relevant **Attribute** to the dice sum. 
3. **The Result:** The player must compare the final total to the Standard Resolution Brackets to determine the narrative outcome.

.. container:: deemphasized

    **Game Methodology: The Bell Curve**

    Utilizing 2d10 instead of a single flat die creates a mathematical bell curve. Results naturally cluster around the average, making standard outcomes highly predictable. This methodology dictates that a character's static **Attributes** must act as the primary driver of success, significantly reducing random, unearned variance. (See: :ref:`bell_curve_philosophy`)

.. _outcome_brackets:

Resolution Brackets
^^^^^^^^^^^^^^^^^^^

For unopposed actions against the environment or static challenges, the GM sets the Difficulty and resolves all **Resolution Rolls** by comparing the final total to the table below. The numbers for Fumble, Standard, and Perfect represent the **minimum inclusive** total required to achieve that outcome bracket.

+-------------+----------+---------+----------+-------------+
| Difficulty  | Disaster | Fumble  | Standard | Perfect     |
+=============+==========+=========+==========+=============+
| Trivial     | ≤ 4      | 5       | 10       | 15          |
+-------------+----------+---------+----------+-------------+
| Novice      | ≤ 9      | 10      | 15       | 20          |
+-------------+----------+---------+----------+-------------+
| Adept       | ≤ 14     | 15      | 20       | 25          |
+-------------+----------+---------+----------+-------------+
| Master      | ≤ 19     | 20      | 25       | 30          |
+-------------+----------+---------+----------+-------------+
| Grandmaster | ≤ 24     | 25      | 30       | 35          |
+-------------+----------+---------+----------+-------------+

* **Disaster:** The character does not achieve their intended goal. The GM must introduce a severe consequence, inflict damage, or shift the narrative situation significantly against the players. This is a primary trigger for inflicting a negative **Status** (e.g., *Stunned*, *Bleeding*, or *Exposed*).
* **Fumble:** The character achieves their goal, but the GM must introduce a complication, a minor consequence, or a required cost (e.g., spending **Stamina** or **Essence**, or suffering a minor negative **Status** like *Rattled*).
* **Standard:** The character flawlessly achieves their goal without compromise.
* **Perfect:** The character achieves their goal with spectacular efficiency. The GM must grant an unexpected narrative advantage, bonus information, or an expanded positive effect (e.g., granting a positive **Status** like *Inspired* or *Empowered*).

While the difficulty table provides a fast baseline, the GM has the freedom to manually define custom outcome brackets for unique or highly specific situations. By using a player's relevant **Attributes** and the baseline 2d10 average (11) as a reference point, the GM can precisely tailor the tension of a scene. For example, the GM could widen the numerical gap between a Fumble and a Standard success to represent an extraordinarily unpredictable environment, or compress the brackets for a challenge focused purely on binary, pass/fail skill.

.. container:: deemphasized

    **Game Methodology: Attribute-Anchored Brackets**

    GMs can precisely tailor the tension of a scene by anchoring custom brackets to a character's relevant **Attribute** and the mathematical average of 2d10 (11). This ensures that the difficulty of a task is relative to the character's skill, allowing for "fair" or "heroic" challenges that scale with the player. (See: :ref:`anchored_brackets_philosophy`)

Miracles and Catastrophes
^^^^^^^^^^^^^^^^^^^^^^^^^
Regardless of a character's **Attribute** modifiers, the raw dice will dictate absolute extremes:

* **Catastrophe (Natural 2):** If the dice show two 1s, the action will automatically result in a Disaster. 
* **Miracle (Natural 20):** If the dice show two 10s, the action will automatically result in a Perfect success. 

.. container:: deemphasized

    **Game Methodology: The 1% Extremes**

    [Game Name] restricts automatic natural results to a strict 1% probability (rolling exactly a 2 or a 20). Restricting natural failures to 1% prevents the frustrating "slapstick variance" found in traditional 5% systems, ensuring a highly trained expert does not suffer a 5% chance to comically fail at a routine task. The 1% rule guarantees that a catastrophe remains a rare, dramatic edge case for experts, while leaving a tiny window for untrained characters to pull off a miracle. (See: :ref:`outcome_brackets_philosophy`)

.. _contested_rolls:

3. Contested Roll
~~~~~~~~~~~~~~~~~

When a character directly opposes an active, resisting entity with an attack, the GM must call for a **Contested Roll** to determine the outcome and subsequent damage.

1. **The Opposed Rolls:** Both the attacker and the defender must roll two ten-sided dice (2d10) and add their respective relevant **Attribute** modifiers. (For non-player forces, the GM may choose to use a static result of 11 plus the relevant Attribute rather than rolling.)
2. **Calculate the Difference:** The GM must calculate the final numeric difference by subtracting the defender's total from the attacker's total.

3. **The Outcome:** The GM must apply the following brackets based on the numeric difference between the two rolls:

* **Miss (Difference of -10 or lower):** The attacker must completely fail to overcome the opposition. The defender evades or blocks the attack entirely. The GM must apply zero damage to the defender's **Health**.
* **Glance (Difference of -1 to -9):** The attacker must land a partial or grazing strike. The GM must calculate the attack's base damage and divide it in half (rounded up). The GM must then subtract the defender's **Physical Armor** or **Ephemeral Armor** from this halved value before applying the remaining damage to the defender's **Health**.
* **Hit (Difference of 0 to +9):** The attacker must overcome the defender, winning the tie. The GM must calculate the attack's base damage. The GM must then subtract the defender's **Physical Armor** or **Ephemeral Armor** from this value before applying the remaining damage to the defender's **Health**.
* **Critical (Difference of +10 or higher):** The attacker must overwhelmingly defeat the defender, striking a vulnerable point. The GM must calculate the attack's base damage and double it. The GM must then subtract the defender's **Physical Armor** or **Ephemeral Armor** from this doubled value before applying the remaining damage to the defender's **Health**.

Miracles and Catastrophes in Contested Rolls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The raw dice will supersede mathematical differences in Contested Rolls, imposing immediate states based on the roll.

* **Attacker Rolls a Catastrophe (2):** The attack must automatically Miss, regardless of the defender's total.
* **Attacker Rolls a Miracle (20):** The attack must automatically become a Critical Hit, regardless of the defender's total.
* **Defender Rolls a Catastrophe (2):** The defender must automatically suffer a Critical Hit, regardless of the attacker's total.
* **Defender Rolls a Miracle (20):** The defender must automatically evade or block, forcing the attack to Miss, regardless of the attacker's total.

**Conflicting Natural Results:** If both the attacker and defender roll critical states that yield conflicting results, the GM must ignore the automatic natural results. The GM must calculate the **Contested Roll** normally using the standard Difference Brackets.

.. container:: deemphasized

    **Game Methodology: Zero-Centered Differences and The Emergent 5% Critical**

    The Contested Roll brackets are centered precisely around 0. However, 0 is included in the "Hit" bracket, the system intentionally favors the attacker on ties to maintain combat momentum and guarantee **Health** depletion, preventing stagnant wars of attrition. 

    Also, the GM and players can rely on the mathematical difference of +10 to generate combat criticals, rather than raw dice faces. Statistically, if the contested attributes are equal, an attacker will beat a defender by 10 or more roughly 4.85% of the time. This naturally produces the traditional, highly satisfying ~5% critical hit rate during combat encounters without forcing players to memorize arbitrary dice combinations or suffer from an unearned 5% failure rate during narrative roleplay.

    Furthermore, attribute differences can lead to interesting character strategies where players may choose to increase specific attributes to increase their chance to land a critical hit. These implications also apply to Glances and Misses for defending. (See: :ref:`contested_roll_statistics`)

.. _crisis_roll:

4. Crisis Roll
~~~~~~~~~~~~~~

When a character's Health reaches 0, they enter a state of **Incapacitation**. In this dire condition, the standard rules of action and reaction are suspended as the character fights for survival. The **Crisis Roll** represents this struggle—a desperate bridge between life and death.

At the start of their turn, an **Incapacitated** character must make a **Crisis Roll** to determine if they stabilize or succumb to their wounds.

* **Roll:** 2d10
* **Resolution Brackets:**

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Result          | Effect                                                                                                                                              |
+=================+=====================================================================================================================================================+
| **Miracle**     | **20**: The character stabilizes immediately. Their Health is set to 10 (or their max if it is less than 10) and they are no longer Incapacitated.  |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Standard**    | **15-19**: The character is stabilized but remains unconscious. They gain a **Short-term Status** (e.g., *Concussed* or *Rattled*).                 |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Fumble**      | **11-14**: The character gains a **Long-term Status** (Wound) requiring a **Recovery Rest** to heal or a permanent **Minor Trait** (Scar/Limp).     |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Disaster**    | **3-10**: The character's condition worsens. Roll on the **Critical Trauma Chart** (Chance permanent Trait or death).                               |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Catastrophe** | **2**: The character dies.                                                                                                                          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

**Modifying the Crisis Roll**
Characters can influence their fate through their inherent resilience and the manipulation of destiny:

* **Favor & Disfavor:** Depending on the circumstances, a character may gain **Favor** or **Disfavor** on their Crisis Roll, but this should be rare. 
* **Persona's Edge:** A player may invoke a relevant **Persona Tag** (e.g., *Tough as Nails*, *Survivor*) to gain a **Persona Up-Shift** on the Crisis Roll.
* **Intervention:** A player may spend **1 Intervention** to shift the resolution bracket up one, potentially avoiding a **Disaster**.

.. note:: 
   The **Critical Trauma Chart** and specific details on **Recovery Rests** can be found in the forthcoming Advanced Combat rules.

.. _modifying_ramification_rolls:

5. Modifying Ramification Rolls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ramification Rolls can be influenced by external circumstances, internal character effort, or the expenditure of rare narrative resources. The primary methods for modifying a roll include:

* **Favor:** The environment acting for the character (Roll 3d10, keep highest 2).
* **Disfavor:** The environment acting against the character (Roll 3d10, keep lowest 2).
* **Pushing the Roll:** The character’s focus acting upon the present moment.
* **Persona's Edge:** The character's identity acting upon their fate.
* **Intervention:** The group or destiny acting upon the meta-narrative.

However, these modifiers are not always applicable to all Ramification Rolls and rules for when they can be used are detailed in their respective sections. For example, a Crisis Roll cannot be modified by Pushing. 

Favor
^^^^^
Favor represents **The World** acting upon the character’s attempt. When external circumstances or tactical positioning favor a character, the GM may award **Favor**. To resolve a roll with **Favor**, the player must roll **three ten-sided dice (3d10)** and sum the **two highest** results before adding their **Attribute**. 

**Favor** is strictly for situational factors such as superior positioning (high ground), favorable environmental conditions (perfect lighting), or the use of specialized tools. It is never awarded for a character's inherent background or training, which are instead handled by **Persona's Edge**.

Disfavor
^^^^^^^^
Disfavor represents the restrictive force of **The World** acting against the character. When external circumstances or tactical hurdles hinder a character...

**Disfavor** is strictly for situational factors such as poor visibility, unstable terrain, or the lack of proper equipment. Like its positive counterpart, it does not apply to character flaws or narrative compulsions, which are handled through the hindering aspect of **Persona's Edge**.

Pushing the Roll
^^^^^^^^^^^^^^^^
Pushing represents **The Character's Will** acting upon the present moment—the raw effort and immediate resource expenditure required to force a better outcome. After an **Action Roll** is made, the player may choose to "push" their character's limits to achieve a better outcome. To push a roll, the player must spend a resource amount (such as **Stamina** or **Essence** or **Health**) equal to half of their current pool (rounded up). 

Upon paying this cost, the player may reroll the dice and must accept the new result, even if it is worse than the original. An **Action Roll** may only be pushed once.

.. _persona_edge:

Persona's Edge
^^^^^^^^^^^^^^
Persona's Edge represents the character's identity acting upon their successes. A character's narrative background provides a decisive advantage or a significant hurdle depending on the situation. After an **Action Roll** is made, if the player or GM can justify how a relevant **Persona Tag** (Identity, Talent, Compulsion, Trait, Status, Technique, or Item) applies to the task, the result is modified by a **Persona Shift**.

**The Non-Scaling Rule**

Persona's Edge does not scale; it is either applied or it is not. A roll may only benefit from or be hindered by **Persona's Edge** once, regardless of how many relevant tags a character possesses. **Constraint:** If a Persona Tag is required to activate a specific Technique or Trait, neither that tag nor any tag of the same type (e.g., a higher tier of the same skill, as determined by the GM) can be used to grant **Persona's Edge** for the resulting action.

**Standard Persona Shifts**

In unopposed **Resolution Rolls**, the character's own background shifts the outcome:

* **Helping:** If the Persona provides a narrative advantage, the final resolution outcome is shifted **one step up** the ladder (e.g., a Fumble becomes a Standard Success). This move is called a **Persona Up-Shift**.
* **Hindering:** If the Persona introduces a narrative complication or aligns with a character's flaws, the final resolution outcome is shifted **one step down** the ladder (e.g., a Standard Success becomes a Fumble). This move is called a **Persona Down-Shift**.
* **Canceling:** If a roll involves Persona Tags that both help and hinder the resolution, they **cancel each other out completely**. No shift is applied and the Persona's Edge does not go into effect. This rule applies regardless of how many tags are present on either side.

**Contested Persona Shifts**

In **Contested Rolls**, both the attacker and defender may independently apply their Persona's Edge. While the attacker's Edge follows the standard shifts, a defender's Edge has an **inverse effect** on the attacker's final resolution outcome:

* **Defender Helping:** If the defender's Persona provides a defensive advantage, the attacker's final outcome is shifted **one step down** the ladder (e.g., a "Hit" becomes a "Glance").
* **Defender Hindering:** If the defender's Persona introduces a vulnerability or complication, the attacker's final outcome is shifted **one step up** the ladder (e.g., a "Hit" becomes a "Critical").

Intervention
^^^^^^^^^^^^
**Intervention** represents Fate—the authorial agency of the player and the collective will of the group acting upon the meta-narrative when neither the environment (Favor) nor background (Persona's Edge) is enough. Unlike other modifications, **Intervention** can be used to influence the world directly or to aid fellow characters.

* **Narrative Retcon:** A player may spend **1 Intervention** to introduce a minor, favorable detail into the current scene that was not previously established (e.g., finding a useful tool, a convenient distraction, or a hidden passage). This requires GM approval.
* **Narrative Flashback:** A player may spend **1 Intervention** to trigger a brief flashback scene showing their character preparing for the current situation in the past. This allows the character to have a specific item, piece of information, or set-up advantage that was not previously established, provided it is narratively plausible. (e.g., "I made sure to pack a backup lockpick," or "I scouted this guard's routine yesterday.")
* **Team Up-Shift:** A player may spend **1 Intervention** and describe how they assist a teammate during an **Action Roll** to shift the **Action Roll** resolution bracket up one. (Cannot be used to shift an Action Roll down).
* **Intervention Shift:** A player may spend **1 Intervention** to shift their own **Action Roll** resolution bracket either up or down one.
* **Trait & Techniques:** Some **Traits** and **Techniques** may require the expenditure of **Intervention** to activate.

Additionally, only one **Intervention** may be spent per **Action Roll**, so players cannot stack an Intervention Shift with a teammate's Team Up-Shift.

Shift Stacking
^^^^^^^^^^^^^^
Action outcomes can be influenced by multiple distinct narrative forces simultaneously. To maintain balance and tension, these shifts are governed by the following stacking rules:

* **The Global Cap:** A single Action Roll can never be shifted by more than **two brackets** in any single direction (e.g., a maximum of +2 or -2), regardless of the number of sources.
* **The Summation Rule:** All helping (+1) and hindering (-1) shifts from both **Persona's Edge** and **Intervention** are summed together to determine the final resolution shift.
* **Persona's Edge Limit:** As per the Non-Scaling Rule, a character may only derive one shift (Help or Hinder) from their own Persona per roll, regardless of the number of tags invoked.
* **Contested Summation:** In **Contested Rolls**, the final outcome is determined by the net sum of all attacker and defender shifts. For example, if an attacker has a **Persona Up-Shift** (+1) and the defender has a **Defender Helping** shift (which acts as a -1 to the attacker), the net shift is 0.

**Game Methodology: The Hierarchy of Modification**
When players seek to influence the outcome of a critical task, they should prioritize their mechanical levers based on their relative weight and reliability:

1. **Persona's Edge (Primary Impact):** The most potent and consistent modifier. It allows a character's expertise to bypass the dice entirely by shifting the narrative result *after* the calculation. 
2. **Intervention (Primary/Secondary Impact):** A rare but powerful "wildcard" that can mimic Persona's Edge or provide unique utility (like aiding others). While as impactful as an Edge, its rarity makes it a precious narrative resource.
3. **Favor (Secondary Impact):** The most effective way to influence the probability of a successful roll. It significantly clusters results toward higher success brackets without any resource cost.
4. **Pushing the Roll (Tertiary Impact):** A high-cost "panic button." It offers a second chance but no mathematical improvement to the dice total. Best reserved for desperate mitigation of a catastrophic initial roll.
