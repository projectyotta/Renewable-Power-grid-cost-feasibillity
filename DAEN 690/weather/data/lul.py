
# code to remove first n lines in a file 
filelist=["26.1_-80.6.txt","26.1_-81.6.txt","26.1_-97.6.txt","26.1_-98.6.txt","27.1_-80.6.txt","27.1_-81.6.txt","27.1_-82.6.txt","27.1_-97.6.txt","27.1_-98.6.txt","27.1_-99.6.txt","28.1_-80.6.txt","28.1_-81.6.txt","28.1_-82.6.txt","28.1_-97.6.txt","28.1_-98.6.txt","28.1_-99.6.txt","29.1_-100.6.txt","29.1_-101.6.txt","29.1_-102.6.txt","29.1_-103.6.txt","29.1_-81.6.txt","29.1_-82.6.txt","29.1_-90.6.txt","29.1_-95.6.txt","29.1_-96.6.txt","29.1_-97.6.txt","29.1_-98.6.txt","29.1_-99.6.txt","30.1_-100.6.txt","30.1_-101.6.txt","30.1_-102.6.txt","30.1_-103.6.txt","30.1_-104.6.txt","30.1_-81.6.txt","30.1_-82.6.txt","30.1_-83.6.txt","30.1_-90.6.txt","30.1_-91.6.txt","30.1_-92.6.txt","30.1_-93.6.txt","30.1_-94.6.txt","30.1_-95.6.txt","30.1_-96.6.txt","30.1_-97.6.txt","30.1_-98.6.txt","30.1_-99.6.txt","31.1_-100.6.txt","31.1_-101.6.txt","31.1_-102.6.txt","31.1_-103.6.txt","31.1_-104.6.txt","31.1_-105.6.txt","31.1_-81.6.txt","31.1_-82.6.txt","31.1_-83.6.txt","31.1_-84.6.txt","31.1_-85.6.txt","31.1_-86.6.txt","31.1_-87.6.txt","31.1_-88.6.txt","31.1_-89.6.txt","31.1_-90.6.txt","31.1_-91.6.txt","31.1_-92.6.txt","31.1_-93.6.txt","31.1_-94.6.txt","31.1_-95.6.txt","31.1_-96.6.txt","31.1_-97.6.txt","31.1_-98.6.txt","31.1_-99.6.txt","32.1_-100.6.txt","32.1_-101.6.txt","32.1_-102.6.txt","32.1_-103.6.txt","32.1_-104.6.txt","32.1_-105.6.txt","32.1_-106.6.txt","32.1_-107.6.txt","32.1_-108.6.txt","32.1_-109.6.txt","32.1_-110.6.txt","32.1_-111.6.txt","32.1_-112.6.txt","32.1_-81.6.txt","32.1_-82.6.txt","32.1_-83.6.txt","32.1_-84.6.txt","32.1_-85.6.txt","32.1_-86.6.txt","32.1_-87.6.txt","32.1_-88.6.txt","32.1_-89.6.txt","32.1_-90.6.txt","32.1_-91.6.txt","32.1_-92.6.txt","32.1_-93.6.txt","32.1_-94.6.txt","32.1_-95.6.txt","32.1_-96.6.txt","32.1_-97.6.txt","32.1_-98.6.txt","32.1_-99.6.txt","33.1_-100.6.txt","33.1_-101.6.txt","33.1_-102.6.txt","33.1_-103.6.txt","33.1_-104.6.txt","33.1_-105.6.txt","33.1_-106.6.txt","33.1_-107.6.txt","33.1_-108.6.txt","33.1_-109.6.txt","33.1_-110.6.txt","33.1_-111.6.txt","33.1_-112.6.txt","33.1_-113.6.txt","33.1_-114.6.txt","33.1_-115.6.txt","33.1_-116.6.txt","33.1_-117.6.txt","33.1_-79.6.txt","33.1_-80.6.txt","33.1_-81.6.txt","33.1_-82.6.txt","33.1_-83.6.txt","33.1_-84.6.txt","33.1_-85.6.txt","33.1_-86.6.txt","33.1_-87.6.txt","33.1_-88.6.txt","33.1_-89.6.txt","33.1_-90.6.txt","33.1_-91.6.txt","33.1_-92.6.txt","33.1_-93.6.txt","33.1_-94.6.txt","33.1_-95.6.txt","33.1_-96.6.txt","33.1_-97.6.txt","33.1_-98.6.txt","33.1_-99.6.txt","34.1_-100.6.txt","34.1_-101.6.txt","34.1_-102.6.txt","34.1_-103.6.txt","34.1_-104.6.txt","34.1_-105.6.txt","34.1_-106.6.txt","34.1_-107.6.txt","34.1_-108.6.txt","34.1_-109.6.txt","34.1_-110.6.txt","34.1_-111.6.txt","34.1_-112.6.txt","34.1_-113.6.txt","34.1_-114.6.txt","34.1_-115.6.txt","34.1_-116.6.txt","34.1_-117.6.txt","34.1_-118.6.txt","34.1_-77.6.txt","34.1_-78.6.txt","34.1_-79.6.txt","34.1_-80.6.txt","34.1_-81.6.txt","34.1_-82.6.txt","34.1_-83.6.txt","34.1_-84.6.txt","34.1_-85.6.txt","34.1_-86.6.txt","34.1_-87.6.txt","34.1_-88.6.txt","34.1_-89.6.txt","34.1_-90.6.txt","34.1_-91.6.txt","34.1_-92.6.txt","34.1_-93.6.txt","34.1_-94.6.txt","34.1_-95.6.txt","34.1_-96.6.txt","34.1_-97.6.txt","34.1_-98.6.txt","34.1_-99.6.txt","35.1_-100.6.txt","35.1_-101.6.txt","35.1_-102.6.txt","35.1_-103.6.txt","35.1_-104.6.txt","35.1_-105.6.txt","35.1_-106.6.txt","35.1_-107.6.txt","35.1_-108.6.txt","35.1_-109.6.txt","35.1_-110.6.txt","35.1_-111.6.txt","35.1_-112.6.txt","35.1_-113.6.txt","35.1_-114.6.txt","35.1_-115.6.txt","35.1_-116.6.txt","35.1_-117.6.txt","35.1_-118.6.txt","35.1_-119.6.txt","35.1_-120.6.txt","35.1_-76.6.txt","35.1_-77.6.txt","35.1_-78.6.txt","35.1_-79.6.txt","35.1_-80.6.txt","35.1_-81.6.txt","35.1_-82.6.txt","35.1_-83.6.txt","35.1_-84.6.txt","35.1_-85.6.txt","35.1_-86.6.txt","35.1_-87.6.txt","35.1_-88.6.txt","35.1_-89.6.txt","35.1_-90.6.txt","35.1_-91.6.txt","35.1_-92.6.txt","35.1_-93.6.txt","35.1_-94.6.txt","35.1_-95.6.txt","35.1_-96.6.txt","35.1_-97.6.txt","35.1_-98.6.txt","35.1_-99.6.txt","36.1_-100.6.txt","36.1_-101.6.txt","36.1_-102.6.txt","36.1_-103.6.txt","36.1_-104.6.txt","36.1_-105.6.txt","36.1_-106.6.txt","36.1_-107.6.txt","36.1_-108.6.txt","36.1_-109.6.txt","36.1_-110.6.txt","36.1_-111.6.txt","36.1_-112.6.txt","36.1_-113.6.txt","36.1_-114.6.txt","36.1_-115.6.txt","36.1_-116.6.txt","36.1_-117.6.txt","36.1_-118.6.txt","36.1_-119.6.txt","36.1_-120.6.txt","36.1_-121.6.txt","36.1_-76.6.txt","36.1_-77.6.txt","36.1_-78.6.txt","36.1_-79.6.txt","36.1_-80.6.txt","36.1_-81.6.txt","36.1_-82.6.txt","36.1_-83.6.txt","36.1_-84.6.txt","36.1_-85.6.txt","36.1_-86.6.txt","36.1_-87.6.txt","36.1_-88.6.txt","36.1_-89.6.txt","36.1_-90.6.txt","36.1_-91.6.txt","36.1_-92.6.txt","36.1_-93.6.txt","36.1_-94.6.txt","36.1_-95.6.txt","36.1_-96.6.txt","36.1_-97.6.txt","36.1_-98.6.txt","36.1_-99.6.txt","37.1_-100.6.txt","37.1_-101.6.txt","37.1_-102.6.txt","37.1_-103.6.txt","37.1_-104.6.txt","37.1_-105.6.txt","37.1_-106.6.txt","37.1_-107.6.txt","37.1_-108.6.txt","37.1_-109.6.txt","37.1_-110.6.txt","37.1_-111.6.txt","37.1_-112.6.txt","37.1_-113.6.txt","37.1_-114.6.txt","37.1_-115.6.txt","37.1_-116.6.txt","37.1_-117.6.txt","37.1_-118.6.txt","37.1_-119.6.txt","37.1_-120.6.txt","37.1_-121.6.txt","37.1_-76.6.txt","37.1_-77.6.txt","37.1_-78.6.txt","37.1_-79.6.txt","37.1_-80.6.txt","37.1_-81.6.txt","37.1_-82.6.txt","37.1_-83.6.txt","37.1_-84.6.txt","37.1_-85.6.txt","37.1_-86.6.txt","37.1_-87.6.txt","37.1_-88.6.txt","37.1_-89.6.txt","37.1_-90.6.txt","37.1_-91.6.txt","37.1_-92.6.txt","37.1_-93.6.txt","37.1_-94.6.txt","37.1_-95.6.txt","37.1_-96.6.txt","37.1_-97.6.txt","37.1_-98.6.txt","37.1_-99.6.txt","38.1_-100.6.txt","38.1_-101.6.txt","38.1_-102.6.txt","38.1_-103.6.txt","38.1_-104.6.txt","38.1_-105.6.txt","38.1_-106.6.txt","38.1_-107.6.txt","38.1_-108.6.txt","38.1_-109.6.txt","38.1_-110.6.txt","38.1_-111.6.txt","38.1_-112.6.txt","38.1_-113.6.txt","38.1_-114.6.txt","38.1_-115.6.txt","38.1_-116.6.txt","38.1_-117.6.txt","38.1_-118.6.txt","38.1_-119.6.txt","38.1_-120.6.txt","38.1_-121.6.txt","38.1_-122.6.txt","38.1_-75.6.txt","38.1_-76.6.txt","38.1_-77.6.txt","38.1_-78.6.txt","38.1_-79.6.txt","38.1_-80.6.txt","38.1_-81.6.txt","38.1_-82.6.txt","38.1_-83.6.txt","38.1_-84.6.txt","38.1_-85.6.txt","38.1_-86.6.txt","38.1_-87.6.txt","38.1_-88.6.txt","38.1_-89.6.txt","38.1_-90.6.txt","38.1_-91.6.txt","38.1_-92.6.txt","38.1_-93.6.txt","38.1_-94.6.txt","38.1_-95.6.txt","38.1_-96.6.txt","38.1_-97.6.txt","38.1_-98.6.txt","38.1_-99.6.txt","39.1_-100.6.txt","39.1_-101.6.txt","39.1_-102.6.txt","39.1_-103.6.txt","39.1_-104.6.txt","39.1_-105.6.txt","39.1_-106.6.txt","39.1_-107.6.txt","39.1_-108.6.txt","39.1_-109.6.txt","39.1_-110.6.txt","39.1_-111.6.txt","39.1_-112.6.txt","39.1_-113.6.txt","39.1_-114.6.txt","39.1_-115.6.txt","39.1_-116.6.txt","39.1_-117.6.txt","39.1_-118.6.txt","39.1_-119.6.txt","39.1_-120.6.txt","39.1_-121.6.txt","39.1_-122.6.txt","39.1_-123.6.txt","39.1_-75.6.txt","39.1_-76.6.txt","39.1_-77.6.txt","39.1_-78.6.txt","39.1_-79.6.txt","39.1_-80.6.txt","39.1_-81.6.txt","39.1_-82.6.txt","39.1_-83.6.txt","39.1_-84.6.txt","39.1_-85.6.txt","39.1_-86.6.txt","39.1_-87.6.txt","39.1_-88.6.txt","39.1_-89.6.txt","39.1_-90.6.txt","39.1_-91.6.txt","39.1_-92.6.txt","39.1_-93.6.txt","39.1_-94.6.txt","39.1_-95.6.txt","39.1_-96.6.txt","39.1_-97.6.txt","39.1_-98.6.txt","39.1_-99.6.txt","40.1_-100.6.txt","40.1_-101.6.txt","40.1_-102.6.txt","40.1_-103.6.txt","40.1_-104.6.txt","40.1_-105.6.txt","40.1_-106.6.txt","40.1_-107.6.txt","40.1_-108.6.txt","40.1_-109.6.txt","40.1_-110.6.txt","40.1_-111.6.txt","40.1_-112.6.txt","40.1_-113.6.txt","40.1_-114.6.txt","40.1_-115.6.txt","40.1_-116.6.txt","40.1_-117.6.txt","40.1_-118.6.txt","40.1_-119.6.txt","40.1_-120.6.txt","40.1_-121.6.txt","40.1_-122.6.txt","40.1_-123.6.txt","40.1_-124.6.txt","40.1_-74.6.txt","40.1_-75.6.txt","40.1_-76.6.txt","40.1_-77.6.txt","40.1_-78.6.txt","40.1_-79.6.txt","40.1_-80.6.txt","40.1_-81.6.txt","40.1_-82.6.txt","40.1_-83.6.txt","40.1_-84.6.txt","40.1_-85.6.txt","40.1_-86.6.txt","40.1_-87.6.txt","40.1_-88.6.txt","40.1_-89.6.txt","40.1_-90.6.txt","40.1_-91.6.txt","40.1_-92.6.txt","40.1_-93.6.txt","40.1_-94.6.txt","40.1_-95.6.txt","40.1_-96.6.txt","40.1_-97.6.txt","40.1_-98.6.txt","40.1_-99.6.txt","41.1_-100.6.txt","41.1_-101.6.txt","41.1_-102.6.txt","41.1_-103.6.txt","41.1_-104.6.txt","41.1_-105.6.txt","41.1_-106.6.txt","41.1_-107.6.txt","41.1_-108.6.txt","41.1_-109.6.txt","41.1_-110.6.txt","41.1_-111.6.txt","41.1_-112.6.txt","41.1_-113.6.txt","41.1_-114.6.txt","41.1_-115.6.txt","41.1_-116.6.txt","41.1_-117.6.txt","41.1_-118.6.txt","41.1_-119.6.txt","41.1_-120.6.txt","41.1_-121.6.txt","41.1_-122.6.txt","41.1_-123.6.txt","41.1_-124.6.txt","41.1_-72.6.txt","41.1_-73.6.txt","41.1_-74.6.txt","41.1_-75.6.txt","41.1_-76.6.txt","41.1_-77.6.txt","41.1_-78.6.txt","41.1_-79.6.txt","41.1_-80.6.txt","41.1_-81.6.txt","41.1_-82.6.txt","41.1_-83.6.txt","41.1_-84.6.txt","41.1_-85.6.txt","41.1_-86.6.txt","41.1_-87.6.txt","41.1_-88.6.txt","41.1_-89.6.txt","41.1_-90.6.txt","41.1_-91.6.txt","41.1_-92.6.txt","41.1_-93.6.txt","41.1_-94.6.txt","41.1_-95.6.txt","41.1_-96.6.txt","41.1_-97.6.txt","41.1_-98.6.txt","41.1_-99.6.txt","42.1_-100.6.txt","42.1_-101.6.txt","42.1_-102.6.txt","42.1_-103.6.txt","42.1_-104.6.txt","42.1_-105.6.txt","42.1_-106.6.txt","42.1_-107.6.txt","42.1_-108.6.txt","42.1_-109.6.txt","42.1_-110.6.txt","42.1_-111.6.txt","42.1_-112.6.txt","42.1_-113.6.txt","42.1_-114.6.txt","42.1_-115.6.txt","42.1_-116.6.txt","42.1_-117.6.txt","42.1_-118.6.txt","42.1_-119.6.txt","42.1_-120.6.txt","42.1_-121.6.txt","42.1_-122.6.txt","42.1_-123.6.txt","42.1_-124.6.txt","42.1_-70.6.txt","42.1_-71.6.txt","42.1_-72.6.txt","42.1_-73.6.txt","42.1_-74.6.txt","42.1_-75.6.txt","42.1_-76.6.txt","42.1_-77.6.txt","42.1_-78.6.txt","42.1_-79.6.txt","42.1_-80.6.txt","42.1_-83.6.txt","42.1_-84.6.txt","42.1_-85.6.txt","42.1_-86.6.txt","42.1_-87.6.txt","42.1_-88.6.txt","42.1_-89.6.txt","42.1_-90.6.txt","42.1_-91.6.txt","42.1_-92.6.txt","42.1_-93.6.txt","42.1_-94.6.txt","42.1_-95.6.txt","42.1_-96.6.txt","42.1_-97.6.txt","42.1_-98.6.txt","42.1_-99.6.txt","43.1_-100.6.txt","43.1_-101.6.txt","43.1_-102.6.txt","43.1_-103.6.txt","43.1_-104.6.txt","43.1_-105.6.txt","43.1_-106.6.txt","43.1_-107.6.txt","43.1_-108.6.txt","43.1_-109.6.txt","43.1_-110.6.txt","43.1_-111.6.txt","43.1_-112.6.txt","43.1_-113.6.txt","43.1_-114.6.txt","43.1_-115.6.txt","43.1_-116.6.txt","43.1_-117.6.txt","43.1_-118.6.txt","43.1_-119.6.txt","43.1_-120.6.txt","43.1_-121.6.txt","43.1_-122.6.txt","43.1_-123.6.txt","43.1_-124.6.txt","43.1_-70.6.txt","43.1_-71.6.txt","43.1_-72.6.txt","43.1_-73.6.txt","43.1_-74.6.txt","43.1_-75.6.txt","43.1_-76.6.txt","43.1_-77.6.txt","43.1_-78.6.txt","43.1_-82.6.txt","43.1_-83.6.txt","43.1_-84.6.txt","43.1_-85.6.txt","43.1_-86.6.txt","43.1_-87.6.txt","43.1_-88.6.txt","43.1_-89.6.txt","43.1_-90.6.txt","43.1_-91.6.txt","43.1_-92.6.txt","43.1_-93.6.txt","43.1_-94.6.txt","43.1_-95.6.txt","43.1_-96.6.txt","43.1_-97.6.txt","43.1_-98.6.txt","43.1_-99.6.txt","44.1_-100.6.txt","44.1_-101.6.txt","44.1_-102.6.txt","44.1_-103.6.txt","44.1_-104.6.txt","44.1_-105.6.txt","44.1_-106.6.txt","44.1_-107.6.txt","44.1_-108.6.txt","44.1_-109.6.txt","44.1_-110.6.txt","44.1_-111.6.txt","44.1_-112.6.txt","44.1_-113.6.txt","44.1_-114.6.txt","44.1_-115.6.txt","44.1_-116.6.txt","44.1_-117.6.txt","44.1_-118.6.txt","44.1_-119.6.txt","44.1_-120.6.txt","44.1_-121.6.txt","44.1_-122.6.txt","44.1_-123.6.txt","44.1_-124.6.txt","44.1_-69.6.txt","44.1_-70.6.txt","44.1_-71.6.txt","44.1_-72.6.txt","44.1_-73.6.txt","44.1_-74.6.txt","44.1_-75.6.txt","44.1_-82.6.txt","44.1_-83.6.txt","44.1_-84.6.txt","44.1_-85.6.txt","44.1_-86.6.txt","44.1_-87.6.txt","44.1_-88.6.txt","44.1_-89.6.txt","44.1_-90.6.txt","44.1_-91.6.txt","44.1_-92.6.txt","44.1_-93.6.txt","44.1_-94.6.txt","44.1_-95.6.txt","44.1_-96.6.txt","44.1_-97.6.txt","44.1_-98.6.txt","44.1_-99.6.txt","45.1_-100.6.txt","45.1_-101.6.txt","45.1_-102.6.txt","45.1_-103.6.txt","45.1_-104.6.txt","45.1_-105.6.txt","45.1_-106.6.txt","45.1_-107.6.txt","45.1_-108.6.txt","45.1_-109.6.txt","45.1_-110.6.txt","45.1_-111.6.txt","45.1_-112.6.txt","45.1_-113.6.txt","45.1_-114.6.txt","45.1_-115.6.txt","45.1_-116.6.txt","45.1_-117.6.txt","45.1_-118.6.txt","45.1_-119.6.txt","45.1_-120.6.txt","45.1_-121.6.txt","45.1_-122.6.txt","45.1_-123.6.txt","45.1_-124.6.txt","45.1_-67.6.txt","45.1_-68.6.txt","45.1_-69.6.txt","45.1_-70.6.txt","45.1_-71.6.txt","45.1_-72.6.txt","45.1_-73.6.txt","45.1_-74.6.txt","45.1_-82.6.txt","45.1_-83.6.txt","45.1_-84.6.txt","45.1_-85.6.txt","45.1_-86.6.txt","45.1_-87.6.txt","45.1_-88.6.txt","45.1_-89.6.txt","45.1_-90.6.txt","45.1_-91.6.txt","45.1_-92.6.txt","45.1_-93.6.txt","45.1_-94.6.txt","45.1_-95.6.txt","45.1_-96.6.txt","45.1_-97.6.txt","45.1_-98.6.txt","45.1_-99.6.txt","46.1_-100.6.txt","46.1_-101.6.txt","46.1_-102.6.txt","46.1_-103.6.txt","46.1_-104.6.txt","46.1_-105.6.txt","46.1_-106.6.txt","46.1_-107.6.txt","46.1_-108.6.txt","46.1_-109.6.txt","46.1_-110.6.txt","46.1_-111.6.txt","46.1_-112.6.txt","46.1_-113.6.txt","46.1_-114.6.txt","46.1_-115.6.txt","46.1_-116.6.txt","46.1_-117.6.txt","46.1_-118.6.txt","46.1_-119.6.txt","46.1_-120.6.txt","46.1_-121.6.txt","46.1_-122.6.txt","46.1_-123.6.txt","46.1_-124.6.txt","46.1_-68.6.txt","46.1_-69.6.txt","46.1_-84.6.txt","46.1_-85.6.txt","46.1_-86.6.txt","46.1_-87.6.txt","46.1_-88.6.txt","46.1_-89.6.txt","46.1_-90.6.txt","46.1_-91.6.txt","46.1_-92.6.txt","46.1_-93.6.txt","46.1_-94.6.txt","46.1_-95.6.txt","46.1_-96.6.txt","46.1_-97.6.txt","46.1_-98.6.txt","46.1_-99.6.txt","47.1_-100.6.txt","47.1_-101.6.txt","47.1_-102.6.txt","47.1_-103.6.txt","47.1_-104.6.txt","47.1_-105.6.txt","47.1_-106.6.txt","47.1_-107.6.txt","47.1_-108.6.txt","47.1_-109.6.txt","47.1_-110.6.txt","47.1_-111.6.txt","47.1_-112.6.txt","47.1_-113.6.txt","47.1_-114.6.txt","47.1_-115.6.txt","47.1_-116.6.txt","47.1_-117.6.txt","47.1_-118.6.txt","47.1_-119.6.txt","47.1_-120.6.txt","47.1_-121.6.txt","47.1_-122.6.txt","47.1_-123.6.txt","47.1_-124.6.txt","47.1_-68.6.txt","47.1_-69.6.txt","47.1_-85.6.txt","47.1_-86.6.txt","47.1_-87.6.txt","47.1_-88.6.txt","47.1_-89.6.txt","47.1_-90.6.txt","47.1_-91.6.txt","47.1_-92.6.txt","47.1_-93.6.txt","47.1_-94.6.txt","47.1_-95.6.txt","47.1_-96.6.txt","47.1_-97.6.txt","47.1_-98.6.txt","47.1_-99.6.txt","48.1_-100.6.txt","48.1_-101.6.txt","48.1_-102.6.txt","48.1_-103.6.txt","48.1_-104.6.txt","48.1_-105.6.txt","48.1_-106.6.txt","48.1_-107.6.txt","48.1_-108.6.txt","48.1_-109.6.txt","48.1_-110.6.txt","48.1_-111.6.txt","48.1_-112.6.txt","48.1_-113.6.txt","48.1_-114.6.txt","48.1_-115.6.txt","48.1_-116.6.txt","48.1_-117.6.txt","48.1_-118.6.txt","48.1_-119.6.txt","48.1_-120.6.txt","48.1_-121.6.txt","48.1_-122.6.txt","48.1_-123.6.txt","48.1_-124.6.txt","48.1_-88.6.txt","48.1_-89.6.txt","48.1_-90.6.txt","48.1_-91.6.txt","48.1_-92.6.txt","48.1_-93.6.txt","48.1_-94.6.txt","48.1_-95.6.txt","48.1_-96.6.txt","48.1_-97.6.txt","48.1_-98.6.txt","48.1_-99.6.txt","49.1_-100.6.txt","49.1_-101.6.txt","49.1_-102.6.txt","49.1_-103.6.txt","49.1_-104.6.txt","49.1_-105.6.txt","49.1_-106.6.txt","49.1_-107.6.txt","49.1_-108.6.txt","49.1_-109.6.txt","49.1_-110.6.txt","49.1_-111.6.txt","49.1_-112.6.txt","49.1_-113.6.txt","49.1_-114.6.txt","49.1_-115.6.txt","49.1_-116.6.txt","49.1_-117.6.txt","49.1_-118.6.txt","49.1_-119.6.txt","49.1_-120.6.txt","49.1_-121.6.txt","49.1_-122.6.txt","49.1_-123.6.txt","49.1_-124.6.txt","49.1_-95.6.txt","49.1_-96.6.txt","49.1_-97.6.txt","49.1_-98.6.txt","49.1_-99.6.txt","56.2_-153.1.txt","56.2_-154.1.txt","56.2_-155.1.txt","56.2_-156.1.txt","56.2_-157.1.txt","56.2_-158.1.txt","57.2_-153.1.txt","57.2_-154.1.txt","57.2_-155.1.txt","57.2_-156.1.txt","57.2_-157.1.txt","57.2_-158.1.txt","58.2_-153.1.txt","58.2_-154.1.txt","58.2_-155.1.txt","58.2_-156.1.txt","58.2_-157.1.txt","58.2_-158.1.txt","59.2_-153.1.txt","59.2_-154.1.txt","59.2_-155.1.txt","59.2_-156.1.txt","59.2_-157.1.txt","59.2_-158.1.txt","59.2_-159.1.txt","59.2_-160.1.txt","59.2_-161.1.txt","60.2_-141.1.txt","60.2_-142.1.txt","60.2_-143.1.txt","60.2_-144.1.txt","60.2_-145.1.txt","60.2_-146.1.txt","60.2_-147.1.txt","60.2_-148.1.txt","60.2_-149.1.txt","60.2_-150.1.txt","60.2_-151.1.txt","60.2_-152.1.txt","60.2_-153.1.txt","60.2_-154.1.txt","60.2_-155.1.txt","60.2_-156.1.txt","60.2_-157.1.txt","60.2_-158.1.txt","60.2_-159.1.txt","60.2_-160.1.txt","60.2_-161.1.txt","60.2_-162.1.txt","60.2_-163.1.txt","60.2_-164.1.txt","60.2_-165.1.txt","61.2_-141.1.txt","61.2_-142.1.txt","61.2_-143.1.txt","61.2_-144.1.txt","61.2_-145.1.txt","61.2_-146.1.txt","61.2_-147.1.txt","61.2_-148.1.txt","61.2_-149.1.txt","61.2_-150.1.txt","61.2_-151.1.txt","61.2_-152.1.txt","61.2_-153.1.txt","61.2_-154.1.txt","61.2_-155.1.txt","61.2_-156.1.txt","61.2_-157.1.txt","61.2_-158.1.txt","61.2_-159.1.txt","61.2_-160.1.txt","61.2_-161.1.txt","61.2_-162.1.txt","61.2_-163.1.txt","61.2_-164.1.txt","61.2_-165.1.txt","62.2_-141.1.txt","62.2_-142.1.txt","62.2_-143.1.txt","62.2_-144.1.txt","62.2_-145.1.txt","62.2_-146.1.txt","62.2_-147.1.txt","62.2_-148.1.txt","62.2_-149.1.txt","62.2_-150.1.txt","62.2_-151.1.txt","62.2_-152.1.txt","62.2_-153.1.txt","62.2_-154.1.txt","62.2_-155.1.txt","62.2_-156.1.txt","62.2_-157.1.txt","62.2_-158.1.txt","62.2_-159.1.txt","62.2_-160.1.txt","62.2_-161.1.txt","62.2_-162.1.txt","62.2_-163.1.txt","62.2_-164.1.txt","62.2_-165.1.txt","63.2_-141.1.txt","63.2_-142.1.txt","63.2_-143.1.txt","63.2_-144.1.txt","63.2_-145.1.txt","63.2_-146.1.txt","63.2_-147.1.txt","63.2_-148.1.txt","63.2_-149.1.txt","63.2_-150.1.txt","63.2_-151.1.txt","63.2_-152.1.txt","63.2_-153.1.txt","63.2_-154.1.txt","63.2_-155.1.txt","63.2_-156.1.txt","63.2_-157.1.txt","63.2_-158.1.txt","63.2_-159.1.txt","63.2_-160.1.txt","64.2_-141.1.txt","64.2_-142.1.txt","64.2_-143.1.txt","64.2_-144.1.txt","64.2_-145.1.txt","64.2_-146.1.txt","64.2_-147.1.txt","64.2_-148.1.txt","64.2_-149.1.txt","64.2_-150.1.txt","64.2_-151.1.txt","64.2_-152.1.txt","64.2_-153.1.txt","64.2_-154.1.txt","64.2_-155.1.txt","64.2_-156.1.txt","64.2_-157.1.txt","64.2_-158.1.txt","64.2_-159.1.txt","64.2_-160.1.txt","65.2_-141.1.txt","65.2_-142.1.txt","65.2_-143.1.txt","65.2_-144.1.txt","65.2_-145.1.txt","65.2_-146.1.txt","65.2_-147.1.txt","65.2_-148.1.txt","65.2_-149.1.txt","65.2_-150.1.txt","65.2_-151.1.txt","65.2_-152.1.txt","65.2_-153.1.txt","65.2_-154.1.txt","65.2_-155.1.txt","65.2_-156.1.txt","65.2_-157.1.txt","65.2_-158.1.txt","65.2_-159.1.txt","65.2_-160.1.txt","65.2_-161.1.txt","65.2_-162.1.txt","65.2_-163.1.txt","65.2_-164.1.txt","65.2_-165.1.txt","65.2_-166.1.txt","65.2_-167.1.txt","66.2_-141.1.txt","66.2_-142.1.txt","66.2_-143.1.txt","66.2_-144.1.txt","66.2_-145.1.txt","66.2_-146.1.txt","66.2_-147.1.txt","66.2_-148.1.txt","66.2_-149.1.txt","66.2_-150.1.txt","66.2_-151.1.txt","66.2_-152.1.txt","66.2_-153.1.txt","66.2_-154.1.txt","66.2_-155.1.txt","66.2_-156.1.txt","66.2_-157.1.txt","66.2_-158.1.txt","66.2_-159.1.txt","66.2_-160.1.txt","66.2_-161.1.txt","66.2_-162.1.txt","66.2_-163.1.txt","66.2_-164.1.txt","66.2_-165.1.txt","66.2_-166.1.txt","66.2_-167.1.txt","67.2_-141.1.txt","67.2_-142.1.txt","67.2_-143.1.txt","67.2_-144.1.txt","67.2_-145.1.txt","67.2_-146.1.txt","67.2_-147.1.txt","67.2_-148.1.txt","67.2_-149.1.txt","67.2_-150.1.txt","67.2_-151.1.txt","67.2_-152.1.txt","67.2_-153.1.txt","67.2_-154.1.txt","67.2_-155.1.txt","67.2_-156.1.txt","67.2_-157.1.txt","67.2_-158.1.txt","67.2_-159.1.txt","67.2_-160.1.txt","67.2_-161.1.txt","67.2_-162.1.txt","67.2_-163.1.txt","68.2_-141.1.txt","68.2_-142.1.txt","68.2_-143.1.txt","68.2_-144.1.txt","68.2_-145.1.txt","68.2_-146.1.txt","68.2_-147.1.txt","68.2_-148.1.txt","68.2_-149.1.txt","68.2_-150.1.txt","68.2_-151.1.txt","68.2_-152.1.txt","68.2_-153.1.txt","68.2_-154.1.txt","68.2_-155.1.txt","68.2_-156.1.txt","68.2_-157.1.txt","68.2_-158.1.txt","68.2_-159.1.txt","68.2_-160.1.txt","68.2_-161.1.txt","68.2_-162.1.txt","68.2_-163.1.txt","68.2_-164.1.txt","68.2_-165.1.txt","68.2_-166.1.txt","68.2_-167.1.txt","69.2_-141.1.txt","69.2_-142.1.txt","69.2_-143.1.txt","69.2_-144.1.txt","69.2_-145.1.txt","69.2_-146.1.txt","69.2_-147.1.txt","69.2_-148.1.txt","69.2_-149.1.txt","69.2_-150.1.txt","69.2_-151.1.txt","69.2_-152.1.txt","69.2_-153.1.txt","69.2_-154.1.txt","69.2_-155.1.txt","69.2_-156.1.txt","69.2_-157.1.txt","69.2_-158.1.txt","69.2_-159.1.txt","69.2_-160.1.txt","69.2_-161.1.txt","69.2_-162.1.txt","69.2_-163.1.txt","69.2_-164.1.txt","69.2_-165.1.txt","69.2_-166.1.txt","69.2_-167.1.txt","70.2_-141.1.txt","70.2_-142.1.txt","70.2_-143.1.txt","70.2_-144.1.txt","70.2_-145.1.txt","70.2_-146.1.txt","70.2_-147.1.txt","70.2_-148.1.txt","70.2_-149.1.txt","70.2_-150.1.txt","70.2_-151.1.txt","70.2_-152.1.txt","70.2_-153.1.txt","70.2_-154.1.txt","70.2_-155.1.txt","70.2_-156.1.txt","70.2_-157.1.txt","70.2_-158.1.txt","70.2_-159.1.txt","70.2_-160.1.txt","70.2_-161.1.txt","70.2_-162.1.txt"]
latlist=["26.1","26.1","26.1","26.1","27.1","27.1","27.1","27.1","27.1","27.1","28.1","28.1","28.1","28.1","28.1","28.1","29.1","29.1","29.1","29.1","29.1","29.1","29.1","29.1","29.1","29.1","29.1","29.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","30.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","31.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","32.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","33.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","34.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","35.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","36.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","37.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","38.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","39.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","40.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","41.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","42.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","43.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","44.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","45.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","46.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","47.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","48.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","49.1","56.2","56.2","56.2","56.2","56.2","56.2","57.2","57.2","57.2","57.2","57.2","57.2","58.2","58.2","58.2","58.2","58.2","58.2","59.2","59.2","59.2","59.2","59.2","59.2","59.2","59.2","59.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","60.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","61.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","62.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","63.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","64.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","65.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","66.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","67.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","68.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","69.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2","70.2"]
lonlist=["-80.6","-81.6","-97.6","-98.6","-80.6","-81.6","-82.6","-97.6","-98.6","-99.6","-80.6","-81.6","-82.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-81.6","-82.6","-90.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-81.6","-82.6","-83.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-75.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-75.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-74.6","-75.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-72.6","-73.6","-74.6","-75.6","-76.6","-77.6","-78.6","-79.6","-80.6","-81.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-70.6","-71.6","-72.6","-73.6","-74.6","-75.6","-76.6","-77.6","-78.6","-79.6","-80.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-70.6","-71.6","-72.6","-73.6","-74.6","-75.6","-76.6","-77.6","-78.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-69.6","-70.6","-71.6","-72.6","-73.6","-74.6","-75.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-67.6","-68.6","-69.6","-70.6","-71.6","-72.6","-73.6","-74.6","-82.6","-83.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-68.6","-69.6","-84.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-68.6","-69.6","-85.6","-86.6","-87.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-88.6","-89.6","-90.6","-91.6","-92.6","-93.6","-94.6","-95.6","-96.6","-97.6","-98.6","-99.6","-100.6","-101.6","-102.6","-103.6","-104.6","-105.6","-106.6","-107.6","-108.6","-109.6","-110.6","-111.6","-112.6","-113.6","-114.6","-115.6","-116.6","-117.6","-118.6","-119.6","-120.6","-121.6","-122.6","-123.6","-124.6","-95.6","-96.6","-97.6","-98.6","-99.6","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-166.1","-167.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-166.1","-167.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-166.1","-167.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1","-163.1","-164.1","-165.1","-166.1","-167.1","-141.1","-142.1","-143.1","-144.1","-145.1","-146.1","-147.1","-148.1","-149.1","-150.1","-151.1","-152.1","-153.1","-154.1","-155.1","-156.1","-157.1","-158.1","-159.1","-160.1","-161.1","-162.1"]


import pandas as pd 

raw ={}
df={}
for i in range(0,len(filelist)):
    raw[i]=pd.read_table(filelist[i],delimiter=",")
    raw[i]['latitude']=latlist[i]
    raw[i]['longitude']=lonlist[i]

frames=[raw[i] for i in range(0,len(filelist))]
result=pd.concat(frames)

result.to_csv("dank.csv")