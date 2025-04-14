# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.047x faster
- HPT reliability: 99.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                            |
| html5lib       | 65.1 ms                                                               | 64.1 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 652 ms: 1.40x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                             |
| nbody          | 105 ms                                                                | 128 ms: 1.22x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                             |
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                              |
| regex_dna      | 254 ms                                                                | 250 ms: 1.02x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 28.1 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 175 ms: 1.11x faster                                                              |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                            |
| xml_etree_process   | 79.0 ms                                                               | 79.9 ms: 1.01x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 386 us: 1.06x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                             |
| json_loads          | 30.7 us                                                               | 34.9 us: 1.14x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                             |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 60.2 ms: 1.01x faster                                                             |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 652 ms: 1.40x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                              |
| deepcopy                   | 446 us                                                                | 334 us: 1.33x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 39.1 us: 1.27x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 51.5 ms: 1.20x faster                                                             |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                             |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                              |
| go                         | 157 ms                                                                | 139 ms: 1.13x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 175 ms: 1.11x faster                                                              |
| raytrace                   | 353 ms                                                                | 320 ms: 1.10x faster                                                              |
| async_generators           | 491 ms                                                                | 449 ms: 1.09x faster                                                              |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                             |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                              |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                             |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                                              |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                             |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                                              |
| logging_format             | 8.34 us                                                               | 7.82 us: 1.07x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                              |
| float                      | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                            |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.05x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                             |
| chaos                      | 71.4 ms                                                               | 69.1 ms: 1.03x faster                                                             |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                            |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                              |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.02x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 64.1 ms: 1.01x faster                                                             |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                            |
| regex_v8                   | 28.3 ms                                                               | 28.1 ms: 1.01x faster                                                             |
| genshi_xml                 | 60.6 ms                                                               | 60.2 ms: 1.01x faster                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                             |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                              |
| xml_etree_process          | 79.0 ms                                                               | 79.9 ms: 1.01x slower                                                             |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                              |
| scimark_fft                | 418 ms                                                                | 427 ms: 1.02x slower                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                             |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                              |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                              |
| nqueens                    | 99.2 ms                                                               | 102 ms: 1.03x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.03x slower                                                            |
| pyflate                    | 559 ms                                                                | 577 ms: 1.03x slower                                                              |
| pprint_safe_repr           | 916 ms                                                                | 950 ms: 1.04x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.48 ms: 1.05x slower                                                             |
| json                       | 5.54 ms                                                               | 5.83 ms: 1.05x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 386 us: 1.06x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 7.41 ms: 1.06x slower                                                             |
| richards                   | 50.9 ms                                                               | 54.4 ms: 1.07x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| coverage                   | 87.3 ms                                                               | 97.3 ms: 1.11x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.60 ms: 1.13x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                             |
| fannkuch                   | 443 ms                                                                | 503 ms: 1.14x slower                                                              |
| json_loads                 | 30.7 us                                                               | 34.9 us: 1.14x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                             |
| nbody                      | 105 ms                                                                | 128 ms: 1.22x slower                                                              |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.63 ms: 1.51x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.57 ms: 1.86x slower                                                             |
| bench_mp_pool              | 7.05 ms                                                               | 4.51 sec: 639.39x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                                      |

Benchmark hidden because not significant (14): deltablue, sympy_integrate, genshi_text, xml_etree_generate, asyncio_websockets, pycparser, scimark_sor, coroutines, crypto_pyaes, thrift, pidigits, richards_super, django_template, unpickle_pure_python
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.43% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x