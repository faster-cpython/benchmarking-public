# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.025x faster
- HPT reliability: 94.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 896 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 479 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 508 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 928 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 382 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 687 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.48x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                     |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 265 ms: 1.04x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                   |
| json_loads         | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| xml_etree_process  | 79.0 ms                                                               | 85.7 ms: 1.08x slower                                                    |
| pickle_pure_python | 365 us                                                                | 401 us: 1.10x slower                                                     |
| xml_etree_generate | 112 ms                                                                | 123 ms: 1.10x slower                                                     |
| json_dumps         | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                    |
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 896 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 479 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 508 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 928 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 382 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 687 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                                     |
| deepcopy                   | 446 us                                                                | 342 us: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.1 us: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.9 ms: 1.18x faster                                                    |
| pylint                     | 355 ms                                                                | 306 ms: 1.16x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.9 us: 1.16x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                    |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.3 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.87 us: 1.06x faster                                                    |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.23 us: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.04x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.04x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                     |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.96 sec: 1.04x slower                                                   |
| regex_dna                  | 254 ms                                                                | 265 ms: 1.04x slower                                                     |
| sympy_expand               | 454 ms                                                                | 473 ms: 1.04x slower                                                     |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 966 ms: 1.05x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.05x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.39 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| thrift                     | 937 us                                                                | 994 us: 1.06x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 134 ms: 1.06x slower                                                     |
| pyflate                    | 559 ms                                                                | 597 ms: 1.07x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 85.7 ms: 1.08x slower                                                    |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.09x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 66.7 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 401 us: 1.10x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 123 ms: 1.10x slower                                                     |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| fannkuch                   | 443 ms                                                                | 491 ms: 1.11x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.48 ms: 1.11x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                     |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.03 sec: 1.18x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.83 ms: 1.55x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.61 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.34 sec: 615.15x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (28): go, xml_etree_parse, sqlalchemy_declarative, deltablue, crypto_pyaes, html5lib, xml_etree_iterparse, sympy_str, sqlglot_transpile, async_generators, 2to3, float, dulwich_log, sympy_integrate, coroutines, sqlglot_parse, mdp, spectral_norm, django_template, scimark_fft, scimark_monte_carlo, json, asyncio_websockets, richards_super, unpickle_pure_python, chaos, scimark_sparse_mat_mult, genshi_xml
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 94.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x