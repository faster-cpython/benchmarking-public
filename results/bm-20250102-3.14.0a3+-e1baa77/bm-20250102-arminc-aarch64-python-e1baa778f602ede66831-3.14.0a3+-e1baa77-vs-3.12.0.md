# Results vs. 3.12.0

- fork: python
- ref: e1baa778f602ede66831
- machine: linux-aarch64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.034x faster
- HPT reliability: 98.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 393 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 894 ms: 1.57x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 904 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 502 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 677 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 663 ms: 1.33x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 246 ms: 1.06x slower                                                     |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_dna      | 254 ms                                                                | 250 ms: 1.02x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| pickle_pure_python  | 365 us                                                                | 382 us: 1.05x slower                                                     |
| xml_etree_process   | 79.0 ms                                                               | 83.1 ms: 1.05x slower                                                    |
| json_loads          | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| xml_etree_generate  | 112 ms                                                                | 119 ms: 1.06x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.97 ms: 1.07x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 64.3 ms: 1.06x slower                                                    |
| mako           | 12.9 ms                                                               | 14.4 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 393 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 894 ms: 1.57x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 904 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 502 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 677 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 663 ms: 1.33x faster                                                     |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.3 us: 1.20x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.5 us: 1.18x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| pylint                     | 355 ms                                                                | 307 ms: 1.15x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.9 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                    |
| go                         | 157 ms                                                                | 143 ms: 1.10x faster                                                     |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                     |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.90 us: 1.06x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.8 ms: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.26 us: 1.05x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.97 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.02x faster                                                     |
| docutils                   | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                     |
| richards                   | 50.9 ms                                                               | 52.0 ms: 1.02x slower                                                    |
| pyflate                    | 559 ms                                                                | 573 ms: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 63.3 ms: 1.03x slower                                                    |
| scimark_fft                | 418 ms                                                                | 437 ms: 1.04x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                   |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 962 ms: 1.05x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 83.1 ms: 1.05x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                                     |
| sympy_expand               | 454 ms                                                                | 478 ms: 1.05x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.05x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| pidigits                   | 233 ms                                                                | 246 ms: 1.06x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 64.3 ms: 1.06x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 119 ms: 1.06x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.97 ms: 1.07x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.06 us: 1.08x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.53 ms: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.10x slower                                                     |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.12x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.56 ms: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| mypy2                      | 873 ms                                                                | 1.03 sec: 1.18x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.00 ms: 1.59x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.59 ms: 1.87x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.93 sec: 698.37x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (25): sympy_str, spectral_norm, crypto_pyaes, sqlglot_parse, sqlglot_transpile, dulwich_log, 2to3, tomli_loads, genshi_text, chaos, thrift, float, scimark_sparse_mat_mult, mdp, html5lib, sympy_integrate, coroutines, django_template, async_generators, scimark_monte_carlo, pycparser, bench_thread_pool, unpickle_pure_python, richards_super, scimark_sor
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 98.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x