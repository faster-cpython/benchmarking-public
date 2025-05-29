# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 290 ms: 1.06x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.96 sec: 1.01x faster                                                   |
| html5lib       | 65.1 ms                                                               | 59.3 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 382 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 362 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 899 ms: 1.56x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 707 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.13x slower                                                     |
| pidigits       | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                     |
| regex_dna      | 254 ms                                                                | 239 ms: 1.06x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                   |
| xml_etree_generate | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| unpickle           | 18.5 us                                                               | 17.3 us: 1.07x faster                                                    |
| unpickle_list      | 6.17 us                                                               | 5.77 us: 1.07x faster                                                    |
| xml_etree_process  | 79.0 ms                                                               | 74.7 ms: 1.06x faster                                                    |
| pickle_dict        | 37.3 us                                                               | 35.5 us: 1.05x faster                                                    |
| pickle_list        | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| pickle_pure_python | 365 us                                                                | 374 us: 1.03x slower                                                     |
| xml_etree_parse    | 195 ms                                                                | 204 ms: 1.05x slower                                                     |
| json_loads         | 30.7 us                                                               | 33.2 us: 1.08x slower                                                    |
| pickle             | 13.4 us                                                               | 15.6 us: 1.16x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| genshi_text     | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 58.6 ms: 1.03x faster                                                    |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 382 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 362 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 899 ms: 1.56x faster                                                     |
| deepcopy                   | 446 us                                                                | 310 us: 1.44x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.5 us: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 707 ms: 1.25x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.34 us: 1.23x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 50.6 ms: 1.23x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                                    |
| async_generators           | 491 ms                                                                | 416 ms: 1.18x faster                                                     |
| pylint                     | 355 ms                                                                | 301 ms: 1.18x faster                                                     |
| go                         | 157 ms                                                                | 135 ms: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                    |
| raytrace                   | 353 ms                                                                | 311 ms: 1.13x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                    |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                     |
| spectral_norm              | 131 ms                                                                | 117 ms: 1.12x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.50 us: 1.11x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.89 us: 1.11x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 77.2 ms: 1.10x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 59.3 ms: 1.10x faster                                                    |
| logging_silent             | 127 ns                                                                | 116 ns: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.09x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| float                      | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                    |
| unpickle                   | 18.5 us                                                               | 17.3 us: 1.07x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.77 us: 1.07x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.19 sec: 1.07x faster                                                   |
| 2to3                       | 308 ms                                                                | 290 ms: 1.06x faster                                                     |
| regex_dna                  | 254 ms                                                                | 239 ms: 1.06x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                    |
| django_template            | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| scimark_fft                | 418 ms                                                                | 395 ms: 1.06x faster                                                     |
| xml_etree_process          | 79.0 ms                                                               | 74.7 ms: 1.06x faster                                                    |
| pyflate                    | 559 ms                                                                | 530 ms: 1.05x faster                                                     |
| pickle_dict                | 37.3 us                                                               | 35.5 us: 1.05x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.94 ms: 1.05x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                     |
| richards_super             | 58.5 ms                                                               | 56.0 ms: 1.04x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 58.6 ms: 1.03x faster                                                    |
| thrift                     | 937 us                                                                | 910 us: 1.03x faster                                                     |
| richards                   | 50.9 ms                                                               | 49.5 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.29 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.96 sec: 1.01x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 88.3 ms: 1.02x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 374 us: 1.03x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.24 ms: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                     |
| xml_etree_parse            | 195 ms                                                                | 204 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 190 us: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                    |
| coverage                   | 87.3 ms                                                               | 95.7 ms: 1.10x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.43 ms: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                     |
| nbody                      | 105 ms                                                                | 119 ms: 1.13x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.16x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.51 ms: 1.48x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 3.25 sec: 460.38x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (13): scimark_sor, sympy_str, chaos, coroutines, asyncio_tcp, pprint_safe_repr, xml_etree_iterparse, pycparser, unpickle_pure_python, nqueens, sympy_expand, asyncio_websockets, scimark_sparse_mat_mult
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x