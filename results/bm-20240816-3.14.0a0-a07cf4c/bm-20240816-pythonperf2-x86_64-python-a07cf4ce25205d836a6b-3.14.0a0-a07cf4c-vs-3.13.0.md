# Results vs. 3.13.0

- fork: python
- ref: a07cf4ce25205d836a6b
- machine: linux-x86_64
- commit hash: a07cf4c
- commit date: 2024-08-16
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 73.5 ms: 1.02x slower                                                       |
| tornado_http   | 120 ms                                                       | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 774 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 812 ms: 1.04x faster                                                        |
| async_generators           | 359 ms                                                       | 353 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| asyncio_websockets         | 382 ms                                                       | 385 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 81.6 ms: 1.00x faster                                                       |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| regex_dna      | 244 ms                                                       | 239 ms: 1.02x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.64 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.22 sec: 1.09x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.2 ms: 1.01x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.02x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.0 ms: 1.06x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 55.3 ms: 1.04x faster                                                       |
| mako            | 10.4 ms                                                      | 10.2 ms: 1.02x faster                                                       |
| django_template | 38.9 ms                                                      | 39.4 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 293 us: 1.35x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.3 us: 1.30x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.99 us: 1.19x faster                                                       |
| generators                 | 33.5 ms                                                      | 28.7 ms: 1.16x faster                                                       |
| scimark_sor                | 126 ms                                                       | 109 ms: 1.15x faster                                                        |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.22 sec: 1.09x faster                                                      |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                       |
| raytrace                   | 289 ms                                                       | 269 ms: 1.07x faster                                                        |
| richards_super             | 59.8 ms                                                      | 55.9 ms: 1.07x faster                                                       |
| richards                   | 52.7 ms                                                      | 49.3 ms: 1.07x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.07 ms: 1.06x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.0 ms: 1.06x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 774 ms: 1.06x faster                                                        |
| scimark_fft                | 314 ms                                                       | 297 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 812 ms: 1.04x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 866 us: 1.04x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 94.1 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.13 ms: 1.04x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 55.3 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.93 sec: 1.03x faster                                                      |
| logging_format             | 7.07 us                                                      | 6.85 us: 1.03x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.24 us: 1.02x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| tornado_http               | 120 ms                                                       | 117 ms: 1.02x faster                                                        |
| regex_dna                  | 244 ms                                                       | 239 ms: 1.02x faster                                                        |
| async_generators           | 359 ms                                                       | 353 ms: 1.02x faster                                                        |
| mako                       | 10.4 ms                                                      | 10.2 ms: 1.02x faster                                                       |
| fannkuch                   | 365 ms                                                       | 359 ms: 1.02x faster                                                        |
| pyflate                    | 492 ms                                                       | 485 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.01x faster                                                        |
| thrift                     | 877 us                                                       | 864 us: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                                       |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 84.2 ms: 1.01x faster                                                       |
| logging_silent             | 97.7 ns                                                      | 96.5 ns: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.01x faster                                                      |
| hexiom                     | 6.33 ms                                                      | 6.30 ms: 1.01x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 72.4 ms: 1.00x faster                                                       |
| float                      | 81.9 ms                                                      | 81.6 ms: 1.00x faster                                                       |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                                       |
| chaos                      | 61.7 ms                                                      | 62.0 ms: 1.01x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 60.1 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 385 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.4 ms: 1.01x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.9 ms: 1.02x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                                       |
| go                         | 160 ms                                                       | 164 ms: 1.02x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 73.5 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.02x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.6 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| json                       | 5.22 ms                                                      | 5.37 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 841 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 123 ms: 1.04x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.73 sec: 1.05x slower                                                      |
| coverage                   | 81.1 ms                                                      | 85.5 ms: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.64 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.95 ms: 1.11x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.68 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (11): pickle_pure_python, deltablue, sympy_integrate, asyncio_tcp_ssl, sympy_expand, mdp, bench_mp_pool, sympy_str, xml_etree_iterparse, pylint, nbody
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x