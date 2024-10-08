# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 386 ms: 1.01x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.04 sec: 1.15x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 140 ms: 1.27x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 435 ms: 2.18x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.98x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 580 ms: 1.95x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 751 ms: 1.70x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.95x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.3 ms: 1.53x faster                                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 246 ms: 1.04x faster                                                    |
| regex_compile  | 177 ms                                                                | 188 ms: 1.06x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.81 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.36x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 391 us: 1.35x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 50.8 ms: 1.05x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.3 ms: 1.03x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.15x faster                                                    |
| async_tree_none          | 950 ms                                                                | 435 ms: 2.18x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.24 ms: 2.11x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.98x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 580 ms: 1.95x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.56 ms: 1.92x faster                                                   |
| raytrace                 | 573 ms                                                                | 328 ms: 1.75x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 751 ms: 1.70x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 36.8 us: 1.67x faster                                                   |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                    |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                    |
| scimark_lu               | 227 ms                                                                | 147 ms: 1.54x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 614 ms: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 88.3 ms: 1.53x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 88.2 ms: 1.52x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| richards_super           | 107 ms                                                                | 75.0 ms: 1.43x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.69 ms: 1.42x faster                                                   |
| go                       | 264 ms                                                                | 186 ms: 1.42x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 90.8 ms: 1.41x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.2 us: 1.37x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.36x faster                                                    |
| chaos                    | 121 ms                                                                | 88.9 ms: 1.36x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 391 us: 1.35x faster                                                    |
| richards                 | 91.7 ms                                                               | 68.4 ms: 1.34x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.44 us: 1.31x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.16 us: 1.30x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| deepcopy                 | 511 us                                                                | 397 us: 1.29x faster                                                    |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.22 ms: 1.28x faster                                                   |
| thrift                   | 1.26 ms                                                               | 992 us: 1.27x faster                                                    |
| tornado_http             | 178 ms                                                                | 140 ms: 1.27x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| pyflate                  | 795 ms                                                                | 643 ms: 1.24x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.21x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.81 us: 1.21x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                   |
| generators               | 68.1 ms                                                               | 57.2 ms: 1.19x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.13x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.80 ms: 1.12x faster                                                   |
| scimark_fft              | 500 ms                                                                | 454 ms: 1.10x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.0 ms: 1.09x faster                                                   |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.06x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.06x faster                                                   |
| django_template          | 53.3 ms                                                               | 50.8 ms: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 246 ms: 1.04x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| meteor_contest           | 126 ms                                                                | 122 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.3 ms: 1.03x faster                                                   |
| 2to3                     | 381 ms                                                                | 386 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.32 ms: 1.03x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 78.4 ms: 1.04x slower                                                   |
| nqueens                  | 117 ms                                                                | 123 ms: 1.04x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| regex_compile            | 177 ms                                                                | 188 ms: 1.06x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 28.9 ms: 1.09x slower                                                   |
| sympy_expand             | 543 ms                                                                | 604 ms: 1.11x slower                                                    |
| sympy_str                | 329 ms                                                                | 370 ms: 1.13x slower                                                    |
| async_generators         | 452 ms                                                                | 511 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.81 ms: 1.13x slower                                                   |
| docutils                 | 3.53 sec                                                              | 4.04 sec: 1.15x slower                                                  |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.7 ms: 1.17x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.35 sec: 1.17x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                   |
| sympy_sum                | 184 ms                                                                | 218 ms: 1.18x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.79 sec: 1.18x slower                                                  |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.08 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_iterparse, pylint, pidigits, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.25x