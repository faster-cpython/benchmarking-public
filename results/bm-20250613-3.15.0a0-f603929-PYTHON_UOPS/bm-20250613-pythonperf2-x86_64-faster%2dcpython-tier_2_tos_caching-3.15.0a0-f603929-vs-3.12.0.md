# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.144x slower
- HPT reliability: 99.70%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 331 ms: 1.16x slower                                                                |
| docutils       | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                              |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 683 ms: 1.54x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 679 ms: 1.54x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 364 ms: 1.50x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 361 ms: 1.50x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 296 ms: 1.46x faster                                                                |
| async_tree_none            | 452 ms                                                       | 315 ms: 1.43x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 535 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 540 ms: 1.29x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.44x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 260 ms: 1.02x faster                                                                |
| float          | 76.6 ms                                                      | 112 ms: 1.46x slower                                                                |
| nbody          | 88.0 ms                                                      | 216 ms: 2.46x slower                                                                |
| Geometric mean | (ref)                                                        | 1.52x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 222 ms: 1.08x faster                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.75 ms: 1.05x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                               |
| regex_compile  | 144 ms                                                       | 164 ms: 1.14x slower                                                                |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                                |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                               |
| xml_etree_generate   | 86.1 ms                                                      | 115 ms: 1.34x slower                                                                |
| pickle_pure_python   | 318 us                                                       | 432 us: 1.36x slower                                                                |
| xml_etree_process    | 58.4 ms                                                      | 80.7 ms: 1.38x slower                                                               |
| tomli_loads          | 2.16 sec                                                     | 3.34 sec: 1.55x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 425 us: 2.03x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.28x slower                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                               |
| mako            | 10.0 ms                                                      | 19.9 ms: 1.99x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.36x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.51 sec: 1.70x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 683 ms: 1.54x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 679 ms: 1.54x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 364 ms: 1.50x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 361 ms: 1.50x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 296 ms: 1.46x faster                                                                |
| async_tree_none            | 452 ms                                                       | 315 ms: 1.43x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 27.3 us: 1.35x faster                                                               |
| generators                 | 37.4 ms                                                      | 27.9 ms: 1.34x faster                                                               |
| deepcopy                   | 368 us                                                       | 278 us: 1.33x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 535 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 540 ms: 1.29x faster                                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 17.5 ms: 1.08x faster                                                               |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.08x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                               |
| logging_format             | 7.48 us                                                      | 7.04 us: 1.06x faster                                                               |
| scimark_lu                 | 98.8 ms                                                      | 93.3 ms: 1.06x faster                                                               |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.42 us: 1.05x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 63.6 ms: 1.03x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                               |
| pidigits                   | 265 ms                                                       | 260 ms: 1.02x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                                |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                                |
| chaos                      | 64.0 ms                                                      | 65.3 ms: 1.02x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                               |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                               |
| json                       | 5.12 ms                                                      | 5.38 ms: 1.05x slower                                                               |
| regex_effbot               | 3.57 ms                                                      | 3.75 ms: 1.05x slower                                                               |
| sympy_str                  | 302 ms                                                       | 321 ms: 1.06x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                               |
| sqlite_synth               | 2.77 us                                                      | 3.07 us: 1.11x slower                                                               |
| docutils                   | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                              |
| raytrace                   | 298 ms                                                       | 339 ms: 1.14x slower                                                                |
| regex_compile              | 144 ms                                                       | 164 ms: 1.14x slower                                                                |
| 2to3                       | 285 ms                                                       | 331 ms: 1.16x slower                                                                |
| sympy_expand               | 484 ms                                                       | 562 ms: 1.16x slower                                                                |
| coverage                   | 66.7 ms                                                      | 77.5 ms: 1.16x slower                                                               |
| async_generators           | 390 ms                                                       | 462 ms: 1.18x slower                                                                |
| nqueens                    | 89.9 ms                                                      | 110 ms: 1.22x slower                                                                |
| pycparser                  | 1.23 sec                                                     | 1.55 sec: 1.25x slower                                                              |
| richards_super             | 51.3 ms                                                      | 64.5 ms: 1.26x slower                                                               |
| richards                   | 45.7 ms                                                      | 57.9 ms: 1.27x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                               |
| xml_etree_generate         | 86.1 ms                                                      | 115 ms: 1.34x slower                                                                |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.36x slower                                                                |
| pickle_pure_python         | 318 us                                                       | 432 us: 1.36x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 80.7 ms: 1.38x slower                                                               |
| telco                      | 6.96 ms                                                      | 9.67 ms: 1.39x slower                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 97.8 ms: 1.42x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 215 us: 1.42x slower                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 117 ms: 1.45x slower                                                                |
| float                      | 76.6 ms                                                      | 112 ms: 1.46x slower                                                                |
| comprehensions             | 21.9 us                                                      | 33.2 us: 1.51x slower                                                               |
| tomli_loads                | 2.16 sec                                                     | 3.34 sec: 1.55x slower                                                              |
| pyflate                    | 439 ms                                                       | 691 ms: 1.58x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 2.67 sec: 1.61x slower                                                              |
| pprint_safe_repr           | 807 ms                                                       | 1.31 sec: 1.63x slower                                                              |
| go                         | 150 ms                                                       | 249 ms: 1.66x slower                                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                               |
| scimark_fft                | 301 ms                                                       | 538 ms: 1.79x slower                                                                |
| gc_traversal               | 3.48 ms                                                      | 6.38 ms: 1.84x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 11.7 ms: 1.96x slower                                                               |
| mako                       | 10.0 ms                                                      | 19.9 ms: 1.99x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 6.51 ms: 2.01x slower                                                               |
| unpickle_pure_python       | 210 us                                                       | 425 us: 2.03x slower                                                                |
| fannkuch                   | 350 ms                                                       | 725 ms: 2.07x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 9.65 ms: 2.29x slower                                                               |
| spectral_norm              | 91.6 ms                                                      | 214 ms: 2.34x slower                                                                |
| nbody                      | 88.0 ms                                                      | 216 ms: 2.46x slower                                                                |
| logging_silent             | 94.4 ns                                                      | 501 ns: 5.30x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.19x slower                                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, sympy_integrate
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250613-3.15.0a0-f603929-PYTHON_UOPS/bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x slower

# HPT report

- Reliability score: 99.70% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.11x