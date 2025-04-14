# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                   |
| html5lib       | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 876 ms: 1.61x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                     |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 890 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 642 ms: 1.38x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                    |
| nbody          | 105 ms                                                                | 128 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                     |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 173 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.46 sec: 1.05x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 78.4 ms: 1.01x faster                                                    |
| unpickle_list       | 6.17 us                                                               | 6.35 us: 1.03x slower                                                    |
| pickle_dict         | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 386 us: 1.06x slower                                                     |
| pickle_list         | 5.25 us                                                               | 5.63 us: 1.07x slower                                                    |
| json_loads          | 30.7 us                                                               | 35.0 us: 1.14x slower                                                    |
| pickle              | 13.4 us                                                               | 15.5 us: 1.15x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.9 ms: 1.21x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): unpickle, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 59.0 ms: 1.03x faster                                                    |
| mako           | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.07x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 876 ms: 1.61x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                     |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 890 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 642 ms: 1.38x faster                                                     |
| deepcopy                   | 446 us                                                                | 340 us: 1.31x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.5 us: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 53.7 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 137 ms: 1.14x faster                                                     |
| pylint                     | 355 ms                                                                | 310 ms: 1.14x faster                                                     |
| raytrace                   | 353 ms                                                                | 313 ms: 1.13x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 173 ms: 1.12x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.68 us: 1.11x faster                                                    |
| async_generators           | 491 ms                                                                | 441 ms: 1.11x faster                                                     |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.93 us: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.79 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                     |
| float                      | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.05x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                     |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 550 ms: 1.03x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 59.0 ms: 1.03x faster                                                    |
| richards_super             | 58.5 ms                                                               | 57.3 ms: 1.02x faster                                                    |
| scimark_sor                | 150 ms                                                                | 147 ms: 1.02x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 85.3 ms: 1.02x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 78.4 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                   |
| richards                   | 50.9 ms                                                               | 50.7 ms: 1.00x faster                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 938 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.35 ms: 1.02x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.35 us: 1.03x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.94 sec: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 467 ms: 1.03x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.04x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.30 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 386 us: 1.06x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.63 us: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.58 ms: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.0 ms: 1.13x slower                                                    |
| json_loads                 | 30.7 us                                                               | 35.0 us: 1.14x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.5 us: 1.15x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.21x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| nbody                      | 105 ms                                                                | 128 ms: 1.22x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.65 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.63 ms: 1.89x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.93 sec: 273.69x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (16): spectral_norm, sympy_integrate, chaos, scimark_monte_carlo, unpickle, django_template, genshi_text, pyflate, pycparser, regex_v8, scimark_fft, logging_silent, unpickle_pure_python, xml_etree_generate, pidigits, coroutines
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x