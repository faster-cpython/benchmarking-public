# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.039x faster
- HPT reliability: 99.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.61x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| regex_dna      | 239 ms                                                       | 238 ms: 1.00x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 202 us: 1.04x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                        |
| json_loads           | 24.4 us                                                      | 23.9 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.2 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.61x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                        |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                        |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.96 us: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.7 ms: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.6 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.33 us: 1.06x faster                                                        |
| raytrace                   | 298 ms                                                       | 281 ms: 1.06x faster                                                         |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 94.3 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                       |
| chaos                      | 64.0 ms                                                      | 61.3 ms: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 202 us: 1.04x faster                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.34 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 783 ms: 1.03x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                       |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.73 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 87.9 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                        |
| json_loads                 | 24.4 us                                                      | 23.9 us: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.4 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 113 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 90.4 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                         |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| regex_dna                  | 239 ms                                                       | 238 ms: 1.00x faster                                                         |
| richards_super             | 51.3 ms                                                      | 51.7 ms: 1.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.02 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| fannkuch                   | 350 ms                                                       | 354 ms: 1.01x slower                                                         |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| scimark_fft                | 301 ms                                                       | 308 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                                         |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 98.4 ns: 1.04x slower                                                        |
| pyflate                    | 439 ms                                                       | 459 ms: 1.05x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 68.5 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| async_generators           | 390 ms                                                       | 435 ms: 1.11x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.81 ms: 1.12x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.72 ms: 1.12x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| coverage                   | 66.7 ms                                                      | 77.9 ms: 1.17x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.03 sec: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.2 ms: 1.40x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.75 ms: 1.73x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.34 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.26 sec: 264.58x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (7): float, sqlglot_optimize, nbody, asyncio_websockets, richards, json, bench_thread_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.61% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x