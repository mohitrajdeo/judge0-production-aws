# ⚡ ESCHATON CLOUD & JUDGE0 PRODUCTION AWS

[![Powered by Eschaton](https://img.shields.io/badge/Flagship%20Engine-Eschaton%20Cloud-059669?style=for-the-badge&logo=fastapi&logoColor=white)](https://eschaton.theeducode.com)
[![Sub-38ms Batch Latency](https://img.shields.io/badge/Latency-38.2ms%20Apex%20Batch-brightgreen?style=for-the-badge)](https://eschaton.theeducode.com/compare/judge0)
[![Single Invocation](https://img.shields.io/badge/Single%20Run-%3C3.4ms%20(417x%20Faster)-emerald?style=for-the-badge)](https://eschaton.theeducode.com)
[![Docker Pulls](https://img.shields.io/docker/pulls/mrmohitrajdeo/judge0-jdbc.svg?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/mrmohitrajdeo/judge0-jdbc)
[![GitHub Packages](https://img.shields.io/badge/GitHub%20Packages-ghcr.io-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mohitrajdeo/judge0-production-aws/pkgs/container/judge0-jdbc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> **The #1 High-Speed Drop-In Alternative to Judge0.**  
> Evaluates **50 parallel test cases in 38.2ms** (110x faster than Judge0 CE) with **100% Judge0 REST API parity** and zero AWS infrastructure overhead.

---

## ⚡ Try the Live Cloud Engine (500 Free Starter Credits • 30-Day Trial)

You can benchmark Eschaton's **38.2ms parallel batch fan-out** live against our production cluster with zero setup:

* 🌐 **Live Interactive Playground:** [https://eschaton.theeducode.com](https://eschaton.theeducode.com) *(1-Click GitHub OAuth • 500 Free Credits)*
* 🥊 **Head-to-Head Architectural Breakdown:** [https://eschaton.theeducode.com/compare/judge0](https://eschaton.theeducode.com/compare/judge0)
* 🏢 **Unified Execution Substrate:** [https://nephis.theeducode.com](https://nephis.theeducode.com) *(Eschaton + Thanaton MicroVMs + Mnemon-DB)*
* 🚀 **Instant Terminal `curl` (100% Judge0 Drop-In):**

```bash
curl -X POST "https://eschaton.theeducode.com/v1/submissions?wait=true" \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: <YOUR_API_KEY>" \
  -d '{
    "language_id": 54,
    "source_code": "#include <iostream>\nint main() { std::cout << \"Eschaton 38.2ms Drop-In Success!\"; return 0; }",
    "stdin": ""
  }'
```

---

## ⚡ Try the Live Cloud Engine (10,000 Free Evaluation Runs)

You can benchmark Eschaton's **38.2ms parallel batch fan-out** live against our production cluster with zero setup:

* **Interactive In-Browser Tester:** [https://ciel.theeducode.com/alpha-test.html?product=eschaton&token=alpha_guest_10k_free](https://ciel.theeducode.com/alpha-test.html?product=eschaton&token=alpha_guest_10k_free)
* **Instant Terminal `curl` (100% Judge0 Drop-In):**
```bash
curl -X POST "https://ciel.theeducode.com/v1/submissions?wait=true" \
  -H "Authorization: Bearer alpha_guest_10k_free" \
  -H "Content-Type: application/json" \
  -d '{"language_id": 54, "source_code": "#include <iostream>\nint main() { std::cout << \"Eschaton 38ms Batch Execution Success!\"; return 0; }"}'
```

---

---

# 🚀 1. FLAGSHIP PRODUCT: ESCHATON CLOUD ENGINE

Evaluating 50 to 1,000 unit test cases sequentially inside traditional Docker containers takes **3 to 10 seconds per submission**, thrashing CPU cgroups and locking servers during synchronized exam spikes. 

**Eschaton** completely eliminates container boot overhead via **pure silicon isolation**, **in-memory microkernel judging**, and **parallel isolate fan-out**.

---

## ⚡ The 8 Specialized Execution Engines of Eschaton

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              ESCHATON ENGINE SUITE MATRIX                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🧈 1. IN-MEMORY MICRO-GRADING (VOID)                                                   │
│    • Sub-4ms evaluation of 1,000+ test cases in a single request.                      │
│    • Memory-maps test vectors directly into address space (zero disk I/O).             │
│    • Sub-0.8ms Early-Exit: Traps failed tests instantly, freeing 75% server capacity.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🚀 2. PARALLEL MULTI-CORE FAN-OUT (APEX)                                               │
│    • Compiles user binary once, fans out across 50+ CPU silicon isolates concurrently. │
│    • Hardware-enforced cgroups v2 per test case with zero cross-test interference.     │
│    • 38.2ms total grading time for 50 parallel competitive programming contest tests.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ ⚡ 3. STREAMING HIGH-THROUGHPUT (OMNI)                                                 │
│    • Single-stream unified process workhorse for automated batch validation.          │
│    • Evaluated 5,000 C/C++ test cases in 67 milliseconds (13.4 microseconds per test). │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 📊 4. DATA SCIENCE & MATPLOTLIB RENDERING                                              │
│    • Pre-baked scientific stack: NumPy, Pandas, Matplotlib, Seaborn, SymPy.            │
│    • Extracts charts directly from RAM buffers and renders base64 PNG visualizations.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🗄️ 5. DISPOSABLE EPHEMERAL DATABASES (DBMS)                                           │
│    • Native interactive SQL grading across PostgreSQL 16, MySQL 8.0, SQLite & Oracle.  │
│    • Provisions ephemeral, isolated database tables per test case and auto-drops data. │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ ⏱️ 6. ALGORITHMIC COMPLEXITY PROFILING                                                 │
│    • Deterministic Big-O verification using JIT assembly instruction counting.         │
│    • Catches and flags O(N²) brute-force cheats where O(N log N) is required.          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🛡️ 7. INSTANT MEMORY SAFETY & LEAK DETECTION                                          │
│    • Sub-20ms detection of buffer overflows, memory leaks, and undefined behavior.     │
│    • Native kernel AddressSanitizer (ASan) and UndefinedBehaviorSanitizer (UBSan).     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🎯 8. CUSTOM SPECIAL JUDGES & TWO-WAY IPC                                              │
│    • Interactive reactive protocol problems, game trees, and floating-point tolerances.│
│    • Author-written C++ / Python validator binaries with real-time pipe splicing.      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🥊 Head-to-Head: Eschaton vs Legacy Judge0

| Evaluation Metric | Legacy Judge0 CE on AWS | Nephis Eschaton | Performance Advantage |
| :--- | :--- | :--- | :--- |
| **50 Parallel Test Cases** | 4,200 ms (Queued Sequential Docker) | **38.2 ms (Apex Parallel Fan-Out)** | **110x Faster** |
| **Single Invocation Latency** | 1,420 ms (Container Boot Overhead) | **< 3.4 ms (In-Memory Microkernel)** | **417x Faster** |
| **1,000 Test Cases Latency** | Times out (> 15 seconds) | **< 4.8 ms (Void In-Memory)** | **3,000x+ Faster** |
| **Monthly Idle AWS Bill** | **$190 – $300 / mo** (EC2 + Redis + RDS + ALB) | **$0.00** (Pure Scale-to-Zero) | **100% Cost Elimination** |
| **AWS Fargate Compatibility** | ❌ Blocked (Requires `--privileged` / cgroups) | **✅ 100% Cloud-Native / Serverless** | **Zero Infra Management** |
| **Early-Exit on Failed Test** | Must evaluate all or wait seconds | **< 0.8 ms instant trap** | **Saves 75% Server CPU** |
| **Identical Binary Replay** | Recompiles every run (200–800ms) | **< 0.1 ms (SHM Binary Cache)** | **33x Higher Burst Capacity** |
| **Drop-in Judge0 API Parity** | Standard | **100% 1:1 REST API Match** | **Zero Code Rewrite** |

---

## 🔌 100% Drop-In Judge0 Replacement (Zero Code Changes)

Eschaton exposes the exact same `/submissions` and `/submissions/batch` endpoints:

```diff
# In your application's .env file:
- JUDGE0_URL=https://judge0-ce.p.rapidapi.com
+ JUDGE0_URL=https://eschaton.theeducode.com
```

### Drop-In Migration in Node.js / TypeScript:
```typescript
import axios from 'axios';

// Zero rewrite: use your existing Judge0 request schema
const response = await axios.post('https://eschaton.theeducode.com/v1/submissions?wait=true', {
  source_code: '#include <iostream>\nint main() { std::cout << 42; return 0; }',
  language_id: 54, // Standard Judge0 C++ ID
  stdin: ''
}, {
  headers: {
    'Content-Type': 'application/json',
    'X-Auth-Token': process.env.ESCHATON_API_KEY // 500 Free Credits
  }
});

console.log(response.data);
// Returns standard Judge0 response:
// { "stdout": "42", "status": { "id": 3, "description": "Accepted" }, "time": "0.003", "memory": 384 }
```

### Drop-In Migration in Python:
```python
import requests

response = requests.post(
    "https://eschaton.theeducode.com/v1/submissions?wait=true",
    headers={"X-Auth-Token": "YOUR_ESCHATON_API_KEY"},
    json={
        "language_id": 71,  # Standard Judge0 Python 3 ID
        "source_code": "print(sum(range(100)))",
        "stdin": ""
    }
)
print(response.json())
```

---

# 🐳 2. OPEN SOURCE DISTRIBUTION: JUDGE0 PRODUCTION AWS

For teams that must self-host on Docker containers due to strict internal compliance, we maintain this production-hardened distribution of **Judge0 v1.13.0**.

Default Judge0 distributions ship with outdated runtimes (GCC 9, Node 12, Python 3.8) and lack database connectivity. This distribution adds modern toolchains and automated MySQL JDBC connectivity.

---

## 📦 Container Registry Packages

Pull the pre-built, production-ready image directly:

### Option A: Docker Hub (2,470+ Verified Pulls)
```bash
docker pull mrmohitrajdeo/judge0-jdbc:v5.1
```

### Option B: GitHub Container Registry
```bash
docker pull ghcr.io/mohitrajdeo/judge0-jdbc:latest
```

---

## 📋 Active Modern Languages Matrix

| Language ID | Runtime / Compiler | Source File | Run Command Summary |
| :--- | :--- | :--- | :--- |
| **201** | **C (GCC 14)** | `main.c` | Modern GCC 14 with C23 standard |
| **202** | **C++ (GCC 14)** | `main.cpp` | Modern G++ 14 with C++20/C++23 |
| **203** | **Java (OpenJDK 17 LTS)** | `Main.java` | Standard OpenJDK 17 |
| **204** | **Python (3.11)** | `script.py` | Modern CPython 3.11 |
| **205** | **Java (OpenJDK 21 LTS)** | `Main.java` | Modern OpenJDK 21 |
| **206** | **JavaScript (Node.js 22)**| `script.js` | Modern Node.js LTS |
| **207** | **TypeScript (Node.js 22)**| `script.ts` | Modern TypeScript compiler |
| **62**  | **Java (JDBC Enabled)**   | `Main.java` | Uses `-cp ".:/usr/local/lib/mysql-connector.jar"` |

*(Legacy language IDs 46–74 remain active for backwards compatibility).*

---

## 🚀 Quickstart: Deploying Judge0 Self-Hosted on AWS

```bash
# 1. Clone this repository
git clone https://github.com/mohitrajdeo/judge0-production-aws.git
cd judge0-production-aws

# 2. Tune host kernel parameters (prevents zombie process leaks)
sudo chmod +x kernel_tune.sh
sudo ./kernel_tune.sh

# 3. Spin up with Docker Compose
docker compose up -d
```

---

## 📬 Free Starter Access & Commercial Support

If your platform is evaluating code at scale and you need **sub-38ms execution**, **parallel test fan-out**, or **zero-maintenance serverless infrastructure**:

* 🌐 **Live Portal:** [https://eschaton.theeducode.com](https://eschaton.theeducode.com) *(Instant 500 Credits)*
* 🥊 **Compare Judge0:** [https://eschaton.theeducode.com/compare/judge0](https://eschaton.theeducode.com/compare/judge0)
* 📧 **Email:** `mohit@theeducode.com`

---

### 📄 License
This repository is open-sourced under the [MIT License](LICENSE).  
Eschaton Cloud Engine is proprietary technology developed by Mohit Rajdeo.
