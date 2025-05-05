# Results vs. 3.12.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.022x faster
- HPT reliability: 81.48%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 291 ms: 1.06x slower                                                          |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 519 ms: 2.28x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 552 ms: 2.09x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 227 ms: 1.98x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 296 ms: 1.94x faster                                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.74x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 463 ms: 1.57x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 503 ms: 1.44x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.83x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                         |
| pidigits       | 187 ms                                                 | 182 ms: 1.03x faster                                                          |
| nbody          | 97.0 ms                                                | 128 ms: 1.32x slower                                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                         |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                          |
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                          |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.8 ms: 1.11x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                                          |
| tomli_loads          | 2.33 sec                                               | 2.23 sec: 1.04x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 241 us: 1.05x slower                                                          |
| pickle_pure_python   | 324 us                                                 | 343 us: 1.06x slower                                                          |
| xml_etree_generate   | 89.2 ms                                                | 96.6 ms: 1.08x slower                                                         |
| xml_etree_process    | 61.7 ms                                                | 68.0 ms: 1.10x slower                                                         |
| json_loads           | 28.5 us                                                | 32.9 us: 1.16x slower                                                         |
| json_dumps           | 10.4 ms                                                | 13.1 ms: 1.27x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.11 ms: 1.31x slower                                                         |
| python_startup         | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 39.7 ms: 1.15x slower                                                         |
| mako            | 11.9 ms                                                | 16.3 ms: 1.37x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 519 ms: 2.28x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 552 ms: 2.09x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 227 ms: 1.98x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 296 ms: 1.94x faster                                                          |
| mdp                        | 2.63 sec                                               | 1.40 sec: 1.87x faster                                                        |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.74x faster                                                          |
| gc_traversal               | 3.79 ms                                                | 2.28 ms: 1.66x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 463 ms: 1.57x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 503 ms: 1.44x faster                                                          |
| deepcopy                   | 371 us                                                 | 297 us: 1.25x faster                                                          |
| float                      | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 36.4 us: 1.12x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 95.8 ms: 1.11x faster                                                         |
| comprehensions             | 21.8 us                                                | 19.7 us: 1.10x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 62.7 ms: 1.09x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.8 ms: 1.09x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.08 us: 1.09x faster                                                         |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                                          |
| go                         | 139 ms                                                 | 132 ms: 1.05x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 2.23 sec: 1.04x faster                                                        |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                          |
| pidigits                   | 187 ms                                                 | 182 ms: 1.03x faster                                                          |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                          |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                        |
| pyflate                    | 482 ms                                                 | 480 ms: 1.00x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                        |
| chaos                      | 67.0 ms                                                | 67.7 ms: 1.01x slower                                                         |
| deltablue                  | 3.72 ms                                                | 3.76 ms: 1.01x slower                                                         |
| generators                 | 31.2 ms                                                | 31.7 ms: 1.01x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                          |
| sympy_str                  | 300 ms                                                 | 308 ms: 1.03x slower                                                          |
| logging_simple             | 6.46 us                                                | 6.64 us: 1.03x slower                                                         |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                          |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                          |
| raytrace                   | 312 ms                                                 | 323 ms: 1.04x slower                                                          |
| sympy_integrate            | 21.4 ms                                                | 22.2 ms: 1.04x slower                                                         |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.04x slower                                                          |
| logging_format             | 7.23 us                                                | 7.51 us: 1.04x slower                                                         |
| unpickle_pure_python       | 230 us                                                 | 241 us: 1.05x slower                                                          |
| pickle_pure_python         | 324 us                                                 | 343 us: 1.06x slower                                                          |
| pprint_safe_repr           | 776 ms                                                 | 822 ms: 1.06x slower                                                          |
| 2to3                       | 274 ms                                                 | 291 ms: 1.06x slower                                                          |
| scimark_fft                | 382 ms                                                 | 406 ms: 1.06x slower                                                          |
| json                       | 5.26 ms                                                | 5.64 ms: 1.07x slower                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 158 ms: 1.08x slower                                                          |
| xml_etree_generate         | 89.2 ms                                                | 96.6 ms: 1.08x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.70 sec: 1.08x slower                                                        |
| sympy_expand               | 478 ms                                                 | 525 ms: 1.10x slower                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 82.6 ms: 1.10x slower                                                         |
| crypto_pyaes               | 81.9 ms                                                | 90.1 ms: 1.10x slower                                                         |
| nqueens                    | 83.3 ms                                                | 91.7 ms: 1.10x slower                                                         |
| xml_etree_process          | 61.7 ms                                                | 68.0 ms: 1.10x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.8 ms: 1.11x slower                                                         |
| coroutines                 | 23.2 ms                                                | 25.8 ms: 1.11x slower                                                         |
| richards                   | 45.8 ms                                                | 51.6 ms: 1.12x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.67 ms: 1.13x slower                                                         |
| hexiom                     | 6.41 ms                                                | 7.31 ms: 1.14x slower                                                         |
| django_template            | 34.6 ms                                                | 39.7 ms: 1.15x slower                                                         |
| meteor_contest             | 112 ms                                                 | 130 ms: 1.15x slower                                                          |
| json_loads                 | 28.5 us                                                | 32.9 us: 1.16x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 137 ms: 1.16x slower                                                          |
| richards_super             | 51.5 ms                                                | 60.1 ms: 1.17x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.94 ms: 1.18x slower                                                         |
| fannkuch                   | 417 ms                                                 | 498 ms: 1.19x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 13.1 ms: 1.27x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 201 us: 1.27x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 9.11 ms: 1.31x slower                                                         |
| nbody                      | 97.0 ms                                                | 128 ms: 1.32x slower                                                          |
| telco                      | 7.10 ms                                                | 9.35 ms: 1.32x slower                                                         |
| mako                       | 11.9 ms                                                | 16.3 ms: 1.37x slower                                                         |
| python_startup             | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                         |
| coverage                   | 72.7 ms                                                | 125 ms: 1.71x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 90.7 ms: 3.78x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 3.26 ms: 3.87x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): sqlite_synth, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250503-3.14.0a7+-a8a0e1d-NOGIL/bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 81.48% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.33x