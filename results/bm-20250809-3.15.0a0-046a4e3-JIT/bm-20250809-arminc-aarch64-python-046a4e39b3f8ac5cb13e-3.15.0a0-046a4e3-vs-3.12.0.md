# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.025x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 314 ms: 1.02x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 63.4 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                    |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 913 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.3 ms: 1.12x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 127 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                   |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.3 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                  |
| xml_etree_parse      | 195 ms                                                                | 177 ms: 1.10x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 250 us: 1.04x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                                   |
| unpickle_list        | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 389 us: 1.06x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.69 us: 1.08x slower                                                   |
| pickle               | 13.4 us                                                               | 15.8 us: 1.18x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): json_dumps, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 12.7 ms: 1.02x faster                                                   |
| genshi_xml     | 60.6 ms                                                               | 62.9 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.63 sec: 2.09x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                    |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 913 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                    |
| deepcopy                   | 446 us                                                                | 324 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.7 us: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                   |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 54.5 ms: 1.14x faster                                                   |
| spectral_norm              | 131 ms                                                                | 116 ms: 1.12x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.6 us: 1.12x faster                                                   |
| float                      | 92.1 ms                                                               | 82.3 ms: 1.12x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                  |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 177 ms: 1.10x faster                                                    |
| richards                   | 50.9 ms                                                               | 46.3 ms: 1.10x faster                                                   |
| richards_super             | 58.5 ms                                                               | 53.4 ms: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.65 us: 1.09x faster                                                   |
| pyflate                    | 559 ms                                                                | 513 ms: 1.09x faster                                                    |
| pylint                     | 355 ms                                                                | 326 ms: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.79 ms: 1.09x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.04 us: 1.08x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.3 ms: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.1 ms: 1.06x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.1 ms: 1.05x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 250 us: 1.04x faster                                                    |
| go                         | 157 ms                                                                | 151 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.04x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 548 ms: 1.03x faster                                                    |
| sympy_str                  | 280 ms                                                                | 271 ms: 1.03x faster                                                    |
| scimark_fft                | 418 ms                                                                | 406 ms: 1.03x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 63.4 ms: 1.03x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.70 us: 1.02x faster                                                   |
| mako                       | 12.9 ms                                                               | 12.7 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| 2to3                       | 308 ms                                                                | 314 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 62.9 ms: 1.04x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.35 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 389 us: 1.06x slower                                                    |
| sympy_expand               | 454 ms                                                                | 486 ms: 1.07x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.69 us: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.09x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.03 ms: 1.13x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.8 us: 1.18x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.09 sec: 1.19x slower                                                  |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.25 sec: 1.20x slower                                                  |
| nbody                      | 105 ms                                                                | 127 ms: 1.22x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.77 ms: 1.54x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                   |
| telco                      | 8.51 ms                                                               | 163 ms: 19.14x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 1.23 sec: 174.53x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (13): json_dumps, scimark_sor, async_generators, genshi_text, unpickle, meteor_contest, django_template, logging_silent, crypto_pyaes, pickle_dict, thrift, scimark_lu, coroutines
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.12x