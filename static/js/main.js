$(document).ready(function() {
    // Initialize all components
    initializeNavigation();
    initializeFlashMessages();
    initializeSmoothScrolling();
    initializeLazyLoading();
    initializeAccessibility();
    
    // Initialize page-specific features
    if ($('.hero').length) {
        initializeHeroAnimations();
    }
    
    if ($('.timeline').length) {
        initializeTimeline();
    }
    
    if ($('.articles-grid').length) {
        initializeArticleCards();
    }
    
    if ($('.filters-form').length) {
        initializeFilters();
    }
    
    if ($('.contact-form').length) {
        initializeContactForm();
    }
    
    if ($('.faq-item').length) {
        initializeFAQ();
    }
    
    if ($('.modal').length) {
        initializeModals();
    }
    
    if ($('.newsletter-signup').length) {
        initializeNewsletter();
    }
    
    if ($('.footer-modern').length) {
        initializeFooter();
    }
});

// Navigation functionality
function initializeNavigation() {
    const navToggle = $('#nav-toggle');
    const navMenu = $('#nav-menu');
    
    // Mobile menu toggle
    navToggle.on('click', function() {
        $(this).toggleClass('active');
        navMenu.toggleClass('active');
        $('body').toggleClass('menu-open');
    });
    
    // Close mobile menu when clicking on a link
    $('.nav-link').on('click', function() {
        navToggle.removeClass('active');
        navMenu.removeClass('active');
        $('body').removeClass('menu-open');
    });
    
    // Close mobile menu when clicking outside
    $(document).on('click', function(e) {
        if (!$(e.target).closest('.navbar').length) {
            navToggle.removeClass('active');
            navMenu.removeClass('active');
            $('body').removeClass('menu-open');
        }
    });
    
    // Active navigation highlighting
    const currentPath = window.location.pathname;
    $('.nav-link').each(function() {
        const linkPath = $(this).attr('href');
        if (linkPath === currentPath || (currentPath === '/' && linkPath === '/')) {
            $(this).addClass('active');
        }
    });
    
    // Sticky header behavior
    let lastScrollTop = 0;
    const header = $('.header');
    
    $(window).on('scroll', function() {
        const scrollTop = $(this).scrollTop();
        
        if (scrollTop > 100) {
            header.addClass('scrolled');
        } else {
            header.removeClass('scrolled');
        }
        
        // Hide/show header on scroll
        if (scrollTop > lastScrollTop && scrollTop > 200) {
            header.addClass('header-hidden');
        } else {
            header.removeClass('header-hidden');
        }
        
        lastScrollTop = scrollTop;
    });
}

// Flash messages functionality
function initializeFlashMessages() {
    // Auto-hide flash messages after 5 seconds
    $('.flash-message').each(function() {
        const message = $(this);
        setTimeout(function() {
            message.fadeOut(300, function() {
                $(this).remove();
            });
        }, 5000);
    });
    
    // Manual close functionality
    $('.flash-close').on('click', function() {
        $(this).parent().fadeOut(300, function() {
            $(this).remove();
        });
    });
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    $('a[href^="#"]').on('click', function(e) {
        const target = $(this.getAttribute('href'));
        
        if (target.length) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: target.offset().top - 80
            }, 800, 'swing');
        }
    });
}

// Lazy loading for images
function initializeLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

// Accessibility enhancements
function initializeAccessibility() {
    // Skip link functionality
    $('.skip-link').on('click', function(e) {
        e.preventDefault();
        const target = $($(this).attr('href'));
        if (target.length) {
            target.focus();
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 300);
        }
    });
    
    // Keyboard navigation for custom elements
    $('.btn, .nav-link, .quick-link').on('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            $(this).click();
        }
    });
    
    // Focus management for modals
    $(document).on('keydown', function(e) {
        if (e.key === 'Escape') {
            $('.modal.active').each(function() {
                closeModal($(this));
            });
        }
    });
}

// Hero section animations
function initializeHeroAnimations() {
    // Animate hero elements on scroll
    const heroObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.hero-text, .hero-image').forEach(el => {
        heroObserver.observe(el);
    });
    
    // Parallax effect for hero background
    $(window).on('scroll', function() {
        const scrolled = $(window).scrollTop();
        const parallax = $('.hero');
        const speed = scrolled * 0.5;
        
        parallax.css('transform', `translateY(${speed}px)`);
    });
}

