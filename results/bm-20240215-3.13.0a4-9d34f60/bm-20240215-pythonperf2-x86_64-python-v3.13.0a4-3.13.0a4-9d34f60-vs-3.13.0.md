# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x slower
- HPT reliability: 86.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 292 ms: 1.00x slower                                             |
| docutils       | 2.81 sec                                                     | 2.84 sec: 1.01x slower                                           |
| html5lib       | 71.9 ms                                                      | 76.0 ms: 1.06x slower                                            |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                           |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 699 ms: 1.16x slower                                             |
| async_tree_none            | 372 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 551 ms: 1.19x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 546 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 705 ms: 1.23x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.08 sec: 1.27x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 434 ms: 1.28x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                     |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                            |
| nbody          | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                            |
| pidigits       | 253 ms                                                       | 262 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                             |
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                             |
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| regex_effbot   | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.33 us: 1.06x faster                                            |
| pickle_dict          | 32.1 us                                                      | 30.3 us: 1.06x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 57.7 ms: 1.05x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.5 ms: 1.05x faster                                            |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| tomli_loads          | 2.41 sec                                                     | 2.38 sec: 1.01x faster                                           |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                             |
| xml_etree_generate   | 85.3 ms                                                      | 85.1 ms: 1.00x faster                                            |
| unpickle             | 15.1 us                                                      | 15.3 us: 1.01x slower                                            |
| unpickle_list        | 4.62 us                                                      | 4.68 us: 1.01x slower                                            |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                             |
| xml_etree_parse      | 145 ms                                                       | 148 ms: 1.02x slower                                             |
| xml_etree_iterparse  | 100 ms                                                       | 105 ms: 1.05x slower                                             |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.6 ms: 1.06x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.0 ms: 1.23x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                            |
| genshi_xml      | 57.3 ms                                                      | 55.8 ms: 1.03x faster                                            |
| django_template | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 117 us: 1.49x faster                                             |
| mypy2                      | 1.05 sec                                                     | 867 ms: 1.21x faster                                             |
| raytrace                   | 289 ms                                                       | 262 ms: 1.10x faster                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.61 ms: 1.10x faster                                            |
| gc_traversal               | 4.11 ms                                                      | 3.76 ms: 1.09x faster                                            |
| deepcopy                   | 397 us                                                       | 369 us: 1.08x faster                                             |
| deepcopy_memo              | 39.5 us                                                      | 37.2 us: 1.06x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.33 us: 1.06x faster                                            |
| pickle_dict                | 32.1 us                                                      | 30.3 us: 1.06x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.6 ms: 1.06x faster                                            |
| xml_etree_process          | 60.9 ms                                                      | 57.7 ms: 1.05x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.5 ms: 1.05x faster                                            |
| telco                      | 8.58 ms                                                      | 8.16 ms: 1.05x faster                                            |
| json_dumps                 | 11.0 ms                                                      | 10.5 ms: 1.05x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.5 us: 1.05x faster                                            |
| scimark_fft                | 314 ms                                                       | 301 ms: 1.04x faster                                             |
| logging_silent             | 97.7 ns                                                      | 93.6 ns: 1.04x faster                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.12 ms: 1.04x faster                                            |
| float                      | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.41 us: 1.04x faster                                            |
| nbody                      | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                            |
| scimark_lu                 | 97.8 ms                                                      | 94.4 ms: 1.04x faster                                            |
| sqlglot_normalize          | 118 ms                                                       | 115 ms: 1.03x faster                                             |
| genshi_text                | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                            |
| genshi_xml                 | 57.3 ms                                                      | 55.8 ms: 1.03x faster                                            |
| pprint_safe_repr           | 812 ms                                                       | 791 ms: 1.03x faster                                             |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                             |
| sqlite_synth               | 2.79 us                                                      | 2.73 us: 1.02x faster                                            |
| crypto_pyaes               | 72.8 ms                                                      | 71.3 ms: 1.02x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                           |
| sqlglot_optimize           | 59.7 ms                                                      | 58.6 ms: 1.02x faster                                            |
| sympy_expand               | 505 ms                                                       | 496 ms: 1.02x faster                                             |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                             |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                             |
| django_template            | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                           |
| chaos                      | 61.7 ms                                                      | 61.0 ms: 1.01x faster                                            |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                             |
| tomli_loads                | 2.41 sec                                                     | 2.38 sec: 1.01x faster                                           |
| regex_v8                   | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                             |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                             |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                           |
| xml_etree_generate         | 85.3 ms                                                      | 85.1 ms: 1.00x faster                                            |
| 2to3                       | 291 ms                                                       | 292 ms: 1.00x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| nqueens                    | 88.2 ms                                                      | 88.8 ms: 1.01x slower                                            |
| unpickle                   | 15.1 us                                                      | 15.3 us: 1.01x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                            |
| unpickle_list              | 4.62 us                                                      | 4.68 us: 1.01x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.84 sec: 1.01x slower                                           |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                             |
| json                       | 5.22 ms                                                      | 5.30 ms: 1.01x slower                                            |
| hexiom                     | 6.33 ms                                                      | 6.44 ms: 1.02x slower                                            |
| richards_super             | 59.8 ms                                                      | 60.8 ms: 1.02x slower                                            |
| logging_format             | 7.07 us                                                      | 7.21 us: 1.02x slower                                            |
| generators                 | 33.5 ms                                                      | 34.1 ms: 1.02x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.28 sec: 1.02x slower                                           |
| coverage                   | 81.1 ms                                                      | 82.9 ms: 1.02x slower                                            |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                             |
| xml_etree_parse            | 145 ms                                                       | 148 ms: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| pyflate                    | 492 ms                                                       | 506 ms: 1.03x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.0 ms: 1.03x slower                                            |
| richards                   | 52.7 ms                                                      | 54.4 ms: 1.03x slower                                            |
| regex_effbot               | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                            |
| logging_simple             | 6.40 us                                                      | 6.63 us: 1.04x slower                                            |
| pidigits                   | 253 ms                                                       | 262 ms: 1.04x slower                                             |
| xml_etree_iterparse        | 100 ms                                                       | 105 ms: 1.05x slower                                             |
| dulwich_log                | 65.5 ms                                                      | 69.0 ms: 1.05x slower                                            |
| deltablue                  | 3.41 ms                                                      | 3.59 ms: 1.05x slower                                            |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.05x slower                                            |
| html5lib                   | 71.9 ms                                                      | 76.0 ms: 1.06x slower                                            |
| go                         | 160 ms                                                       | 170 ms: 1.06x slower                                             |
| bench_thread_pool          | 901 us                                                       | 958 us: 1.06x slower                                             |
| fannkuch                   | 365 ms                                                       | 393 ms: 1.08x slower                                             |
| pathlib                    | 17.4 ms                                                      | 19.0 ms: 1.09x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 699 ms: 1.16x slower                                             |
| scimark_sor                | 126 ms                                                       | 146 ms: 1.17x slower                                             |
| async_tree_none            | 372 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 551 ms: 1.19x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 546 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 705 ms: 1.23x slower                                             |
| python_startup_no_site     | 8.94 ms                                                      | 11.0 ms: 1.23x slower                                            |
| async_tree_io              | 847 ms                                                       | 1.08 sec: 1.27x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 434 ms: 1.28x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (10): bench_mp_pool, flaskblogging, mako, pylint, thrift, aiohttp, chameleon, async_generators, gunicorn, asyncio_websockets
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence

# HPT report

- Reliability score: 86.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x