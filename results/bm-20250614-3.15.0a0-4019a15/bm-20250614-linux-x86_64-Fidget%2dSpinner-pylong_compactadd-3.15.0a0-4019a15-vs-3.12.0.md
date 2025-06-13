# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-x86_64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.096x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                         |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                         |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                        |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                        |
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                         |
| regex_dna      | 212 ms                                                 | 183 ms: 1.16x faster                                                         |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                         |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                        |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                        |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                        |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                         |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                        |
| comprehensions             | 21.8 us                                                | 15.9 us: 1.37x faster                                                        |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                        |
| float                      | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                        |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                       |
| regex_dna                  | 212 ms                                                 | 183 ms: 1.16x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                                        |
| raytrace                   | 312 ms                                                 | 273 ms: 1.15x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                        |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                        |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                        |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.11x faster                                                         |
| async_generators           | 463 ms                                                 | 418 ms: 1.11x faster                                                         |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                         |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                                        |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.03 ms: 1.06x faster                                                        |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.50 ms: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                         |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.06x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                       |
| logging_simple             | 6.46 us                                                | 6.13 us: 1.05x faster                                                        |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                        |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.05x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                        |
| logging_format             | 7.23 us                                                | 6.94 us: 1.04x faster                                                        |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                         |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                        |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                         |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                         |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.02 ms: 1.01x faster                                                        |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                        |
| pprint_safe_repr           | 776 ms                                                 | 813 ms: 1.05x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                        |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.13x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.90 ms: 1.29x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                        |
| logging_silent             | 104 ns                                                 | 473 ns: 4.53x slower                                                         |
| coverage                   | 72.7 ms                                                | 423 ms: 5.81x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (3): json, asyncio_websockets, nbody
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.096x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x