# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.01x faster
- HPT reliability: 93.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 309 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 805 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 397 ms: 1.04x slower                                                        |
| async_generators           | 359 ms                                                       | 386 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 78.7 ms: 1.12x faster                                                       |
| float          | 81.9 ms                                                      | 74.2 ms: 1.10x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 237 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.8 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.61 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                      |
| xml_etree_process   | 60.9 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| pickle_list         | 4.59 us                                                      | 4.22 us: 1.09x faster                                                       |
| xml_etree_generate  | 85.3 ms                                                      | 78.5 ms: 1.09x faster                                                       |
| pickle_dict         | 32.1 us                                                      | 30.7 us: 1.04x faster                                                       |
| xml_etree_iterparse | 100 ms                                                       | 97.4 ms: 1.03x faster                                                       |
| xml_etree_parse     | 145 ms                                                       | 142 ms: 1.02x faster                                                        |
| pickle              | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| json_dumps          | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| unpickle_list       | 4.62 us                                                      | 4.69 us: 1.01x slower                                                       |
| json_loads          | 24.0 us                                                      | 24.5 us: 1.02x slower                                                       |
| pickle_pure_python  | 318 us                                                       | 326 us: 1.02x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.93 ms: 1.00x faster                                                       |
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.18 ms: 1.13x faster                                                       |
| django_template | 38.9 ms                                                      | 41.6 ms: 1.07x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 29.3 ms: 1.10x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 66.1 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 26.5 us: 1.49x faster                                                       |
| deepcopy                   | 397 us                                                       | 292 us: 1.36x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                       |
| scimark_sor                | 126 ms                                                       | 103 ms: 1.22x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                        |
| richards                   | 52.7 ms                                                      | 44.7 ms: 1.18x faster                                                       |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                      |
| richards_super             | 59.8 ms                                                      | 52.4 ms: 1.14x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.18 ms: 1.13x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| nbody                      | 88.0 ms                                                      | 78.7 ms: 1.12x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| float                      | 81.9 ms                                                      | 74.2 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.22 us: 1.09x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 78.5 ms: 1.09x faster                                                       |
| scimark_fft                | 314 ms                                                       | 290 ms: 1.08x faster                                                        |
| pyflate                    | 492 ms                                                       | 454 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.76 sec: 1.07x faster                                                      |
| go                         | 160 ms                                                       | 150 ms: 1.07x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.08 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.23 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.06 ms: 1.05x faster                                                       |
| async_tree_io              | 847 ms                                                       | 805 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 69.7 ms: 1.04x faster                                                       |
| pickle_dict                | 32.1 us                                                      | 30.7 us: 1.04x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 783 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.71 us: 1.03x faster                                                       |
| regex_dna                  | 244 ms                                                       | 237 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 97.4 ms: 1.03x faster                                                       |
| coverage                   | 81.1 ms                                                      | 79.4 ms: 1.02x faster                                                       |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.8 ms: 1.02x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                      |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.3 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 8.93 ms: 1.00x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| thrift                     | 877 us                                                       | 885 us: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| unpickle_list              | 4.62 us                                                      | 4.69 us: 1.01x slower                                                       |
| logging_format             | 7.07 us                                                      | 7.20 us: 1.02x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.53 us: 1.02x slower                                                       |
| json_loads                 | 24.0 us                                                      | 24.5 us: 1.02x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 922 us: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.61 sec: 1.03x slower                                                      |
| pycparser                  | 1.26 sec                                                     | 1.30 sec: 1.03x slower                                                      |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 397 ms: 1.04x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 101 ns: 1.04x slower                                                        |
| sympy_expand               | 505 ms                                                       | 525 ms: 1.04x slower                                                        |
| sympy_str                  | 296 ms                                                       | 308 ms: 1.04x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.36 ms: 1.06x slower                                                       |
| chaos                      | 61.7 ms                                                      | 65.6 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                       | 309 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 186 us: 1.07x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.61 ms: 1.07x slower                                                       |
| django_template            | 38.9 ms                                                      | 41.6 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.07x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 5.00 ms: 1.07x slower                                                       |
| async_generators           | 359 ms                                                       | 386 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 128 ms: 1.08x slower                                                        |
| raytrace                   | 289 ms                                                       | 313 ms: 1.08x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 167 ms: 1.08x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.93 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 65.0 ms: 1.09x slower                                                       |
| generators                 | 33.5 ms                                                      | 36.5 ms: 1.09x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.95 ms: 1.10x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 97.0 ms: 1.10x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 29.3 ms: 1.10x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| sympy_integrate            | 23.3 ms                                                      | 26.3 ms: 1.13x slower                                                       |
| genshi_xml                 | 57.3 ms                                                      | 66.1 ms: 1.15x slower                                                       |
| pylint                     | 346 ms                                                       | 408 ms: 1.18x slower                                                        |
| unpack_sequence            | 56.8 ns                                                      | 87.7 ns: 1.54x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (7): json, scimark_lu, unpickle_pure_python, async_tree_io_tg, asyncio_tcp_ssl, unpickle, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 93.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x