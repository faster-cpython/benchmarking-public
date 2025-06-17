# Results vs. 3.12.0

- fork: python
- ref: 3.14
- machine: linux-aarch64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                     |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                     |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                     |
| async_tree_none            | 624 ms                                                                | 391 ms: 1.59x faster                                     |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                     |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.0 ms: 1.08x faster                                    |
| pidigits       | 233 ms                                                                | 241 ms: 1.03x slower                                     |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                    |
| regex_dna      | 254 ms                                                                | 220 ms: 1.16x faster                                     |
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                     |
| regex_v8       | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.07x faster                                     |
| tomli_loads         | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                   |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                     |
| xml_etree_process   | 79.0 ms                                                               | 81.7 ms: 1.04x slower                                    |
| pickle_pure_python  | 365 us                                                                | 396 us: 1.08x slower                                     |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                    |
| json_loads          | 30.7 us                                                               | 35.7 us: 1.16x slower                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                             |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                    |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 59.7 ms: 1.02x faster                                    |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                   |
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                     |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                     |
| async_tree_none            | 624 ms                                                                | 391 ms: 1.59x faster                                     |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                     |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                    |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                    |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                     |
| comprehensions             | 25.4 us                                                               | 21.1 us: 1.20x faster                                    |
| regex_effbot               | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                    |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.16x faster                                     |
| dulwich_log                | 62.0 ms                                                               | 54.2 ms: 1.14x faster                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                    |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                     |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                     |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.10x faster                                    |
| async_generators           | 491 ms                                                                | 447 ms: 1.10x faster                                     |
| float                      | 92.1 ms                                                               | 85.0 ms: 1.08x faster                                    |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.9 ms: 1.08x faster                                    |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.07x faster                                     |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.06x faster                                    |
| pyflate                    | 559 ms                                                                | 529 ms: 1.06x faster                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                     |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                   |
| regex_v8                   | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                    |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                     |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                     |
| crypto_pyaes               | 86.6 ms                                                               | 83.2 ms: 1.04x faster                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.1 ms: 1.03x faster                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.02x faster                                   |
| meteor_contest             | 112 ms                                                                | 110 ms: 1.02x faster                                     |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                     |
| genshi_xml                 | 60.6 ms                                                               | 59.7 ms: 1.02x faster                                    |
| pprint_safe_repr           | 916 ms                                                                | 903 ms: 1.01x faster                                     |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                   |
| richards                   | 50.9 ms                                                               | 50.4 ms: 1.01x faster                                    |
| logging_simple             | 7.63 us                                                               | 7.69 us: 1.01x slower                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                     |
| logging_format             | 8.34 us                                                               | 8.49 us: 1.02x slower                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                    |
| pidigits                   | 233 ms                                                                | 241 ms: 1.03x slower                                     |
| xml_etree_process          | 79.0 ms                                                               | 81.7 ms: 1.04x slower                                    |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                     |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                     |
| coroutines                 | 29.0 ms                                                               | 30.8 ms: 1.06x slower                                    |
| fannkuch                   | 443 ms                                                                | 475 ms: 1.07x slower                                     |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.08x slower                                     |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                     |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                    |
| json                       | 5.54 ms                                                               | 6.12 ms: 1.11x slower                                    |
| telco                      | 8.51 ms                                                               | 9.43 ms: 1.11x slower                                    |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.93 ms: 1.12x slower                                    |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                     |
| json_loads                 | 30.7 us                                                               | 35.7 us: 1.16x slower                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                     |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 6.89 ms: 1.57x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                    |
| logging_silent             | 127 ns                                                                | 613 ns: 4.83x slower                                     |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                             |

Benchmark hidden because not significant (15): html5lib, chaos, spectral_norm, scimark_sor, django_template, sympy_sum, genshi_text, pycparser, richards_super, nqueens, hexiom, xml_etree_generate, sqlite_synth, sympy_expand, unpickle_pure_python
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.10x