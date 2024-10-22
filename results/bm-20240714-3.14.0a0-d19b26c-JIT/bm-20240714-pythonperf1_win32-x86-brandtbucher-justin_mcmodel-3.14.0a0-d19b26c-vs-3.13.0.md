# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-x86
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.11x faster
- HPT reliability: 98.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.82 sec                                                        | 1.92 sec: 1.06x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.7 ms: 1.01x faster                                                          |
| tornado_http   | 104 ms                                                          | 97.7 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 609 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| async_tree_io_tg           | 509 ms                                                          | 501 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 469 ms: 1.01x slower                                                           |
| async_generators           | 274 ms                                                          | 308 ms: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 54.9 ms: 1.49x faster                                                          |
| float          | 57.8 ms                                                         | 43.2 ms: 1.34x faster                                                          |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 96.0 ms: 1.08x faster                                                          |
| regex_v8       | 15.6 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| pickle_pure_python   | 238 us                                                          | 215 us: 1.11x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 147 us: 1.10x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 61.4 ms: 1.06x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.15 ms: 1.04x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 44.4 ms: 1.01x faster                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 62.1 ms: 1.01x faster                                                          |
| json_loads           | 21.0 us                                                         | 21.6 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.9 ms: 1.06x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.1 ms: 1.05x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 7.31 ms                                                         | 5.45 ms: 1.34x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                          |
| genshi_xml     | 49.5 ms                                                         | 53.2 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 753 us: 13.48x faster                                                          |
| coverage                   | 333 ms                                                          | 51.1 ms: 6.52x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 15.2 us: 1.72x faster                                                          |
| nbody                      | 81.9 ms                                                         | 54.9 ms: 1.49x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 48.2 ms: 1.48x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 609 ms: 1.38x faster                                                           |
| mako                       | 7.31 ms                                                         | 5.45 ms: 1.34x faster                                                          |
| float                      | 57.8 ms                                                         | 43.2 ms: 1.34x faster                                                          |
| deepcopy                   | 307 us                                                          | 237 us: 1.29x faster                                                           |
| fannkuch                   | 293 ms                                                          | 233 ms: 1.26x faster                                                           |
| scimark_fft                | 206 ms                                                          | 168 ms: 1.23x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 48.3 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.37 us: 1.20x faster                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 41.9 ms: 1.20x faster                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.45 ms: 1.18x faster                                                          |
| telco                      | 6.67 ms                                                         | 5.64 ms: 1.18x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| pyflate                    | 326 ms                                                          | 283 ms: 1.15x faster                                                           |
| pprint_safe_repr           | 644 ms                                                          | 560 ms: 1.15x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| comprehensions             | 12.7 us                                                         | 11.2 us: 1.14x faster                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.15 sec: 1.12x faster                                                         |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 941 us: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.12x faster                                                           |
| pickle_pure_python         | 238 us                                                          | 215 us: 1.11x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 147 us: 1.10x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 82.3 ms: 1.09x faster                                                          |
| regex_compile              | 103 ms                                                          | 96.0 ms: 1.08x faster                                                          |
| logging_silent             | 61.6 ns                                                         | 57.3 ns: 1.08x faster                                                          |
| tornado_http               | 104 ms                                                          | 97.7 ms: 1.07x faster                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.21 ms: 1.07x faster                                                          |
| logging_format             | 8.57 us                                                         | 8.05 us: 1.06x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.40 us: 1.06x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 61.4 ms: 1.06x faster                                                          |
| python_startup             | 24.3 ms                                                         | 22.9 ms: 1.06x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 975 us: 1.05x faster                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.1 ms: 1.05x faster                                                          |
| pycparser                  | 869 ms                                                          | 834 ms: 1.04x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 72.2 ms: 1.04x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.15 ms: 1.04x faster                                                          |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| meteor_contest             | 77.0 ms                                                         | 74.6 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| richards                   | 33.8 ms                                                         | 32.9 ms: 1.03x faster                                                          |
| hexiom                     | 4.64 ms                                                         | 4.56 ms: 1.02x faster                                                          |
| async_tree_io_tg           | 509 ms                                                          | 501 ms: 1.02x faster                                                           |
| gc_traversal               | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| xml_etree_process          | 45.0 ms                                                         | 44.4 ms: 1.01x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 47.7 ms: 1.01x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 73.6 ms: 1.01x faster                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 62.1 ms: 1.01x faster                                                          |
| genshi_text                | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                          |
| sympy_str                  | 215 ms                                                          | 217 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 469 ms: 1.01x slower                                                           |
| go                         | 111 ms                                                          | 113 ms: 1.01x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 109 ms: 1.01x slower                                                           |
| richards_super             | 38.0 ms                                                         | 38.6 ms: 1.02x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                         |
| sympy_expand               | 375 ms                                                          | 385 ms: 1.03x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 43.7 ms: 1.03x slower                                                          |
| json_loads                 | 21.0 us                                                         | 21.6 us: 1.03x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.9 ms: 1.04x slower                                                          |
| chaos                      | 51.2 ms                                                         | 53.5 ms: 1.04x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.92 sec: 1.06x slower                                                         |
| create_gc_cycles           | 713 us                                                          | 756 us: 1.06x slower                                                           |
| json                       | 4.27 ms                                                         | 4.56 ms: 1.07x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 236 ms: 1.07x slower                                                           |
| genshi_xml                 | 49.5 ms                                                         | 53.2 ms: 1.07x slower                                                          |
| pylint                     | 225 ms                                                          | 241 ms: 1.07x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 100 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 153 us: 1.12x slower                                                           |
| async_generators           | 274 ms                                                          | 308 ms: 1.13x slower                                                           |
| raytrace                   | 205 ms                                                          | 233 ms: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.74 ms: 1.14x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 77.8 ms: 1.22x slower                                                          |
| generators                 | 22.1 ms                                                         | 27.6 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (4): django_template, 2to3, regex_dna, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.49% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown