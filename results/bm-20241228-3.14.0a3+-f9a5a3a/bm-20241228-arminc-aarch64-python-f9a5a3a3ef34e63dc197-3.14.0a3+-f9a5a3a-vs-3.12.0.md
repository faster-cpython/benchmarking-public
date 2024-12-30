# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.027x faster
- HPT reliability: 91.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 910 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 407 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 486 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 929 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 519 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 391 ms: 1.47x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 694 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| nbody          | 105 ms                                                                | 126 ms: 1.21x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 131 ms: 1.05x faster                                                     |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 33.6 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| xml_etree_generate  | 112 ms                                                                | 116 ms: 1.04x slower                                                     |
| xml_etree_process   | 79.0 ms                                                               | 83.5 ms: 1.06x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                     |
| json_loads          | 30.7 us                                                               | 33.4 us: 1.09x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                    |
| genshi_xml     | 60.6 ms                                                               | 64.5 ms: 1.07x slower                                                    |
| mako           | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 910 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 407 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 486 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 929 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 519 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 391 ms: 1.47x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 694 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                                     |
| deepcopy                   | 446 us                                                                | 344 us: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.1 us: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.4 us: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.67 us: 1.12x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                                     |
| pylint                     | 355 ms                                                                | 325 ms: 1.09x faster                                                     |
| go                         | 157 ms                                                                | 145 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.89 us: 1.06x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.22 us: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                     |
| regex_compile              | 137 ms                                                                | 131 ms: 1.05x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.98 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.16 ms: 1.01x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.6 ms: 1.03x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 116 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 131 ms: 1.05x slower                                                     |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 64.4 ms: 1.05x slower                                                    |
| thrift                     | 937 us                                                                | 983 us: 1.05x slower                                                     |
| pidigits                   | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 83.5 ms: 1.06x slower                                                    |
| pyflate                    | 559 ms                                                                | 592 ms: 1.06x slower                                                     |
| sympy_expand               | 454 ms                                                                | 482 ms: 1.06x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 64.5 ms: 1.07x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.03 sec: 1.08x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                     |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.57 ms: 1.09x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.4 us: 1.09x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 996 ms: 1.09x slower                                                     |
| logging_silent             | 127 ns                                                                | 141 ns: 1.11x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 202 us: 1.12x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.65 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.6 ms: 1.19x slower                                                    |
| nbody                      | 105 ms                                                                | 126 ms: 1.21x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.06 sec: 1.21x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.90 ms: 1.57x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.57 ms: 1.86x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.30 sec: 893.69x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (23): xml_etree_parse, crypto_pyaes, sympy_str, async_generators, django_template, mdp, 2to3, scimark_monte_carlo, coroutines, tomli_loads, html5lib, sqlglot_parse, bench_thread_pool, spectral_norm, sqlglot_transpile, chaos, json, sympy_integrate, scimark_fft, dulwich_log, float, richards_super, unpickle_pure_python
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 91.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x