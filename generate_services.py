"""
OKLUT Premium Service Pages Generator
Generates all 19 service detail pages with consistent premium navy blue glass theme
"""

import os
import re

# Service definitions with unique content for each page
SERVICES = {
    "SEO": {
        "title": "SEO Services",
        "hero_title": 'Dominate Search Rankings With <span class="gradient-text">Data-Driven SEO</span>',
        "hero_desc": "Dominate search engine rankings with data-driven organic strategies, technical optimization, and authoritative link building designed for sustained growth.",
        "badge": "Search Engine Optimization",
        "cta_primary": "Start Your SEO Audit",
        "cta_secondary": "View Case Studies",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80",
        "image_alt": "SEO Analytics Dashboard",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>',
        "badge_text": "Search Rankings",
        "badge_value": "+150%",
        "stat1_value": "150%", "stat1_label": "Avg Traffic Increase",
        "stat2_value": "95%", "stat2_label": "Client Retention",
        "stat3_value": "500+", "stat3_label": "Keywords Ranked",
        "overview_title": "Technical Precision Meets Content Authority",
        "overview_desc": "Our SEO methodology goes beyond simple keywords. We architect search-optimized experiences that compound traffic and drive high-intent leads over time.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>', "title": "Semantic Keyword Strategy", "desc": "We identify high-value, long-tail opportunities and map them to user intent, ensuring you capture traffic that converts."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>', "title": "Technical Foundation", "desc": "Optimizing crawlability, site architecture, and Core Web Vitals for seamless search engine access."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>', "title": "Content Architecture", "desc": "Building topical authority through strategic pillar pages and cluster content."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>', "title": "Authoritative Link Building", "desc": "Acquiring high-quality, contextual backlinks from relevant industry publications."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "Local SEO Dominance", "desc": "Google Business Profile optimization and local citation building for maximum visibility."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Analytics & Reporting", "desc": "Comprehensive performance tracking with actionable insights and monthly reports."}
        ],
        "process": [
            {"num": "01", "title": "Technical Audit", "desc": "Deep-dive analysis of your site's technical health, crawlability, and performance metrics."},
            {"num": "02", "title": "Strategy Development", "desc": "Custom roadmap with keyword targets, content plan, and link building strategy."},
            {"num": "03", "title": "Execution & Optimization", "desc": "Implement changes, create content, build links, and continuously optimize for results."}
        ],
        "tech_tags": ["Google Analytics", "Search Console", "Ahrefs", "SEMrush", "Screaming Frog", "Schema Markup", "Core Web Vitals", "PageSpeed Insights"],
        "stats": [
            {"value": "150%", "label": "Avg Traffic Increase"},
            {"value": "95%", "label": "Client Retention"},
            {"value": "500+", "label": "Keywords Page 1"},
            {"value": "10+", "label": "Years Experience"}
        ]
    },
    "AI_code": {
        "title": "AI Cold Calling",
        "hero_title": 'Unstoppable Sales With <span class="gradient-text">Human-Like AI</span>',
        "hero_desc": "Scale your outbound efforts with intelligent voice agents. Leveraging advanced neural voice synthesis and real-time semantic logic to handle objections and close deals.",
        "badge": "AI-Powered Sales",
        "cta_primary": "Deploy AI Agents",
        "cta_secondary": "Hear Samples",
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80",
        "image_alt": "AI Voice Processing Interface",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>',
        "badge_text": "AI Processing",
        "badge_value": "Real-time",
        "stat1_value": "10x", "stat1_label": "Call Volume",
        "stat2_value": "65%", "stat2_label": "Lead Qualification",
        "stat3_value": "85%", "stat3_label": "Cost Reduction",
        "overview_title": "The Intelligence Behind the Voice",
        "overview_desc": "Our AI doesn't just read scripts; it understands context, manages objections, and seamlessly integrates with your existing workflow.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "Neural Voice Synthesis", "desc": "Ultra-realistic voice engines that sound indistinguishable from human agents."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "Objection Handling", "desc": "Real-time semantic logic processes prospect responses instantly."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "CRM Integration", "desc": "Automated pipeline updates push transcripts directly into your CRM."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" x2="22" y1="12" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>', "title": "Multilingual Support", "desc": "Communicate with prospects globally in their native language."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>', "title": "Smart Scheduling", "desc": "Automatically book meetings based on availability during the call."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>', "title": "Sentiment Analysis", "desc": "Analyze tone and adjust conversational approach in real-time."}
        ],
        "process": [
            {"num": "01", "title": "Model Training", "desc": "Customize the AI with your brand voice, scripts, and industry context."},
            {"num": "02", "title": "Integration & Testing", "desc": "Connect to your tech stack and run simulated calls to refine responses."},
            {"num": "03", "title": "Go Live & Scale", "desc": "Deploy agents and effortlessly scale call volume as needed."}
        ],
        "tech_tags": ["Neural TTS", "NLP Engine", "Salesforce", "HubSpot", "Pipedrive", "Zapier", "Real-time Analytics", "API Integration"],
        "stats": [
            {"value": "10x", "label": "Call Volume"},
            {"value": "65%", "label": "Lead Qualification"},
            {"value": "85%", "label": "Cost Reduction"},
            {"value": "24/7", "label": "Availability"}
        ]
    },
    "performance": {
        "title": "Performance Marketing",
        "hero_title": 'Maximize ROI With <span class="gradient-text">Performance Marketing</span>',
        "hero_desc": "Data-driven advertising campaigns across Google, Meta, and premium networks. We optimize every dollar for maximum conversions and measurable business growth.",
        "badge": "Paid Advertising",
        "cta_primary": "Launch Your Campaign",
        "cta_secondary": "View Results",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80",
        "image_alt": "Performance Marketing Analytics",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>',
        "badge_text": "ROAS",
        "badge_value": "8.5x",
        "stat1_value": "8.5x", "stat1_label": "Average ROAS",
        "stat2_value": "40%", "stat2_label": "Cost Reduction",
        "stat3_value": "200+", "stat3_label": "Campaigns Managed",
        "overview_title": "Precision-Driven Ad Performance",
        "overview_desc": "We combine creative excellence with mathematical precision to deliver advertising that converts. Every impression, click, and conversion is tracked and optimized.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>', "title": "Google Ads Management", "desc": "Search, Display, Shopping, and YouTube campaign optimization."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>', "title": "Meta Advertising", "desc": "Facebook, Instagram, and WhatsApp campaign strategies."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Conversion Tracking", "desc": "Advanced pixel setup and attribution modeling for accurate measurement."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>', "title": "A/B Testing", "desc": "Continuous creative and landing page testing to maximize conversions."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "Remarketing Campaigns", "desc": "Re-engage warm audiences across the buyer journey."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>', "title": "Landing Page Optimization", "desc": "High-converting landing pages designed for maximum ROI."}
        ],
        "process": [
            {"num": "01", "title": "Audit & Strategy", "desc": "Analyze current performance, competitor landscape, and define growth targets."},
            {"num": "02", "title": "Campaign Setup", "desc": "Create optimized campaigns with precise targeting and compelling creatives."},
            {"num": "03", "title": "Optimize & Scale", "desc": "Continuous monitoring, A/B testing, and scaling winning campaigns."}
        ],
        "tech_tags": ["Google Ads", "Meta Ads", "Google Analytics", "Hotjar", "Unbounce", "AdEspresso", "SEMrush", "SpyFu"],
        "stats": [
            {"value": "8.5x", "label": "Average ROAS"},
            {"value": "40%", "label": "Cost Reduction"},
            {"value": "200+", "label": "Campaigns"},
            {"value": "$5M+", "label": "Ad Spend Managed"}
        ]
    },
    "social": {
        "title": "Social Media Marketing",
        "hero_title": 'Build Brand Authority With <span class="gradient-text">Social Media</span>',
        "hero_desc": "Strategic social media management that builds communities, drives engagement, and converts followers into loyal customers across all major platforms.",
        "badge": "Social Growth",
        "cta_primary": "Grow Your Audience",
        "cta_secondary": "See Our Work",
        "image": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=800&q=80",
        "image_alt": "Social Media Dashboard",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
        "badge_text": "Engagement",
        "badge_value": "+280%",
        "stat1_value": "280%", "stat1_label": "Engagement Growth",
        "stat2_value": "50K+", "stat2_label": "Followers Generated",
        "stat3_value": "98%", "stat3_label": "Client Satisfaction",
        "overview_title": "Community-Driven Growth",
        "overview_desc": "We don't just post content; we build thriving communities. Our strategies combine creative storytelling with data-driven optimization.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>', "title": "Content Strategy", "desc": "Custom content calendars aligned with your brand voice and business goals."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>', "title": "Visual Content Creation", "desc": "Eye-catching graphics, reels, and stories that stop the scroll."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "Community Management", "desc": "Active engagement with your audience to build loyalty and trust."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" x2="18" y1="20" y2="10"/><line x1="12" x2="12" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="14"/></svg>', "title": "Analytics & Insights", "desc": "Detailed performance reports with actionable growth recommendations."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>', "title": "Influencer Partnerships", "desc": "Strategic collaborations with relevant creators in your niche."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>', "title": "Paid Social Advertising", "desc": "Targeted ad campaigns that amplify your organic reach."}
        ],
        "process": [
            {"num": "01", "title": "Brand Audit", "desc": "Analyze your current social presence, competitors, and audience behavior."},
            {"num": "02", "title": "Strategy & Content", "desc": "Develop a custom content strategy with creative assets and posting schedule."},
            {"num": "03", "title": "Engage & Grow", "desc": "Execute campaigns, engage with community, and optimize for growth."}
        ],
        "tech_tags": ["Instagram", "Facebook", "LinkedIn", "Twitter/X", "TikTok", "YouTube", "Canva", "Hootsuite"],
        "stats": [
            {"value": "280%", "label": "Engagement Growth"},
            {"value": "50K+", "label": "Followers Generated"},
            {"value": "98%", "label": "Client Satisfaction"},
            {"value": "3x", "label": "Content Output"}
        ]
    },
    "web": {
        "title": "Web Development",
        "hero_title": 'Build Premium Websites With <span class="gradient-text">Web Development</span>',
        "hero_desc": "Custom-built, high-performance websites that convert visitors into customers. From sleek landing pages to complex enterprise platforms.",
        "badge": "Web Development",
        "cta_primary": "Start Your Project",
        "cta_secondary": "View Portfolio",
        "image": "https://images.unsplash.com/photo-1547658719-da2b51169166?w=800&q=80",
        "image_alt": "Modern Web Development",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
        "badge_text": "Projects",
        "badge_value": "200+",
        "stat1_value": "200+", "stat1_label": "Websites Built",
        "stat2_value": "99.9%", "stat2_label": "Uptime Guarantee",
        "stat3_value": "2s", "stat3_label": "Avg Load Time",
        "overview_title": "Code That Converts",
        "overview_desc": "We build websites that don't just look good—they perform. Every pixel, every interaction, every line of code is optimized for conversion.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>', "title": "Custom Development", "desc": "Tailored solutions built from scratch to match your exact requirements."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>', "title": "Responsive Design", "desc": "Flawless experience across all devices and screen sizes."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>', "title": "Performance Optimization", "desc": "Lightning-fast load times with optimized code and assets."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>', "title": "Security First", "desc": "Enterprise-grade security with SSL, WAF, and regular audits."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>', "title": "Fast Delivery", "desc": "Agile development process with rapid prototyping and iteration."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>', "title": "Ongoing Support", "desc": "Post-launch maintenance, updates, and technical support."}
        ],
        "process": [
            {"num": "01", "title": "Discovery & Planning", "desc": "Understanding your goals, audience, and technical requirements."},
            {"num": "02", "title": "Design & Development", "desc": "Creating stunning designs and building with clean, scalable code."},
            {"num": "03", "title": "Launch & Support", "desc": "Thorough testing, deployment, and ongoing maintenance."}
        ],
        "tech_tags": ["React", "Next.js", "Node.js", "WordPress", "Shopify", "Tailwind CSS", "AWS", "Vercel"],
        "stats": [
            {"value": "200+", "label": "Websites Built"},
            {"value": "99.9%", "label": "Uptime"},
            {"value": "2s", "label": "Load Time"},
            {"value": "4.9/5", "label": "Client Rating"}
        ]
    },
    "app_development": {
        "title": "App Development",
        "hero_title": 'Build Powerful Apps With <span class="gradient-text">Mobile Development</span>',
        "hero_desc": "Native and cross-platform mobile applications that deliver exceptional user experiences. From concept to App Store, we build apps that scale.",
        "badge": "Mobile Apps",
        "cta_primary": "Build Your App",
        "cta_secondary": "View Apps",
        "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&q=80",
        "image_alt": "Mobile App Development",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>',
        "badge_text": "Apps Built",
        "badge_value": "50+",
        "stat1_value": "50+", "stat1_label": "Apps Launched",
        "stat2_value": "4.8", "stat2_label": "Avg App Rating",
        "stat3_value": "1M+", "stat3_label": "Downloads",
        "overview_title": "Apps That Users Love",
        "overview_desc": "We craft mobile experiences that delight users and drive business results. Every interaction is designed for maximum engagement and retention.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>', "title": "iOS Development", "desc": "Native Swift/SwiftUI apps optimized for Apple ecosystem."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>', "title": "Android Development", "desc": "Kotlin/Jetpack Compose apps for the Android ecosystem."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>', "title": "Cross-Platform", "desc": "React Native/Flutter apps for both platforms simultaneously."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "Backend & APIs", "desc": "Robust backend systems and RESTful/GraphQL APIs."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "title": "App Store Optimization", "desc": "ASO strategies to maximize visibility and downloads."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Analytics Integration", "desc": "Comprehensive tracking and user behavior analytics."}
        ],
        "process": [
            {"num": "01", "title": "Strategy & Design", "desc": "Wireframing, UI/UX design, and technical architecture planning."},
            {"num": "02", "title": "Development & Testing", "desc": "Agile development with continuous testing and quality assurance."},
            {"num": "03", "title": "Launch & Growth", "desc": "App Store submission, marketing support, and ongoing updates."}
        ],
        "tech_tags": ["Swift", "Kotlin", "React Native", "Flutter", "Firebase", "AWS", "Figma", "Xcode"],
        "stats": [
            {"value": "50+", "label": "Apps Launched"},
            {"value": "4.8", "label": "Avg Rating"},
            {"value": "1M+", "label": "Downloads"},
            {"value": "99%", "label": "Success Rate"}
        ]
    },
    "wordpress": {
        "title": "WordPress Development",
        "hero_title": 'Powerful Websites With <span class="gradient-text">WordPress</span>',
        "hero_desc": "Custom WordPress solutions that go beyond templates. From business sites to complex e-commerce, we build WordPress websites that perform.",
        "badge": "WordPress Expert",
        "cta_primary": "Get WordPress Site",
        "cta_secondary": "View Examples",
        "image": "https://images.unsplash.com/photo-1587620962725-abab7fe55159?w=800&q=80",
        "image_alt": "WordPress Development",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
        "badge_text": "Sites Built",
        "badge_value": "150+",
        "stat1_value": "150+", "stat1_label": "WordPress Sites",
        "stat2_value": "100%", "stat2_label": "Custom Themes",
        "stat3_value": "24/7", "stat3_label": "Support",
        "overview_title": "WordPress Beyond Templates",
        "overview_desc": "We don't use off-the-shelf templates. Every WordPress site we build is custom-designed and developed to match your brand and business needs.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>', "title": "Custom Theme Development", "desc": "Unique designs built from scratch, no generic templates."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>', "title": "WooCommerce Solutions", "desc": "Full-featured e-commerce stores with payment integration."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "title": "Security Hardening", "desc": "Enterprise-grade security with malware protection and firewalls."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>', "title": "Speed Optimization", "desc": "Caching, CDN, and code optimization for blazing fast speeds."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>', "title": "Plugin Development", "desc": "Custom plugins to extend functionality exactly as you need."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Maintenance & Support", "desc": "Ongoing updates, backups, and technical support."}
        ],
        "process": [
            {"num": "01", "title": "Requirements Analysis", "desc": "Understanding your content needs, functionality, and goals."},
            {"num": "02", "title": "Custom Development", "desc": "Building custom themes, plugins, and configurations."},
            {"num": "03", "title": "Launch & Maintenance", "desc": "Deployment, training, and ongoing support."}
        ],
        "tech_tags": ["WordPress", "WooCommerce", "PHP", "MySQL", "ACF Pro", "Elementor", "WP Engine", "Cloudflare"],
        "stats": [
            {"value": "150+", "label": "Sites Built"},
            {"value": "100%", "label": "Custom Themes"},
            {"value": "99.9%", "label": "Uptime"},
            {"value": "24/7", "label": "Support"}
        ]
    },
    "whatsapp": {
        "title": "WhatsApp Automation",
        "hero_title": 'Scale Outreach With <span class="gradient-text">WhatsApp Automation</span>',
        "hero_desc": "Automated WhatsApp marketing campaigns, bulk messaging, and conversational AI that converts. Reach millions with personalized messaging at scale.",
        "badge": "WhatsApp Marketing",
        "cta_primary": "Start Messaging",
        "cta_secondary": "See Results",
        "image": "https://images.unsplash.com/photo-1611746872915-64382b5c76da?w=800&q=80",
        "image_alt": "WhatsApp Marketing Dashboard",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
        "badge_text": "Messages Sent",
        "badge_value": "10M+",
        "stat1_value": "10M+", "stat1_label": "Messages Sent",
        "stat2_value": "95%", "stat2_label": "Delivery Rate",
        "stat3_value": "45%", "stat3_label": "Open Rate",
        "overview_title": "Conversational Commerce at Scale",
        "overview_desc": "WhatsApp is the world's most popular messaging app. We help you leverage its power for marketing, sales, and customer support automation.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>', "title": "Bulk Messaging", "desc": "Send thousands of personalized messages simultaneously."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "Chatbot Automation", "desc": "AI-powered chatbots for instant customer responses."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>', "title": "Campaign Scheduling", "desc": "Schedule messages for optimal delivery times."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Analytics Dashboard", "desc": "Track delivery, read rates, and engagement metrics."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "Contact Management", "desc": "Segment and manage your contact lists effectively."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "title": "API Integration", "desc": "Connect with your CRM, e-commerce, and other tools."}
        ],
        "process": [
            {"num": "01", "title": "Setup & Configuration", "desc": "WhatsApp Business API setup and template approval."},
            {"num": "02", "title": "Campaign Creation", "desc": "Design messaging flows, chatbots, and automation rules."},
            {"num": "03", "title": "Launch & Optimize", "desc": "Send campaigns, analyze results, and optimize performance."}
        ],
        "tech_tags": ["WhatsApp Business API", "Twilio", "MessageBird", "HubSpot", "Zapier", "Node.js", "Python", "PostgreSQL"],
        "stats": [
            {"value": "10M+", "label": "Messages Sent"},
            {"value": "95%", "label": "Delivery Rate"},
            {"value": "45%", "label": "Open Rate"},
            {"value": "3x", "label": "ROI Increase"}
        ]
    },
    "Email": {
        "title": "Email Automation",
        "hero_title": 'Automate Growth With <span class="gradient-text">Email Marketing</span>',
        "hero_desc": "Strategic email automation that nurtures leads, converts customers, and drives repeat business. From welcome sequences to complex workflows.",
        "badge": "Email Marketing",
        "cta_primary": "Start Automating",
        "cta_secondary": "View Templates",
        "image": "https://images.unsplash.com/photo-1596526131083-e8c633c948d2?w=800&q=80",
        "image_alt": "Email Marketing Dashboard",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
        "badge_text": "Open Rate",
        "badge_value": "35%",
        "stat1_value": "35%", "stat1_label": "Avg Open Rate",
        "stat2_value": "12x", "stat2_label": "ROI Average",
        "stat3_value": "500K+", "stat3_label": "Emails Sent Daily",
        "overview_title": "Email That Converts",
        "overview_desc": "Email marketing delivers the highest ROI of any digital channel. We build automated sequences that work 24/7 to nurture and convert your audience.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>', "title": "Welcome Sequences", "desc": "Automated onboarding flows that make great first impressions."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>', "title": "Drip Campaigns", "desc": "Nurture sequences that guide prospects through the funnel."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Behavioral Triggers", "desc": "Automated emails based on user actions and engagement."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" x2="23" y1="10" y2="10"/></svg>', "title": "Payment Integration", "desc": "Recovery carts, receipts, and subscription management."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "List Segmentation", "desc": "Advanced targeting based on behavior and demographics."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" x2="18" y1="20" y2="10"/><line x1="12" x2="12" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="14"/></svg>', "title": "A/B Testing", "desc": "Optimize subject lines, content, and send times."}
        ],
        "process": [
            {"num": "01", "title": "Strategy & Setup", "desc": "Audit current email program and design automation workflows."},
            {"num": "02", "title": "Content & Design", "desc": "Create email templates, copy, and segmentation rules."},
            {"num": "03", "title": "Launch & Optimize", "desc": "Deploy campaigns, analyze performance, and iterate."}
        ],
        "tech_tags": ["Mailchimp", "ActiveCampaign", "Klaviyo", "SendGrid", "HubSpot", "Zapier", "Google Analytics", "Mixpanel"],
        "stats": [
            {"value": "35%", "label": "Avg Open Rate"},
            {"value": "12x", "label": "ROI"},
            {"value": "500K+", "label": "Emails/Day"},
            {"value": "98%", "label": "Delivery Rate"}
        ]
    },
    "AEO": {
        "title": "AEO Services",
        "hero_title": 'Optimize For AI With <span class="gradient-text">Answer Engine Optimization</span>',
        "hero_desc": "Optimize your content for AI-powered answer engines like ChatGPT, Perplexity, and Google SGE. Be the source AI recommends.",
        "badge": "AEO Specialist",
        "cta_primary": "Optimize Your Content",
        "cta_secondary": "Learn AEO",
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80",
        "image_alt": "AI Answer Engine Optimization",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
        "badge_text": "AI Citations",
        "badge_value": "+300%",
        "stat1_value": "300%", "stat1_label": "Citation Increase",
        "stat2_value": "85%", "stat2_label": "Visibility Score",
        "stat3_value": "50+", "stat3_label": "AI Platforms",
        "overview_title": "Be the Answer AI Recommends",
        "overview_desc": "As AI search engines reshape how users find information, AEO ensures your content is cited, recommended, and surfaced by generative AI systems.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>', "title": "AI Content Structuring", "desc": "Format content to be easily parsed and cited by AI models."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>', "title": "Schema Markup", "desc": "Structured data that helps AI understand your content context."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "Conversational Optimization", "desc": "Content written in natural language that matches AI queries."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Citation Tracking", "desc": "Monitor where and how AI systems cite your content."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>', "title": "Performance Analytics", "desc": "Track visibility across ChatGPT, Perplexity, and SGE."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "title": "Future-Proofing", "desc": "Stay ahead of AI search evolution with ongoing optimization."}
        ],
        "process": [
            {"num": "01", "title": "AEO Audit", "desc": "Analyze current AI visibility and identify optimization opportunities."},
            {"num": "02", "title": "Content Optimization", "desc": "Restructure content for AI parsing and citation."},
            {"num": "03", "title": "Monitor & Scale", "desc": "Track AI citations and continuously optimize for visibility."}
        ],
        "tech_tags": ["ChatGPT", "Perplexity", "Google SGE", "Schema.org", "JSON-LD", "NLP", "BERT", "GPT-4"],
        "stats": [
            {"value": "300%", "label": "Citation Increase"},
            {"value": "85%", "label": "Visibility Score"},
            {"value": "50+", "label": "AI Platforms"},
            {"value": "24/7", "label": "Monitoring"}
        ]
    },
    "GEO": {
        "title": "GEO Services",
        "hero_title": 'Future-Proof SEO With <span class="gradient-text">Generative Engine Optimization</span>',
        "hero_desc": "Optimize for Google's AI Overviews, SGE, and generative search experiences. Stay visible as search evolves.",
        "badge": "GEO Specialist",
        "cta_primary": "Future-Proof Your SEO",
        "cta_secondary": "Learn GEO",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80",
        "image_alt": "Generative Search Optimization",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>',
        "badge_text": "SGE Visibility",
        "badge_value": "+250%",
        "stat1_value": "250%", "stat1_label": "SGE Appearances",
        "stat2_value": "90%", "stat2_label": "Content Optimization",
        "stat3_value": "100+", "stat3_label": "Topics Covered",
        "overview_title": "Search Is Evolving. Are You?",
        "overview_desc": "Google's Search Generative Experience is changing how users interact with search results. GEO ensures your content appears in AI-generated answers.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "SGE Optimization", "desc": "Content structured to appear in Google AI Overviews."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>', "title": "Real-Time Monitoring", "desc": "Track when and how your content appears in generative results."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>', "title": "Content Restructuring", "desc": "Adapt existing content for generative search formats."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Performance Tracking", "desc": "Measure impact on traffic and visibility."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "title": "Competitive Analysis", "desc": "Benchmark against competitors in generative search."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>', "title": "Strategy Consulting", "desc": "Expert guidance on adapting to generative search."}
        ],
        "process": [
            {"num": "01", "title": "GEO Assessment", "desc": "Evaluate current visibility in generative search results."},
            {"num": "02", "title": "Content Adaptation", "desc": "Restructure and optimize content for AI-powered search."},
            {"num": "03", "title": "Monitor & Evolve", "desc": "Track performance and adapt to algorithm changes."}
        ],
        "tech_tags": ["Google SGE", "AI Overviews", "Schema Markup", "NLP Optimization", "BERT", "Knowledge Graph", "Entity SEO", "Featured Snippets"],
        "stats": [
            {"value": "250%", "label": "SGE Appearances"},
            {"value": "90%", "label": "Optimization Score"},
            {"value": "100+", "label": "Topics Covered"},
            {"value": "50+", "label": "Clients Served"}
        ]
    },
    "ONpage": {
        "title": "On-Page SEO",
        "hero_title": 'Perfect Your Rankings With <span class="gradient-text">On-Page SEO</span>',
        "hero_desc": "Technical and content optimization that makes search engines love your website. From meta tags to Core Web Vitals, we optimize every element.",
        "badge": "On-Page Specialist",
        "cta_primary": "Get On-Page Audit",
        "cta_secondary": "Learn More",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80",
        "image_alt": "On-Page SEO Analysis",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
        "badge_text": "Optimization",
        "badge_value": "100%",
        "stat1_value": "100%", "stat1_label": "Optimization Score",
        "stat2_value": "2s", "stat2_label": "Page Speed",
        "stat3_value": "100%", "stat3_label": "Core Web Vitals",
        "overview_title": "Every Element Optimized",
        "overview_desc": "On-page SEO is the foundation of search visibility. We optimize every element of your pages to maximize ranking potential.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>', "title": "Meta Optimization", "desc": "Title tags, meta descriptions, and header hierarchy."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>', "title": "Content Optimization", "desc": "Keyword placement, semantic relevance, and readability."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>', "title": "Core Web Vitals", "desc": "LCP, FID, and CLS optimization for page experience."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>', "title": "Internal Linking", "desc": "Strategic link architecture for better crawlability."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "Schema Markup", "desc": "Structured data for rich snippets and enhanced results."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>', "title": "Mobile Optimization", "desc": "Mobile-first design and responsive implementation."}
        ],
        "process": [
            {"num": "01", "title": "Technical Audit", "desc": "Comprehensive analysis of on-page elements and performance."},
            {"num": "02", "title": "Optimization", "desc": "Implement fixes for meta tags, content, speed, and structure."},
            {"num": "03", "title": "Monitor & Maintain", "desc": "Ongoing monitoring and optimization as algorithms update."}
        ],
        "tech_tags": ["Google Search Console", "PageSpeed Insights", "Screaming Frog", "GTmetrix", "Ahrefs", "Schema.org", "JSON-LD", "Webpack"],
        "stats": [
            {"value": "100%", "label": "Optimization Score"},
            {"value": "2s", "label": "Page Speed"},
            {"value": "100%", "label": "Core Web Vitals"},
            {"value": "50+", "label": "Sites Optimized"}
        ]
    },
    "influencer": {
        "title": "Influencer Marketing",
        "hero_title": 'Amplify Your Brand With <span class="gradient-text">Influencer Marketing</span>',
        "hero_desc": "Strategic influencer partnerships that build trust, expand reach, and drive conversions. We connect you with the right voices.",
        "badge": "Influencer Strategy",
        "cta_primary": "Find Influencers",
        "cta_secondary": "View Campaigns",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800&q=80",
        "image_alt": "Influencer Marketing Campaign",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
        "badge_text": "Reach",
        "badge_value": "5M+",
        "stat1_value": "5M+", "stat1_label": "Total Reach",
        "stat2_value": "200+", "stat2_label": "Influencers",
        "stat3_value": "8.5x", "stat3_label": "Avg ROI",
        "overview_title": "Authentic Influence, Real Results",
        "overview_desc": "We craft influencer campaigns that feel authentic and drive measurable results. From micro-influencers to macro creators, we find the perfect match.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>', "title": "Influencer Discovery", "desc": "Data-driven matching with influencers in your niche."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>', "title": "Campaign Strategy", "desc": "Creative briefs, content guidelines, and campaign planning."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>', "title": "Content Creation", "desc": "Supporting influencers with creative assets and guidelines."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Performance Tracking", "desc": "Measure reach, engagement, and conversion metrics."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "Relationship Management", "desc": "Long-term partnerships with top-performing creators."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" x2="23" y1="10" y2="10"/></svg>', "title": "Budget Optimization", "desc": "Maximize ROI with strategic spend allocation."}
        ],
        "process": [
            {"num": "01", "title": "Discovery & Matching", "desc": "Identify influencers that align with your brand and audience."},
            {"num": "02", "title": "Campaign Execution", "desc": "Manage partnerships, content creation, and posting."},
            {"num": "03", "title": "Analyze & Scale", "desc": "Measure results and scale successful partnerships."}
        ],
        "tech_tags": ["Instagram", "YouTube", "TikTok", "LinkedIn", "Upfluence", "AspireIQ", "CreatorIQ", "Google Analytics"],
        "stats": [
            {"value": "5M+", "label": "Total Reach"},
            {"value": "200+", "label": "Influencers"},
            {"value": "8.5x", "label": "Avg ROI"},
            {"value": "95%", "label": "Satisfaction"}
        ]
    },
    "personal_marketing": {
        "title": "Personal Branding",
        "hero_title": 'Build Authority With <span class="gradient-text">Personal Branding</span>',
        "hero_desc": "Craft a powerful personal brand that establishes thought leadership, builds trust, and opens doors to opportunities.",
        "badge": "Brand Building",
        "cta_primary": "Build Your Brand",
        "cta_secondary": "See Examples",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&q=80",
        "image_alt": "Personal Branding Strategy",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
        "badge_text": "Authority",
        "badge_value": "+400%",
        "stat1_value": "400%", "stat1_label": "Profile Views",
        "stat2_value": "50+", "stat2_label": "Brands Built",
        "stat3_value": "10K+", "stat3_label": "Connections",
        "overview_title": "Your Personal Brand Is Your Superpower",
        "overview_desc": "In today's digital world, your personal brand is your most valuable asset. We help you build an authentic, powerful presence that opens doors.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>', "title": "Brand Identity", "desc": "Define your unique value proposition and brand story."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>', "title": "Visual Branding", "desc": "Professional headshots, color palette, and visual assets."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>', "title": "Content Strategy", "desc": "Thought leadership content that establishes expertise."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "LinkedIn Optimization", "desc": "Profile optimization and engagement strategies."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>', "title": "Networking Strategy", "desc": "Build meaningful connections in your industry."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Analytics & Growth", "desc": "Track your brand's growth and engagement metrics."}
        ],
        "process": [
            {"num": "01", "title": "Brand Discovery", "desc": "Define your unique story, values, and positioning."},
            {"num": "02", "title": "Build & Launch", "desc": "Create content, optimize profiles, and start building."},
            {"num": "03", "title": "Grow & Scale", "desc": "Consistent content, networking, and thought leadership."}
        ],
        "tech_tags": ["LinkedIn", "Twitter/X", "Medium", "Substack", "Canva", "WordPress", "Notion", "Buffer"],
        "stats": [
            {"value": "400%", "label": "Profile Views"},
            {"value": "50+", "label": "Brands Built"},
            {"value": "10K+", "label": "Connections"},
            {"value": "95%", "label": "Satisfaction"}
        ]
    },
    "content": {
        "title": "Content Creation",
        "hero_title": 'Captivate Audiences With <span class="gradient-text">Content Creation</span>',
        "hero_desc": "High-quality content that engages, educates, and converts. From blog posts to video scripts, we create content that drives results.",
        "badge": "Content Studio",
        "cta_primary": "Create Content",
        "cta_secondary": "View Portfolio",
        "image": "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&q=80",
        "image_alt": "Content Creation Studio",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>',
        "badge_text": "Content Pieces",
        "badge_value": "5000+",
        "stat1_value": "5000+", "stat1_label": "Content Pieces",
        "stat2_value": "3x", "stat2_label": "Engagement Boost",
        "stat3_value": "98%", "stat3_label": "Client Satisfaction",
        "overview_title": "Content That Converts",
        "overview_desc": "Great content is the foundation of digital success. We create strategic content that attracts, engages, and converts your target audience.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>', "title": "Blog & Articles", "desc": "SEO-optimized blog posts that drive organic traffic."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>', "title": "Video Content", "desc": "Scriptwriting, storyboarding, and production support."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>', "title": "Social Content", "desc": "Engaging posts, stories, and reels for all platforms."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>', "title": "Email Content", "desc": "Newsletters, drip campaigns, and promotional emails."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>', "title": "Whitepapers & Ebooks", "desc": "Long-form content for lead generation and authority."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>', "title": "Visual Content", "desc": "Infographics, graphics, and visual assets."}
        ],
        "process": [
            {"num": "01", "title": "Strategy & Planning", "desc": "Content audit, audience research, and editorial calendar."},
            {"num": "02", "title": "Creation & Production", "desc": "Writing, designing, and producing content assets."},
            {"num": "03", "title": "Publish & Promote", "desc": "Distribution, promotion, and performance tracking."}
        ],
        "tech_tags": ["WordPress", "Grammarly", "Canva", "Adobe Creative", "Notion", "Trello", "SEMrush", "BuzzSumo"],
        "stats": [
            {"value": "5000+", "label": "Content Pieces"},
            {"value": "3x", "label": "Engagement Boost"},
            {"value": "98%", "label": "Satisfaction"},
            {"value": "50+", "label": "Industries"}
        ]
    },
    "Animation": {
        "title": "2D & 3D Animation",
        "hero_title": 'Bring Ideas to Life With <span class="gradient-text">Animation</span>',
        "hero_desc": "Stunning 2D and 3D animations that captivate audiences and tell your brand story. From explainer videos to product visualizations.",
        "badge": "Creative Studio",
        "cta_primary": "Start Animating",
        "cta_secondary": "View Reel",
        "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&q=80",
        "image_alt": "Animation Studio Work",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>',
        "badge_text": "Projects",
        "badge_value": "100+",
        "stat1_value": "100+", "stat1_label": "Animations",
        "stat2_value": "50+", "stat2_label": "Happy Clients",
        "stat3_value": "1M+", "stat3_label": "Views Generated",
        "overview_title": "Visual Stories That Captivate",
        "overview_desc": "Animation brings abstract concepts to life. Our creative team produces stunning visuals that communicate your message with impact.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>', "title": "Explainer Videos", "desc": "Animated videos that simplify complex concepts."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "3D Product Viz", "desc": "Photorealistic 3D renders and product animations."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>', "title": "Motion Graphics", "desc": "Dynamic animations for social media and ads."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "Character Animation", "desc": "Custom character design and animation."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>', "title": "UI Animations", "desc": "Micro-interactions and interface animations."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>', "title": "Brand Videos", "desc": "Corporate videos, brand stories, and testimonials."}
        ],
        "process": [
            {"num": "01", "title": "Concept & Script", "desc": "Story development, storyboarding, and creative direction."},
            {"num": "02", "title": "Production", "desc": "Animation, voiceover, sound design, and compositing."},
            {"num": "03", "title": "Delivery & Support", "desc": "Final rendering, format optimization, and revisions."}
        ],
        "tech_tags": ["After Effects", "Blender", "Cinema 4D", "Maya", "Premiere Pro", "Illustrator", "Figma", "DaVinci Resolve"],
        "stats": [
            {"value": "100+", "label": "Animations"},
            {"value": "50+", "label": "Clients"},
            {"value": "1M+", "label": "Views"},
            {"value": "4.9/5", "label": "Rating"}
        ]
    },
    "retargeting": {
        "title": "Re-targeting Campaigns",
        "hero_title": 'Recover Lost Visitors With <span class="gradient-text">Re-targeting</span>',
        "hero_desc": "Bring back website visitors who didn't convert. Strategic re-engagement campaigns that turn browsers into buyers.",
        "badge": "Retargeting Expert",
        "cta_primary": "Start Retargeting",
        "cta_secondary": "Learn More",
        "image": "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800&q=80",
        "image_alt": "Retargeting Campaign Dashboard",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
        "badge_text": "Recovery Rate",
        "badge_value": "35%",
        "stat1_value": "35%", "stat1_label": "Recovery Rate",
        "stat2_value": "5x", "stat2_label": "ROI Average",
        "stat3_value": "60%", "stat3_label": "Cost Reduction",
        "overview_title": "Turn Abandonment Into Conversion",
        "overview_desc": "97% of first-time visitors leave without converting. Re-targeting keeps your brand top-of-mind and brings them back to complete their journey.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>', "title": "Pixel Implementation", "desc": "Advanced tracking for precise audience targeting."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "Audience Segmentation", "desc": "Target specific visitor groups with tailored messages."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>', "title": "Dynamic Ads", "desc": "Personalized ads showing products users viewed."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Performance Analytics", "desc": "Track recovery rates and optimize campaigns."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>', "title": "Email Retargeting", "desc": "Abandoned cart emails and browse abandonment."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>', "title": "Cross-Platform", "desc": "Retarget across Google, Meta, and email channels."}
        ],
        "process": [
            {"num": "01", "title": "Audit & Setup", "desc": "Install tracking pixels and define retargeting audiences."},
            {"num": "02", "title": "Campaign Creation", "desc": "Design segmented campaigns with tailored messaging."},
            {"num": "03", "title": "Optimize & Scale", "desc": "Monitor performance and scale winning campaigns."}
        ],
        "tech_tags": ["Google Ads", "Meta Pixel", "TikTok Pixel", "Hotjar", "Google Analytics", "Mailchimp", "Klaviyo", "Zapier"],
        "stats": [
            {"value": "35%", "label": "Recovery Rate"},
            {"value": "5x", "label": "ROI"},
            {"value": "60%", "label": "Cost Reduction"},
            {"value": "24/7", "label": "Automation"}
        ]
    },
    "branding": {
        "title": "Personal Branding",
        "hero_title": 'Build Authority With <span class="gradient-text">Personal Branding</span>',
        "hero_desc": "Craft a powerful personal brand that establishes thought leadership, builds trust, and opens doors to opportunities.",
        "badge": "Brand Building",
        "cta_primary": "Build Your Brand",
        "cta_secondary": "See Examples",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&q=80",
        "image_alt": "Personal Branding Strategy",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
        "badge_text": "Authority",
        "badge_value": "+400%",
        "stat1_value": "400%", "stat1_label": "Profile Views",
        "stat2_value": "50+", "stat2_label": "Brands Built",
        "stat3_value": "10K+", "stat3_label": "Connections",
        "overview_title": "Your Personal Brand Is Your Superpower",
        "overview_desc": "In today's digital world, your personal brand is your most valuable asset. We help you build an authentic, powerful presence that opens doors.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>', "title": "Brand Identity", "desc": "Define your unique value proposition and brand story."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>', "title": "Visual Branding", "desc": "Professional headshots, color palette, and visual assets."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>', "title": "Content Strategy", "desc": "Thought leadership content that establishes expertise."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "title": "LinkedIn Optimization", "desc": "Profile optimization and engagement strategies."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>', "title": "Networking Strategy", "desc": "Build meaningful connections in your industry."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Analytics & Growth", "desc": "Track your brand's growth and engagement metrics."}
        ],
        "process": [
            {"num": "01", "title": "Brand Discovery", "desc": "Define your unique story, values, and positioning."},
            {"num": "02", "title": "Build & Launch", "desc": "Create content, optimize profiles, and start building."},
            {"num": "03", "title": "Grow & Scale", "desc": "Consistent content, networking, and thought leadership."}
        ],
        "tech_tags": ["LinkedIn", "Twitter/X", "Medium", "Substack", "Canva", "WordPress", "Notion", "Buffer"],
        "stats": [
            {"value": "400%", "label": "Profile Views"},
            {"value": "50+", "label": "Brands Built"},
            {"value": "10K+", "label": "Connections"},
            {"value": "95%", "label": "Satisfaction"}
        ]
    },
    "app_android": {
        "title": "Android & iOS App Development",
        "hero_title": 'Build Cross-Platform Apps With <span class="gradient-text">Mobile Development</span>',
        "hero_desc": "Native and cross-platform mobile applications for both Android and iOS. One codebase, two platforms, unlimited potential.",
        "badge": "Cross-Platform",
        "cta_primary": "Build Your App",
        "cta_secondary": "View Apps",
        "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&q=80",
        "image_alt": "Cross-Platform App Development",
        "badge_icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>',
        "badge_text": "Apps Built",
        "badge_value": "75+",
        "stat1_value": "75+", "stat1_label": "Apps Built",
        "stat2_value": "4.8", "stat2_label": "Avg Rating",
        "stat3_value": "2M+", "stat3_label": "Downloads",
        "overview_title": "One Codebase, Every Platform",
        "overview_desc": "Why build twice when you can build once? Our cross-platform expertise delivers native-quality apps for both Android and iOS simultaneously.",
        "features": [
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>', "title": "React Native", "desc": "Cross-platform apps with native performance."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>', "title": "Flutter Development", "desc": "Beautiful, natively compiled apps from one codebase."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>', "title": "Native Development", "desc": "Swift/Kotlin for platform-specific requirements."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>', "title": "Backend Integration", "desc": "RESTful APIs, GraphQL, and cloud backend."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "title": "App Security", "desc": "Secure authentication, data encryption, and compliance."},
            {"icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>', "title": "Analytics & Crash Reporting", "desc": "Firebase, Crashlytics, and custom analytics."}
        ],
        "process": [
            {"num": "01", "title": "Strategy & Design", "desc": "UX/UI design, wireframing, and technical architecture."},
            {"num": "02", "title": "Development", "desc": "Cross-platform development with shared codebase."},
            {"num": "03", "title": "Launch & Support", "desc": "App Store submission, marketing, and maintenance."}
        ],
        "tech_tags": ["React Native", "Flutter", "Swift", "Kotlin", "Firebase", "AWS Amplify", "Xcode", "Android Studio"],
        "stats": [
            {"value": "75+", "label": "Apps Built"},
            {"value": "4.8", "label": "Avg Rating"},
            {"value": "2M+", "label": "Downloads"},
            {"value": "60%", "label": "Cost Savings"}
        ]
    }
}

