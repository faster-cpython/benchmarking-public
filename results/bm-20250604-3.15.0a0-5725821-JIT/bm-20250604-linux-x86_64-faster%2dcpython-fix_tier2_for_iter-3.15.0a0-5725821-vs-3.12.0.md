# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_tier2_for_iter
- machine: linux-x86_64
- commit hash: 5725821
- commit date: 2025-06-04
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                          |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.2 ms: 1.32x faster                                                         |
| nbody          | 97.0 ms                                                | 90.2 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.11x faster                                                         |
| regex_dna      | 212 ms                                                 | 207 ms: 1.03x faster                                                          |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 200 us: 1.15x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                          |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.12x faster                                                         |
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.26 sec: 2.08x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                          |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                         |
| richards                   | 45.8 ms                                                | 34.0 ms: 1.35x faster                                                         |
| float                      | 84.7 ms                                                | 64.2 ms: 1.32x faster                                                         |
| richards_super             | 51.5 ms                                                | 40.0 ms: 1.29x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                         |
| pyflate                    | 482 ms                                                 | 410 ms: 1.18x faster                                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 200 us: 1.15x faster                                                          |
| scimark_fft                | 382 ms                                                 | 334 ms: 1.14x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                          |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                          |
| go                         | 139 ms                                                 | 123 ms: 1.13x faster                                                          |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.0 ms: 1.12x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 61.2 ms: 1.12x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                          |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.12x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                         |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.11x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                         |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                         |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                         |
| chaos                      | 67.0 ms                                                | 62.0 ms: 1.08x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 75.9 ms: 1.08x faster                                                         |
| nbody                      | 97.0 ms                                                | 90.2 ms: 1.07x faster                                                         |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                          |
| logging_format             | 7.23 us                                                | 6.79 us: 1.07x faster                                                         |
| logging_simple             | 6.46 us                                                | 6.13 us: 1.05x faster                                                         |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                        |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                         |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.03x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.93 ms: 1.02x faster                                                         |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                        |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                         |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.45 ms: 1.01x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                         |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 776 ms                                                 | 818 ms: 1.05x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                          |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.09x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.70 sec: 1.09x slower                                                        |
| coroutines                 | 23.2 ms                                                | 26.0 ms: 1.12x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                         |
| logging_silent             | 104 ns                                                 | 474 ns: 4.54x slower                                                          |
| coverage                   | 72.7 ms                                                | 436 ms: 6.00x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (4): pidigits, json_loads, asyncio_websockets, sqlite_synth
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250604-3.15.0a0-5725821-JIT/bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x