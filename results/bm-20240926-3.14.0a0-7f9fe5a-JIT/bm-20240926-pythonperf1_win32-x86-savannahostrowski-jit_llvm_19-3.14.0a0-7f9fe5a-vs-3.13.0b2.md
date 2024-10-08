# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-x86
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.03x faster
- HPT reliability: 98.98%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 260 ms: 1.12x slower                                                             |
| docutils       | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                           |
| html5lib       | 45.4 ms                                                             | 47.0 ms: 1.04x slower                                                            |
| tornado_http   | 94.3 ms                                                             | 110 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                             |
| async_tree_memoization     | 275 ms                                                              | 280 ms: 1.02x slower                                                             |
| async_tree_memoization_tg  | 254 ms                                                              | 260 ms: 1.02x slower                                                             |
| async_tree_io              | 530 ms                                                              | 548 ms: 1.03x slower                                                             |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 467 ms: 1.04x slower                                                             |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                     |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 48.6 ms: 1.58x faster                                                            |
| float          | 52.4 ms                                                             | 43.3 ms: 1.21x faster                                                            |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                               | 1.25x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                             |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                            |
| regex_compile  | 99.9 ms                                                             | 103 ms: 1.04x slower                                                             |
| regex_effbot   | 1.88 ms                                                             | 1.96 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_generate   | 59.6 ms                                                             | 54.0 ms: 1.10x faster                                                            |
| unpickle_list        | 2.93 us                                                             | 2.75 us: 1.07x faster                                                            |
| tomli_loads          | 1.65 sec                                                            | 1.56 sec: 1.06x faster                                                           |
| pickle_list          | 3.57 us                                                             | 3.38 us: 1.06x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.8 ms: 1.04x faster                                                            |
| pickle_dict          | 20.8 us                                                             | 20.0 us: 1.04x faster                                                            |
| xml_etree_process    | 42.1 ms                                                             | 40.6 ms: 1.04x faster                                                            |
| xml_etree_parse      | 104 ms                                                              | 104 ms: 1.01x faster                                                             |
| pickle               | 8.07 us                                                             | 8.02 us: 1.01x faster                                                            |
| json_loads           | 20.5 us                                                             | 21.2 us: 1.03x slower                                                            |
| unpickle             | 9.79 us                                                             | 10.5 us: 1.07x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 168 us: 1.14x slower                                                             |
| pickle_pure_python   | 213 us                                                              | 255 us: 1.20x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.5 ms: 1.10x slower                                                            |
| python_startup_no_site | 18.2 ms                                                             | 20.2 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.48 ms: 1.27x faster                                                            |
| django_template | 30.1 ms                                                             | 34.7 ms: 1.15x slower                                                            |
| genshi_text     | 20.1 ms                                                             | 24.5 ms: 1.22x slower                                                            |
| genshi_xml      | 44.3 ms                                                             | 56.6 ms: 1.28x slower                                                            |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 788 us: 12.34x faster                                                            |
| coverage                   | 307 ms                                                              | 54.9 ms: 5.59x faster                                                            |
| nbody                      | 76.9 ms                                                             | 48.6 ms: 1.58x faster                                                            |
| deepcopy_memo              | 23.5 us                                                             | 15.5 us: 1.51x faster                                                            |
| spectral_norm              | 68.0 ms                                                             | 47.0 ms: 1.45x faster                                                            |
| mako                       | 6.94 ms                                                             | 5.48 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.36 ms: 1.22x faster                                                            |
| float                      | 52.4 ms                                                             | 43.3 ms: 1.21x faster                                                            |
| scimark_sor                | 81.0 ms                                                             | 68.2 ms: 1.19x faster                                                            |
| crypto_pyaes               | 55.8 ms                                                             | 47.6 ms: 1.17x faster                                                            |
| deepcopy                   | 280 us                                                              | 239 us: 1.17x faster                                                             |
| fannkuch                   | 270 ms                                                              | 235 ms: 1.15x faster                                                             |
| scimark_fft                | 198 ms                                                              | 173 ms: 1.14x faster                                                             |
| xml_etree_generate         | 59.6 ms                                                             | 54.0 ms: 1.10x faster                                                            |
| unpickle_list              | 2.93 us                                                             | 2.75 us: 1.07x faster                                                            |
| tomli_loads                | 1.65 sec                                                            | 1.56 sec: 1.06x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.38 us: 1.06x faster                                                            |
| deltablue                  | 2.23 ms                                                             | 2.12 ms: 1.05x faster                                                            |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.8 ms: 1.04x faster                                                            |
| pyflate                    | 308 ms                                                              | 297 ms: 1.04x faster                                                             |
| pickle_dict                | 20.8 us                                                             | 20.0 us: 1.04x faster                                                            |
| xml_etree_process          | 42.1 ms                                                             | 40.6 ms: 1.04x faster                                                            |
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                             |
| sqlite_synth               | 1.96 us                                                             | 1.91 us: 1.03x faster                                                            |
| meteor_contest             | 74.1 ms                                                             | 72.2 ms: 1.03x faster                                                            |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                             |
| pprint_safe_repr           | 607 ms                                                              | 599 ms: 1.01x faster                                                             |
| deepcopy_reduce            | 2.59 us                                                             | 2.56 us: 1.01x faster                                                            |
| xml_etree_parse            | 104 ms                                                              | 104 ms: 1.01x faster                                                             |
| pickle                     | 8.07 us                                                             | 8.02 us: 1.01x faster                                                            |
| scimark_lu                 | 59.4 ms                                                             | 59.8 ms: 1.01x slower                                                            |
| gc_traversal               | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                            |
| telco                      | 6.03 ms                                                             | 6.08 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                           |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                             |
| richards_super             | 35.5 ms                                                             | 35.9 ms: 1.01x slower                                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.26 sec: 1.01x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 280 ms: 1.02x slower                                                             |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 260 ms: 1.02x slower                                                             |
| json_loads                 | 20.5 us                                                             | 21.2 us: 1.03x slower                                                            |
| async_tree_io              | 530 ms                                                              | 548 ms: 1.03x slower                                                             |
| html5lib                   | 45.4 ms                                                             | 47.0 ms: 1.04x slower                                                            |
| regex_compile              | 99.9 ms                                                             | 103 ms: 1.04x slower                                                             |
| go                         | 101 ms                                                              | 104 ms: 1.04x slower                                                             |
| regex_effbot               | 1.88 ms                                                             | 1.96 ms: 1.04x slower                                                            |
| pathlib                    | 83.9 ms                                                             | 87.5 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 467 ms: 1.04x slower                                                             |
| sympy_str                  | 211 ms                                                              | 222 ms: 1.05x slower                                                             |
| pycparser                  | 777 ms                                                              | 818 ms: 1.05x slower                                                             |
| richards                   | 31.2 ms                                                             | 33.0 ms: 1.06x slower                                                            |
| logging_format             | 8.13 us                                                             | 8.65 us: 1.06x slower                                                            |
| sympy_expand               | 375 ms                                                              | 400 ms: 1.07x slower                                                             |
| scimark_monte_carlo        | 45.2 ms                                                             | 48.2 ms: 1.07x slower                                                            |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                           |
| generators                 | 21.2 ms                                                             | 22.7 ms: 1.07x slower                                                            |
| unpickle                   | 9.79 us                                                             | 10.5 us: 1.07x slower                                                            |
| logging_silent             | 57.9 ns                                                             | 62.2 ns: 1.08x slower                                                            |
| logging_simple             | 7.47 us                                                             | 8.05 us: 1.08x slower                                                            |
| sympy_sum                  | 105 ms                                                              | 114 ms: 1.08x slower                                                             |
| nqueens                    | 68.7 ms                                                             | 74.5 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.09x slower                                                             |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                                            |
| python_startup             | 22.2 ms                                                             | 24.5 ms: 1.10x slower                                                            |
| docutils                   | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.2 ms: 1.11x slower                                                            |
| sqlglot_normalize          | 206 ms                                                              | 230 ms: 1.12x slower                                                             |
| 2to3                       | 233 ms                                                              | 260 ms: 1.12x slower                                                             |
| bench_mp_pool              | 69.4 ms                                                             | 77.5 ms: 1.12x slower                                                            |
| chaos                      | 48.0 ms                                                             | 53.9 ms: 1.12x slower                                                            |
| unpickle_pure_python       | 147 us                                                              | 168 us: 1.14x slower                                                             |
| sqlglot_transpile          | 1.19 ms                                                             | 1.36 ms: 1.14x slower                                                            |
| sympy_integrate            | 14.6 ms                                                             | 16.8 ms: 1.14x slower                                                            |
| django_template            | 30.1 ms                                                             | 34.7 ms: 1.15x slower                                                            |
| tornado_http               | 94.3 ms                                                             | 110 ms: 1.17x slower                                                             |
| hexiom                     | 4.23 ms                                                             | 4.96 ms: 1.17x slower                                                            |
| coroutines                 | 15.5 ms                                                             | 18.2 ms: 1.18x slower                                                            |
| sqlglot_optimize           | 39.7 ms                                                             | 46.9 ms: 1.18x slower                                                            |
| pickle_pure_python         | 213 us                                                              | 255 us: 1.20x slower                                                             |
| async_generators           | 266 ms                                                              | 322 ms: 1.21x slower                                                             |
| genshi_text                | 20.1 ms                                                             | 24.5 ms: 1.22x slower                                                            |
| pylint                     | 217 ms                                                              | 271 ms: 1.25x slower                                                             |
| genshi_xml                 | 44.3 ms                                                             | 56.6 ms: 1.28x slower                                                            |
| raytrace                   | 189 ms                                                              | 249 ms: 1.32x slower                                                             |
| Geometric mean             | (ref)                                                               | 1.03x faster                                                                     |

Benchmark hidden because not significant (9): create_gc_cycles, comprehensions, async_tree_io_tg, json_dumps, json, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 98.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown