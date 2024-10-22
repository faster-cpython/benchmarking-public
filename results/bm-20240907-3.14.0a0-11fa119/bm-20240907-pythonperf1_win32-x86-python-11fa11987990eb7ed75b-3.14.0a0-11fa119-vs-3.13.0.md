# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 757 ms: 1.11x faster                                                           |
| async_tree_none            | 246 ms                                                          | 222 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 480 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 502 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                           |
| async_generators           | 274 ms                                                          | 298 ms: 1.09x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.4 ms: 1.17x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| float          | 57.8 ms                                                         | 62.0 ms: 1.07x slower                                                          |
| nbody          | 81.9 ms                                                         | 94.3 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| regex_compile  | 103 ms                                                          | 109 ms: 1.05x slower                                                           |
| regex_dna      | 117 ms                                                          | 124 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| pickle               | 8.42 us                                                         | 7.97 us: 1.06x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 3.02 us: 1.02x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.5 us: 1.02x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| pickle_list          | 3.40 us                                                         | 3.35 us: 1.01x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 68.0 ms: 1.04x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 66.7 ms: 1.07x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 255 us: 1.07x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| xml_etree_process    | 45.0 ms                                                         | 49.5 ms: 1.10x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 47.0 ms: 1.05x faster                                                          |
| django_template | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                          |
| mako            | 7.31 ms                                                         | 8.27 ms: 1.13x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 719 us: 14.11x faster                                                          |
| coverage                   | 333 ms                                                          | 52.1 ms: 6.39x faster                                                          |
| deepcopy                   | 307 us                                                          | 242 us: 1.27x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.9 us: 1.20x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.47 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 757 ms: 1.11x faster                                                           |
| async_tree_none            | 246 ms                                                          | 222 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.97 us: 1.06x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 47.0 ms: 1.05x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 72.1 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 480 ms: 1.03x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 86.9 ms: 1.03x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 3.02 us: 1.02x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.5 us: 1.02x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 502 ms: 1.01x faster                                                           |
| sqlite_synth               | 1.97 us                                                         | 1.94 us: 1.01x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.35 us: 1.01x faster                                                          |
| pidigits                   | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| django_template            | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                          |
| logging_format             | 8.57 us                                                         | 8.61 us: 1.01x slower                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 58.7 ms: 1.01x slower                                                          |
| logging_simple             | 7.87 us                                                         | 7.94 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                           |
| dulwich_log                | 49.7 ms                                                         | 50.4 ms: 1.02x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.02x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.32 sec: 1.02x slower                                                         |
| sympy_expand               | 375 ms                                                          | 381 ms: 1.02x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 76.5 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.08 ms: 1.02x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| sqlglot_transpile          | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 43.9 ms: 1.03x slower                                                          |
| telco                      | 6.67 ms                                                         | 6.90 ms: 1.04x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 739 us: 1.04x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 233 ms: 1.04x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 68.0 ms: 1.04x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.75 sec: 1.05x slower                                                         |
| sqlglot_normalize          | 220 ms                                                          | 232 ms: 1.05x slower                                                           |
| regex_compile              | 103 ms                                                          | 109 ms: 1.05x slower                                                           |
| chaos                      | 51.2 ms                                                         | 54.1 ms: 1.06x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 81.4 ms: 1.06x slower                                                          |
| regex_dna                  | 117 ms                                                          | 124 ms: 1.07x slower                                                           |
| spectral_norm              | 71.3 ms                                                         | 76.0 ms: 1.07x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 66.7 ms: 1.07x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 255 us: 1.07x slower                                                           |
| float                      | 57.8 ms                                                         | 62.0 ms: 1.07x slower                                                          |
| comprehensions             | 12.7 us                                                         | 13.7 us: 1.08x slower                                                          |
| unpack_sequence            | 42.9 ns                                                         | 46.5 ns: 1.08x slower                                                          |
| async_generators           | 274 ms                                                          | 298 ms: 1.09x slower                                                           |
| pyflate                    | 326 ms                                                          | 355 ms: 1.09x slower                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| xml_etree_process          | 45.0 ms                                                         | 49.5 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.19 ms: 1.10x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 179 us: 1.11x slower                                                           |
| raytrace                   | 205 ms                                                          | 229 ms: 1.11x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.68 ms: 1.12x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 152 us: 1.12x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 103 ms: 1.13x slower                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 56.8 ms: 1.13x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.27 ms: 1.13x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.25 ms: 1.13x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 72.3 ms: 1.14x slower                                                          |
| fannkuch                   | 293 ms                                                          | 336 ms: 1.15x slower                                                           |
| richards                   | 33.8 ms                                                         | 38.8 ms: 1.15x slower                                                          |
| richards_super             | 38.0 ms                                                         | 43.7 ms: 1.15x slower                                                          |
| nbody                      | 81.9 ms                                                         | 94.3 ms: 1.15x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.4 ms: 1.17x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 75.2 ns: 1.22x slower                                                          |
| scimark_fft                | 206 ms                                                          | 253 ms: 1.22x slower                                                           |
| generators                 | 22.1 ms                                                         | 27.6 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (13): json, sympy_sum, bench_thread_pool, pycparser, 2to3, pprint_safe_repr, genshi_text, python_startup, unpickle, async_tree_io, gc_traversal, sympy_str, tornado_http
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown