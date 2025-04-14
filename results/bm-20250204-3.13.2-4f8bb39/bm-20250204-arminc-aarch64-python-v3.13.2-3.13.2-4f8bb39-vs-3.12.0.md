# Results vs. 3.12.0

- fork: python
- ref: v3.13.2
- machine: linux-aarch64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.009x slower
- HPT reliability: 53.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 9.11 ms: 1.03x slower                                    |
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                   |
| tornado_http   | 136 ms                                                                | 126 ms: 1.07x faster                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                   |
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.15 sec: 1.22x faster                                   |
| async_tree_none_tg         | 577 ms                                                                | 474 ms: 1.22x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 784 ms: 1.16x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 674 ms: 1.15x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 658 ms: 1.13x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 816 ms: 1.08x faster                                     |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                     |
| float          | 92.1 ms                                                               | 97.4 ms: 1.06x slower                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 269 ms: 1.06x slower                                     |
| regex_v8       | 28.3 ms                                                               | 31.7 ms: 1.12x slower                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| tomli_loads    | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                   |
| json_loads     | 30.7 us                                                               | 32.1 us: 1.05x slower                                    |
| json_dumps     | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                             |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, pickle_pure_python, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                    |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.0 ms: 1.04x slower                                    |
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                    |
| genshi_text    | 27.4 ms                                                               | 29.8 ms: 1.09x slower                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                   |
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.15 sec: 1.22x faster                                   |
| async_tree_none_tg         | 577 ms                                                                | 474 ms: 1.22x faster                                     |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 784 ms: 1.16x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 674 ms: 1.15x faster                                     |
| raytrace                   | 353 ms                                                                | 308 ms: 1.15x faster                                     |
| generators                 | 43.5 ms                                                               | 38.0 ms: 1.14x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 658 ms: 1.13x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 816 ms: 1.08x faster                                     |
| tornado_http               | 136 ms                                                                | 126 ms: 1.07x faster                                     |
| async_generators           | 491 ms                                                                | 464 ms: 1.06x faster                                     |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.05x faster                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                    |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.05x faster                                     |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                    |
| pathlib                    | 24.5 ms                                                               | 23.6 ms: 1.04x faster                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 152 ms: 1.03x faster                                     |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                   |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                   |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                     |
| tomli_loads                | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                   |
| chameleon                  | 8.81 ms                                                               | 9.11 ms: 1.03x slower                                    |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                     |
| genshi_xml                 | 60.6 ms                                                               | 63.0 ms: 1.04x slower                                    |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.05x slower                                    |
| go                         | 157 ms                                                                | 164 ms: 1.05x slower                                     |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.05x slower                                    |
| sympy_expand               | 454 ms                                                                | 475 ms: 1.05x slower                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 64.3 ms: 1.05x slower                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                    |
| regex_dna                  | 254 ms                                                                | 269 ms: 1.06x slower                                     |
| float                      | 92.1 ms                                                               | 97.4 ms: 1.06x slower                                    |
| deepcopy_memo              | 49.6 us                                                               | 52.6 us: 1.06x slower                                    |
| pycparser                  | 1.26 sec                                                              | 1.33 sec: 1.06x slower                                   |
| sqlglot_normalize          | 126 ms                                                                | 134 ms: 1.06x slower                                     |
| pprint_safe_repr           | 916 ms                                                                | 977 ms: 1.07x slower                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.38 us: 1.07x slower                                    |
| hexiom                     | 6.98 ms                                                               | 7.45 ms: 1.07x slower                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                   |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                     |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                     |
| thrift                     | 937 us                                                                | 1.01 ms: 1.07x slower                                    |
| richards_super             | 58.5 ms                                                               | 62.8 ms: 1.07x slower                                    |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                     |
| deepcopy                   | 446 us                                                                | 479 us: 1.08x slower                                     |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                    |
| pyflate                    | 559 ms                                                                | 604 ms: 1.08x slower                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.72 ms: 1.08x slower                                    |
| richards                   | 50.9 ms                                                               | 55.4 ms: 1.09x slower                                    |
| genshi_text                | 27.4 ms                                                               | 29.8 ms: 1.09x slower                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 93.6 ms: 1.10x slower                                    |
| scimark_fft                | 418 ms                                                                | 461 ms: 1.10x slower                                     |
| scimark_sor                | 150 ms                                                                | 165 ms: 1.10x slower                                     |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                     |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                     |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                    |
| sqlite_synth               | 3.77 us                                                               | 4.20 us: 1.11x slower                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.90 ms: 1.12x slower                                    |
| regex_v8                   | 28.3 ms                                                               | 31.7 ms: 1.12x slower                                    |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                     |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                     |
| telco                      | 8.51 ms                                                               | 10.8 ms: 1.27x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 5.92 ms: 1.35x slower                                    |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.59 ms: 1.87x slower                                    |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                             |

Benchmark hidden because not significant (24): regex_effbot, regex_compile, chaos, logging_format, sqlglot_transpile, scimark_lu, bench_thread_pool, sqlglot_parse, xml_etree_parse, logging_simple, xml_etree_iterparse, crypto_pyaes, unpickle_pure_python, html5lib, coroutines, sympy_integrate, 2to3, pylint, gunicorn, django_template, pickle_pure_python, xml_etree_process, xml_etree_generate, nqueens
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39.json: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 53.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x