# HTML Template
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | OKLUT Digital Excellence</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../service-premium.css">
</head>
<body>

  <!-- Ambient Background -->
  <div class="ambient-bg"></div>
  <div class="grid-overlay"></div>
  <canvas id="particlesCanvas" class="particles-canvas"></canvas>

  <!-- Navbar -->
  <nav class="service-nav">
    <div class="nav-inner">
      <a href="../index.html" class="nav-brand">
        <img src="../logo.png" alt="OKLUT" class="nav-logo">
      </a>
      <a href="../index.html" class="nav-back">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
        Back to Home
      </a>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="service-hero">
    <div class="hero-glow hero-glow-1"></div>
    <div class="hero-glow hero-glow-2"></div>
    <div class="hero-grid"></div>
    <div class="service-container">
      <div class="hero-inner">
        <div class="hero-content">
          <div class="hero-badge">
            <span class="pulse-dot"></span>
            {badge}
          </div>
          <h1 class="hero-title">{hero_title}</h1>
          <p class="hero-description">{hero_desc}</p>
          <div class="hero-cta-group">
            <a href="#contact" class="btn-premium btn-premium-primary">{cta_primary}</a>
            <a href="#features" class="btn-premium btn-premium-outline">{cta_secondary}</a>
          </div>
          <div class="hero-stats">
            <div class="hero-stat">
              <span class="hero-stat-value" data-count="{stat1_value_num}" data-suffix="{stat1_suffix}">{stat1_value}</span>
              <span class="hero-stat-label">{stat1_label}</span>
            </div>
            <div class="hero-stat">
              <span class="hero-stat-value" data-count="{stat2_value_num}" data-suffix="{stat2_suffix}">{stat2_value}</span>
              <span class="hero-stat-label">{stat2_label}</span>
            </div>
            <div class="hero-stat">
              <span class="hero-stat-value">{stat3_value}</span>
              <span class="hero-stat-label">{stat3_label}</span>
            </div>
          </div>
        </div>
        <div class="hero-visual">
          <div class="hero-image-frame">
            <img src="{image}" alt="{image_alt}" class="hero-image">
            <div class="hero-image-overlay"></div>
          </div>
          <div class="floating-badge top-left">
            <div class="badge-icon">{badge_icon}</div>
            <div class="badge-text">
              <span class="badge-label">{badge_text}</span>
              <span class="badge-value">{badge_value}</span>
            </div>
          </div>
          <div class="floating-badge bottom-right">
            <div class="badge-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </div>
            <div class="badge-text">
              <span class="badge-label">Performance</span>
              <span class="badge-value">Real-time</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Overview Section -->
  <section class="service-section" id="overview">
    <div class="service-container">
      <div class="section-header reveal">
        <span class="section-badge">Service Overview</span>
        <h2 class="section-title">{overview_title}</h2>
        <p class="section-subtitle">{overview_desc}</p>
      </div>
    </div>
  </section>

  <!-- Features Section -->
  <section class="service-section" id="features">
    <div class="service-container">
      <div class="section-header reveal">
        <span class="section-badge">What We Deliver</span>
        <h2 class="section-title">Key <span class="gradient-text">Capabilities</span></h2>
        <p class="section-subtitle">Comprehensive solutions designed to drive measurable results for your business.</p>
      </div>
      <div class="features-grid reveal">
        {features_html}
      </div>
    </div>
  </section>

  <!-- Process Section -->
  <section class="service-section" id="process">
    <div class="service-container">
      <div class="section-header reveal">
        <span class="section-badge">Our Process</span>
        <h2 class="section-title">How We <span class="gradient-text">Deliver</span></h2>
        <p class="section-subtitle">A proven methodology that ensures consistent, high-quality results.</p>
      </div>
      <div class="process-steps reveal">
        {process_html}
      </div>
    </div>
  </section>

  <!-- Technologies Section -->
  <section class="service-section" id="technologies">
    <div class="service-container">
      <div class="section-header reveal">
        <span class="section-badge">Technologies</span>
        <h2 class="section-title">Tools & <span class="gradient-text">Technologies</span></h2>
        <p class="section-subtitle">We leverage industry-leading tools to deliver exceptional results.</p>
      </div>
      <div class="tech-tags reveal">
        {tech_tags_html}
      </div>
    </div>
  </section>

  <!-- Stats Section -->
  <section class="service-section" id="stats">
    <div class="service-container">
      <div class="stats-grid reveal">
        {stats_html}
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="cta-section" id="contact">
    <div class="service-container">
      <div class="reveal">
        <span class="section-badge">Get Started</span>
        <h2 class="cta-title">Ready to <span class="gradient-text">Transform</span> Your Business?</h2>
        <p class="cta-description">Let's discuss how our {title_lower} services can help you achieve your goals and drive measurable growth.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="../index.html#contact" class="btn-premium btn-premium-primary">Talk to an Expert</a>
          <a href="mailto:info@oklut.com" class="btn-premium btn-premium-outline">Email Us</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="service-footer">
    <div class="service-container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand-name">OKLUT</div>
          <div class="footer-brand-tag">Innovative & Digital Excellence</div>
          <p class="footer-desc">Elite digital marketing and technology solutions agency engineering sustainable growth for high-growth enterprises.</p>
        </div>
        <div>
          <h4 class="footer-heading">Quick Links</h4>
          <ul class="footer-links">
            <li><a href="../index.html">Home</a></li>
            <li><a href="../index.html#about">About Us</a></li>
            <li><a href="../index.html#careers">Careers</a></li>
            <li><a href="../index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Services</h4>
          <ul class="footer-links">
            <li><a href="../SEO/code.html">SEO</a></li>
            <li><a href="../performance/code.html">Performance Marketing</a></li>
            <li><a href="../social/code.html">Social Media</a></li>
            <li><a href="../web/code.html">Web Development</a></li>
            <li><a href="../AI_code/code.html">AI Solutions</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Contact</h4>
          <ul class="footer-links">
            <li><a href="mailto:info@oklut.com">info@oklut.com</a></li>
            <li><a href="tel:+919876543210">+91 98765 43210</a></li>
            <li><a href="#">Madhapur, Hyderabad, India</a></li>
            <li><a href="#">Newcastle, KwaZulu-Natal, South Africa</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2024 OKLUT Innovative & Digital Excellence. All rights reserved.
      </div>
    </div>
  </footer>

  <script src="../service-premium.js"></script>
