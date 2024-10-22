# Results vs. 3.13.0

- fork: mdboom
- ref: disable_interpreter_
- machine: windows-x86
- commit hash: 46655f3
- commit date: 2024-10-09
- overall geometric mean: 1.10x faster
- HPT reliability: 97.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 262 ms: 1.03x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.05 sec: 1.13x slower                                                         |
| html5lib       | 48.3 ms                                                         | 45.3 ms: 1.07x faster                                                          |
| tornado_http   | 104 ms                                                          | 108 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 196 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 809 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 477 ms: 1.03x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.1 ms: 1.15x slower                                                          |
| async_generators           | 274 ms                                                          | 326 ms: 1.19x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_tcp_ssl, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 52.9 ms: 1.55x faster                                                          |
| float          | 57.8 ms                                                         | 45.3 ms: 1.27x faster                                                          |
| pidigits       | 202 ms                                                          | 205 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 114 ms: 1.02x faster                                                           |
| regex_v8       | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.84 ms: 1.01x slower                                                          |
| regex_compile  | 103 ms                                                          | 106 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 62.6 ms                                                         | 54.1 ms: 1.16x faster                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                         |
| xml_etree_process    | 45.0 ms                                                         | 40.6 ms: 1.11x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.79 ms: 1.09x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 2.92 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 63.4 ms: 1.03x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 159 us: 1.02x faster                                                           |
| pickle               | 8.42 us                                                         | 8.46 us: 1.00x slower                                                          |
| json_loads           | 21.0 us                                                         | 21.2 us: 1.01x slower                                                          |
| pickle_list          | 3.40 us                                                         | 3.44 us: 1.01x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 250 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (3): pickle_dict, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.2 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 7.31 ms                                                         | 5.69 ms: 1.28x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 23.4 ms: 1.04x slower                                                          |
| genshi_xml     | 49.5 ms                                                         | 54.6 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 756 us: 13.42x faster                                                          |
| coverage                   | 333 ms                                                          | 51.6 ms: 6.45x faster                                                          |
| sqlglot_normalize          | 220 ms                                                          | 104 ms: 2.12x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 15.2 us: 1.72x faster                                                          |
| nbody                      | 81.9 ms                                                         | 52.9 ms: 1.55x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 50.9 ms: 1.40x faster                                                          |
| deepcopy                   | 307 us                                                          | 232 us: 1.32x faster                                                           |
| scimark_sor                | 91.8 ms                                                         | 69.6 ms: 1.32x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.69 ms: 1.28x faster                                                          |
| float                      | 57.8 ms                                                         | 45.3 ms: 1.27x faster                                                          |
| fannkuch                   | 293 ms                                                          | 239 ms: 1.23x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 47.8 ms: 1.22x faster                                                          |
| scimark_fft                | 206 ms                                                          | 170 ms: 1.21x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.41 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.39 us: 1.19x faster                                                          |
| deltablue                  | 2.41 ms                                                         | 2.03 ms: 1.18x faster                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 54.1 ms: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                         |
| pyflate                    | 326 ms                                                          | 288 ms: 1.13x faster                                                           |
| pprint_safe_repr           | 644 ms                                                          | 572 ms: 1.13x faster                                                           |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 196 ms: 1.11x faster                                                           |
| go                         | 111 ms                                                          | 100 ms: 1.11x faster                                                           |
| xml_etree_process          | 45.0 ms                                                         | 40.6 ms: 1.11x faster                                                          |
| telco                      | 6.67 ms                                                         | 6.02 ms: 1.11x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| scimark_lu                 | 63.5 ms                                                         | 57.9 ms: 1.10x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.79 ms: 1.09x faster                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.19 sec: 1.09x faster                                                         |
| logging_silent             | 61.6 ns                                                         | 56.7 ns: 1.09x faster                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 46.8 ms: 1.08x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 45.3 ms: 1.07x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 2.92 us: 1.06x faster                                                          |
| pycparser                  | 869 ms                                                          | 824 ms: 1.06x faster                                                           |
| comprehensions             | 12.7 us                                                         | 12.1 us: 1.05x faster                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.89 us: 1.04x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 809 ms: 1.04x faster                                                           |
| meteor_contest             | 77.0 ms                                                         | 74.3 ms: 1.04x faster                                                          |
| json                       | 4.27 ms                                                         | 4.14 ms: 1.03x faster                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.02 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 63.4 ms: 1.03x faster                                                          |
| logging_format             | 8.57 us                                                         | 8.36 us: 1.02x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.69 us: 1.02x faster                                                          |
| regex_dna                  | 117 ms                                                          | 114 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 159 us: 1.02x faster                                                           |
| richards_super             | 38.0 ms                                                         | 37.4 ms: 1.01x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 88.4 ms: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| pickle                     | 8.42 us                                                         | 8.46 us: 1.00x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                                          |
| json_loads                 | 21.0 us                                                         | 21.2 us: 1.01x slower                                                          |
| pickle_list                | 3.40 us                                                         | 3.44 us: 1.01x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 20.2 ms: 1.01x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.84 ms: 1.01x slower                                                          |
| pidigits                   | 202 ms                                                          | 205 ms: 1.02x slower                                                           |
| mdp                        | 1.67 sec                                                        | 1.70 sec: 1.02x slower                                                         |
| regex_compile              | 103 ms                                                          | 106 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 477 ms: 1.03x slower                                                           |
| 2to3                       | 253 ms                                                          | 262 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.34 ms: 1.04x slower                                                          |
| tornado_http               | 104 ms                                                          | 108 ms: 1.04x slower                                                           |
| genshi_text                | 22.4 ms                                                         | 23.4 ms: 1.04x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 77.8 ms: 1.05x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 250 us: 1.05x slower                                                           |
| chaos                      | 51.2 ms                                                         | 53.9 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 145 us: 1.06x slower                                                           |
| sympy_str                  | 215 ms                                                          | 230 ms: 1.07x slower                                                           |
| sympy_expand               | 375 ms                                                          | 403 ms: 1.07x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 117 ms: 1.09x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.08 ms: 1.10x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 784 us: 1.10x slower                                                           |
| generators                 | 22.1 ms                                                         | 24.4 ms: 1.10x slower                                                          |
| genshi_xml                 | 49.5 ms                                                         | 54.6 ms: 1.10x slower                                                          |
| docutils                   | 1.82 sec                                                        | 2.05 sec: 1.13x slower                                                         |
| coroutines                 | 15.7 ms                                                         | 18.1 ms: 1.15x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 17.6 ms: 1.16x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 50.1 ms: 1.18x slower                                                          |
| async_generators           | 274 ms                                                          | 326 ms: 1.19x slower                                                           |
| raytrace                   | 205 ms                                                          | 253 ms: 1.23x slower                                                           |
| pylint                     | 225 ms                                                          | 281 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (14): bench_thread_pool, pickle_dict, unpack_sequence, async_tree_cpu_io_mixed, nqueens, async_tree_io_tg, richards, dulwich_log, django_template, unpickle, asyncio_tcp_ssl, xml_etree_parse, async_tree_io, python_startup
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 97.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown