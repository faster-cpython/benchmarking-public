# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.041x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                                |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 630 ms: 1.67x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 329 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 60.5 ms: 1.27x faster                                                               |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| nbody          | 88.0 ms                                                      | 86.4 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 134 ms: 1.08x faster                                                                |
| regex_dna      | 239 ms                                                       | 226 ms: 1.06x faster                                                                |
| regex_v8       | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                               |
| regex_effbot   | 3.57 ms                                                      | 3.69 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.92 sec: 1.12x faster                                                              |
| xml_etree_generate   | 86.1 ms                                                      | 79.5 ms: 1.08x faster                                                               |
| xml_etree_process    | 58.4 ms                                                      | 55.2 ms: 1.06x faster                                                               |
| unpickle_pure_python | 210 us                                                       | 199 us: 1.06x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 98.2 ms: 1.05x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.02x faster                                                                |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.01x faster                                                               |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.5 ms: 1.08x faster                                                               |
| mako            | 10.0 ms                                                      | 9.87 ms: 1.01x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.30 sec: 1.97x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 630 ms: 1.67x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 329 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                                |
| deepcopy                   | 368 us                                                       | 276 us: 1.34x faster                                                                |
| richards                   | 45.7 ms                                                      | 34.3 ms: 1.33x faster                                                               |
| deepcopy_memo              | 36.8 us                                                      | 27.7 us: 1.33x faster                                                               |
| richards_super             | 51.3 ms                                                      | 39.8 ms: 1.29x faster                                                               |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                                               |
| float                      | 76.6 ms                                                      | 60.5 ms: 1.27x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                               |
| go                         | 150 ms                                                       | 122 ms: 1.22x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.14x faster                                                               |
| spectral_norm              | 91.6 ms                                                      | 80.6 ms: 1.14x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                               |
| deltablue                  | 3.24 ms                                                      | 2.86 ms: 1.13x faster                                                               |
| tomli_loads                | 2.16 sec                                                     | 1.92 sec: 1.12x faster                                                              |
| logging_format             | 7.48 us                                                      | 6.70 us: 1.12x faster                                                               |
| logging_simple             | 6.71 us                                                      | 6.04 us: 1.11x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                              |
| dulwich_log                | 65.4 ms                                                      | 59.8 ms: 1.09x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 742 ms: 1.09x faster                                                                |
| chaos                      | 64.0 ms                                                      | 58.9 ms: 1.09x faster                                                               |
| xml_etree_generate         | 86.1 ms                                                      | 79.5 ms: 1.08x faster                                                               |
| regex_compile              | 144 ms                                                       | 134 ms: 1.08x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.5 ms: 1.08x faster                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.4 ms: 1.07x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.07x faster                                                               |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                                |
| pyflate                    | 439 ms                                                       | 414 ms: 1.06x faster                                                                |
| xml_etree_process          | 58.4 ms                                                      | 55.2 ms: 1.06x faster                                                               |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.06x faster                                                                |
| unpickle_pure_python       | 210 us                                                       | 199 us: 1.06x faster                                                                |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 98.2 ms: 1.05x faster                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 77.3 ms: 1.04x faster                                                               |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 95.3 ms: 1.04x faster                                                               |
| logging_silent             | 94.4 ns                                                      | 91.5 ns: 1.03x faster                                                               |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.02x faster                                                                |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                               |
| nbody                      | 88.0 ms                                                      | 86.4 ms: 1.02x faster                                                               |
| mako                       | 10.0 ms                                                      | 9.87 ms: 1.01x faster                                                               |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.01x faster                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                               |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                                |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                              |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 92.2 ms: 1.03x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 6.12 ms: 1.03x slower                                                               |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.69 ms: 1.03x slower                                                               |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                                |
| fannkuch                   | 350 ms                                                       | 367 ms: 1.05x slower                                                                |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                                |
| async_generators           | 390 ms                                                       | 442 ms: 1.13x slower                                                                |
| coverage                   | 66.7 ms                                                      | 78.9 ms: 1.18x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.09 ms: 1.21x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.87 ms: 1.80x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                               |
| telco                      | 6.96 ms                                                      | 161 ms: 23.06x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (1): scimark_fft
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250811-3.15.0a0-6041480-JIT/bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x