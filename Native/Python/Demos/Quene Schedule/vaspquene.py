#!/usr/bin/python

import os
import shutil
import re
import commands
import time

def submit(task,state):
    os.chdir('structure_'+str(task+1))
    if state == 1:
        shutil.copy('INCAR_1','INCAR')
    if state == 2:
        shutil.copy('INCAR_2','INCAR')
        shutil.copy('CONTCAR','POSCAR')
    if state == 3:
        shutil.copy('INCAR_3','INCAR')
        shutil.copy('CONTCAR','POSCAR')
    
    (status,output) = commands.getstatusoutput('qsub vasp.pbs')
    jobid = int(re.match('^[0-9]*',output).group())
    os.chdir('..')
    return jobid

def checkstate(jobid):
    (status,output) = commands.getstatusoutput('qstat '+str(jobid))
    if ('R score' in output) or ('Q score' in output) and (status == 0):
        return 1
    else:
        return 0

if __name__ == '__main__':
    maxtask = 30 #Amount of Total Tasks
    numberofparallel = 5 #Number of task running parallel

    for i in range(maxtask):
        os.mkdir('structure_'+str(i+1))
        shutil.copy('INCAR_1','structure_'+str(i+1)+'/INCAR_1')
        shutil.copy('INCAR_2','structure_'+str(i+1)+'/INCAR_2')
        shutil.copy('INCAR_3','structure_'+str(i+1)+'/INCAR_3')
        shutil.copy('POTCAR','structure_'+str(i+1)+'/POTCAR')
        shutil.copy('POSCAR_'+str(i+1),'structure_'+str(i+1)+'/POSCAR')

    taskstates = [0 for i in range(maxtask)]
    taskrunning = [0 for i in range(maxtask)]
    jobtable = [0 for i in range(numberofparallel)]
    job2task = [0 for i in range(numberofparallel)]

    print 'VASP Quene Start, Task NUM: {num}'.format(num=3*maxtask)

    finished = 0

    while finished <= 3*maxtask:
        for jobindex in range(numberofparallel):
            if not checkstate(jobtable[jobindex]):
                if job2task[jobindex] != 0:
                    taskid = job2task[jobindex]
                    taskstates[taskid] = taskstates[taskid] + 1
                    taskrunning[taskid] = 0
                    finished += 1
                    print 'Completing... {i}/{num}'.format(i=finished,num=3*maxtask)

                for i in range(maxtask):
                    if (taskstates[i] <= 2) and not taskrunning[i]:
                        jobid = submit(i,taskstates[i]+1)
                        jobtable[jobindex] = jobid
                        job2task[jobindex] = i
                        taskrunning[i] = 1
						break
        time.sleep(5*60) # Wait for 5 minutes! 

    for i in range(maxtask):
        shutil.copy('structure_'+str(i+1)+'/CONTCAR','POSCAR_'+str(i+1))

    print 'Calculation Quene Finished'
