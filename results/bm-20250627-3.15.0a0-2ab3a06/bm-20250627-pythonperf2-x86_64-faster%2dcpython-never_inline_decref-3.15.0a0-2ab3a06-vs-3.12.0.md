# Results vs. 3.12.0

- fork: faster-cpython
- ref: never_inline_decref
- machine: linux-x86_64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.055x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                                 |
| docutils       | 2.87 sec                                                     | 2.86 sec: 1.00x faster                                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                                 |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 636 ms: 1.64x faster                                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                                 |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                                 |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 508 ms: 1.37x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 514 ms: 1.36x faster                                                                 |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.4 ms: 1.09x faster                                                                |
| pidigits       | 265 ms                                                       | 258 ms: 1.03x faster                                                                 |
| nbody          | 88.0 ms                                                      | 94.5 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                 |
| regex_dna      | 239 ms                                                       | 225 ms: 1.06x faster                                                                 |
| regex_v8       | 23.6 ms                                                      | 24.2 ms: 1.02x slower                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.75 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                               |
| xml_etree_generate   | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                                 |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                                |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                                 |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                                 |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                                |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                                |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                                                |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 2.00x faster                                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                                 |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 636 ms: 1.64x faster                                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                                 |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                                 |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 508 ms: 1.37x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 514 ms: 1.36x faster                                                                 |
| deepcopy                   | 368 us                                                       | 276 us: 1.34x faster                                                                 |
| comprehensions             | 21.9 us                                                      | 16.4 us: 1.34x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 28.5 us: 1.29x faster                                                                |
| generators                 | 37.4 ms                                                      | 29.7 ms: 1.26x faster                                                                |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                                 |
| logging_format             | 7.48 us                                                      | 6.58 us: 1.14x faster                                                                |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                                |
| logging_simple             | 6.71 us                                                      | 5.98 us: 1.12x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.4 ms: 1.09x faster                                                                |
| float                      | 76.6 ms                                                      | 70.4 ms: 1.09x faster                                                                |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                 |
| dulwich_log                | 65.4 ms                                                      | 60.5 ms: 1.08x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                                |
| chaos                      | 64.0 ms                                                      | 59.7 ms: 1.07x faster                                                                |
| spectral_norm              | 91.6 ms                                                      | 85.7 ms: 1.07x faster                                                                |
| raytrace                   | 298 ms                                                       | 280 ms: 1.07x faster                                                                 |
| django_template            | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                                                |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                               |
| regex_dna                  | 239 ms                                                       | 225 ms: 1.06x faster                                                                 |
| pyflate                    | 439 ms                                                       | 415 ms: 1.06x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 76.0 ms: 1.06x faster                                                                |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                               |
| pidigits                   | 265 ms                                                       | 258 ms: 1.03x faster                                                                 |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 793 ms: 1.02x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                                |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                               |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                                 |
| logging_silent             | 94.4 ns                                                      | 93.3 ns: 1.01x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                                 |
| deltablue                  | 3.24 ms                                                      | 3.20 ms: 1.01x faster                                                                |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                                |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                                 |
| hexiom                     | 5.96 ms                                                      | 5.93 ms: 1.00x faster                                                                |
| docutils                   | 2.87 sec                                                     | 2.86 sec: 1.00x faster                                                               |
| nqueens                    | 89.9 ms                                                      | 90.8 ms: 1.01x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                                |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 24.2 ms: 1.02x slower                                                                |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.03x slower                                                                 |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                                 |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                                |
| sqlite_synth               | 2.77 us                                                      | 2.91 us: 1.05x slower                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.75 ms: 1.05x slower                                                                |
| json                       | 5.12 ms                                                      | 5.40 ms: 1.05x slower                                                                |
| fannkuch                   | 350 ms                                                       | 370 ms: 1.06x slower                                                                 |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                |
| nbody                      | 88.0 ms                                                      | 94.5 ms: 1.07x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 164 us: 1.08x slower                                                                 |
| async_generators           | 390 ms                                                       | 427 ms: 1.09x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.93 ms: 1.17x slower                                                                |
| telco                      | 6.96 ms                                                      | 8.28 ms: 1.19x slower                                                                |
| coverage                   | 66.7 ms                                                      | 87.9 ms: 1.32x slower                                                                |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                                |
| gc_traversal               | 3.48 ms                                                      | 6.73 ms: 1.93x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                         |

Benchmark hidden because not significant (3): richards, scimark_lu, richards_super
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x