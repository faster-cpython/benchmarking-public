# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                            |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 907 ms: 1.27x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.3 ms: 1.11x faster                                                           |
| float          | 84.7 ms                                                | 77.9 ms: 1.09x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                            |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 907 ms: 1.27x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                           |
| raytrace                   | 312 ms                                                 | 256 ms: 1.22x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                           |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.19x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                           |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 73.5 ms: 1.11x faster                                                           |
| nbody                      | 97.0 ms                                                | 87.3 ms: 1.11x faster                                                           |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                           |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                            |
| float                      | 84.7 ms                                                | 77.9 ms: 1.09x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.08x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 786 us: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                           |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                           |
| scimark_fft                | 382 ms                                                 | 361 ms: 1.06x faster                                                            |
| nqueens                    | 83.3 ms                                                | 78.8 ms: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 746 ms: 1.04x faster                                                            |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                          |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 486 ms: 1.01x faster                                                            |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                           |
| richards                   | 45.8 ms                                                | 45.4 ms: 1.01x faster                                                           |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                                           |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.01x slower                                                          |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.02x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                            |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.14 ms: 1.15x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (6): logging_silent, xml_etree_parse, regex_effbot, go, bench_mp_pool, coroutines
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x