import numpy as np

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    centroids = initial_centroids[:] 
    labels = [0] * len(points)  

    for _ in range(max_iterations):
       
        for i, point in enumerate(points):
            min_dist = float('inf')
            for j, centroid in enumerate(centroids):
                dist = np.linalg.norm(np.array(point) - np.array(centroid))  
                if dist < min_dist:
                    min_dist = dist
                    labels[i] = j  

        new_centroids = []
        for j in range(k):
            cluster_points = [points[i] for i in range(len(points)) if labels[i] == j]
            if cluster_points:
                new_x = sum(p[0] for p in cluster_points) / len(cluster_points)
                new_y = sum(p[1] for p in cluster_points) / len(cluster_points)
                new_centroids.append((round(new_x, 4), round(new_y, 4)))
            else:
                new_centroids.append(centroids[j])  
        
        if new_centroids == centroids: 
            break
        centroids = new_centroids

    return centroids
