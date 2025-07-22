# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.034x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 623 ms: 1.67x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 633 ms: 1.66x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                                |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 61.7 ms: 1.24x faster                                                               |
| nbody          | 88.0 ms                                                      | 84.4 ms: 1.04x faster                                                               |
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                              |
| xml_etree_generate   | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                               |
| unpickle_pure_python | 210 us                                                       | 199 us: 1.05x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 97.9 ms: 1.05x faster                                                               |
| xml_etree_process    | 58.4 ms                                                      | 56.4 ms: 1.03x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.02x faster                                                                |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.72 ms: 1.01x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.31x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                               |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 623 ms: 1.67x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 633 ms: 1.66x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                                |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                                |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 28.1 us: 1.31x faster                                                               |
| richards                   | 45.7 ms                                                      | 35.4 ms: 1.29x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                               |
| float                      | 76.6 ms                                                      | 61.7 ms: 1.24x faster                                                               |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                                               |
| richards_super             | 51.3 ms                                                      | 41.6 ms: 1.23x faster                                                               |
| go                         | 150 ms                                                       | 124 ms: 1.21x faster                                                                |
| spectral_norm              | 91.6 ms                                                      | 80.9 ms: 1.13x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 58.3 ms: 1.12x faster                                                               |
| logging_format             | 7.48 us                                                      | 6.69 us: 1.12x faster                                                               |
| tomli_loads                | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.4 ms: 1.11x faster                                                               |
| deltablue                  | 3.24 ms                                                      | 2.93 ms: 1.10x faster                                                               |
| logging_simple             | 6.71 us                                                      | 6.12 us: 1.10x faster                                                               |
| django_template            | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.52 sec: 1.09x faster                                                              |
| chaos                      | 64.0 ms                                                      | 59.1 ms: 1.08x faster                                                               |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                |
| pprint_safe_repr           | 807 ms                                                       | 753 ms: 1.07x faster                                                                |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                               |
| pyflate                    | 439 ms                                                       | 417 ms: 1.05x faster                                                                |
| unpickle_pure_python       | 210 us                                                       | 199 us: 1.05x faster                                                                |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 97.9 ms: 1.05x faster                                                               |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                                |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.04x faster                                                                |
| nbody                      | 88.0 ms                                                      | 84.4 ms: 1.04x faster                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 77.2 ms: 1.04x faster                                                               |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                                |
| raytrace                   | 298 ms                                                       | 288 ms: 1.04x faster                                                                |
| xml_etree_process          | 58.4 ms                                                      | 56.4 ms: 1.03x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                               |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.02x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 96.6 ms: 1.02x faster                                                               |
| logging_silent             | 94.4 ns                                                      | 93.4 ns: 1.01x faster                                                               |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 8.72 ms: 1.01x slower                                                               |
| sympy_expand               | 484 ms                                                       | 493 ms: 1.02x slower                                                                |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                              |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 6.18 ms: 1.04x slower                                                               |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                                                |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                               |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 94.4 ms: 1.05x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                                |
| fannkuch                   | 350 ms                                                       | 372 ms: 1.06x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                               |
| async_generators           | 390 ms                                                       | 443 ms: 1.13x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.16x slower                                                                |
| coverage                   | 66.7 ms                                                      | 77.9 ms: 1.17x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.07 ms: 1.21x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.31x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.91 ms: 1.83x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                               |
| telco                      | 6.96 ms                                                      | 163 ms: 23.41x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                        |

Benchmark hidden because not significant (2): pycparser, 2to3
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.15x