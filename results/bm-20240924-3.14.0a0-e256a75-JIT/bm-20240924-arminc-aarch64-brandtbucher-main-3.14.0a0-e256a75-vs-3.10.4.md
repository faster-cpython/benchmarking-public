# Results vs. 3.10.4

- fork: brandtbucher
- ref: main
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.175x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 4.02 sec: 1.14x slower                                        |
| html5lib       | 86.5 ms                                                               | 72.5 ms: 1.19x faster                                         |
| tornado_http   | 178 ms                                                                | 150 ms: 1.19x faster                                          |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                  |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 445 ms: 2.13x faster                                          |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                        |
| async_tree_memoization  | 1.13 sec                                                              | 588 ms: 1.93x faster                                          |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 754 ms: 1.69x faster                                          |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.5 ms: 1.52x faster                                         |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                          |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                         |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                          |
| regex_compile  | 177 ms                                                                | 197 ms: 1.12x slower                                          |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                         |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 266 us: 1.38x faster                                          |
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                          |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                        |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                         |
| xml_etree_process    | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                         |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                          |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                          |
| unpickle_list        | 6.99 us                                                               | 6.37 us: 1.10x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                          |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.03x slower                                         |
| pickle_dict          | 35.1 us                                                               | 38.2 us: 1.09x slower                                         |
| pickle               | 12.5 us                                                               | 13.8 us: 1.11x slower                                         |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.11x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                  |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                         |
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                         |
| django_template | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                         |
| genshi_text     | 35.2 ms                                                               | 34.6 ms: 1.02x faster                                         |
| genshi_xml      | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                         |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 215 us: 3.08x faster                                          |
| async_tree_none          | 950 ms                                                                | 445 ms: 2.13x faster                                          |
| deltablue                | 8.94 ms                                                               | 4.36 ms: 2.05x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.35 ms: 1.98x faster                                         |
| async_tree_memoization   | 1.13 sec                                                              | 588 ms: 1.93x faster                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 754 ms: 1.69x faster                                          |
| raytrace                 | 573 ms                                                                | 347 ms: 1.65x faster                                          |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.64x faster                                         |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                          |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                          |
| float                    | 135 ms                                                                | 88.5 ms: 1.52x faster                                         |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                          |
| asyncio_tcp              | 944 ms                                                                | 623 ms: 1.52x faster                                          |
| crypto_pyaes             | 134 ms                                                                | 89.9 ms: 1.49x faster                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                        |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                          |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                         |
| go                       | 264 ms                                                                | 186 ms: 1.42x faster                                          |
| richards_super           | 107 ms                                                                | 76.3 ms: 1.41x faster                                         |
| sqlglot_parse            | 2.40 ms                                                               | 1.75 ms: 1.38x faster                                         |
| richards                 | 91.7 ms                                                               | 66.6 ms: 1.38x faster                                         |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.38x faster                                          |
| scimark_monte_carlo      | 128 ms                                                                | 93.0 ms: 1.37x faster                                         |
| comprehensions           | 33.1 us                                                               | 24.3 us: 1.36x faster                                         |
| chaos                    | 121 ms                                                                | 90.8 ms: 1.33x faster                                         |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                          |
| thrift                   | 1.26 ms                                                               | 953 us: 1.32x faster                                          |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.49 us: 1.31x faster                                         |
| logging_format           | 10.6 us                                                               | 8.16 us: 1.30x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.28x faster                                         |
| deepcopy                 | 511 us                                                                | 398 us: 1.28x faster                                          |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                        |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.27x faster                                          |
| pyflate                  | 795 ms                                                                | 628 ms: 1.27x faster                                          |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                         |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                         |
| generators               | 68.1 ms                                                               | 56.5 ms: 1.20x faster                                         |
| html5lib                 | 86.5 ms                                                               | 72.5 ms: 1.19x faster                                         |
| tornado_http             | 178 ms                                                                | 150 ms: 1.19x faster                                          |
| deepcopy_reduce          | 4.60 us                                                               | 3.90 us: 1.18x faster                                         |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                         |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                          |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                        |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                          |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.86 ms: 1.11x faster                                         |
| unpickle_list            | 6.99 us                                                               | 6.37 us: 1.10x faster                                         |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                          |
| fannkuch                 | 546 ms                                                                | 510 ms: 1.07x faster                                          |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                          |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                         |
| django_template          | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                         |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.03x faster                                         |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                          |
| genshi_text              | 35.2 ms                                                               | 34.6 ms: 1.02x faster                                         |
| sqlglot_normalize        | 156 ms                                                                | 154 ms: 1.01x faster                                          |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                          |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                          |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.03x slower                                         |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                         |
| sqlglot_optimize         | 75.4 ms                                                               | 79.1 ms: 1.05x slower                                         |
| sympy_integrate          | 26.5 ms                                                               | 28.4 ms: 1.07x slower                                         |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                          |
| pickle_dict              | 35.1 us                                                               | 38.2 us: 1.09x slower                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                        |
| dulwich_log              | 73.5 ms                                                               | 81.1 ms: 1.10x slower                                         |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.11x slower                                         |
| pprint_pformat           | 2.36 sec                                                              | 2.61 sec: 1.11x slower                                        |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.11x slower                                         |
| sympy_str                | 329 ms                                                                | 366 ms: 1.11x slower                                          |
| regex_compile            | 177 ms                                                                | 197 ms: 1.12x slower                                          |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                          |
| sympy_expand             | 543 ms                                                                | 613 ms: 1.13x slower                                          |
| sympy_sum                | 184 ms                                                                | 209 ms: 1.14x slower                                          |
| docutils                 | 3.53 sec                                                              | 4.02 sec: 1.14x slower                                        |
| genshi_xml               | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                         |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                         |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                         |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                          |
| gc_traversal             | 4.15 ms                                                               | 5.12 ms: 1.23x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                         |
| telco                    | 8.49 ms                                                               | 10.7 ms: 1.27x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                  |

Benchmark hidden because not significant (4): pylint, pidigits, 2to3, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.175x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.25x