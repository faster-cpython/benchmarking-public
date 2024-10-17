# Results vs. 3.13.0b2

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-amd64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 247 ms: 1.19x slower                                                        |
| docutils       | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                      |
| html5lib       | 35.0 ms                                                         | 39.7 ms: 1.14x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 98.1 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                           | 1.18x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 588 ms                                                          | 554 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 202 ms                                                          | 209 ms: 1.03x slower                                                        |
| async_tree_memoization     | 264 ms                                                          | 276 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 400 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 605 ms                                                          | 635 ms: 1.05x slower                                                        |
| async_tree_none            | 218 ms                                                          | 234 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 54.7 ms: 1.24x faster                                                       |
| float          | 49.7 ms                                                         | 47.5 ms: 1.05x faster                                                       |
| pidigits       | 150 ms                                                          | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 123 ms: 1.03x slower                                                        |
| regex_effbot   | 1.58 ms                                                         | 1.65 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 91.5 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.71 us: 1.07x faster                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 51.1 ms: 1.04x faster                                                       |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                       |
| pickle               | 7.11 us                                                         | 7.21 us: 1.01x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                                       |
| unpickle             | 8.40 us                                                         | 9.04 us: 1.08x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.87 us: 1.09x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 197 us: 1.12x slower                                                        |
| json_dumps           | 5.61 ms                                                         | 6.37 ms: 1.13x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 142 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                |

