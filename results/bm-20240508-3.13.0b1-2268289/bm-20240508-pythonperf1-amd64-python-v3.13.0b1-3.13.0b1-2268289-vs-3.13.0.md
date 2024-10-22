# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: windows-amd64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.01x faster
- HPT reliability: 90.13%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 212 ms: 1.02x faster                                            |
| chameleon      | 4.72 ms                                                     | 4.75 ms: 1.01x slower                                           |
| docutils       | 1.57 sec                                                    | 1.64 sec: 1.04x slower                                          |
| html5lib       | 38.6 ms                                                     | 35.0 ms: 1.10x faster                                           |
| tornado_http   | 92.8 ms                                                     | 82.5 ms: 1.13x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 482 ms: 1.36x faster                                            |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.51 sec: 1.08x faster                                          |
| async_tree_memoization_tg | 288 ms                                                      | 267 ms: 1.08x faster                                            |
| async_tree_none           | 223 ms                                                      | 219 ms: 1.02x faster                                            |
| async_generators          | 223 ms                                                      | 225 ms: 1.01x slower                                            |
| coroutines                | 12.5 ms                                                     | 12.6 ms: 1.01x slower                                           |
| async_tree_none_tg        | 206 ms                                                      | 213 ms: 1.03x slower                                            |
| async_tree_io             | 521 ms                                                      | 582 ms: 1.12x slower                                            |
| async_tree_io_tg          | 512 ms                                                      | 604 ms: 1.18x slower                                            |
| Geometric mean            | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| nbody          | 64.5 ms                                                     | 67.1 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                           |
| regex_v8       | 14.7 ms                                                     | 14.3 ms: 1.02x faster                                           |
| regex_compile  | 80.1 ms                                                     | 78.5 ms: 1.02x faster                                           |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads         | 14.3 us                                                     | 13.7 us: 1.04x faster                                           |
| pickle_pure_python | 183 us                                                      | 177 us: 1.04x faster                                            |
| xml_etree_parse    | 93.2 ms                                                     | 90.0 ms: 1.04x faster                                           |
| json_dumps         | 5.76 ms                                                     | 5.59 ms: 1.03x faster                                           |
| unpickle           | 8.63 us                                                     | 8.44 us: 1.02x faster                                           |
| pickle             | 7.34 us                                                     | 7.17 us: 1.02x faster                                           |
| xml_etree_generate | 53.3 ms                                                     | 53.7 ms: 1.01x slower                                           |
| xml_etree_process  | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                           |
| tomli_loads        | 1.36 sec                                                    | 1.37 sec: 1.01x slower                                          |
| unpickle_list      | 2.72 us                                                     | 2.77 us: 1.02x slower                                           |
| pickle_dict        | 18.0 us                                                     | 18.4 us: 1.02x slower                                           |
| pickle_list        | 2.89 us                                                     | 3.02 us: 1.05x slower                                           |
| Geometric mean     | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 20.4 ms: 1.09x faster                                           |
| python_startup_no_site | 17.8 ms                                                     | 16.5 ms: 1.08x faster                                           |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 21.5 ms: 1.01x faster                                           |
| genshi_text     | 14.9 ms                                                     | 14.7 ms: 1.01x faster                                           |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 482 ms: 1.36x faster                                            |
| pycparser                 | 758 ms                                                      | 669 ms: 1.13x faster                                            |
| tornado_http              | 92.8 ms                                                     | 82.5 ms: 1.13x faster                                           |
| html5lib                  | 38.6 ms                                                     | 35.0 ms: 1.10x faster                                           |
| python_startup            | 22.2 ms                                                     | 20.4 ms: 1.09x faster                                           |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.51 sec: 1.08x faster                                          |
| python_startup_no_site    | 17.8 ms                                                     | 16.5 ms: 1.08x faster                                           |
| async_tree_memoization_tg | 288 ms                                                      | 267 ms: 1.08x faster                                            |
| bench_mp_pool             | 69.6 ms                                                     | 65.3 ms: 1.07x faster                                           |
| thrift                    | 8.68 ms                                                     | 8.23 ms: 1.05x faster                                           |
| mdp                       | 1.38 sec                                                    | 1.31 sec: 1.05x faster                                          |
| generators                | 19.5 ms                                                     | 18.6 ms: 1.05x faster                                           |
| bench_thread_pool         | 828 us                                                      | 793 us: 1.04x faster                                            |
| json_loads                | 14.3 us                                                     | 13.7 us: 1.04x faster                                           |
| sympy_expand              | 285 ms                                                      | 275 ms: 1.04x faster                                            |
| pickle_pure_python        | 183 us                                                      | 177 us: 1.04x faster                                            |
| xml_etree_parse           | 93.2 ms                                                     | 90.0 ms: 1.04x faster                                           |
| coverage                  | 46.7 ms                                                     | 45.3 ms: 1.03x faster                                           |
| json_dumps                | 5.76 ms                                                     | 5.59 ms: 1.03x faster                                           |
| telco                     | 4.85 ms                                                     | 4.72 ms: 1.03x faster                                           |
| aiohttp                   | 932 us                                                      | 908 us: 1.03x faster                                            |
| regex_effbot              | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                           |
| sympy_str                 | 166 ms                                                      | 162 ms: 1.02x faster                                            |
| regex_v8                  | 14.7 ms                                                     | 14.3 ms: 1.02x faster                                           |
| pprint_safe_repr          | 493 ms                                                      | 481 ms: 1.02x faster                                            |
| 2to3                      | 217 ms                                                      | 212 ms: 1.02x faster                                            |
| unpickle                  | 8.63 us                                                     | 8.44 us: 1.02x faster                                           |
| pickle                    | 7.34 us                                                     | 7.17 us: 1.02x faster                                           |
| regex_compile             | 80.1 ms                                                     | 78.5 ms: 1.02x faster                                           |
| deepcopy_reduce           | 2.02 us                                                     | 1.98 us: 1.02x faster                                           |
| json                      | 2.98 ms                                                     | 2.93 ms: 1.02x faster                                           |
| dulwich_log               | 40.4 ms                                                     | 39.6 ms: 1.02x faster                                           |
| async_tree_none           | 223 ms                                                      | 219 ms: 1.02x faster                                            |
| raytrace                  | 156 ms                                                      | 154 ms: 1.02x faster                                            |
| django_template           | 21.8 ms                                                     | 21.5 ms: 1.01x faster                                           |
| sympy_sum                 | 86.4 ms                                                     | 85.2 ms: 1.01x faster                                           |
| meteor_contest            | 72.3 ms                                                     | 71.3 ms: 1.01x faster                                           |
| pathlib                   | 81.2 ms                                                     | 80.1 ms: 1.01x faster                                           |
| pidigits                  | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| pprint_pformat            | 991 ms                                                      | 982 ms: 1.01x faster                                            |
| sqlglot_parse             | 761 us                                                      | 754 us: 1.01x faster                                            |
| genshi_text               | 14.9 ms                                                     | 14.7 ms: 1.01x faster                                           |
| flaskblogging             | 2.04 sec                                                    | 2.03 sec: 1.01x faster                                          |
| sqlglot_optimize          | 33.1 ms                                                     | 32.9 ms: 1.01x faster                                           |
| fannkuch                  | 245 ms                                                      | 244 ms: 1.00x faster                                            |
| sqlglot_normalize         | 171 ms                                                      | 172 ms: 1.01x slower                                            |
| scimark_monte_carlo       | 40.3 ms                                                     | 40.5 ms: 1.01x slower                                           |
| async_generators          | 223 ms                                                      | 225 ms: 1.01x slower                                            |
| xml_etree_generate        | 53.3 ms                                                     | 53.7 ms: 1.01x slower                                           |
| xml_etree_process         | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                           |
| coroutines                | 12.5 ms                                                     | 12.6 ms: 1.01x slower                                           |
| chameleon                 | 4.72 ms                                                     | 4.75 ms: 1.01x slower                                           |
| tomli_loads               | 1.36 sec                                                    | 1.37 sec: 1.01x slower                                          |
| chaos                     | 37.9 ms                                                     | 38.3 ms: 1.01x slower                                           |
| logging_format            | 6.15 us                                                     | 6.22 us: 1.01x slower                                           |
| sqlglot_transpile         | 952 us                                                      | 962 us: 1.01x slower                                            |
| nqueens                   | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                           |
| logging_simple            | 5.72 us                                                     | 5.80 us: 1.01x slower                                           |
| logging_silent            | 51.0 ns                                                     | 51.7 ns: 1.01x slower                                           |
| sympy_integrate           | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                           |
| sqlite_synth              | 1.60 us                                                     | 1.62 us: 1.02x slower                                           |
| unpickle_list             | 2.72 us                                                     | 2.77 us: 1.02x slower                                           |
| pyflate                   | 275 ms                                                      | 280 ms: 1.02x slower                                            |
| hexiom                    | 3.69 ms                                                     | 3.76 ms: 1.02x slower                                           |
| deltablue                 | 1.86 ms                                                     | 1.90 ms: 1.02x slower                                           |
| richards                  | 26.0 ms                                                     | 26.6 ms: 1.02x slower                                           |
| richards_super            | 29.3 ms                                                     | 29.9 ms: 1.02x slower                                           |
| pickle_dict               | 18.0 us                                                     | 18.4 us: 1.02x slower                                           |
| typing_runtime_protocols  | 100 us                                                      | 103 us: 1.03x slower                                            |
| regex_dna                 | 114 ms                                                      | 118 ms: 1.03x slower                                            |
| async_tree_none_tg        | 206 ms                                                      | 213 ms: 1.03x slower                                            |
| docutils                  | 1.57 sec                                                    | 1.64 sec: 1.04x slower                                          |
| nbody                     | 64.5 ms                                                     | 67.1 ms: 1.04x slower                                           |
| spectral_norm             | 59.2 ms                                                     | 61.9 ms: 1.05x slower                                           |
| pickle_list               | 2.89 us                                                     | 3.02 us: 1.05x slower                                           |
| scimark_lu                | 54.0 ms                                                     | 56.8 ms: 1.05x slower                                           |
| scimark_sor               | 72.0 ms                                                     | 75.9 ms: 1.05x slower                                           |
| deepcopy_memo             | 21.8 us                                                     | 23.1 us: 1.06x slower                                           |
| create_gc_cycles          | 829 us                                                      | 893 us: 1.08x slower                                            |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.53 ms: 1.08x slower                                           |
| crypto_pyaes              | 42.8 ms                                                     | 46.9 ms: 1.09x slower                                           |
| async_tree_io             | 521 ms                                                      | 582 ms: 1.12x slower                                            |
| async_tree_io_tg          | 512 ms                                                      | 604 ms: 1.18x slower                                            |
| Geometric mean            | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (15): async_tree_memoization, genshi_xml, pylint, xml_etree_iterparse, async_tree_cpu_io_mixed, mypy2, go, gc_traversal, unpickle_pure_python, comprehensions, deepcopy, scimark_fft, mako, float, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence
Ignored benchmarks (1) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json: dask

# HPT report

- Reliability score: 90.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown