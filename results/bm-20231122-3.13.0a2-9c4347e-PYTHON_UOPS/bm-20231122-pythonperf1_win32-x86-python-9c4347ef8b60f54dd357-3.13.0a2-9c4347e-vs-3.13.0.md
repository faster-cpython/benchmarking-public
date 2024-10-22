# Results vs. 3.13.0

- fork: python
- ref: 9c4347ef8b60f54dd357
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 268 ms: 1.06x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                         |
| tornado_http   | 104 ms                                                          | 112 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 658 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 523 ms: 1.06x slower                                                           |
| async_tree_memoization     | 302 ms                                                          | 329 ms: 1.09x slower                                                           |
| async_tree_none            | 246 ms                                                          | 270 ms: 1.10x slower                                                           |
| async_generators           | 274 ms                                                          | 304 ms: 1.11x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 518 ms: 1.12x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 327 ms: 1.14x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                          |
| async_tree_none_tg         | 219 ms                                                          | 264 ms: 1.21x slower                                                           |
| async_tree_io              | 537 ms                                                          | 651 ms: 1.21x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 634 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 62.3 ms: 1.08x slower                                                          |
| nbody          | 81.9 ms                                                         | 91.9 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 2.01 ms: 1.11x slower                                                          |
| regex_dna      | 117 ms                                                          | 132 ms: 1.13x slower                                                           |
| regex_compile  | 103 ms                                                          | 131 ms: 1.27x slower                                                           |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_list        | 3.09 us                                                         | 2.69 us: 1.15x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 19.7 us: 1.10x faster                                                          |
| pickle               | 8.42 us                                                         | 7.66 us: 1.10x faster                                                          |
| unpickle             | 10.5 us                                                         | 9.65 us: 1.09x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.20 us: 1.06x faster                                                          |
| json_loads           | 21.0 us                                                         | 19.9 us: 1.05x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.11 ms: 1.04x faster                                                          |
| pickle_pure_python   | 238 us                                                          | 235 us: 1.01x faster                                                           |
| xml_etree_parse      | 109 ms                                                          | 111 ms: 1.02x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.79 sec: 1.04x slower                                                         |
| xml_etree_process    | 45.0 ms                                                         | 47.9 ms: 1.06x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 173 us: 1.07x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 67.3 ms: 1.08x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 71.7 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.3 ms: 1.04x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 21.2 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 7.31 ms                                                         | 8.20 ms: 1.12x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                          | 105 us: 1.30x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 658 ms: 1.28x faster                                                           |
| unpickle_list              | 3.09 us                                                         | 2.69 us: 1.15x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 19.7 us: 1.10x faster                                                          |
| create_gc_cycles           | 713 us                                                          | 648 us: 1.10x faster                                                           |
| pickle                     | 8.42 us                                                         | 7.66 us: 1.10x faster                                                          |
| unpickle                   | 10.5 us                                                         | 9.65 us: 1.09x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.64 us: 1.08x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.20 us: 1.06x faster                                                          |
| json_loads                 | 21.0 us                                                         | 19.9 us: 1.05x faster                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.87 us: 1.05x faster                                                          |
| python_startup             | 24.3 ms                                                         | 23.3 ms: 1.04x faster                                                          |
| telco                      | 6.67 ms                                                         | 6.40 ms: 1.04x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.11 ms: 1.04x faster                                                          |
| json                       | 4.27 ms                                                         | 4.12 ms: 1.04x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.40 ms: 1.04x faster                                                          |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| pickle_pure_python         | 238 us                                                          | 235 us: 1.01x faster                                                           |
| unpack_sequence            | 42.9 ns                                                         | 42.6 ns: 1.01x faster                                                          |
| pprint_safe_repr           | 644 ms                                                          | 649 ms: 1.01x slower                                                           |
| deepcopy                   | 307 us                                                          | 310 us: 1.01x slower                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 58.8 ms: 1.01x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.06 ms: 1.01x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 75.2 ms: 1.01x slower                                                          |
| xml_etree_parse            | 109 ms                                                          | 111 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.33 sec: 1.03x slower                                                         |
| sqlglot_transpile          | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.79 sec: 1.04x slower                                                         |
| regex_v8                   | 15.6 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| richards                   | 33.8 ms                                                         | 35.6 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 523 ms: 1.06x slower                                                           |
| 2to3                       | 253 ms                                                          | 268 ms: 1.06x slower                                                           |
| deepcopy_memo              | 26.2 us                                                         | 27.8 us: 1.06x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 21.2 ms: 1.06x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 47.9 ms: 1.06x slower                                                          |
| logging_format             | 8.57 us                                                         | 9.15 us: 1.07x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                         |
| richards_super             | 38.0 ms                                                         | 40.6 ms: 1.07x slower                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 1.09 ms: 1.07x slower                                                          |
| tornado_http               | 104 ms                                                          | 112 ms: 1.07x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 173 us: 1.07x slower                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 67.3 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 237 ms: 1.08x slower                                                           |
| float                      | 57.8 ms                                                         | 62.3 ms: 1.08x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 83.2 ms: 1.08x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.81 sec: 1.08x slower                                                         |
| go                         | 111 ms                                                          | 121 ms: 1.08x slower                                                           |
| async_tree_memoization     | 302 ms                                                          | 329 ms: 1.09x slower                                                           |
| sympy_expand               | 375 ms                                                          | 408 ms: 1.09x slower                                                           |
| logging_simple             | 7.87 us                                                         | 8.58 us: 1.09x slower                                                          |
| fannkuch                   | 293 ms                                                          | 321 ms: 1.09x slower                                                           |
| async_tree_none            | 246 ms                                                          | 270 ms: 1.10x slower                                                           |
| pycparser                  | 869 ms                                                          | 955 ms: 1.10x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 46.8 ms: 1.10x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 71.7 ms: 1.10x slower                                                          |
| async_generators           | 274 ms                                                          | 304 ms: 1.11x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 2.01 ms: 1.11x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 102 ms: 1.11x slower                                                           |
| chaos                      | 51.2 ms                                                         | 57.2 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 518 ms: 1.12x slower                                                           |
| mako                       | 7.31 ms                                                         | 8.20 ms: 1.12x slower                                                          |
| nbody                      | 81.9 ms                                                         | 91.9 ms: 1.12x slower                                                          |
| sympy_str                  | 215 ms                                                          | 241 ms: 1.12x slower                                                           |
| pyflate                    | 326 ms                                                          | 367 ms: 1.13x slower                                                           |
| regex_dna                  | 117 ms                                                          | 132 ms: 1.13x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 327 ms: 1.14x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 123 ms: 1.14x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.4 ms: 1.15x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 57.8 ms: 1.15x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                          |
| scimark_fft                | 206 ms                                                          | 243 ms: 1.17x slower                                                           |
| async_tree_none_tg         | 219 ms                                                          | 264 ms: 1.21x slower                                                           |
| async_tree_io              | 537 ms                                                          | 651 ms: 1.21x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 91.2 ms: 1.21x slower                                                          |
| comprehensions             | 12.7 us                                                         | 15.7 us: 1.23x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 634 ms: 1.25x slower                                                           |
| scimark_lu                 | 63.5 ms                                                         | 79.2 ms: 1.25x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 76.8 ns: 1.25x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.63 ms: 1.25x slower                                                          |
| raytrace                   | 205 ms                                                          | 257 ms: 1.25x slower                                                           |
| regex_compile              | 103 ms                                                          | 131 ms: 1.27x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 3.08 ms: 1.28x slower                                                          |
| generators                 | 22.1 ms                                                         | 29.6 ms: 1.34x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 6.24 ms: 1.35x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 96.9 ms: 1.36x slower                                                          |
| coverage                   | 333 ms                                                          | 510 ms: 1.53x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                                   |

Benchmark hidden because not significant (3): pathlib, asyncio_tcp_ssl, chameleon
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown