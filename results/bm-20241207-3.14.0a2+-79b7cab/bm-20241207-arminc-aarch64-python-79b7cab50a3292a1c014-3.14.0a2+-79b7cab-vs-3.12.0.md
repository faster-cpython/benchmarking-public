# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.028x faster
- HPT reliability: 86.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 917 ms: 1.54x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 946 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 528 ms: 1.47x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 520 ms: 1.42x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 411 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 690 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 698 ms: 1.27x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.43x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                     |
| float          | 92.1 ms                                                               | 95.8 ms: 1.04x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 128 ms: 1.08x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse | 150 ms                                                                | 140 ms: 1.07x faster                                                     |
| xml_etree_parse     | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| xml_etree_generate  | 112 ms                                                                | 116 ms: 1.03x slower                                                     |
| json_loads          | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 386 us: 1.06x slower                                                     |
| xml_etree_process   | 79.0 ms                                                               | 83.6 ms: 1.06x slower                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.76 sec: 1.07x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.08 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.3 ms: 1.05x slower                                                    |
| genshi_text    | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                    |
| mako           | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 917 ms: 1.54x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 946 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 528 ms: 1.47x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 520 ms: 1.42x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 411 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 690 ms: 1.32x faster                                                     |
| deepcopy                   | 446 us                                                                | 344 us: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 698 ms: 1.27x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.3 us: 1.23x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.0 us: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.62 us: 1.13x faster                                                    |
| pylint                     | 355 ms                                                                | 318 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                                     |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.09x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.74 us: 1.08x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 140 ms: 1.07x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.24 us: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.98 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 60.6 ms: 1.02x faster                                                    |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 62.9 ms: 1.03x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 116 ms: 1.03x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.95 sec: 1.04x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.25 ms: 1.04x slower                                                    |
| sympy_expand               | 454 ms                                                                | 471 ms: 1.04x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 952 ms: 1.04x slower                                                     |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                     |
| float                      | 92.1 ms                                                               | 95.8 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 977 us: 1.04x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 63.3 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 386 us: 1.06x slower                                                     |
| richards_super             | 58.5 ms                                                               | 61.8 ms: 1.06x slower                                                    |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.06x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 83.6 ms: 1.06x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 134 ms: 1.06x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.76 sec: 1.07x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.08x slower                                                     |
| richards                   | 50.9 ms                                                               | 55.0 ms: 1.08x slower                                                    |
| pyflate                    | 559 ms                                                                | 605 ms: 1.08x slower                                                     |
| scimark_fft                | 418 ms                                                                | 453 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.08 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                                    |
| scimark_sor                | 150 ms                                                                | 164 ms: 1.10x slower                                                     |
| fannkuch                   | 443 ms                                                                | 490 ms: 1.11x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.86 ms: 1.11x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                     |
| logging_silent             | 127 ns                                                                | 143 ns: 1.13x slower                                                     |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.13x slower                                                     |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.00 ms: 1.18x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.92 ms: 1.57x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.30 ms: 1.72x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 3.66 sec: 519.44x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (17): sqlglot_transpile, html5lib, crypto_pyaes, sqlglot_parse, sympy_str, chaos, 2to3, django_template, coroutines, scimark_monte_carlo, regex_dna, mdp, sympy_integrate, bench_thread_pool, asyncio_websockets, unpickle_pure_python, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 86.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x