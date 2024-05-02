import streamlit as st
from collections import OrderedDict
import functools
import pandas as pd
st.title("Can we qualify for semifinals ?")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = []
for dd in range(9):
    i = 0
    j = 9
    while i < j:
        v.append((a[i], a[j]))
        i += 1
        j -= 1
    temp = a[9]
    for i in range(9, 1, -1):
        a[i] = a[i-1]
    a[1] = temp

st.header('Tournament Structure')
st.image('tourny.jpg')

wins = [0] * 11
l=[]
with st.sidebar:
    number = st.number_input('Enter number matches played till now',min_value=0, max_value=45, value=5, step=1)
    
    col1, col2 = st.columns(2)
    for i in range(0,number,2):
        
        with col1:
            option = st.selectbox(
            f'Who won {i+1} match',
            (v[i][0], v[i][1]))
            wins[option]=wins[option]+1
            l.append(option)
        
        i+=1
        if(i<number):
            with col2:
                option = st.selectbox(
                f'Who won {i+1} match',
                (v[i][0], v[i][1]))
                wins[option]=wins[option]+1
                l.append(option)



if (number<=20):
    st.header("Can Qualify for semifinals")
    winner=[]
    for i in range(number):
        winner.append(l[i])
    
    for j in range(number,45):
        if j % 5 == 0:
            winner.append(1)
            wins[1] += 1
        else:
            winner.append(v[j][0])
            wins[v[j][0]]=wins[v[j][0]]+1
    st.header('Matches result')

    col3, col4, col5 = st.columns(3)
    for i in range(0, 45, 3):
        with col3:
            st.write(f"Match {i+1} Won by {winner[i]}")
        with col4:
            st.write(f"Match {i+2} Won by {winner[i+1]}")
        with col5:
            st.write(f"Match {i+3} Won by {winner[i+2]}")

    table=[]    
    for i in range(1,11):
        t=[]
        t.append(wins[i])
        t.append(i)
        table.append(t)
    table=sorted(table)
    table=table[::-1]
    for i in range(10):
        if (table[i][1]==1):
            j=i-1
            while(j>=0 and table[j][0]==table[j+1][0]):
                table[j], table[j+1] = table[j+1], table[j]
                j=j-1
    

    st.header('Final Leaderboard')
    data_df = pd.DataFrame(
        {
            "Team": [table[i][1] for i in range(10)],
            "Matches Won": [table[i][0] for i in range(10)]
        }
    )
    st.data_editor(data_df, hide_index=True)


else:
    winner=[]
    for i in range(number):
        winner.append(l[i])
    u=[]
    for j in range(number,45):
        if j % 5 == 0:
            winner.append(1)
            wins[1] += 1
        else:
            u.append(v[j])
    sz=len(u)
    found=0

    for msk in range(1 << sz):
        m = wins[:]
        winner2 = winner
        for i in range(sz):
            if msk & (1 << i):
                m[u[i][0]] += 1
                winner2.append(u[i][0])
            else:
                winner2.append(u[i][1])
                m[u[i][1]] += 1
        wins2=m
        w = sorted(m[1:11])
        if m[1] >= w[6]:
            st.header('Matches result')
            winner=winner2
            wins=wins2
            found=1
            break


    if (found==0):
        st.header("Cannot Qualify for semifinals")

    else:
        st.header("Can Qualify for semifinals")
        col3, col4, col5 = st.columns(3)
        for i in range(0, 45, 3):
            with col3:
                st.write(f"Match {i+1} Won by {winner[i]}")
            with col4:
                st.write(f"Match {i+2} Won by {winner[i+1]}")
            with col5:
                st.write(f"Match {i+3} Won by {winner[i+2]}")
    
        table=[]
        for i in range(1,11):
            t=[]
            t.append(wins[i])
            t.append(i)
            table.append(t)
        table=sorted(table)
        table=table[::-1]
        for i in range(10):
            if (table[i][1]==1):
                j=i-1
                while(j>=0 and table[j][0]==table[j+1][0]):
                    table[j], table[j+1] = table[j+1], table[j]
                    j=j-1
        
        st.header('Final Leaderboard')
        data_df = pd.DataFrame(
            {
                "Team": [table[i][1] for i in range(10)],
                "Matches Won": [table[i][0] for i in range(10)]
            }
        )
        st.data_editor(data_df, hide_index=True)

