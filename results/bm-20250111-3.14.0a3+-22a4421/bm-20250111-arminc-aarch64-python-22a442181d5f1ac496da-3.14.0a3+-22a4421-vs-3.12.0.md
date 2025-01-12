# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.038x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 889 ms: 1.59x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 495 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 367 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 679 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 667 ms: 1.33x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.1 ms: 1.03x faster                                                    |
| pidigits       | 233 ms                                                                | 243 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.11 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.4 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 385 us: 1.05x slower                                                     |
| pickle_dict         | 37.3 us                                                               | 39.5 us: 1.06x slower                                                    |
| xml_etree_process   | 79.0 ms                                                               | 84.2 ms: 1.07x slower                                                    |
| unpickle_list       | 6.17 us                                                               | 6.76 us: 1.10x slower                                                    |
| pickle              | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| pickle_list         | 5.25 us                                                               | 6.29 us: 1.20x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (4): unpickle, tomli_loads, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 889 ms: 1.59x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 495 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 367 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 679 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 667 ms: 1.33x faster                                                     |
| deepcopy                   | 446 us                                                                | 350 us: 1.27x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.2 us: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.7 us: 1.17x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.11 ms: 1.13x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.74 us: 1.10x faster                                                    |
| pylint                     | 355 ms                                                                | 324 ms: 1.09x faster                                                     |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                     |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.4 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.00 us: 1.04x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 83.1 ms: 1.04x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| float                      | 92.1 ms                                                               | 89.1 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                    |
| docutils                   | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                   |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                                     |
| richards                   | 50.9 ms                                                               | 52.1 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.9 ms: 1.03x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                   |
| pidigits                   | 233 ms                                                                | 243 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 963 ms: 1.05x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.98 sec: 1.05x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 385 us: 1.05x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.5 us: 1.06x slower                                                    |
| sympy_expand               | 454 ms                                                                | 482 ms: 1.06x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 84.2 ms: 1.07x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 478 ms: 1.08x slower                                                     |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.76 us: 1.10x slower                                                    |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.70 ms: 1.10x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.19 us: 1.11x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 201 us: 1.11x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.7 ms: 1.14x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.4 ms: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.96 ms: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.29 us: 1.20x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.85 ms: 1.56x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.87x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.18 sec: 592.93x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (32): sympy_sum, deltablue, logging_simple, html5lib, 2to3, regex_dna, spectral_norm, unpickle, sqlglot_transpile, sympy_integrate, mdp, asyncio_tcp, tomli_loads, sqlglot_parse, scimark_sparse_mat_mult, dulwich_log, async_generators, django_template, json, pycparser, pyflate, asyncio_websockets, unpickle_pure_python, scimark_fft, scimark_monte_carlo, meteor_contest, bench_thread_pool, chaos, genshi_text, xml_etree_generate, richards_super, genshi_xml
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x