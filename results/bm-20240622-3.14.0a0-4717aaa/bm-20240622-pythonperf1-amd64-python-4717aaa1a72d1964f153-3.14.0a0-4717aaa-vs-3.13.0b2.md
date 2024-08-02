# Results vs. 3.13.0b2

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.04x faster
- HPT reliability: 85.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 211 ms: 1.02x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.62 sec: 1.01x faster                                                     |
| tornado_http   | 81.8 ms                                                         | 79.7 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 505 ms: 1.20x faster                                                       |
| async_tree_io             | 588 ms                                                          | 503 ms: 1.17x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 179 ms: 1.13x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 234 ms: 1.10x faster                                                       |
| async_tree_none           | 218 ms                                                          | 199 ms: 1.10x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 243 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.10x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 65.8 ms: 1.03x faster                                                      |
| float          | 49.7 ms                                                         | 49.1 ms: 1.01x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 77.2 ms: 1.01x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.8 us: 1.03x faster                                                      |
| pickle               | 7.11 us                                                         | 7.10 us: 1.00x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 18.2 us: 1.00x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 36.9 ms: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.0 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.2 ms: 1.01x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.02x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.02x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.59 us: 1.02x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 181 us: 1.03x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.82 ms: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.84 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 16.8 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                      |
| mako            | 6.36 ms                                                         | 6.60 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 504 us: 16.10x faster                                                      |
| deepcopy                  | 220 us                                                          | 164 us: 1.34x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 17.1 us: 1.30x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 505 ms: 1.20x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.68 us: 1.18x faster                                                      |
| async_tree_io             | 588 ms                                                          | 503 ms: 1.17x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 179 ms: 1.13x faster                                                       |
| json                      | 3.19 ms                                                         | 2.88 ms: 1.11x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 234 ms: 1.10x faster                                                       |
| async_tree_none           | 218 ms                                                          | 199 ms: 1.10x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 243 ms: 1.09x faster                                                       |
| scimark_lu                | 56.6 ms                                                         | 53.4 ms: 1.06x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 61.2 ms: 1.04x faster                                                      |
| bench_thread_pool         | 768 us                                                          | 742 us: 1.03x faster                                                       |
| richards                  | 26.7 ms                                                         | 25.9 ms: 1.03x faster                                                      |
| json_loads                | 14.2 us                                                         | 13.8 us: 1.03x faster                                                      |
| nbody                     | 67.6 ms                                                         | 65.8 ms: 1.03x faster                                                      |
| tornado_http              | 81.8 ms                                                         | 79.7 ms: 1.03x faster                                                      |
| richards_super            | 30.2 ms                                                         | 29.4 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.02x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.02x faster                                                      |
| raytrace                  | 162 ms                                                          | 159 ms: 1.02x faster                                                       |
| nqueens                   | 56.7 ms                                                         | 55.8 ms: 1.01x faster                                                      |
| float                     | 49.7 ms                                                         | 49.1 ms: 1.01x faster                                                      |
| regex_compile             | 78.0 ms                                                         | 77.2 ms: 1.01x faster                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 45.1 ms: 1.01x faster                                                      |
| hexiom                    | 3.72 ms                                                         | 3.70 ms: 1.01x faster                                                      |
| docutils                  | 1.63 sec                                                        | 1.62 sec: 1.01x faster                                                     |
| pathlib                   | 75.9 ms                                                         | 75.5 ms: 1.00x faster                                                      |
| chaos                     | 38.4 ms                                                         | 38.2 ms: 1.00x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| pickle                    | 7.11 us                                                         | 7.10 us: 1.00x faster                                                      |
| pickle_dict               | 18.1 us                                                         | 18.2 us: 1.00x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.3 ms: 1.01x slower                                                      |
| fannkuch                  | 243 ms                                                          | 245 ms: 1.01x slower                                                       |
| pyflate                   | 279 ms                                                          | 281 ms: 1.01x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 65.3 ms: 1.01x slower                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.61 us: 1.01x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 70.6 ms: 1.01x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 966 us: 1.01x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 36.9 ms: 1.01x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.0 ms: 1.01x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 33.1 ms: 1.01x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 63.2 ms: 1.01x slower                                                      |
| coroutines                | 12.8 ms                                                         | 12.9 ms: 1.01x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 53.6 ns: 1.01x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 102 us: 1.01x slower                                                       |
| scimark_fft               | 171 ms                                                          | 173 ms: 1.01x slower                                                       |
| pprint_safe_repr          | 474 ms                                                          | 481 ms: 1.02x slower                                                       |
| sympy_str                 | 159 ms                                                          | 162 ms: 1.02x slower                                                       |
| sympy_expand              | 271 ms                                                          | 275 ms: 1.02x slower                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.37 sec: 1.02x slower                                                     |
| sqlglot_normalize         | 173 ms                                                          | 176 ms: 1.02x slower                                                       |
| go                        | 82.1 ms                                                         | 83.6 ms: 1.02x slower                                                      |
| django_template           | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                                      |
| python_startup            | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                                      |
| 2to3                      | 207 ms                                                          | 211 ms: 1.02x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 986 ms: 1.02x slower                                                       |
| async_generators          | 223 ms                                                          | 228 ms: 1.02x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 125 us: 1.02x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.59 us: 1.02x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 914 us: 1.03x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 771 us: 1.03x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 181 us: 1.03x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 40.5 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.59 ms: 1.03x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 16.8 ms: 1.04x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.82 ms: 1.04x slower                                                      |
| mako                      | 6.36 ms                                                         | 6.60 ms: 1.04x slower                                                      |
| regex_dna                 | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| generators                | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.38 sec: 1.05x slower                                                     |
| telco                     | 4.67 ms                                                         | 4.93 ms: 1.05x slower                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.57 sec: 1.06x slower                                                     |
| unpickle_list             | 2.62 us                                                         | 2.84 us: 1.08x slower                                                      |
| coverage                  | 42.1 ms                                                         | 46.8 ms: 1.11x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                               |

Benchmark hidden because not significant (13): pycparser, async_tree_cpu_io_mixed_tg, pylint, html5lib, logging_simple, sympy_sum, logging_format, gc_traversal, scimark_sor, asyncio_tcp, pickle_list, genshi_xml, regex_v8
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2

# HPT report

- Reliability score: 85.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown