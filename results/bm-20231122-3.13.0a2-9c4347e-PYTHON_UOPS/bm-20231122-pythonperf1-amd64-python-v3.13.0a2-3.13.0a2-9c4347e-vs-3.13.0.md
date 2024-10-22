# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| chameleon      | 4.72 ms                                                     | 4.84 ms: 1.03x slower                                           |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| tornado_http   | 92.8 ms                                                     | 89.4 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 477 ms: 1.37x faster                                            |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 454 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 267 ms: 1.20x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 363 ms: 1.26x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 346 ms: 1.28x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 481 ms: 1.28x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 281 ms: 1.37x slower                                            |
| async_tree_io              | 521 ms                                                      | 729 ms: 1.40x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 766 ms: 1.50x slower                                            |
| Geometric mean             | (ref)                                                       | 1.17x slower                                                    |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.00x faster                                            |
| float          | 48.1 ms                                                     | 57.1 ms: 1.19x slower                                           |
| nbody          | 64.5 ms                                                     | 81.4 ms: 1.26x slower                                           |
| Geometric mean | (ref)                                                       | 1.14x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                           |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                            |
| regex_compile  | 80.1 ms                                                     | 88.1 ms: 1.10x slower                                           |
| regex_v8       | 14.7 ms                                                     | 17.9 ms: 1.22x slower                                           |
| Geometric mean | (ref)                                                       | 1.08x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle             | 8.63 us                                                     | 8.09 us: 1.07x faster                                           |
| json_loads           | 14.3 us                                                     | 13.4 us: 1.07x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.46 ms: 1.05x faster                                           |
| pickle               | 7.34 us                                                     | 6.96 us: 1.05x faster                                           |
| pickle_pure_python   | 183 us                                                      | 175 us: 1.05x faster                                            |
| unpickle_list        | 2.72 us                                                     | 2.62 us: 1.04x faster                                           |
| xml_etree_process    | 36.5 ms                                                     | 37.6 ms: 1.03x slower                                           |
| pickle_dict          | 18.0 us                                                     | 18.6 us: 1.03x slower                                           |
| xml_etree_generate   | 53.3 ms                                                     | 55.1 ms: 1.03x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.43 sec: 1.05x slower                                          |
| unpickle_pure_python | 127 us                                                      | 136 us: 1.07x slower                                            |
| xml_etree_iterparse  | 62.3 ms                                                     | 67.5 ms: 1.08x slower                                           |
| pickle_list          | 2.89 us                                                     | 3.32 us: 1.15x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 20.7 ms: 1.07x faster                                           |
| python_startup_no_site | 17.8 ms                                                     | 19.6 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.24 ms                                                     | 7.38 ms: 1.18x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 477 ms: 1.37x faster                                            |
| typing_runtime_protocols   | 100 us                                                      | 77.0 us: 1.30x faster                                           |
| create_gc_cycles           | 829 us                                                      | 732 us: 1.13x faster                                            |
| pycparser                  | 758 ms                                                      | 675 ms: 1.12x faster                                            |
| bench_mp_pool              | 69.6 ms                                                     | 64.9 ms: 1.07x faster                                           |
| python_startup             | 22.2 ms                                                     | 20.7 ms: 1.07x faster                                           |
| unpickle                   | 8.63 us                                                     | 8.09 us: 1.07x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.4 us: 1.07x faster                                           |
| json_dumps                 | 5.76 ms                                                     | 5.46 ms: 1.05x faster                                           |
| pickle                     | 7.34 us                                                     | 6.96 us: 1.05x faster                                           |
| pickle_pure_python         | 183 us                                                      | 175 us: 1.05x faster                                            |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.04x faster                                           |
| gc_traversal               | 1.55 ms                                                     | 1.49 ms: 1.04x faster                                           |
| unpickle_list              | 2.72 us                                                     | 2.62 us: 1.04x faster                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                           |
| tornado_http               | 92.8 ms                                                     | 89.4 ms: 1.04x faster                                           |
| pathlib                    | 81.2 ms                                                     | 78.5 ms: 1.03x faster                                           |
| coverage                   | 46.7 ms                                                     | 45.2 ms: 1.03x faster                                           |
| deepcopy                   | 223 us                                                      | 216 us: 1.03x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| sqlite_synth               | 1.60 us                                                     | 1.57 us: 1.02x faster                                           |
| sympy_expand               | 285 ms                                                      | 281 ms: 1.02x faster                                            |
| pidigits                   | 148 ms                                                      | 148 ms: 1.00x faster                                            |
| sympy_str                  | 166 ms                                                      | 168 ms: 1.01x slower                                            |
| sqlglot_parse              | 761 us                                                      | 779 us: 1.02x slower                                            |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                            |
| chameleon                  | 4.72 ms                                                     | 4.84 ms: 1.03x slower                                           |
| richards_super             | 29.3 ms                                                     | 30.1 ms: 1.03x slower                                           |
| xml_etree_process          | 36.5 ms                                                     | 37.6 ms: 1.03x slower                                           |
| sympy_sum                  | 86.4 ms                                                     | 89.1 ms: 1.03x slower                                           |
| pickle_dict                | 18.0 us                                                     | 18.6 us: 1.03x slower                                           |
| xml_etree_generate         | 53.3 ms                                                     | 55.1 ms: 1.03x slower                                           |
| bench_thread_pool          | 828 us                                                      | 858 us: 1.04x slower                                            |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                          |
| richards                   | 26.0 ms                                                     | 27.0 ms: 1.04x slower                                           |
| generators                 | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                           |
| tomli_loads                | 1.36 sec                                                    | 1.43 sec: 1.05x slower                                          |
| deepcopy_memo              | 21.8 us                                                     | 22.9 us: 1.05x slower                                           |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                            |
| sqlglot_optimize           | 33.1 ms                                                     | 34.8 ms: 1.05x slower                                           |
| pprint_safe_repr           | 493 ms                                                      | 519 ms: 1.05x slower                                            |
| sqlglot_transpile          | 952 us                                                      | 1.01 ms: 1.06x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                           |
| dulwich_log                | 40.4 ms                                                     | 42.8 ms: 1.06x slower                                           |
| scimark_lu                 | 54.0 ms                                                     | 57.6 ms: 1.07x slower                                           |
| sqlglot_normalize          | 171 ms                                                      | 183 ms: 1.07x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 77.5 ms: 1.07x slower                                           |
| unpickle_pure_python       | 127 us                                                      | 136 us: 1.07x slower                                            |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                           |
| pprint_pformat             | 991 ms                                                      | 1.07 sec: 1.08x slower                                          |
| xml_etree_iterparse        | 62.3 ms                                                     | 67.5 ms: 1.08x slower                                           |
| logging_silent             | 51.0 ns                                                     | 55.5 ns: 1.09x slower                                           |
| go                         | 84.6 ms                                                     | 92.1 ms: 1.09x slower                                           |
| logging_simple             | 5.72 us                                                     | 6.24 us: 1.09x slower                                           |
| scimark_sor                | 72.0 ms                                                     | 78.6 ms: 1.09x slower                                           |
| logging_format             | 6.15 us                                                     | 6.76 us: 1.10x slower                                           |
| regex_compile              | 80.1 ms                                                     | 88.1 ms: 1.10x slower                                           |
| python_startup_no_site     | 17.8 ms                                                     | 19.6 ms: 1.10x slower                                           |
| fannkuch                   | 245 ms                                                      | 277 ms: 1.13x slower                                            |
| raytrace                   | 156 ms                                                      | 177 ms: 1.14x slower                                            |
| crypto_pyaes               | 42.8 ms                                                     | 49.2 ms: 1.15x slower                                           |
| pickle_list                | 2.89 us                                                     | 3.32 us: 1.15x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 454 ms: 1.17x slower                                            |
| chaos                      | 37.9 ms                                                     | 44.4 ms: 1.17x slower                                           |
| pyflate                    | 275 ms                                                      | 324 ms: 1.17x slower                                            |
| nqueens                    | 55.5 ms                                                     | 65.3 ms: 1.18x slower                                           |
| mako                       | 6.24 ms                                                     | 7.38 ms: 1.18x slower                                           |
| float                      | 48.1 ms                                                     | 57.1 ms: 1.19x slower                                           |
| async_tree_none            | 223 ms                                                      | 267 ms: 1.20x slower                                            |
| regex_v8                   | 14.7 ms                                                     | 17.9 ms: 1.22x slower                                           |
| scimark_fft                | 174 ms                                                      | 213 ms: 1.22x slower                                            |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.4 ms: 1.23x slower                                           |
| comprehensions             | 10.2 us                                                     | 12.9 us: 1.26x slower                                           |
| async_tree_memoization_tg  | 288 ms                                                      | 363 ms: 1.26x slower                                            |
| nbody                      | 64.5 ms                                                     | 81.4 ms: 1.26x slower                                           |
| async_tree_memoization     | 271 ms                                                      | 346 ms: 1.28x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 481 ms: 1.28x slower                                            |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 3.09 ms: 1.32x slower                                           |
| hexiom                     | 3.69 ms                                                     | 5.03 ms: 1.36x slower                                           |
| async_tree_none_tg         | 206 ms                                                      | 281 ms: 1.37x slower                                            |
| mypy2                      | 429 ms                                                      | 589 ms: 1.37x slower                                            |
| async_tree_io              | 521 ms                                                      | 729 ms: 1.40x slower                                            |
| spectral_norm              | 59.2 ms                                                     | 84.1 ms: 1.42x slower                                           |
| deltablue                  | 1.86 ms                                                     | 2.72 ms: 1.46x slower                                           |
| async_tree_io_tg           | 512 ms                                                      | 766 ms: 1.50x slower                                            |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                    |

Benchmark hidden because not significant (5): xml_etree_parse, 2to3, unpack_sequence, asyncio_tcp_ssl, json
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown