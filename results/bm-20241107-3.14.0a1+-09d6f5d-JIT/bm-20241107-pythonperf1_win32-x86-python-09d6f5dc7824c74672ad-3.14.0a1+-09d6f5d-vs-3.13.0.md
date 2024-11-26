# Results vs. 3.13.0

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: windows-x86
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.064x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 293 ms: 1.15x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.14 sec: 1.19x slower                                                          |
| html5lib       | 47.1 ms                                                         | 49.9 ms: 1.06x slower                                                           |
| sphinx         | 729 ms                                                          | 901 ms: 1.24x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 276 ms: 1.04x faster                                                            |
| async_tree_none_tg         | 216 ms                                                          | 221 ms: 1.02x slower                                                            |
| coroutines                 | 16.1 ms                                                         | 16.5 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 483 ms: 1.03x slower                                                            |
| async_tree_io              | 530 ms                                                          | 547 ms: 1.03x slower                                                            |
| asyncio_websockets         | 352 ms                                                          | 365 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 516 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 499 ms                                                          | 568 ms: 1.14x slower                                                            |
| async_generators           | 267 ms                                                          | 330 ms: 1.24x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (2): async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 55.8 ms: 1.01x faster                                                           |
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| nbody          | 81.4 ms                                                         | 98.5 ms: 1.21x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                           |
| regex_dna      | 112 ms                                                          | 116 ms: 1.03x slower                                                            |
| regex_compile  | 101 ms                                                          | 121 ms: 1.20x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.4 us: 1.01x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.83 sec: 1.05x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 114 ms: 1.11x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 70.0 ms: 1.14x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 71.8 ms: 1.16x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 8.80 ms: 1.17x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 192 us: 1.18x slower                                                            |
| xml_etree_process    | 44.6 ms                                                         | 53.6 ms: 1.20x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 301 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.8 ms: 1.05x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.39 ms: 1.05x slower                                                           |
| django_template | 32.0 ms                                                         | 36.3 ms: 1.13x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 58.5 ms: 1.19x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 26.4 ms: 1.22x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 779 us: 13.18x faster                                                           |
| coverage                   | 326 ms                                                          | 52.1 ms: 6.27x faster                                                           |
| sqlglot_normalize          | 223 ms                                                          | 115 ms: 1.94x faster                                                            |
| deepcopy                   | 311 us                                                          | 274 us: 1.13x faster                                                            |
| deepcopy_memo              | 26.2 us                                                         | 23.8 us: 1.10x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 82.0 ms: 1.09x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.76 us: 1.07x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.8 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 276 ms: 1.04x faster                                                            |
| dulwich_log                | 50.2 ms                                                         | 49.3 ms: 1.02x faster                                                           |
| float                      | 56.4 ms                                                         | 55.8 ms: 1.01x faster                                                           |
| json_loads                 | 21.7 us                                                         | 21.4 us: 1.01x faster                                                           |
| pidigits                   | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| bench_mp_pool              | 93.6 ms                                                         | 92.9 ms: 1.01x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                           |
| async_tree_none_tg         | 216 ms                                                          | 221 ms: 1.02x slower                                                            |
| coroutines                 | 16.1 ms                                                         | 16.5 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 483 ms: 1.03x slower                                                            |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.03x slower                                                            |
| logging_format             | 8.59 us                                                         | 8.85 us: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                          | 547 ms: 1.03x slower                                                            |
| asyncio_websockets         | 352 ms                                                          | 365 ms: 1.04x slower                                                            |
| logging_simple             | 7.89 us                                                         | 8.25 us: 1.04x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.83 sec: 1.05x slower                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 516 ms: 1.05x slower                                                            |
| mako                       | 7.02 ms                                                         | 7.39 ms: 1.05x slower                                                           |
| html5lib                   | 47.1 ms                                                         | 49.9 ms: 1.06x slower                                                           |
| shortest_path              | 298 ms                                                          | 317 ms: 1.06x slower                                                            |
| pycparser                  | 869 ms                                                          | 931 ms: 1.07x slower                                                            |
| create_gc_cycles           | 1.08 ms                                                         | 1.17 ms: 1.08x slower                                                           |
| connected_components       | 266 ms                                                          | 288 ms: 1.08x slower                                                            |
| xml_etree_parse            | 102 ms                                                          | 114 ms: 1.11x slower                                                            |
| mdp                        | 1.70 sec                                                        | 1.89 sec: 1.11x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.22 ms: 1.12x slower                                                           |
| sympy_expand               | 377 ms                                                          | 422 ms: 1.12x slower                                                            |
| telco                      | 6.27 ms                                                         | 7.08 ms: 1.13x slower                                                           |
| pprint_safe_repr           | 658 ms                                                          | 743 ms: 1.13x slower                                                            |
| spectral_norm              | 70.0 ms                                                         | 79.2 ms: 1.13x slower                                                           |
| fannkuch                   | 288 ms                                                          | 326 ms: 1.13x slower                                                            |
| bpe_tokeniser              | 3.49 sec                                                        | 3.96 sec: 1.13x slower                                                          |
| django_template            | 32.0 ms                                                         | 36.3 ms: 1.13x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.50 sec: 1.14x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 568 ms: 1.14x slower                                                            |
| xml_etree_iterparse        | 61.3 ms                                                         | 70.0 ms: 1.14x slower                                                           |
| 2to3                       | 255 ms                                                          | 293 ms: 1.15x slower                                                            |
| scimark_lu                 | 60.7 ms                                                         | 69.7 ms: 1.15x slower                                                           |
| go                         | 111 ms                                                          | 127 ms: 1.15x slower                                                            |
| sqlglot_parse              | 1.02 ms                                                         | 1.18 ms: 1.15x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 90.4 ms: 1.16x slower                                                           |
| sympy_str                  | 214 ms                                                          | 248 ms: 1.16x slower                                                            |
| xml_etree_generate         | 61.9 ms                                                         | 71.8 ms: 1.16x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 125 ms: 1.16x slower                                                            |
| scimark_sor                | 85.8 ms                                                         | 99.7 ms: 1.16x slower                                                           |
| json_dumps                 | 7.53 ms                                                         | 8.80 ms: 1.17x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 167 us: 1.18x slower                                                            |
| unpickle_pure_python       | 162 us                                                          | 192 us: 1.18x slower                                                            |
| crypto_pyaes               | 56.6 ms                                                         | 67.1 ms: 1.19x slower                                                           |
| docutils                   | 1.80 sec                                                        | 2.14 sec: 1.19x slower                                                          |
| genshi_xml                 | 49.0 ms                                                         | 58.5 ms: 1.19x slower                                                           |
| xml_etree_process          | 44.6 ms                                                         | 53.6 ms: 1.20x slower                                                           |
| regex_compile              | 101 ms                                                          | 121 ms: 1.20x slower                                                            |
| nbody                      | 81.4 ms                                                         | 98.5 ms: 1.21x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.53 ms: 1.21x slower                                                           |
| scimark_fft                | 204 ms                                                          | 247 ms: 1.21x slower                                                            |
| genshi_text                | 21.7 ms                                                         | 26.4 ms: 1.22x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 76.9 ns: 1.23x slower                                                           |
| pyflate                    | 322 ms                                                          | 398 ms: 1.24x slower                                                            |
| async_generators           | 267 ms                                                          | 330 ms: 1.24x slower                                                            |
| sphinx                     | 729 ms                                                          | 901 ms: 1.24x slower                                                            |
| pickle_pure_python         | 239 us                                                          | 301 us: 1.26x slower                                                            |
| scimark_monte_carlo        | 48.7 ms                                                         | 62.1 ms: 1.27x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 19.5 ms: 1.28x slower                                                           |
| chaos                      | 49.4 ms                                                         | 63.3 ms: 1.28x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 97.0 ms: 1.29x slower                                                           |
| pylint                     | 225 ms                                                          | 293 ms: 1.30x slower                                                            |
| sqlglot_optimize           | 42.4 ms                                                         | 56.6 ms: 1.34x slower                                                           |
| richards                   | 33.4 ms                                                         | 45.5 ms: 1.36x slower                                                           |
| richards_super             | 37.0 ms                                                         | 51.3 ms: 1.38x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 3.29 ms: 1.40x slower                                                           |
| comprehensions             | 13.1 us                                                         | 18.4 us: 1.40x slower                                                           |
| k_core                     | 1.43 sec                                                        | 2.05 sec: 1.43x slower                                                          |
| raytrace                   | 203 ms                                                          | 314 ms: 1.55x slower                                                            |
| hexiom                     | 4.60 ms                                                         | 7.19 ms: 1.56x slower                                                           |
| generators                 | 21.5 ms                                                         | 35.8 ms: 1.67x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                                    |

Benchmark hidden because not significant (6): regex_effbot, async_tree_none, json, async_tree_memoization, gc_traversal, bench_thread_pool
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.064x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown