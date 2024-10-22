# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.0 ms: 1.03x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 385 ms: 1.20x faster                                                        |
| async_tree_none            | 372 ms                                                       | 317 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 395 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 569 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.04x faster                                                        |
| async_generators           | 359 ms                                                       | 355 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.00x faster                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.1 ms: 1.02x faster                                                       |
| nbody          | 88.0 ms                                                      | 86.4 ms: 1.02x faster                                                       |
| pidigits       | 253 ms                                                       | 255 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| regex_dna      | 244 ms                                                       | 238 ms: 1.02x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python  | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_process   | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| json_dumps          | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| xml_etree_generate  | 85.3 ms                                                      | 85.1 ms: 1.00x faster                                                       |
| xml_etree_iterparse | 100 ms                                                       | 101 ms: 1.01x slower                                                        |
| json_loads          | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| tomli_loads         | 2.41 sec                                                     | 2.55 sec: 1.06x slower                                                      |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 55.5 ms: 1.03x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 26.0 ms: 1.02x faster                                                       |
| django_template | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 280 us: 1.42x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.0 us: 1.36x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.88 us: 1.23x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 385 ms: 1.20x faster                                                        |
| go                         | 160 ms                                                       | 135 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 317 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.6 ms: 1.17x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 395 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.37 ms: 1.06x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.3 ms: 1.06x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.68 us: 1.06x faster                                                       |
| raytrace                   | 289 ms                                                       | 273 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| scimark_sor                | 126 ms                                                       | 119 ms: 1.06x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 853 us: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 569 ms: 1.05x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.2 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.20 sec: 1.05x faster                                                      |
| bpe_tokeniser              | 5.10 sec                                                     | 4.88 sec: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.11 ms: 1.04x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.27 ms: 1.04x faster                                                       |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                        |
| scimark_fft                | 314 ms                                                       | 303 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 55.5 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 70.0 ms: 1.03x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.23 us: 1.03x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 95.4 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.03x faster                                                        |
| regex_dna                  | 244 ms                                                       | 238 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.3 ms: 1.02x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 26.0 ms: 1.02x faster                                                       |
| float                      | 81.9 ms                                                      | 80.1 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 95.4 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.4 ms: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                      |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| async_generators           | 359 ms                                                       | 355 ms: 1.01x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.26 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 499 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| fannkuch                   | 365 ms                                                       | 362 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.00x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 85.1 ms: 1.00x faster                                                       |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.00x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| pidigits                   | 253 ms                                                       | 255 ms: 1.01x slower                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 73.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                        |
| pyflate                    | 492 ms                                                       | 497 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.9 ms: 1.02x slower                                                       |
| json                       | 5.22 ms                                                      | 5.31 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| django_template            | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 90.4 ms: 1.02x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| json_loads                 | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| coverage                   | 81.1 ms                                                      | 85.2 ms: 1.05x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.55 sec: 1.06x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.44 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (10): thrift, unpickle_pure_python, asyncio_tcp_ssl, sqlglot_transpile, deltablue, chaos, comprehensions, mako, pylint, xml_etree_parse
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x