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
  // 2. STICKY NAVBAR & SCROLL EFFECTS
  // ==========================================================================
  const navbar = document.getElementById('navbar');
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
    const overlay = document.getElementById('mobileOverlay');
    if (overlay) overlay.classList.toggle('open');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }

  function closeMobileMenu() {
    mobileNavDrawer.classList.remove('open');
    mobileMenuBtn.classList.remove('active');
    mobileMenuBtn.setAttribute('aria-expanded', 'false');
    const overlay = document.getElementById('mobileOverlay');
    if (overlay) overlay.classList.remove('open');
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

    // Close on close button click
    const mobileCloseBtn = document.getElementById('mobileCloseBtn');
    if (mobileCloseBtn) {
      mobileCloseBtn.addEventListener('click', closeMobileMenu);
    }

    // Close on overlay click
    const mobileOverlay = document.getElementById('mobileOverlay');
    if (mobileOverlay) {
      mobileOverlay.addEventListener('click', closeMobileMenu);
    }
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
            ctx.strokeStyle = `rgba(37, 99, 235, ${lineAlpha})`;
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
        ctx.fillStyle = `rgba(37, 99, 235, ${p.alpha * 0.2})`;
        ctx.fill();

        // Inner solid node
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(37, 99, 235, ${p.alpha * 0.6})`;
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
  const jobApplicationForm = document.getElementById('jobApplicationForm');
  const jobSuccessBox = document.getElementById('jobSuccessBox');
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

  // ==========================================================================
  // PARTICLES ANIMATION
  // ==========================================================================
  const particlesCanvas = document.getElementById('particlesCanvas');
  if (particlesCanvas) {
    const ctx = particlesCanvas.getContext('2d');
    let particles = [];
    let animationId;

    function resizeCanvas() {
      const section = particlesCanvas.parentElement;
      particlesCanvas.width = section.offsetWidth;
      particlesCanvas.height = section.offsetHeight;
    }

    class Particle {
      constructor() {
        this.reset();
      }

      reset() {
        this.x = Math.random() * particlesCanvas.width;
        this.y = Math.random() * particlesCanvas.height;
        this.size = Math.random() * 1.5 + 0.5;
        this.speedX = (Math.random() - 0.5) * 0.3;
        this.speedY = (Math.random() - 0.5) * 0.3;
        this.opacity = Math.random() * 0.4 + 0.1;
        this.fadeSpeed = Math.random() * 0.005 + 0.002;
        this.fadingIn = Math.random() > 0.5;
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.fadingIn) {
          this.opacity += this.fadeSpeed;
          if (this.opacity >= 0.5) this.fadingIn = false;
        } else {
          this.opacity -= this.fadeSpeed;
          if (this.opacity <= 0.05) this.fadingIn = true;
        }

        if (this.x < 0 || this.x > particlesCanvas.width ||
            this.y < 0 || this.y > particlesCanvas.height) {
          this.reset();
        }
      }

      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(37, 99, 235, ${this.opacity * 0.6})`;
        ctx.fill();
      }
    }

    function initParticles() {
      particles = [];
      const count = Math.min(60, Math.floor((particlesCanvas.width * particlesCanvas.height) / 15000));
      for (let i = 0; i < count; i++) {
        particles.push(new Particle());
      }
    }

    function connectParticles() {
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 120) {
            const opacity = (1 - dist / 120) * 0.08;
            ctx.beginPath();
            ctx.strokeStyle = `rgba(37, 99, 235, ${opacity * 0.6})`;
            ctx.lineWidth = 0.5;
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.stroke();
          }
        }
      }
    }

    function animateParticles() {
      ctx.clearRect(0, 0, particlesCanvas.width, particlesCanvas.height);
      particles.forEach(p => {
        p.update();
        p.draw();
      });
      connectParticles();
      animationId = requestAnimationFrame(animateParticles);
    }

    resizeCanvas();
    initParticles();
    animateParticles();

    window.addEventListener('resize', () => {
      resizeCanvas();
      initParticles();
    });
  }


  // ==========================================================================
  // LOCATION MAP SHOWCASE SWITCHER
  // ==========================================================================
  const officeLocations = {
    hyderabad: {
      title: "Madhapur, Hyderabad",
      subtitle: "Telangana, India • Registered Headquarters",
      hours: "Working Hours: Mon – Sat | 9:30 AM – 7:00 PM IST",
      directionsUrl: "https://www.google.com/maps/dir/?api=1&destination=Second+Floor,+Samridhi+Vasyam,+D+No+1%2F98%2F9%2F3%2F23,+Capital+Pk+Rd,+beside+Narayana+High+School,+Cyber+Hills+Colony,+VIP+Hills,+Jaihind+Enclave,+Madhapur,+Hyderabad,+Telangana+500081",
      embedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3806.326500057038!2d78.38421867591656!3d17.444078701168175!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb93dc8c5d69df%3A0x19688ebb557fa321!2sMadhapur%2C%20Hyderabad%2C%20Telangana!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin",
      dotClass: "map-dot"
    },
    vijayawada: {
      title: "Vijayawada, NTR District",
      subtitle: "Andhra Pradesh, India • Regional Office",
      hours: "Working Hours: Mon – Sat | 9:30 AM – 7:00 PM IST",
      directionsUrl: "https://www.google.com/maps/search/D.No.+24-29-210A,+Durgapuram,+Gulabithota+Road,+Vijayawada,+NTR+District,+Andhra+Pradesh+520003",
      embedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d61205.47414902251!2d80.612025!3d16.506174!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a35eff9482d944b%3A0x939b7e84ab4a0265!2sVijayawada%2C%20Andhra%20Pradesh!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin",
      dotClass: "map-dot map-dot--alt"
    },
    southafrica: {
      title: "Newcastle, KwaZulu-Natal",
      subtitle: "South Africa • International Branch (PTY LTD)",
      hours: "Working Hours: Mon – Sat | 9:30 AM – 7:00 PM SAST",
      directionsUrl: "https://www.google.com/maps/search/Unit+11+Sunset+View+10+Hazy+Street+Newcastle+Kwa-Zulu+Natal+2930+South+Africa",
      embedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d56466.50741273015!2d29.928!3d-27.747!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1ef467a34b1a70e3%3A0x1597d6d96e6b20c6!2sNewcastle%2C%20KwaZulu-Natal!5e0!3m2!1sen!2sza!4v1700000000000!5m2!1sen!2sza",
      dotClass: "map-dot"
    }
  };

  const activeMapTitle = document.getElementById('activeMapTitle');
  const activeMapSubtitle = document.getElementById('activeMapSubtitle');
  const activeMapHours = document.getElementById('activeMapHours');
  const activeMapLink = document.getElementById('activeMapLink');
  const activeDirectionsBtn = document.getElementById('activeDirectionsBtn');
  const activeMapIframe = document.getElementById('activeMapIframe');
  const activeMapDot = document.getElementById('activeMapDot');
  const officeCards = document.querySelectorAll('.location-office-card');
  const mapTabBtns = document.querySelectorAll('.map-tab-btn');

  window.switchOfficeLocation = switchOfficeLocation;
  function switchOfficeLocation(locKey) {
    const loc = officeLocations[locKey];
    if (!loc) return;

    if (activeMapTitle) activeMapTitle.textContent = loc.title;
    if (activeMapSubtitle) activeMapSubtitle.textContent = loc.subtitle;
    if (activeMapHours) activeMapHours.textContent = loc.hours;
    if (activeMapLink) activeMapLink.href = loc.directionsUrl;
    if (activeDirectionsBtn) activeDirectionsBtn.href = loc.directionsUrl;
    if (activeMapDot) activeMapDot.className = loc.dotClass;

    // Instantly toggle multi-iframe active state
    const iframes = document.querySelectorAll('.office-map-iframe');
    if (iframes.length > 0) {
      iframes.forEach(iframe => {
        iframe.classList.remove('active');
      });
      const targetIframe = document.getElementById('iframe-' + locKey);
      if (targetIframe) {
        targetIframe.classList.add('active');
      }
    } else if (activeMapIframe && activeMapIframe.src !== loc.embedUrl) {
      activeMapIframe.src = loc.embedUrl;
    }

    officeCards.forEach(card => {
      card.classList.toggle('active', card.getAttribute('data-location') === locKey);
    });

    mapTabBtns.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-target') === locKey);
    });
  }

  officeCards.forEach(card => {
    card.addEventListener('click', () => {
      const locKey = card.getAttribute('data-location');
      switchOfficeLocation(locKey);
      const showcase = document.querySelector('.map-showcase-card');
      if (showcase && window.innerWidth <= 768) {
        showcase.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const locKey = card.getAttribute('data-location');
        switchOfficeLocation(locKey);
      }
    });
  });

  mapTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-target');
      switchOfficeLocation(target);
    });
  });

});
