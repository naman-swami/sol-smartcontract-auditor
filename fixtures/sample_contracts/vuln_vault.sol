// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VulnerableEtherVault {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        // VULNERABILITY: External call before state update (SWC-107 Reentrancy)
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        balances[msg.sender] -= amount;
    }

    function adminWithdraw(address payable recipient) external {
        // VULNERABILITY: Phishing risk via tx.origin (SWC-115)
        require(tx.origin == 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4, "Not owner");
        recipient.transfer(address(this).balance);
    }
}
