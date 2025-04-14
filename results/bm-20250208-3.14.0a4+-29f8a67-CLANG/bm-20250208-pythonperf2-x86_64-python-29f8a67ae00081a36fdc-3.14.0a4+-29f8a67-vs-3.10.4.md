# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.421x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 273 ms: 1.28x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                       |
| html5lib       | 94.6 ms                                                      | 64.7 ms: 1.46x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 613 ms: 2.61x faster                                                         |
| async_tree_none         | 692 ms                                                       | 270 ms: 2.56x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 323 ms: 2.53x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 532 ms: 1.76x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 65.3 ms: 1.70x faster                                                        |
| nbody          | 134 ms                                                       | 82.2 ms: 1.63x faster                                                        |
| pidigits       | 271 ms                                                       | 291 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 130 ms: 1.46x faster                                                         |
| regex_dna      | 261 ms                                                       | 226 ms: 1.16x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.02 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 198 us: 1.58x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 304 us: 1.49x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.00 sec: 1.46x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 53.8 ms: 1.41x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 76.9 ms: 1.20x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 163 ms: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 33.2 ms: 1.51x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 21.0 ms: 1.50x faster                                                        |
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 49.2 ms: 1.29x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 159 us: 3.38x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 613 ms: 2.61x faster                                                         |
| async_tree_none          | 692 ms                                                       | 270 ms: 2.56x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 323 ms: 2.53x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.04 ms: 2.46x faster                                                        |
| go                       | 262 ms                                                       | 120 ms: 2.18x faster                                                         |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                        |
| logging_silent           | 167 ns                                                       | 84.3 ns: 1.99x faster                                                        |
| chaos                    | 109 ms                                                       | 54.8 ms: 1.98x faster                                                        |
| scimark_sor              | 180 ms                                                       | 90.9 ms: 1.98x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 54.4 ms: 1.97x faster                                                        |
| spectral_norm            | 139 ms                                                       | 70.9 ms: 1.96x faster                                                        |
| raytrace                 | 489 ms                                                       | 252 ms: 1.94x faster                                                         |
| richards_super           | 90.6 ms                                                      | 46.7 ms: 1.94x faster                                                        |
| scimark_lu               | 167 ms                                                       | 87.2 ms: 1.91x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 26.1 us: 1.91x faster                                                        |
| pyflate                  | 733 ms                                                       | 395 ms: 1.86x faster                                                         |
| pylint                   | 566 ms                                                       | 306 ms: 1.85x faster                                                         |
| richards                 | 75.1 ms                                                      | 40.8 ms: 1.84x faster                                                        |
| deepcopy                 | 468 us                                                       | 258 us: 1.81x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.24 ms: 1.80x faster                                                        |
| comprehensions           | 26.7 us                                                      | 14.9 us: 1.80x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 532 ms: 1.76x faster                                                         |
| float                    | 111 ms                                                       | 65.3 ms: 1.70x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.62 ms: 1.66x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.72 ms: 1.65x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.5 ms: 1.64x faster                                                        |
| nbody                    | 134 ms                                                       | 82.2 ms: 1.63x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 198 us: 1.58x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.62 us: 1.53x faster                                                        |
| django_template          | 50.2 ms                                                      | 33.2 ms: 1.51x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 21.0 ms: 1.50x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 304 us: 1.49x faster                                                         |
| logging_simple           | 8.88 us                                                      | 5.95 us: 1.49x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.4 ms: 1.48x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.56 us: 1.47x faster                                                        |
| thrift                   | 1.18 ms                                                      | 800 us: 1.47x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 64.7 ms: 1.46x faster                                                        |
| regex_compile            | 190 ms                                                       | 130 ms: 1.46x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.00 sec: 1.46x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 53.8 ms: 1.41x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 754 ms: 1.39x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                       |
| nqueens                  | 115 ms                                                       | 84.5 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                        |
| scimark_fft              | 361 ms                                                       | 267 ms: 1.36x faster                                                         |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.36x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.0 ms: 1.33x faster                                                        |
| sympy_sum                | 193 ms                                                       | 146 ms: 1.32x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 111 ms: 1.30x faster                                                         |
| sympy_str                | 360 ms                                                       | 278 ms: 1.29x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 883 us: 1.29x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 49.2 ms: 1.29x faster                                                        |
| 2to3                     | 350 ms                                                       | 273 ms: 1.28x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 55.0 ms: 1.28x faster                                                        |
| sympy_expand             | 600 ms                                                       | 471 ms: 1.27x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.1 ms: 1.27x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.3 ms: 1.26x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.17 ms: 1.22x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 76.9 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                                        |
| regex_dna                | 261 ms                                                       | 226 ms: 1.16x faster                                                         |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.76 us: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 411 ms: 1.02x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.02 ms: 1.02x faster                                                        |
| telco                    | 7.23 ms                                                      | 7.35 ms: 1.02x slower                                                        |
| xml_etree_parse          | 160 ms                                                       | 163 ms: 1.02x slower                                                         |
| pidigits                 | 271 ms                                                       | 291 ms: 1.07x slower                                                         |
| coverage                 | 63.3 ms                                                      | 74.2 ms: 1.17x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.81 ms: 1.59x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.66 ms: 1.66x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.22 sec: 192.05x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.421x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x