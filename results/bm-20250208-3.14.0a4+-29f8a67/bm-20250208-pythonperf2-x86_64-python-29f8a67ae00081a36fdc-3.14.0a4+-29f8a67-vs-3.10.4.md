# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.354x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 643 ms: 2.48x faster                                                         |
| async_tree_none         | 692 ms                                                       | 288 ms: 2.40x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 519 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.0 ms: 1.61x faster                                                        |
| nbody          | 134 ms                                                       | 93.7 ms: 1.43x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                        |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 95.2 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.89 us: 1.05x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.6 us: 1.08x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.7 us: 1.21x slower                                                        |
| pickle               | 9.89 us                                                      | 12.3 us: 1.24x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.39 us: 1.31x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                        |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.3 ms: 1.30x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 53.9 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 643 ms: 2.48x faster                                                         |
| async_tree_none          | 692 ms                                                       | 288 ms: 2.40x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.27x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                         |
| go                       | 262 ms                                                       | 127 ms: 2.05x faster                                                         |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                       |
| chaos                    | 109 ms                                                       | 60.1 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 519 ms: 1.80x faster                                                         |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                         |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                         |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.6 ms: 1.76x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.5 ms: 1.75x faster                                                        |
| pyflate                  | 733 ms                                                       | 426 ms: 1.72x faster                                                         |
| logging_silent           | 167 ns                                                       | 97.8 ns: 1.71x faster                                                        |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.66x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.35 ms: 1.66x faster                                                        |
| spectral_norm            | 139 ms                                                       | 84.1 ms: 1.65x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.7 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.9 ms: 1.64x faster                                                        |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                         |
| float                    | 111 ms                                                       | 69.0 ms: 1.61x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 31.0 us: 1.61x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.06 ms: 1.55x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.73 ms: 1.55x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                        |
| nbody                    | 134 ms                                                       | 93.7 ms: 1.43x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.43x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.77 us: 1.42x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                         |
| thrift                   | 1.18 ms                                                      | 856 us: 1.37x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.36x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 781 ms: 1.34x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.31x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.4 ms: 1.30x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.3 ms: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                                         |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 57.4 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 939 us: 1.22x faster                                                         |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.21x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 66.9 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                       |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 50.4 ns: 1.19x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.9 ms: 1.17x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 95.2 ms: 1.16x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.13x faster                                                        |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                         |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.67 ms: 1.09x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| async_generators         | 421 ms                                                       | 410 ms: 1.03x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.89 us: 1.05x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.6 us: 1.08x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.89 ms: 1.09x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.7 us: 1.21x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.3 us: 1.24x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.5 ms: 1.26x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.39 us: 1.31x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.85 ms: 1.62x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.37 ms: 1.87x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 889 ms: 139.49x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.354x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x