// Timeline functionality
function initializeTimeline() {
    const timelineObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, { threshold: 0.2 });
    
    document.querySelectorAll('.timeline-item').forEach(item => {
        timelineObserver.observe(item);
    });
}

// Article cards functionality
function initializeArticleCards() {
    // Hover effects for article cards
    $('.article-card').on('mouseenter', function() {
        $(this).addClass('hovered');
    }).on('mouseleave', function() {
        $(this).removeClass('hovered');
    });
    
    // Reading time estimation
    $('.article-preview').each(function() {
        const text = $(this).text();
        const wordsPerMinute = 200;
        const wordCount = text.split(' ').length;
        const readingTime = Math.ceil(wordCount / wordsPerMinute);
        
        $(this).siblings('.article-meta').append(
            `<span class="reading-time"><i class="fas fa-clock"></i> ${readingTime} min lectura</span>`
        );
    });
}

// Filters functionality
function initializeFilters() {
    const filterForm = $('.filters-form');
    const resourcesGrid = $('#resources-grid');
    
    // Real-time filtering
    filterForm.find('select').on('change', function() {
        const formData = filterForm.serialize();
        
        $.ajax({
            url: '/api/recursos',
            type: 'GET',
            data: formData,
            beforeSend: function() {
                resourcesGrid.addClass('loading');
            },
            success: function(data) {
                updateResourcesDisplay(data);
            },
            error: function() {
                showNotification('Error al cargar los recursos', 'error');
            },
            complete: function() {
                resourcesGrid.removeClass('loading');
            }
        });
    });
    
    // Clear filters
    $('.clear-filters').on('click', function() {
        filterForm[0].reset();
        filterForm.find('select').trigger('change');
    });
}

// Contact form functionality
function initializeContactForm() {
    const contactForm = $('.contact-form');
    
    contactForm.on('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const submitBtn = $(this).find('button[type="submit"]');
        const originalText = submitBtn.html();
        
        // Show loading state
        submitBtn.html('<i class="fas fa-spinner fa-spin"></i> Enviando...').prop('disabled', true);
        
        // Simulate form submission (replace with actual AJAX call)
        setTimeout(function() {
            showNotification('Mensaje enviado correctamente', 'success');
            contactForm[0].reset();
            submitBtn.html(originalText).prop('disabled', false);
        }, 2000);
    });
    
    // Form validation
    contactForm.find('input, textarea, select').on('blur', function() {
        validateField($(this));
    });
    
    // Real-time validation for email
    contactForm.find('input[type="email"]').on('input', function() {
        const email = $(this).val();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (email && !emailRegex.test(email)) {
            $(this).addClass('error');
            showFieldError($(this), 'Por favor, introduce un email válido');
        } else {
            $(this).removeClass('error');
            hideFieldError($(this));
        }
    });
}

// FAQ functionality
function initializeFAQ() {
    $('.faq-question').on('click', function() {
        const faqItem = $(this).parent();
        const answer = faqItem.find('.faq-answer');
        const icon = $(this).find('i');
        
        // Close other open FAQs
        $('.faq-item').not(faqItem).removeClass('active');
        $('.faq-answer').not(answer).slideUp(300);
        $('.faq-question i').not(icon).removeClass('fa-chevron-up').addClass('fa-chevron-down');
        
        // Toggle current FAQ
        faqItem.toggleClass('active');
        answer.slideToggle(300);
        icon.toggleClass('fa-chevron-down fa-chevron-up');
    });
}

// Modal functionality
function initializeModals() {
    // Open modal
    $(document).on('click', '[data-modal]', function(e) {
        e.preventDefault();
        const modalId = $(this).data('modal');
        openModal($(`#${modalId}`));
    });
    
    // Close modal
    $(document).on('click', '.modal-close, .modal-overlay', function() {
        closeModal($(this).closest('.modal'));
    });
    
    // Close modal with escape key
    $(document).on('keydown', function(e) {
        if (e.key === 'Escape') {
            $('.modal.active').each(function() {
                closeModal($(this));
            });
        }
    });
}

