# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                                |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 621 ms: 1.68x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 329 ms: 1.66x faster                                                                |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 59.7 ms: 1.28x faster                                                               |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| nbody          | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                                |
| regex_v8       | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                               |
| regex_effbot   | 3.57 ms                                                      | 3.68 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                              |
| unpickle_pure_python | 210 us                                                       | 192 us: 1.09x faster                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 79.6 ms: 1.08x faster                                                               |
| xml_etree_process    | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 99.3 ms: 1.04x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.02x faster                                                                |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.00x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 329 us: 1.04x slower                                                                |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.28 sec: 2.00x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 621 ms: 1.68x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 329 ms: 1.66x faster                                                                |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                                |
| richards                   | 45.7 ms                                                      | 33.4 ms: 1.37x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                                |
| richards_super             | 51.3 ms                                                      | 38.6 ms: 1.33x faster                                                               |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                                               |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                                |
| float                      | 76.6 ms                                                      | 59.7 ms: 1.28x faster                                                               |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                               |
| go                         | 150 ms                                                       | 122 ms: 1.23x faster                                                                |
| spectral_norm              | 91.6 ms                                                      | 79.4 ms: 1.15x faster                                                               |
| logging_format             | 7.48 us                                                      | 6.54 us: 1.14x faster                                                               |
| tomli_loads                | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                              |
| logging_simple             | 6.71 us                                                      | 5.91 us: 1.14x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 16.8 ms: 1.12x faster                                                               |
| deltablue                  | 3.24 ms                                                      | 2.88 ms: 1.12x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 3.01 us: 1.12x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.48 sec: 1.12x faster                                                              |
| dulwich_log                | 65.4 ms                                                      | 59.0 ms: 1.11x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 731 ms: 1.10x faster                                                                |
| unpickle_pure_python       | 210 us                                                       | 192 us: 1.09x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                               |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 79.6 ms: 1.08x faster                                                               |
| chaos                      | 64.0 ms                                                      | 59.2 ms: 1.08x faster                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.0 ms: 1.08x faster                                                               |
| pyflate                    | 439 ms                                                       | 408 ms: 1.07x faster                                                                |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                               |
| raytrace                   | 298 ms                                                       | 281 ms: 1.06x faster                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 75.8 ms: 1.06x faster                                                               |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                                |
| xml_etree_process          | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                                               |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                                |
| pycparser                  | 1.23 sec                                                     | 1.18 sec: 1.04x faster                                                              |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                                |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 99.3 ms: 1.04x faster                                                               |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                               |
| logging_silent             | 94.4 ns                                                      | 92.2 ns: 1.02x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                               |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.02x faster                                                                |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                                |
| nbody                      | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                               |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.00x slower                                                               |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                                |
| hexiom                     | 5.96 ms                                                      | 5.99 ms: 1.01x slower                                                               |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                               |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.68 ms: 1.03x slower                                                               |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                                |
| nqueens                    | 89.9 ms                                                      | 92.9 ms: 1.03x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 329 us: 1.04x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                               |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                                |
| async_generators           | 390 ms                                                       | 451 ms: 1.16x slower                                                                |
| coverage                   | 66.7 ms                                                      | 79.0 ms: 1.18x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.00 ms: 1.19x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.33x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.94 ms: 1.85x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.72 ms: 1.93x slower                                                               |
| telco                      | 6.96 ms                                                      | 158 ms: 22.62x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (2): mako, scimark_fft
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x