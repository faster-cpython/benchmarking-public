# Results vs. 3.12.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                          |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 384 ms: 1.50x faster                                                          |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 804 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 832 ms: 1.42x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 324 ms: 1.39x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 580 ms: 1.25x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                         |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                          |
| nbody          | 97.0 ms                                                | 99.2 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.11 ms: 1.16x faster                                                         |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                         |
| regex_dna      | 212 ms                                                 | 207 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                          |
| json_loads           | 28.5 us                                                | 30.5 us: 1.07x slower                                                         |
| json_dumps           | 10.4 ms                                                | 12.2 ms: 1.18x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                         |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                         |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 384 ms: 1.50x faster                                                          |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 804 ms: 1.44x faster                                                          |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 832 ms: 1.42x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 324 ms: 1.39x faster                                                          |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 580 ms: 1.25x faster                                                          |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                         |
| float                      | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                         |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.11 ms: 1.16x faster                                                         |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                          |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.13x faster                                                         |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                          |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.12x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.11x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                                         |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                         |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 76.3 ms: 1.07x faster                                                         |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                                          |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                          |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                         |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                          |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                        |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                         |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                         |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.03x faster                                                          |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                                         |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                          |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                         |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.03x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                         |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                         |
| fannkuch                   | 417 ms                                                 | 421 ms: 1.01x slower                                                          |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                          |
| nbody                      | 97.0 ms                                                | 99.2 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.19 ms: 1.03x slower                                                         |
| json                       | 5.26 ms                                                | 5.49 ms: 1.04x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 893 us: 1.06x slower                                                          |
| json_loads                 | 28.5 us                                                | 30.5 us: 1.07x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                          |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                         |
| coroutines                 | 23.2 ms                                                | 26.3 ms: 1.14x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 12.2 ms: 1.18x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                         |
| coverage                   | 72.7 ms                                                | 91.5 ms: 1.26x slower                                                         |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (4): nqueens, pycparser, asyncio_websockets, sqlite_synth
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-bd38cdb/bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x