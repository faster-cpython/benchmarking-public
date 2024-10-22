# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.03x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 250 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 45.1 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 731 ms: 1.15x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none           | 246 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 471 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 518 ms: 1.02x slower                                                           |
| async_generators          | 274 ms                                                          | 300 ms: 1.09x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| float          | 57.8 ms                                                         | 60.6 ms: 1.05x slower                                                          |
| nbody          | 81.9 ms                                                         | 96.5 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_dna      | 117 ms                                                          | 127 ms: 1.09x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 68.5 ms: 1.05x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 254 us: 1.07x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 176 us: 1.09x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.90 sec: 1.10x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 69.1 ms: 1.10x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 50.8 ms: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 46.4 ms: 1.07x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 21.2 ms: 1.06x faster                                                          |
| django_template | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| mako            | 7.31 ms                                                         | 8.10 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 738 us: 13.76x faster                                                          |
| coverage                  | 333 ms                                                          | 52.5 ms: 6.34x faster                                                          |
| deepcopy                  | 307 us                                                          | 243 us: 1.26x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 21.6 us: 1.21x faster                                                          |
| asyncio_tcp               | 842 ms                                                          | 731 ms: 1.15x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.50 us: 1.14x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none           | 246 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                           |
| go                        | 111 ms                                                          | 103 ms: 1.08x faster                                                           |
| html5lib                  | 48.3 ms                                                         | 45.1 ms: 1.07x faster                                                          |
| genshi_xml                | 49.5 ms                                                         | 46.4 ms: 1.07x faster                                                          |
| genshi_text               | 22.4 ms                                                         | 21.2 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 471 ms: 1.05x faster                                                           |
| json_loads                | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| json_dumps                | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| pathlib                   | 89.4 ms                                                         | 87.2 ms: 1.03x faster                                                          |
| gc_traversal              | 1.45 ms                                                         | 1.42 ms: 1.02x faster                                                          |
| 2to3                      | 253 ms                                                          | 250 ms: 1.01x faster                                                           |
| bench_mp_pool             | 74.3 ms                                                         | 73.5 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| sympy_sum                 | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| pidigits                  | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| python_startup            | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                          |
| pycparser                 | 869 ms                                                          | 864 ms: 1.01x faster                                                           |
| crypto_pyaes              | 58.2 ms                                                         | 57.8 ms: 1.01x faster                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| logging_simple            | 7.87 us                                                         | 7.94 us: 1.01x slower                                                          |
| dulwich_log               | 49.7 ms                                                         | 50.3 ms: 1.01x slower                                                          |
| telco                     | 6.67 ms                                                         | 6.78 ms: 1.02x slower                                                          |
| async_tree_io_tg          | 509 ms                                                          | 518 ms: 1.02x slower                                                           |
| django_template           | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| docutils                  | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                                         |
| sqlglot_transpile         | 1.29 ms                                                         | 1.32 ms: 1.02x slower                                                          |
| pprint_pformat            | 1.30 sec                                                        | 1.33 sec: 1.02x slower                                                         |
| sqlglot_parse             | 1.05 ms                                                         | 1.08 ms: 1.02x slower                                                          |
| mdp                       | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                         |
| regex_compile             | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| create_gc_cycles          | 713 us                                                          | 741 us: 1.04x slower                                                           |
| sqlglot_optimize          | 42.5 ms                                                         | 44.2 ms: 1.04x slower                                                          |
| regex_v8                  | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 229 ms: 1.04x slower                                                           |
| float                     | 57.8 ms                                                         | 60.6 ms: 1.05x slower                                                          |
| nqueens                   | 75.1 ms                                                         | 79.0 ms: 1.05x slower                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 68.5 ms: 1.05x slower                                                          |
| meteor_contest            | 77.0 ms                                                         | 81.3 ms: 1.06x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 144 us: 1.06x slower                                                           |
| spectral_norm             | 71.3 ms                                                         | 75.5 ms: 1.06x slower                                                          |
| chaos                     | 51.2 ms                                                         | 54.6 ms: 1.07x slower                                                          |
| pylint                    | 225 ms                                                          | 239 ms: 1.07x slower                                                           |
| pickle_pure_python        | 238 us                                                          | 254 us: 1.07x slower                                                           |
| scimark_sor               | 91.8 ms                                                         | 98.2 ms: 1.07x slower                                                          |
| comprehensions            | 12.7 us                                                         | 13.6 us: 1.07x slower                                                          |
| unpickle_pure_python      | 162 us                                                          | 176 us: 1.09x slower                                                           |
| regex_dna                 | 117 ms                                                          | 127 ms: 1.09x slower                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.17 ms: 1.09x slower                                                          |
| async_generators          | 274 ms                                                          | 300 ms: 1.09x slower                                                           |
| tomli_loads               | 1.73 sec                                                        | 1.90 sec: 1.10x slower                                                         |
| pyflate                   | 326 ms                                                          | 358 ms: 1.10x slower                                                           |
| xml_etree_generate        | 62.6 ms                                                         | 69.1 ms: 1.10x slower                                                          |
| regex_effbot              | 1.81 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| raytrace                  | 205 ms                                                          | 227 ms: 1.10x slower                                                           |
| scimark_lu                | 63.5 ms                                                         | 70.3 ms: 1.11x slower                                                          |
| mako                      | 7.31 ms                                                         | 8.10 ms: 1.11x slower                                                          |
| scimark_monte_carlo       | 50.3 ms                                                         | 55.8 ms: 1.11x slower                                                          |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                          |
| scimark_fft               | 206 ms                                                          | 231 ms: 1.12x slower                                                           |
| deltablue                 | 2.41 ms                                                         | 2.70 ms: 1.12x slower                                                          |
| xml_etree_process         | 45.0 ms                                                         | 50.8 ms: 1.13x slower                                                          |
| fannkuch                  | 293 ms                                                          | 332 ms: 1.13x slower                                                           |
| hexiom                    | 4.64 ms                                                         | 5.29 ms: 1.14x slower                                                          |
| richards_super            | 38.0 ms                                                         | 44.3 ms: 1.17x slower                                                          |
| richards                  | 33.8 ms                                                         | 39.8 ms: 1.18x slower                                                          |
| nbody                     | 81.9 ms                                                         | 96.5 ms: 1.18x slower                                                          |
| logging_silent            | 61.6 ns                                                         | 72.8 ns: 1.18x slower                                                          |
| generators                | 22.1 ms                                                         | 26.7 ms: 1.21x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (11): json, sympy_str, python_startup_no_site, xml_etree_parse, sympy_expand, logging_format, pprint_safe_repr, async_tree_cpu_io_mixed_tg, async_tree_io, tornado_http, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown