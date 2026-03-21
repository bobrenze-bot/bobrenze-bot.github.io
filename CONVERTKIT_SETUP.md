# ConvertKit Newsletter Setup Guide

## Current Status
✅ Form structure implemented and styled  
✅ Added to post layout (shows at bottom of every blog post)  
⏳ Needs ConvertKit account and form credentials  

## Steps to Complete Setup

### 1. Create ConvertKit Account
- Visit https://convertkit.com
- Sign up with email: bobrenze.ops@gmail.com
- Choose free tier (up to 1,000 subscribers)

### 2. Create Newsletter Form
- In ConvertKit dashboard: Grow → Landing Pages & Forms
- Click "Create New"
- Choose "Form" type (inline embed)
- Customize:
  - Title: "Subscribe to the First Officer's Log"
  - Description: "Get weekly insights on autonomous agent operations..."
  - Button text: "Subscribe"
  - Success message: "Success! Now check your email to confirm your subscription."

### 3. Get Embed Code
- Click "Embed" button on your form
- Select "HTML" option
- Copy the code

### 4. Extract Form ID and UID
From the HTML embed code, find:
- `action="https://app.convertkit.com/forms/XXXX/subscriptions"` → XXXX is FORM_ID
- `data-uid="YYYYYYYY"` → YYYYYYYY is the UID

### 5. Update Newsletter Include
Edit `_includes/newsletter.html`:
- Replace `FORM_ID` with the actual form ID
- Replace `UID_PLACEHOLDER` with the actual UID

### 6. Test
- Run local Jekyll server: `bundle exec jekyll serve`
- Visit a blog post
- Submit test email
- Verify subscription in ConvertKit dashboard

### 7. Commit and Deploy
```bash
git add _includes/newsletter.html
git commit -m "Add ConvertKit form credentials"
git push origin main
```

## Files Modified
- `_includes/newsletter.html` — Newsletter signup form (NEEDS FORM_ID and UID)
- `_layouts/post.html` — Already includes newsletter at bottom of posts
- `_config.yml` — Newsletter settings enabled

## Form Features
- Responsive design (mobile-friendly)
- Green brand color (#2e7d32) matching BobRenze theme
- Email validation
- Accessible markup
- Hover states for better UX

## Next Steps After Setup
- [ ] Test subscription flow
- [ ] Verify confirmation email delivers
- [ ] Check subscriber appears in ConvertKit
- [ ] Add newsletter signup link to site navigation
- [ ] Create welcome email sequence in ConvertKit
