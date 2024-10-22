# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x faster
- HPT reliability: 93.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 261 ms: 1.01x faster                                                            |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                          |
| html5lib       | 64.5 ms                                                | 64.8 ms: 1.00x slower                                                           |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                            |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 486 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 885 ms: 1.07x slower                                                            |
| async_tree_io              | 843 ms                                                 | 907 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.9 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 87.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.60 ms: 1.08x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                           |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                            |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                          |
| xml_etree_process   | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                           |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| xml_etree_generate  | 87.0 ms                                                | 86.4 ms: 1.01x faster                                                           |
| xml_etree_parse     | 156 ms                                                 | 159 ms: 1.02x slower                                                            |
| xml_etree_iterparse | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| json_loads          | 27.0 us                                                | 28.3 us: 1.05x slower                                                           |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.3 ms: 1.00x faster                                                           |
| genshi_text     | 22.9 ms                                                | 23.0 ms: 1.01x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 51.0 ms: 1.01x slower                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 259 us: 1.36x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 29.8 us: 1.28x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                           |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.60 ms: 1.08x faster                                                           |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| richards                   | 48.1 ms                                                | 45.4 ms: 1.06x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                          |
| richards_super             | 54.4 ms                                                | 51.9 ms: 1.05x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.45 us: 1.04x faster                                                           |
| telco                      | 8.45 ms                                                | 8.14 ms: 1.04x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 786 us: 1.04x faster                                                            |
| logging_format             | 6.25 us                                                | 6.07 us: 1.03x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.67 sec: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                            |
| raytrace                   | 262 ms                                                 | 256 ms: 1.02x faster                                                            |
| nqueens                    | 80.6 ms                                                | 78.8 ms: 1.02x faster                                                           |
| scimark_fft                | 369 ms                                                 | 361 ms: 1.02x faster                                                            |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| tomli_loads                | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                          |
| go                         | 142 ms                                                 | 139 ms: 1.02x faster                                                            |
| 2to3                       | 265 ms                                                 | 261 ms: 1.01x faster                                                            |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                           |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                                           |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                            |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                            |
| sympy_expand               | 462 ms                                                 | 457 ms: 1.01x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 86.4 ms: 1.01x faster                                                           |
| float                      | 78.5 ms                                                | 77.9 ms: 1.01x faster                                                           |
| chaos                      | 58.4 ms                                                | 58.1 ms: 1.01x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 486 ms: 1.00x faster                                                            |
| django_template            | 34.4 ms                                                | 34.3 ms: 1.00x faster                                                           |
| hexiom                     | 6.13 ms                                                | 6.10 ms: 1.00x faster                                                           |
| deltablue                  | 3.15 ms                                                | 3.14 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| coverage                   | 83.7 ms                                                | 84.0 ms: 1.00x slower                                                           |
| html5lib                   | 64.5 ms                                                | 64.8 ms: 1.00x slower                                                           |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 66.6 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.51 sec                                               | 1.52 sec: 1.01x slower                                                          |
| genshi_text                | 22.9 ms                                                | 23.0 ms: 1.01x slower                                                           |
| crypto_pyaes               | 73.0 ms                                                | 73.5 ms: 1.01x slower                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                            |
| pyflate                    | 460 ms                                                 | 464 ms: 1.01x slower                                                            |
| gc_traversal               | 3.81 ms                                                | 3.85 ms: 1.01x slower                                                           |
| genshi_xml                 | 50.3 ms                                                | 51.0 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                                            |
| nbody                      | 85.7 ms                                                | 87.3 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                            |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.78 sec: 1.02x slower                                                          |
| json                       | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| fannkuch                   | 381 ms                                                 | 396 ms: 1.04x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                          |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 885 ms: 1.07x slower                                                            |
| async_tree_io              | 843 ms                                                 | 907 ms: 1.08x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (9): sympy_str, pickle_pure_python, bench_mp_pool, sqlglot_transpile, unpickle_pure_python, async_generators, pprint_safe_repr, logging_silent, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 93.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x