# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-aarch64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.04x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                              |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                            |
| html5lib       | 65.1 ms                                                               | 66.2 ms: 1.02x slower                                                             |
| tornado_http   | 136 ms                                                                | 125 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                                              |
| async_tree_none            | 624 ms                                                                | 436 ms: 1.43x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 532 ms: 1.39x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 698 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| float          | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                             |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                              |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                             |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 351 us: 1.04x faster                                                              |
| unpickle_pure_python | 260 us                                                                | 250 us: 1.04x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                                            |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                             |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                             |
| django_template | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                             |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                                              |
| async_tree_none            | 624 ms                                                                | 436 ms: 1.43x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 532 ms: 1.39x faster                                                              |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                             |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 698 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                              |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                             |
| raytrace                   | 353 ms                                                                | 296 ms: 1.19x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                             |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.16x faster                                                             |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.09x faster                                                             |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                             |
| tornado_http               | 136 ms                                                                | 125 ms: 1.09x faster                                                              |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.08x faster                                                              |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                             |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                              |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 81.7 ms: 1.06x faster                                                             |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                             |
| chaos                      | 71.4 ms                                                               | 67.9 ms: 1.05x faster                                                             |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.6 ms: 1.04x faster                                                             |
| pickle_pure_python         | 365 us                                                                | 351 us: 1.04x faster                                                              |
| unpickle_pure_python       | 260 us                                                                | 250 us: 1.04x faster                                                              |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                                            |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                              |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                                            |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                             |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.02x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                                            |
| hexiom                     | 6.98 ms                                                               | 6.91 ms: 1.01x faster                                                             |
| bench_mp_pool              | 7.05 ms                                                               | 7.00 ms: 1.01x faster                                                             |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                              |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                              |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                                             |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                             |
| html5lib                   | 65.1 ms                                                               | 66.2 ms: 1.02x slower                                                             |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                              |
| thrift                     | 937 us                                                                | 956 us: 1.02x slower                                                              |
| django_template            | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                             |
| float                      | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                             |
| logging_silent             | 127 ns                                                                | 130 ns: 1.03x slower                                                              |
| richards                   | 50.9 ms                                                               | 52.5 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                                             |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                             |
| pyflate                    | 559 ms                                                                | 579 ms: 1.04x slower                                                              |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                             |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                            |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                             |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                             |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                             |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                             |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                              |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                              |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.10x slower                                                              |
| gc_traversal               | 4.40 ms                                                               | 4.85 ms: 1.10x slower                                                             |
| coverage                   | 87.3 ms                                                               | 98.3 ms: 1.13x slower                                                             |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                             |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.18x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                             |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                                      |

Benchmark hidden because not significant (17): sqlglot_parse, xml_etree_parse, xml_etree_iterparse, async_generators, asyncio_tcp, genshi_xml, regex_dna, pprint_pformat, asyncio_websockets, asyncio_tcp_ssl, pprint_safe_repr, meteor_contest, richards_super, pylint, sqlglot_normalize, xml_etree_generate, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: bpe_tokeniser

# HPT report

- Reliability score: 99.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x