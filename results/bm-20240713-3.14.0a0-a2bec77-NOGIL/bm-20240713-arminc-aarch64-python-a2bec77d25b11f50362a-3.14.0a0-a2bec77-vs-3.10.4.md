# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 517 ms: 1.36x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.10 sec: 1.16x slower                                                  |
| html5lib       | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| tornado_http   | 178 ms                                                                | 202 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.40 sec: 1.64x faster                                                  |
| async_tree_none         | 950 ms                                                                | 611 ms: 1.55x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 748 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 910 ms: 1.40x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 210 ms: 1.56x slower                                                    |
| nbody          | 166 ms                                                                | 289 ms: 1.74x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.39x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 32.5 ms: 1.01x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.30 ms: 1.01x slower                                                   |
| regex_compile  | 177 ms                                                                | 256 ms: 1.45x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 17.6 ms: 1.05x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.7 us: 1.25x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                  |
| xml_etree_process    | 99.5 ms                                                               | 129 ms: 1.30x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 160 ms: 1.30x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 774 us: 1.46x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 542 us: 1.48x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.20x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 17.6 ms: 1.58x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 11.7 ms: 1.70x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.64x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 104 ms: 1.48x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 53.2 ms: 1.51x slower                                                   |
| mako            | 18.9 ms                                                               | 28.8 ms: 1.52x slower                                                   |
| django_template | 53.3 ms                                                               | 83.2 ms: 1.56x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.52x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.25 ms: 2.33x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 331 us: 2.00x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.40 sec: 1.64x faster                                                  |
| async_tree_none          | 950 ms                                                                | 611 ms: 1.55x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 748 ms: 1.52x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.58 ms: 1.43x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 910 ms: 1.40x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 684 ms: 1.38x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.47 sec: 1.33x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.42 ms: 1.21x faster                                                   |
| generators               | 68.1 ms                                                               | 58.4 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 32.5 ms: 1.01x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.30 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                    |
| pylint                   | 485 ms                                                                | 504 ms: 1.04x slower                                                    |
| crypto_pyaes             | 134 ms                                                                | 140 ms: 1.04x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 17.6 ms: 1.05x slower                                                   |
| coroutines               | 37.2 ms                                                               | 39.2 ms: 1.06x slower                                                   |
| deepcopy                 | 511 us                                                                | 559 us: 1.10x slower                                                    |
| tornado_http             | 178 ms                                                                | 202 ms: 1.13x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.10 sec: 1.16x slower                                                  |
| deepcopy_memo            | 61.7 us                                                               | 72.0 us: 1.17x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.37 sec: 1.18x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 9.05 ms: 1.19x slower                                                   |
| json                     | 5.88 ms                                                               | 7.01 ms: 1.19x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.91 ms: 1.20x slower                                                   |
| scimark_fft              | 500 ms                                                                | 601 ms: 1.20x slower                                                    |
| pycparser                | 1.69 sec                                                              | 2.06 sec: 1.22x slower                                                  |
| comprehensions           | 33.1 us                                                               | 40.7 us: 1.23x slower                                                   |
| json_loads               | 30.9 us                                                               | 38.7 us: 1.25x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                  |
| spectral_norm            | 186 ms                                                                | 237 ms: 1.27x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.02 sec: 1.28x slower                                                  |
| nqueens                  | 117 ms                                                                | 151 ms: 1.28x slower                                                    |
| logging_silent           | 222 ns                                                                | 287 ns: 1.29x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 129 ms: 1.30x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 160 ms: 1.30x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 6.02 us: 1.31x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 35.0 ms: 1.32x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.67 ms: 1.32x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 97.3 ms: 1.32x slower                                                   |
| chaos                    | 121 ms                                                                | 161 ms: 1.33x slower                                                    |
| richards_super           | 107 ms                                                                | 145 ms: 1.36x slower                                                    |
| 2to3                     | 381 ms                                                                | 517 ms: 1.36x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 175 ms: 1.37x slower                                                    |
| fannkuch                 | 546 ms                                                                | 750 ms: 1.38x slower                                                    |
| meteor_contest           | 126 ms                                                                | 174 ms: 1.38x slower                                                    |
| richards                 | 91.7 ms                                                               | 127 ms: 1.39x slower                                                    |
| scimark_sor              | 246 ms                                                                | 343 ms: 1.39x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.8 ms: 1.39x slower                                                   |
| html5lib                 | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.6 ms: 1.43x slower                                                   |
| raytrace                 | 573 ms                                                                | 825 ms: 1.44x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.9 ms: 1.44x slower                                                   |
| regex_compile            | 177 ms                                                                | 256 ms: 1.45x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 774 us: 1.46x slower                                                    |
| logging_format           | 10.6 us                                                               | 15.6 us: 1.47x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 230 ms: 1.48x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 542 us: 1.48x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 104 ms: 1.48x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.6 us: 1.49x slower                                                   |
| async_generators         | 452 ms                                                                | 678 ms: 1.50x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 53.2 ms: 1.51x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.8 ms: 1.52x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 116 ms: 1.53x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.38 ms: 1.54x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 3.64 sec: 1.54x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.77 sec: 1.54x slower                                                  |
| float                    | 135 ms                                                                | 210 ms: 1.56x slower                                                    |
| django_template          | 53.3 ms                                                               | 83.2 ms: 1.56x slower                                                   |
| scimark_lu               | 227 ms                                                                | 355 ms: 1.56x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.78 ms: 1.57x slower                                                   |
| python_startup           | 11.2 ms                                                               | 17.6 ms: 1.58x slower                                                   |
| sympy_str                | 329 ms                                                                | 519 ms: 1.58x slower                                                    |
| coverage                 | 83.6 ms                                                               | 134 ms: 1.60x slower                                                    |
| go                       | 264 ms                                                                | 448 ms: 1.70x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 11.7 ms: 1.70x slower                                                   |
| sympy_sum                | 184 ms                                                                | 318 ms: 1.73x slower                                                    |
| nbody                    | 166 ms                                                                | 289 ms: 1.74x slower                                                    |
| sympy_expand             | 543 ms                                                                | 956 ms: 1.76x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (3): pathlib, pidigits, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 1.32x