Benchmark hidden because not significant (2): json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                       |
| python_startup         | 20.3 ms                                                         | 23.9 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.94 ms: 1.29x faster                                                       |
| django_template | 21.7 ms                                                         | 27.0 ms: 1.25x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 19.6 ms: 1.36x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 46.3 ms: 1.47x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 513 us: 15.79x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 16.4 us: 1.35x faster                                                       |
| mako                       | 6.36 ms                                                         | 4.94 ms: 1.29x faster                                                       |
| nbody                      | 67.6 ms                                                         | 54.7 ms: 1.24x faster                                                       |
| scimark_sor                | 75.3 ms                                                         | 64.0 ms: 1.18x faster                                                       |
| spectral_norm              | 63.7 ms                                                         | 54.5 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.18 ms: 1.15x faster                                                       |
| deepcopy                   | 220 us                                                          | 192 us: 1.14x faster                                                        |
| crypto_pyaes               | 45.5 ms                                                         | 39.8 ms: 1.14x faster                                                       |
| scimark_fft                | 171 ms                                                          | 154 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 39.1 ms                                                         | 36.1 ms: 1.08x faster                                                       |
| telco                      | 4.67 ms                                                         | 4.34 ms: 1.08x faster                                                       |
| pickle_list                | 2.90 us                                                         | 2.71 us: 1.07x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.88 us: 1.06x faster                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                      |
| async_tree_io              | 588 ms                                                          | 554 ms: 1.06x faster                                                        |
| json                       | 3.19 ms                                                         | 3.01 ms: 1.06x faster                                                       |
| fannkuch                   | 243 ms                                                          | 231 ms: 1.05x faster                                                        |
| float                      | 49.7 ms                                                         | 47.5 ms: 1.05x faster                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 51.1 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 474 ms                                                          | 458 ms: 1.03x faster                                                        |
| pprint_pformat             | 966 ms                                                          | 935 ms: 1.03x faster                                                        |
| pickle_dict                | 18.1 us                                                         | 17.6 us: 1.03x faster                                                       |
| scimark_lu                 | 56.6 ms                                                         | 55.4 ms: 1.02x faster                                                       |
| pidigits                   | 150 ms                                                          | 148 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                       |
| pickle                     | 7.11 us                                                         | 7.21 us: 1.01x slower                                                       |
| regex_dna                  | 119 ms                                                          | 123 ms: 1.03x slower                                                        |
| async_tree_none_tg         | 202 ms                                                          | 209 ms: 1.03x slower                                                        |
| pyflate                    | 279 ms                                                          | 289 ms: 1.04x slower                                                        |
| regex_effbot               | 1.58 ms                                                         | 1.65 ms: 1.04x slower                                                       |
| async_tree_memoization     | 264 ms                                                          | 276 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 400 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 605 ms                                                          | 635 ms: 1.05x slower                                                        |
| xml_etree_parse            | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 80.5 ms: 1.06x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 40.4 ms: 1.06x slower                                                       |
| logging_format             | 6.22 us                                                         | 6.62 us: 1.06x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.17 us: 1.07x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 56.5 ns: 1.07x slower                                                       |
| async_tree_none            | 218 ms                                                          | 234 ms: 1.07x slower                                                        |
| unpickle                   | 8.40 us                                                         | 9.04 us: 1.08x slower                                                       |
| bench_thread_pool          | 768 us                                                          | 827 us: 1.08x slower                                                        |
| coroutines                 | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 75.5 ms: 1.08x slower                                                       |
| chaos                      | 38.4 ms                                                         | 41.7 ms: 1.09x slower                                                       |
| unpickle_list              | 2.62 us                                                         | 2.87 us: 1.09x slower                                                       |
| comprehensions             | 10.4 us                                                         | 11.4 us: 1.10x slower                                                       |
| go                         | 82.1 ms                                                         | 91.2 ms: 1.11x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 63.5 ms: 1.12x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 197 us: 1.12x slower                                                        |
| typing_runtime_protocols   | 101 us                                                          | 113 us: 1.12x slower                                                        |
| json_dumps                 | 5.61 ms                                                         | 6.37 ms: 1.13x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 39.7 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                       |
| coverage                   | 42.1 ms                                                         | 48.0 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 142 us: 1.16x slower                                                        |
| async_generators           | 223 ms                                                          | 260 ms: 1.16x slower                                                        |
| regex_compile              | 78.0 ms                                                         | 91.5 ms: 1.17x slower                                                       |
| generators                 | 19.6 ms                                                         | 23.0 ms: 1.18x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                      |
| python_startup             | 20.3 ms                                                         | 23.9 ms: 1.18x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.56 sec: 1.19x slower                                                      |
| 2to3                       | 207 ms                                                          | 247 ms: 1.19x slower                                                        |
| sqlglot_normalize          | 173 ms                                                          | 207 ms: 1.20x slower                                                        |
| tornado_http               | 81.8 ms                                                         | 98.1 ms: 1.20x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 897 us: 1.20x slower                                                        |
| sympy_expand               | 271 ms                                                          | 325 ms: 1.20x slower                                                        |
| sympy_str                  | 159 ms                                                          | 192 ms: 1.21x slower                                                        |
| sympy_sum                  | 84.4 ms                                                         | 103 ms: 1.22x slower                                                        |
| sqlglot_transpile          | 955 us                                                          | 1.18 ms: 1.23x slower                                                       |
| django_template            | 21.7 ms                                                         | 27.0 ms: 1.25x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.96 ms: 1.26x slower                                                       |
| richards                   | 26.7 ms                                                         | 34.0 ms: 1.27x slower                                                       |
| richards_super             | 30.2 ms                                                         | 38.5 ms: 1.28x slower                                                       |
| sympy_integrate            | 12.2 ms                                                         | 15.8 ms: 1.29x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 43.2 ms: 1.32x slower                                                       |
| raytrace                   | 162 ms                                                          | 215 ms: 1.33x slower                                                        |
| pylint                     | 205 ms                                                          | 279 ms: 1.36x slower                                                        |
| genshi_text                | 14.4 ms                                                         | 19.6 ms: 1.36x slower                                                       |
| bench_mp_pool              | 64.8 ms                                                         | 89.8 ms: 1.39x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 5.21 ms: 1.40x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 665 ms: 1.41x slower                                                        |
| genshi_xml                 | 31.6 ms                                                         | 46.3 ms: 1.47x slower                                                       |
| create_gc_cycles           | 888 us                                                          | 1.41 ms: 1.58x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                |

Benchmark hidden because not significant (8): regex_v8, async_tree_cpu_io_mixed, sqlite_synth, pycparser, json_loads, xml_etree_process, async_tree_memoization_tg, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown