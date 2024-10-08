# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.03x slower                                                            |
| docutils       | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                          |
| html5lib       | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 93.0 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                                            |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                           |
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                           |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.50 ms: 1.05x faster                                                           |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                           |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                            |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                          |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 98.8 ms: 1.09x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 81.9 ms: 1.07x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 209 us: 1.04x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                            |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                           |
| django_template | 34.8 ms                                                    | 35.7 ms: 1.02x slower                                                           |
| genshi_text     | 23.7 ms                                                    | 26.0 ms: 1.10x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 59.7 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.5 us: 1.50x faster                                                           |
| deepcopy                   | 367 us                                                     | 268 us: 1.37x faster                                                            |
| richards                   | 50.9 ms                                                    | 39.0 ms: 1.30x faster                                                           |
| richards_super             | 57.4 ms                                                    | 44.3 ms: 1.29x faster                                                           |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 65.5 ms: 1.18x faster                                                           |
| spectral_norm              | 116 ms                                                     | 98.6 ms: 1.18x faster                                                           |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                            |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                           |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.12x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                                            |
| float                      | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.4 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                            |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.57 sec: 1.10x faster                                                          |
| coverage                   | 93.1 ms                                                    | 84.9 ms: 1.10x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                          |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                                           |
| telco                      | 8.41 ms                                                    | 7.77 ms: 1.08x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.69 ms: 1.08x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.02 us: 1.08x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 81.9 ms: 1.07x faster                                                           |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                                            |
| pyflate                    | 484 ms                                                     | 456 ms: 1.06x faster                                                            |
| logging_silent             | 105 ns                                                     | 98.7 ns: 1.06x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                           |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                           |
| regex_effbot               | 3.67 ms                                                    | 3.50 ms: 1.05x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.66 sec: 1.05x faster                                                          |
| unpickle_pure_python       | 218 us                                                     | 209 us: 1.04x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.12 ms: 1.04x faster                                                           |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                            |
| thrift                     | 823 us                                                     | 794 us: 1.04x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                           |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 736 ms: 1.03x faster                                                            |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 816 us: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                           |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 93.0 ms: 1.02x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                          |
| raytrace                   | 267 ms                                                     | 263 ms: 1.01x faster                                                            |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                           |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                           |
| go                         | 145 ms                                                     | 145 ms: 1.01x slower                                                            |
| json                       | 5.31 ms                                                    | 5.37 ms: 1.01x slower                                                           |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                            |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                            |
| django_template            | 34.8 ms                                                    | 35.7 ms: 1.02x slower                                                           |
| 2to3                       | 274 ms                                                     | 281 ms: 1.03x slower                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                           |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 57.9 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 165 us                                                     | 174 us: 1.06x slower                                                            |
| docutils                   | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                          |
| nqueens                    | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                           |
| hexiom                     | 6.30 ms                                                    | 6.76 ms: 1.07x slower                                                           |
| sympy_str                  | 282 ms                                                     | 305 ms: 1.08x slower                                                            |
| sympy_expand               | 473 ms                                                     | 513 ms: 1.09x slower                                                            |
| genshi_text                | 23.7 ms                                                    | 26.0 ms: 1.10x slower                                                           |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                           |
| sympy_integrate            | 20.5 ms                                                    | 23.0 ms: 1.12x slower                                                           |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                                            |
| genshi_xml                 | 51.6 ms                                                    | 59.7 ms: 1.16x slower                                                           |
| pylint                     | 317 ms                                                     | 368 ms: 1.16x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (4): pycparser, pprint_pformat, comprehensions, sqlglot_parse
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x