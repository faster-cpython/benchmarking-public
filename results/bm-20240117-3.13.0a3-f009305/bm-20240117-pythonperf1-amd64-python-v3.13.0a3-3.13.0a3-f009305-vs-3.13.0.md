# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.02x slower
- HPT reliability: 99.07%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 210 ms: 1.03x faster                                            |
| chameleon      | 4.72 ms                                                     | 4.91 ms: 1.04x slower                                           |
| docutils       | 1.57 sec                                                    | 1.53 sec: 1.03x faster                                          |
| html5lib       | 38.6 ms                                                     | 35.9 ms: 1.07x faster                                           |
| tornado_http   | 92.8 ms                                                     | 85.5 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 462 ms: 1.41x faster                                            |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.83 sec: 1.12x slower                                          |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 448 ms: 1.16x slower                                            |
| async_tree_none            | 223 ms                                                      | 263 ms: 1.18x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 465 ms: 1.24x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 270 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 724 ms: 1.39x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 750 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.16x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.01x faster                                            |
| float          | 48.1 ms                                                     | 52.5 ms: 1.09x slower                                           |
| nbody          | 64.5 ms                                                     | 74.1 ms: 1.15x slower                                           |
| Geometric mean | (ref)                                                       | 1.08x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 77.7 ms: 1.03x faster                                           |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| regex_v8       | 14.7 ms                                                     | 15.3 ms: 1.04x slower                                           |
| regex_dna      | 114 ms                                                      | 121 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 13.7 us: 1.05x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.54 ms: 1.04x faster                                           |
| unpickle             | 8.63 us                                                     | 8.42 us: 1.03x faster                                           |
| pickle_pure_python   | 183 us                                                      | 179 us: 1.03x faster                                            |
| xml_etree_process    | 36.5 ms                                                     | 36.4 ms: 1.00x faster                                           |
| pickle               | 7.34 us                                                     | 7.31 us: 1.00x faster                                           |
| pickle_dict          | 18.0 us                                                     | 18.2 us: 1.01x slower                                           |
| unpickle_pure_python | 127 us                                                      | 128 us: 1.01x slower                                            |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.5 ms: 1.02x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.39 sec: 1.02x slower                                          |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_list, unpickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 20.1 ms: 1.11x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 21.4 ms: 1.02x faster                                           |
| mako            | 6.24 ms                                                     | 6.57 ms: 1.05x slower                                           |
| genshi_text     | 14.9 ms                                                     | 16.1 ms: 1.08x slower                                           |
| genshi_xml      | 32.8 ms                                                     | 36.0 ms: 1.10x slower                                           |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 100 us                                                      | 70.5 us: 1.43x faster                                           |
| asyncio_tcp                | 654 ms                                                      | 462 ms: 1.41x faster                                            |
| create_gc_cycles           | 829 us                                                      | 732 us: 1.13x faster                                            |
| python_startup             | 22.2 ms                                                     | 20.1 ms: 1.11x faster                                           |
| tornado_http               | 92.8 ms                                                     | 85.5 ms: 1.09x faster                                           |
| pycparser                  | 758 ms                                                      | 701 ms: 1.08x faster                                            |
| html5lib                   | 38.6 ms                                                     | 35.9 ms: 1.07x faster                                           |
| sympy_expand               | 285 ms                                                      | 268 ms: 1.07x faster                                            |
| sympy_str                  | 166 ms                                                      | 156 ms: 1.06x faster                                            |
| coverage                   | 46.7 ms                                                     | 44.3 ms: 1.05x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.7 us: 1.05x faster                                           |
| mypy2                      | 429 ms                                                      | 409 ms: 1.05x faster                                            |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                           |
| sympy_sum                  | 86.4 ms                                                     | 82.6 ms: 1.05x faster                                           |
| bench_mp_pool              | 69.6 ms                                                     | 66.6 ms: 1.05x faster                                           |
| thrift                     | 8.68 ms                                                     | 8.32 ms: 1.04x faster                                           |
| json_dumps                 | 5.76 ms                                                     | 5.54 ms: 1.04x faster                                           |
| aiohttp                    | 932 us                                                      | 896 us: 1.04x faster                                            |
| json                       | 2.98 ms                                                     | 2.88 ms: 1.03x faster                                           |
| 2to3                       | 217 ms                                                      | 210 ms: 1.03x faster                                            |
| regex_compile              | 80.1 ms                                                     | 77.7 ms: 1.03x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.53 sec: 1.03x faster                                          |
| unpickle                   | 8.63 us                                                     | 8.42 us: 1.03x faster                                           |
| gc_traversal               | 1.55 ms                                                     | 1.52 ms: 1.03x faster                                           |
| pickle_pure_python         | 183 us                                                      | 179 us: 1.03x faster                                            |
| pathlib                    | 81.2 ms                                                     | 79.3 ms: 1.02x faster                                           |
| sqlite_synth               | 1.60 us                                                     | 1.57 us: 1.02x faster                                           |
| django_template            | 21.8 ms                                                     | 21.4 ms: 1.02x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| telco                      | 4.85 ms                                                     | 4.77 ms: 1.02x faster                                           |
| scimark_monte_carlo        | 40.3 ms                                                     | 39.9 ms: 1.01x faster                                           |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x faster                                            |
| meteor_contest             | 72.3 ms                                                     | 71.9 ms: 1.00x faster                                           |
| flaskblogging              | 2.04 sec                                                    | 2.03 sec: 1.00x faster                                          |
| xml_etree_process          | 36.5 ms                                                     | 36.4 ms: 1.00x faster                                           |
| pickle                     | 7.34 us                                                     | 7.31 us: 1.00x faster                                           |
| go                         | 84.6 ms                                                     | 84.9 ms: 1.00x slower                                           |
| pickle_dict                | 18.0 us                                                     | 18.2 us: 1.01x slower                                           |
| unpickle_pure_python       | 127 us                                                      | 128 us: 1.01x slower                                            |
| mdp                        | 1.38 sec                                                    | 1.40 sec: 1.01x slower                                          |
| pprint_pformat             | 991 ms                                                      | 1.00 sec: 1.01x slower                                          |
| deepcopy_memo              | 21.8 us                                                     | 22.2 us: 1.01x slower                                           |
| scimark_lu                 | 54.0 ms                                                     | 54.9 ms: 1.02x slower                                           |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| dulwich_log                | 40.4 ms                                                     | 41.1 ms: 1.02x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.5 ms: 1.02x slower                                           |
| scimark_fft                | 174 ms                                                      | 178 ms: 1.02x slower                                            |
| tomli_loads                | 1.36 sec                                                    | 1.39 sec: 1.02x slower                                          |
| sqlglot_normalize          | 171 ms                                                      | 175 ms: 1.02x slower                                            |
| raytrace                   | 156 ms                                                      | 161 ms: 1.03x slower                                            |
| sqlglot_transpile          | 952 us                                                      | 981 us: 1.03x slower                                            |
| hexiom                     | 3.69 ms                                                     | 3.82 ms: 1.03x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                           |
| spectral_norm              | 59.2 ms                                                     | 61.6 ms: 1.04x slower                                           |
| regex_v8                   | 14.7 ms                                                     | 15.3 ms: 1.04x slower                                           |
| chameleon                  | 4.72 ms                                                     | 4.91 ms: 1.04x slower                                           |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                           |
| pyflate                    | 275 ms                                                      | 288 ms: 1.05x slower                                            |
| richards_super             | 29.3 ms                                                     | 30.8 ms: 1.05x slower                                           |
| richards                   | 26.0 ms                                                     | 27.4 ms: 1.05x slower                                           |
| logging_format             | 6.15 us                                                     | 6.47 us: 1.05x slower                                           |
| mako                       | 6.24 ms                                                     | 6.57 ms: 1.05x slower                                           |
| logging_simple             | 5.72 us                                                     | 6.04 us: 1.05x slower                                           |
| deltablue                  | 1.86 ms                                                     | 1.97 ms: 1.06x slower                                           |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.06x slower                                            |
| logging_silent             | 51.0 ns                                                     | 54.1 ns: 1.06x slower                                           |
| nqueens                    | 55.5 ms                                                     | 59.3 ms: 1.07x slower                                           |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.52 ms: 1.08x slower                                           |
| genshi_text                | 14.9 ms                                                     | 16.1 ms: 1.08x slower                                           |
| scimark_sor                | 72.0 ms                                                     | 78.0 ms: 1.08x slower                                           |
| float                      | 48.1 ms                                                     | 52.5 ms: 1.09x slower                                           |
| genshi_xml                 | 32.8 ms                                                     | 36.0 ms: 1.10x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.83 sec: 1.12x slower                                          |
| generators                 | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                           |
| nbody                      | 64.5 ms                                                     | 74.1 ms: 1.15x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 448 ms: 1.16x slower                                            |
| async_tree_none            | 223 ms                                                      | 263 ms: 1.18x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 465 ms: 1.24x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 270 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 724 ms: 1.39x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 750 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (15): pylint, pprint_safe_repr, xml_etree_parse, deepcopy, sqlglot_optimize, sympy_integrate, crypto_pyaes, pickle_list, sqlglot_parse, unpickle_list, comprehensions, fannkuch, xml_etree_generate, python_startup_no_site, bench_thread_pool
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 99.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown