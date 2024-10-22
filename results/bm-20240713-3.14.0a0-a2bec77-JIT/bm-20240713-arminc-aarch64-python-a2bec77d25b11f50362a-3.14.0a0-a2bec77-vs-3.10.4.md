# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 361 ms: 1.05x faster                                                    |
| html5lib       | 86.5 ms                                                               | 69.9 ms: 1.24x faster                                                   |
| tornado_http   | 178 ms                                                                | 142 ms: 1.25x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.13x faster                                                  |
| async_tree_none         | 950 ms                                                                | 451 ms: 2.11x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 590 ms: 1.92x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 739 ms: 1.72x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.96x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.6 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 274 us: 1.33x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 415 us: 1.28x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.94 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 50.9 ms: 1.05x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.17x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.13x faster                                                  |
| async_tree_none          | 950 ms                                                                | 451 ms: 2.11x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.45 ms: 2.01x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 590 ms: 1.92x faster                                                    |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                    |
| generators               | 68.1 ms                                                               | 38.6 ms: 1.76x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 8.27 ms: 1.76x faster                                                   |
| richards_super           | 107 ms                                                                | 61.4 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 739 ms: 1.72x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.3 ms: 1.69x faster                                                   |
| logging_silent           | 222 ns                                                                | 136 ns: 1.64x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.62x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 87.0 ms: 1.54x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 625 ms: 1.51x faster                                                    |
| float                    | 135 ms                                                                | 90.6 ms: 1.49x faster                                                   |
| go                       | 264 ms                                                                | 181 ms: 1.46x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 89.9 ms: 1.42x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.4 us: 1.41x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.02 ms: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 178 ms: 1.39x faster                                                    |
| deepcopy                 | 511 us                                                                | 372 us: 1.37x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.17 us: 1.36x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.93 us: 1.34x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 274 us: 1.33x faster                                                    |
| chaos                    | 121 ms                                                                | 90.9 ms: 1.33x faster                                                   |
| pyflate                  | 795 ms                                                                | 603 ms: 1.32x faster                                                    |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.29x faster                                                    |
| thrift                   | 1.26 ms                                                               | 974 us: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 415 us: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                   |
| tornado_http             | 178 ms                                                                | 142 ms: 1.25x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                  |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 69.9 ms: 1.24x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.03 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                   |
| pylint                   | 485 ms                                                                | 413 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 470 ms: 1.16x faster                                                    |
| dask                     | 450 ms                                                                | 391 ms: 1.15x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.03 us: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.76 ms: 1.13x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 69.1 ms: 1.09x faster                                                   |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| 2to3                     | 381 ms                                                                | 361 ms: 1.05x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.9 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 71.1 ms: 1.03x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.13 sec: 1.02x faster                                                  |
| sympy_str                | 329 ms                                                                | 324 ms: 1.02x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 26.2 ms: 1.01x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.34 sec: 1.01x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 660 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.39 ms: 1.06x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.02 ms: 1.21x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.94 ms: 1.30x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (8): sympy_expand, pidigits, nqueens, sympy_sum, docutils, regex_compile, regex_dna, json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.24x