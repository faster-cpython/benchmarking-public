# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.042x faster
- HPT reliability: 99.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 306 ms: 1.01x faster                                                     |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| html5lib       | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 479 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 886 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                     |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 919 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.37x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 81.4 ms: 1.13x faster                                                    |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                     |
| nbody          | 105 ms                                                                | 122 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                     |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 27.8 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 173 ms: 1.13x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.40 sec: 1.08x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| unpickle            | 18.5 us                                                               | 17.8 us: 1.04x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 108 ms: 1.04x faster                                                     |
| xml_etree_process   | 79.0 ms                                                               | 77.6 ms: 1.02x faster                                                    |
| unpickle_list       | 6.17 us                                                               | 6.36 us: 1.03x slower                                                    |
| pickle_dict         | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 397 us: 1.09x slower                                                     |
| pickle_list         | 5.25 us                                                               | 5.85 us: 1.11x slower                                                    |
| json_loads          | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| pickle              | 13.4 us                                                               | 15.4 us: 1.15x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                    |
| genshi_xml     | 60.6 ms                                                               | 60.9 ms: 1.01x slower                                                    |
| mako           | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.63 sec: 2.09x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 479 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 886 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                     |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 919 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.37x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 36.3 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                     |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                     |
| generators                 | 43.5 ms                                                               | 35.5 ms: 1.23x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                                    |
| float                      | 92.1 ms                                                               | 81.4 ms: 1.13x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 54.9 ms: 1.13x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 173 ms: 1.13x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.69 us: 1.11x faster                                                    |
| pylint                     | 355 ms                                                                | 320 ms: 1.11x faster                                                     |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                                    |
| richards_super             | 58.5 ms                                                               | 53.5 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.70 us: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.81 ms: 1.08x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.40 sec: 1.08x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                    |
| richards                   | 50.9 ms                                                               | 48.1 ms: 1.06x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.3 us: 1.04x faster                                                    |
| async_generators           | 491 ms                                                                | 471 ms: 1.04x faster                                                     |
| unpickle                   | 18.5 us                                                               | 17.8 us: 1.04x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 545 ms: 1.04x faster                                                     |
| spectral_norm              | 131 ms                                                                | 126 ms: 1.04x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.2 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| sympy_str                  | 280 ms                                                                | 272 ms: 1.03x faster                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.68 us: 1.02x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 77.6 ms: 1.02x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.8 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.8 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                   |
| 2to3                       | 308 ms                                                                | 306 ms: 1.01x faster                                                     |
| genshi_xml                 | 60.6 ms                                                               | 60.9 ms: 1.01x slower                                                    |
| pyflate                    | 559 ms                                                                | 567 ms: 1.01x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                    |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.36 us: 1.03x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.49 ms: 1.05x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.93 ms: 1.07x slower                                                    |
| sympy_expand               | 454 ms                                                                | 486 ms: 1.07x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.08x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                     |
| go                         | 157 ms                                                                | 171 ms: 1.09x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 94.9 ms: 1.09x slower                                                    |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.85 us: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 498 ms: 1.12x slower                                                     |
| coverage                   | 87.3 ms                                                               | 98.2 ms: 1.13x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.91 ms: 1.13x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.4 us: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.79 ms: 1.15x slower                                                    |
| nbody                      | 105 ms                                                                | 122 ms: 1.17x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.17 sec: 1.27x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.40 sec: 1.28x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.62 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.09 sec: 154.67x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (9): sympy_integrate, scimark_lu, scimark_fft, django_template, scimark_sor, chaos, unpickle_pure_python, coroutines, logging_silent
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.53% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x