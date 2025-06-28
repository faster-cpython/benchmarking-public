# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_o2
- machine: linux-aarch64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.330x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 312 ms: 1.22x faster                                            |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                          |
| html5lib       | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                           |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 898 ms: 2.54x faster                                            |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                            |
| async_tree_none         | 950 ms                                                                | 397 ms: 2.39x faster                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 664 ms: 1.91x faster                                            |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.4 ms: 1.62x faster                                           |
| nbody          | 166 ms                                                                | 128 ms: 1.29x faster                                            |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                            |
| regex_v8       | 32.2 ms                                                               | 26.6 ms: 1.21x faster                                           |
| regex_dna      | 257 ms                                                                | 226 ms: 1.14x faster                                            |
| regex_effbot   | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                          |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                            |
| pickle_pure_python   | 529 us                                                                | 390 us: 1.36x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                           |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                           |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                            |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                            |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                            |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                           |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                           |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                           |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                           |
| genshi_xml      | 69.8 ms                                                               | 64.0 ms: 1.09x faster                                           |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.22x faster                                            |
| async_tree_io            | 2.28 sec                                                              | 898 ms: 2.54x faster                                            |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                            |
| async_tree_none          | 950 ms                                                                | 397 ms: 2.39x faster                                            |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                           |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.23x faster                                          |
| richards_super           | 107 ms                                                                | 53.5 ms: 2.00x faster                                           |
| richards                 | 91.7 ms                                                               | 46.5 ms: 1.97x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 664 ms: 1.91x faster                                            |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.83x faster                                           |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                           |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                            |
| raytrace                 | 573 ms                                                                | 335 ms: 1.71x faster                                            |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                            |
| go                       | 264 ms                                                                | 158 ms: 1.67x faster                                            |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                           |
| float                    | 135 ms                                                                | 83.4 ms: 1.62x faster                                           |
| scimark_monte_carlo      | 128 ms                                                                | 81.7 ms: 1.56x faster                                           |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                            |
| comprehensions           | 33.1 us                                                               | 21.8 us: 1.52x faster                                           |
| deepcopy                 | 511 us                                                                | 339 us: 1.51x faster                                            |
| pylint                   | 485 ms                                                                | 323 ms: 1.50x faster                                            |
| pyflate                  | 795 ms                                                                | 532 ms: 1.49x faster                                            |
| hexiom                   | 10.9 ms                                                               | 7.56 ms: 1.44x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                          |
| scimark_lu               | 227 ms                                                                | 158 ms: 1.44x faster                                            |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                           |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                            |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 95.2 ms: 1.41x faster                                           |
| logging_simple           | 9.78 us                                                               | 7.12 us: 1.37x faster                                           |
| html5lib                 | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                           |
| pickle_pure_python       | 529 us                                                                | 390 us: 1.36x faster                                            |
| logging_format           | 10.6 us                                                               | 7.86 us: 1.35x faster                                           |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                           |
| thrift                   | 1.26 ms                                                               | 965 us: 1.31x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 56.7 ms: 1.30x faster                                           |
| nbody                    | 166 ms                                                                | 128 ms: 1.29x faster                                            |
| xml_etree_process        | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                           |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                           |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                           |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.71 us: 1.24x faster                                           |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.24x faster                                            |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                           |
| scimark_fft              | 500 ms                                                                | 409 ms: 1.22x faster                                            |
| 2to3                     | 381 ms                                                                | 312 ms: 1.22x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.22x faster                                          |
| regex_v8                 | 32.2 ms                                                               | 26.6 ms: 1.21x faster                                           |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                            |
| sympy_str                | 329 ms                                                                | 278 ms: 1.18x faster                                            |
| fannkuch                 | 546 ms                                                                | 473 ms: 1.15x faster                                            |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                            |
| regex_dna                | 257 ms                                                                | 226 ms: 1.14x faster                                            |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                          |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                           |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                            |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                            |
| genshi_xml               | 69.8 ms                                                               | 64.0 ms: 1.09x faster                                           |
| sympy_expand             | 543 ms                                                                | 498 ms: 1.09x faster                                            |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                            |
| regex_effbot             | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                           |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.15 ms: 1.07x faster                                           |
| json                     | 5.88 ms                                                               | 5.63 ms: 1.04x faster                                           |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.02x faster                                          |
| pprint_safe_repr         | 1.15 sec                                                              | 1.13 sec: 1.01x faster                                          |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                            |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                           |
| async_generators         | 452 ms                                                                | 482 ms: 1.07x slower                                            |
| telco                    | 8.49 ms                                                               | 9.50 ms: 1.12x slower                                           |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.21x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                           |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.62x slower                                           |
| gc_traversal             | 4.15 ms                                                               | 6.80 ms: 1.64x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.330x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.39x