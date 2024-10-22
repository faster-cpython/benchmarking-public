# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 289 ms: 1.01x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.96 sec: 1.05x slower                                                      |
| html5lib       | 71.9 ms                                                      | 74.0 ms: 1.03x slower                                                       |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 383 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 776 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 811 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 579 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 367 ms: 1.02x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.6 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna      | 244 ms                                                       | 240 ms: 1.02x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.52 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.25 sec: 1.07x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.6 ms: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                        |
| xml_etree_parse      | 145 ms                                                       | 146 ms: 1.01x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 104 ms: 1.04x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.0 ms: 1.07x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 38.3 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 284 us: 1.40x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.8 us: 1.33x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 383 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.2 ms: 1.08x faster                                                       |
| raytrace                   | 289 ms                                                       | 269 ms: 1.07x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.25 sec: 1.07x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.0 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 776 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| async_tree_io              | 847 ms                                                       | 811 ms: 1.04x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.25 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 579 ms: 1.04x faster                                                        |
| coverage                   | 81.1 ms                                                      | 78.4 ms: 1.03x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 873 us: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                                        |
| richards                   | 52.7 ms                                                      | 51.5 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| richards_super             | 59.8 ms                                                      | 58.5 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| sympy_expand               | 505 ms                                                       | 496 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 171 us: 1.02x faster                                                        |
| float                      | 81.9 ms                                                      | 80.6 ms: 1.02x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 95.8 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.02x faster                                                        |
| django_template            | 38.9 ms                                                      | 38.3 ms: 1.02x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.7 ms: 1.02x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| sqlglot_optimize           | 59.7 ms                                                      | 58.9 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                                       |
| sympy_str                  | 296 ms                                                       | 292 ms: 1.01x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.27 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 5.05 sec: 1.01x faster                                                      |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.6 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| nqueens                    | 88.2 ms                                                      | 87.7 ms: 1.01x faster                                                       |
| 2to3                       | 291 ms                                                       | 289 ms: 1.01x faster                                                        |
| pyflate                    | 492 ms                                                       | 490 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| scimark_fft                | 314 ms                                                       | 315 ms: 1.00x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 98.4 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                        |
| xml_etree_parse            | 145 ms                                                       | 146 ms: 1.01x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                      |
| fannkuch                   | 365 ms                                                       | 368 ms: 1.01x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 66.2 ms: 1.01x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 98.8 ns: 1.01x slower                                                       |
| dask                       | 379 ms                                                       | 386 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| async_generators           | 359 ms                                                       | 367 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.38 ms: 1.02x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.50 ms: 1.03x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 74.0 ms: 1.03x slower                                                       |
| go                         | 160 ms                                                       | 166 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.5 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 104 ms: 1.04x slower                                                        |
| scimark_sor                | 126 ms                                                       | 131 ms: 1.04x slower                                                        |
| json                       | 5.22 ms                                                      | 5.47 ms: 1.05x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.52 ms: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.96 sec: 1.05x slower                                                      |
| json_loads                 | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.46 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (15): pylint, chaos, logging_format, sympy_sum, regex_v8, sqlglot_transpile, pidigits, logging_simple, sqlglot_normalize, pprint_safe_repr, generators, nbody, thrift, mako, bench_mp_pool
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x