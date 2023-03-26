const btnNotifications = document.querySelector('#registration__of__tenants__content__top__right__notifications')
const OpenNotifications = document.querySelector('.registration__of__tenants__content__top__right__notifications__item')

btnNotifications.addEventListener('click', function () {
	OpenNotifications.classList.toggle('active')
})

const btnProfile = document.querySelector('#registration__of__tenants__content__top__right__profile')
const openProfile = document.querySelector('.registration__of__tenants__content__top__right__profile__item')

btnProfile.addEventListener('click', function () {
	openProfile.classList.toggle('active')
})
