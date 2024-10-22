# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-x86
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.7 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 105 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 696 ms: 1.21x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 199 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 479 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 468 ms: 1.01x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 521 ms: 1.02x slower                                                           |
| async_generators           | 274 ms                                                          | 310 ms: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 62.7 ms: 1.09x slower                                                          |
| nbody          | 81.9 ms                                                         | 93.9 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| regex_compile  | 103 ms                                                          | 111 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.5 us: 1.06x faster                                                          |
| pickle               | 8.42 us                                                         | 8.00 us: 1.05x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.33 us: 1.02x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| json_loads           | 21.0 us                                                         | 20.7 us: 1.01x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 3.07 us: 1.01x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.3 ms: 1.03x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                                         |
| pickle_pure_python   | 238 us                                                          | 263 us: 1.11x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 70.2 ms: 1.12x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 51.8 ms: 1.15x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 188 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 24.8 ms: 1.02x slower                                                          |
| python_startup_no_site | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.5 ms: 1.02x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| django_template | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                          |
| mako            | 7.31 ms                                                         | 8.31 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 743 us: 13.67x faster                                                          |
| coverage                   | 333 ms                                                          | 51.0 ms: 6.53x faster                                                          |
| deepcopy                   | 307 us                                                          | 250 us: 1.23x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 696 ms: 1.21x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.13x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 23.5 us: 1.12x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.59 us: 1.10x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 199 ms: 1.10x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 20.5 us: 1.06x faster                                                          |
| pickle                     | 8.42 us                                                         | 8.00 us: 1.05x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.7 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 479 ms: 1.03x faster                                                           |
| gc_traversal               | 1.45 ms                                                         | 1.41 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 87.2 ms: 1.03x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.33 us: 1.02x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 48.5 ms: 1.02x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| json_loads                 | 21.0 us                                                         | 20.7 us: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.01x faster                                                         |
| genshi_text                | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 3.07 us: 1.01x faster                                                          |
| pycparser                  | 869 ms                                                          | 863 ms: 1.01x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 75.5 ms: 1.01x slower                                                          |
| regex_dna                  | 117 ms                                                          | 118 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 468 ms: 1.01x slower                                                           |
| tornado_http               | 104 ms                                                          | 105 ms: 1.01x slower                                                           |
| sqlite_synth               | 1.97 us                                                         | 1.99 us: 1.01x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.69 sec: 1.01x slower                                                         |
| create_gc_cycles           | 713 us                                                          | 723 us: 1.01x slower                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 59.0 ms: 1.01x slower                                                          |
| sympy_str                  | 215 ms                                                          | 218 ms: 1.01x slower                                                           |
| python_startup             | 24.3 ms                                                         | 24.8 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 521 ms: 1.02x slower                                                           |
| telco                      | 6.67 ms                                                         | 6.82 ms: 1.02x slower                                                          |
| unpack_sequence            | 42.9 ns                                                         | 44.0 ns: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                          | 384 ms: 1.03x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| json_dumps                 | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.6 ms: 1.03x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.3 ms: 1.03x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 77.0 ms: 1.04x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 668 ms: 1.04x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.91 us: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| logging_simple             | 7.87 us                                                         | 8.23 us: 1.05x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 80.6 ms: 1.05x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.10 ms: 1.05x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.37 ms: 1.06x slower                                                          |
| django_template            | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 145 us: 1.07x slower                                                           |
| regex_compile              | 103 ms                                                          | 111 ms: 1.07x slower                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.40 sec: 1.08x slower                                                         |
| sqlglot_optimize           | 42.5 ms                                                         | 45.8 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 238 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.15 ms: 1.08x slower                                                          |
| float                      | 57.8 ms                                                         | 62.7 ms: 1.09x slower                                                          |
| comprehensions             | 12.7 us                                                         | 13.9 us: 1.09x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 78.6 ms: 1.10x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                                         |
| pickle_pure_python         | 238 us                                                          | 263 us: 1.11x slower                                                           |
| scimark_lu                 | 63.5 ms                                                         | 70.5 ms: 1.11x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 70.2 ms: 1.12x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 104 ms: 1.13x slower                                                           |
| chaos                      | 51.2 ms                                                         | 58.0 ms: 1.13x slower                                                          |
| async_generators           | 274 ms                                                          | 310 ms: 1.13x slower                                                           |
| pyflate                    | 326 ms                                                          | 370 ms: 1.14x slower                                                           |
| mako                       | 7.31 ms                                                         | 8.31 ms: 1.14x slower                                                          |
| nbody                      | 81.9 ms                                                         | 93.9 ms: 1.15x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 51.8 ms: 1.15x slower                                                          |
| scimark_fft                | 206 ms                                                          | 238 ms: 1.15x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.36 ms: 1.16x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 58.3 ms: 1.16x slower                                                          |
| fannkuch                   | 293 ms                                                          | 340 ms: 1.16x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 188 us: 1.16x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.81 ms: 1.17x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 73.7 ns: 1.20x slower                                                          |
| generators                 | 22.1 ms                                                         | 26.8 ms: 1.21x slower                                                          |
| richards                   | 33.8 ms                                                         | 41.4 ms: 1.23x slower                                                          |
| raytrace                   | 205 ms                                                          | 252 ms: 1.23x slower                                                           |
| richards_super             | 38.0 ms                                                         | 46.8 ms: 1.23x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (7): sympy_sum, 2to3, bench_thread_pool, unpickle, go, json, async_tree_io
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown