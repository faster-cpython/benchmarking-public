# Results vs. 3.12.0

- fork: kumaraditya303
- ref: future_iter
- machine: linux-aarch64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.035x faster
- HPT reliability: 97.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 862 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 875 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 486 ms: 1.60x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 670 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 245 ms: 1.05x slower                                                    |
| nbody          | 105 ms                                                                | 126 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                   |
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                    |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 140 ms: 1.08x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| xml_etree_process   | 79.0 ms                                                               | 81.3 ms: 1.03x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 393 us: 1.08x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.3 ms: 1.16x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.94 ms: 1.07x slower                                                   |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.8 ms: 1.05x slower                                                   |
| genshi_text    | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                   |
| mako           | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 862 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 875 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 486 ms: 1.60x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 670 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 356 us: 1.25x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 41.3 us: 1.20x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                                   |
| pylint                     | 355 ms                                                                | 308 ms: 1.15x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.3 us: 1.14x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.72 us: 1.10x faster                                                   |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                    |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 140 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                   |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.06x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.94 us: 1.05x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.35 us: 1.04x faster                                                   |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| scimark_sor                | 150 ms                                                                | 151 ms: 1.01x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 81.3 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 579 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 972 us: 1.04x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 104 ms: 1.05x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 962 ms: 1.05x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.6 ms: 1.05x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 63.8 ms: 1.05x slower                                                   |
| sympy_expand               | 454 ms                                                                | 478 ms: 1.05x slower                                                    |
| pidigits                   | 233 ms                                                                | 245 ms: 1.05x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.39 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.94 ms: 1.07x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.05 us: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                    |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 483 ms: 1.09x slower                                                    |
| meteor_contest             | 112 ms                                                                | 122 ms: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.16x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.99 ms: 1.17x slower                                                   |
| mypy2                      | 873 ms                                                                | 1.05 sec: 1.20x slower                                                  |
| nbody                      | 105 ms                                                                | 126 ms: 1.20x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.69 ms: 1.52x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.88x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 4.57 sec: 647.19x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (29): deltablue, sqlglot_parse, crypto_pyaes, sqlglot_transpile, spectral_norm, json, 2to3, coroutines, mdp, float, scimark_sparse_mat_mult, dulwich_log, unpickle_pure_python, docutils, html5lib, tomli_loads, async_generators, json_loads, bench_thread_pool, pycparser, chaos, sympy_str, sympy_integrate, asyncio_websockets, scimark_fft, scimark_monte_carlo, django_template, richards_super, sqlglot_optimize
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 97.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x