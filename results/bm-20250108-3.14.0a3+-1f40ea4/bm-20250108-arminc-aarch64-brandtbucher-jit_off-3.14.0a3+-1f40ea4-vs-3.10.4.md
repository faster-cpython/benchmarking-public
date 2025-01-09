# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_off
- machine: linux-aarch64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                              |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                            |
| html5lib       | 86.5 ms                                                               | 63.4 ms: 1.36x faster                                             |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 895 ms: 2.55x faster                                              |
| async_tree_none         | 950 ms                                                                | 381 ms: 2.49x faster                                              |
| async_tree_memoization  | 1.13 sec                                                              | 492 ms: 2.30x faster                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 677 ms: 1.88x faster                                              |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.9 ms: 1.50x faster                                             |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                              |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                              |
| regex_effbot   | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                             |
| regex_dna      | 257 ms                                                                | 244 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.39x faster                                              |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                              |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                            |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                              |
| xml_etree_process    | 99.5 ms                                                               | 83.0 ms: 1.20x faster                                             |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                             |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.08x faster                                              |
| xml_etree_generate   | 123 ms                                                                | 118 ms: 1.04x faster                                              |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.07 ms: 1.32x slower                                             |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.2 ms: 1.34x faster                                             |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                             |
| django_template | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                             |
| genshi_xml      | 69.8 ms                                                               | 63.6 ms: 1.10x faster                                             |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.17x faster                                              |
| async_tree_io            | 2.28 sec                                                              | 895 ms: 2.55x faster                                              |
| async_tree_none          | 950 ms                                                                | 381 ms: 2.49x faster                                              |
| async_tree_memoization   | 1.13 sec                                                              | 492 ms: 2.30x faster                                              |
| deltablue                | 8.94 ms                                                               | 3.99 ms: 2.24x faster                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 677 ms: 1.88x faster                                              |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.87x faster                                             |
| go                       | 264 ms                                                                | 147 ms: 1.80x faster                                              |
| richards_super           | 107 ms                                                                | 60.1 ms: 1.78x faster                                             |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                              |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                             |
| chaos                    | 121 ms                                                                | 73.7 ms: 1.64x faster                                             |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.64x faster                                              |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.64x faster                                             |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                              |
| crypto_pyaes             | 134 ms                                                                | 83.5 ms: 1.61x faster                                             |
| sqlglot_transpile        | 2.84 ms                                                               | 1.77 ms: 1.60x faster                                             |
| comprehensions           | 33.1 us                                                               | 21.0 us: 1.58x faster                                             |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                              |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                              |
| scimark_monte_carlo      | 128 ms                                                                | 85.1 ms: 1.50x faster                                             |
| float                    | 135 ms                                                                | 89.9 ms: 1.50x faster                                             |
| deepcopy_memo            | 61.7 us                                                               | 41.7 us: 1.48x faster                                             |
| hexiom                   | 10.9 ms                                                               | 7.51 ms: 1.45x faster                                             |
| deepcopy                 | 511 us                                                                | 355 us: 1.44x faster                                              |
| spectral_norm            | 186 ms                                                                | 131 ms: 1.43x faster                                              |
| pyflate                  | 795 ms                                                                | 566 ms: 1.41x faster                                              |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                              |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.39x faster                                              |
| html5lib                 | 86.5 ms                                                               | 63.4 ms: 1.36x faster                                             |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                              |
| thrift                   | 1.26 ms                                                               | 940 us: 1.34x faster                                              |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.34x faster                                             |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                              |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                            |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.33x faster                                             |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                              |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                            |
| logging_format           | 10.6 us                                                               | 8.23 us: 1.29x faster                                             |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                             |
| django_template          | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                             |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                              |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                             |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.6 ms: 1.24x faster                                             |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.72 us: 1.23x faster                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.24 ms: 1.22x faster                                             |
| dulwich_log              | 73.5 ms                                                               | 60.7 ms: 1.21x faster                                             |
| sympy_integrate          | 26.5 ms                                                               | 22.0 ms: 1.21x faster                                             |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                              |
| sqlglot_normalize        | 156 ms                                                                | 130 ms: 1.20x faster                                              |
| xml_etree_process        | 99.5 ms                                                               | 83.0 ms: 1.20x faster                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 958 ms: 1.20x faster                                              |
| sqlglot_optimize         | 75.4 ms                                                               | 63.2 ms: 1.19x faster                                             |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                             |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.18x faster                                            |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                            |
| scimark_fft              | 500 ms                                                                | 429 ms: 1.17x faster                                              |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.17x faster                                             |
| sympy_str                | 329 ms                                                                | 287 ms: 1.15x faster                                              |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                             |
| fannkuch                 | 546 ms                                                                | 489 ms: 1.12x faster                                              |
| sympy_expand             | 543 ms                                                                | 487 ms: 1.11x faster                                              |
| nqueens                  | 117 ms                                                                | 106 ms: 1.11x faster                                              |
| genshi_xml               | 69.8 ms                                                               | 63.6 ms: 1.10x faster                                             |
| regex_effbot             | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                             |
| mdp                      | 3.70 sec                                                              | 3.42 sec: 1.08x faster                                            |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.08x faster                                              |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                              |
| json                     | 5.88 ms                                                               | 5.51 ms: 1.07x faster                                             |
| regex_dna                | 257 ms                                                                | 244 ms: 1.05x faster                                              |
| xml_etree_generate       | 123 ms                                                                | 118 ms: 1.04x faster                                              |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                              |
| async_generators         | 452 ms                                                                | 506 ms: 1.12x slower                                              |
| telco                    | 8.49 ms                                                               | 9.82 ms: 1.16x slower                                             |
| coverage                 | 83.6 ms                                                               | 106 ms: 1.27x slower                                              |
| python_startup_no_site   | 6.89 ms                                                               | 9.07 ms: 1.32x slower                                             |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.62 ms: 1.60x slower                                             |
| gc_traversal             | 4.15 ms                                                               | 6.96 ms: 1.67x slower                                             |
| bench_mp_pool            | 14.5 ms                                                               | 5.05 sec: 347.53x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                      |

Benchmark hidden because not significant (4): sqlite_synth, regex_v8, pidigits, json_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x