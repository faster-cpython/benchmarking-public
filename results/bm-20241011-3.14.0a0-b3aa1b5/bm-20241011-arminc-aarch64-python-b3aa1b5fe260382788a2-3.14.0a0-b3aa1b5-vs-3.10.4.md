# Results vs. 3.10.4

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: linux-aarch64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 293 ms: 1.30x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                                  |
| html5lib       | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                   |
| tornado_http   | 178 ms                                                                | 126 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 428 ms: 2.22x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 550 ms: 2.06x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.16 sec: 1.97x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 722 ms: 1.76x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 115 ms: 1.45x faster                                                    |
| float          | 135 ms                                                                | 94.6 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 260 ms: 1.01x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 5.01 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 364 us: 1.45x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.53 us: 1.07x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 198 ms: 1.07x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.17 us: 1.01x faster                                                   |
| json_loads           | 30.9 us                                                               | 31.3 us: 1.01x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.2 us: 1.10x slower                                                   |
| pickle               | 12.5 us                                                               | 13.9 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| django_template | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.38x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| async_tree_none          | 950 ms                                                                | 428 ms: 2.22x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 550 ms: 2.06x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.16 sec: 1.97x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 137 ms: 1.93x faster                                                    |
| raytrace                 | 573 ms                                                                | 310 ms: 1.85x faster                                                    |
| richards_super           | 107 ms                                                                | 59.9 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 722 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.9 ms: 1.73x faster                                                   |
| chaos                    | 121 ms                                                                | 70.5 ms: 1.72x faster                                                   |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                                    |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 563 ms: 1.68x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.5 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| deepcopy                 | 511 us                                                                | 332 us: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                                   |
| scimark_sor              | 246 ms                                                                | 161 ms: 1.53x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 84.5 ms: 1.51x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 364 us: 1.45x faster                                                    |
| nbody                    | 166 ms                                                                | 115 ms: 1.45x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.44x faster                                                    |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                    |
| float                    | 135 ms                                                                | 94.6 ms: 1.42x faster                                                   |
| tornado_http             | 178 ms                                                                | 126 ms: 1.42x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.55 us: 1.40x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.40x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                                   |
| pyflate                  | 795 ms                                                                | 582 ms: 1.37x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                  |
| pylint                   | 485 ms                                                                | 356 ms: 1.36x faster                                                    |
| thrift                   | 1.26 ms                                                               | 931 us: 1.35x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.51 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 293 ms: 1.30x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 58.0 ms: 1.27x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 911 ms: 1.26x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 264 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.3 ms: 1.21x faster                                                   |
| sympy_expand             | 543 ms                                                                | 456 ms: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 100.0 ms: 1.17x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                                  |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.60 ms: 1.16x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                   |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 441 ms: 1.14x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.53 us: 1.07x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 198 ms: 1.07x faster                                                    |
| json                     | 5.88 ms                                                               | 5.57 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.05x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| pickle_list              | 5.24 us                                                               | 5.17 us: 1.01x faster                                                   |
| json_loads               | 30.9 us                                                               | 31.3 us: 1.01x slower                                                   |
| regex_dna                | 257 ms                                                                | 260 ms: 1.01x slower                                                    |
| async_generators         | 452 ms                                                                | 475 ms: 1.05x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.37 ms: 1.05x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.31 ms: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.2 us: 1.10x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.9 us: 1.11x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.9 ms: 1.17x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 5.01 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 5.11 sec: 351.81x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.327x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x