</body>
</html>'''


def parse_stat_value(val):
    """Extract numeric value and suffix from stat value string."""
    val = val.strip()
    if not val:
        return "0", ""
    # Handle cases like "150%", "50+", "4.8", "$5M+", "24/7", "4.9/5"
    import re
    m = re.match(r'^(\$?)(\d+\.?\d*)(%?\+?/?\d*)', val)
    if m:
        prefix = m.group(1)
        num = m.group(2)
        suffix = prefix + m.group(3)
        return num, suffix
    return val, ""


def generate_features_html(features):
    html = ""
    for f in features:
        html += f'''        <div class="glass-card">
          <div class="glass-card-icon">{f["icon"]}</div>
          <h3>{f["title"]}</h3>
          <p>{f["desc"]}</p>
        </div>
'''
    return html


def generate_process_html(process):
    html = ""
    for p in process:
        html += f'''        <div class="process-step">
          <div class="process-step-number">{p["num"]}</div>
          <h3>{p["title"]}</h3>
          <p>{p["desc"]}</p>
        </div>
'''
    return html


def generate_tech_tags_html(tags):
    html = ""
    for t in tags:
        html += f'        <span class="tech-tag">{t}</span>\n'
    return html


def generate_stats_html(stats):
    html = ""
    for s in stats:
        html += f'''        <div class="stat-card">
          <div class="stat-value">{s["value"]}</div>
          <div class="stat-label">{s["label"]}</div>
        </div>
