# Results vs. 3.12.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                          |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 383 ms: 1.51x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                          |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 804 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 824 ms: 1.43x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                         |
| nbody          | 97.0 ms                                                | 96.3 ms: 1.01x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                         |
| regex_dna      | 212 ms                                                 | 207 ms: 1.03x faster                                                          |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.8 ms: 1.07x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                          |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                         |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 383 ms: 1.51x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                          |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 804 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 824 ms: 1.43x faster                                                          |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                          |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                         |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                         |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                         |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                          |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                         |
| logging_format             | 7.23 us                                                | 6.26 us: 1.15x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                          |
| pyflate                    | 482 ms                                                 | 426 ms: 1.13x faster                                                          |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                         |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                         |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                         |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                         |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                          |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.8 ms: 1.07x faster                                                         |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                         |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                          |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                                          |
| logging_silent             | 104 ns                                                 | 99.4 ns: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                         |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.04x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                         |
| richards                   | 45.8 ms                                                | 44.4 ms: 1.03x faster                                                         |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                         |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.03x faster                                                          |
| richards_super             | 51.5 ms                                                | 50.5 ms: 1.02x faster                                                         |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                          |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.02x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                          |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                         |
| nbody                      | 97.0 ms                                                | 96.3 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                          |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.14 ms: 1.02x slower                                                         |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.05x slower                                                          |
| coroutines                 | 23.2 ms                                                | 25.8 ms: 1.11x slower                                                         |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                         |
| coverage                   | 72.7 ms                                                | 94.5 ms: 1.30x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.01 ms: 1.32x slower                                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.51 ms: 1.70x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250503-3.14.0a7+-a8a0e1d/bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x