// Utility functions
function updateResourcesDisplay(resources) {
    const grid = $('#resources-grid');
    const count = $('#resources-count');
    
    count.text(resources.length);
    
    if (resources.length === 0) {
        grid.html(`
            <div class="no-resources">
                <i class="fas fa-search"></i>
                <h3>No se encontraron recursos</h3>
                <p>Intenta ajustar los filtros para encontrar más contenido.</p>
            </div>
        `);
        return;
    }
    
    let html = '';
    resources.forEach(function(resource) {
        html += generateResourceCard(resource);
    });
    
    grid.html(html);
}

function generateResourceCard(resource) {
    const typeIcon = getResourceTypeIcon(resource.tipo);
    const typeLabel = getResourceTypeLabel(resource.tipo);
    
    return `
        <div class="resource-card" data-type="${resource.tipo}">
            <div class="resource-header">
                <div class="resource-type">
                    <i class="${typeIcon}"></i> ${typeLabel}
                </div>
                <div class="resource-date">
                    ${resource.fecha_agregado.substring(0, 10)}
                </div>
            </div>
            
            <div class="resource-content">
                <h3>${resource.titulo}</h3>
                ${resource.descripcion ? `<p class="resource-description">${resource.descripcion}</p>` : ''}
                
                <div class="resource-meta">
                    ${generateMetaTags(resource)}
                </div>
                
                ${generateResourceContent(resource)}
            </div>
        </div>
    `;
}

function getResourceTypeIcon(type) {
    const icons = {
        'audio': 'fas fa-music',
        'video': 'fas fa-video',
        'partitura': 'fas fa-file-alt'
    };
    return icons[type] || 'fas fa-file';
}

function getResourceTypeLabel(type) {
    const labels = {
        'audio': 'Audio',
        'video': 'Video',
        'partitura': 'Partitura'
    };
    return labels[type] || 'Recurso';
}

function generateMetaTags(resource) {
    let tags = '';
    if (resource.epoca) {
        tags += `<span class="meta-tag"><i class="fas fa-clock"></i> ${resource.epoca}</span>`;
    }
    if (resource.tipo_canto) {
        tags += `<span class="meta-tag"><i class="fas fa-music"></i> ${resource.tipo_canto}</span>`;
    }
    if (resource.comunidad_monastica) {
        tags += `<span class="meta-tag"><i class="fas fa-church"></i> ${resource.comunidad_monastica}</span>`;
    }
    return tags;
}

function generateResourceContent(resource) {
    switch (resource.tipo) {
        case 'audio':
            return `
                <div class="audio-player">
                    <audio controls class="audio-controls">
                        ${resource.archivo_path ? `<source src="/static/audio/${resource.archivo_path}" type="audio/mpeg">` : ''}
                        ${resource.url_externa ? `<source src="${resource.url_externa}" type="audio/mpeg">` : ''}
                        Tu navegador no soporta el elemento de audio.
                    </audio>
                </div>
            `;
        case 'video':
            return `
                <div class="video-container">
                    ${resource.url_externa ? 
                        `<iframe src="${resource.url_externa}" frameborder="0" allowfullscreen></iframe>` :
                        `<div class="video-placeholder"><i class="fas fa-play-circle"></i><p>Video no disponible</p></div>`
                    }
                </div>
            `;
        case 'partitura':
            return `
                <div class="partitura-viewer">
                    <div class="partitura-content">
                        <i class="fas fa-file-pdf"></i>
                        <p>Partitura: ${resource.titulo}</p>
                        ${resource.archivo_path ? 
                            `<a href="/static/partituras/${resource.archivo_path}" target="_blank" class="btn btn-outline"><i class="fas fa-download"></i> Descargar</a>` :
                            resource.url_externa ?
                            `<a href="${resource.url_externa}" target="_blank" class="btn btn-outline"><i class="fas fa-external-link-alt"></i> Ver enlace</a>` :
                            `<p>Partitura no disponible</p>`
                        }
                    </div>
                </div>
            `;
        default:
            return '';
    }
}

