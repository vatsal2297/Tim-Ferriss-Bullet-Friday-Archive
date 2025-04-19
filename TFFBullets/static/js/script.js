function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

function toggleAccordion(element) {
    const body = element.nextElementSibling;
    //body.style.display = body.style.display === 'block' ? 'none' : 'block';
    body.style.display = body.style.display === 'none' || !body.style.display ? 'block' : 'none';
    //$(body).slideToggle( "slow", function() {
        // Animation complete.
        //$(body).style.display = $(body).style.display === 'none' || !$(body).style.display ? 'block' : 'none';
        //$(body).css('display') = $(body).css('display','none') || !$(body).css('display') ? $(body).css('display', 'block') : $(body).css('display', 'none');
        //console.log($(body).css('display'))
    //});
}

function filterByYear(year) {
    fetch(`/api/emails/${year}`)
        .then(response => response.json())
        .then(data => {
            const contentDiv = document.querySelector('.email-list');
            contentDiv.innerHTML = '';

            if (data.emails && data.emails.length > 0) {
                data.emails.forEach(email => {
                    const emailItem = document.createElement('div');
                    emailItem.classList.add('email-item');

                    const emailHeader = document.createElement('div');
                    emailHeader.classList.add('email-header');
                    
                    let email_date = new Date(email.email_date)
                    const email_date_options = {
                        month: "short",
                        day: "numeric"
                    }
                    let email_date_converted = email_date.toLocaleString('en-us', email_date_options);
                    console.log(email_date_converted);

                    emailHeader.innerHTML = `<div class="email-meta">
                                            <span class="email-date">${email_date_converted}
                                            <span class="divider"></span> 
                                            <span class="email-title">${email.email_title}</span>
                                            </div>`;
                       
                    emailHeader.onclick = () => toggleAccordion(emailHeader);
                    const emailBody = document.createElement('div');
                    emailBody.classList.add('email-body');
                    emailBody.style.display = 'none';

                    const bulletList = document.createElement('ul');
                    email.bullets.forEach(bullet => {
                        const bulletItem = document.createElement('li');
                        bulletItem.innerHTML = `<strong>${bullet.bullet_heading}</strong>: ${bullet.bullet_content}`;
                        bulletList.appendChild(bulletItem);
                    });

                    emailBody.appendChild(bulletList);
                    emailItem.appendChild(emailHeader);
                    emailItem.appendChild(emailBody);
                    contentDiv.appendChild(emailItem);
                });
            } else {
                contentDiv.innerHTML = '<p>No data available for this year.</p>';
            }
        })
        .catch(error => console.error('Error fetching data:', error));
}
