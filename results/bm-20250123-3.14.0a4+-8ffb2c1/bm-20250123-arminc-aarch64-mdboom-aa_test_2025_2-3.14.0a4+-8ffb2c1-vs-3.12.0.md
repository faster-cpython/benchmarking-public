# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.033x faster
- HPT reliability: 99.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 377 ms: 1.65x faster                                               |
| async_tree_memoization     | 777 ms                                                                | 490 ms: 1.58x faster                                               |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                               |
| async_tree_io_tg           | 1.40 sec                                                              | 897 ms: 1.57x faster                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                               |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 681 ms: 1.34x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 664 ms: 1.33x faster                                               |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.0 ms: 1.08x faster                                              |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                              |
| regex_v8       | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 150 ms                                                                | 143 ms: 1.05x faster                                               |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                              |
| xml_etree_process    | 79.0 ms                                                               | 85.3 ms: 1.08x slower                                              |
| pickle_pure_python   | 365 us                                                                | 404 us: 1.11x slower                                               |
| unpickle_pure_python | 260 us                                                                | 290 us: 1.12x slower                                               |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                              |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                              |
| genshi_text    | 27.4 ms                                                               | 29.5 ms: 1.07x slower                                              |
| mako           | 12.9 ms                                                               | 14.4 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 377 ms: 1.65x faster                                               |
| async_tree_memoization     | 777 ms                                                                | 490 ms: 1.58x faster                                               |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                               |
| async_tree_io_tg           | 1.40 sec                                                              | 897 ms: 1.57x faster                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                               |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 681 ms: 1.34x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 664 ms: 1.33x faster                                               |
| deepcopy                   | 446 us                                                                | 351 us: 1.27x faster                                               |
| deepcopy_memo              | 49.6 us                                                               | 40.8 us: 1.22x faster                                              |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.18x faster                                              |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                              |
| pylint                     | 355 ms                                                                | 307 ms: 1.15x faster                                               |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                              |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                               |
| go                         | 157 ms                                                                | 141 ms: 1.12x faster                                               |
| deepcopy_reduce            | 4.10 us                                                               | 3.72 us: 1.10x faster                                              |
| async_generators           | 491 ms                                                                | 447 ms: 1.10x faster                                               |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.10x faster                                              |
| float                      | 92.1 ms                                                               | 85.0 ms: 1.08x faster                                              |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                               |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                               |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                               |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                               |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                               |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                               |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                               |
| sqlglot_transpile          | 1.83 ms                                                               | 1.76 ms: 1.04x faster                                              |
| chaos                      | 71.4 ms                                                               | 68.9 ms: 1.04x faster                                              |
| thrift                     | 937 us                                                                | 948 us: 1.01x slower                                               |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                             |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                             |
| asyncio_websockets         | 658 ms                                                                | 679 ms: 1.03x slower                                               |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                               |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                               |
| sympy_expand               | 454 ms                                                                | 475 ms: 1.05x slower                                               |
| sqlglot_optimize           | 61.3 ms                                                               | 64.3 ms: 1.05x slower                                              |
| pyflate                    | 559 ms                                                                | 589 ms: 1.05x slower                                               |
| genshi_xml                 | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                              |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.00 sec: 1.06x slower                                             |
| pprint_safe_repr           | 916 ms                                                                | 974 ms: 1.06x slower                                               |
| json                       | 5.54 ms                                                               | 5.91 ms: 1.07x slower                                              |
| hexiom                     | 6.98 ms                                                               | 7.44 ms: 1.07x slower                                              |
| sqlglot_normalize          | 126 ms                                                                | 135 ms: 1.07x slower                                               |
| genshi_text                | 27.4 ms                                                               | 29.5 ms: 1.07x slower                                              |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                               |
| xml_etree_process          | 79.0 ms                                                               | 85.3 ms: 1.08x slower                                              |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                              |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                               |
| sqlite_synth               | 3.77 us                                                               | 4.13 us: 1.10x slower                                              |
| pickle_pure_python         | 365 us                                                                | 404 us: 1.11x slower                                               |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.12x slower                                              |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                               |
| unpickle_pure_python       | 260 us                                                                | 290 us: 1.12x slower                                               |
| telco                      | 8.51 ms                                                               | 9.60 ms: 1.13x slower                                              |
| coverage                   | 87.3 ms                                                               | 99.5 ms: 1.14x slower                                              |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                               |
| regex_v8                   | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                              |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                              |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                              |
| gc_traversal               | 4.40 ms                                                               | 7.01 ms: 1.60x slower                                              |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                              |
| bench_mp_pool              | 7.05 ms                                                               | 6.60 sec: 935.11x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                       |

Benchmark hidden because not significant (24): regex_compile, sqlalchemy_imperative, crypto_pyaes, logging_format, dulwich_log, deltablue, html5lib, sympy_integrate, scimark_monte_carlo, sqlglot_parse, logging_simple, richards_super, xml_etree_generate, tomli_loads, richards, coroutines, scimark_sparse_mat_mult, scimark_fft, nqueens, bench_thread_pool, 2to3, pidigits, regex_dna, django_template
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.22% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x