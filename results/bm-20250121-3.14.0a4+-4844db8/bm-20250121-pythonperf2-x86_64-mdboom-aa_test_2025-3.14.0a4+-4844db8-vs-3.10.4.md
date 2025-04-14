# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                 |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                               |
| html5lib       | 94.6 ms                                                      | 66.5 ms: 1.42x faster                                                |
| Geometric mean | (ref)                                                        | 1.28x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 626 ms: 2.55x faster                                                 |
| async_tree_none         | 692 ms                                                       | 275 ms: 2.51x faster                                                 |
| async_tree_memoization  | 819 ms                                                       | 340 ms: 2.41x faster                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 507 ms: 1.85x faster                                                 |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.5 ms: 1.60x faster                                                |
| nbody          | 134 ms                                                       | 87.1 ms: 1.54x faster                                                |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                        | 1.38x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                 |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                 |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                |
| regex_effbot   | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                        | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 219 us: 1.42x faster                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                               |
| pickle_pure_python   | 455 us                                                       | 339 us: 1.34x faster                                                 |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                |
| xml_etree_process    | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                                |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 96.2 ms: 1.15x faster                                                |
| xml_etree_generate   | 92.3 ms                                                      | 83.2 ms: 1.11x faster                                                |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.0 ms: 1.40x faster                                                |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                |
| genshi_text     | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.93x faster                                                 |
| async_tree_io            | 1.60 sec                                                     | 626 ms: 2.55x faster                                                 |
| async_tree_none          | 692 ms                                                       | 275 ms: 2.51x faster                                                 |
| async_tree_memoization   | 819 ms                                                       | 340 ms: 2.41x faster                                                 |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                |
| go                       | 262 ms                                                       | 126 ms: 2.08x faster                                                 |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 507 ms: 1.85x faster                                                 |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                 |
| chaos                    | 109 ms                                                       | 59.5 ms: 1.83x faster                                                |
| pylint                   | 566 ms                                                       | 316 ms: 1.79x faster                                                 |
| scimark_lu               | 167 ms                                                       | 96.3 ms: 1.73x faster                                                |
| richards_super           | 90.6 ms                                                      | 52.6 ms: 1.72x faster                                                |
| logging_silent           | 167 ns                                                       | 97.1 ns: 1.72x faster                                                |
| scimark_monte_carlo      | 107 ms                                                       | 62.6 ms: 1.72x faster                                                |
| sqlglot_parse            | 2.24 ms                                                      | 1.31 ms: 1.71x faster                                                |
| spectral_norm            | 139 ms                                                       | 83.7 ms: 1.66x faster                                                |
| deepcopy                 | 468 us                                                       | 283 us: 1.65x faster                                                 |
| richards                 | 75.1 ms                                                      | 45.5 ms: 1.65x faster                                                |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                |
| pyflate                  | 733 ms                                                       | 446 ms: 1.64x faster                                                 |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                 |
| crypto_pyaes             | 119 ms                                                       | 73.9 ms: 1.61x faster                                                |
| float                    | 111 ms                                                       | 69.5 ms: 1.60x faster                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 1.69 ms: 1.59x faster                                                |
| hexiom                   | 9.42 ms                                                      | 6.00 ms: 1.57x faster                                                |
| nbody                    | 134 ms                                                       | 87.1 ms: 1.54x faster                                                |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                |
| unpickle_pure_python     | 312 us                                                       | 219 us: 1.42x faster                                                 |
| html5lib                 | 94.6 ms                                                      | 66.5 ms: 1.42x faster                                                |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                               |
| django_template          | 50.2 ms                                                      | 36.0 ms: 1.40x faster                                                |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                 |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.36x faster                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 779 ms: 1.35x faster                                                 |
| pickle_pure_python       | 455 us                                                       | 339 us: 1.34x faster                                                 |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                |
| logging_simple           | 8.88 us                                                      | 6.69 us: 1.33x faster                                                |
| logging_format           | 9.64 us                                                      | 7.28 us: 1.32x faster                                                |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                 |
| nqueens                  | 115 ms                                                       | 89.8 ms: 1.28x faster                                                |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                 |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                |
| genshi_text              | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                |
| xml_etree_process        | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                                |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                 |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                 |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                 |
| mdp                      | 3.01 sec                                                     | 2.44 sec: 1.23x faster                                               |
| bench_thread_pool        | 1.14 ms                                                      | 926 us: 1.23x faster                                                 |
| dulwich_log              | 81.1 ms                                                      | 66.1 ms: 1.23x faster                                                |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 57.7 ms: 1.22x faster                                                |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                 |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                 |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                 |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 96.2 ms: 1.15x faster                                                |
| xml_etree_generate       | 92.3 ms                                                      | 83.2 ms: 1.11x faster                                                |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.59 ms: 1.11x faster                                                |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                 |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                |
| async_generators         | 421 ms                                                       | 410 ms: 1.03x faster                                                 |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                                |
| telco                    | 7.23 ms                                                      | 7.99 ms: 1.11x slower                                                |
| coverage                 | 63.3 ms                                                      | 74.1 ms: 1.17x slower                                                |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.75 ms: 1.56x slower                                                |
| gc_traversal             | 3.42 ms                                                      | 6.36 ms: 1.86x slower                                                |
| bench_mp_pool            | 6.37 ms                                                      | 1.87 sec: 293.37x slower                                             |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                         |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x