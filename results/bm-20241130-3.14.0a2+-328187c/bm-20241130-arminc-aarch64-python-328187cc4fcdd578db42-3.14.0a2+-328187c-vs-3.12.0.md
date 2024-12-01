# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.009x faster
- HPT reliability: 63.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 573 ms: 1.36x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 564 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 751 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 760 ms: 1.16x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| float          | 92.1 ms                                                               | 99.0 ms: 1.07x slower                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_dna      | 254 ms                                                                | 263 ms: 1.04x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| json_loads         | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.74 sec: 1.06x slower                                                   |
| xml_etree_process  | 79.0 ms                                                               | 83.6 ms: 1.06x slower                                                    |
| pickle_pure_python | 365 us                                                                | 411 us: 1.13x slower                                                     |
| json_dumps         | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 573 ms: 1.36x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 564 ms: 1.31x faster                                                     |
| deepcopy                   | 446 us                                                                | 354 us: 1.26x faster                                                     |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 751 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.0 us: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                   |
| pylint                     | 355 ms                                                                | 297 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 760 ms: 1.16x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.8 us: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.14x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                   |
| go                         | 157 ms                                                                | 142 ms: 1.11x faster                                                     |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.99 us: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.78 us: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.05x faster                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 63.0 ms: 1.03x slower                                                    |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 947 ms: 1.03x slower                                                     |
| regex_dna                  | 254 ms                                                                | 263 ms: 1.04x slower                                                     |
| async_generators           | 491 ms                                                                | 509 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.96 sec: 1.04x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.74 sec: 1.06x slower                                                   |
| sympy_expand               | 454 ms                                                                | 480 ms: 1.06x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 83.6 ms: 1.06x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.07x slower                                                    |
| pyflate                    | 559 ms                                                                | 601 ms: 1.07x slower                                                     |
| float                      | 92.1 ms                                                               | 99.0 ms: 1.07x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.75 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.9 ms: 1.09x slower                                                    |
| fannkuch                   | 443 ms                                                                | 486 ms: 1.10x slower                                                     |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 138 ms: 1.10x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.38 ms: 1.10x slower                                                    |
| scimark_sor                | 150 ms                                                                | 165 ms: 1.11x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.4 ms: 1.11x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.18 us: 1.11x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.11x slower                                                     |
| logging_silent             | 127 ns                                                                | 143 ns: 1.12x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 411 us: 1.13x slower                                                     |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                                    |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.36 ms: 1.45x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.89 sec: 834.75x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (27): crypto_pyaes, 2to3, sympy_sum, deltablue, coroutines, django_template, bench_thread_pool, html5lib, json, sqlalchemy_imperative, mdp, sqlglot_transpile, sqlglot_parse, xml_etree_parse, chaos, sympy_str, pycparser, unpickle_pure_python, sympy_integrate, asyncio_websockets, dulwich_log, xml_etree_iterparse, meteor_contest, thrift, genshi_xml, hexiom, genshi_text
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 63.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x