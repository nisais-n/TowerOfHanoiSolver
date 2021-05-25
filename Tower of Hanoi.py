def HanoiSolver(disks, source, helper, target):
    if disks == 1:
        print('\nMove disk 1 from peg - {} to peg - {}.'.format(source,target))
        return

    HanoiSolver(disks-1, source,target,helper)
    print('\nMove disk {} from peg - {} to peg - {}.'.format(disks,source,target))
    HanoiSolver(disks-1,helper,source,target)


print('\nSource peg - A\nHelper peg - B\nTarget peg - C')
disks = str(input('\nEnter no.of Disks in Source peg - A : '))
if disks.isnumeric()==True:
    if int(disks) <= 0:   #Validate disks presents
        print('\nPlese add Minimum 1 disk to Source peg A')
    else:
        moves = (pow(2,int(disks)) - 1)
        print('\nYou will need minium {} moves to solve {} disk(s) puzzle.'.format(moves,disks))
        HanoiSolver(int(disks), 'A','B','C')

else:
    print('Please enter a numeric value')