'''
    return html


def generate_service_page(service_key, service_data):
    """Generate a complete service page HTML."""
    features_html = generate_features_html(service_data["features"])
    process_html = generate_process_html(service_data["process"])
    tech_tags_html = generate_tech_tags_html(service_data["tech_tags"])
    stats_html = generate_stats_html(service_data["stats"])

    stat1_num, stat1_suffix = parse_stat_value(service_data["stat1_value"])
    stat2_num, stat2_suffix = parse_stat_value(service_data["stat2_value"])

    html = HTML_TEMPLATE.format(
        title=service_data["title"],
        hero_title=service_data["hero_title"],
        hero_desc=service_data["hero_desc"],
        badge=service_data["badge"],
        cta_primary=service_data["cta_primary"],
        cta_secondary=service_data["cta_secondary"],
        image=service_data["image"],
        image_alt=service_data["image_alt"],
        badge_icon=service_data["badge_icon"],
        badge_text=service_data["badge_text"],
        badge_value=service_data["badge_value"],
        stat1_value=service_data["stat1_value"],
        stat1_label=service_data["stat1_label"],
        stat1_value_num=stat1_num,
        stat1_suffix=stat1_suffix,
        stat2_value=service_data["stat2_value"],
        stat2_label=service_data["stat2_label"],
        stat2_value_num=stat2_num,
        stat2_suffix=stat2_suffix,
        stat3_value=service_data["stat3_value"],
        stat3_label=service_data["stat3_label"],
        overview_title=service_data["overview_title"],
        overview_desc=service_data["overview_desc"],
        features_html=features_html,
        process_html=process_html,
        tech_tags_html=tech_tags_html,
        stats_html=stats_html,
        title_lower=service_data["title"].lower(),
    )
    return html


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for service_key, service_data in SERVICES.items():
        service_dir = os.path.join(base_dir, service_key)
        code_html_path = os.path.join(service_dir, "code.html")

        if not os.path.exists(service_dir):
            os.makedirs(service_dir)

        html_content = generate_service_page(service_key, service_data)

        with open(code_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Generated: {service_key}/code.html")

    print(f"\nDone! Generated {len(SERVICES)} service pages.")


if __name__ == "__main__":
    main()
