// CV Builder JavaScript
let experienceCount = 0;
let educationCount = 0;
let skills = {
    technical: [],
    soft: [],
    language: []
};

// Initialize the form
document.addEventListener('DOMContentLoaded', function() {
    // Add initial experience and education sections
    addExperience();
    addEducation();
    
    // Add form submit handler
    document.getElementById('cvForm').addEventListener('submit', handleSubmit);
    
    // Add enter key handlers for skill inputs
    document.getElementById('technicalSkillInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            addSkill('technical');
        }
    });
    
    document.getElementById('softSkillInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            addSkill('soft');
        }
    });
    
    document.getElementById('languageInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            addSkill('language');
        }
    });
});

function addExperience() {
    experienceCount++;
    const experienceHTML = `
        <div class="experience-item bg-gray-50 p-6 rounded-lg border border-gray-200" data-id="${experienceCount}">
            <div class="flex justify-between items-start mb-4">
                <h3 class="text-lg font-semibold text-gray-800">Experience ${experienceCount}</h3>
                <button type="button" onclick="removeExperience(${experienceCount})" 
                        class="text-red-500 hover:text-red-700 transition">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Job Title *</label>
                    <input type="text" name="exp_title_${experienceCount}" required 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Company *</label>
                    <input type="text" name="exp_company_${experienceCount}" required 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Location</label>
                    <input type="text" name="exp_location_${experienceCount}" 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Duration</label>
                    <input type="text" name="exp_duration_${experienceCount}" placeholder="e.g., Jan 2020 - Present" 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
            </div>
            <div class="mt-4">
                <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
                <textarea name="exp_description_${experienceCount}" rows="3" 
                          class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"></textarea>
            </div>
        </div>
    `;
    
    document.getElementById('experienceList').insertAdjacentHTML('beforeend', experienceHTML);
}

function removeExperience(id) {
    const element = document.querySelector(`.experience-item[data-id="${id}"]`);
    if (element) {
        element.remove();
    }
}

function addEducation() {
    educationCount++;
    const educationHTML = `
        <div class="education-item bg-gray-50 p-6 rounded-lg border border-gray-200" data-id="${educationCount}">
            <div class="flex justify-between items-start mb-4">
                <h3 class="text-lg font-semibold text-gray-800">Education ${educationCount}</h3>
                <button type="button" onclick="removeEducation(${educationCount})" 
                        class="text-red-500 hover:text-red-700 transition">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Degree *</label>
                    <input type="text" name="edu_degree_${educationCount}" required 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Institution *</label>
                    <input type="text" name="edu_institution_${educationCount}" required 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Location</label>
                    <input type="text" name="edu_location_${educationCount}" 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Duration</label>
                    <input type="text" name="edu_duration_${educationCount}" placeholder="e.g., 2016 - 2020" 
                           class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent">
                </div>
            </div>
            <div class="mt-4">
                <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
                <textarea name="edu_description_${educationCount}" rows="2" 
                          class="form-input w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"></textarea>
            </div>
        </div>
    `;
    
    document.getElementById('educationList').insertAdjacentHTML('beforeend', educationHTML);
}

function removeEducation(id) {
    const element = document.querySelector(`.education-item[data-id="${id}"]`);
    if (element) {
        element.remove();
    }
}

function addSkill(type) {
    const inputId = type + 'SkillInput';
    const containerId = type + 'Skills';
    const input = document.getElementById(inputId);
    const container = document.getElementById(containerId);
    
    if (input.value.trim() === '') return;
    
    const skill = input.value.trim();
    
    // Check if skill already exists
    if (skills[type].includes(skill)) {
        showNotification('This skill already exists!', 'warning');
        return;
    }
    
    skills[type].push(skill);
    
    const skillHTML = `
        <span class="skill-tag inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-purple-100 text-purple-800 cursor-pointer" onclick="removeSkill('${type}', '${skill}')">
            ${skill}
            <i class="fas fa-times ml-2 text-xs"></i>
        </span>
    `;
    
    container.insertAdjacentHTML('beforeend', skillHTML);
    input.value = '';
}

function removeSkill(type, skill) {
    const index = skills[type].indexOf(skill);
    if (index > -1) {
        skills[type].splice(index, 1);
        updateSkillsDisplay(type);
    }
}

