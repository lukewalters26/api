import requests


response = requests.get("https://api.fbi.gov/wanted/v1/list")
response.raise_for_status()
fbi_data = response.json()
wanted_list = fbi_data["items"]


output_lines = []


# Part 1: Armed and dangerous individuals
output_lines.append("1) Individuals with warning SHOULD BE CONSIDERED ARMED AND DANGEROUS:\n")


for entry in wanted_list:
   warning = (entry.get("warning_message") or "").upper()


   if "SHOULD BE CONSIDERED ARMED AND DANGEROUS" in warning:
       output_lines.append(f"Name: {entry.get('title', 'Unknown')}")
       direct_link = entry.get("url", "")


       for file_entry in entry.get("files", []):
           file_url = file_entry.get("url", "")


           if file_url.lower().endswith(".pdf"):
               direct_link = file_url


       output_lines.append(f"FBI direct link: {direct_link}")


       if entry.get("sex"):
           output_lines.append(f"Gender: {entry['sex']}")


       for subject in entry.get("subjects", []):
           output_lines.append(f"subject: {subject}")


       output_lines.append("")  # blank line between people


# Part 2: Crime subject counts
output_lines.append("2) Crime subjects and counts (descending order):\n")


crime_counts = {}
for entry in wanted_list:
   for subject in entry.get("subjects", []):
       crime_counts[subject] = crime_counts.get(subject, 0) + 1


sorted_crimes = sorted(crime_counts.items(), key=lambda item: item[1], reverse=True)


for crime, count in sorted_crimes:
   output_lines.append(f"Crime: {crime} Count: {count}")


# Write to json
with open("fbi.json", "w") as outfile:
   outfile.write("\n".join(output_lines))
