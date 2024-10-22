# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 518 ms: 1.36x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.08 sec: 1.16x slower                                                  |
| html5lib       | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| tornado_http   | 178 ms                                                                | 208 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.27x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.39 sec: 1.65x faster                                                  |
| async_tree_none         | 950 ms                                                                | 606 ms: 1.57x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 731 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 908 ms: 1.40x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 206 ms: 1.53x slower                                                    |
| nbody          | 166 ms                                                                | 281 ms: 1.70x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.37x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 33.0 ms: 1.03x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.46 ms: 1.05x slower                                                   |
| regex_compile  | 177 ms                                                                | 257 ms: 1.46x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 18.2 ms: 1.09x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.6 us: 1.25x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.22 sec: 1.26x slower                                                  |
| xml_etree_process    | 99.5 ms                                                               | 132 ms: 1.32x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 773 us: 1.46x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 546 us: 1.49x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 18.2 ms: 1.63x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.70x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 104 ms: 1.48x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 52.9 ms: 1.50x slower                                                   |
| mako            | 18.9 ms                                                               | 28.7 ms: 1.52x slower                                                   |
| django_template | 53.3 ms                                                               | 82.7 ms: 1.55x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.51x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 337 us: 1.96x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.51 ms: 1.93x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.39 sec: 1.65x faster                                                  |
| async_tree_none          | 950 ms                                                                | 606 ms: 1.57x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 731 ms: 1.55x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 673 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 908 ms: 1.40x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.62 ms: 1.39x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.56 sec: 1.28x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.50 ms: 1.19x faster                                                   |
| generators               | 68.1 ms                                                               | 58.4 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 33.0 ms: 1.03x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                    |
| crypto_pyaes             | 134 ms                                                                | 139 ms: 1.03x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.46 ms: 1.05x slower                                                   |
| pylint                   | 485 ms                                                                | 514 ms: 1.06x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 18.2 ms: 1.09x slower                                                   |
| deepcopy                 | 511 us                                                                | 557 us: 1.09x slower                                                    |
| coroutines               | 37.2 ms                                                               | 40.6 ms: 1.09x slower                                                   |
| scimark_fft              | 500 ms                                                                | 576 ms: 1.15x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.08 sec: 1.16x slower                                                  |
| tornado_http             | 178 ms                                                                | 208 ms: 1.17x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.33 sec: 1.17x slower                                                  |
| deepcopy_memo            | 61.7 us                                                               | 72.3 us: 1.17x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.94 ms: 1.17x slower                                                   |
| json                     | 5.88 ms                                                               | 6.93 ms: 1.18x slower                                                   |
| pycparser                | 1.69 sec                                                              | 2.03 sec: 1.20x slower                                                  |
| comprehensions           | 33.1 us                                                               | 40.9 us: 1.23x slower                                                   |
| spectral_norm            | 186 ms                                                                | 231 ms: 1.24x slower                                                    |
| json_loads               | 30.9 us                                                               | 38.6 us: 1.25x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 4.22 sec: 1.26x slower                                                  |
| richards                 | 91.7 ms                                                               | 117 ms: 1.27x slower                                                    |
| richards_super           | 107 ms                                                                | 138 ms: 1.28x slower                                                    |
| nqueens                  | 117 ms                                                                | 151 ms: 1.29x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.02 sec: 1.29x slower                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 5.94 us: 1.29x slower                                                   |
| logging_silent           | 222 ns                                                                | 287 ns: 1.29x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 34.8 ms: 1.31x slower                                                   |
| chaos                    | 121 ms                                                                | 159 ms: 1.31x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 97.1 ms: 1.32x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 132 ms: 1.32x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.67 ms: 1.33x slower                                                   |
| meteor_contest           | 126 ms                                                                | 168 ms: 1.33x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 2.13 ms: 1.34x slower                                                   |
| fannkuch                 | 546 ms                                                                | 736 ms: 1.35x slower                                                    |
| 2to3                     | 381 ms                                                                | 518 ms: 1.36x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 174 ms: 1.36x slower                                                    |
| scimark_sor              | 246 ms                                                                | 342 ms: 1.39x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| raytrace                 | 573 ms                                                                | 812 ms: 1.42x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.8 ms: 1.43x slower                                                   |
| async_generators         | 452 ms                                                                | 652 ms: 1.44x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.8 ms: 1.45x slower                                                   |
| regex_compile            | 177 ms                                                                | 257 ms: 1.46x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 773 us: 1.46x slower                                                    |
| go                       | 264 ms                                                                | 389 ms: 1.47x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 104 ms: 1.48x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 546 us: 1.49x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 234 ms: 1.50x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.27 ms: 1.50x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 52.9 ms: 1.50x slower                                                   |
| telco                    | 8.49 ms                                                               | 12.8 ms: 1.50x slower                                                   |
| logging_format           | 10.6 us                                                               | 16.1 us: 1.51x slower                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 3.65 ms: 1.52x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.7 ms: 1.52x slower                                                   |
| logging_simple           | 9.78 us                                                               | 14.9 us: 1.53x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.76 sec: 1.53x slower                                                  |
| float                    | 135 ms                                                                | 206 ms: 1.53x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.63 sec: 1.54x slower                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 116 ms: 1.54x slower                                                    |
| django_template          | 53.3 ms                                                               | 82.7 ms: 1.55x slower                                                   |
| scimark_lu               | 227 ms                                                                | 353 ms: 1.56x slower                                                    |
| sympy_str                | 329 ms                                                                | 516 ms: 1.57x slower                                                    |
| coverage                 | 83.6 ms                                                               | 135 ms: 1.61x slower                                                    |
| python_startup           | 11.2 ms                                                               | 18.2 ms: 1.63x slower                                                   |
| nbody                    | 166 ms                                                                | 281 ms: 1.70x slower                                                    |
| sympy_sum                | 184 ms                                                                | 317 ms: 1.73x slower                                                    |
| sympy_expand             | 543 ms                                                                | 959 ms: 1.77x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (3): pidigits, pathlib, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 1.34x