# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-x86
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.04x faster
- HPT reliability: 93.21%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.11x slower                                                              |
| docutils       | 1.81 sec                                                            | 1.95 sec: 1.08x slower                                                            |
| html5lib       | 45.4 ms                                                             | 46.4 ms: 1.02x slower                                                             |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                              |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 203 ms                                                              | 194 ms: 1.05x faster                                                              |
| async_tree_io_tg           | 529 ms                                                              | 509 ms: 1.04x faster                                                              |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                              |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                              |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                              |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 53.1 ms: 1.45x faster                                                             |
| float          | 52.4 ms                                                             | 42.9 ms: 1.22x faster                                                             |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                               | 1.21x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 95.3 ms: 1.05x faster                                                             |
| regex_dna      | 118 ms                                                              | 116 ms: 1.01x faster                                                              |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                             |
| regex_effbot   | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.46 sec: 1.13x faster                                                            |
| unpickle_pure_python | 147 us                                                              | 149 us: 1.01x slower                                                              |
| pickle_pure_python   | 213 us                                                              | 217 us: 1.02x slower                                                              |
| json_dumps           | 6.84 ms                                                             | 7.00 ms: 1.02x slower                                                             |
| json_loads           | 20.5 us                                                             | 21.2 us: 1.03x slower                                                             |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.04x slower                                                              |
| xml_etree_process    | 42.1 ms                                                             | 44.7 ms: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.9 ms: 1.08x slower                                                             |
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.11x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.41 ms: 1.28x faster                                                             |
| django_template | 30.1 ms                                                             | 32.2 ms: 1.07x slower                                                             |
| genshi_text     | 20.1 ms                                                             | 22.8 ms: 1.13x slower                                                             |
| genshi_xml      | 44.3 ms                                                             | 51.4 ms: 1.16x slower                                                             |
| Geometric mean  | (ref)                                                               | 1.02x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 725 us: 13.42x faster                                                             |
| coverage                   | 307 ms                                                              | 52.8 ms: 5.82x faster                                                             |
| deepcopy_memo              | 23.5 us                                                             | 15.7 us: 1.49x faster                                                             |
| nbody                      | 76.9 ms                                                             | 53.1 ms: 1.45x faster                                                             |
| spectral_norm              | 68.0 ms                                                             | 47.3 ms: 1.44x faster                                                             |
| mako                       | 6.94 ms                                                             | 5.41 ms: 1.28x faster                                                             |
| float                      | 52.4 ms                                                             | 42.9 ms: 1.22x faster                                                             |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.37 ms: 1.21x faster                                                             |
| scimark_fft                | 198 ms                                                              | 167 ms: 1.18x faster                                                              |
| deepcopy                   | 280 us                                                              | 237 us: 1.18x faster                                                              |
| pyflate                    | 308 ms                                                              | 264 ms: 1.17x faster                                                              |
| crypto_pyaes               | 55.8 ms                                                             | 48.7 ms: 1.15x faster                                                             |
| fannkuch                   | 270 ms                                                              | 238 ms: 1.13x faster                                                              |
| tomli_loads                | 1.65 sec                                                            | 1.46 sec: 1.13x faster                                                            |
| deepcopy_reduce            | 2.59 us                                                             | 2.42 us: 1.07x faster                                                             |
| regex_compile              | 99.9 ms                                                             | 95.3 ms: 1.05x faster                                                             |
| async_tree_none_tg         | 203 ms                                                              | 194 ms: 1.05x faster                                                              |
| meteor_contest             | 74.1 ms                                                             | 70.8 ms: 1.05x faster                                                             |
| telco                      | 6.03 ms                                                             | 5.77 ms: 1.05x faster                                                             |
| pprint_safe_repr           | 607 ms                                                              | 582 ms: 1.04x faster                                                              |
| comprehensions             | 11.9 us                                                             | 11.4 us: 1.04x faster                                                             |
| async_tree_io_tg           | 529 ms                                                              | 509 ms: 1.04x faster                                                              |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                              |
| pprint_pformat             | 1.24 sec                                                            | 1.20 sec: 1.03x faster                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                              |
| sqlglot_parse              | 964 us                                                              | 936 us: 1.03x faster                                                              |
| scimark_monte_carlo        | 45.2 ms                                                             | 44.0 ms: 1.03x faster                                                             |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.01x faster                                                              |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                              |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                             |
| unpickle_pure_python       | 147 us                                                              | 149 us: 1.01x slower                                                              |
| sympy_expand               | 375 ms                                                              | 380 ms: 1.01x slower                                                              |
| sqlglot_transpile          | 1.19 ms                                                             | 1.21 ms: 1.01x slower                                                             |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                             |
| pickle_pure_python         | 213 us                                                              | 217 us: 1.02x slower                                                              |
| create_gc_cycles           | 756 us                                                              | 769 us: 1.02x slower                                                              |
| logging_silent             | 57.9 ns                                                             | 59.0 ns: 1.02x slower                                                             |
| sympy_str                  | 211 ms                                                              | 215 ms: 1.02x slower                                                              |
| html5lib                   | 45.4 ms                                                             | 46.4 ms: 1.02x slower                                                             |
| json_dumps                 | 6.84 ms                                                             | 7.00 ms: 1.02x slower                                                             |
| pycparser                  | 777 ms                                                              | 796 ms: 1.02x slower                                                              |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                              |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                              |
| mdp                        | 1.60 sec                                                            | 1.66 sec: 1.03x slower                                                            |
| json_loads                 | 20.5 us                                                             | 21.2 us: 1.03x slower                                                             |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                              |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.04x slower                                                              |
| bench_thread_pool          | 985 us                                                              | 1.03 ms: 1.05x slower                                                             |
| json                       | 4.10 ms                                                             | 4.31 ms: 1.05x slower                                                             |
| pathlib                    | 83.9 ms                                                             | 88.8 ms: 1.06x slower                                                             |
| regex_effbot               | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                             |
| xml_etree_process          | 42.1 ms                                                             | 44.7 ms: 1.06x slower                                                             |
| django_template            | 30.1 ms                                                             | 32.2 ms: 1.07x slower                                                             |
| chaos                      | 48.0 ms                                                             | 51.6 ms: 1.08x slower                                                             |
| docutils                   | 1.81 sec                                                            | 1.95 sec: 1.08x slower                                                            |
| python_startup             | 22.2 ms                                                             | 23.9 ms: 1.08x slower                                                             |
| typing_runtime_protocols   | 136 us                                                              | 146 us: 1.08x slower                                                              |
| nqueens                    | 68.7 ms                                                             | 74.3 ms: 1.08x slower                                                             |
| richards                   | 31.2 ms                                                             | 33.8 ms: 1.08x slower                                                             |
| hexiom                     | 4.23 ms                                                             | 4.62 ms: 1.09x slower                                                             |
| sqlglot_optimize           | 39.7 ms                                                             | 43.6 ms: 1.10x slower                                                             |
| sympy_integrate            | 14.6 ms                                                             | 16.1 ms: 1.10x slower                                                             |
| python_startup_no_site     | 18.2 ms                                                             | 20.1 ms: 1.11x slower                                                             |
| 2to3                       | 233 ms                                                              | 258 ms: 1.11x slower                                                              |
| richards_super             | 35.5 ms                                                             | 39.5 ms: 1.11x slower                                                             |
| bench_mp_pool              | 69.4 ms                                                             | 77.4 ms: 1.12x slower                                                             |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                              |
| genshi_text                | 20.1 ms                                                             | 22.8 ms: 1.13x slower                                                             |
| pylint                     | 217 ms                                                              | 248 ms: 1.14x slower                                                              |
| sqlglot_normalize          | 206 ms                                                              | 236 ms: 1.14x slower                                                              |
| go                         | 101 ms                                                              | 115 ms: 1.15x slower                                                              |
| genshi_xml                 | 44.3 ms                                                             | 51.4 ms: 1.16x slower                                                             |
| coroutines                 | 15.5 ms                                                             | 18.0 ms: 1.17x slower                                                             |
| async_generators           | 266 ms                                                              | 310 ms: 1.17x slower                                                              |
| raytrace                   | 189 ms                                                              | 226 ms: 1.20x slower                                                              |
| deltablue                  | 2.23 ms                                                             | 2.71 ms: 1.21x slower                                                             |
| scimark_sor                | 81.0 ms                                                             | 107 ms: 1.32x slower                                                              |
| scimark_lu                 | 59.4 ms                                                             | 78.9 ms: 1.33x slower                                                             |
| generators                 | 21.2 ms                                                             | 28.2 ms: 1.33x slower                                                             |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                      |

Benchmark hidden because not significant (8): async_tree_memoization, xml_etree_iterparse, logging_simple, logging_format, xml_etree_generate, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: dulwich_log

# HPT report

- Reliability score: 93.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown