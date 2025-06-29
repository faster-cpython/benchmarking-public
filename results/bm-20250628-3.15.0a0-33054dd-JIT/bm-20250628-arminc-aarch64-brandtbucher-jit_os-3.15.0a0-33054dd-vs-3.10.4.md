# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_os
- machine: linux-aarch64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 314 ms: 1.21x faster                                            |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                          |
| html5lib       | 86.5 ms                                                               | 62.8 ms: 1.38x faster                                           |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 908 ms: 2.52x faster                                            |
| async_tree_memoization  | 1.13 sec                                                              | 473 ms: 2.39x faster                                            |
| async_tree_none         | 950 ms                                                                | 402 ms: 2.36x faster                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 672 ms: 1.89x faster                                            |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.7 ms: 1.61x faster                                           |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                            |
| pidigits       | 235 ms                                                                | 236 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                            |
| regex_v8       | 32.2 ms                                                               | 26.4 ms: 1.22x faster                                           |
| regex_dna      | 257 ms                                                                | 224 ms: 1.15x faster                                            |
| regex_effbot   | 4.25 ms                                                               | 3.80 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                          |
| unpickle_pure_python | 366 us                                                                | 258 us: 1.42x faster                                            |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 77.6 ms: 1.28x faster                                           |
| xml_etree_parse      | 212 ms                                                                | 177 ms: 1.20x faster                                            |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                           |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                            |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                            |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.66 ms: 1.26x slower                                           |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                           |
| django_template | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                           |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.29x faster                                           |
| genshi_xml      | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                           |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.08x faster                                            |
| async_tree_io            | 2.28 sec                                                              | 908 ms: 2.52x faster                                            |
| async_tree_memoization   | 1.13 sec                                                              | 473 ms: 2.39x faster                                            |
| async_tree_none          | 950 ms                                                                | 402 ms: 2.36x faster                                            |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                           |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                          |
| richards_super           | 107 ms                                                                | 50.4 ms: 2.13x faster                                           |
| richards                 | 91.7 ms                                                               | 44.7 ms: 2.05x faster                                           |
| generators               | 68.1 ms                                                               | 35.9 ms: 1.90x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 672 ms: 1.89x faster                                            |
| chaos                    | 121 ms                                                                | 69.5 ms: 1.74x faster                                           |
| raytrace                 | 573 ms                                                                | 335 ms: 1.71x faster                                            |
| go                       | 264 ms                                                                | 154 ms: 1.71x faster                                            |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                            |
| deepcopy_memo            | 61.7 us                                                               | 36.3 us: 1.70x faster                                           |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.69x faster                                            |
| float                    | 135 ms                                                                | 83.7 ms: 1.61x faster                                           |
| spectral_norm            | 186 ms                                                                | 117 ms: 1.59x faster                                            |
| scimark_monte_carlo      | 128 ms                                                                | 80.6 ms: 1.59x faster                                           |
| pyflate                  | 795 ms                                                                | 520 ms: 1.53x faster                                            |
| deepcopy                 | 511 us                                                                | 336 us: 1.52x faster                                            |
| comprehensions           | 33.1 us                                                               | 21.8 us: 1.52x faster                                           |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                            |
| hexiom                   | 10.9 ms                                                               | 7.36 ms: 1.48x faster                                           |
| pylint                   | 485 ms                                                                | 328 ms: 1.48x faster                                            |
| tomli_loads              | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                          |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                           |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 93.2 ms: 1.44x faster                                           |
| unpickle_pure_python     | 366 us                                                                | 258 us: 1.42x faster                                            |
| logging_simple           | 9.78 us                                                               | 7.01 us: 1.39x faster                                           |
| html5lib                 | 86.5 ms                                                               | 62.8 ms: 1.38x faster                                           |
| logging_format           | 10.6 us                                                               | 7.74 us: 1.37x faster                                           |
| django_template          | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                           |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 55.8 ms: 1.32x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                           |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                            |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.29x faster                                           |
| xml_etree_process        | 99.5 ms                                                               | 77.6 ms: 1.28x faster                                           |
| thrift                   | 1.26 ms                                                               | 991 us: 1.27x faster                                            |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                           |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.23x faster                                          |
| coroutines               | 37.2 ms                                                               | 30.2 ms: 1.23x faster                                           |
| scimark_fft              | 500 ms                                                                | 410 ms: 1.22x faster                                            |
| regex_v8                 | 32.2 ms                                                               | 26.4 ms: 1.22x faster                                           |
| 2to3                     | 381 ms                                                                | 314 ms: 1.21x faster                                            |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                            |
| xml_etree_parse          | 212 ms                                                                | 177 ms: 1.20x faster                                            |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                            |
| sympy_str                | 329 ms                                                                | 282 ms: 1.17x faster                                            |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                           |
| regex_dna                | 257 ms                                                                | 224 ms: 1.15x faster                                            |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                           |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                            |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                            |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                          |
| sympy_expand             | 543 ms                                                                | 485 ms: 1.12x faster                                            |
| regex_effbot             | 4.25 ms                                                               | 3.80 ms: 1.12x faster                                           |
| genshi_xml               | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                           |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                           |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                            |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.10 ms: 1.07x faster                                           |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                          |
| pidigits                 | 235 ms                                                                | 236 ms: 1.00x slower                                            |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                            |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                           |
| async_generators         | 452 ms                                                                | 479 ms: 1.06x slower                                            |
| telco                    | 8.49 ms                                                               | 9.76 ms: 1.15x slower                                           |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.24x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.66 ms: 1.26x slower                                           |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                           |
| gc_traversal             | 4.15 ms                                                               | 6.91 ms: 1.66x slower                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.97 ms: 1.76x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                    |

Benchmark hidden because not significant (2): json, pprint_safe_repr
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.40x