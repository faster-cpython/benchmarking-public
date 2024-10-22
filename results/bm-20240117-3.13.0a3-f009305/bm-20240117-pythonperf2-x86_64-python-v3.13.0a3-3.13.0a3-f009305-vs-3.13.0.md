# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.01x slower
- HPT reliability: 94.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 294 ms: 1.01x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.26 ms: 1.02x faster                                            |
| docutils       | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| html5lib       | 71.9 ms                                                      | 73.9 ms: 1.03x slower                                            |
| tornado_http   | 120 ms                                                       | 118 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.03x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.01x faster                                           |
| async_generators           | 359 ms                                                       | 368 ms: 1.02x slower                                             |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 701 ms: 1.17x slower                                             |
| async_tree_none            | 372 ms                                                       | 435 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 545 ms: 1.18x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 547 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 701 ms: 1.22x slower                                             |
| async_tree_none_tg         | 340 ms                                                       | 430 ms: 1.27x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.08 sec: 1.27x slower                                           |
| async_tree_io_tg           | 819 ms                                                       | 1.07 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.0 ms: 1.05x faster                                            |
| nbody          | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                            |
| pidigits       | 253 ms                                                       | 263 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.03x faster                                             |
| regex_dna      | 244 ms                                                       | 238 ms: 1.02x faster                                             |
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.23 sec: 1.08x faster                                           |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.04x faster                                            |
| pickle_pure_python   | 318 us                                                       | 307 us: 1.04x faster                                             |
| xml_etree_process    | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                            |
| pickle_list          | 4.59 us                                                      | 4.49 us: 1.02x faster                                            |
| pickle               | 10.5 us                                                      | 10.4 us: 1.02x faster                                            |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                             |
| xml_etree_generate   | 85.3 ms                                                      | 85.6 ms: 1.00x slower                                            |
| pickle_dict          | 32.1 us                                                      | 32.5 us: 1.01x slower                                            |
| unpickle             | 15.1 us                                                      | 15.4 us: 1.02x slower                                            |
| xml_etree_parse      | 145 ms                                                       | 150 ms: 1.03x slower                                             |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                            |
| unpickle_list        | 4.62 us                                                      | 4.82 us: 1.04x slower                                            |
| xml_etree_iterparse  | 100 ms                                                       | 107 ms: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.6 ms: 1.06x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.0 ms: 1.23x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.7 ms: 1.03x faster                                            |
| genshi_xml      | 57.3 ms                                                      | 55.6 ms: 1.03x faster                                            |
| django_template | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 113 us: 1.54x faster                                             |
| mypy2                      | 1.05 sec                                                     | 864 ms: 1.21x faster                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.57 ms: 1.12x faster                                            |
| raytrace                   | 289 ms                                                       | 265 ms: 1.09x faster                                             |
| deepcopy                   | 397 us                                                       | 367 us: 1.08x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 3.28 us: 1.08x faster                                            |
| tomli_loads                | 2.41 sec                                                     | 2.23 sec: 1.08x faster                                           |
| deepcopy_memo              | 39.5 us                                                      | 37.1 us: 1.06x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.6 ms: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.3 ms: 1.05x faster                                            |
| float                      | 81.9 ms                                                      | 78.0 ms: 1.05x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.5 us: 1.04x faster                                            |
| gc_traversal               | 4.11 ms                                                      | 3.94 ms: 1.04x faster                                            |
| telco                      | 8.58 ms                                                      | 8.23 ms: 1.04x faster                                            |
| scimark_fft                | 314 ms                                                       | 302 ms: 1.04x faster                                             |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.04x faster                                            |
| pickle_pure_python         | 318 us                                                       | 307 us: 1.04x faster                                             |
| xml_etree_process          | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                            |
| genshi_text                | 26.6 ms                                                      | 25.7 ms: 1.03x faster                                            |
| genshi_xml                 | 57.3 ms                                                      | 55.6 ms: 1.03x faster                                            |
| nbody                      | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                            |
| chaos                      | 61.7 ms                                                      | 59.9 ms: 1.03x faster                                            |
| regex_compile              | 144 ms                                                       | 141 ms: 1.03x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.03x faster                                             |
| sqlglot_normalize          | 118 ms                                                       | 116 ms: 1.02x faster                                             |
| regex_dna                  | 244 ms                                                       | 238 ms: 1.02x faster                                             |
| chameleon                  | 7.42 ms                                                      | 7.26 ms: 1.02x faster                                            |
| sympy_expand               | 505 ms                                                       | 494 ms: 1.02x faster                                             |
| pickle_list                | 4.59 us                                                      | 4.49 us: 1.02x faster                                            |
| crypto_pyaes               | 72.8 ms                                                      | 71.4 ms: 1.02x faster                                            |
| tornado_http               | 120 ms                                                       | 118 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.21 ms: 1.02x faster                                            |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.02x faster                                            |
| logging_silent             | 97.7 ns                                                      | 96.0 ns: 1.02x faster                                            |
| django_template            | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                            |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                           |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                             |
| regex_v8                   | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| sympy_str                  | 296 ms                                                       | 294 ms: 1.01x faster                                             |
| richards_super             | 59.8 ms                                                      | 59.4 ms: 1.01x faster                                            |
| thrift                     | 877 us                                                       | 872 us: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.01x faster                                           |
| xml_etree_generate         | 85.3 ms                                                      | 85.6 ms: 1.00x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                           |
| docutils                   | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| gunicorn                   | 1.04 ms                                                      | 1.05 ms: 1.01x slower                                            |
| json                       | 5.22 ms                                                      | 5.27 ms: 1.01x slower                                            |
| generators                 | 33.5 ms                                                      | 33.8 ms: 1.01x slower                                            |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                             |
| nqueens                    | 88.2 ms                                                      | 89.1 ms: 1.01x slower                                            |
| 2to3                       | 291 ms                                                       | 294 ms: 1.01x slower                                             |
| pickle_dict                | 32.1 us                                                      | 32.5 us: 1.01x slower                                            |
| unpickle                   | 15.1 us                                                      | 15.4 us: 1.02x slower                                            |
| pyflate                    | 492 ms                                                       | 501 ms: 1.02x slower                                             |
| richards                   | 52.7 ms                                                      | 53.7 ms: 1.02x slower                                            |
| hexiom                     | 6.33 ms                                                      | 6.46 ms: 1.02x slower                                            |
| coverage                   | 81.1 ms                                                      | 82.9 ms: 1.02x slower                                            |
| async_generators           | 359 ms                                                       | 368 ms: 1.02x slower                                             |
| html5lib                   | 71.9 ms                                                      | 73.9 ms: 1.03x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| logging_format             | 7.07 us                                                      | 7.31 us: 1.03x slower                                            |
| go                         | 160 ms                                                       | 166 ms: 1.03x slower                                             |
| xml_etree_parse            | 145 ms                                                       | 150 ms: 1.03x slower                                             |
| deltablue                  | 3.41 ms                                                      | 3.54 ms: 1.04x slower                                            |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                            |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 68.2 ms: 1.04x slower                                            |
| logging_simple             | 6.40 us                                                      | 6.66 us: 1.04x slower                                            |
| unpickle_list              | 4.62 us                                                      | 4.82 us: 1.04x slower                                            |
| pidigits                   | 253 ms                                                       | 263 ms: 1.04x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.9 ms: 1.05x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.32 sec: 1.05x slower                                           |
| fannkuch                   | 365 ms                                                       | 386 ms: 1.06x slower                                             |
| xml_etree_iterparse        | 100 ms                                                       | 107 ms: 1.07x slower                                             |
| bench_thread_pool          | 901 us                                                       | 960 us: 1.07x slower                                             |
| pathlib                    | 17.4 ms                                                      | 18.9 ms: 1.08x slower                                            |
| scimark_sor                | 126 ms                                                       | 144 ms: 1.15x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 701 ms: 1.17x slower                                             |
| async_tree_none            | 372 ms                                                       | 435 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 545 ms: 1.18x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 547 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 701 ms: 1.22x slower                                             |
| python_startup_no_site     | 8.94 ms                                                      | 11.0 ms: 1.23x slower                                            |
| async_tree_none_tg         | 340 ms                                                       | 430 ms: 1.27x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.08 sec: 1.27x slower                                           |
| async_tree_io_tg           | 819 ms                                                       | 1.07 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (10): bench_mp_pool, pylint, mako, sqlite_synth, aiohttp, flaskblogging, sympy_sum, sympy_integrate, scimark_lu, pprint_safe_repr
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence

# HPT report

- Reliability score: 94.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x