function validateField(field) {
    const value = field.val().trim();
    const fieldType = field.attr('type');
    const isRequired = field.prop('required');
    
    if (isRequired && !value) {
        field.addClass('error');
        showFieldError(field, 'Este campo es obligatorio');
        return false;
    }
    
    if (fieldType === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            field.addClass('error');
            showFieldError(field, 'Por favor, introduce un email válido');
            return false;
        }
    }
    
    field.removeClass('error');
    hideFieldError(field);
    return true;
}

function showFieldError(field, message) {
    hideFieldError(field);
    field.after(`<div class="field-error">${message}</div>`);
}

function hideFieldError(field) {
    field.siblings('.field-error').remove();
}

function showNotification(message, type = 'info') {
    const notification = $(`
        <div class="notification notification-${type}">
            <i class="fas fa-${getNotificationIcon(type)}"></i>
            <span>${message}</span>
            <button class="notification-close">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `);
    
    $('body').append(notification);
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        notification.fadeOut(300, function() {
            $(this).remove();
        });
    }, 5000);
    
    // Manual close
    notification.find('.notification-close').on('click', function() {
        notification.fadeOut(300, function() {
            $(this).remove();
        });
    });
}

function getNotificationIcon(type) {
    const icons = {
        'success': 'check-circle',
        'error': 'exclamation-circle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle'
    };
    return icons[type] || 'info-circle';
}

function openModal(modal) {
    modal.addClass('active');
    $('body').addClass('modal-open');
    
    // Focus management
    const focusableElements = modal.find('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    if (focusableElements.length) {
        focusableElements.first().focus();
    }
}

function closeModal(modal) {
    modal.removeClass('active');
    $('body').removeClass('modal-open');
}

// Audio player enhancements
function initializeAudioPlayer() {
    $('audio').each(function() {
        const audio = $(this)[0];
        const container = $(this).closest('.audio-player');
        
        // Add custom controls
        const customControls = $(`
            <div class="custom-audio-controls">
                <button class="play-pause-btn">
                    <i class="fas fa-play"></i>
                </button>
                <div class="progress-container">
                    <div class="progress-bar">
                        <div class="progress"></div>
                    </div>
                </div>
                <div class="time-display">
                    <span class="current-time">0:00</span>
                    <span class="duration">0:00</span>
                </div>
                <button class="volume-btn">
                    <i class="fas fa-volume-up"></i>
                </button>
            </div>
        `);
        
        container.append(customControls);
        
        // Custom control functionality
        const playPauseBtn = container.find('.play-pause-btn');
        const progressBar = container.find('.progress');
        const currentTimeSpan = container.find('.current-time');
        const durationSpan = container.find('.duration');
        
        // Play/pause functionality
        playPauseBtn.on('click', function() {
            if (audio.paused) {
                audio.play();
                playPauseBtn.find('i').removeClass('fa-play').addClass('fa-pause');
            } else {
                audio.pause();
                playPauseBtn.find('i').removeClass('fa-pause').addClass('fa-play');
            }
        });
        
        // Update progress bar
        audio.addEventListener('timeupdate', function() {
            const progress = (audio.currentTime / audio.duration) * 100;
            progressBar.css('width', progress + '%');
            currentTimeSpan.text(formatTime(audio.currentTime));
        });
        
        // Update duration
        audio.addEventListener('loadedmetadata', function() {
            durationSpan.text(formatTime(audio.duration));
        });
        
        // Click on progress bar to seek
        container.find('.progress-container').on('click', function(e) {
            const rect = this.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const width = rect.width;
            const clickTime = (clickX / width) * audio.duration;
            audio.currentTime = clickTime;
        });
    });
}

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

// Search functionality
function initializeSearch() {
    const searchInput = $('.search-input');
    const searchResults = $('.search-results');
    
    if (searchInput.length) {
        let searchTimeout;
        
        searchInput.on('input', function() {
            const query = $(this).val().trim();
            
            clearTimeout(searchTimeout);
            
            if (query.length >= 2) {
                searchTimeout = setTimeout(() => {
                    performSearch(query);
                }, 300);
            } else {
                searchResults.hide();
            }
        });
    }
}

