# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x faster
- HPT reliability: 72.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 281 ms: 1.06x slower                                                            |
| docutils       | 2.58 sec                                               | 3.00 sec: 1.16x slower                                                          |
| html5lib       | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                           |
| tornado_http   | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 396 ms: 1.17x faster                                                            |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 429 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                           |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                            |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                                            |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                           |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.50 ms: 1.11x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                           |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                            |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                          |
| xml_etree_generate   | 87.0 ms                                                | 81.9 ms: 1.06x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                            |
| xml_etree_process    | 60.4 ms                                                | 57.7 ms: 1.05x faster                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                            |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                            |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                           |
| django_template | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                           |
| genshi_text     | 22.9 ms                                                | 26.0 ms: 1.13x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 59.7 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.5 us: 1.44x faster                                                           |
| deepcopy                   | 352 us                                                 | 268 us: 1.32x faster                                                            |
| richards                   | 48.1 ms                                                | 39.0 ms: 1.23x faster                                                           |
| richards_super             | 54.4 ms                                                | 44.3 ms: 1.23x faster                                                           |
| scimark_fft                | 369 ms                                                 | 306 ms: 1.20x faster                                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 396 ms: 1.17x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                           |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.15x faster                                                           |
| mako                       | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                           |
| float                      | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 65.5 ms: 1.11x faster                                                           |
| regex_effbot               | 3.88 ms                                                | 3.50 ms: 1.11x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                          |
| telco                      | 8.45 ms                                                | 7.77 ms: 1.09x faster                                                           |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                            |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.08x faster                                                            |
| nbody                      | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 81.9 ms: 1.06x faster                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 62.4 ms: 1.06x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                            |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 57.7 ms: 1.05x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                          |
| logging_format             | 6.25 us                                                | 6.02 us: 1.04x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                           |
| logging_silent             | 102 ns                                                 | 98.7 ns: 1.03x faster                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.69 ms: 1.03x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 429 ms: 1.03x faster                                                            |
| mdp                        | 2.74 sec                                               | 2.66 sec: 1.03x faster                                                          |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.03x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                            |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 736 ms: 1.01x faster                                                            |
| fannkuch                   | 381 ms                                                 | 377 ms: 1.01x faster                                                            |
| deltablue                  | 3.15 ms                                                | 3.12 ms: 1.01x faster                                                           |
| pyflate                    | 460 ms                                                 | 456 ms: 1.01x faster                                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| coverage                   | 83.7 ms                                                | 84.9 ms: 1.01x slower                                                           |
| tornado_http               | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                           |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                           |
| html5lib                   | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                           |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.55 sec: 1.02x slower                                                          |
| go                         | 142 ms                                                 | 145 ms: 1.03x slower                                                            |
| json                       | 5.20 ms                                                | 5.37 ms: 1.03x slower                                                           |
| django_template            | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                           |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                           |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                                            |
| 2to3                       | 265 ms                                                 | 281 ms: 1.06x slower                                                            |
| json_loads                 | 27.0 us                                                | 28.7 us: 1.06x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                           |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                            |
| nqueens                    | 80.6 ms                                                | 86.6 ms: 1.07x slower                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                           |
| regex_compile              | 131 ms                                                 | 141 ms: 1.08x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 174 us: 1.10x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.76 ms: 1.10x slower                                                           |
| sympy_expand               | 462 ms                                                 | 513 ms: 1.11x slower                                                            |
| sympy_str                  | 274 ms                                                 | 305 ms: 1.11x slower                                                            |
| genshi_text                | 22.9 ms                                                | 26.0 ms: 1.13x slower                                                           |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.15x slower                                                           |
| docutils                   | 2.58 sec                                               | 3.00 sec: 1.16x slower                                                          |
| pylint                     | 313 ms                                                 | 368 ms: 1.18x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.18x slower                                                            |
| genshi_xml                 | 50.3 ms                                                | 59.7 ms: 1.19x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (6): thrift, chaos, json_dumps, bench_mp_pool, bench_thread_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 72.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x