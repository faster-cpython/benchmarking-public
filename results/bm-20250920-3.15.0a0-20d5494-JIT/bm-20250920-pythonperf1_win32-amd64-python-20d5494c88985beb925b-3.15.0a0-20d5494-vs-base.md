# Results vs. base

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.039x faster
- HPT reliability: 96.06%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                                                                                     | 222 ms: 1.03x slower                                                                                                           |
| docutils       | 1.59 sec                                                                                                                   | 1.66 sec: 1.04x slower                                                                                                         |
| sphinx         | 625 ms                                                                                                                     | 639 ms: 1.02x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.03x slower                                                                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                | 491 ms                                                                                                                     | 472 ms: 1.04x faster                                                                                                           |
| asyncio_tcp_ssl            | 1.37 sec                                                                                                                   | 1.38 sec: 1.01x slower                                                                                                         |
| async_tree_cpu_io_mixed    | 328 ms                                                                                                                     | 331 ms: 1.01x slower                                                                                                           |
| async_tree_io_tg           | 379 ms                                                                                                                     | 385 ms: 1.02x slower                                                                                                           |
| async_tree_cpu_io_mixed_tg | 332 ms                                                                                                                     | 339 ms: 1.02x slower                                                                                                           |
| async_tree_memoization_tg  | 205 ms                                                                                                                     | 210 ms: 1.02x slower                                                                                                           |
| async_tree_none            | 169 ms                                                                                                                     | 173 ms: 1.02x slower                                                                                                           |
| async_tree_memoization     | 200 ms                                                                                                                     | 206 ms: 1.03x slower                                                                                                           |
| async_generators           | 227 ms                                                                                                                     | 246 ms: 1.08x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (4): coroutines, async_tree_none_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.9 ms                                                                                                                    | 55.0 ms: 1.16x faster                                                                                                          |
| float          | 42.0 ms                                                                                                                    | 39.7 ms: 1.06x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.53 ms                                                                                                                    | 1.54 ms: 1.01x slower                                                                                                          |
| regex_dna      | 120 ms                                                                                                                     | 121 ms: 1.01x slower                                                                                                           |
| regex_v8       | 13.9 ms                                                                                                                    | 14.2 ms: 1.02x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 132 us                                                                                                                     | 107 us: 1.24x faster                                                                                                           |
| tomli_loads          | 1.33 sec                                                                                                                   | 1.10 sec: 1.22x faster                                                                                                         |
| xml_etree_generate   | 55.0 ms                                                                                                                    | 49.8 ms: 1.11x faster                                                                                                          |
| xml_etree_process    | 38.3 ms                                                                                                                    | 35.2 ms: 1.09x faster                                                                                                          |
| pickle_pure_python   | 213 us                                                                                                                     | 199 us: 1.07x faster                                                                                                           |
| unpickle_list        | 2.80 us                                                                                                                    | 2.72 us: 1.03x faster                                                                                                          |
| json_loads           | 14.3 us                                                                                                                    | 14.0 us: 1.02x faster                                                                                                          |
| xml_etree_iterparse  | 62.4 ms                                                                                                                    | 61.7 ms: 1.01x faster                                                                                                          |
| pickle_dict          | 19.8 us                                                                                                                    | 19.9 us: 1.01x slower                                                                                                          |
| xml_etree_parse      | 85.3 ms                                                                                                                    | 86.2 ms: 1.01x slower                                                                                                          |
| json_dumps           | 5.31 ms                                                                                                                    | 5.38 ms: 1.01x slower                                                                                                          |
| pickle_list          | 3.32 us                                                                                                                    | 3.38 us: 1.02x slower                                                                                                          |
| unpickle             | 8.31 us                                                                                                                    | 8.47 us: 1.02x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.3 ms                                                                                                                    | 25.5 ms: 1.01x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.66 ms                                                                                                                    | 5.26 ms: 1.27x faster                                                                                                          |
| genshi_xml     | 34.3 ms                                                                                                                    | 35.1 ms: 1.02x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| bench_thread_pool          | 8.12 ms                                                                                                                    | 851 us: 9.55x faster                                                                                                           |
| mako                       | 6.66 ms                                                                                                                    | 5.26 ms: 1.27x faster                                                                                                          |
| unpickle_pure_python       | 132 us                                                                                                                     | 107 us: 1.24x faster                                                                                                           |
| tomli_loads                | 1.33 sec                                                                                                                   | 1.10 sec: 1.22x faster                                                                                                         |
| fannkuch                   | 257 ms                                                                                                                     | 212 ms: 1.21x faster                                                                                                           |
| scimark_fft                | 179 ms                                                                                                                     | 149 ms: 1.20x faster                                                                                                           |
| bpe_tokeniser              | 2.96 sec                                                                                                                   | 2.52 sec: 1.17x faster                                                                                                         |
| nbody                      | 63.9 ms                                                                                                                    | 55.0 ms: 1.16x faster                                                                                                          |
| pprint_safe_repr           | 490 ms                                                                                                                     | 430 ms: 1.14x faster                                                                                                           |
| pprint_pformat             | 995 ms                                                                                                                     | 873 ms: 1.14x faster                                                                                                           |
| pyflate                    | 280 ms                                                                                                                     | 253 ms: 1.11x faster                                                                                                           |
| xml_etree_generate         | 55.0 ms                                                                                                                    | 49.8 ms: 1.11x faster                                                                                                          |
| scimark_sparse_mat_mult    | 2.55 ms                                                                                                                    | 2.32 ms: 1.10x faster                                                                                                          |
| xml_etree_process          | 38.3 ms                                                                                                                    | 35.2 ms: 1.09x faster                                                                                                          |
| telco                      | 4.29 ms                                                                                                                    | 3.98 ms: 1.08x faster                                                                                                          |
| pickle_pure_python         | 213 us                                                                                                                     | 199 us: 1.07x faster                                                                                                           |
| float                      | 42.0 ms                                                                                                                    | 39.7 ms: 1.06x faster                                                                                                          |
| sqlglot_v2_parse           | 813 us                                                                                                                     | 779 us: 1.04x faster                                                                                                           |
| asyncio_tcp                | 491 ms                                                                                                                     | 472 ms: 1.04x faster                                                                                                           |
| k_core                     | 1.67 sec                                                                                                                   | 1.61 sec: 1.04x faster                                                                                                         |
| sqlglot_v2_transpile       | 1.01 ms                                                                                                                    | 984 us: 1.03x faster                                                                                                           |
| unpickle_list              | 2.80 us                                                                                                                    | 2.72 us: 1.03x faster                                                                                                          |
| coverage                   | 50.4 ms                                                                                                                    | 49.1 ms: 1.03x faster                                                                                                          |
| logging_silent             | 55.4 ns                                                                                                                    | 54.2 ns: 1.02x faster                                                                                                          |
| json_loads                 | 14.3 us                                                                                                                    | 14.0 us: 1.02x faster                                                                                                          |
| crypto_pyaes               | 47.0 ms                                                                                                                    | 46.0 ms: 1.02x faster                                                                                                          |
| scimark_lu                 | 58.7 ms                                                                                                                    | 57.8 ms: 1.01x faster                                                                                                          |
| comprehensions             | 10.9 us                                                                                                                    | 10.7 us: 1.01x faster                                                                                                          |
| xml_etree_iterparse        | 62.4 ms                                                                                                                    | 61.7 ms: 1.01x faster                                                                                                          |
| scimark_monte_carlo        | 40.6 ms                                                                                                                    | 40.5 ms: 1.00x faster                                                                                                          |
| shortest_path              | 355 ms                                                                                                                     | 357 ms: 1.01x slower                                                                                                           |
| pickle_dict                | 19.8 us                                                                                                                    | 19.9 us: 1.01x slower                                                                                                          |
| raytrace                   | 176 ms                                                                                                                     | 177 ms: 1.01x slower                                                                                                           |
| python_startup             | 25.3 ms                                                                                                                    | 25.5 ms: 1.01x slower                                                                                                          |
| regex_effbot               | 1.53 ms                                                                                                                    | 1.54 ms: 1.01x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.37 sec                                                                                                                   | 1.38 sec: 1.01x slower                                                                                                         |
| xml_etree_parse            | 85.3 ms                                                                                                                    | 86.2 ms: 1.01x slower                                                                                                          |
| async_tree_cpu_io_mixed    | 328 ms                                                                                                                     | 331 ms: 1.01x slower                                                                                                           |
| regex_dna                  | 120 ms                                                                                                                     | 121 ms: 1.01x slower                                                                                                           |
| json_dumps                 | 5.31 ms                                                                                                                    | 5.38 ms: 1.01x slower                                                                                                          |
| deepcopy_memo              | 16.7 us                                                                                                                    | 16.9 us: 1.01x slower                                                                                                          |
| create_gc_cycles           | 1.27 ms                                                                                                                    | 1.29 ms: 1.02x slower                                                                                                          |
| sqlglot_v2_normalize       | 69.7 ms                                                                                                                    | 70.9 ms: 1.02x slower                                                                                                          |
| pickle_list                | 3.32 us                                                                                                                    | 3.38 us: 1.02x slower                                                                                                          |
| meteor_contest             | 71.5 ms                                                                                                                    | 72.7 ms: 1.02x slower                                                                                                          |
| async_tree_io_tg           | 379 ms                                                                                                                     | 385 ms: 1.02x slower                                                                                                           |
| gc_traversal               | 2.10 ms                                                                                                                    | 2.14 ms: 1.02x slower                                                                                                          |
| generators                 | 19.2 ms                                                                                                                    | 19.5 ms: 1.02x slower                                                                                                          |
| deepcopy                   | 164 us                                                                                                                     | 167 us: 1.02x slower                                                                                                           |
| unpickle                   | 8.31 us                                                                                                                    | 8.47 us: 1.02x slower                                                                                                          |
| async_tree_cpu_io_mixed_tg | 332 ms                                                                                                                     | 339 ms: 1.02x slower                                                                                                           |
| sympy_str                  | 167 ms                                                                                                                     | 171 ms: 1.02x slower                                                                                                           |
| genshi_xml                 | 34.3 ms                                                                                                                    | 35.1 ms: 1.02x slower                                                                                                          |
| sphinx                     | 625 ms                                                                                                                     | 639 ms: 1.02x slower                                                                                                           |
| async_tree_memoization_tg  | 205 ms                                                                                                                     | 210 ms: 1.02x slower                                                                                                           |
| chaos                      | 40.1 ms                                                                                                                    | 41.1 ms: 1.02x slower                                                                                                          |
| regex_v8                   | 13.9 ms                                                                                                                    | 14.2 ms: 1.02x slower                                                                                                          |
| async_tree_none            | 169 ms                                                                                                                     | 173 ms: 1.02x slower                                                                                                           |
| sympy_sum                  | 85.0 ms                                                                                                                    | 87.4 ms: 1.03x slower                                                                                                          |
| go                         | 74.2 ms                                                                                                                    | 76.4 ms: 1.03x slower                                                                                                          |
| deepcopy_reduce            | 1.76 us                                                                                                                    | 1.81 us: 1.03x slower                                                                                                          |
| 2to3                       | 215 ms                                                                                                                     | 222 ms: 1.03x slower                                                                                                           |
| async_tree_memoization     | 200 ms                                                                                                                     | 206 ms: 1.03x slower                                                                                                           |
| sqlglot_v2_optimize        | 33.7 ms                                                                                                                    | 34.7 ms: 1.03x slower                                                                                                          |
| logging_simple             | 5.86 us                                                                                                                    | 6.03 us: 1.03x slower                                                                                                          |
| hexiom                     | 4.00 ms                                                                                                                    | 4.12 ms: 1.03x slower                                                                                                          |
| mdp                        | 793 ms                                                                                                                     | 820 ms: 1.03x slower                                                                                                           |
| deltablue                  | 2.14 ms                                                                                                                    | 2.22 ms: 1.04x slower                                                                                                          |
| subparsers                 | 30.3 ms                                                                                                                    | 31.4 ms: 1.04x slower                                                                                                          |
| sympy_integrate            | 12.2 ms                                                                                                                    | 12.7 ms: 1.04x slower                                                                                                          |
| docutils                   | 1.59 sec                                                                                                                   | 1.66 sec: 1.04x slower                                                                                                         |
| many_optionals             | 561 us                                                                                                                     | 587 us: 1.05x slower                                                                                                           |
| dulwich_log                | 38.9 ms                                                                                                                    | 40.8 ms: 1.05x slower                                                                                                          |
| richards_super             | 29.6 ms                                                                                                                    | 31.0 ms: 1.05x slower                                                                                                          |
| sympy_expand               | 283 ms                                                                                                                     | 296 ms: 1.05x slower                                                                                                           |
| richards                   | 26.1 ms                                                                                                                    | 27.5 ms: 1.05x slower                                                                                                          |
| scimark_sor                | 74.2 ms                                                                                                                    | 78.5 ms: 1.06x slower                                                                                                          |
| async_generators           | 227 ms                                                                                                                     | 246 ms: 1.08x slower                                                                                                           |
| spectral_norm              | 61.9 ms                                                                                                                    | 67.2 ms: 1.09x slower                                                                                                          |
| Geometric mean             | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (23): coroutines, async_tree_none_tg, connected_components, regex_compile, json, unpack_sequence, pidigits, nqueens, sqlite_synth, django_template, bench_mp_pool, pycparser, genshi_text, pickle, html5lib, typing_runtime_protocols, pylint, python_startup_no_site, pathlib, logging_format, asyncio_websockets, async_tree_io, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 96.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown