# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_shim
- machine: linux-aarch64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.295x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                              |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                            |
| html5lib       | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                             |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 898 ms: 2.55x faster                                              |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.40x faster                                              |
| async_tree_none         | 950 ms                                                                | 399 ms: 2.38x faster                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 668 ms: 1.90x faster                                              |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.5 ms: 1.63x faster                                             |
| nbody          | 166 ms                                                                | 124 ms: 1.33x faster                                              |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                              |
| regex_v8       | 32.2 ms                                                               | 27.2 ms: 1.18x faster                                             |
| regex_dna      | 257 ms                                                                | 221 ms: 1.17x faster                                              |
| regex_effbot   | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                             |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 249 us: 1.47x faster                                              |
| tomli_loads          | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                            |
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                              |
| xml_etree_process    | 99.5 ms                                                               | 77.8 ms: 1.28x faster                                             |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                             |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                              |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.08x faster                                              |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                             |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                             |
| genshi_text     | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                             |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                             |
| genshi_xml      | 69.8 ms                                                               | 62.0 ms: 1.13x faster                                             |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                              |
| async_tree_io            | 2.28 sec                                                              | 898 ms: 2.55x faster                                              |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.40x faster                                              |
| async_tree_none          | 950 ms                                                                | 399 ms: 2.38x faster                                              |
| deltablue                | 8.94 ms                                                               | 3.83 ms: 2.33x faster                                             |
| mdp                      | 3.70 sec                                                              | 1.62 sec: 2.29x faster                                            |
| richards_super           | 107 ms                                                                | 49.7 ms: 2.16x faster                                             |
| richards                 | 91.7 ms                                                               | 43.3 ms: 2.12x faster                                             |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.91x faster                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 668 ms: 1.90x faster                                              |
| scimark_sor              | 246 ms                                                                | 139 ms: 1.78x faster                                              |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                             |
| go                       | 264 ms                                                                | 150 ms: 1.76x faster                                              |
| logging_silent           | 222 ns                                                                | 128 ns: 1.74x faster                                              |
| raytrace                 | 573 ms                                                                | 330 ms: 1.74x faster                                              |
| deepcopy_memo            | 61.7 us                                                               | 36.0 us: 1.72x faster                                             |
| float                    | 135 ms                                                                | 82.5 ms: 1.63x faster                                             |
| spectral_norm            | 186 ms                                                                | 117 ms: 1.59x faster                                              |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.58x faster                                              |
| scimark_monte_carlo      | 128 ms                                                                | 81.0 ms: 1.58x faster                                             |
| deepcopy                 | 511 us                                                                | 337 us: 1.52x faster                                              |
| comprehensions           | 33.1 us                                                               | 21.9 us: 1.52x faster                                             |
| pylint                   | 485 ms                                                                | 321 ms: 1.51x faster                                              |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                             |
| hexiom                   | 10.9 ms                                                               | 7.41 ms: 1.47x faster                                             |
| pyflate                  | 795 ms                                                                | 541 ms: 1.47x faster                                              |
| unpickle_pure_python     | 366 us                                                                | 249 us: 1.47x faster                                              |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                              |
| tomli_loads              | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 93.2 ms: 1.44x faster                                             |
| logging_format           | 10.6 us                                                               | 7.55 us: 1.41x faster                                             |
| logging_simple           | 9.78 us                                                               | 7.00 us: 1.40x faster                                             |
| html5lib                 | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                             |
| dulwich_log              | 73.5 ms                                                               | 53.2 ms: 1.38x faster                                             |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                              |
| nbody                    | 166 ms                                                                | 124 ms: 1.33x faster                                              |
| genshi_text              | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                             |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                             |
| sympy_integrate          | 26.5 ms                                                               | 20.5 ms: 1.29x faster                                             |
| xml_etree_process        | 99.5 ms                                                               | 77.8 ms: 1.28x faster                                             |
| thrift                   | 1.26 ms                                                               | 988 us: 1.28x faster                                              |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                             |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                              |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.26x faster                                            |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                              |
| scimark_fft              | 500 ms                                                                | 411 ms: 1.22x faster                                              |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                             |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.18x faster                                             |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                              |
| regex_v8                 | 32.2 ms                                                               | 27.2 ms: 1.18x faster                                             |
| sympy_str                | 329 ms                                                                | 281 ms: 1.17x faster                                              |
| regex_dna                | 257 ms                                                                | 221 ms: 1.17x faster                                              |
| fannkuch                 | 546 ms                                                                | 470 ms: 1.16x faster                                              |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                            |
| sqlite_synth             | 4.12 us                                                               | 3.61 us: 1.14x faster                                             |
| genshi_xml               | 69.8 ms                                                               | 62.0 ms: 1.13x faster                                             |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                              |
| nqueens                  | 117 ms                                                                | 106 ms: 1.11x faster                                              |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                              |
| sympy_expand             | 543 ms                                                                | 490 ms: 1.11x faster                                              |
| regex_effbot             | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                             |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.08x faster                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.15 ms: 1.07x faster                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.24 sec: 1.05x faster                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.04x faster                                            |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                              |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                             |
| async_generators         | 452 ms                                                                | 486 ms: 1.07x slower                                              |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                              |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                             |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                             |
| gc_traversal             | 4.15 ms                                                               | 6.75 ms: 1.63x slower                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.78 ms: 1.67x slower                                             |
| telco                    | 8.49 ms                                                               | 164 ms: 19.32x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                      |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.295x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.40x