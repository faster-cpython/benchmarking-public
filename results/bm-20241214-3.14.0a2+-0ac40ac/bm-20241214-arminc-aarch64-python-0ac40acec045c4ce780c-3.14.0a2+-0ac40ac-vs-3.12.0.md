# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.025x faster
- HPT reliability: 85.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.55x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 922 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 512 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 671 ms: 1.32x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 243 ms: 1.04x slower                                                     |
| float          | 92.1 ms                                                               | 97.1 ms: 1.05x slower                                                    |
| nbody          | 105 ms                                                                | 121 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| regex_dna      | 254 ms                                                                | 266 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                     |
| xml_etree_process   | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.70 sec: 1.04x slower                                                   |
| json_loads          | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 400 us: 1.10x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.1 ms: 1.02x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                    |
| django_template | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                    |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.05x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.55x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 922 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 512 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 671 ms: 1.32x faster                                                     |
| deepcopy                   | 446 us                                                                | 353 us: 1.26x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 42.7 us: 1.16x faster                                                    |
| pylint                     | 355 ms                                                                | 306 ms: 1.16x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                                    |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                     |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.02 us: 1.04x faster                                                    |
| json                       | 5.54 ms                                                               | 5.61 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 86.5 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 28.1 ms: 1.02x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.04x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.70 sec: 1.04x slower                                                   |
| pidigits                   | 233 ms                                                                | 243 ms: 1.04x slower                                                     |
| regex_dna                  | 254 ms                                                                | 266 ms: 1.05x slower                                                     |
| django_template            | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                                     |
| float                      | 92.1 ms                                                               | 97.1 ms: 1.05x slower                                                    |
| richards_super             | 58.5 ms                                                               | 61.7 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| sympy_expand               | 454 ms                                                                | 484 ms: 1.07x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.45 ms: 1.07x slower                                                    |
| scimark_sor                | 150 ms                                                                | 161 ms: 1.07x slower                                                     |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.07x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 997 ms: 1.09x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.05 sec: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                     |
| richards                   | 50.9 ms                                                               | 55.9 ms: 1.10x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.17 us: 1.10x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                     |
| coverage                   | 87.3 ms                                                               | 97.7 ms: 1.12x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.73 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                     |
| nbody                      | 105 ms                                                                | 121 ms: 1.16x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.05 sec: 1.20x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.95 ms: 1.58x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.14 sec: 870.94x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (26): regex_compile, deltablue, crypto_pyaes, mdp, html5lib, sympy_str, 2to3, spectral_norm, scimark_fft, logging_simple, pyflate, dulwich_log, pycparser, coroutines, scimark_sparse_mat_mult, async_generators, sqlglot_transpile, xml_etree_generate, sqlglot_parse, sympy_integrate, unpickle_pure_python, thrift, bench_thread_pool, chaos, sqlglot_optimize, meteor_contest
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 85.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x