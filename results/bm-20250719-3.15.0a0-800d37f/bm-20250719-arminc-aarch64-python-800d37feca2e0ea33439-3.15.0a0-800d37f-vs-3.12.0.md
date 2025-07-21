# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 372 ms: 1.68x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 871 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 892 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.9 ms: 1.08x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                                   |
| regex_dna      | 254 ms                                                                | 219 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.6 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 259 us: 1.01x faster                                                    |
| unpickle_list        | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 387 us: 1.06x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.63 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                   |
| pickle               | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.42 ms: 1.01x slower                                                   |
| python_startup         | 11.4 ms                                                               | 14.8 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.14x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                   |
| mako           | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.70 sec: 2.01x faster                                                  |
| async_tree_none            | 624 ms                                                                | 372 ms: 1.68x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 871 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 892 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.2 us: 1.34x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.3 ms: 1.23x faster                                                   |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                                   |
| regex_dna                  | 254 ms                                                                | 219 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.61 us: 1.14x faster                                                   |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 55.1 ms: 1.13x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.97 us: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                   |
| float                      | 92.1 ms                                                               | 84.9 ms: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 529 ms: 1.07x faster                                                    |
| async_generators           | 491 ms                                                                | 459 ms: 1.07x faster                                                    |
| sympy_str                  | 280 ms                                                                | 262 ms: 1.07x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.6 ms: 1.06x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.2 ms: 1.06x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.5 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.6 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| pyflate                    | 559 ms                                                                | 534 ms: 1.05x faster                                                    |
| meteor_contest             | 112 ms                                                                | 107 ms: 1.04x faster                                                    |
| hexiom                     | 6.98 ms                                                               | 6.80 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.02x faster                                                  |
| genshi_text                | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.14 sec: 1.02x faster                                                  |
| pprint_safe_repr           | 916 ms                                                                | 900 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 259 us: 1.01x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 29.1 ms: 1.00x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.42 ms: 1.01x slower                                                   |
| richards_super             | 58.5 ms                                                               | 58.8 ms: 1.01x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 957 us: 1.02x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 470 ms: 1.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.63 us: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.09 ms: 1.14x slower                                                   |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                    |
| python_startup             | 11.4 ms                                                               | 14.8 ms: 1.30x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.94 ms: 1.58x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.82 ms: 1.99x slower                                                   |
| telco                      | 8.51 ms                                                               | 163 ms: 19.21x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 3.17 sec: 449.90x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (19): scimark_sor, html5lib, deltablue, 2to3, pycparser, docutils, crypto_pyaes, xml_etree_generate, django_template, xml_etree_process, scimark_lu, unpickle, nqueens, asyncio_websockets, scimark_fft, pickle_dict, logging_silent, genshi_xml, richards
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x