function updateSkillsDisplay(type) {
    const container = document.getElementById(type + 'Skills');
    container.innerHTML = '';
    
    skills[type].forEach(skill => {
        const skillHTML = `
            <span class="skill-tag inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-purple-100 text-purple-800 cursor-pointer" onclick="removeSkill('${type}', '${skill}')">
                ${skill}
                <i class="fas fa-times ml-2 text-xs"></i>
            </span>
        `;
        container.insertAdjacentHTML('beforeend', skillHTML);
    });
}

function handleSubmit(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = new FormData(e.target);
    const cvData = {
        personal: {
            fullName: formData.get('fullName'),
            title: formData.get('title'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            location: formData.get('location'),
            portfolio: formData.get('portfolio'),
            summary: formData.get('summary')
        },
        experience: [],
        education: [],
        skills: skills
    };
    
    // Collect experience data
    for (let i = 1; i <= experienceCount; i++) {
        const title = formData.get(`exp_title_${i}`);
        if (title) {
            cvData.experience.push({
                title: title,
                company: formData.get(`exp_company_${i}`),
                location: formData.get(`exp_location_${i}`),
                duration: formData.get(`exp_duration_${i}`),
                description: formData.get(`exp_description_${i}`)
            });
        }
    }
    
    // Collect education data
    for (let i = 1; i <= educationCount; i++) {
        const degree = formData.get(`edu_degree_${i}`);
        if (degree) {
            cvData.education.push({
                degree: degree,
                institution: formData.get(`edu_institution_${i}`),
                location: formData.get(`edu_location_${i}`),
                duration: formData.get(`edu_duration_${i}`),
                description: formData.get(`edu_description_${i}`)
            });
        }
    }
    
    // Generate CV preview
    generateCVPreview(cvData);
    
    // Show success message
    showNotification('CV generated successfully!', 'success');
}

function generateCVPreview(data) {
    const previewContent = document.getElementById('previewContent');
    
    let html = `
        <div class="cv-preview bg-white">
            <!-- Header -->
            <div class="border-b-4 border-purple-600 pb-6 mb-6">
                <h1 class="text-3xl font-bold text-gray-800 mb-2">${data.personal.fullName || 'Your Name'}</h1>
                <p class="text-xl text-gray-600 mb-4">${data.personal.title || 'Professional Title'}</p>
                <div class="flex flex-wrap gap-4 text-sm text-gray-600">
                    ${data.personal.email ? `<span><i class="fas fa-envelope mr-1"></i>${data.personal.email}</span>` : ''}
                    ${data.personal.phone ? `<span><i class="fas fa-phone mr-1"></i>${data.personal.phone}</span>` : ''}
                    ${data.personal.location ? `<span><i class="fas fa-map-marker-alt mr-1"></i>${data.personal.location}</span>` : ''}
                    ${data.personal.portfolio ? `<span><i class="fas fa-globe mr-1"></i>${data.personal.portfolio}</span>` : ''}
                </div>
            </div>
    `;
    
    if (data.personal.summary) {
        html += `
            <div class="mb-6">
                <h2 class="text-xl font-bold text-gray-800 mb-3 border-b-2 border-purple-600 pb-1">Professional Summary</h2>
                <p class="text-gray-700">${data.personal.summary}</p>
            </div>
        `;
    }
    
    if (data.experience.length > 0) {
        html += `
            <div class="mb-6">
                <h2 class="text-xl font-bold text-gray-800 mb-3 border-b-2 border-purple-600 pb-1">Work Experience</h2>
                <div class="space-y-4">
        `;
        
        data.experience.forEach(exp => {
            html += `
                <div>
                    <div class="flex justify-between items-start mb-2">
                        <div>
                            <h3 class="font-semibold text-gray-800">${exp.title}</h3>
                            <p class="text-gray-600">${exp.company}</p>
                        </div>
                        <div class="text-right text-sm text-gray-600">
                            ${exp.duration ? `<p>${exp.duration}</p>` : ''}
                            ${exp.location ? `<p>${exp.location}</p>` : ''}
                        </div>
                    </div>
                    ${exp.description ? `<p class="text-gray-700 text-sm">${exp.description}</p>` : ''}
                </div>
            `;
        });
        
        html += `
                </div>
            </div>
        `;
    }
    
    if (data.education.length > 0) {
        html += `
            <div class="mb-6">
                <h2 class="text-xl font-bold text-gray-800 mb-3 border-b-2 border-purple-600 pb-1">Education</h2>
                <div class="space-y-4">
        `;
        
        data.education.forEach(edu => {
            html += `
                <div>
                    <div class="flex justify-between items-start mb-2">
                        <div>
                            <h3 class="font-semibold text-gray-800">${edu.degree}</h3>
                            <p class="text-gray-600">${edu.institution}</p>
                        </div>
                        <div class="text-right text-sm text-gray-600">
                            ${edu.duration ? `<p>${edu.duration}</p>` : ''}
                            ${edu.location ? `<p>${edu.location}</p>` : ''}
                        </div>
                    </div>
                    ${edu.description ? `<p class="text-gray-700 text-sm">${edu.description}</p>` : ''}
                </div>
            `;
        });
        
        html += `
                </div>
            </div>
        `;
    }
    
    // Skills section
    const hasSkills = skills.technical.length > 0 || skills.soft.length > 0 || skills.language.length > 0;
    if (hasSkills) {
        html += `
            <div class="mb-6">
                <h2 class="text-xl font-bold text-gray-800 mb-3 border-b-2 border-purple-600 pb-1">Skills</h2>
        `;
        
        if (skills.technical.length > 0) {
            html += `
                <div class="mb-3">
                    <h3 class="font-semibold text-gray-700 mb-2">Technical Skills:</h3>
                    <p class="text-gray-600">${skills.technical.join(', ')}</p>
                </div>
            `;
        }
        
        if (skills.soft.length > 0) {
            html += `
                <div class="mb-3">
                    <h3 class="font-semibold text-gray-700 mb-2">Soft Skills:</h3>
                    <p class="text-gray-600">${skills.soft.join(', ')}</p>
                </div>
            `;
        }
        
        if (skills.language.length > 0) {
            html += `
                <div class="mb-3">
                    <h3 class="font-semibold text-gray-700 mb-2">Languages:</h3>
                    <p class="text-gray-600">${skills.language.join(', ')}</p>
                </div>
            `;
        }
        
        html += `
            </div>
        `;
    }
    
    html += `
        </div>
        <div class="mt-6 flex justify-center space-x-4">
            <button onclick="downloadCV()" class="px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition">
                <i class="fas fa-download mr-2"></i>Download PDF
            </button>
            <button onclick="window.print()" class="px-6 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition">
                <i class="fas fa-print mr-2"></i>Print
            </button>
        </div>
    `;
    
    previewContent.innerHTML = html;
    document.getElementById('previewModal').classList.remove('hidden');
}

function previewCV() {
    const form = document.getElementById('cvForm');
    const formData = new FormData(form);
    
    const cvData = {
        personal: {
            fullName: formData.get('fullName'),
            title: formData.get('title'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            location: formData.get('location'),
            portfolio: formData.get('portfolio'),
            summary: formData.get('summary')
        },
        experience: [],
        education: [],
        skills: skills
    };
    
    // Collect experience data
    for (let i = 1; i <= experienceCount; i++) {
        const title = formData.get(`exp_title_${i}`);
        if (title) {
            cvData.experience.push({
                title: title,
                company: formData.get(`exp_company_${i}`),
                location: formData.get(`exp_location_${i}`),
                duration: formData.get(`exp_duration_${i}`),
                description: formData.get(`exp_description_${i}`)
            });
        }
    }
    
    // Collect education data
    for (let i = 1; i <= educationCount; i++) {
        const degree = formData.get(`edu_degree_${i}`);
        if (degree) {
            cvData.education.push({
                degree: degree,
                institution: formData.get(`edu_institution_${i}`),
                location: formData.get(`edu_location_${i}`),
                duration: formData.get(`edu_duration_${i}`),
                description: formData.get(`edu_description_${i}`)
            });
        }
    }
    
    generateCVPreview(cvData);
}

function closePreview() {
    document.getElementById('previewModal').classList.add('hidden');
}

function resetForm() {
    if (confirm('Are you sure you want to reset the entire form?')) {
        document.getElementById('cvForm').reset();
        document.getElementById('experienceList').innerHTML = '';
        document.getElementById('educationList').innerHTML = '';
        skills = { technical: [], soft: [], language: [] };
        updateSkillsDisplay('technical');
        updateSkillsDisplay('soft');
        updateSkillsDisplay('language');
        experienceCount = 0;
        educationCount = 0;
        addExperience();
        addEducation();
        showNotification('Form reset successfully!', 'info');
    }
}

function downloadCV() {
    // This would require a backend service or a library like jsPDF
    showNotification('PDF download feature requires backend implementation', 'info');
}

function showNotification(message, type = 'info') {
    const colors = {
        success: 'bg-green-500',
        warning: 'bg-yellow-500',
        error: 'bg-red-500',
        info: 'bg-blue-500'
    };
    
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 ${colors[type]} text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}
