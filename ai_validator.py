import yaml
import sys

file = sys.argv[1]

with open(file, 'r') as f:
    template = yaml.safe_load(f)

issues = []

resources = template.get("Resources", {})

for name, res in resources.items():

    if res["Type"] == "AWS::EC2::SecurityGroup":
        ingress = res["Properties"].get("SecurityGroupIngress", [])
        for rule in ingress:
            if rule.get("CidrIp") == "0.0.0.0/0":
                issues.append("Open security group detected")

    if res["Type"] == "AWS::ECS::TaskDefinition":
        cpu = int(res["Properties"].get("Cpu", 0))
        if cpu > 1024:
            issues.append("ECS CPU is over-provisioned")

if issues:
    print("❌ Validation Failed")
    for i in issues:
        print("Issue:", i)
    sys.exit(1)

print("✅ Validation Passed")
