def isHappy(n):
    tar = n
    while(True):
        if tar == 4:
            break
        sum = 0
        while(tar > 0):
            sum = sum + (tar%10) * (tar%10)
            tar = tar//10
        if sum == 1:
            return True
        tar = sum
    return False
    

if __name__ == "__main__":
    sample0_output=isHappy(19)
    sample1_output=isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f: 
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
        
    print("Results saved to /app/bind_mount/output.txt")