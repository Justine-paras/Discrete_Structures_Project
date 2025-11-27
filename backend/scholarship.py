import webview

# Scholarship logic using discrete set operations
SCHOLARSHIP_REQUIREMENTS = {
    "academic": {"High GPA (3.5+)", "Dean's List", "Recommendation Letter"},
    "athletic": {"Varsity Team Member", "Coach Endorsement", "Fitness Test"},
    "financial": {"Income Statement", "Barangay Clearance", "Parent's Employment Certificate"}
}

class ScholarshipAPI:
    def to_bool(self, answer):
        return str(answer).strip().lower() in ["y", "yes", "true", "1"]

    def check_academic(self, answers):
        A1 = self.to_bool(answers.get("A1"))
        A2 = self.to_bool(answers.get("A2"))
        A3 = self.to_bool(answers.get("A3"))
        A4 = self.to_bool(answers.get("A4"))
        eligible = A1 and A2 and A3 and A4

        missing = []
        if not A1: missing.append("Grade below 3.25")
        if not A2: missing.append("Less than 18 units")
        if not A3: missing.append("Residency requirement not met")
        if not A4: missing.append("Not in top 30 Percent GPA ranking")

        return {"eligible": eligible, "missing": missing}

    def check_financial(self, answers):
        F1 = self.to_bool(answers.get("F1"))
        F2 = self.to_bool(answers.get("F2"))  # preferred
        F3 = self.to_bool(answers.get("F3"))
        F4 = self.to_bool(answers.get("F4"))  # preferred
        F5 = self.to_bool(answers.get("F5"))
        F6 = self.to_bool(answers.get("F6"))
        F7 = self.to_bool(answers.get("F7"))
        eligible = F1 and F3 and F5 and F6 and F7

        missing = []
        if not F1: missing.append("Must be a Filipino citizen")
        if not F3: missing.append("Not of good moral character")
        if not F5: missing.append("GPA/Average requirement not met")
        if not F6: missing.append("Has failing grade")
        if not F7: missing.append("Less than 18 units")

        return {"eligible": eligible, "missing": missing}

    def check_athletic(self, answers):
        AT1 = self.to_bool(answers.get("AT1"))
        AT2 = self.to_bool(answers.get("AT2"))
        AT3 = self.to_bool(answers.get("AT3"))
        eligible = AT1 and AT2 and AT3

        missing = []
        if not AT1: missing.append("Must be varsity player/member")
        if not AT2: missing.append("Coach recommendation missing")
        if not AT3: missing.append("Sport not in university list")

        return {"eligible": eligible, "missing": missing}

    def check_eligibility(self, scholarship_type, answers):
        if scholarship_type == "academic":
            result = self.check_academic(answers)
        elif scholarship_type == "financial":
            result = self.check_financial(answers)
        elif scholarship_type == "athletic":
            result = self.check_athletic(answers)
        else:
            return "Invalid scholarship type."

        if result["eligible"]:
            return f"✅ Congratulations! You are eligible for a {scholarship_type.capitalize()} Scholarship!"
        else:
            missing_text = "<br>".join(f"❌ {req}" for req in result["missing"])
            return f"You are not eligible yet.<br>Missing requirements:<br>{missing_text}"
        

    def get_requirements(self, scholarship_type):
        if scholarship_type == "academic":
            return [
            {"key": "A1", "label": "I have NO grade below 3.25."},
            {"key": "A2", "label": "I am enrolled in at least 18 units."},
            {"key": "A3", "label": "I have completed at least one semester of residency."},
            {"key": "A4", "label": "I am within the Top 30 Percent GPA ranking."}
        ]
        elif scholarship_type == "financial":
            return [
            {"key": "F1", "label": "Are you a Filipino citizen?"},
            {"key": "F2", "label": "Are you Catholic?"},  # preferred
            {"key": "F3", "label": "Do you have a good disciplinary record?"},
            {"key": "F4", "label": "Are you a public school graduate?"},  # preferred
            {"key": "F5", "label": "Do you have at least 85% (freshmen) or GPA 2.50 (upperclassmen)?"},
            {"key": "F6", "label": "Do you have no failing grade?"},
            {"key": "F7", "label": "Are you enrolled in at least 18 units?"}
        ]
        elif scholarship_type == "athletic":
            return [
            {"key": "AT1", "label": "Are you an incoming varsity player OR current varsity member?"},
            {"key": "AT2", "label": "Do you have a coach evaluation and recommendation?"},
            {"key": "AT3", "label": "Is your sport included (Basketball/Volleyball/Track/Badminton/TT/Swim/Chess)?"}
        ]
        else:
            return []