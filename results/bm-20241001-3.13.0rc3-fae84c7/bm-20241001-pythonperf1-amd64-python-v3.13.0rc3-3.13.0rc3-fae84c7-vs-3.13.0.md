# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: windows-amd64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.01x slower
- HPT reliability: 99.61%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| chameleon      | 4.72 ms                                                     | 4.89 ms: 1.04x slower                                             |
| docutils       | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                            |
| html5lib       | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 517 ms: 1.26x faster                                              |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.47 sec: 1.11x faster                                            |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 374 ms: 1.04x faster                                              |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                              |
| async_tree_none_tg         | 206 ms                                                      | 203 ms: 1.01x faster                                              |
| async_tree_none            | 223 ms                                                      | 220 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 370 ms: 1.01x faster                                              |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                      |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                              |
| float          | 48.1 ms                                                     | 50.3 ms: 1.05x slower                                             |
| nbody          | 64.5 ms                                                     | 71.0 ms: 1.10x slower                                             |
| Geometric mean | (ref)                                                       | 1.05x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                             |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                              |
| regex_compile  | 80.1 ms                                                     | 83.8 ms: 1.05x slower                                             |
| regex_v8       | 14.7 ms                                                     | 17.1 ms: 1.17x slower                                             |
| Geometric mean | (ref)                                                       | 1.05x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 90.9 ms: 1.03x faster                                             |
| unpickle_list        | 2.72 us                                                     | 2.66 us: 1.02x faster                                             |
| json_loads           | 14.3 us                                                     | 14.0 us: 1.02x faster                                             |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.1 ms: 1.02x faster                                             |
| unpickle             | 8.63 us                                                     | 8.49 us: 1.02x faster                                             |
| pickle               | 7.34 us                                                     | 7.21 us: 1.02x faster                                             |
| xml_etree_generate   | 53.3 ms                                                     | 53.0 ms: 1.01x faster                                             |
| tomli_loads          | 1.36 sec                                                    | 1.39 sec: 1.02x slower                                            |
| unpickle_pure_python | 127 us                                                      | 130 us: 1.03x slower                                              |
| pickle_dict          | 18.0 us                                                     | 18.8 us: 1.04x slower                                             |
| pickle_list          | 2.89 us                                                     | 3.11 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                      |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 22.1 ms: 1.01x slower                                             |
| genshi_text     | 14.9 ms                                                     | 15.5 ms: 1.04x slower                                             |
| genshi_xml      | 32.8 ms                                                     | 34.3 ms: 1.05x slower                                             |
| mako            | 6.24 ms                                                     | 6.68 ms: 1.07x slower                                             |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 517 ms: 1.26x faster                                              |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.47 sec: 1.11x faster                                            |
| unpack_sequence            | 40.0 ns                                                     | 37.8 ns: 1.06x faster                                             |
| bench_thread_pool          | 828 us                                                      | 786 us: 1.05x faster                                              |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 374 ms: 1.04x faster                                              |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                             |
| create_gc_cycles           | 829 us                                                      | 807 us: 1.03x faster                                              |
| xml_etree_parse            | 93.2 ms                                                     | 90.9 ms: 1.03x faster                                             |
| unpickle_list              | 2.72 us                                                     | 2.66 us: 1.02x faster                                             |
| pathlib                    | 81.2 ms                                                     | 79.3 ms: 1.02x faster                                             |
| json_loads                 | 14.3 us                                                     | 14.0 us: 1.02x faster                                             |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.1 ms: 1.02x faster                                             |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                              |
| unpickle                   | 8.63 us                                                     | 8.49 us: 1.02x faster                                             |
| coverage                   | 46.7 ms                                                     | 45.9 ms: 1.02x faster                                             |
| pickle                     | 7.34 us                                                     | 7.21 us: 1.02x faster                                             |
| mdp                        | 1.38 sec                                                    | 1.36 sec: 1.02x faster                                            |
| async_tree_none_tg         | 206 ms                                                      | 203 ms: 1.01x faster                                              |
| async_tree_none            | 223 ms                                                      | 220 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 370 ms: 1.01x faster                                              |
| docutils                   | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                            |
| logging_format             | 6.15 us                                                     | 6.11 us: 1.01x faster                                             |
| xml_etree_generate         | 53.3 ms                                                     | 53.0 ms: 1.01x faster                                             |
| gc_traversal               | 1.55 ms                                                     | 1.55 ms: 1.01x faster                                             |
| flaskblogging              | 2.04 sec                                                    | 2.03 sec: 1.00x faster                                            |
| fannkuch                   | 245 ms                                                      | 246 ms: 1.01x slower                                              |
| sympy_str                  | 166 ms                                                      | 167 ms: 1.01x slower                                              |
| go                         | 84.6 ms                                                     | 85.4 ms: 1.01x slower                                             |
| scimark_fft                | 174 ms                                                      | 176 ms: 1.01x slower                                              |
| deepcopy                   | 223 us                                                      | 226 us: 1.01x slower                                              |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                              |
| pprint_pformat             | 991 ms                                                      | 1.00 sec: 1.01x slower                                            |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                             |
| richards                   | 26.0 ms                                                     | 26.4 ms: 1.01x slower                                             |
| sqlglot_optimize           | 33.1 ms                                                     | 33.5 ms: 1.01x slower                                             |
| typing_runtime_protocols   | 100 us                                                      | 102 us: 1.01x slower                                              |
| django_template            | 21.8 ms                                                     | 22.1 ms: 1.01x slower                                             |
| richards_super             | 29.3 ms                                                     | 29.8 ms: 1.02x slower                                             |
| aiohttp                    | 932 us                                                      | 950 us: 1.02x slower                                              |
| tomli_loads                | 1.36 sec                                                    | 1.39 sec: 1.02x slower                                            |
| pyflate                    | 275 ms                                                      | 281 ms: 1.02x slower                                              |
| scimark_monte_carlo        | 40.3 ms                                                     | 41.1 ms: 1.02x slower                                             |
| deltablue                  | 1.86 ms                                                     | 1.90 ms: 1.02x slower                                             |
| comprehensions             | 10.2 us                                                     | 10.5 us: 1.02x slower                                             |
| meteor_contest             | 72.3 ms                                                     | 73.9 ms: 1.02x slower                                             |
| sqlglot_normalize          | 171 ms                                                      | 175 ms: 1.02x slower                                              |
| dulwich_log                | 40.4 ms                                                     | 41.4 ms: 1.03x slower                                             |
| nqueens                    | 55.5 ms                                                     | 56.9 ms: 1.03x slower                                             |
| unpickle_pure_python       | 127 us                                                      | 130 us: 1.03x slower                                              |
| sqlglot_transpile          | 952 us                                                      | 980 us: 1.03x slower                                              |
| generators                 | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                             |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                              |
| sqlglot_parse              | 761 us                                                      | 789 us: 1.04x slower                                              |
| chameleon                  | 4.72 ms                                                     | 4.89 ms: 1.04x slower                                             |
| spectral_norm              | 59.2 ms                                                     | 61.5 ms: 1.04x slower                                             |
| html5lib                   | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                             |
| genshi_text                | 14.9 ms                                                     | 15.5 ms: 1.04x slower                                             |
| logging_silent             | 51.0 ns                                                     | 53.2 ns: 1.04x slower                                             |
| hexiom                     | 3.69 ms                                                     | 3.85 ms: 1.04x slower                                             |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                             |
| pickle_dict                | 18.0 us                                                     | 18.8 us: 1.04x slower                                             |
| deepcopy_memo              | 21.8 us                                                     | 22.8 us: 1.04x slower                                             |
| regex_compile              | 80.1 ms                                                     | 83.8 ms: 1.05x slower                                             |
| float                      | 48.1 ms                                                     | 50.3 ms: 1.05x slower                                             |
| genshi_xml                 | 32.8 ms                                                     | 34.3 ms: 1.05x slower                                             |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                             |
| raytrace                   | 156 ms                                                      | 165 ms: 1.06x slower                                              |
| scimark_lu                 | 54.0 ms                                                     | 57.2 ms: 1.06x slower                                             |
| crypto_pyaes               | 42.8 ms                                                     | 45.7 ms: 1.07x slower                                             |
| scimark_sor                | 72.0 ms                                                     | 76.9 ms: 1.07x slower                                             |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.50 ms: 1.07x slower                                             |
| mako                       | 6.24 ms                                                     | 6.68 ms: 1.07x slower                                             |
| pickle_list                | 2.89 us                                                     | 3.11 us: 1.07x slower                                             |
| nbody                      | 64.5 ms                                                     | 71.0 ms: 1.10x slower                                             |
| regex_v8                   | 14.7 ms                                                     | 17.1 ms: 1.17x slower                                             |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (23): pylint, async_tree_io_tg, async_tree_io, tornado_http, async_tree_memoization_tg, async_tree_memoization, logging_simple, bench_mp_pool, 2to3, pprint_safe_repr, sympy_expand, deepcopy_reduce, pickle_pure_python, pycparser, json, thrift, sqlite_synth, xml_etree_process, json_dumps, mypy2, sympy_sum, python_startup_no_site, python_startup

# HPT report

- Reliability score: 99.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown