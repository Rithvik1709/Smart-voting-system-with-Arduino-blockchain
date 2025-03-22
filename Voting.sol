
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    address public admin;
    mapping(string => uint256) public votes;
    string[] public candidates = ["BJP", "AAP", "JDU", "OTHERS"];
    
    event VoteCasted(string candidate, uint256 count);
    event VotesReset();

    constructor() {
        admin = msg.sender;
    }

    // Function to cast a vote
    function vote(string memory candidate) public {
        require(validCandidate(candidate), "Invalid candidate");
        votes[candidate]++;
        emit VoteCasted(candidate, votes[candidate]);
    }

    // Function to get vote count of a candidate
    function getVotes(string memory candidate) public view returns (uint256) {
        require(validCandidate(candidate), "Invalid candidate");
        return votes[candidate];
    }

    // Function to reset votes (Admin only)
    function resetVotes() public {
        require(msg.sender == admin, "Only admin can reset votes");
        for (uint i = 0; i < candidates.length; i++) {
            votes[candidates[i]] = 0;
        }
        emit VotesReset();
    }

    // Internal function to check if candidate is valid
    function validCandidate(string memory candidate) internal view returns (bool) {
        for (uint i = 0; i < candidates.length; i++) {
            if (keccak256(bytes(candidate)) == keccak256(bytes(candidates[i]))) {
                return true;
            }
        }
        return false;
    }
}
