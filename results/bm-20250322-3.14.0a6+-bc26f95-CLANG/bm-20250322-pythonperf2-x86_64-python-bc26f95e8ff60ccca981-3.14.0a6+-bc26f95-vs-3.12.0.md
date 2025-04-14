# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 277 ms: 1.03x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.86 sec: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 311 ms: 1.74x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 615 ms: 1.71x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 259 ms: 1.66x faster                                                         |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.62x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.60x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.1 ms: 1.13x faster                                                        |
| nbody          | 88.0 ms                                                      | 86.6 ms: 1.02x faster                                                        |
| pidigits       | 265 ms                                                       | 291 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.05 ms: 1.17x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_dna      | 239 ms                                                       | 225 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict        | 32.5 us                                                      | 29.5 us: 1.10x faster                                                        |
| xml_etree_generate | 86.1 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| unpickle           | 14.8 us                                                      | 13.7 us: 1.08x faster                                                        |
| xml_etree_process  | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                        |
| tomli_loads        | 2.16 sec                                                     | 2.07 sec: 1.05x faster                                                       |
| unpickle_list      | 4.66 us                                                      | 4.48 us: 1.04x faster                                                        |
| pickle_list        | 4.43 us                                                      | 4.30 us: 1.03x faster                                                        |
| pickle_pure_python | 318 us                                                       | 316 us: 1.01x faster                                                         |
| json_loads         | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| xml_etree_parse    | 144 ms                                                       | 161 ms: 1.12x slower                                                         |
| json_dumps         | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| pickle             | 10.5 us                                                      | 12.0 us: 1.14x slower                                                        |
| Geometric mean     | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.2 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 33.6 ms: 1.13x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 311 ms: 1.74x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 615 ms: 1.71x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 259 ms: 1.66x faster                                                         |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.62x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                         |
| deepcopy                   | 368 us                                                       | 268 us: 1.37x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 27.3 us: 1.35x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.3 us: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.74 us: 1.23x faster                                                        |
| go                         | 150 ms                                                       | 124 ms: 1.21x faster                                                         |
| scimark_sor                | 109 ms                                                       | 92.9 ms: 1.17x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.05 ms: 1.17x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 81.1 ns: 1.16x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 78.9 ms: 1.16x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 19.8 ms: 1.16x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 60.3 ms: 1.14x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.14x faster                                                        |
| raytrace                   | 298 ms                                                       | 262 ms: 1.14x faster                                                         |
| django_template            | 38.2 ms                                                      | 33.6 ms: 1.13x faster                                                        |
| float                      | 76.6 ms                                                      | 68.1 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 88.2 ms: 1.12x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.76 us: 1.11x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 29.5 us: 1.10x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 21.8 ms: 1.10x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.12 us: 1.10x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.5 ms: 1.09x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 60.0 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| unpickle                   | 14.8 us                                                      | 13.7 us: 1.08x faster                                                        |
| pyflate                    | 439 ms                                                       | 409 ms: 1.07x faster                                                         |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.5 ms: 1.07x faster                                                        |
| scimark_fft                | 301 ms                                                       | 282 ms: 1.07x faster                                                         |
| sympy_str                  | 302 ms                                                       | 284 ms: 1.06x faster                                                         |
| regex_dna                  | 239 ms                                                       | 225 ms: 1.06x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.05x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.8 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.04 ms: 1.04x faster                                                        |
| unpickle_list              | 4.66 us                                                      | 4.48 us: 1.04x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 782 ms: 1.03x faster                                                         |
| richards_super             | 51.3 ms                                                      | 49.9 ms: 1.03x faster                                                        |
| 2to3                       | 285 ms                                                       | 277 ms: 1.03x faster                                                         |
| pickle_list                | 4.43 us                                                      | 4.30 us: 1.03x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.0 ms: 1.02x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.17 ms: 1.02x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.85 ms: 1.02x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.6 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.86 sec: 1.00x faster                                                       |
| sympy_expand               | 484 ms                                                       | 487 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 81.3 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                       |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.03x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.39 ms: 1.06x slower                                                        |
| coverage                   | 66.7 ms                                                      | 71.8 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 164 us: 1.08x slower                                                         |
| fannkuch                   | 350 ms                                                       | 381 ms: 1.09x slower                                                         |
| async_generators           | 390 ms                                                       | 425 ms: 1.09x slower                                                         |
| pidigits                   | 265 ms                                                       | 291 ms: 1.10x slower                                                         |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 161 ms: 1.12x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.0 us: 1.14x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 61.4 ns: 1.15x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.2 ms: 1.40x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.85 ms: 1.68x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.10 sec: 230.21x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): bench_thread_pool, pycparser, xml_etree_iterparse, unpickle_pure_python, json, regex_v8
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x