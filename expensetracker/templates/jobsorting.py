def getapp():
    applications = {}
    numapp = int(input("Enter the number of applicants: "))
    for i in range(1, numapp + 1):
        print(f"\nEnter details for applicant {i}:")
        name = input("Name: ")
        age = int(input("Age: "))
        exp = int(input("Years of Experience: "))
        qualification = input("Qualification: ").strip().lower()
        applications[i] = {"name": name, "age": age, "exp": exp, "qualification": qualification}
    return applications

def shortlist_candidates(candidates, min_age, required_qualification, min_experience):
    shortlisted = []
    rejected = []

    for candidate in candidates.values():  # Iterate through candidate dictionaries
        if (candidate["age"] >= min_age and 
            candidate["qualification"] == required_qualification and 
            candidate["exp"] >= min_experience):
            shortlisted.append(candidate)
        else:
            rejected.append(candidate)

    return shortlisted, rejected
    
job_applications = getapp()

print("\nEnter details for shortlisting:")
min_age = int(input("Min Age: "))
required_qualification = input("Required Qualification: ").strip().lower()
min_experience = int(input("Min Experience (years): "))

shortlisted, rejected = shortlist_candidates(job_applications, min_age, required_qualification, min_experience)

print("\nShortlisted Candidates:")
for candidate in shortlisted:
    print(candidate)

print("\nRejected Candidates:")
for candidate in rejected:
    print(candidate)


print("\nRejected Candidates:")
for candidate in rejected:
    print(candidate)