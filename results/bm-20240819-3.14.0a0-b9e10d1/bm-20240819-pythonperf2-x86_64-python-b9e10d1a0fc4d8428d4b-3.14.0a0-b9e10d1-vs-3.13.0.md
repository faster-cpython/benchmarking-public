# Results vs. 3.13.0

- fork: python
- ref: b9e10d1a0fc4d8428d4b
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 284 ms: 1.02x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.5 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 402 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 334 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 762 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| float          | 81.9 ms                                                      | 80.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_dna      | 244 ms                                                       | 238 ms: 1.02x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.64 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|--------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads        | 2.41 sec                                                     | 2.29 sec: 1.05x faster                                                      |
| xml_etree_process  | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                                       |
| xml_etree_parse    | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| json_dumps         | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| xml_etree_generate | 85.3 ms                                                      | 84.3 ms: 1.01x faster                                                       |
| pickle_pure_python | 318 us                                                       | 315 us: 1.01x faster                                                        |
| json_loads         | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| Geometric mean     | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 25.0 ms: 1.07x faster                                                       |
| django_template | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 288 us: 1.38x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.4 us: 1.34x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.23x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.1 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 402 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 334 ms: 1.12x faster                                                        |
| scimark_sor                | 126 ms                                                       | 115 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                       |
| raytrace                   | 289 ms                                                       | 265 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 762 ms: 1.07x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.0 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.06x faster                                                        |
| pyflate                    | 492 ms                                                       | 464 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.8 ms: 1.05x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.29 sec: 1.05x faster                                                      |
| coverage                   | 81.1 ms                                                      | 77.3 ms: 1.05x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.19 ms: 1.05x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 860 us: 1.05x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.77 us: 1.05x faster                                                       |
| richards                   | 52.7 ms                                                      | 50.4 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.18 us: 1.04x faster                                                       |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| scimark_fft                | 314 ms                                                       | 305 ms: 1.03x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.96 sec: 1.03x faster                                                      |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| regex_dna                  | 244 ms                                                       | 238 ms: 1.02x faster                                                        |
| 2to3                       | 291 ms                                                       | 284 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.8 ms: 1.02x faster                                                       |
| go                         | 160 ms                                                       | 157 ms: 1.02x faster                                                        |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.35 ms: 1.02x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| float                      | 81.9 ms                                                      | 80.8 ms: 1.01x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.3 ms: 1.01x faster                                                       |
| django_template            | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                        |
| thrift                     | 877 us                                                       | 867 us: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 59.1 ms: 1.01x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 72.0 ms: 1.01x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| sympy_str                  | 296 ms                                                       | 293 ms: 1.01x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.25 sec: 1.01x faster                                                      |
| sympy_expand               | 505 ms                                                       | 500 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                                       |
| chaos                      | 61.7 ms                                                      | 61.3 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.00x faster                                                       |
| logging_silent             | 97.7 ns                                                      | 97.3 ns: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 72.5 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 820 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.31 ms: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.7 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.0 ms: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.64 ms: 1.08x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.47 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (11): bench_mp_pool, mako, xml_etree_iterparse, sqlglot_transpile, pidigits, pylint, sympy_sum, hexiom, unpickle_pure_python, typing_runtime_protocols, scimark_sparse_mat_mult
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x