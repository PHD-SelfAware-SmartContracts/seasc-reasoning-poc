"""
=========================================================
LegalRuleML Generator

Transforms the semantic contract into a simplified
LegalRuleML representation.

SEASC RQ2 Proof-of-Concept
=========================================================
"""

from pathlib import Path
from model.semantic_model import SemanticContract


class LegalRuleMLGenerator:

    def __init__(self):

        self.output_directory = Path("generated/legalruleml")

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def generate(self, contract: SemanticContract):

        output = []

        output.append('<?xml version="1.0"?>')
        output.append("<LegalRuleML>")

        output.append("  <Participants>")

        for participant in contract.participants:

            output.append(
                f'    <Participant id="{participant.identifier}" '
                f'role="{participant.role}"/>'
            )

        output.append("  </Participants>")

        output.append("")

        output.append("  <Rules>")

        for rule in contract.rules:

            output.append("    <Rule>")

            output.append(
                f"      <Condition>{rule.condition}</Condition>"
            )

            output.append(
                f"      <Action>{rule.action}</Action>"
            )

            output.append("    </Rule>")

        output.append("  </Rules>")

        output.append("</LegalRuleML>")

        filename = self.output_directory / "insurance.xml"

        with open(filename, "w") as f:

            f.write("\n".join(output))

        print(f"LegalRuleML written to {filename}")

        return filename
