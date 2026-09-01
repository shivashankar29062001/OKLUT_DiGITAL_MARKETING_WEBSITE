with open("index.html", "r", encoding="utf8") as f:
    content = f.read()

# Replace the mega column categories with single column
start_marker = "<!-- Category 1: MARKETING -->"
end_marker = "<!-- Bottom CTA in Mega Menu -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx >= 0 and end_idx >= 0:
    # Include the end marker line
    end_idx += len(end_marker)
    replacement = """<!-- Single column: All Services -->
                <div class="mega-column">
                  <ul class="mega-sublist">
                    <li><a href="#contact" data-service="Performance Marketing" class="mega-link"><span class="bullet"></span>Performance Marketing</a></li>
                    <li><a href="#contact" data-service="Social Media Marketing" class="mega-link"><span class="bullet"></span>Social Media Marketing</a></li>
                    <li><a href="#contact" data-service="SEO" class="mega-link"><span class="bullet"></span>SEO (Search Engine Optimization)</a></li>
                    <li><a href="#contact" data-service="AEO" class="mega-link"><span class="bullet"></span>AEO (Answer Engine Optimization)</a></li>
                    <li><a href="#contact" data-service="GEO" class="mega-link"><span class="bullet"></span>GEO (Generative Engine Optimization)</a></li>
                    <li><a href="#contact" data-service="On-Page Optimization" class="mega-link"><span class="bullet"></span>On-Page Optimization</a></li>
                    <li><a href="#contact" data-service="WhatsApp Bulk Messages" class="mega-link"><span class="bullet"></span>WhatsApp Bulk Messages</a></li>
                    <li><a href="#contact" data-service="Email Automation" class="mega-link"><span class="bullet"></span>Email Automation</a></li>
                    <li><a href="#contact" data-service="AI Cold Calling" class="mega-link"><span class="bullet"></span>AI Cold Calling</a></li>
                    <li><a href="#contact" data-service="WordPress Development" class="mega-link"><span class="bullet"></span>WordPress Development</a></li>
                    <li><a href="#contact" data-service="Website Development & Maintenance" class="mega-link"><span class="bullet"></span>Website Development & Maintenance</a></li>
                    <li><a href="#contact" data-service="App Development & Maintenance" class="mega-link"><span class="bullet"></span>App Development & Maintenance</a></li>
                    <li><a href="#contact" data-service="Android & iOS App Development" class="mega-link"><span class="bullet"></span>App Development – Android & iOS</a></li>
                    <li><a href="#contact" data-service="Content Creation" class="mega-link"><span class="bullet"></span>Content Creation</a></li>
                    <li><a href="#contact" data-service="2D & 3D Animations" class="mega-link"><span class="bullet"></span>2D & 3D Animations</a></li>
                  </ul>
                </div>

"""

    new_content = content[:start_idx] + replacement + content[end_idx:]
    with open("index.html", "w", encoding="utf8") as f:
        f.write(new_content)
    print("Replacement done")
else:
    print(f"start_idx={start_idx}, end_idx={end_idx}")