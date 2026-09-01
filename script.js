/**
 * OKLUT Innovative & Digital Excellence
 * Main Interactive JavaScript
 * Vanilla JS only - No external libraries
 */

document.addEventListener('DOMContentLoaded', () => {

  // ==========================================================================
  // 1. ANIMATED SERVICE TEXT ROTATOR (Every 2 seconds)
  // ==========================================================================
  const rotatingServices = [
    "PERFORMANCE MARKETING",
    "SOCIAL MEDIA MARKETING",
    "SEO",
    "AEO",
    "GEO",
    "INFLUENCER MARKETING",
    "PERSONAL BRANDING",
    "AI COLD CALLING",
    "WEB DEVELOPMENT",
    "APP DEVELOPMENT"
  ];

  const rotatingTextEl = document.getElementById('rotatingServiceText');
  let currentServiceIndex = 0;

  function cycleServiceText() {
    if (!rotatingTextEl) return;

    // Exit animation (slide up, fade out, scale down)
    rotatingTextEl.style.opacity = '0';
    rotatingTextEl.style.transform = 'translateY(-16px) scale(0.96)';

    setTimeout(() => {
      currentServiceIndex = (currentServiceIndex + 1) % rotatingServices.length;
      rotatingTextEl.textContent = rotatingServices[currentServiceIndex];

      // Prepare from bottom
      rotatingTextEl.style.transform = 'translateY(16px) scale(0.96)';

      // Trigger reflow
      void rotatingTextEl.offsetWidth;

      // Enter animation (slide to center, fade in, scale normal)
      rotatingTextEl.style.opacity = '1';
      rotatingTextEl.style.transform = 'translateY(0) scale(1)';
    }, 350);
  }

  // Initial style setup
  if (rotatingTextEl) {
    rotatingTextEl.style.transition = 'opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1)';
    setInterval(cycleServiceText, 2000);
  }


  // ==========================================================================
  // 2. STICKY NAVBAR & ACTIVE SCROLL SPY
  // ==========================================================================
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
  const sections = document.querySelectorAll('section[id]');
  const backToTopBtn = document.getElementById('backToTopBtn');

  function handleScroll() {
    const scrollY = window.scrollY;

    // Sticky navbar backdrop styling
    if (scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Back to top button visibility
    if (scrollY > 400) {
      backToTopBtn.classList.add('show');
    } else {
      backToTopBtn.classList.remove('show');
    }

    // Scroll spy for active navigation item
    let currentActiveSection = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        currentActiveSection = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentActiveSection}`) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }


  // ==========================================================================
  // 3. MOBILE MENU & ACCORDION
  // ==========================================================================
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const mobileServicesToggle = document.getElementById('mobileServicesToggle');
  const mobileAccordionItem = mobileServicesToggle ? mobileServicesToggle.closest('.mobile-accordion-item') : null;
  const mobileLinks = document.querySelectorAll('.mobile-nav-link, .mobile-service-link');

  function toggleMobileMenu() {
    const isOpen = mobileNavDrawer.classList.toggle('open');
    mobileMenuBtn.classList.toggle('active');
    mobileMenuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }

  function closeMobileMenu() {
    mobileNavDrawer.classList.remove('open');
    mobileMenuBtn.classList.remove('active');
    mobileMenuBtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (mobileMenuBtn && mobileNavDrawer) {
    mobileMenuBtn.addEventListener('click', toggleMobileMenu);

    // Close on navigation link click
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        closeMobileMenu();
      });
    });
  }

  // Mobile Services Accordion
  if (mobileServicesToggle && mobileAccordionItem) {
    mobileServicesToggle.addEventListener('click', (e) => {
      e.preventDefault();
      mobileAccordionItem.classList.toggle('active');
    });
  }


  // ==========================================================================
  // 4. DESKTOP SERVICES MEGA MENU HOVER & CLICK HANDLERS
  // ==========================================================================
  const servicesDropdownItem = document.getElementById('servicesDropdownItem');
  const servicesToggleBtn = document.getElementById('servicesToggleBtn');
  const serviceMegaLinks = document.querySelectorAll('[data-service]');
  const contactServiceSelect = document.getElementById('contactService');

  if (servicesToggleBtn && servicesDropdownItem) {
    servicesToggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const isOpen = servicesDropdownItem.classList.toggle('open');
      servicesToggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close dropdown on clicking outside
    document.addEventListener('click', (e) => {
      if (!servicesDropdownItem.contains(e.target)) {
        servicesDropdownItem.classList.remove('open');
        servicesToggleBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // When clicking on any service link (desktop or mobile), pre-select in contact form
  serviceMegaLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const selectedService = this.getAttribute('data-service');
      if (contactServiceSelect && selectedService) {
        for (let i = 0; i < contactServiceSelect.options.length; i++) {
          if (contactServiceSelect.options[i].value.toLowerCase() === selectedService.toLowerCase()) {
            contactServiceSelect.selectedIndex = i;
            break;
          }
        }
      }
      if (servicesDropdownItem) {
        servicesDropdownItem.classList.remove('open');
      }
    });
  });


  // ==========================================================================
  // 5. GLOBAL NETWORK / DIGITAL EARTH CANVAS VISUALIZATION (ABOUT US)
  // ==========================================================================
  const canvas = document.getElementById('globeNetworkCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width, height;
    let nodes = [];
    const totalNodes = 36;
    let angleOffset = 0;

    function resizeCanvas() {
      width = canvas.width = canvas.parentElement.offsetWidth;
      height = canvas.height = canvas.parentElement.offsetHeight;
      initNodes();
    }

    function initNodes() {
      nodes = [];
      const centerX = width / 2;
      const centerY = height / 2;
      const maxRadius = Math.min(width, height) * 0.42;

      for (let i = 0; i < totalNodes; i++) {
        const phi = Math.acos(-1 + (2 * i) / totalNodes);
        const theta = Math.sqrt(totalNodes * Math.PI) * phi;

        nodes.push({
          x3d: maxRadius * Math.cos(theta) * Math.sin(phi),
          y3d: maxRadius * Math.sin(theta) * Math.sin(phi),
          z3d: maxRadius * Math.cos(phi),
          baseRadius: 2.5 + Math.random() * 2,
          pulseSpeed: 0.02 + Math.random() * 0.03,
          pulse: Math.random() * Math.PI
        });
      }
    }

    function animateGlobe() {
      ctx.clearRect(0, 0, width, height);

      const centerX = width / 2;
      const centerY = height / 2;
      angleOffset += 0.0035;

      const cosAngle = Math.cos(angleOffset);
      const sinAngle = Math.sin(angleOffset);

      // Project 3D nodes to 2D screen
      const projected = nodes.map(node => {
        // Rotate around Y axis
        const rotX = node.x3d * cosAngle - node.z3d * sinAngle;
        const rotZ = node.x3d * sinAngle + node.z3d * cosAngle;
        const rotY = node.y3d;

        // Perspective scale
        const fov = 400;
        const scale = fov / (fov + rotZ);
        const x2d = centerX + rotX * scale;
        const y2d = centerY + rotY * scale;

        node.pulse += node.pulseSpeed;
        const alpha = Math.max(0.15, (rotZ + 200) / 400);

        return {
          x: x2d,
          y: y2d,
          z: rotZ,
          scale: scale,
          alpha: alpha,
          radius: node.baseRadius * scale * (1 + 0.2 * Math.sin(node.pulse))
        };
      });

      // Draw connection lines between nearby nodes
      for (let i = 0; i < projected.length; i++) {
        for (let j = i + 1; j < projected.length; j++) {
          const dx = projected[i].x - projected[j].x;
          const dy = projected[i].y - projected[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 110) {
            const lineAlpha = (1 - dist / 110) * projected[i].alpha * projected[j].alpha * 0.35;
            ctx.beginPath();
            ctx.moveTo(projected[i].x, projected[i].y);
            ctx.lineTo(projected[j].x, projected[j].y);
            ctx.strokeStyle = `rgba(56, 189, 248, ${lineAlpha})`;
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      }

      // Draw glowing nodes
      projected.forEach(p => {
        // Outer glow
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius * 2, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 168, 255, ${p.alpha * 0.25})`;
        ctx.fill();

        // Inner solid node
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${p.alpha * 0.95})`;
        ctx.fill();
      });

      requestAnimationFrame(animateGlobe);
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    animateGlobe();
  }


  // ==========================================================================
  // 6. MODALS MANAGEMENT (ABOUT US & JOB APPLICATION)
  // ==========================================================================
  
  // More About Us Modal
  const aboutModal = document.getElementById('aboutModal');
  const moreAboutUsBtn = document.getElementById('moreAboutUsBtn');
  const closeAboutModalBtn = document.getElementById('closeAboutModalBtn');
  const aboutModalBackdrop = document.getElementById('aboutModalBackdrop');
  const modalExploreServicesBtn = document.getElementById('modalExploreServicesBtn');

  function openAboutModal() {
    if (aboutModal) {
      aboutModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeAboutModal() {
    if (aboutModal) {
      aboutModal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  if (moreAboutUsBtn) moreAboutUsBtn.addEventListener('click', openAboutModal);
  if (closeAboutModalBtn) closeAboutModalBtn.addEventListener('click', closeAboutModal);
  if (aboutModalBackdrop) aboutModalBackdrop.addEventListener('click', closeAboutModal);
  if (modalExploreServicesBtn) {
    modalExploreServicesBtn.addEventListener('click', () => {
      closeAboutModal();
    });
  }

  // Job Application Modal
  const jobModal = document.getElementById('jobModal');
  const closeJobModalBtn = document.getElementById('closeJobModalBtn');
  const jobModalBackdrop = document.getElementById('jobModalBackdrop');
  const modalJobPosition = document.getElementById('modalJobPosition');
  const applyJobBtns = document.querySelectorAll('.btn-apply-job');
  const jobApplicationForm = document.getElementById('jobApplicationForm');
  const jobSuccessBox = document.getElementById('jobSuccessBox');

  function openJobModal(jobTitle) {
    if (jobModal) {
      if (modalJobPosition) modalJobPosition.value = jobTitle || 'Digital Marketing Specialist';
      if (jobSuccessBox) jobSuccessBox.classList.remove('show');
      jobModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeJobModal() {
    if (jobModal) {
      jobModal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  applyJobBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const title = this.getAttribute('data-job') || this.closest('.job-card').querySelector('.job-title').textContent;
      openJobModal(title);
    });
  });

  if (closeJobModalBtn) closeJobModalBtn.addEventListener('click', closeJobModal);
  if (jobModalBackdrop) jobModalBackdrop.addEventListener('click', closeJobModal);

  // Global ESC Key Closes Any Open Modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAboutModal();
      closeJobModal();
      closeMobileMenu();
    }
  });


  // ==========================================================================
  // 7. CLIENT-SIDE VALIDATION FOR CONTACT FORM
  // ==========================================================================
  const contactForm = document.getElementById('contactForm');
  const nameInput = document.getElementById('contactName');
  const emailInput = document.getElementById('contactEmail');
  const phoneInput = document.getElementById('contactPhone');
  const serviceInput = document.getElementById('contactService');
  const submitBtn = document.getElementById('submitBtn');
  const formSuccessBox = document.getElementById('formSuccessBox');

  const nameError = document.getElementById('nameError');
  const emailError = document.getElementById('emailError');
  const phoneError = document.getElementById('phoneError');
  const serviceError = document.getElementById('serviceError');

  function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }

  function isValidPhone(phone) {
    const cleaned = phone.replace(/[\s\-\+\(\)]/g, '');
    return cleaned.length >= 10;
  }

  function validateContactForm() {
    let isValid = true;

    // Validate Name
    if (!nameInput.value.trim()) {
      nameInput.classList.add('is-invalid');
      nameError.classList.add('show');
      isValid = false;
    } else {
      nameInput.classList.remove('is-invalid');
      nameError.classList.remove('show');
    }

    // Validate Email
    if (!emailInput.value.trim() || !isValidEmail(emailInput.value.trim())) {
      emailInput.classList.add('is-invalid');
      emailError.classList.add('show');
      isValid = false;
    } else {
      emailInput.classList.remove('is-invalid');
      emailError.classList.remove('show');
    }

    // Validate Phone
    if (!phoneInput.value.trim() || !isValidPhone(phoneInput.value.trim())) {
      phoneInput.classList.add('is-invalid');
      phoneError.classList.add('show');
      isValid = false;
    } else {
      phoneInput.classList.remove('is-invalid');
      phoneError.classList.remove('show');
    }

    // Validate Service
    if (!serviceInput.value) {
      serviceInput.classList.add('is-invalid');
      serviceError.classList.add('show');
      isValid = false;
    } else {
      serviceInput.classList.remove('is-invalid');
      serviceError.classList.remove('show');
    }

    return isValid;
  }

  // Clear errors on input
  [nameInput, emailInput, phoneInput, serviceInput].forEach(field => {
    if (field) {
      field.addEventListener('input', () => {
        field.classList.remove('is-invalid');
        const errEl = document.getElementById(`${field.name || field.id.replace('contact', '').toLowerCase()}Error`);
        if (errEl) errEl.classList.remove('show');
      });
    }
  });

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      if (!validateContactForm()) {
        return;
      }

      // Simulate loading state
      if (submitBtn) submitBtn.classList.add('loading');

      setTimeout(() => {
        if (submitBtn) submitBtn.classList.remove('loading');
        if (formSuccessBox) {
          formSuccessBox.classList.add('show');
          contactForm.reset();

          // Smooth scroll to success box if needed
          formSuccessBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }, 700);
    });
  }


  // ==========================================================================
  // 8. CLIENT-SIDE VALIDATION FOR JOB APPLICATION FORM
  // ==========================================================================
  if (jobApplicationForm) {
    const applicantName = document.getElementById('applicantName');
    const applicantEmail = document.getElementById('applicantEmail');
    const applicantPhone = document.getElementById('applicantPhone');
    const submitAppBtn = document.getElementById('submitAppBtn');

    const applicantNameError = document.getElementById('applicantNameError');
    const applicantEmailError = document.getElementById('applicantEmailError');
    const applicantPhoneError = document.getElementById('applicantPhoneError');

    jobApplicationForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let isJobFormValid = true;

      if (!applicantName.value.trim()) {
        applicantName.classList.add('is-invalid');
        applicantNameError.classList.add('show');
        isJobFormValid = false;
      } else {
        applicantName.classList.remove('is-invalid');
        applicantNameError.classList.remove('show');
      }

      if (!applicantEmail.value.trim() || !isValidEmail(applicantEmail.value.trim())) {
        applicantEmail.classList.add('is-invalid');
        applicantEmailError.classList.add('show');
        isJobFormValid = false;
      } else {
        applicantEmail.classList.remove('is-invalid');
        applicantEmailError.classList.remove('show');
      }

      if (!applicantPhone.value.trim() || !isValidPhone(applicantPhone.value.trim())) {
        applicantPhone.classList.add('is-invalid');
        applicantPhoneError.classList.add('show');
        isJobFormValid = false;
      } else {
        applicantPhone.classList.remove('is-invalid');
        applicantPhoneError.classList.remove('show');
      }

      if (!isJobFormValid) return;

      if (submitAppBtn) submitAppBtn.classList.add('loading');

      setTimeout(() => {
        if (submitAppBtn) submitAppBtn.classList.remove('loading');
        if (jobSuccessBox) {
          jobSuccessBox.classList.add('show');
          jobApplicationForm.reset();
        }
      }, 700);
    });
  }

});
