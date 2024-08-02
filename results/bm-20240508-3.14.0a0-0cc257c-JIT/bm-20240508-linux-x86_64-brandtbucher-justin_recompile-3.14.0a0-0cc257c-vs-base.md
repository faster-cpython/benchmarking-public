# Results vs. base

- fork: brandtbucher
- ref: justin_recompile
- machine: linux-x86_64
- commit hash: 0cc257c
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 302 ms: 1.08x slower                                                    |
| chameleon      | 7.20 ms                                                               | 7.11 ms: 1.01x faster                                                   |
| docutils       | 2.96 sec                                                              | 3.83 sec: 1.29x slower                                                  |
| html5lib       | 70.7 ms                                                               | 75.0 ms: 1.06x slower                                                   |
| tornado_http   | 98.4 ms                                                               | 99.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.02 sec                                                              | 1.21 sec: 1.19x slower                                                  |
| async_tree_cpu_io_mixed    | 632 ms                                                                | 754 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed_tg | 595 ms                                                                | 718 ms: 1.21x slower                                                    |
| async_tree_io              | 933 ms                                                                | 1.18 sec: 1.26x slower                                                  |
| async_tree_memoization     | 482 ms                                                                | 618 ms: 1.28x slower                                                    |
| async_tree_memoization_tg  | 453 ms                                                                | 588 ms: 1.30x slower                                                    |
| async_tree_none            | 370 ms                                                                | 489 ms: 1.32x slower                                                    |
| async_tree_none_tg         | 345 ms                                                                | 467 ms: 1.36x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 81.0 ms: 1.04x faster                                                   |
| float          | 71.1 ms                                                               | 89.8 ms: 1.26x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 224 ms: 1.02x faster                                                    |
| regex_v8       | 25.3 ms                                                               | 25.8 ms: 1.02x slower                                                   |
| regex_effbot   | 3.68 ms                                                               | 3.85 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 15.8 us                                                               | 15.2 us: 1.04x faster                                                   |
| pickle_list         | 5.56 us                                                               | 5.46 us: 1.02x faster                                                   |
| pickle_dict         | 34.7 us                                                               | 34.2 us: 1.02x faster                                                   |
| pickle              | 12.1 us                                                               | 12.0 us: 1.01x faster                                                   |
| json_loads          | 28.9 us                                                               | 28.7 us: 1.01x faster                                                   |
| json_dumps          | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                   |
| unpickle_list       | 5.21 us                                                               | 5.26 us: 1.01x slower                                                   |
| tomli_loads         | 1.98 sec                                                              | 2.02 sec: 1.02x slower                                                  |
| xml_etree_generate  | 83.2 ms                                                               | 93.2 ms: 1.12x slower                                                   |
| xml_etree_process   | 58.9 ms                                                               | 66.2 ms: 1.12x slower                                                   |
| xml_etree_parse     | 151 ms                                                                | 174 ms: 1.15x slower                                                    |
| xml_etree_iterparse | 102 ms                                                                | 140 ms: 1.37x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                                   |
| python_startup_no_site | 7.67 ms                                                               | 7.68 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 37.1 ms                                                               | 36.4 ms: 1.02x faster                                                   |
| mako            | 9.67 ms                                                               | 9.72 ms: 1.01x slower                                                   |
| genshi_xml      | 59.9 ms                                                               | 61.3 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody                      | 84.0 ms                                                               | 81.0 ms: 1.04x faster                                                   |
| pyflate                    | 460 ms                                                                | 444 ms: 1.04x faster                                                    |
| unpickle                   | 15.8 us                                                               | 15.2 us: 1.04x faster                                                   |
| pprint_safe_repr           | 739 ms                                                                | 714 ms: 1.03x faster                                                    |
| pickle_list                | 5.56 us                                                               | 5.46 us: 1.02x faster                                                   |
| django_template            | 37.1 ms                                                               | 36.4 ms: 1.02x faster                                                   |
| crypto_pyaes               | 68.9 ms                                                               | 67.6 ms: 1.02x faster                                                   |
| dulwich_log                | 70.7 ms                                                               | 69.4 ms: 1.02x faster                                                   |
| pickle_dict                | 34.7 us                                                               | 34.2 us: 1.02x faster                                                   |
| pprint_pformat             | 1.50 sec                                                              | 1.48 sec: 1.02x faster                                                  |
| regex_dna                  | 228 ms                                                                | 224 ms: 1.02x faster                                                    |
| logging_silent             | 109 ns                                                                | 107 ns: 1.01x faster                                                    |
| logging_simple             | 5.85 us                                                               | 5.77 us: 1.01x faster                                                   |
| chameleon                  | 7.20 ms                                                               | 7.11 ms: 1.01x faster                                                   |
| logging_format             | 6.53 us                                                               | 6.45 us: 1.01x faster                                                   |
| coroutines                 | 23.3 ms                                                               | 23.0 ms: 1.01x faster                                                   |
| typing_runtime_protocols   | 177 us                                                                | 175 us: 1.01x faster                                                    |
| telco                      | 172 ms                                                                | 170 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult    | 4.58 ms                                                               | 4.54 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 64.6 ms                                                               | 64.1 ms: 1.01x faster                                                   |
| pickle                     | 12.1 us                                                               | 12.0 us: 1.01x faster                                                   |
| scimark_sor                | 130 ms                                                                | 129 ms: 1.01x faster                                                    |
| json_loads                 | 28.9 us                                                               | 28.7 us: 1.01x faster                                                   |
| sqlglot_normalize          | 116 ms                                                                | 115 ms: 1.01x faster                                                    |
| meteor_contest             | 110 ms                                                                | 109 ms: 1.01x faster                                                    |
| generators                 | 30.0 ms                                                               | 29.9 ms: 1.01x faster                                                   |
| asyncio_websockets         | 567 ms                                                                | 564 ms: 1.01x faster                                                    |
| bench_thread_pool          | 874 us                                                                | 871 us: 1.00x faster                                                    |
| python_startup             | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                                   |
| python_startup_no_site     | 7.67 ms                                                               | 7.68 ms: 1.00x slower                                                   |
| comprehensions             | 16.8 us                                                               | 16.8 us: 1.00x slower                                                   |
| sympy_str                  | 302 ms                                                                | 304 ms: 1.01x slower                                                    |
| deepcopy_memo              | 37.5 us                                                               | 37.7 us: 1.01x slower                                                   |
| mako                       | 9.67 ms                                                               | 9.72 ms: 1.01x slower                                                   |
| sympy_integrate            | 22.7 ms                                                               | 22.8 ms: 1.01x slower                                                   |
| deepcopy                   | 371 us                                                                | 374 us: 1.01x slower                                                    |
| pathlib                    | 17.8 ms                                                               | 17.9 ms: 1.01x slower                                                   |
| json_dumps                 | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                   |
| raytrace                   | 278 ms                                                                | 280 ms: 1.01x slower                                                    |
| unpickle_list              | 5.21 us                                                               | 5.26 us: 1.01x slower                                                   |
| richards                   | 43.6 ms                                                               | 44.0 ms: 1.01x slower                                                   |
| tornado_http               | 98.4 ms                                                               | 99.4 ms: 1.01x slower                                                   |
| deepcopy_reduce            | 3.35 us                                                               | 3.39 us: 1.01x slower                                                   |
| scimark_lu                 | 123 ms                                                                | 125 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 58.0 ms                                                               | 58.8 ms: 1.01x slower                                                   |
| gunicorn                   | 1.36 ms                                                               | 1.38 ms: 1.01x slower                                                   |
| coverage                   | 88.2 ms                                                               | 89.6 ms: 1.02x slower                                                   |
| tomli_loads                | 1.98 sec                                                              | 2.02 sec: 1.02x slower                                                  |
| richards_super             | 49.5 ms                                                               | 50.5 ms: 1.02x slower                                                   |
| asyncio_tcp                | 505 ms                                                                | 515 ms: 1.02x slower                                                    |
| genshi_xml                 | 59.9 ms                                                               | 61.3 ms: 1.02x slower                                                   |
| regex_v8                   | 25.3 ms                                                               | 25.8 ms: 1.02x slower                                                   |
| aiohttp                    | 1.25 ms                                                               | 1.28 ms: 1.02x slower                                                   |
| go                         | 146 ms                                                                | 151 ms: 1.03x slower                                                    |
| async_generators           | 471 ms                                                                | 488 ms: 1.04x slower                                                    |
| regex_effbot               | 3.68 ms                                                               | 3.85 ms: 1.04x slower                                                   |
| deltablue                  | 3.82 ms                                                               | 3.99 ms: 1.05x slower                                                   |
| pycparser                  | 1.20 sec                                                              | 1.26 sec: 1.06x slower                                                  |
| sqlglot_transpile          | 1.64 ms                                                               | 1.74 ms: 1.06x slower                                                   |
| html5lib                   | 70.7 ms                                                               | 75.0 ms: 1.06x slower                                                   |
| sqlglot_parse              | 1.31 ms                                                               | 1.40 ms: 1.06x slower                                                   |
| mdp                        | 2.60 sec                                                              | 2.80 sec: 1.08x slower                                                  |
| 2to3                       | 280 ms                                                                | 302 ms: 1.08x slower                                                    |
| gc_traversal               | 3.94 ms                                                               | 4.32 ms: 1.09x slower                                                   |
| xml_etree_generate         | 83.2 ms                                                               | 93.2 ms: 1.12x slower                                                   |
| flaskblogging              | 9.30 ms                                                               | 10.4 ms: 1.12x slower                                                   |
| xml_etree_process          | 58.9 ms                                                               | 66.2 ms: 1.12x slower                                                   |
| xml_etree_parse            | 151 ms                                                                | 174 ms: 1.15x slower                                                    |
| pylint                     | 358 ms                                                                | 415 ms: 1.16x slower                                                    |
| dask                       | 380 ms                                                                | 449 ms: 1.18x slower                                                    |
| async_tree_io_tg           | 1.02 sec                                                              | 1.21 sec: 1.19x slower                                                  |
| async_tree_cpu_io_mixed    | 632 ms                                                                | 754 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed_tg | 595 ms                                                                | 718 ms: 1.21x slower                                                    |
| create_gc_cycles           | 1.83 ms                                                               | 2.23 ms: 1.21x slower                                                   |
| async_tree_io              | 933 ms                                                                | 1.18 sec: 1.26x slower                                                  |
| float                      | 71.1 ms                                                               | 89.8 ms: 1.26x slower                                                   |
| async_tree_memoization     | 482 ms                                                                | 618 ms: 1.28x slower                                                    |
| docutils                   | 2.96 sec                                                              | 3.83 sec: 1.29x slower                                                  |
| async_tree_memoization_tg  | 453 ms                                                                | 588 ms: 1.30x slower                                                    |
| async_tree_none            | 370 ms                                                                | 489 ms: 1.32x slower                                                    |
| async_tree_none_tg         | 345 ms                                                                | 467 ms: 1.36x slower                                                    |
| xml_etree_iterparse        | 102 ms                                                                | 140 ms: 1.37x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (18): spectral_norm, pickle_pure_python, chaos, sqlite_synth, json, pidigits, sympy_expand, nqueens, asyncio_tcp_ssl, scimark_fft, sympy_sum, regex_compile, hexiom, unpickle_pure_python, bench_mp_pool, fannkuch, genshi_text, thrift

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x