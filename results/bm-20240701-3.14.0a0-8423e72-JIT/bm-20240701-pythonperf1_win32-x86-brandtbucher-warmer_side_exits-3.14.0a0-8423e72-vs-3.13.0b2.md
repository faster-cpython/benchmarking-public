# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-x86
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.01x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 264 ms: 1.13x slower                                                              |
| docutils       | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                            |
| html5lib       | 45.4 ms                                                             | 51.6 ms: 1.14x slower                                                             |
| tornado_http   | 94.3 ms                                                             | 101 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 490 ms: 1.04x slower                                                              |
| async_tree_memoization_tg  | 254 ms                                                              | 267 ms: 1.05x slower                                                              |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                              |
| async_tree_none            | 228 ms                                                              | 240 ms: 1.05x slower                                                              |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 472 ms: 1.06x slower                                                              |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                              |
| async_tree_io              | 530 ms                                                              | 575 ms: 1.08x slower                                                              |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 51.5 ms: 1.49x faster                                                             |
| float          | 52.4 ms                                                             | 45.6 ms: 1.15x faster                                                             |
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                               | 1.20x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                              |
| regex_compile  | 99.9 ms                                                             | 101 ms: 1.01x slower                                                              |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                             |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 147 us                                                              | 130 us: 1.13x faster                                                              |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.5 ms: 1.01x faster                                                             |
| tomli_loads          | 1.65 sec                                                            | 1.63 sec: 1.01x faster                                                            |
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.01x slower                                                              |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                             |
| pickle_pure_python   | 213 us                                                              | 223 us: 1.05x slower                                                              |
| xml_etree_generate   | 59.6 ms                                                             | 63.0 ms: 1.06x slower                                                             |
| json_dumps           | 6.84 ms                                                             | 7.39 ms: 1.08x slower                                                             |
| xml_etree_process    | 42.1 ms                                                             | 48.5 ms: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.2 ms: 1.04x slower                                                             |
| python_startup_no_site | 18.2 ms                                                             | 19.2 ms: 1.06x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.05x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                             |
| django_template | 30.1 ms                                                             | 35.9 ms: 1.19x slower                                                             |
| genshi_text     | 20.1 ms                                                             | 25.8 ms: 1.28x slower                                                             |
| genshi_xml      | 44.3 ms                                                             | 57.1 ms: 1.29x slower                                                             |
| Geometric mean  | (ref)                                                               | 1.12x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 786 us: 12.38x faster                                                             |
| coverage                   | 307 ms                                                              | 52.4 ms: 5.86x faster                                                             |
| sqlglot_normalize          | 206 ms                                                              | 101 ms: 2.04x faster                                                              |
| nbody                      | 76.9 ms                                                             | 51.5 ms: 1.49x faster                                                             |
| deepcopy_memo              | 23.5 us                                                             | 16.5 us: 1.42x faster                                                             |
| spectral_norm              | 68.0 ms                                                             | 49.3 ms: 1.38x faster                                                             |
| mako                       | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                             |
| fannkuch                   | 270 ms                                                              | 216 ms: 1.25x faster                                                              |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.37 ms: 1.21x faster                                                             |
| scimark_fft                | 198 ms                                                              | 166 ms: 1.19x faster                                                              |
| crypto_pyaes               | 55.8 ms                                                             | 48.3 ms: 1.16x faster                                                             |
| float                      | 52.4 ms                                                             | 45.6 ms: 1.15x faster                                                             |
| unpickle_pure_python       | 147 us                                                              | 130 us: 1.13x faster                                                              |
| deepcopy                   | 280 us                                                              | 250 us: 1.12x faster                                                              |
| pyflate                    | 308 ms                                                              | 283 ms: 1.09x faster                                                              |
| telco                      | 6.03 ms                                                             | 5.61 ms: 1.07x faster                                                             |
| comprehensions             | 11.9 us                                                             | 11.1 us: 1.07x faster                                                             |
| asyncio_tcp                | 662 ms                                                              | 622 ms: 1.06x faster                                                              |
| scimark_monte_carlo        | 45.2 ms                                                             | 42.9 ms: 1.05x faster                                                             |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.5 ms: 1.01x faster                                                             |
| tomli_loads                | 1.65 sec                                                            | 1.63 sec: 1.01x faster                                                            |
| pprint_safe_repr           | 607 ms                                                              | 602 ms: 1.01x faster                                                              |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.24 sec                                                            | 1.23 sec: 1.00x faster                                                            |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                              |
| regex_compile              | 99.9 ms                                                             | 101 ms: 1.01x slower                                                              |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.01x slower                                                              |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                             |
| json                       | 4.10 ms                                                             | 4.16 ms: 1.01x slower                                                             |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                             |
| logging_silent             | 57.9 ns                                                             | 59.0 ns: 1.02x slower                                                             |
| meteor_contest             | 74.1 ms                                                             | 76.5 ms: 1.03x slower                                                             |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 490 ms: 1.04x slower                                                              |
| python_startup             | 22.2 ms                                                             | 23.2 ms: 1.04x slower                                                             |
| nqueens                    | 68.7 ms                                                             | 71.6 ms: 1.04x slower                                                             |
| pickle_pure_python         | 213 us                                                              | 223 us: 1.05x slower                                                              |
| async_tree_memoization_tg  | 254 ms                                                              | 267 ms: 1.05x slower                                                              |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                              |
| async_tree_none            | 228 ms                                                              | 240 ms: 1.05x slower                                                              |
| sqlglot_parse              | 964 us                                                              | 1.02 ms: 1.05x slower                                                             |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 472 ms: 1.06x slower                                                              |
| python_startup_no_site     | 18.2 ms                                                             | 19.2 ms: 1.06x slower                                                             |
| xml_etree_generate         | 59.6 ms                                                             | 63.0 ms: 1.06x slower                                                             |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                             |
| logging_format             | 8.13 us                                                             | 8.69 us: 1.07x slower                                                             |
| tornado_http               | 94.3 ms                                                             | 101 ms: 1.07x slower                                                              |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                              |
| logging_simple             | 7.47 us                                                             | 8.05 us: 1.08x slower                                                             |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                                            |
| bench_mp_pool              | 69.4 ms                                                             | 74.9 ms: 1.08x slower                                                             |
| json_dumps                 | 6.84 ms                                                             | 7.39 ms: 1.08x slower                                                             |
| sqlglot_transpile          | 1.19 ms                                                             | 1.29 ms: 1.08x slower                                                             |
| sympy_str                  | 211 ms                                                              | 229 ms: 1.08x slower                                                              |
| async_tree_io              | 530 ms                                                              | 575 ms: 1.08x slower                                                              |
| sympy_sum                  | 105 ms                                                              | 115 ms: 1.10x slower                                                              |
| sympy_expand               | 375 ms                                                              | 413 ms: 1.10x slower                                                              |
| docutils                   | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                            |
| hexiom                     | 4.23 ms                                                             | 4.68 ms: 1.11x slower                                                             |
| sympy_integrate            | 14.6 ms                                                             | 16.6 ms: 1.13x slower                                                             |
| 2to3                       | 233 ms                                                              | 264 ms: 1.13x slower                                                              |
| html5lib                   | 45.4 ms                                                             | 51.6 ms: 1.14x slower                                                             |
| xml_etree_process          | 42.1 ms                                                             | 48.5 ms: 1.15x slower                                                             |
| chaos                      | 48.0 ms                                                             | 55.7 ms: 1.16x slower                                                             |
| sqlglot_optimize           | 39.7 ms                                                             | 46.6 ms: 1.17x slower                                                             |
| pylint                     | 217 ms                                                              | 256 ms: 1.18x slower                                                              |
| pycparser                  | 777 ms                                                              | 917 ms: 1.18x slower                                                              |
| typing_runtime_protocols   | 136 us                                                              | 160 us: 1.18x slower                                                              |
| django_template            | 30.1 ms                                                             | 35.9 ms: 1.19x slower                                                             |
| richards                   | 31.2 ms                                                             | 37.5 ms: 1.20x slower                                                             |
| richards_super             | 35.5 ms                                                             | 42.9 ms: 1.21x slower                                                             |
| go                         | 101 ms                                                              | 122 ms: 1.21x slower                                                              |
| coroutines                 | 15.5 ms                                                             | 19.3 ms: 1.25x slower                                                             |
| deltablue                  | 2.23 ms                                                             | 2.82 ms: 1.26x slower                                                             |
| async_generators           | 266 ms                                                              | 338 ms: 1.27x slower                                                              |
| genshi_text                | 20.1 ms                                                             | 25.8 ms: 1.28x slower                                                             |
| genshi_xml                 | 44.3 ms                                                             | 57.1 ms: 1.29x slower                                                             |
| scimark_sor                | 81.0 ms                                                             | 110 ms: 1.36x slower                                                              |
| scimark_lu                 | 59.4 ms                                                             | 84.2 ms: 1.42x slower                                                             |
| raytrace                   | 189 ms                                                              | 268 ms: 1.42x slower                                                              |
| generators                 | 21.2 ms                                                             | 30.2 ms: 1.43x slower                                                             |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                      |

Benchmark hidden because not significant (7): pathlib, deepcopy_reduce, gc_traversal, bench_thread_pool, asyncio_tcp_ssl, create_gc_cycles, async_tree_io_tg
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown