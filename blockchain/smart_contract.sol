// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract KnowledgeStorage {
    struct Knowledge {
        string hash;
        string category;
        address uploader;
    }
    
    mapping(uint256 => Knowledge) public knowledgeRecords;
    uint256 public recordCount;
    
    event KnowledgeStored(uint256 indexed recordId, string hash, string category, address uploader);

    function storeKnowledge(string memory _hash, string memory _category) public {
        knowledgeRecords[recordCount] = Knowledge(_hash, _category, msg.sender);
        emit KnowledgeStored(recordCount, _hash, _category, msg.sender);
        recordCount++;
    }
    
    function getKnowledge(uint256 _id) public view returns (string memory, string memory, address) {
        require(_id < recordCount, "Record does not exist");
        Knowledge memory knowledge = knowledgeRecords[_id];
        return (knowledge.hash, knowledge.category, knowledge.uploader);
    }
}
