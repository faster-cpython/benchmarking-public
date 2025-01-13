# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.013x slower
- HPT reliability: 70.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 9.22 ms: 1.05x slower                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                             |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                   |
| async_tree_none            | 624 ms                                                                | 504 ms: 1.24x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                   |
| async_tree_none_tg         | 577 ms                                                                | 484 ms: 1.19x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 789 ms: 1.16x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 663 ms: 1.12x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 801 ms: 1.10x faster                                     |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 92.1 ms                                                               | 95.8 ms: 1.04x slower                                    |
| nbody          | 105 ms                                                                | 118 ms: 1.13x slower                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 263 ms: 1.03x slower                                     |
| regex_effbot   | 4.64 ms                                                               | 5.10 ms: 1.10x slower                                    |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                   |
| xml_etree_parse     | 195 ms                                                                | 203 ms: 1.04x slower                                     |
| xml_etree_process   | 79.0 ms                                                               | 82.1 ms: 1.04x slower                                    |
| xml_etree_iterparse | 150 ms                                                                | 159 ms: 1.06x slower                                     |
| json_loads          | 30.7 us                                                               | 32.8 us: 1.07x slower                                    |
| json_dumps          | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                    |
| Geometric mean      | (ref)                                                                 | 1.05x slower                                             |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                    |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                    |
| genshi_xml      | 60.6 ms                                                               | 61.6 ms: 1.02x slower                                    |
| genshi_text     | 27.4 ms                                                               | 28.6 ms: 1.04x slower                                    |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                    |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                   |
| async_tree_none            | 624 ms                                                                | 504 ms: 1.24x faster                                     |
| comprehensions             | 25.4 us                                                               | 20.8 us: 1.22x faster                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                   |
| async_tree_none_tg         | 577 ms                                                                | 484 ms: 1.19x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 789 ms: 1.16x faster                                     |
| raytrace                   | 353 ms                                                                | 310 ms: 1.14x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 663 ms: 1.12x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 801 ms: 1.10x faster                                     |
| generators                 | 43.5 ms                                                               | 40.3 ms: 1.08x faster                                    |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                     |
| logging_simple             | 7.63 us                                                               | 7.25 us: 1.05x faster                                    |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                    |
| genshi_xml                 | 60.6 ms                                                               | 61.6 ms: 1.02x slower                                    |
| async_generators           | 491 ms                                                                | 500 ms: 1.02x slower                                     |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.03x slower                                     |
| tomli_loads                | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                   |
| gunicorn                   | 1.14 ms                                                               | 1.17 ms: 1.03x slower                                    |
| regex_dna                  | 254 ms                                                                | 263 ms: 1.03x slower                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.24 us: 1.04x slower                                    |
| xml_etree_parse            | 195 ms                                                                | 203 ms: 1.04x slower                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.1 ms: 1.04x slower                                    |
| richards_super             | 58.5 ms                                                               | 60.8 ms: 1.04x slower                                    |
| float                      | 92.1 ms                                                               | 95.8 ms: 1.04x slower                                    |
| pyflate                    | 559 ms                                                                | 582 ms: 1.04x slower                                     |
| sqlglot_normalize          | 126 ms                                                                | 131 ms: 1.04x slower                                     |
| genshi_text                | 27.4 ms                                                               | 28.6 ms: 1.04x slower                                    |
| sympy_expand               | 454 ms                                                                | 472 ms: 1.04x slower                                     |
| go                         | 157 ms                                                                | 164 ms: 1.04x slower                                     |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                     |
| chameleon                  | 8.81 ms                                                               | 9.22 ms: 1.05x slower                                    |
| pprint_safe_repr           | 916 ms                                                                | 962 ms: 1.05x slower                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                    |
| hexiom                     | 6.98 ms                                                               | 7.34 ms: 1.05x slower                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                   |
| xml_etree_iterparse        | 150 ms                                                                | 159 ms: 1.06x slower                                     |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                     |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 65.2 ms: 1.06x slower                                    |
| deepcopy_memo              | 49.6 us                                                               | 53.0 us: 1.07x slower                                    |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                    |
| richards                   | 50.9 ms                                                               | 54.5 ms: 1.07x slower                                    |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                   |
| json                       | 5.54 ms                                                               | 5.94 ms: 1.07x slower                                    |
| deepcopy                   | 446 us                                                                | 479 us: 1.07x slower                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.66 ms: 1.07x slower                                    |
| fannkuch                   | 443 ms                                                                | 478 ms: 1.08x slower                                     |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                    |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                     |
| scimark_sor                | 150 ms                                                                | 164 ms: 1.10x slower                                     |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.10x slower                                     |
| regex_effbot               | 4.64 ms                                                               | 5.10 ms: 1.10x slower                                    |
| scimark_fft                | 418 ms                                                                | 463 ms: 1.11x slower                                     |
| nbody                      | 105 ms                                                                | 118 ms: 1.13x slower                                     |
| bench_mp_pool              | 7.05 ms                                                               | 8.07 ms: 1.14x slower                                    |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                    |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                    |
| coverage                   | 87.3 ms                                                               | 106 ms: 1.21x slower                                     |
| telco                      | 8.51 ms                                                               | 10.5 ms: 1.23x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 5.92 ms: 1.35x slower                                    |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.39 ms: 1.77x slower                                    |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                             |

Benchmark hidden because not significant (26): deltablue, sqlalchemy_imperative, logging_format, tornado_http, regex_compile, pylint, sqlalchemy_declarative, sympy_sum, sqlglot_parse, crypto_pyaes, chaos, pathlib, sympy_integrate, docutils, scimark_lu, sqlglot_transpile, html5lib, mdp, coroutines, 2to3, unpickle_pure_python, bench_thread_pool, pickle_pure_python, pidigits, scimark_monte_carlo, xml_etree_generate
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 70.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x