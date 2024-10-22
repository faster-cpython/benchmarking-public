# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.22x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 522 ms: 1.37x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.12 sec: 1.17x slower                                                  |
| html5lib       | 86.5 ms                                                               | 123 ms: 1.42x slower                                                    |
| tornado_http   | 178 ms                                                                | 209 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.28x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.39 sec: 1.64x faster                                                  |
| async_tree_none         | 950 ms                                                                | 612 ms: 1.55x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 743 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 917 ms: 1.39x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 209 ms: 1.55x slower                                                    |
| nbody          | 166 ms                                                                | 285 ms: 1.72x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.39x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 256 ms: 1.00x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 33.0 ms: 1.03x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.47 ms: 1.05x slower                                                   |
| regex_compile  | 177 ms                                                                | 258 ms: 1.46x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.17x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 18.2 ms: 1.09x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.9 us: 1.26x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.28 sec: 1.27x slower                                                  |
| xml_etree_process    | 99.5 ms                                                               | 131 ms: 1.32x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 787 us: 1.49x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 546 us: 1.49x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.22x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 18.1 ms: 1.62x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.69x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 109 ms: 1.56x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 55.1 ms: 1.56x slower                                                   |
| django_template | 53.3 ms                                                               | 84.1 ms: 1.58x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.56x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 7.16 ms: 2.03x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 344 us: 1.92x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.39 sec: 1.64x faster                                                  |
| async_tree_none          | 950 ms                                                                | 612 ms: 1.55x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 743 ms: 1.53x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 672 ms: 1.41x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.62 ms: 1.39x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 917 ms: 1.39x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.47 sec: 1.33x faster                                                  |
| generators               | 68.1 ms                                                               | 57.2 ms: 1.19x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 3.51 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.17x faster                                                    |
| regex_dna                | 257 ms                                                                | 256 ms: 1.00x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 26.6 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                    |
| regex_v8                 | 32.2 ms                                                               | 33.0 ms: 1.03x slower                                                   |
| crypto_pyaes             | 134 ms                                                                | 139 ms: 1.03x slower                                                    |
| pylint                   | 485 ms                                                                | 509 ms: 1.05x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.47 ms: 1.05x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 18.2 ms: 1.09x slower                                                   |
| deepcopy                 | 511 us                                                                | 564 us: 1.10x slower                                                    |
| coroutines               | 37.2 ms                                                               | 41.1 ms: 1.11x slower                                                   |
| scimark_fft              | 500 ms                                                                | 582 ms: 1.16x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.12 sec: 1.17x slower                                                  |
| tornado_http             | 178 ms                                                                | 209 ms: 1.17x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.34 sec: 1.17x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.96 ms: 1.18x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 73.0 us: 1.18x slower                                                   |
| json                     | 5.88 ms                                                               | 7.04 ms: 1.20x slower                                                   |
| pycparser                | 1.69 sec                                                              | 2.06 sec: 1.22x slower                                                  |
| spectral_norm            | 186 ms                                                                | 231 ms: 1.24x slower                                                    |
| comprehensions           | 33.1 us                                                               | 41.2 us: 1.24x slower                                                   |
| json_loads               | 30.9 us                                                               | 38.9 us: 1.26x slower                                                   |
| pyflate                  | 795 ms                                                                | 1.01 sec: 1.27x slower                                                  |
| tomli_loads              | 3.36 sec                                                              | 4.28 sec: 1.27x slower                                                  |
| richards                 | 91.7 ms                                                               | 117 ms: 1.28x slower                                                    |
| nqueens                  | 117 ms                                                                | 152 ms: 1.29x slower                                                    |
| richards_super           | 107 ms                                                                | 141 ms: 1.31x slower                                                    |
| logging_silent           | 222 ns                                                                | 291 ns: 1.31x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 131 ms: 1.32x slower                                                    |
| chaos                    | 121 ms                                                                | 160 ms: 1.32x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.67 ms: 1.32x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 35.2 ms: 1.33x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 6.10 us: 1.33x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 2.11 ms: 1.33x slower                                                   |
| meteor_contest           | 126 ms                                                                | 168 ms: 1.33x slower                                                    |
| fannkuch                 | 546 ms                                                                | 746 ms: 1.37x slower                                                    |
| 2to3                     | 381 ms                                                                | 522 ms: 1.37x slower                                                    |
| scimark_sor              | 246 ms                                                                | 342 ms: 1.39x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 180 ms: 1.41x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.7 ms: 1.42x slower                                                   |
| html5lib                 | 86.5 ms                                                               | 123 ms: 1.42x slower                                                    |
| raytrace                 | 573 ms                                                                | 820 ms: 1.43x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.7 ms: 1.44x slower                                                   |
| regex_compile            | 177 ms                                                                | 258 ms: 1.46x slower                                                    |
| logging_format           | 10.6 us                                                               | 15.6 us: 1.47x slower                                                   |
| async_generators         | 452 ms                                                                | 670 ms: 1.48x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.5 us: 1.48x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 232 ms: 1.49x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 787 us: 1.49x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 546 us: 1.49x slower                                                    |
| mako                     | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 4.37 ms: 1.54x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.1 ms: 1.54x slower                                                   |
| scimark_lu               | 227 ms                                                                | 351 ms: 1.55x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.72 ms: 1.55x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.78 sec: 1.55x slower                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 117 ms: 1.55x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.66 sec: 1.55x slower                                                  |
| float                    | 135 ms                                                                | 209 ms: 1.55x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 109 ms: 1.56x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 55.1 ms: 1.56x slower                                                   |
| django_template          | 53.3 ms                                                               | 84.1 ms: 1.58x slower                                                   |
| sympy_str                | 329 ms                                                                | 523 ms: 1.59x slower                                                    |
| python_startup           | 11.2 ms                                                               | 18.1 ms: 1.62x slower                                                   |
| coverage                 | 83.6 ms                                                               | 138 ms: 1.65x slower                                                    |
| go                       | 264 ms                                                                | 447 ms: 1.69x slower                                                    |
| nbody                    | 166 ms                                                                | 285 ms: 1.72x slower                                                    |
| sympy_sum                | 184 ms                                                                | 318 ms: 1.73x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| sympy_expand             | 543 ms                                                                | 971 ms: 1.79x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.22x slower                                                            |

Benchmark hidden because not significant (2): pidigits, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 1.32x