# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.012x faster
- HPT reliability: 87.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 310 ms: 1.01x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.17 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                     |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 880 ms: 1.60x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 371 ms: 1.55x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 919 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.3 ms: 1.08x faster                                                    |
| nbody          | 105 ms                                                                | 129 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 28.1 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| unpickle             | 18.5 us                                                               | 17.4 us: 1.06x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                   |
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 78.5 ms: 1.01x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.55 us: 1.06x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.65 us: 1.08x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 288 us: 1.11x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.0 us: 1.11x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 406 us: 1.11x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.15x slower                                                    |
| pickle               | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 40.1 ms: 1.01x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                                    |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                     |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 880 ms: 1.60x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 371 ms: 1.55x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 919 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                    |
| deepcopy                   | 446 us                                                                | 349 us: 1.28x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.5 ms: 1.16x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.92 us: 1.10x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.60 us: 1.10x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                    |
| pylint                     | 355 ms                                                                | 325 ms: 1.09x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 57.1 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                     |
| float                      | 92.1 ms                                                               | 85.3 ms: 1.08x faster                                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.83 us: 1.07x faster                                                    |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| unpickle                   | 18.5 us                                                               | 17.4 us: 1.06x faster                                                    |
| richards_super             | 58.5 ms                                                               | 55.3 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 151 ms: 1.04x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 4.01 ms: 1.03x faster                                                    |
| async_generators           | 491 ms                                                                | 478 ms: 1.03x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                     |
| django_template            | 40.7 ms                                                               | 40.1 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 28.1 ms: 1.01x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 78.5 ms: 1.01x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.9 ms: 1.00x faster                                                    |
| thrift                     | 937 us                                                                | 941 us: 1.00x slower                                                     |
| 2to3                       | 308 ms                                                                | 310 ms: 1.01x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                    |
| spectral_norm              | 131 ms                                                                | 134 ms: 1.02x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.6 ms: 1.03x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                                    |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.55 us: 1.06x slower                                                    |
| pyflate                    | 559 ms                                                                | 594 ms: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.17 sec: 1.06x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.65 us: 1.08x slower                                                    |
| sympy_expand               | 454 ms                                                                | 498 ms: 1.10x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 288 us: 1.11x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.0 us: 1.11x slower                                                    |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 406 us: 1.11x slower                                                     |
| coverage                   | 87.3 ms                                                               | 98.2 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.98 ms: 1.13x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 112 ms: 1.13x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.43 sec: 1.14x slower                                                   |
| go                         | 157 ms                                                                | 180 ms: 1.14x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.88 ms: 1.16x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 102 ms: 1.18x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.57 ms: 1.23x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 222 us: 1.23x slower                                                     |
| nbody                      | 105 ms                                                                | 129 ms: 1.24x slower                                                     |
| fannkuch                   | 443 ms                                                                | 551 ms: 1.24x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.58 ms: 1.50x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 814 ms: 115.39x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (14): html5lib, asyncio_tcp, scimark_sor, sqlite_synth, scimark_lu, sympy_sum, sqlalchemy_imperative, richards, chaos, genshi_text, sympy_str, sympy_integrate, pidigits, comprehensions
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 87.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x