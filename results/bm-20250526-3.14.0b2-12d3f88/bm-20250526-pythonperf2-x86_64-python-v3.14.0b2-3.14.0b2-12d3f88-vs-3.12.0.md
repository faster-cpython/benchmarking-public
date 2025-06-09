# Results vs. 3.12.0

- fork: python
- ref: v3.14.0b2
- machine: linux-x86_64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.052x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                             |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                           |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.67x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 650 ms: 1.62x faster                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                             |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 506 ms: 1.38x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                             |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.0 ms: 1.11x faster                                            |
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                             |
| nbody          | 88.0 ms                                                      | 94.6 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                             |
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                            |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                             |
| regex_v8       | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                             |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                           |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                             |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                            |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                             |
| json_loads           | 24.4 us                                                      | 27.1 us: 1.11x slower                                            |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                            |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.79 ms: 1.02x slower                                            |
| python_startup         | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                            |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                            |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.31 sec: 1.96x faster                                           |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.67x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 650 ms: 1.62x faster                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                             |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 506 ms: 1.38x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                             |
| deepcopy                   | 368 us                                                       | 278 us: 1.32x faster                                             |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                            |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.30x faster                                            |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.26x faster                                            |
| go                         | 150 ms                                                       | 123 ms: 1.21x faster                                             |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                            |
| float                      | 76.6 ms                                                      | 69.0 ms: 1.11x faster                                            |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.4 ms: 1.11x faster                                            |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                             |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                            |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                             |
| chaos                      | 64.0 ms                                                      | 60.1 ms: 1.06x faster                                            |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                            |
| django_template            | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                            |
| sqlalchemy_declarative     | 159 ms                                                       | 151 ms: 1.06x faster                                             |
| dulwich_log                | 65.4 ms                                                      | 61.9 ms: 1.06x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.06x faster                                           |
| raytrace                   | 298 ms                                                       | 285 ms: 1.04x faster                                             |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                             |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                             |
| pprint_safe_repr           | 807 ms                                                       | 775 ms: 1.04x faster                                             |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                           |
| deltablue                  | 3.24 ms                                                      | 3.12 ms: 1.04x faster                                            |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                             |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                            |
| pidigits                   | 265 ms                                                       | 257 ms: 1.03x faster                                             |
| pyflate                    | 439 ms                                                       | 426 ms: 1.03x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 78.3 ms: 1.03x faster                                            |
| scimark_lu                 | 98.8 ms                                                      | 96.7 ms: 1.02x faster                                            |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                            |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                            |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.02x faster                                            |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                             |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                             |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                             |
| logging_format             | 7.48 us                                                      | 7.41 us: 1.01x faster                                            |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                             |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                             |
| spectral_norm              | 91.6 ms                                                      | 92.7 ms: 1.01x slower                                            |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                           |
| sqlalchemy_imperative      | 18.7 ms                                                      | 19.0 ms: 1.01x slower                                            |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 8.79 ms: 1.02x slower                                            |
| scimark_fft                | 301 ms                                                       | 308 ms: 1.02x slower                                             |
| nqueens                    | 89.9 ms                                                      | 92.0 ms: 1.02x slower                                            |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.02x slower                                             |
| regex_v8                   | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                            |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                             |
| sqlite_synth               | 2.77 us                                                      | 2.91 us: 1.05x slower                                            |
| fannkuch                   | 350 ms                                                       | 369 ms: 1.06x slower                                             |
| nbody                      | 88.0 ms                                                      | 94.6 ms: 1.08x slower                                            |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                            |
| json                       | 5.12 ms                                                      | 5.57 ms: 1.09x slower                                            |
| async_generators           | 390 ms                                                       | 433 ms: 1.11x slower                                             |
| json_loads                 | 24.4 us                                                      | 27.1 us: 1.11x slower                                            |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.70 ms: 1.12x slower                                            |
| telco                      | 6.96 ms                                                      | 7.84 ms: 1.13x slower                                            |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.17x slower                                             |
| coverage                   | 66.7 ms                                                      | 85.6 ms: 1.28x slower                                            |
| python_startup             | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.81 ms: 1.76x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 6.21 ms: 1.79x slower                                            |
| logging_silent             | 94.4 ns                                                      | 518 ns: 5.49x slower                                             |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (4): pycparser, richards_super, xml_etree_generate, hexiom
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x