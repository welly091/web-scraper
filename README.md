# LAB - 17 
## Project Web Scraping
### Author: Yu-Wei Hsieh

### Setup
#### Requirements:
- ``.venv``

### Run the application
Inside [web-scraper folder](./web-scraper), execute ``python scraper.py``

### Feature Tasks and Requirements
- Scrape a Wikipedia page of your choosing and record which passages need citations.
  - E.g. History of Mexico has a few “citations needed”.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
  - E.g. Citation needed for “lorem spam and impsum eggs”
  - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

### Implementation Notes
- Module must be named scraper.py
- Create function named get_citations_needed_count
  - takes in a url string and returns an integer.
- Create function named get_citations_needed_report
  - takes in a url string and returns a report string
  - the string should be formatted with each citation listed in the order found.

### Example 
#### Scrape: https://en.wikipedia.org/wiki/American_Civil_War

```
There are 11 cititations needed.

The Davis government of the new Confederacy sent three delegates to Washington to negotiate a peace treaty with the United States of America. Lincoln rejected any negotiations with Confederate agents becau
se he claimed the Confederacy was not a legitimate government, and that making any treaty with it would be tantamount to recognition of it as a sovereign government. Lincoln instead attempted to negotiate 
directly with the governors of individual seceded states, whose administrations he continued to recognize.

The Eastern theater refers to the military operations east of the Appalachian Mountains, including the states of Virginia, West Virginia, Maryland, and Pennsylvania, the District of Columbia, and the coast
al fortifications and seaports of North Carolina.

The Northern Virginia Campaign, which included the Second Battle of Bull Run, ended in yet another victory for the South. McClellan resisted General-in-Chief Halleck's orders to send reinforcements to John
 Pope's Union Army of Virginia, which made it easier for Lee's Confederates to defeat twice the number of combined enemy troops.

The primary Union forces in the Western theater were the Army of the Tennessee and the Army of the Cumberland, named for the two rivers, the Tennessee River and Cumberland River. After Meade's inconclusive
 fall campaign, Lincoln turned to the Western Theater for new leadership. At the same time, the Confederate stronghold of Vicksburg surrendered, giving the Union control of the Mississippi River, permanent
ly isolating the western Confederacy, and producing the new leader Lincoln needed, Ulysses S. Grant.

The Union's key strategist and tactician in the West was Ulysses S. Grant, who won victories at Forts Henry (February 6, 1862) and Donelson (February 11 to 16, 1862), earning him the nickname of "Unconditi
onal Surrender" Grant, by which the Union seized control of the Tennessee and Cumberland Rivers. Nathan Bedford Forrest rallied nearly 4,000 Confederate troops and led them to escape across the Cumberland.
 Nashville and central Tennessee thus fell to the Union, leading to attrition of local food supplies and livestock and a breakdown in social organization.

In April 1862, the Union Navy captured New Orleans. "The key to the river was New Orleans, the South's largest port [and] greatest industrial center." U.S. Naval forces under Farragut ran past Confederate 
defenses south of New Orleans. Confederate forces abandoned the city, giving the Union a critical anchor in the deep South. which allowed Union forces to begin moving up the Mississippi. Memphis fell to Un
ion forces on June 6, 1862, and became a key base for further advances south along the Mississippi River. Only the fortress city of Vicksburg, Mississippi, prevented Union control of the entire river.     

The one clear Confederate victory in the West was the Battle of Chickamauga. After Rosecrans' successful Tullahoma Campaign, Bragg, reinforced by Lt. Gen. James Longstreet's corps (from Lee's army in the e
ast), defeated Rosecrans, despite the heroic defensive stand of Maj. Gen. George Henry Thomas.

The Lower Seaboard theater refers to military and naval operations that occurred near the coastal areas of the Southeast (Alabama, Florida, Louisiana, Mississippi, South Carolina, and Texas) as well as the
 southern part of the Mississippi River (Port Hudson and south). Union Naval activities were dictated by the Anaconda Plan.

Several small skirmishes were fought in Florida, but no major battles. The biggest was the Battle of Olustee in early 1864.

Analyzing the number of dead by using census data to calculate the deviation of the death rate of men of fighting age from the norm suggests that at least 627,000 and at most 888,000, but most likely 761,0
00 soldiers, died in the war. This would break down to approximately 350,000 Confederate and 411,000 Union military deaths, going by the proportion of Union to Confederate battle losses.

President Johnson took a lenient approach and saw the achievement of the main war goals as realized in 1865 when each ex-rebel state repudiated secession and ratified the Thirteenth Amendment. Radical Repu
blicans demanded proof that Confederate nationalism was dead and that the slaves were truly free. They came to the fore after the 1866 elections and undid much of Johnson's work. In 1872, the "Liberal Repu
blicans" argued that the war goals had been achieved and that Reconstruction should end. They ran a presidential ticket in 1872 but were decisively defeated. In 1874, Democrats, primarily Southern, took co
ntrol of Congress and opposed further reconstruction. The Compromise of 1877 closed with a national consensus that the Civil War had finally ended. With the withdrawal of federal troops, however, whites re
took control of every Southern legislature, and the Jim Crow era of disenfranchisement and legal segregation was ushered in.
```
