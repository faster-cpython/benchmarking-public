# Results vs. base

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.010x faster
- HPT reliability: 97.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 219 ms                                                                                                               | 222 ms: 1.01x slower                                                                                                     |
| docutils       | 1.59 sec                                                                                                             | 1.66 sec: 1.05x slower                                                                                                   |
| html5lib       | 37.2 ms                                                                                                              | 38.3 ms: 1.03x slower                                                                                                    |
| sphinx         | 626 ms                                                                                                               | 637 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 14.5 ms                                                                                                              | 14.7 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 327 ms                                                                                                               | 334 ms: 1.02x slower                                                                                                     |
| async_tree_none            | 171 ms                                                                                                               | 175 ms: 1.02x slower                                                                                                     |
| async_tree_memoization_tg  | 207 ms                                                                                                               | 211 ms: 1.02x slower                                                                                                     |
| async_tree_io              | 382 ms                                                                                                               | 391 ms: 1.02x slower                                                                                                     |
| async_tree_none_tg         | 164 ms                                                                                                               | 167 ms: 1.02x slower                                                                                                     |
| async_tree_io_tg           | 379 ms                                                                                                               | 388 ms: 1.02x slower                                                                                                     |
| async_tree_memoization     | 200 ms                                                                                                               | 206 ms: 1.03x slower                                                                                                     |
| asyncio_tcp                | 509 ms                                                                                                               | 522 ms: 1.03x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                                                               | 343 ms: 1.03x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.39 sec                                                                                                             | 1.44 sec: 1.04x slower                                                                                                   |
| async_generators           | 228 ms                                                                                                               | 245 ms: 1.07x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.2 ms                                                                                                              | 57.5 ms: 1.14x faster                                                                                                    |
| pidigits       | 145 ms                                                                                                               | 146 ms: 1.01x slower                                                                                                     |
| float          | 43.1 ms                                                                                                              | 44.9 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 78.4 ms                                                                                                              | 78.1 ms: 1.01x faster                                                                                                    |
| regex_dna      | 115 ms                                                                                                               | 117 ms: 1.02x slower                                                                                                     |
| regex_effbot   | 1.48 ms                                                                                                              | 1.58 ms: 1.07x slower                                                                                                    |
| regex_v8       | 13.2 ms                                                                                                              | 14.1 ms: 1.07x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 132 us                                                                                                               | 106 us: 1.25x faster                                                                                                     |
| tomli_loads          | 1.36 sec                                                                                                             | 1.11 sec: 1.23x faster                                                                                                   |
| xml_etree_generate   | 57.5 ms                                                                                                              | 50.1 ms: 1.15x faster                                                                                                    |
| xml_etree_process    | 38.8 ms                                                                                                              | 35.6 ms: 1.09x faster                                                                                                    |
| unpickle_list        | 2.81 us                                                                                                              | 2.72 us: 1.03x faster                                                                                                    |
| xml_etree_iterparse  | 64.5 ms                                                                                                              | 62.6 ms: 1.03x faster                                                                                                    |
| pickle               | 7.82 us                                                                                                              | 7.64 us: 1.02x faster                                                                                                    |
| pickle_pure_python   | 208 us                                                                                                               | 205 us: 1.01x faster                                                                                                     |
| unpickle             | 8.60 us                                                                                                              | 8.48 us: 1.01x faster                                                                                                    |
| xml_etree_parse      | 86.8 ms                                                                                                              | 87.6 ms: 1.01x slower                                                                                                    |
| json_loads           | 14.0 us                                                                                                              | 14.2 us: 1.01x slower                                                                                                    |
| json_dumps           | 5.27 ms                                                                                                              | 5.44 ms: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (2): pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 26.1 ms                                                                                                              | 26.6 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.53 ms                                                                                                              | 5.26 ms: 1.24x faster                                                                                                    |
| genshi_text     | 15.6 ms                                                                                                              | 15.4 ms: 1.01x faster                                                                                                    |
| genshi_xml      | 34.4 ms                                                                                                              | 34.9 ms: 1.01x slower                                                                                                    |
| django_template | 23.9 ms                                                                                                              | 24.4 ms: 1.02x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.05x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 132 us                                                                                                               | 106 us: 1.25x faster                                                                                                     |
| mako                       | 6.53 ms                                                                                                              | 5.26 ms: 1.24x faster                                                                                                    |
| tomli_loads                | 1.36 sec                                                                                                             | 1.11 sec: 1.23x faster                                                                                                   |
| fannkuch                   | 262 ms                                                                                                               | 217 ms: 1.21x faster                                                                                                     |
| scimark_fft                | 182 ms                                                                                                               | 153 ms: 1.19x faster                                                                                                     |
| bpe_tokeniser              | 2.93 sec                                                                                                             | 2.53 sec: 1.16x faster                                                                                                   |
| xml_etree_generate         | 57.5 ms                                                                                                              | 50.1 ms: 1.15x faster                                                                                                    |
| nbody                      | 65.2 ms                                                                                                              | 57.5 ms: 1.14x faster                                                                                                    |
| pprint_safe_repr           | 487 ms                                                                                                               | 436 ms: 1.12x faster                                                                                                     |
| pprint_pformat             | 988 ms                                                                                                               | 889 ms: 1.11x faster                                                                                                     |
| pyflate                    | 289 ms                                                                                                               | 261 ms: 1.11x faster                                                                                                     |
| xml_etree_process          | 38.8 ms                                                                                                              | 35.6 ms: 1.09x faster                                                                                                    |
| raytrace                   | 193 ms                                                                                                               | 179 ms: 1.08x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.46 ms                                                                                                              | 2.28 ms: 1.08x faster                                                                                                    |
| unpack_sequence            | 37.1 ns                                                                                                              | 34.4 ns: 1.08x faster                                                                                                    |
| k_core                     | 1.69 sec                                                                                                             | 1.61 sec: 1.05x faster                                                                                                   |
| telco                      | 4.47 ms                                                                                                              | 4.29 ms: 1.04x faster                                                                                                    |
| logging_silent             | 56.0 ns                                                                                                              | 54.2 ns: 1.03x faster                                                                                                    |
| sqlglot_v2_parse           | 803 us                                                                                                               | 778 us: 1.03x faster                                                                                                     |
| unpickle_list              | 2.81 us                                                                                                              | 2.72 us: 1.03x faster                                                                                                    |
| xml_etree_iterparse        | 64.5 ms                                                                                                              | 62.6 ms: 1.03x faster                                                                                                    |
| spectral_norm              | 66.0 ms                                                                                                              | 64.1 ms: 1.03x faster                                                                                                    |
| pickle                     | 7.82 us                                                                                                              | 7.64 us: 1.02x faster                                                                                                    |
| crypto_pyaes               | 46.9 ms                                                                                                              | 46.0 ms: 1.02x faster                                                                                                    |
| pickle_pure_python         | 208 us                                                                                                               | 205 us: 1.01x faster                                                                                                     |
| connected_components       | 328 ms                                                                                                               | 324 ms: 1.01x faster                                                                                                     |
| unpickle                   | 8.60 us                                                                                                              | 8.48 us: 1.01x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.00 ms                                                                                                              | 988 us: 1.01x faster                                                                                                     |
| genshi_text                | 15.6 ms                                                                                                              | 15.4 ms: 1.01x faster                                                                                                    |
| comprehensions             | 10.8 us                                                                                                              | 10.7 us: 1.01x faster                                                                                                    |
| nqueens                    | 60.8 ms                                                                                                              | 60.2 ms: 1.01x faster                                                                                                    |
| generators                 | 19.8 ms                                                                                                              | 19.6 ms: 1.01x faster                                                                                                    |
| meteor_contest             | 71.5 ms                                                                                                              | 70.9 ms: 1.01x faster                                                                                                    |
| shortest_path              | 356 ms                                                                                                               | 353 ms: 1.01x faster                                                                                                     |
| regex_compile              | 78.4 ms                                                                                                              | 78.1 ms: 1.01x faster                                                                                                    |
| typing_runtime_protocols   | 102 us                                                                                                               | 103 us: 1.01x slower                                                                                                     |
| xml_etree_parse            | 86.8 ms                                                                                                              | 87.6 ms: 1.01x slower                                                                                                    |
| sqlite_synth               | 1.55 us                                                                                                              | 1.56 us: 1.01x slower                                                                                                    |
| logging_simple             | 5.99 us                                                                                                              | 6.05 us: 1.01x slower                                                                                                    |
| pidigits                   | 145 ms                                                                                                               | 146 ms: 1.01x slower                                                                                                     |
| json_loads                 | 14.0 us                                                                                                              | 14.2 us: 1.01x slower                                                                                                    |
| coroutines                 | 14.5 ms                                                                                                              | 14.7 ms: 1.01x slower                                                                                                    |
| 2to3                       | 219 ms                                                                                                               | 222 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_normalize       | 69.3 ms                                                                                                              | 70.3 ms: 1.01x slower                                                                                                    |
| create_gc_cycles           | 1.30 ms                                                                                                              | 1.32 ms: 1.01x slower                                                                                                    |
| scimark_sor                | 75.7 ms                                                                                                              | 76.8 ms: 1.01x slower                                                                                                    |
| bench_mp_pool              | 94.9 ms                                                                                                              | 96.3 ms: 1.01x slower                                                                                                    |
| genshi_xml                 | 34.4 ms                                                                                                              | 34.9 ms: 1.01x slower                                                                                                    |
| sqlglot_v2_optimize        | 33.6 ms                                                                                                              | 34.1 ms: 1.02x slower                                                                                                    |
| sympy_sum                  | 85.2 ms                                                                                                              | 86.7 ms: 1.02x slower                                                                                                    |
| mdp                        | 790 ms                                                                                                               | 804 ms: 1.02x slower                                                                                                     |
| sphinx                     | 626 ms                                                                                                               | 637 ms: 1.02x slower                                                                                                     |
| python_startup             | 26.1 ms                                                                                                              | 26.6 ms: 1.02x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 327 ms                                                                                                               | 334 ms: 1.02x slower                                                                                                     |
| regex_dna                  | 115 ms                                                                                                               | 117 ms: 1.02x slower                                                                                                     |
| async_tree_none            | 171 ms                                                                                                               | 175 ms: 1.02x slower                                                                                                     |
| async_tree_memoization_tg  | 207 ms                                                                                                               | 211 ms: 1.02x slower                                                                                                     |
| deepcopy                   | 167 us                                                                                                               | 171 us: 1.02x slower                                                                                                     |
| async_tree_io              | 382 ms                                                                                                               | 391 ms: 1.02x slower                                                                                                     |
| async_tree_none_tg         | 164 ms                                                                                                               | 167 ms: 1.02x slower                                                                                                     |
| django_template            | 23.9 ms                                                                                                              | 24.4 ms: 1.02x slower                                                                                                    |
| async_tree_io_tg           | 379 ms                                                                                                               | 388 ms: 1.02x slower                                                                                                     |
| async_tree_memoization     | 200 ms                                                                                                               | 206 ms: 1.03x slower                                                                                                     |
| asyncio_tcp                | 509 ms                                                                                                               | 522 ms: 1.03x slower                                                                                                     |
| deepcopy_reduce            | 1.77 us                                                                                                              | 1.82 us: 1.03x slower                                                                                                    |
| sympy_str                  | 165 ms                                                                                                               | 170 ms: 1.03x slower                                                                                                     |
| json                       | 2.96 ms                                                                                                              | 3.04 ms: 1.03x slower                                                                                                    |
| richards_super             | 30.1 ms                                                                                                              | 31.0 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                                                               | 343 ms: 1.03x slower                                                                                                     |
| deepcopy_memo              | 17.8 us                                                                                                              | 18.3 us: 1.03x slower                                                                                                    |
| html5lib                   | 37.2 ms                                                                                                              | 38.3 ms: 1.03x slower                                                                                                    |
| dulwich_log                | 39.1 ms                                                                                                              | 40.3 ms: 1.03x slower                                                                                                    |
| json_dumps                 | 5.27 ms                                                                                                              | 5.44 ms: 1.03x slower                                                                                                    |
| scimark_monte_carlo        | 38.9 ms                                                                                                              | 40.2 ms: 1.03x slower                                                                                                    |
| chaos                      | 39.7 ms                                                                                                              | 41.1 ms: 1.03x slower                                                                                                    |
| pylint                     | 193 ms                                                                                                               | 200 ms: 1.04x slower                                                                                                     |
| gc_traversal               | 2.11 ms                                                                                                              | 2.18 ms: 1.04x slower                                                                                                    |
| richards                   | 26.1 ms                                                                                                              | 27.1 ms: 1.04x slower                                                                                                    |
| deltablue                  | 2.20 ms                                                                                                              | 2.28 ms: 1.04x slower                                                                                                    |
| many_optionals             | 555 us                                                                                                               | 576 us: 1.04x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.39 sec                                                                                                             | 1.44 sec: 1.04x slower                                                                                                   |
| float                      | 43.1 ms                                                                                                              | 44.9 ms: 1.04x slower                                                                                                    |
| hexiom                     | 3.97 ms                                                                                                              | 4.13 ms: 1.04x slower                                                                                                    |
| sympy_integrate            | 12.2 ms                                                                                                              | 12.8 ms: 1.05x slower                                                                                                    |
| docutils                   | 1.59 sec                                                                                                             | 1.66 sec: 1.05x slower                                                                                                   |
| scimark_lu                 | 55.9 ms                                                                                                              | 59.3 ms: 1.06x slower                                                                                                    |
| sympy_expand               | 279 ms                                                                                                               | 296 ms: 1.06x slower                                                                                                     |
| regex_effbot               | 1.48 ms                                                                                                              | 1.58 ms: 1.07x slower                                                                                                    |
| regex_v8                   | 13.2 ms                                                                                                              | 14.1 ms: 1.07x slower                                                                                                    |
| async_generators           | 228 ms                                                                                                               | 245 ms: 1.07x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (12): pickle_list, pathlib, pickle_dict, thrift, go, asyncio_websockets, coverage, logging_format, bench_thread_pool, python_startup_no_site, pycparser, subparsers

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 97.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown