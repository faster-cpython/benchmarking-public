# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-x86
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.06x faster
- HPT reliability: 78.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 265 ms: 1.05x slower                                                            |
| docutils       | 1.82 sec                                                        | 2.03 sec: 1.11x slower                                                          |
| html5lib       | 48.3 ms                                                         | 44.6 ms: 1.08x faster                                                           |
| tornado_http   | 104 ms                                                          | 108 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                            |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.12x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 219 ms                                                          | 199 ms: 1.10x faster                                                            |
| async_tree_io              | 537 ms                                                          | 514 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 499 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 483 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 509 ms                                                          | 543 ms: 1.07x slower                                                            |
| coroutines                 | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                           |
| async_generators           | 274 ms                                                          | 324 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 65.2 ms: 1.26x faster                                                           |
| float          | 57.8 ms                                                         | 46.1 ms: 1.25x faster                                                           |
| pidigits       | 202 ms                                                          | 201 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.4 ms: 1.01x faster                                                           |
| regex_compile  | 103 ms                                                          | 104 ms: 1.01x slower                                                            |
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                            |
| regex_effbot   | 1.81 ms                                                         | 1.86 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|---------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 1.73 sec                                                        | 1.49 sec: 1.16x faster                                                          |
| xml_etree_generate  | 62.6 ms                                                         | 55.8 ms: 1.12x faster                                                           |
| xml_etree_process   | 45.0 ms                                                         | 40.5 ms: 1.11x faster                                                           |
| unpickle_list       | 3.09 us                                                         | 2.96 us: 1.05x faster                                                           |
| pickle_pure_python  | 238 us                                                          | 230 us: 1.03x faster                                                            |
| unpickle            | 10.5 us                                                         | 10.3 us: 1.03x faster                                                           |
| pickle_dict         | 21.7 us                                                         | 21.2 us: 1.02x faster                                                           |
| xml_etree_iterparse | 65.1 ms                                                         | 63.8 ms: 1.02x faster                                                           |
| json_loads          | 21.0 us                                                         | 20.6 us: 1.02x faster                                                           |
| json_dumps          | 7.40 ms                                                         | 8.31 ms: 1.12x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_list, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                           |
| python_startup         | 24.3 ms                                                         | 26.7 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.75 ms: 1.27x faster                                                           |
| django_template | 32.7 ms                                                         | 32.1 ms: 1.02x faster                                                           |
| genshi_text     | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| genshi_xml      | 49.5 ms                                                         | 53.8 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 767 us: 13.23x faster                                                           |
| coverage                   | 333 ms                                                          | 53.5 ms: 6.23x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 17.0 us: 1.54x faster                                                           |
| scimark_sor                | 91.8 ms                                                         | 68.5 ms: 1.34x faster                                                           |
| deepcopy                   | 307 us                                                          | 236 us: 1.30x faster                                                            |
| mako                       | 7.31 ms                                                         | 5.75 ms: 1.27x faster                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 39.6 ms: 1.27x faster                                                           |
| nbody                      | 81.9 ms                                                         | 65.2 ms: 1.26x faster                                                           |
| float                      | 57.8 ms                                                         | 46.1 ms: 1.25x faster                                                           |
| spectral_norm              | 71.3 ms                                                         | 57.8 ms: 1.23x faster                                                           |
| fannkuch                   | 293 ms                                                          | 248 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 2.85 us                                                         | 2.43 us: 1.17x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.50 ms: 1.16x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.49 sec: 1.16x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 50.2 ms: 1.16x faster                                                           |
| go                         | 111 ms                                                          | 96.6 ms: 1.15x faster                                                           |
| scimark_fft                | 206 ms                                                          | 180 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                            |
| xml_etree_generate         | 62.6 ms                                                         | 55.8 ms: 1.12x faster                                                           |
| async_tree_none            | 246 ms                                                          | 219 ms: 1.12x faster                                                            |
| xml_etree_process          | 45.0 ms                                                         | 40.5 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                            |
| pprint_safe_repr           | 644 ms                                                          | 585 ms: 1.10x faster                                                            |
| telco                      | 6.67 ms                                                         | 6.08 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 199 ms: 1.10x faster                                                            |
| logging_silent             | 61.6 ns                                                         | 56.2 ns: 1.10x faster                                                           |
| html5lib                   | 48.3 ms                                                         | 44.6 ms: 1.08x faster                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.21 sec: 1.07x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.36 us: 1.07x faster                                                           |
| scimark_lu                 | 63.5 ms                                                         | 59.5 ms: 1.07x faster                                                           |
| meteor_contest             | 77.0 ms                                                         | 72.1 ms: 1.07x faster                                                           |
| unpack_sequence            | 42.9 ns                                                         | 40.5 ns: 1.06x faster                                                           |
| pycparser                  | 869 ms                                                          | 821 ms: 1.06x faster                                                            |
| logging_format             | 8.57 us                                                         | 8.11 us: 1.06x faster                                                           |
| unpickle_list              | 3.09 us                                                         | 2.96 us: 1.05x faster                                                           |
| async_tree_io              | 537 ms                                                          | 514 ms: 1.04x faster                                                            |
| pickle_pure_python         | 238 us                                                          | 230 us: 1.03x faster                                                            |
| pyflate                    | 326 ms                                                          | 316 ms: 1.03x faster                                                            |
| bench_thread_pool          | 1.02 ms                                                         | 995 us: 1.03x faster                                                            |
| unpickle                   | 10.5 us                                                         | 10.3 us: 1.03x faster                                                           |
| sqlite_synth               | 1.97 us                                                         | 1.92 us: 1.02x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 21.2 us: 1.02x faster                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 63.8 ms: 1.02x faster                                                           |
| django_template            | 32.7 ms                                                         | 32.1 ms: 1.02x faster                                                           |
| json_loads                 | 21.0 us                                                         | 20.6 us: 1.02x faster                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 1.04 ms: 1.01x faster                                                           |
| regex_v8                   | 15.6 ms                                                         | 15.4 ms: 1.01x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 88.5 ms: 1.01x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 74.6 ms: 1.01x faster                                                           |
| pidigits                   | 202 ms                                                          | 201 ms: 1.01x faster                                                            |
| regex_compile              | 103 ms                                                          | 104 ms: 1.01x slower                                                            |
| genshi_text                | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 499 ms: 1.01x slower                                                            |
| regex_dna                  | 117 ms                                                          | 118 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.86 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.34 ms: 1.03x slower                                                           |
| tornado_http               | 104 ms                                                          | 108 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 136 us                                                          | 141 us: 1.04x slower                                                            |
| mdp                        | 1.67 sec                                                        | 1.74 sec: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 483 ms: 1.04x slower                                                            |
| 2to3                       | 253 ms                                                          | 265 ms: 1.05x slower                                                            |
| sympy_expand               | 375 ms                                                          | 394 ms: 1.05x slower                                                            |
| deltablue                  | 2.41 ms                                                         | 2.53 ms: 1.05x slower                                                           |
| sympy_str                  | 215 ms                                                          | 229 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 509 ms                                                          | 543 ms: 1.07x slower                                                            |
| chaos                      | 51.2 ms                                                         | 55.1 ms: 1.08x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 116 ms: 1.08x slower                                                            |
| sqlglot_normalize          | 220 ms                                                          | 239 ms: 1.08x slower                                                            |
| genshi_xml                 | 49.5 ms                                                         | 53.8 ms: 1.09x slower                                                           |
| python_startup             | 24.3 ms                                                         | 26.7 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                           |
| docutils                   | 1.82 sec                                                        | 2.03 sec: 1.11x slower                                                          |
| richards_super             | 38.0 ms                                                         | 42.3 ms: 1.12x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.31 ms: 1.12x slower                                                           |
| generators                 | 22.1 ms                                                         | 24.9 ms: 1.13x slower                                                           |
| richards                   | 33.8 ms                                                         | 38.3 ms: 1.13x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.4 ms: 1.15x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 49.2 ms: 1.16x slower                                                           |
| json                       | 4.27 ms                                                         | 4.99 ms: 1.17x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.46 ms: 1.18x slower                                                           |
| async_generators           | 274 ms                                                          | 324 ms: 1.18x slower                                                            |
| gc_traversal               | 1.45 ms                                                         | 1.80 ms: 1.24x slower                                                           |
| pylint                     | 225 ms                                                          | 283 ms: 1.26x slower                                                            |
| bench_mp_pool              | 74.3 ms                                                         | 94.3 ms: 1.27x slower                                                           |
| raytrace                   | 205 ms                                                          | 271 ms: 1.32x slower                                                            |
| create_gc_cycles           | 713 us                                                          | 1.20 ms: 1.69x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (8): asyncio_tcp, dulwich_log, comprehensions, unpickle_pure_python, pickle_list, pickle, asyncio_tcp_ssl, xml_etree_parse
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx

# HPT report

- Reliability score: 78.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown