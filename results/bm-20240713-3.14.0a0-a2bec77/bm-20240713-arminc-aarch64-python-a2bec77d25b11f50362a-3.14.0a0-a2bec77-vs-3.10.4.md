# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.25x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 68.2 ms: 1.27x faster                                                   |
| tornado_http   | 178 ms                                                                | 136 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 437 ms: 2.18x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.13x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 562 ms: 2.02x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 725 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 93.0 ms: 1.45x faster                                                   |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 360 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.5 ms: 1.20x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| django_template | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.5 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                                   |
| async_tree_none          | 950 ms                                                                | 437 ms: 2.18x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.13x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.08 ms: 2.05x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 562 ms: 2.02x faster                                                    |
| raytrace                 | 573 ms                                                                | 299 ms: 1.92x faster                                                    |
| richards_super           | 107 ms                                                                | 59.9 ms: 1.79x faster                                                   |
| generators               | 68.1 ms                                                               | 38.0 ms: 1.79x faster                                                   |
| chaos                    | 121 ms                                                                | 68.7 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 725 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                                   |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                    |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                                    |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.62x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 592 ms: 1.59x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.8 ms: 1.54x faster                                                   |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 360 us: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| float                    | 135 ms                                                                | 93.0 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.92 us: 1.41x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.64 us: 1.39x faster                                                   |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| pyflate                  | 795 ms                                                                | 578 ms: 1.38x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.39 us: 1.36x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                  |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| tornado_http             | 178 ms                                                                | 136 ms: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 969 us: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 68.2 ms: 1.27x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                   |
| 2to3                     | 381 ms                                                                | 306 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.23x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.7 ms: 1.23x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                                   |
| dask                     | 450 ms                                                                | 368 ms: 1.22x faster                                                    |
| sympy_str                | 329 ms                                                                | 271 ms: 1.21x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.95 sec: 1.21x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 952 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.9 ms: 1.20x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.53 ms: 1.17x faster                                                   |
| sympy_expand             | 543 ms                                                                | 465 ms: 1.17x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 64.6 ms: 1.14x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 61.5 ms: 1.14x faster                                                   |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.36 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                    |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 494 ms: 1.09x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 4.98 ms: 1.20x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.5 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.14x