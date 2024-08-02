# Results vs. 3.13.0b2

- fork: python
- ref: d9efa45d7457b0dfea46
- machine: linux-x86_64
- commit hash: d9efa45
- commit date: 2024-07-25
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                |
| html5lib       | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 399 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 527 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| float          | 78.9 ms                                                    | 78.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.3 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                 |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.9 us: 1.33x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.62 us: 1.28x faster                                                 |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 399 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                  |
| richards                   | 50.9 ms                                                    | 45.1 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                  |
| richards_super             | 57.4 ms                                                    | 51.2 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 527 ms: 1.11x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.09x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.1 ms: 1.07x faster                                                 |
| scimark_fft                | 392 ms                                                     | 366 ms: 1.07x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.94 ms: 1.07x faster                                                 |
| thrift                     | 823 us                                                     | 773 us: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 784 us: 1.06x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.05x faster                                                  |
| generators                 | 29.6 ms                                                    | 28.1 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.45 us: 1.05x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                                 |
| logging_silent             | 105 ns                                                     | 99.6 ns: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                 |
| dask                       | 369 ms                                                     | 354 ms: 1.04x faster                                                  |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                 |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                 |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                  |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                |
| docutils                   | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                 |
| raytrace                   | 267 ms                                                     | 257 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                                 |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.85 sec: 1.04x faster                                                |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                 |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 739 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 85.3 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                  |
| async_generators           | 442 ms                                                     | 432 ms: 1.02x faster                                                  |
| sympy_expand               | 473 ms                                                     | 462 ms: 1.02x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 79.7 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.7 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| django_template            | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.21 ms: 1.01x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                 |
| float                      | 78.9 ms                                                    | 78.0 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                 |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| fannkuch                   | 402 ms                                                     | 406 ms: 1.01x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (9): coverage, regex_dna, pyflate, scimark_sor, pylint, genshi_xml, nbody, pycparser, genshi_text
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x