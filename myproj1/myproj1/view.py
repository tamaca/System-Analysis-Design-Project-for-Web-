# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    context['title'] = "医院预约挂号系统"
    return render(request, 'index.html', context)

def login(request):
    context = {}
    context['title'] = "登录"
    return render(request, 'login.html', context)

def register(request):
    context = {}
    context['title'] = "注册"
    return render(request, 'register.html', context)

def hospitals(request):
    context = {}
    #test data begin
    hosp1 = {}
    hosp1["name"] = "PLA301"
    hosp1["loc"] = "WuKeSong"
    hosp1["intro"] = "sanitized"
    hList = [hosp1]
    context["hospitalList"] = hList
    #test data end
    context['title'] = "查找医院"
    return render(request, 'hospitals.html', context)

def select(request):
    context = {}
    #test data begin
    dept1 = {}
    dept2 = {}
    dr1 = {}
    dr2 = {}
    dr1["name"] = "dr1"
    dr1["price"] = "$20"
    dr2["name"] = "dr2"
    dr2["price"] = "$25"
    dept1["name"] = "Orthodontics1"
    dept2["name"] = "Orthodontics2"
    drs = [dr1,dr2]
    dept1["doctors"] = drs
    dept2["doctors"] = drs
    dept = [dept1, dept2]
    context["departments"] = dept
    #test data end
    context['title'] = "预约选择"
    return render(request, 'select.html', context)

def list(request):
    context = {}
    ord1 = {}
    ord1["hospital"] = "PLA301"
    ord1["dept"] = "Orthodontics1"
    ord1["price"] = "$25"
    ord1["date"] = "2016-01-01"
    ord1["doctor"] = "dr1"
    ord1["rank"] = "professor"
    unpayed = [ord1]
    payed = [ord1]
    past = [ord1]
    context['unpayedOrders'] = unpayed
    context['payedOrders'] = payed
    context['pastOrders'] = past
    context['title'] = "我的预约单"
    return render(request, 'list.html', context)

def contact(request):
    context = {}
    context['key'] = "value"
    return render(request, 'contact.html', context)