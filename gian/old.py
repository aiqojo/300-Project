print(len(r))
for ra in range(len(r) - 1):
    if ra % 100 == 0:
        print(ra, end=" ")
    # get the starting positions
    temp = starting_pos[ra].copy()
    # remove the raceId
    temp = np.delete(temp, 0)
    # get the driverIds
    temp2 = r[ra].copy()
    temp2 = temp2["driverId"].unique()
    # if temp2 is empty, continue
    if len(temp2) == 0:
        continue

    # find how many laps there are for this
    laps = r[ra].copy()
    laps = laps["lap"].unique()

    for lap in range(len(laps)):
        # get the order of the drivers for this lap
        order = get_order(r[ra], laps[lap])
        # compare the order to the starting positions
        for i in range(len(order)):
            # print(order, temp)
            # make sure we arent comparing empty arrays
            if len(order) != 0 and len(temp) != 0:
                if order[i] != temp[i] and i < len(temp):
                    try:
                        time.sleep(2)
                        # increment the number of times the driver has changed positions by how many positions they have changed
                        temp2[i] += abs(i - np.where(temp == order[i])[0][0]) - 1
                        print("raceId:", ra, "lap:", lap, "driverId:", order[i])
                        print(
                            "from position:",
                            i,
                            "to position:",
                            np.where(temp == order[i])[0][0] - 1,
                            "with",
                            abs(i - np.where(temp == order[i])[0][0]) - 1,
                            "changes",
                        )
                    except:
                        pass
            # set the starting positions to the order of the drivers for the next lap
            temp = order.copy()

    # add the raceId to the front of the array
    temp2 = np.insert(temp2, 0, rIds[ra])
    changes.append(temp2)

print(changes[1])
