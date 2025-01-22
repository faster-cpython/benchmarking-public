# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.188x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 336 ms: 1.04x faster                                                 |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                               |
| html5lib       | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                |
| Geometric mean | (ref)                                                        | 1.15x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 609 ms: 2.62x faster                                                 |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                 |
| async_tree_memoization  | 819 ms                                                       | 359 ms: 2.28x faster                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 527 ms: 1.77x faster                                                 |
| Geometric mean          | (ref)                                                        | 2.25x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 111 ms                                                       | 74.6 ms: 1.49x faster                                                |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                        | 1.18x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 156 ms: 1.22x faster                                                 |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                 |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                |
| regex_effbot   | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 110 ms                                                       | 87.8 ms: 1.26x faster                                                |
| unpickle_pure_python | 312 us                                                       | 250 us: 1.25x faster                                                 |
| xml_etree_parse      | 160 ms                                                       | 132 ms: 1.22x faster                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.42 sec: 1.21x faster                                               |
| pickle_pure_python   | 455 us                                                       | 392 us: 1.16x faster                                                 |
| json_loads           | 30.3 us                                                      | 27.7 us: 1.10x faster                                                |
| json_dumps           | 14.5 ms                                                      | 13.4 ms: 1.09x faster                                                |
| xml_etree_process    | 75.9 ms                                                      | 74.2 ms: 1.02x faster                                                |
| xml_etree_generate   | 92.3 ms                                                      | 97.4 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                |
| python_startup         | 11.5 ms                                                      | 18.7 ms: 1.63x slower                                                |
| Geometric mean         | (ref)                                                        | 1.62x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 46.2 ms: 1.09x faster                                                |
| genshi_text     | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                |
| genshi_xml      | 63.3 ms                                                      | 63.9 ms: 1.01x slower                                                |
| mako            | 14.7 ms                                                      | 18.0 ms: 1.22x slower                                                |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 609 ms: 2.62x faster                                                 |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                 |
| typing_runtime_protocols | 537 us                                                       | 225 us: 2.39x faster                                                 |
| async_tree_memoization   | 819 ms                                                       | 359 ms: 2.28x faster                                                 |
| generators               | 57.3 ms                                                      | 31.7 ms: 1.81x faster                                                |
| go                       | 262 ms                                                       | 147 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 527 ms: 1.77x faster                                                 |
| deltablue                | 7.50 ms                                                      | 4.47 ms: 1.68x faster                                                |
| logging_silent           | 167 ns                                                       | 102 ns: 1.64x faster                                                 |
| pylint                   | 566 ms                                                       | 351 ms: 1.61x faster                                                 |
| chaos                    | 109 ms                                                       | 71.1 ms: 1.53x faster                                                |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.51x faster                                                 |
| pyflate                  | 733 ms                                                       | 491 ms: 1.49x faster                                                 |
| float                    | 111 ms                                                       | 74.6 ms: 1.49x faster                                                |
| raytrace                 | 489 ms                                                       | 338 ms: 1.45x faster                                                 |
| deepcopy                 | 468 us                                                       | 332 us: 1.41x faster                                                 |
| scimark_lu               | 167 ms                                                       | 119 ms: 1.40x faster                                                 |
| spectral_norm            | 139 ms                                                       | 99.4 ms: 1.40x faster                                                |
| sqlglot_parse            | 2.24 ms                                                      | 1.61 ms: 1.39x faster                                                |
| richards_super           | 90.6 ms                                                      | 66.1 ms: 1.37x faster                                                |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                |
| deepcopy_memo            | 49.8 us                                                      | 37.4 us: 1.33x faster                                                |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                               |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                |
| richards                 | 75.1 ms                                                      | 57.1 ms: 1.32x faster                                                |
| hexiom                   | 9.42 ms                                                      | 7.24 ms: 1.30x faster                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 2.08 ms: 1.29x faster                                                |
| scimark_monte_carlo      | 107 ms                                                       | 83.3 ms: 1.29x faster                                                |
| crypto_pyaes             | 119 ms                                                       | 93.0 ms: 1.28x faster                                                |
| html5lib                 | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 87.8 ms: 1.26x faster                                                |
| comprehensions           | 26.7 us                                                      | 21.3 us: 1.25x faster                                                |
| unpickle_pure_python     | 312 us                                                       | 250 us: 1.25x faster                                                 |
| regex_compile            | 190 ms                                                       | 156 ms: 1.22x faster                                                 |
| xml_etree_parse          | 160 ms                                                       | 132 ms: 1.22x faster                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.42 sec: 1.21x faster                                               |
| logging_simple           | 8.88 us                                                      | 7.39 us: 1.20x faster                                                |
| logging_format           | 9.64 us                                                      | 8.18 us: 1.18x faster                                                |
| dulwich_log              | 81.1 ms                                                      | 69.7 ms: 1.16x faster                                                |
| pickle_pure_python       | 455 us                                                       | 392 us: 1.16x faster                                                 |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                               |
| sqlite_synth             | 2.99 us                                                      | 2.60 us: 1.15x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 920 ms: 1.14x faster                                                 |
| thrift                   | 1.18 ms                                                      | 1.04 ms: 1.13x faster                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.90 sec: 1.13x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.61 us: 1.11x faster                                                |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.11x faster                                                 |
| json_loads               | 30.3 us                                                      | 27.7 us: 1.10x faster                                                |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                 |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.9 ms: 1.09x faster                                                |
| json_dumps               | 14.5 ms                                                      | 13.4 ms: 1.09x faster                                                |
| django_template          | 50.2 ms                                                      | 46.2 ms: 1.09x faster                                                |
| sympy_sum                | 193 ms                                                       | 177 ms: 1.09x faster                                                 |
| mdp                      | 3.01 sec                                                     | 2.77 sec: 1.08x faster                                               |
| sqlglot_optimize         | 70.1 ms                                                      | 65.5 ms: 1.07x faster                                                |
| sqlalchemy_declarative   | 190 ms                                                       | 177 ms: 1.07x faster                                                 |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                 |
| json                     | 5.86 ms                                                      | 5.54 ms: 1.06x faster                                                |
| sympy_str                | 360 ms                                                       | 341 ms: 1.06x faster                                                 |
| sympy_expand             | 600 ms                                                       | 570 ms: 1.05x faster                                                 |
| scimark_fft              | 361 ms                                                       | 343 ms: 1.05x faster                                                 |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                |
| genshi_text              | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                |
| 2to3                     | 350 ms                                                       | 336 ms: 1.04x faster                                                 |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.04x faster                                                |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                 |
| xml_etree_process        | 75.9 ms                                                      | 74.2 ms: 1.02x faster                                                |
| fannkuch                 | 483 ms                                                       | 473 ms: 1.02x faster                                                 |
| nqueens                  | 115 ms                                                       | 114 ms: 1.01x faster                                                 |
| genshi_xml               | 63.3 ms                                                      | 63.9 ms: 1.01x slower                                                |
| regex_effbot             | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                |
| xml_etree_generate       | 92.3 ms                                                      | 97.4 ms: 1.06x slower                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.49 ms: 1.08x slower                                                |
| async_generators         | 421 ms                                                       | 470 ms: 1.12x slower                                                 |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.05 ms: 1.16x slower                                                |
| gc_traversal             | 3.42 ms                                                      | 4.09 ms: 1.20x slower                                                |
| mako                     | 14.7 ms                                                      | 18.0 ms: 1.22x slower                                                |
| telco                    | 7.23 ms                                                      | 9.03 ms: 1.25x slower                                                |
| bench_thread_pool        | 1.14 ms                                                      | 1.44 ms: 1.26x slower                                                |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                |
| coverage                 | 63.3 ms                                                      | 102 ms: 1.61x slower                                                 |
| python_startup           | 11.5 ms                                                      | 18.7 ms: 1.63x slower                                                |
| bench_mp_pool            | 6.37 ms                                                      | 49.0 ms: 7.70x slower                                                |
| Geometric mean           | (ref)                                                        | 1.16x faster                                                         |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.188x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.54x