# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.02x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                               |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                             |
| html5lib       | 71.9 ms                                                      | 70.9 ms: 1.01x faster                                              |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.18x faster                                               |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                               |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                               |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                               |
| async_tree_io_tg           | 819 ms                                                       | 774 ms: 1.06x faster                                               |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 569 ms: 1.05x faster                                               |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                               |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                               |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                               |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                              |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                               |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                       |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                              |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                              |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                               |
| regex_dna      | 244 ms                                                       | 237 ms: 1.03x faster                                               |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.18 us: 1.10x faster                                              |
| pickle_dict          | 32.1 us                                                      | 30.3 us: 1.06x faster                                              |
| xml_etree_process    | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                              |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                              |
| xml_etree_generate   | 85.3 ms                                                      | 84.8 ms: 1.01x faster                                              |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                               |
| pickle_pure_python   | 318 us                                                       | 323 us: 1.01x slower                                               |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                               |
| unpickle             | 15.1 us                                                      | 15.5 us: 1.02x slower                                              |
| json_loads           | 24.0 us                                                      | 24.8 us: 1.03x slower                                              |
| unpickle_list        | 4.62 us                                                      | 4.81 us: 1.04x slower                                              |
| tomli_loads          | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                              |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.8 ms: 1.07x faster                                              |
| genshi_xml      | 57.3 ms                                                      | 55.4 ms: 1.04x faster                                              |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.01x slower                                              |
| django_template | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 291 us: 1.36x faster                                               |
| deepcopy_memo              | 39.5 us                                                      | 30.1 us: 1.31x faster                                              |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                              |
| go                         | 160 ms                                                       | 135 ms: 1.19x faster                                               |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.18x faster                                               |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                               |
| generators                 | 33.5 ms                                                      | 28.8 ms: 1.16x faster                                              |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                               |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                               |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                              |
| pickle_list                | 4.59 us                                                      | 4.18 us: 1.10x faster                                              |
| genshi_text                | 26.6 ms                                                      | 24.8 ms: 1.07x faster                                              |
| richards_super             | 59.8 ms                                                      | 55.8 ms: 1.07x faster                                              |
| async_tree_io_tg           | 819 ms                                                       | 774 ms: 1.06x faster                                               |
| pickle_dict                | 32.1 us                                                      | 30.3 us: 1.06x faster                                              |
| richards                   | 52.7 ms                                                      | 50.0 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 569 ms: 1.05x faster                                               |
| raytrace                   | 289 ms                                                       | 275 ms: 1.05x faster                                               |
| regex_v8                   | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                              |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                               |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                               |
| genshi_xml                 | 57.3 ms                                                      | 55.4 ms: 1.04x faster                                              |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                               |
| bpe_tokeniser              | 5.10 sec                                                     | 4.94 sec: 1.03x faster                                             |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                               |
| regex_dna                  | 244 ms                                                       | 237 ms: 1.03x faster                                               |
| unpack_sequence            | 56.8 ns                                                      | 55.2 ns: 1.03x faster                                              |
| float                      | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                              |
| xml_etree_process          | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                               |
| scimark_fft                | 314 ms                                                       | 307 ms: 1.02x faster                                               |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.02x faster                                             |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                              |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                               |
| pyflate                    | 492 ms                                                       | 483 ms: 1.02x faster                                               |
| telco                      | 8.58 ms                                                      | 8.45 ms: 1.02x faster                                              |
| sympy_expand               | 505 ms                                                       | 497 ms: 1.02x faster                                               |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                               |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                               |
| html5lib                   | 71.9 ms                                                      | 70.9 ms: 1.01x faster                                              |
| sqlite_synth               | 2.79 us                                                      | 2.75 us: 1.01x faster                                              |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                               |
| hexiom                     | 6.33 ms                                                      | 6.26 ms: 1.01x faster                                              |
| sympy_integrate            | 23.3 ms                                                      | 23.1 ms: 1.01x faster                                              |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                               |
| sqlglot_optimize           | 59.7 ms                                                      | 59.1 ms: 1.01x faster                                              |
| xml_etree_generate         | 85.3 ms                                                      | 84.8 ms: 1.01x faster                                              |
| mdp                        | 2.52 sec                                                     | 2.51 sec: 1.00x faster                                             |
| pidigits                   | 253 ms                                                       | 253 ms: 1.00x slower                                               |
| python_startup_no_site     | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                              |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                              |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                               |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                               |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                               |
| logging_format             | 7.07 us                                                      | 7.15 us: 1.01x slower                                              |
| chaos                      | 61.7 ms                                                      | 62.5 ms: 1.01x slower                                              |
| pickle_pure_python         | 318 us                                                       | 323 us: 1.01x slower                                               |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.01x slower                                              |
| scimark_lu                 | 97.8 ms                                                      | 99.2 ms: 1.01x slower                                              |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                              |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                               |
| dulwich_log                | 65.5 ms                                                      | 66.5 ms: 1.01x slower                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                              |
| django_template            | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                              |
| unpickle                   | 15.1 us                                                      | 15.5 us: 1.02x slower                                              |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                               |
| comprehensions             | 17.3 us                                                      | 17.7 us: 1.03x slower                                              |
| scimark_sor                | 126 ms                                                       | 129 ms: 1.03x slower                                               |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                               |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.40 ms: 1.03x slower                                              |
| logging_simple             | 6.40 us                                                      | 6.58 us: 1.03x slower                                              |
| json_loads                 | 24.0 us                                                      | 24.8 us: 1.03x slower                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.03x slower                                              |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                             |
| nqueens                    | 88.2 ms                                                      | 91.4 ms: 1.04x slower                                              |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.4 ms: 1.04x slower                                              |
| unpickle_list              | 4.62 us                                                      | 4.81 us: 1.04x slower                                              |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                              |
| coverage                   | 81.1 ms                                                      | 86.1 ms: 1.06x slower                                              |
| tomli_loads                | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                              |
| gc_traversal               | 4.11 ms                                                      | 4.70 ms: 1.14x slower                                              |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                       |

Benchmark hidden because not significant (14): bench_thread_pool, bench_mp_pool, thrift, json_dumps, asyncio_tcp_ssl, fannkuch, json, spectral_norm, deltablue, pprint_safe_repr, xml_etree_parse, crypto_pyaes, pylint, nbody
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x