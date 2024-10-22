# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.10x faster
- HPT reliability: 89.10%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 261 ms: 1.03x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.98 sec: 1.09x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.7 ms: 1.01x faster                                                          |
| tornado_http   | 104 ms                                                          | 107 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 782 ms: 1.08x faster                                                           |
| async_tree_none            | 246 ms                                                          | 229 ms: 1.07x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 288 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 479 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 458 ms: 1.01x faster                                                           |
| async_tree_io              | 537 ms                                                          | 546 ms: 1.02x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| async_generators           | 274 ms                                                          | 320 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 52.6 ms: 1.56x faster                                                          |
| float          | 57.8 ms                                                         | 42.5 ms: 1.36x faster                                                          |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 96.1 ms: 1.08x faster                                                          |
| regex_dna      | 117 ms                                                          | 120 ms: 1.03x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 2.00 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.54 sec: 1.13x faster                                                         |
| pickle_pure_python   | 238 us                                                          | 213 us: 1.12x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 147 us: 1.10x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 63.9 ms: 1.02x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| json_loads           | 21.0 us                                                         | 21.1 us: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 24.8 ms: 1.02x slower                                                          |
| python_startup_no_site | 19.9 ms                                                         | 20.8 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 7.31 ms                                                         | 5.43 ms: 1.35x faster                                                          |
| genshi_xml     | 49.5 ms                                                         | 53.5 ms: 1.08x slower                                                          |
| genshi_text    | 22.4 ms                                                         | 24.5 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 774 us: 13.11x faster                                                          |
| coverage                   | 333 ms                                                          | 51.8 ms: 6.43x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 16.4 us: 1.60x faster                                                          |
| nbody                      | 81.9 ms                                                         | 52.6 ms: 1.56x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 47.9 ms: 1.49x faster                                                          |
| scimark_sor                | 91.8 ms                                                         | 67.0 ms: 1.37x faster                                                          |
| float                      | 57.8 ms                                                         | 42.5 ms: 1.36x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.43 ms: 1.35x faster                                                          |
| fannkuch                   | 293 ms                                                          | 227 ms: 1.29x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.32 ms: 1.25x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 46.9 ms: 1.24x faster                                                          |
| scimark_fft                | 206 ms                                                          | 168 ms: 1.23x faster                                                           |
| pyflate                    | 326 ms                                                          | 269 ms: 1.21x faster                                                           |
| deepcopy                   | 307 us                                                          | 254 us: 1.21x faster                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 41.8 ms: 1.20x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.54 sec: 1.13x faster                                                         |
| deepcopy_reduce            | 2.85 us                                                         | 2.54 us: 1.12x faster                                                          |
| pickle_pure_python         | 238 us                                                          | 213 us: 1.12x faster                                                           |
| meteor_contest             | 77.0 ms                                                         | 69.0 ms: 1.12x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.01 ms: 1.11x faster                                                          |
| comprehensions             | 12.7 us                                                         | 11.5 us: 1.11x faster                                                          |
| unpickle_pure_python       | 162 us                                                          | 147 us: 1.10x faster                                                           |
| pprint_safe_repr           | 644 ms                                                          | 586 ms: 1.10x faster                                                           |
| pycparser                  | 869 ms                                                          | 793 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.20 sec: 1.08x faster                                                         |
| sqlglot_parse              | 1.05 ms                                                         | 973 us: 1.08x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 782 ms: 1.08x faster                                                           |
| regex_compile              | 103 ms                                                          | 96.1 ms: 1.08x faster                                                          |
| async_tree_none            | 246 ms                                                          | 229 ms: 1.07x faster                                                           |
| scimark_lu                 | 63.5 ms                                                         | 59.7 ms: 1.06x faster                                                          |
| logging_silent             | 61.6 ns                                                         | 58.2 ns: 1.06x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 288 ms: 1.05x faster                                                           |
| logging_simple             | 7.87 us                                                         | 7.62 us: 1.03x faster                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.25 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 479 ms: 1.03x faster                                                           |
| logging_format             | 8.57 us                                                         | 8.36 us: 1.02x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 63.9 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 458 ms: 1.01x faster                                                           |
| html5lib                   | 48.3 ms                                                         | 47.7 ms: 1.01x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 88.7 ms: 1.01x faster                                                          |
| json_loads                 | 21.0 us                                                         | 21.1 us: 1.01x slower                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.46 ms: 1.01x slower                                                          |
| chaos                      | 51.2 ms                                                         | 51.6 ms: 1.01x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 50.2 ms: 1.01x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.69 sec: 1.01x slower                                                         |
| async_tree_io              | 537 ms                                                          | 546 ms: 1.02x slower                                                           |
| python_startup             | 24.3 ms                                                         | 24.8 ms: 1.02x slower                                                          |
| tornado_http               | 104 ms                                                          | 107 ms: 1.02x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 77.2 ms: 1.03x slower                                                          |
| regex_dna                  | 117 ms                                                          | 120 ms: 1.03x slower                                                           |
| 2to3                       | 253 ms                                                          | 261 ms: 1.03x slower                                                           |
| sympy_str                  | 215 ms                                                          | 222 ms: 1.03x slower                                                           |
| go                         | 111 ms                                                          | 115 ms: 1.03x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| richards                   | 33.8 ms                                                         | 35.1 ms: 1.04x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 77.3 ms: 1.04x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 112 ms: 1.04x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 4.84 ms: 1.04x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 20.8 ms: 1.04x slower                                                          |
| sympy_expand               | 375 ms                                                          | 394 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 232 ms: 1.06x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 44.9 ms: 1.06x slower                                                          |
| genshi_xml                 | 49.5 ms                                                         | 53.5 ms: 1.08x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 771 us: 1.08x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.98 sec: 1.09x slower                                                         |
| genshi_text                | 22.4 ms                                                         | 24.5 ms: 1.09x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 16.6 ms: 1.09x slower                                                          |
| richards_super             | 38.0 ms                                                         | 41.7 ms: 1.10x slower                                                          |
| raytrace                   | 205 ms                                                          | 227 ms: 1.11x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 2.00 ms: 1.11x slower                                                          |
| generators                 | 22.1 ms                                                         | 24.7 ms: 1.12x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 153 us: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| pylint                     | 225 ms                                                          | 257 ms: 1.14x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.75 ms: 1.14x slower                                                          |
| async_generators           | 274 ms                                                          | 320 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (5): async_tree_io_tg, bench_thread_pool, xml_etree_process, django_template, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 89.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown