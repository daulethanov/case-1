
const btnNotifications = document.querySelector('#applications__content__top__right__notifications')
const OpenNotifications = document.querySelector('.applications__content__top__right__notifications__item')

btnNotifications.addEventListener('click', function () {
	OpenNotifications.classList.toggle('active')
})

const btnProfile = document.querySelector('#applications__content__top__right__profile')
const openProfile = document.querySelector('.applications__content__top__right__profile__item')

btnProfile.addEventListener('click', function () {
	openProfile.classList.toggle('active')
})

const btnList = document.querySelector('#applications__content__button__view__button__list')
const openList = document.querySelector('.applications__content__item__applications')

btnList.addEventListener('click', function () {
	openList.classList.add('active')
	btnList.classList.add('active')
	btnBoard.classList.remove('active')
	openBoard.classList.remove('active')
})

const btnBoard = document.querySelector('#applications__content__button__view__button__board')
const openBoard = document.querySelector('.applications__content__item__applications__board')

btnBoard.addEventListener('click', function () {
	btnBoard.classList.add('active')
	openBoard.classList.add('active')
	openList.classList.remove('active')
	btnList.classList.remove('active')
})



const btnExecution = document.querySelector('#item__applications__for__execution')
const openExecution = document.querySelector('.item__applications__for__execution__open')
const btnExecutionImage = document.querySelector('#item__applications__for__execution__img')

btnExecution.addEventListener('click', function () {
	openExecution.classList.toggle('active')
	btnExecutionImage.classList.toggle('active')
	openInWork.classList.remove('active')
	btnInWorkImage.classList.remove('active')
	openCompleted.classList.remove('active')
	btnCompletedImage.classList.remove('active')
})

const btnInWork = document.querySelector('#item__applications__in__work')
const openInWork = document.querySelector('.item__applications__in__work__open')
const btnInWorkImage = document.querySelector('#item__applications__in__work__img')

btnInWork.addEventListener('click', function () {
	openInWork.classList.toggle('active')
	btnInWorkImage.classList.toggle('active')
	openExecution.classList.remove('active')
	btnExecutionImage.classList.remove('active')
	openCompleted.classList.remove('active')
	btnCompletedImage.classList.remove('active')

})

const btnCompleted = document.querySelector('#item__applications__completed')
const openCompleted = document.querySelector('.item__applications__completed__open')
const btnCompletedImage = document.querySelector('#item__applications__completed__img')

btnCompleted.addEventListener('click', function () {
	openCompleted.classList.toggle('active')
	btnCompletedImage.classList.toggle('active')
	openExecution.classList.remove('active')
	btnExecutionImage.classList.remove('active')
	openInWork.classList.remove('active')
	btnInWorkImage.classList.remove('active')
})

const modalForExecution = document.querySelector('.modal__for__execution')
const modalForExecutionItem = document.querySelector('.modal__for__execution__item')
const openModalExecution = document.querySelector('.modal__for__execution__open')

openModalExecution.addEventListener('click', function () {
	modalForExecution.classList.add('active')
})

modalForExecution.addEventListener('click', function (e) {
	if (e.target === modalForExecution) {
		modalForExecution.classList.remove('active')
	}
})

const modalInWork = document.querySelector('.modal__in__work')
const modaInWorkItem = document.querySelector('.modal__in__work__item')
const openModalInWork = document.querySelector('.modal__in__work__open')

openModalInWork.addEventListener('click', function () {
	modalInWork.classList.add('active')
})

modalInWork.addEventListener('click', function (e) {
	if (e.target === modalInWork) {
		modalInWork.classList.remove('active')
	}
})

const modalCompleted = document.querySelector('.modal__completed')
const modaCompletedItem = document.querySelector('.modal__completed__item')
const openModalCompleted = document.querySelector('.modal__completed__open')

openModalCompleted.addEventListener('click', function () {
	modalCompleted.classList.add('active')
})

modalCompleted.addEventListener('click', function (e) {
	if (e.target === modalCompleted) {
		modalCompleted.classList.remove('active')
	}
})

const modalForExecutionBoard = document.querySelector('.modal__for__execution__board')
const modalForExecutionItemBoard = document.querySelector('.modal__for__execution__item__board')
const openModalExecutionBoard = document.querySelector('.modal__for__execution__open__board')

openModalExecutionBoard.addEventListener('click', function () {
	modalForExecutionBoard.classList.add('active')
})

modalForExecutionBoard.addEventListener('click', function (e) {
	if (e.target === modalForExecutionBoard) {
		modalForExecutionBoard.classList.remove('active')
	}
})

const modalInWorkBoard = document.querySelector('.modal__in__work__board')
const modaInWorkItemBoard = document.querySelector('.modal__in__work__item__board')
const openModalInWorkBoard = document.querySelector('.modal__in__work__open__board')

openModalInWorkBoard.addEventListener('click', function () {
	modalInWorkBoard.classList.add('active')
})

modalInWorkBoard.addEventListener('click', function (e) {
	if (e.target === modalInWorkBoard) {
		modalInWorkBoard.classList.remove('active')
	}
})

const modalCompletedBoard  = document.querySelector('.modal__completed__board')
const modaCompletedItemBoard  = document.querySelector('.modal__completed__item__board')
const openModalCompletedBoard  = document.querySelector('.modal__completed__open__board')

openModalCompletedBoard .addEventListener('click', function () {
	modalCompletedBoard .classList.add('active')
})

modalCompletedBoard .addEventListener('click', function (e) {
	if (e.target === modalCompletedBoard ) {
		modalCompletedBoard .classList.remove('active')
	}
})


