# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: 2b1c0da
- commit date: 2025-03-14
- overall geometric mean: 1.453x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.78x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils  | 2.77 sec                                               | 5.32 sec: 1.92x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                       |
| async_tree_io              | 1.16 sec                                               | 1.20 sec: 1.04x slower                                                       |
| async_tree_none            | 472 ms                                                 | 519 ms: 1.10x slower                                                         |
| async_tree_none_tg         | 450 ms                                                 | 495 ms: 1.10x slower                                                         |
| async_tree_memoization     | 578 ms                                                 | 647 ms: 1.12x slower                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 645 ms: 1.12x slower                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 960 ms: 1.32x slower                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 989 ms: 1.36x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.15x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 139 ms: 1.64x slower                                                         |
| nbody          | 97.0 ms                                                | 193 ms: 1.99x slower                                                         |
| pidigits       | 187 ms                                                 | 378 ms: 2.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.87x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 6.44 ms: 1.78x slower                                                        |
| regex_compile  | 148 ms                                                 | 265 ms: 1.79x slower                                                         |
| regex_dna      | 212 ms                                                 | 436 ms: 2.06x slower                                                         |
| regex_v8       | 23.1 ms                                                | 48.8 ms: 2.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.93x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 279 ms: 1.75x slower                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 188 ms: 1.76x slower                                                         |
| tomli_loads          | 2.33 sec                                               | 4.20 sec: 1.80x slower                                                       |
| unpickle_pure_python | 230 us                                                 | 430 us: 1.87x slower                                                         |
| xml_etree_process    | 61.7 ms                                                | 116 ms: 1.88x slower                                                         |
| xml_etree_generate   | 89.2 ms                                                | 168 ms: 1.88x slower                                                         |
| pickle_pure_python   | 324 us                                                 | 649 us: 2.00x slower                                                         |
| json_loads           | 28.5 us                                                | 60.1 us: 2.11x slower                                                        |
| json_dumps           | 10.4 ms                                                | 23.2 ms: 2.23x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.92x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 31.2 ms: 3.26x slower                                                        |
| python_startup_no_site | 6.94 ms                                                | 31.0 ms: 4.47x slower                                                        |
| Geometric mean         | (ref)                                                  | 3.82x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 64.4 ms: 1.86x slower                                                        |
| mako            | 11.9 ms                                                | 23.4 ms: 1.96x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.91x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                       |
| async_tree_io              | 1.16 sec                                               | 1.20 sec: 1.04x slower                                                       |
| async_tree_none            | 472 ms                                                 | 519 ms: 1.10x slower                                                         |
| async_tree_none_tg         | 450 ms                                                 | 495 ms: 1.10x slower                                                         |
| async_tree_memoization     | 578 ms                                                 | 647 ms: 1.12x slower                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 645 ms: 1.12x slower                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 960 ms: 1.32x slower                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 989 ms: 1.36x slower                                                         |
| deepcopy                   | 371 us                                                 | 524 us: 1.41x slower                                                         |
| deepcopy_memo              | 40.7 us                                                | 58.9 us: 1.45x slower                                                        |
| comprehensions             | 21.8 us                                                | 34.1 us: 1.57x slower                                                        |
| deepcopy_reduce            | 3.35 us                                                | 5.34 us: 1.60x slower                                                        |
| float                      | 84.7 ms                                                | 139 ms: 1.64x slower                                                         |
| logging_format             | 7.23 us                                                | 12.2 us: 1.69x slower                                                        |
| logging_simple             | 6.46 us                                                | 11.0 us: 1.71x slower                                                        |
| async_generators           | 463 ms                                                 | 791 ms: 1.71x slower                                                         |
| dulwich_log                | 68.5 ms                                                | 118 ms: 1.73x slower                                                         |
| go                         | 139 ms                                                 | 242 ms: 1.74x slower                                                         |
| pathlib                    | 19.3 ms                                                | 33.8 ms: 1.75x slower                                                        |
| xml_etree_parse            | 159 ms                                                 | 279 ms: 1.75x slower                                                         |
| spectral_norm              | 115 ms                                                 | 202 ms: 1.76x slower                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 188 ms: 1.76x slower                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 133 ms: 1.78x slower                                                         |
| chaos                      | 67.0 ms                                                | 119 ms: 1.78x slower                                                         |
| regex_effbot               | 3.61 ms                                                | 6.44 ms: 1.78x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 301 ms: 1.78x slower                                                         |
| regex_compile              | 148 ms                                                 | 265 ms: 1.79x slower                                                         |
| scimark_fft                | 382 ms                                                 | 686 ms: 1.80x slower                                                         |
| raytrace                   | 312 ms                                                 | 562 ms: 1.80x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 33.6 ms: 1.80x slower                                                        |
| tomli_loads                | 2.33 sec                                               | 4.20 sec: 1.80x slower                                                       |
| scimark_sor                | 129 ms                                                 | 233 ms: 1.80x slower                                                         |
| sympy_str                  | 300 ms                                                 | 542 ms: 1.81x slower                                                         |
| pyflate                    | 482 ms                                                 | 875 ms: 1.81x slower                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 268 ms: 1.83x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 9.29 ms: 1.84x slower                                                        |
| generators                 | 31.2 ms                                                | 57.8 ms: 1.85x slower                                                        |
| crypto_pyaes               | 81.9 ms                                                | 152 ms: 1.86x slower                                                         |
| django_template            | 34.6 ms                                                | 64.4 ms: 1.86x slower                                                        |
| unpickle_pure_python       | 230 us                                                 | 430 us: 1.87x slower                                                         |
| xml_etree_process          | 61.7 ms                                                | 116 ms: 1.88x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 40.3 ms: 1.88x slower                                                        |
| logging_silent             | 104 ns                                                 | 197 ns: 1.88x slower                                                         |
| xml_etree_generate         | 89.2 ms                                                | 168 ms: 1.88x slower                                                         |
| meteor_contest             | 112 ms                                                 | 212 ms: 1.89x slower                                                         |
| pprint_safe_repr           | 776 ms                                                 | 1.47 sec: 1.90x slower                                                       |
| sympy_expand               | 478 ms                                                 | 916 ms: 1.92x slower                                                         |
| hexiom                     | 6.41 ms                                                | 12.3 ms: 1.92x slower                                                        |
| docutils                   | 2.77 sec                                               | 5.32 sec: 1.92x slower                                                       |
| mdp                        | 2.63 sec                                               | 5.06 sec: 1.92x slower                                                       |
| pprint_pformat             | 1.57 sec                                               | 3.01 sec: 1.92x slower                                                       |
| richards                   | 45.8 ms                                                | 88.7 ms: 1.93x slower                                                        |
| pycparser                  | 1.18 sec                                               | 2.28 sec: 1.94x slower                                                       |
| richards_super             | 51.5 ms                                                | 100 ms: 1.94x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 231 ms: 1.96x slower                                                         |
| sqlite_synth               | 2.83 us                                                | 5.55 us: 1.96x slower                                                        |
| mako                       | 11.9 ms                                                | 23.4 ms: 1.96x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 1.08 sec: 1.97x slower                                                       |
| fannkuch                   | 417 ms                                                 | 831 ms: 1.99x slower                                                         |
| nbody                      | 97.0 ms                                                | 193 ms: 1.99x slower                                                         |
| deltablue                  | 3.72 ms                                                | 7.42 ms: 2.00x slower                                                        |
| json                       | 5.26 ms                                                | 10.5 ms: 2.00x slower                                                        |
| pickle_pure_python         | 324 us                                                 | 649 us: 2.00x slower                                                         |
| pidigits                   | 187 ms                                                 | 378 ms: 2.02x slower                                                         |
| nqueens                    | 83.3 ms                                                | 169 ms: 2.03x slower                                                         |
| regex_dna                  | 212 ms                                                 | 436 ms: 2.06x slower                                                         |
| coroutines                 | 23.2 ms                                                | 47.8 ms: 2.06x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 327 us: 2.07x slower                                                         |
| json_loads                 | 28.5 us                                                | 60.1 us: 2.11x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 48.8 ms: 2.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 23.2 ms: 2.23x slower                                                        |
| telco                      | 7.10 ms                                                | 16.2 ms: 2.28x slower                                                        |
| coverage                   | 72.7 ms                                                | 172 ms: 2.36x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 9.25 ms: 2.44x slower                                                        |
| python_startup             | 9.55 ms                                                | 31.2 ms: 3.26x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 5.10 ms: 3.46x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 31.0 ms: 4.47x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 136 ms: 5.65x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 30.2 ms: 35.93x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.93x slower                                                                 |
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250314-3.14.0a5+-2b1c0da-JIT/bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.453x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.80x
- 95% likely to have a slowdown of 1.79x
- 99% likely to have a slowdown of 1.78x

# Memory
- memory change: 1.12x