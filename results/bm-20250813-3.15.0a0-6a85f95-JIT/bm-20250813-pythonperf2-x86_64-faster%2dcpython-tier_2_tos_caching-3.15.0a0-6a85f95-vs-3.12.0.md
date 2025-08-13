# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                                |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 623 ms: 1.67x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.59x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 61.7 ms: 1.24x faster                                                               |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| nbody          | 88.0 ms                                                      | 86.6 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.09x faster                                                                |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                                |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.02x faster                                                               |
| regex_effbot   | 3.57 ms                                                      | 3.71 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                              |
| unpickle_pure_python | 210 us                                                       | 195 us: 1.08x faster                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 80.8 ms: 1.07x faster                                                               |
| xml_etree_process    | 58.4 ms                                                      | 55.2 ms: 1.06x faster                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 99.5 ms: 1.03x faster                                                               |
| json_dumps           | 10.2 ms                                                      | 10.3 ms: 1.00x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                                |
| json_loads           | 24.4 us                                                      | 25.9 us: 1.06x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.5 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                               |
| mako            | 10.0 ms                                                      | 9.73 ms: 1.03x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 623 ms: 1.67x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.59x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                                |
| richards                   | 45.7 ms                                                      | 33.6 ms: 1.36x faster                                                               |
| deepcopy                   | 368 us                                                       | 276 us: 1.34x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 27.6 us: 1.33x faster                                                               |
| richards_super             | 51.3 ms                                                      | 39.1 ms: 1.31x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                               |
| float                      | 76.6 ms                                                      | 61.7 ms: 1.24x faster                                                               |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                                               |
| go                         | 150 ms                                                       | 122 ms: 1.22x faster                                                                |
| spectral_norm              | 91.6 ms                                                      | 78.0 ms: 1.18x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                                               |
| deltablue                  | 3.24 ms                                                      | 2.86 ms: 1.13x faster                                                               |
| tomli_loads                | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                              |
| logging_format             | 7.48 us                                                      | 6.64 us: 1.13x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.48 sec: 1.12x faster                                                              |
| pyflate                    | 439 ms                                                       | 393 ms: 1.12x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.02 us: 1.12x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 59.4 ms: 1.10x faster                                                               |
| chaos                      | 64.0 ms                                                      | 58.5 ms: 1.09x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 739 ms: 1.09x faster                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.3 ms: 1.09x faster                                                               |
| regex_compile              | 144 ms                                                       | 133 ms: 1.09x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                               |
| unpickle_pure_python       | 210 us                                                       | 195 us: 1.08x faster                                                                |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                                |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                                |
| raytrace                   | 298 ms                                                       | 279 ms: 1.07x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 80.8 ms: 1.07x faster                                                               |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.07x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                                |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.06x faster                                                                |
| xml_etree_process          | 58.4 ms                                                      | 55.2 ms: 1.06x faster                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 76.7 ms: 1.05x faster                                                               |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 99.5 ms: 1.03x faster                                                               |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                               |
| mako                       | 10.0 ms                                                      | 9.73 ms: 1.03x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                               |
| nbody                      | 88.0 ms                                                      | 86.6 ms: 1.02x faster                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.02x faster                                                               |
| json_dumps                 | 10.2 ms                                                      | 10.3 ms: 1.00x slower                                                               |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                                |
| hexiom                     | 5.96 ms                                                      | 6.00 ms: 1.01x slower                                                               |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                               |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                                |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.04x slower                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.71 ms: 1.04x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 93.4 ms: 1.04x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.9 us: 1.06x slower                                                               |
| json                       | 5.12 ms                                                      | 5.54 ms: 1.08x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                                |
| async_generators           | 390 ms                                                       | 448 ms: 1.15x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.95 ms: 1.18x slower                                                               |
| coverage                   | 66.7 ms                                                      | 83.8 ms: 1.26x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.5 ms: 1.33x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                               |
| telco                      | 6.96 ms                                                      | 160 ms: 23.04x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (5): logging_silent, asyncio_websockets, xml_etree_parse, pycparser, scimark_fft
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250813-3.15.0a0-6a85f95-JIT/bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x