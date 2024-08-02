# Results vs. 3.12.0

- fork: faster-cpython
- ref: no_globals_builtins_
- machine: linux-x86_64
- commit hash: a701af9
- commit date: 2024-05-07
- overall geometric mean: 1.00x slower
- HPT reliability: 92.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                             |
| chameleon      | 7.41 ms                                                | 7.11 ms: 1.04x faster                                                            |
| docutils       | 2.77 sec                                               | 3.00 sec: 1.08x slower                                                           |
| tornado_http   | 103 ms                                                 | 97.5 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 348 ms: 1.29x faster                                                             |
| async_tree_none            | 472 ms                                                 | 372 ms: 1.27x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 460 ms: 1.25x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 598 ms: 1.21x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 486 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 1.03 sec: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 633 ms: 1.15x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                            |
| float          | 84.7 ms                                                | 71.7 ms: 1.18x faster                                                            |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                            |
| regex_dna      | 212 ms                                                 | 228 ms: 1.07x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                             |
| pickle_dict          | 35.5 us                                                | 33.1 us: 1.07x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 83.7 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                             |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                             |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.05 us: 1.01x faster                                                            |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                            |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.65 ms: 1.10x slower                                                            |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.60 ms: 1.24x faster                                                            |
| django_template | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 348 ms: 1.29x faster                                                             |
| async_tree_none            | 472 ms                                                 | 372 ms: 1.27x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 460 ms: 1.25x faster                                                             |
| mako                       | 11.9 ms                                                | 9.60 ms: 1.24x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 598 ms: 1.21x faster                                                             |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                             |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                                            |
| nbody                      | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 486 ms: 1.19x faster                                                             |
| float                      | 84.7 ms                                                | 71.7 ms: 1.18x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 64.2 ms: 1.17x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 1.03 sec: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 633 ms: 1.15x faster                                                             |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                             |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                                             |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                            |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.81 us: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 37.2 us: 1.09x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                             |
| pickle_dict                | 35.5 us                                                | 33.1 us: 1.07x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 83.7 ms: 1.06x faster                                                            |
| pyflate                    | 482 ms                                                 | 453 ms: 1.06x faster                                                             |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                                            |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                             |
| tornado_http               | 103 ms                                                 | 97.5 ms: 1.05x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                            |
| chameleon                  | 7.41 ms                                                | 7.11 ms: 1.04x faster                                                            |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 3.23 us: 1.04x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                            |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                            |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                             |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| pickle_list                | 5.08 us                                                | 5.05 us: 1.01x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                           |
| coroutines                 | 23.2 ms                                                | 23.1 ms: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| async_generators           | 463 ms                                                 | 465 ms: 1.00x slower                                                             |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.01x slower                                                             |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                            |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                             |
| gc_traversal               | 3.79 ms                                                | 3.84 ms: 1.01x slower                                                            |
| deltablue                  | 3.72 ms                                                | 3.76 ms: 1.01x slower                                                            |
| dask                       | 372 ms                                                 | 380 ms: 1.02x slower                                                             |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                             |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                             |
| dulwich_log                | 68.5 ms                                                | 70.1 ms: 1.02x slower                                                            |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                                             |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                            |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 56.9 ms: 1.04x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                           |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                             |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                             |
| asyncio_tcp                | 491 ms                                                 | 519 ms: 1.06x slower                                                             |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                            |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                             |
| django_template            | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                            |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                                             |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.07x slower                                                             |
| docutils                   | 2.77 sec                                               | 3.00 sec: 1.08x slower                                                           |
| gunicorn                   | 1.24 ms                                                | 1.35 ms: 1.09x slower                                                            |
| aiohttp                    | 1.15 ms                                                | 1.25 ms: 1.09x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.65 ms: 1.10x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                            |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                            |
| coverage                   | 72.7 ms                                                | 86.3 ms: 1.19x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.24x slower                                                            |
| telco                      | 7.10 ms                                                | 172 ms: 24.17x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (8): mypy2, unpickle, deepcopy, bench_mp_pool, unpickle_list, sympy_str, sqlite_synth, json
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240507-3.13.0a6+-a701af9-JIT/bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x