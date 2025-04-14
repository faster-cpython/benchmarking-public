# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.205x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 335 ms: 1.04x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 619 ms: 2.58x faster                                                         |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 365 ms: 2.24x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 534 ms: 1.75x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 73.3 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| nbody          | 134 ms                                                       | 129 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.24x faster                                                         |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 238 us: 1.31x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 90.1 ms: 1.23x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.40 sec: 1.21x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 379 us: 1.20x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 13.3 ms: 1.09x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 69.8 ms: 1.09x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 97.1 ms: 1.05x slower                                                        |
| json_loads           | 30.3 us                                                      | 32.1 us: 1.06x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.6 us: 1.16x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.44 us: 1.17x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 36.7 us: 1.24x slower                                                        |
| pickle               | 9.89 us                                                      | 12.5 us: 1.27x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.30 us: 1.29x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup         | 11.5 ms                                                      | 18.7 ms: 1.63x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.62x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.2 ms: 1.11x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.7 ms: 1.01x faster                                                        |
| mako            | 14.7 ms                                                      | 17.7 ms: 1.20x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 619 ms: 2.58x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 217 us: 2.48x faster                                                         |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 365 ms: 2.24x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 425 ms: 1.83x faster                                                         |
| generators               | 57.3 ms                                                      | 31.7 ms: 1.81x faster                                                        |
| go                       | 262 ms                                                       | 148 ms: 1.77x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 534 ms: 1.75x faster                                                         |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                         |
| deltablue                | 7.50 ms                                                      | 4.52 ms: 1.66x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.06 ms: 1.66x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 351 ms: 1.61x faster                                                         |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                         |
| chaos                    | 109 ms                                                       | 70.7 ms: 1.54x faster                                                        |
| float                    | 111 ms                                                       | 73.3 ms: 1.52x faster                                                        |
| pyflate                  | 733 ms                                                       | 486 ms: 1.51x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                        |
| raytrace                 | 489 ms                                                       | 338 ms: 1.45x faster                                                         |
| spectral_norm            | 139 ms                                                       | 96.8 ms: 1.44x faster                                                        |
| scimark_lu               | 167 ms                                                       | 117 ms: 1.43x faster                                                         |
| deepcopy                 | 468 us                                                       | 332 us: 1.41x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 36.3 us: 1.37x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.64 ms: 1.37x faster                                                        |
| richards_super           | 90.6 ms                                                      | 66.5 ms: 1.36x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.9 us: 1.34x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.04 ms: 1.31x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 238 us: 1.31x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.23 ms: 1.30x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                       |
| richards                 | 75.1 ms                                                      | 58.0 ms: 1.29x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 83.0 ms: 1.29x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 93.3 ms: 1.28x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.11 us: 1.25x faster                                                        |
| regex_compile            | 190 ms                                                       | 154 ms: 1.24x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 90.1 ms: 1.23x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.92 us: 1.22x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.40 sec: 1.21x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 872 ms: 1.20x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 379 us: 1.20x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.84 sec: 1.17x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.57 us: 1.16x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 69.9 ms: 1.16x faster                                                        |
| thrift                   | 1.18 ms                                                      | 1.01 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 127 ms: 1.13x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.56 us: 1.13x faster                                                        |
| django_template          | 50.2 ms                                                      | 45.2 ms: 1.11x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 172 ms: 1.10x faster                                                         |
| sympy_sum                | 193 ms                                                       | 175 ms: 1.10x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.7 ms: 1.10x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 13.3 ms: 1.09x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 69.8 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.78 sec: 1.08x faster                                                       |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 65.3 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                        |
| sympy_str                | 360 ms                                                       | 337 ms: 1.07x faster                                                         |
| sympy_expand             | 600 ms                                                       | 565 ms: 1.06x faster                                                         |
| scimark_fft              | 361 ms                                                       | 341 ms: 1.06x faster                                                         |
| nqueens                  | 115 ms                                                       | 110 ms: 1.05x faster                                                         |
| 2to3                     | 350 ms                                                       | 335 ms: 1.04x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 27.1 ms: 1.04x faster                                                        |
| nbody                    | 134 ms                                                       | 129 ms: 1.04x faster                                                         |
| fannkuch                 | 483 ms                                                       | 468 ms: 1.03x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.03x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 62.7 ms: 1.01x faster                                                        |
| json                     | 5.86 ms                                                      | 6.03 ms: 1.03x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 63.0 ns: 1.05x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 97.1 ms: 1.05x slower                                                        |
| json_loads               | 30.3 us                                                      | 32.1 us: 1.06x slower                                                        |
| async_generators         | 421 ms                                                       | 467 ms: 1.11x slower                                                         |
| meteor_contest           | 138 ms                                                       | 154 ms: 1.11x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.96 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.77 ms: 1.14x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.6 us: 1.16x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.44 us: 1.17x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.7 ms: 1.20x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 36.7 us: 1.24x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.09 ms: 1.26x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.27x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.46 ms: 1.28x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.30 us: 1.29x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup           | 11.5 ms                                                      | 18.7 ms: 1.63x slower                                                        |
| coverage                 | 63.3 ms                                                      | 104 ms: 1.64x slower                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 49.0 ms: 7.69x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.16x faster                                                                 |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.205x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.54x