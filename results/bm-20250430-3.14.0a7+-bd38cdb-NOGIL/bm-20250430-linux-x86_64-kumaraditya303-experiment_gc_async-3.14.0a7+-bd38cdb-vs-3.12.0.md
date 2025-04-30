# Results vs. 3.12.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.033x faster
- HPT reliability: 71.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 291 ms: 1.06x slower                                                          |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 512 ms: 2.31x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 548 ms: 2.11x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 225 ms: 2.00x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 296 ms: 1.94x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 456 ms: 1.59x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.85x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                         |
| pidigits       | 187 ms                                                 | 181 ms: 1.04x faster                                                          |
| nbody          | 97.0 ms                                                | 129 ms: 1.33x slower                                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                         |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                         |
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                          |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 96.4 ms: 1.11x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                          |
| tomli_loads          | 2.33 sec                                               | 2.24 sec: 1.04x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 238 us: 1.03x slower                                                          |
| pickle_pure_python   | 324 us                                                 | 345 us: 1.07x slower                                                          |
| xml_etree_generate   | 89.2 ms                                                | 96.1 ms: 1.08x slower                                                         |
| xml_etree_process    | 61.7 ms                                                | 68.1 ms: 1.10x slower                                                         |
| json_loads           | 28.5 us                                                | 32.7 us: 1.15x slower                                                         |
| json_dumps           | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.06 ms: 1.31x slower                                                         |
| python_startup         | 9.55 ms                                                | 15.4 ms: 1.61x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 38.9 ms: 1.12x slower                                                         |
| mako            | 11.9 ms                                                | 16.2 ms: 1.36x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 512 ms: 2.31x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 548 ms: 2.11x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 225 ms: 2.00x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 296 ms: 1.94x faster                                                          |
| mdp                        | 2.63 sec                                               | 1.40 sec: 1.88x faster                                                        |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| gc_traversal               | 3.79 ms                                                | 2.14 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 456 ms: 1.59x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                          |
| deepcopy                   | 371 us                                                 | 294 us: 1.26x faster                                                          |
| float                      | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 36.0 us: 1.13x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 96.4 ms: 1.11x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 62.8 ms: 1.09x faster                                                         |
| comprehensions             | 21.8 us                                                | 20.0 us: 1.09x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.8 ms: 1.09x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.09 us: 1.08x faster                                                         |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                        |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                         |
| async_generators           | 463 ms                                                 | 442 ms: 1.05x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 2.24 sec: 1.04x faster                                                        |
| pidigits                   | 187 ms                                                 | 181 ms: 1.04x faster                                                          |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                          |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                                          |
| generators                 | 31.2 ms                                                | 30.6 ms: 1.02x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.65 ms: 1.02x faster                                                         |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                          |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                        |
| chaos                      | 67.0 ms                                                | 67.3 ms: 1.00x slower                                                         |
| raytrace                   | 312 ms                                                 | 316 ms: 1.01x slower                                                          |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                          |
| pyflate                    | 482 ms                                                 | 489 ms: 1.01x slower                                                          |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                                          |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.02x slower                                                          |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                          |
| logging_simple             | 6.46 us                                                | 6.66 us: 1.03x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 22.1 ms: 1.03x slower                                                         |
| scimark_fft                | 382 ms                                                 | 395 ms: 1.03x slower                                                          |
| unpickle_pure_python       | 230 us                                                 | 238 us: 1.03x slower                                                          |
| pprint_safe_repr           | 776 ms                                                 | 803 ms: 1.04x slower                                                          |
| logging_format             | 7.23 us                                                | 7.51 us: 1.04x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                        |
| 2to3                       | 274 ms                                                 | 291 ms: 1.06x slower                                                          |
| pickle_pure_python         | 324 us                                                 | 345 us: 1.07x slower                                                          |
| json                       | 5.26 ms                                                | 5.64 ms: 1.07x slower                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 158 ms: 1.07x slower                                                          |
| sympy_expand               | 478 ms                                                 | 515 ms: 1.08x slower                                                          |
| xml_etree_generate         | 89.2 ms                                                | 96.1 ms: 1.08x slower                                                         |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                         |
| crypto_pyaes               | 81.9 ms                                                | 89.3 ms: 1.09x slower                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 82.0 ms: 1.09x slower                                                         |
| richards                   | 45.8 ms                                                | 50.2 ms: 1.09x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.5 ms: 1.10x slower                                                         |
| xml_etree_process          | 61.7 ms                                                | 68.1 ms: 1.10x slower                                                         |
| nqueens                    | 83.3 ms                                                | 91.9 ms: 1.10x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.65 ms: 1.12x slower                                                         |
| hexiom                     | 6.41 ms                                                | 7.21 ms: 1.12x slower                                                         |
| django_template            | 34.6 ms                                                | 38.9 ms: 1.12x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.14x slower                                                          |
| json_loads                 | 28.5 us                                                | 32.7 us: 1.15x slower                                                         |
| meteor_contest             | 112 ms                                                 | 129 ms: 1.15x slower                                                          |
| richards_super             | 51.5 ms                                                | 59.3 ms: 1.15x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.89 ms: 1.17x slower                                                         |
| fannkuch                   | 417 ms                                                 | 502 ms: 1.20x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                         |
| telco                      | 7.10 ms                                                | 9.00 ms: 1.27x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 202 us: 1.28x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 9.06 ms: 1.31x slower                                                         |
| nbody                      | 97.0 ms                                                | 129 ms: 1.33x slower                                                          |
| mako                       | 11.9 ms                                                | 16.2 ms: 1.36x slower                                                         |
| python_startup             | 9.55 ms                                                | 15.4 ms: 1.61x slower                                                         |
| coverage                   | 72.7 ms                                                | 124 ms: 1.70x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 90.6 ms: 3.77x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 3.24 ms: 3.85x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-bd38cdb-NOGIL/bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 71.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.33x