class Twitter {
private:
    int timeStamp = 0;
    
    struct Tweet {
        int     id;
        int     time;
        Tweet*  next;
        Tweet(int _id, int _time) : id(_id), time(_time), next(nullptr) {}
    };
    
    struct User {
        int     id;
        Tweet*  thead;
        unordered_set<int> followed;
        
        User(int _id = 0) : id(_id), thead(nullptr) {}
        void follow(int fid)    { followed.insert(fid); }
        void unfollow(int fid)  { followed.erase(fid);  }
        void post(int tid, int time) {
            Tweet* t = new Tweet(tid, time);
            t->next  = thead;
            thead    = t;
        }
    };
    
    unordered_map<int, User> users;
    
    User& getUser(int uid) {
        if (!users.count(uid)) {
            User cur(uid);
            users[uid] = cur;
        }
        return users[uid];
    }
    
public:
    Twitter() {}
    
    void postTweet(int userId, int tweetId) {
        getUser(userId).post(tweetId, timeStamp++);
    }
    
    vector<int> getNewsFeed(int userId) {
        auto comp = [](const Tweet* lhs, const Tweet* rhs) { return lhs->time < rhs->time; };
        priority_queue<Tweet*, vector<Tweet*>, decltype(comp)> heap(comp);
        
        if (getUser(userId).thead)  heap.push(users[userId].thead);
        for (auto uid : users[userId].followed) {
            if (users[uid].thead)   heap.push(users[uid].thead);
        }
        
        vector<int> ans;
        for (int i = 0; i < 10 && !heap.empty(); i++) {
            Tweet* p = heap.top();  heap.pop();
            ans.push_back(p->id);
            if (p->next) heap.push(p->next);
        }
        return ans;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        getUser(followeeId);
        getUser(followerId).follow(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        getUser(followerId).unfollow(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */



class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {
        cnt=0;
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        friends[userId].insert(userId);
        tweets[userId].push_back(make_pair(cnt++,tweetId));
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
        for(auto id : friends[userId])
        {
            for(auto t:tweets[id])
            {
                if(pq.size()==10 )
                {
                        if(t.first>pq.top().first)
                        {
                            pq.pop();
                            pq.push(t);
                        }
                }
                else
                {
                    pq.push(t);
                }
            }
        }
        vector<int> res;
        while(!pq.empty())
        {
            res.push_back(pq.top().second);
            pq.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
    
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        friends[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if(followerId!=followeeId)
            friends[followerId].erase(followeeId);
    }
    int cnt;
    unordered_map<int,set<int>> friends;
    unordered_map<int,vector<pair<int,int>>> tweets;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */