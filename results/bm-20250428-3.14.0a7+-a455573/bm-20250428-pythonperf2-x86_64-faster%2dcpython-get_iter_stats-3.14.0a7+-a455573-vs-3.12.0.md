# Results vs. 3.12.0

- fork: faster-cpython
- ref: get_iter_stats
- machine: linux-x86_64
- commit hash: a455573
- commit date: 2025-04-28
- overall geometric mean: 1.046x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 274 ms: 1.04x faster                                                             |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization  | 544 ms                                                       | 321 ms: 1.69x faster                                                             |
| async_tree_io           | 1.04 sec                                                     | 625 ms: 1.67x faster                                                             |
| async_tree_none         | 452 ms                                                       | 278 ms: 1.62x faster                                                             |
| async_tree_cpu_io_mixed | 696 ms                                                       | 495 ms: 1.41x faster                                                             |
| Geometric mean          | (ref)                                                        | 1.59x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.4 ms: 1.14x faster                                                            |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                             |
| nbody          | 88.0 ms                                                      | 94.9 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.25 ms: 1.10x faster                                                            |
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                             |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                             |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.6 ms: 1.06x faster                                                            |
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                            |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                             |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                             |
| pickle_pure_python   | 318 us                                                       | 324 us: 1.02x slower                                                             |
| json_loads           | 24.4 us                                                      | 25.9 us: 1.06x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                            |
| python_startup         | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.29x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.5 ms: 1.11x faster                                                            |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                      | 2.57 sec                                                     | 1.27 sec: 2.03x faster                                                           |
| async_tree_memoization   | 544 ms                                                       | 321 ms: 1.69x faster                                                             |
| async_tree_io            | 1.04 sec                                                     | 625 ms: 1.67x faster                                                             |
| async_tree_none          | 452 ms                                                       | 278 ms: 1.62x faster                                                             |
| async_tree_cpu_io_mixed  | 696 ms                                                       | 495 ms: 1.41x faster                                                             |
| deepcopy                 | 368 us                                                       | 270 us: 1.36x faster                                                             |
| deepcopy_memo            | 36.8 us                                                      | 27.5 us: 1.34x faster                                                            |
| comprehensions           | 21.9 us                                                      | 17.1 us: 1.28x faster                                                            |
| generators               | 37.4 ms                                                      | 29.4 ms: 1.27x faster                                                            |
| go                       | 150 ms                                                       | 122 ms: 1.22x faster                                                             |
| deepcopy_reduce          | 3.37 us                                                      | 2.86 us: 1.18x faster                                                            |
| logging_format           | 7.48 us                                                      | 6.51 us: 1.15x faster                                                            |
| logging_simple           | 6.71 us                                                      | 5.87 us: 1.14x faster                                                            |
| float                    | 76.6 ms                                                      | 67.4 ms: 1.14x faster                                                            |
| pathlib                  | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                            |
| scimark_monte_carlo      | 69.0 ms                                                      | 61.6 ms: 1.12x faster                                                            |
| django_template          | 38.2 ms                                                      | 34.5 ms: 1.11x faster                                                            |
| raytrace                 | 298 ms                                                       | 270 ms: 1.10x faster                                                             |
| regex_effbot             | 3.57 ms                                                      | 3.25 ms: 1.10x faster                                                            |
| sympy_integrate          | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                            |
| regex_compile            | 144 ms                                                       | 132 ms: 1.09x faster                                                             |
| sqlalchemy_declarative   | 159 ms                                                       | 147 ms: 1.09x faster                                                             |
| chaos                    | 64.0 ms                                                      | 59.0 ms: 1.09x faster                                                            |
| sympy_sum                | 162 ms                                                       | 150 ms: 1.08x faster                                                             |
| dulwich_log              | 65.4 ms                                                      | 61.1 ms: 1.07x faster                                                            |
| xml_etree_iterparse      | 103 ms                                                       | 96.6 ms: 1.06x faster                                                            |
| sympy_str                | 302 ms                                                       | 285 ms: 1.06x faster                                                             |
| tomli_loads              | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                           |
| sqlalchemy_imperative    | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                            |
| coroutines               | 23.0 ms                                                      | 21.8 ms: 1.05x faster                                                            |
| pprint_pformat           | 1.65 sec                                                     | 1.57 sec: 1.05x faster                                                           |
| deltablue                | 3.24 ms                                                      | 3.08 ms: 1.05x faster                                                            |
| pprint_safe_repr         | 807 ms                                                       | 770 ms: 1.05x faster                                                             |
| logging_silent           | 94.4 ns                                                      | 90.2 ns: 1.05x faster                                                            |
| 2to3                     | 285 ms                                                       | 274 ms: 1.04x faster                                                             |
| pidigits                 | 265 ms                                                       | 254 ms: 1.04x faster                                                             |
| scimark_sor              | 109 ms                                                       | 105 ms: 1.04x faster                                                             |
| xml_etree_generate       | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                            |
| scimark_lu               | 98.8 ms                                                      | 96.1 ms: 1.03x faster                                                            |
| spectral_norm            | 91.6 ms                                                      | 89.2 ms: 1.03x faster                                                            |
| richards                 | 45.7 ms                                                      | 44.6 ms: 1.03x faster                                                            |
| meteor_contest           | 128 ms                                                       | 125 ms: 1.03x faster                                                             |
| xml_etree_parse          | 144 ms                                                       | 141 ms: 1.02x faster                                                             |
| richards_super           | 51.3 ms                                                      | 50.3 ms: 1.02x faster                                                            |
| crypto_pyaes             | 80.3 ms                                                      | 78.8 ms: 1.02x faster                                                            |
| unpickle_pure_python     | 210 us                                                       | 207 us: 1.01x faster                                                             |
| docutils                 | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                           |
| hexiom                   | 5.96 ms                                                      | 5.94 ms: 1.00x faster                                                            |
| regex_dna                | 239 ms                                                       | 240 ms: 1.01x slower                                                             |
| scimark_fft              | 301 ms                                                       | 304 ms: 1.01x slower                                                             |
| pycparser                | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                           |
| pickle_pure_python       | 318 us                                                       | 324 us: 1.02x slower                                                             |
| nqueens                  | 89.9 ms                                                      | 92.5 ms: 1.03x slower                                                            |
| sqlite_synth             | 2.77 us                                                      | 2.86 us: 1.03x slower                                                            |
| fannkuch                 | 350 ms                                                       | 364 ms: 1.04x slower                                                             |
| async_generators         | 390 ms                                                       | 409 ms: 1.05x slower                                                             |
| json                     | 5.12 ms                                                      | 5.38 ms: 1.05x slower                                                            |
| regex_v8                 | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                            |
| json_loads               | 24.4 us                                                      | 25.9 us: 1.06x slower                                                            |
| nbody                    | 88.0 ms                                                      | 94.9 ms: 1.08x slower                                                            |
| mako                     | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                            |
| typing_runtime_protocols | 152 us                                                       | 167 us: 1.10x slower                                                             |
| json_dumps               | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                            |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 4.63 ms: 1.10x slower                                                            |
| telco                    | 6.96 ms                                                      | 7.81 ms: 1.12x slower                                                            |
| python_startup_no_site   | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                            |
| coverage                 | 66.7 ms                                                      | 81.6 ms: 1.22x slower                                                            |
| python_startup           | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                                            |
| create_gc_cycles         | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                            |
| gc_traversal             | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                            |
| bench_mp_pool            | 4.76 ms                                                      | 1.41 sec: 295.91x slower                                                         |
| Geometric mean           | (ref)                                                        | 1.03x slower                                                                     |

Benchmark hidden because not significant (5): xml_etree_process, pyflate, sympy_expand, asyncio_websockets, bench_thread_pool
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250428-3.14.0a7+-a455573/bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x