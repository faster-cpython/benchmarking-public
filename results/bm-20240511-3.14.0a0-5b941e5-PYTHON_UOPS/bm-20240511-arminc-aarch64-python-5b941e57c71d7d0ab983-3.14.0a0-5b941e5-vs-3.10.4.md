# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 354 ms: 1.07x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.96 ms: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 74.8 ms: 1.16x faster                                                   |
| tornado_http   | 178 ms                                                                | 136 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 517 ms: 1.84x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 670 ms: 1.69x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 816 ms: 1.56x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.73x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 138 ms: 1.20x faster                                                    |
| float          | 135 ms                                                                | 114 ms: 1.19x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 167 ms: 1.06x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| regex_dna      | 257 ms                                                                | 261 ms: 1.01x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.20x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 449 us: 1.18x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 88.5 ms: 1.12x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 3.08 sec: 1.09x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 197 ms: 1.08x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.51 us: 1.07x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 349 us: 1.05x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 125 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 162 ms: 1.04x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.9 us: 1.11x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.47 ms: 1.23x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 16.5 ms: 1.15x faster                                                   |
| django_template | 53.3 ms                                                               | 49.9 ms: 1.07x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 36.6 ms: 1.04x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 77.7 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 227 us: 2.91x faster                                                    |
| async_tree_none          | 950 ms                                                                | 517 ms: 1.84x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                  |
| deltablue                | 8.94 ms                                                               | 5.19 ms: 1.72x faster                                                   |
| generators               | 68.1 ms                                                               | 39.7 ms: 1.72x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 670 ms: 1.69x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.60 ms: 1.69x faster                                                   |
| raytrace                 | 573 ms                                                                | 342 ms: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 575 ms: 1.64x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 816 ms: 1.56x faster                                                    |
| richards_super           | 107 ms                                                                | 71.9 ms: 1.49x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.47x faster                                                  |
| chaos                    | 121 ms                                                                | 85.1 ms: 1.42x faster                                                   |
| richards                 | 91.7 ms                                                               | 65.4 ms: 1.40x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.75 ms: 1.37x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.28 us: 1.34x faster                                                   |
| go                       | 264 ms                                                                | 198 ms: 1.33x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 102 ms: 1.31x faster                                                    |
| tornado_http             | 178 ms                                                                | 136 ms: 1.31x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.09 us: 1.31x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.29x faster                                                   |
| thrift                   | 1.26 ms                                                               | 985 us: 1.28x faster                                                    |
| scimark_sor              | 246 ms                                                                | 198 ms: 1.24x faster                                                    |
| pylint                   | 485 ms                                                                | 392 ms: 1.24x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.23x faster                                                  |
| coroutines               | 37.2 ms                                                               | 30.4 ms: 1.22x faster                                                   |
| nbody                    | 166 ms                                                                | 138 ms: 1.20x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.20x faster                                                   |
| float                    | 135 ms                                                                | 114 ms: 1.19x faster                                                    |
| logging_silent           | 222 ns                                                                | 188 ns: 1.18x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 449 us: 1.18x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                   |
| dask                     | 450 ms                                                                | 387 ms: 1.16x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 74.8 ms: 1.16x faster                                                   |
| mako                     | 18.9 ms                                                               | 16.5 ms: 1.15x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 64.9 ms: 1.13x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 88.5 ms: 1.12x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 114 ms: 1.12x faster                                                    |
| comprehensions           | 33.1 us                                                               | 30.0 us: 1.11x faster                                                   |
| scimark_lu               | 227 ms                                                                | 207 ms: 1.10x faster                                                    |
| pyflate                  | 795 ms                                                                | 726 ms: 1.10x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.08 sec: 1.09x faster                                                  |
| chameleon                | 10.8 ms                                                               | 9.96 ms: 1.09x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 24.3 ms: 1.08x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 197 ms: 1.08x faster                                                    |
| 2to3                     | 381 ms                                                                | 354 ms: 1.07x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.51 us: 1.07x faster                                                   |
| django_template          | 53.3 ms                                                               | 49.9 ms: 1.07x faster                                                   |
| sympy_sum                | 184 ms                                                                | 172 ms: 1.07x faster                                                    |
| regex_compile            | 177 ms                                                                | 167 ms: 1.06x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 349 us: 1.05x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 72.4 ms: 1.04x faster                                                   |
| sympy_expand             | 543 ms                                                                | 522 ms: 1.04x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.96 us: 1.04x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.5 ms: 1.04x faster                                                   |
| sympy_str                | 329 ms                                                                | 317 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.60 sec: 1.03x faster                                                  |
| json                     | 5.88 ms                                                               | 5.79 ms: 1.01x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.37 sec: 1.01x slower                                                  |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                                  |
| regex_dna                | 257 ms                                                                | 261 ms: 1.01x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 125 ms: 1.01x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 162 ms: 1.04x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 36.6 ms: 1.04x slower                                                   |
| flaskblogging            | 4.83 ms                                                               | 5.05 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.98 ms: 1.05x slower                                                   |
| meteor_contest           | 126 ms                                                                | 132 ms: 1.05x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.84 us: 1.05x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| fannkuch                 | 546 ms                                                                | 575 ms: 1.05x slower                                                    |
| deepcopy                 | 511 us                                                                | 541 us: 1.06x slower                                                    |
| scimark_fft              | 500 ms                                                                | 537 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.43 ms: 1.08x slower                                                   |
| nqueens                  | 117 ms                                                                | 130 ms: 1.10x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 77.7 ms: 1.11x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.9 us: 1.11x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| async_generators         | 452 ms                                                                | 523 ms: 1.16x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 71.6 us: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.1 ms: 1.19x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.47 ms: 1.23x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.15 ms: 1.24x slower                                                   |
| telco                    | 8.49 ms                                                               | 166 ms: 19.50x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (5): sympy_integrate, pickle_list, spectral_norm, docutils, pidigits
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.14x