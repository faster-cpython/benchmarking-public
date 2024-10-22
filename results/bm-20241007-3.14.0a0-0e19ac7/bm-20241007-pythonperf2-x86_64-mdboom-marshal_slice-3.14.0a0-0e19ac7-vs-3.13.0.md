# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 279 ms: 1.04x faster                                                 |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                               |
| html5lib       | 71.9 ms                                                      | 70.8 ms: 1.02x faster                                                |
| tornado_http   | 120 ms                                                       | 115 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                 |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                 |
| async_tree_memoization     | 452 ms                                                       | 398 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 340 ms                                                       | 305 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                 |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                 |
| async_tree_io_tg           | 819 ms                                                       | 780 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                 |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.04x faster                                                |
| async_generators           | 359 ms                                                       | 353 ms: 1.02x faster                                                 |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                 |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                         |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                         |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                 |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                |
| regex_dna      | 244 ms                                                       | 252 ms: 1.03x slower                                                 |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                        | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 140 ms: 1.04x faster                                                 |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                                 |
| xml_etree_process    | 60.9 ms                                                      | 59.6 ms: 1.02x faster                                                |
| xml_etree_iterparse  | 100 ms                                                       | 98.5 ms: 1.02x faster                                                |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                |
| xml_etree_generate   | 85.3 ms                                                      | 85.1 ms: 1.00x faster                                                |
| pickle_dict          | 32.1 us                                                      | 32.4 us: 1.01x slower                                                |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                 |
| pickle_list          | 4.59 us                                                      | 4.65 us: 1.01x slower                                                |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                                |
| unpickle_list        | 4.62 us                                                      | 4.72 us: 1.02x slower                                                |
| json_loads           | 24.0 us                                                      | 24.6 us: 1.03x slower                                                |
| tomli_loads          | 2.41 sec                                                     | 2.52 sec: 1.05x slower                                               |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                                |
| python_startup         | 13.3 ms                                                      | 13.5 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                |
| genshi_xml     | 57.3 ms                                                      | 52.8 ms: 1.09x faster                                                |
| Geometric mean | (ref)                                                        | 1.05x faster                                                         |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 285 us: 1.39x faster                                                 |
| deepcopy_memo              | 39.5 us                                                      | 29.0 us: 1.36x faster                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.22x faster                                                |
| go                         | 160 ms                                                       | 133 ms: 1.20x faster                                                 |
| generators                 | 33.5 ms                                                      | 28.1 ms: 1.19x faster                                                |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                 |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                 |
| async_tree_memoization     | 452 ms                                                       | 398 ms: 1.13x faster                                                 |
| scimark_sor                | 126 ms                                                       | 111 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 340 ms                                                       | 305 ms: 1.11x faster                                                 |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                |
| scimark_fft                | 314 ms                                                       | 284 ms: 1.10x faster                                                 |
| genshi_text                | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                |
| raytrace                   | 289 ms                                                       | 266 ms: 1.09x faster                                                 |
| genshi_xml                 | 57.3 ms                                                      | 52.8 ms: 1.09x faster                                                |
| telco                      | 8.58 ms                                                      | 7.96 ms: 1.08x faster                                                |
| richards_super             | 59.8 ms                                                      | 55.8 ms: 1.07x faster                                                |
| unpack_sequence            | 56.8 ns                                                      | 53.2 ns: 1.07x faster                                                |
| bpe_tokeniser              | 5.10 sec                                                     | 4.82 sec: 1.06x faster                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                 |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                 |
| scimark_lu                 | 97.8 ms                                                      | 93.1 ms: 1.05x faster                                                |
| async_tree_io_tg           | 819 ms                                                       | 780 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                 |
| 2to3                       | 291 ms                                                       | 279 ms: 1.04x faster                                                 |
| logging_simple             | 6.40 us                                                      | 6.14 us: 1.04x faster                                                |
| float                      | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                                |
| richards                   | 52.7 ms                                                      | 50.8 ms: 1.04x faster                                                |
| xml_etree_parse            | 145 ms                                                       | 140 ms: 1.04x faster                                                 |
| tornado_http               | 120 ms                                                       | 115 ms: 1.04x faster                                                 |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                 |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.04x faster                                                |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                               |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.17 ms: 1.03x faster                                                |
| hexiom                     | 6.33 ms                                                      | 6.16 ms: 1.03x faster                                                |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                                 |
| logging_format             | 7.07 us                                                      | 6.89 us: 1.03x faster                                                |
| typing_runtime_protocols   | 174 us                                                       | 170 us: 1.02x faster                                                 |
| xml_etree_process          | 60.9 ms                                                      | 59.6 ms: 1.02x faster                                                |
| scimark_monte_carlo        | 64.9 ms                                                      | 63.8 ms: 1.02x faster                                                |
| pprint_safe_repr           | 812 ms                                                       | 797 ms: 1.02x faster                                                 |
| async_generators           | 359 ms                                                       | 353 ms: 1.02x faster                                                 |
| fannkuch                   | 365 ms                                                       | 359 ms: 1.02x faster                                                 |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                                 |
| html5lib                   | 71.9 ms                                                      | 70.8 ms: 1.02x faster                                                |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                                |
| sympy_expand               | 505 ms                                                       | 497 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 100 ms                                                       | 98.5 ms: 1.02x faster                                                |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                 |
| thrift                     | 877 us                                                       | 864 us: 1.01x faster                                                 |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                               |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                               |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.01x faster                                                 |
| deltablue                  | 3.41 ms                                                      | 3.38 ms: 1.01x faster                                                |
| pyflate                    | 492 ms                                                       | 488 ms: 1.01x faster                                                 |
| json                       | 5.22 ms                                                      | 5.19 ms: 1.01x faster                                                |
| crypto_pyaes               | 72.8 ms                                                      | 72.3 ms: 1.01x faster                                                |
| spectral_norm              | 97.4 ms                                                      | 96.8 ms: 1.01x faster                                                |
| xml_etree_generate         | 85.3 ms                                                      | 85.1 ms: 1.00x faster                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                                |
| comprehensions             | 17.3 us                                                      | 17.3 us: 1.00x slower                                                |
| python_startup_no_site     | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                                |
| nqueens                    | 88.2 ms                                                      | 89.0 ms: 1.01x slower                                                |
| pickle_dict                | 32.1 us                                                      | 32.4 us: 1.01x slower                                                |
| python_startup             | 13.3 ms                                                      | 13.5 ms: 1.01x slower                                                |
| chaos                      | 61.7 ms                                                      | 62.5 ms: 1.01x slower                                                |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                 |
| pickle_list                | 4.59 us                                                      | 4.65 us: 1.01x slower                                                |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                                |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                 |
| logging_silent             | 97.7 ns                                                      | 99.3 ns: 1.02x slower                                                |
| dulwich_log                | 65.5 ms                                                      | 66.7 ms: 1.02x slower                                                |
| unpickle_list              | 4.62 us                                                      | 4.72 us: 1.02x slower                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                |
| json_loads                 | 24.0 us                                                      | 24.6 us: 1.03x slower                                                |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                |
| coverage                   | 81.1 ms                                                      | 83.6 ms: 1.03x slower                                                |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                               |
| regex_dna                  | 244 ms                                                       | 252 ms: 1.03x slower                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                |
| tomli_loads                | 2.41 sec                                                     | 2.52 sec: 1.05x slower                                               |
| gc_traversal               | 4.11 ms                                                      | 4.53 ms: 1.10x slower                                                |
| create_gc_cycles           | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                                |
| bench_mp_pool              | 4.65 ms                                                      | 1.98 sec: 424.78x slower                                             |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                         |

Benchmark hidden because not significant (9): nbody, bench_thread_pool, mako, unpickle, sympy_integrate, asyncio_tcp_ssl, pylint, pidigits, django_template
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x