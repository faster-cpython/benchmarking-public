# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.01x slower
- HPT reliability: 84.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 292 ms: 1.00x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.28 ms: 1.02x faster                                            |
| docutils       | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| html5lib       | 71.9 ms                                                      | 76.2 ms: 1.06x slower                                            |
| tornado_http   | 120 ms                                                       | 123 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                             |
| async_generators           | 359 ms                                                       | 366 ms: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 697 ms: 1.16x slower                                             |
| async_tree_none            | 372 ms                                                       | 433 ms: 1.16x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 546 ms: 1.18x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 543 ms: 1.20x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 703 ms: 1.22x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.07 sec: 1.27x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 434 ms: 1.28x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.07 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                     |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                            |
| pidigits       | 253 ms                                                       | 262 ms: 1.04x slower                                             |
| nbody          | 88.0 ms                                                      | 91.5 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 237 ms: 1.03x faster                                             |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                            |
| tomli_loads          | 2.41 sec                                                     | 2.29 sec: 1.05x faster                                           |
| pickle_pure_python   | 318 us                                                       | 305 us: 1.04x faster                                             |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                            |
| pickle_dict          | 32.1 us                                                      | 31.0 us: 1.03x faster                                            |
| pickle_list          | 4.59 us                                                      | 4.51 us: 1.02x faster                                            |
| unpickle_pure_python | 214 us                                                       | 211 us: 1.01x faster                                             |
| unpickle_list        | 4.62 us                                                      | 4.56 us: 1.01x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 60.2 ms: 1.01x faster                                            |
| unpickle             | 15.1 us                                                      | 15.3 us: 1.01x slower                                            |
| json_loads           | 24.0 us                                                      | 24.5 us: 1.02x slower                                            |
| xml_etree_generate   | 85.3 ms                                                      | 87.7 ms: 1.03x slower                                            |
| xml_etree_iterparse  | 100 ms                                                       | 105 ms: 1.05x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.7 ms: 1.05x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.1 ms: 1.24x slower                                            |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                            |
| genshi_text     | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                            |
| django_template | 38.9 ms                                                      | 37.7 ms: 1.03x faster                                            |
| mako            | 10.4 ms                                                      | 10.1 ms: 1.03x faster                                            |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 116 us: 1.50x faster                                             |
| mypy2                      | 1.05 sec                                                     | 864 ms: 1.21x faster                                             |
| gc_traversal               | 4.11 ms                                                      | 3.55 ms: 1.16x faster                                            |
| raytrace                   | 289 ms                                                       | 253 ms: 1.14x faster                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.61 ms: 1.09x faster                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.29 us: 1.08x faster                                            |
| deepcopy_memo              | 39.5 us                                                      | 37.0 us: 1.07x faster                                            |
| deepcopy                   | 397 us                                                       | 373 us: 1.06x faster                                             |
| telco                      | 8.58 ms                                                      | 8.09 ms: 1.06x faster                                            |
| json_dumps                 | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.4 ms: 1.05x faster                                            |
| tomli_loads                | 2.41 sec                                                     | 2.29 sec: 1.05x faster                                           |
| python_startup             | 13.3 ms                                                      | 12.7 ms: 1.05x faster                                            |
| genshi_xml                 | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                            |
| pickle_pure_python         | 318 us                                                       | 305 us: 1.04x faster                                             |
| richards_super             | 59.8 ms                                                      | 57.5 ms: 1.04x faster                                            |
| float                      | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                            |
| bench_mp_pool              | 4.65 ms                                                      | 4.49 ms: 1.04x faster                                            |
| genshi_text                | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                            |
| sqlite_synth               | 2.79 us                                                      | 2.69 us: 1.04x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.7 us: 1.04x faster                                            |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.04x faster                                            |
| scimark_lu                 | 97.8 ms                                                      | 94.6 ms: 1.03x faster                                            |
| pickle_dict                | 32.1 us                                                      | 31.0 us: 1.03x faster                                            |
| coverage                   | 81.1 ms                                                      | 78.5 ms: 1.03x faster                                            |
| django_template            | 38.9 ms                                                      | 37.7 ms: 1.03x faster                                            |
| richards                   | 52.7 ms                                                      | 51.2 ms: 1.03x faster                                            |
| mako                       | 10.4 ms                                                      | 10.1 ms: 1.03x faster                                            |
| regex_dna                  | 244 ms                                                       | 237 ms: 1.03x faster                                             |
| logging_silent             | 97.7 ns                                                      | 95.3 ns: 1.02x faster                                            |
| scimark_fft                | 314 ms                                                       | 307 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.20 ms: 1.02x faster                                            |
| chameleon                  | 7.42 ms                                                      | 7.28 ms: 1.02x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.51 us: 1.02x faster                                            |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.02x faster                                             |
| unpickle_pure_python       | 214 us                                                       | 211 us: 1.01x faster                                             |
| unpickle_list              | 4.62 us                                                      | 4.56 us: 1.01x faster                                            |
| pprint_safe_repr           | 812 ms                                                       | 800 ms: 1.01x faster                                             |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                           |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| xml_etree_process          | 60.9 ms                                                      | 60.2 ms: 1.01x faster                                            |
| generators                 | 33.5 ms                                                      | 33.1 ms: 1.01x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                           |
| sympy_str                  | 296 ms                                                       | 293 ms: 1.01x faster                                             |
| chaos                      | 61.7 ms                                                      | 61.1 ms: 1.01x faster                                            |
| sqlglot_optimize           | 59.7 ms                                                      | 59.1 ms: 1.01x faster                                            |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                             |
| regex_v8                   | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                             |
| thrift                     | 877 us                                                       | 870 us: 1.01x faster                                             |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.00x faster                                            |
| crypto_pyaes               | 72.8 ms                                                      | 72.5 ms: 1.00x faster                                            |
| hexiom                     | 6.33 ms                                                      | 6.32 ms: 1.00x faster                                            |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                             |
| 2to3                       | 291 ms                                                       | 292 ms: 1.00x slower                                             |
| nqueens                    | 88.2 ms                                                      | 88.7 ms: 1.00x slower                                            |
| logging_format             | 7.07 us                                                      | 7.11 us: 1.01x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| logging_simple             | 6.40 us                                                      | 6.44 us: 1.01x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| unpickle                   | 15.1 us                                                      | 15.3 us: 1.01x slower                                            |
| flaskblogging              | 4.62 ms                                                      | 4.66 ms: 1.01x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                            |
| async_generators           | 359 ms                                                       | 366 ms: 1.02x slower                                             |
| json_loads                 | 24.0 us                                                      | 24.5 us: 1.02x slower                                            |
| aiohttp                    | 1.07 ms                                                      | 1.09 ms: 1.02x slower                                            |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                            |
| tornado_http               | 120 ms                                                       | 123 ms: 1.02x slower                                             |
| xml_etree_generate         | 85.3 ms                                                      | 87.7 ms: 1.03x slower                                            |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| pyflate                    | 492 ms                                                       | 509 ms: 1.03x slower                                             |
| pidigits                   | 253 ms                                                       | 262 ms: 1.04x slower                                             |
| go                         | 160 ms                                                       | 167 ms: 1.04x slower                                             |
| nbody                      | 88.0 ms                                                      | 91.5 ms: 1.04x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.31 sec: 1.04x slower                                           |
| deltablue                  | 3.41 ms                                                      | 3.56 ms: 1.05x slower                                            |
| dask                       | 379 ms                                                       | 397 ms: 1.05x slower                                             |
| dulwich_log                | 65.5 ms                                                      | 68.8 ms: 1.05x slower                                            |
| xml_etree_iterparse        | 100 ms                                                       | 105 ms: 1.05x slower                                             |
| html5lib                   | 71.9 ms                                                      | 76.2 ms: 1.06x slower                                            |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                            |
| pathlib                    | 17.4 ms                                                      | 18.9 ms: 1.08x slower                                            |
| scimark_monte_carlo        | 64.9 ms                                                      | 70.6 ms: 1.09x slower                                            |
| bench_thread_pool          | 901 us                                                       | 979 us: 1.09x slower                                             |
| fannkuch                   | 365 ms                                                       | 406 ms: 1.11x slower                                             |
| scimark_sor                | 126 ms                                                       | 143 ms: 1.13x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 697 ms: 1.16x slower                                             |
| async_tree_none            | 372 ms                                                       | 433 ms: 1.16x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 546 ms: 1.18x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 543 ms: 1.20x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 703 ms: 1.22x slower                                             |
| python_startup_no_site     | 8.94 ms                                                      | 11.1 ms: 1.24x slower                                            |
| async_tree_io              | 847 ms                                                       | 1.07 sec: 1.27x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 434 ms: 1.28x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.07 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (6): pylint, sympy_expand, asyncio_tcp_ssl, xml_etree_parse, gunicorn, asyncio_websockets
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 84.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x