function performSearch(query) {
    // This would make an AJAX call to search the database
    // For now, we'll simulate search results
    const mockResults = [
        { title: 'Resultado 1', type: 'artículo', url: '#' },
        { title: 'Resultado 2', type: 'recurso', url: '#' },
        { title: 'Resultado 3', type: 'evento', url: '#' }
    ];
    
    const results = mockResults.filter(result => 
        result.title.toLowerCase().includes(query.toLowerCase())
    );
    
    displaySearchResults(results);
}

function displaySearchResults(results) {
    const searchResults = $('.search-results');
    
    if (results.length === 0) {
        searchResults.html('<div class="no-results">No se encontraron resultados</div>');
    } else {
        let html = '<ul class="search-results-list">';
        results.forEach(result => {
            html += `
                <li class="search-result-item">
                    <a href="${result.url}">
                        <span class="result-title">${result.title}</span>
                        <span class="result-type">${result.type}</span>
                    </a>
                </li>
            `;
        });
        html += '</ul>';
        searchResults.html(html);
    }
    
    searchResults.show();
}

// Performance monitoring
function initializePerformanceMonitoring() {
    // Monitor page load time
    window.addEventListener('load', function() {
        const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
        console.log(`Page load time: ${loadTime}ms`);
        
        // Report slow loading pages
        if (loadTime > 3000) {
            console.warn('Slow page load detected');
        }
    });
    
    // Monitor Core Web Vitals
    if ('web-vital' in window) {
        // This would integrate with a real web vitals library
        console.log('Web Vitals monitoring initialized');
    }
}

// Initialize performance monitoring
initializePerformanceMonitoring();

// Newsletter functionality
function initializeNewsletter() {
    $('.newsletter-btn').on('click', function() {
        const email = $('.newsletter-input').val();
        const btn = $(this);
        const originalHtml = btn.html();
        
        if (email && isValidEmail(email)) {
            btn.html('<i class="fas fa-spinner fa-spin"></i>').prop('disabled', true);
            
            // Simulate API call
            setTimeout(function() {
                btn.html('<i class="fas fa-check"></i>').removeClass('btn-primary').addClass('btn-success');
                $('.newsletter-input').val('').prop('disabled', true);
                
                // Show success message
                showNewsletterMessage('¡Gracias! Te has suscrito exitosamente.', 'success');
                
                // Reset after 3 seconds
                setTimeout(function() {
                    btn.html(originalHtml).removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
                    $('.newsletter-input').prop('disabled', false);
                }, 3000);
            }, 1500);
        } else {
            showNewsletterMessage('Por favor, ingresa un email válido.', 'error');
        }
    });
    
    // Newsletter input enter key
    $('.newsletter-input').on('keypress', function(e) {
        if (e.which === 13) {
            $('.newsletter-btn').click();
        }
    });
}

// Footer functionality
function initializeFooter() {
    // Footer animations on scroll
    $(window).on('scroll', function() {
        const footer = $('.footer-modern');
        const footerTop = footer.offset().top;
        const windowBottom = $(window).scrollTop() + $(window).height();
        
        if (windowBottom > footerTop - 200) {
            footer.addClass('animate-in');
        }
    });
    
    // Social media link tracking (analytics)
    $('.social-link').on('click', function() {
        const platform = $(this).attr('class').split(' ')[1]; // Get platform from class
        console.log(`Social media click: ${platform}`);
        // Here you would send analytics data
    });
    
    // Contact info click tracking
    $('.contact-value').on('click', function() {
        const contactType = $(this).closest('.contact-item').find('.contact-label').text();
        console.log(`Contact click: ${contactType}`);
        // Here you would send analytics data
    });
}

// Helper functions for newsletter
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function showNewsletterMessage(message, type) {
    const alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
    const icon = type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle';
    
    const alertHtml = `
        <div class="alert ${alertClass} alert-dismissible fade show mt-3" role="alert">
            <i class="fas ${icon} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    $('.newsletter-signup').append(alertHtml);
    
    // Auto-dismiss after 5 seconds
    setTimeout(function() {
        $('.newsletter-signup .alert').fadeOut();
    }, 5000);
}
