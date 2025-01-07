# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.033x faster
- HPT reliability: 93.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 888 ms: 1.59x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 884 ms: 1.59x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 495 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 473 ms: 1.57x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                   |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                  |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                   |
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                   |
| xml_etree_generate  | 112 ms                                                                | 115 ms: 1.03x slower                                                   |
| xml_etree_process   | 79.0 ms                                                               | 81.6 ms: 1.03x slower                                                  |
| json_loads          | 30.7 us                                                               | 31.7 us: 1.03x slower                                                  |
| pickle_pure_python  | 365 us                                                                | 405 us: 1.11x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                  |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.88 ms: 1.06x slower                                                  |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                  |
| genshi_xml     | 60.6 ms                                                               | 64.4 ms: 1.06x slower                                                  |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 888 ms: 1.59x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 884 ms: 1.59x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 495 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 473 ms: 1.57x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                   |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 41.1 us: 1.21x faster                                                  |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                  |
| pylint                     | 355 ms                                                                | 307 ms: 1.15x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.1 us: 1.15x faster                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.69 us: 1.11x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                  |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                   |
| go                         | 157 ms                                                                | 146 ms: 1.07x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.14 us: 1.07x faster                                                  |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                  |
| logging_format             | 8.34 us                                                               | 7.93 us: 1.05x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.04x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.98 ms: 1.04x faster                                                  |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                 |
| richards                   | 50.9 ms                                                               | 52.1 ms: 1.02x slower                                                  |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                 |
| xml_etree_generate         | 112 ms                                                                | 115 ms: 1.03x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 81.6 ms: 1.03x slower                                                  |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.04x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 63.6 ms: 1.04x slower                                                  |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.98 sec: 1.05x slower                                                 |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 966 ms: 1.05x slower                                                   |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.56 ms: 1.06x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.88 ms: 1.06x slower                                                  |
| sympy_expand               | 454 ms                                                                | 482 ms: 1.06x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 64.4 ms: 1.06x slower                                                  |
| pyflate                    | 559 ms                                                                | 595 ms: 1.06x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.07x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.52 ms: 1.08x slower                                                  |
| logging_silent             | 127 ns                                                                | 140 ns: 1.11x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.17 us: 1.11x slower                                                  |
| pickle_pure_python         | 365 us                                                                | 405 us: 1.11x slower                                                   |
| fannkuch                   | 443 ms                                                                | 492 ms: 1.11x slower                                                   |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.68 ms: 1.14x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                   |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                  |
| mypy2                      | 873 ms                                                                | 1.06 sec: 1.21x slower                                                 |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 6.99 ms: 1.59x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 5.70 sec: 807.52x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                           |

Benchmark hidden because not significant (21): crypto_pyaes, dulwich_log, sqlglot_parse, 2to3, django_template, async_generators, tomli_loads, float, chaos, mdp, sympy_integrate, sqlglot_transpile, spectral_norm, json, coroutines, scimark_fft, unpickle_pure_python, richards_super, scimark_monte_carlo, html5lib, thrift
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 93.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x