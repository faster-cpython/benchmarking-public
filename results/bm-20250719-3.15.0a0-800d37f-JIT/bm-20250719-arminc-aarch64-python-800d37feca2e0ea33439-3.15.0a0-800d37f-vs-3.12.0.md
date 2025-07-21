# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.012x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 312 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 477 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 880 ms: 1.60x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 653 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 657 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.0 ms: 1.12x faster                                                   |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 130 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                   |
| regex_dna      | 254 ms                                                                | 220 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 78.2 ms: 1.01x faster                                                   |
| pickle_dict         | 37.3 us                                                               | 38.7 us: 1.04x slower                                                   |
| unpickle_list       | 6.17 us                                                               | 6.42 us: 1.04x slower                                                   |
| json_loads          | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.80 us: 1.10x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 410 us: 1.12x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                   |
| pickle              | 13.4 us                                                               | 15.3 us: 1.14x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.56 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                   |
| mako           | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                   |
| genshi_xml     | 60.6 ms                                                               | 64.0 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.71 sec: 2.00x faster                                                  |
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 477 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 880 ms: 1.60x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 653 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 657 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.8 us: 1.28x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                   |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.15x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.3 us: 1.14x faster                                                   |
| spectral_norm              | 131 ms                                                                | 116 ms: 1.13x faster                                                    |
| float                      | 92.1 ms                                                               | 82.0 ms: 1.12x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| richards                   | 50.9 ms                                                               | 45.5 ms: 1.12x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 55.6 ms: 1.12x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.68 us: 1.11x faster                                                   |
| richards_super             | 58.5 ms                                                               | 53.2 ms: 1.10x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                    |
| pylint                     | 355 ms                                                                | 326 ms: 1.09x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.5 ms: 1.07x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.18 us: 1.06x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 534 ms: 1.06x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.87 us: 1.06x faster                                                   |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                    |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.9 ms: 1.04x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| scimark_fft                | 418 ms                                                                | 408 ms: 1.03x faster                                                    |
| go                         | 157 ms                                                                | 154 ms: 1.02x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 78.2 ms: 1.01x faster                                                   |
| pyflate                    | 559 ms                                                                | 555 ms: 1.01x faster                                                    |
| mako                       | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| 2to3                       | 308 ms                                                                | 312 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.56 ms: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 38.7 us: 1.04x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 461 ms: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.42 us: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 976 us: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.80 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 64.0 ms: 1.06x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.08x slower                                                  |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| sympy_expand               | 454 ms                                                                | 489 ms: 1.08x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.58 ms: 1.09x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 94.7 ms: 1.09x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.80 us: 1.10x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 410 us: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.02 ms: 1.13x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.3 us: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                    |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.28 sec: 1.21x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.23x slower                                                  |
| nbody                      | 105 ms                                                                | 130 ms: 1.24x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.87 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.96x slower                                                   |
| telco                      | 8.51 ms                                                               | 166 ms: 19.47x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.68 sec: 380.19x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (13): async_generators, sympy_integrate, unpickle_pure_python, sqlite_synth, scimark_monte_carlo, sympy_str, html5lib, sympy_sum, meteor_contest, unpickle, django_template, nqueens, coroutines
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x