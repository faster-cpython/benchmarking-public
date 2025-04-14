# Results vs. base

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.041x faster
- HPT reliability: 83.45%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                                                                        | 264 ms: 1.07x slower                                                                                              |
| docutils       | 1.85 sec                                                                                                      | 2.07 sec: 1.12x slower                                                                                            |
| html5lib       | 44.9 ms                                                                                                       | 47.2 ms: 1.05x slower                                                                                             |
| sphinx         | 758 ms                                                                                                        | 852 ms: 1.12x slower                                                                                              |
| tornado_http   | 104 ms                                                                                                        | 109 ms: 1.05x slower                                                                                              |
| Geometric mean | (ref)                                                                                                         | 1.08x slower                                                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp      | 819 ms                                                                                                        | 789 ms: 1.04x faster                                                                                              |
| async_tree_io    | 534 ms                                                                                                        | 523 ms: 1.02x faster                                                                                              |
| async_tree_none  | 223 ms                                                                                                        | 219 ms: 1.02x faster                                                                                              |
| async_tree_io_tg | 558 ms                                                                                                        | 551 ms: 1.01x faster                                                                                              |
| coroutines       | 17.1 ms                                                                                                       | 17.8 ms: 1.04x slower                                                                                             |
| async_generators | 306 ms                                                                                                        | 325 ms: 1.06x slower                                                                                              |
| Geometric mean   | (ref)                                                                                                         | 1.00x slower                                                                                                      |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| nbody          | 87.2 ms                                                                                                       | 63.2 ms: 1.38x faster                                                                                             |
| float          | 61.9 ms                                                                                                       | 47.0 ms: 1.32x faster                                                                                             |
| pidigits       | 199 ms                                                                                                        | 200 ms: 1.01x slower                                                                                              |
| Geometric mean | (ref)                                                                                                         | 1.22x faster                                                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                                                                       | 15.4 ms: 1.03x faster                                                                                             |
| regex_compile  | 105 ms                                                                                                        | 104 ms: 1.01x faster                                                                                              |
| Geometric mean | (ref)                                                                                                         | 1.01x faster                                                                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.87 sec                                                                                                      | 1.56 sec: 1.20x faster                                                                                            |
| xml_etree_generate   | 66.5 ms                                                                                                       | 55.7 ms: 1.19x faster                                                                                             |
| json_dumps           | 9.09 ms                                                                                                       | 8.11 ms: 1.12x faster                                                                                             |
| xml_etree_process    | 47.6 ms                                                                                                       | 42.8 ms: 1.11x faster                                                                                             |
| unpickle_pure_python | 178 us                                                                                                        | 161 us: 1.10x faster                                                                                              |
| unpickle_list        | 2.98 us                                                                                                       | 2.71 us: 1.10x faster                                                                                             |
| pickle_pure_python   | 265 us                                                                                                        | 246 us: 1.08x faster                                                                                              |
| xml_etree_iterparse  | 69.5 ms                                                                                                       | 64.3 ms: 1.08x faster                                                                                             |
| xml_etree_parse      | 113 ms                                                                                                        | 109 ms: 1.04x faster                                                                                              |
| pickle               | 8.56 us                                                                                                       | 8.60 us: 1.01x slower                                                                                             |
| unpickle             | 10.2 us                                                                                                       | 10.4 us: 1.01x slower                                                                                             |
| json_loads           | 20.5 us                                                                                                       | 20.8 us: 1.02x slower                                                                                             |
| Geometric mean       | (ref)                                                                                                         | 1.07x faster                                                                                                      |

Benchmark hidden because not significant (2): pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 20.1 ms                                                                                                       | 20.3 ms: 1.01x slower                                                                                             |
| python_startup         | 26.6 ms                                                                                                       | 27.1 ms: 1.02x slower                                                                                             |
| Geometric mean         | (ref)                                                                                                         | 1.01x slower                                                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| mako            | 7.83 ms                                                                                                       | 5.70 ms: 1.37x faster                                                                                             |
| django_template | 32.5 ms                                                                                                       | 33.6 ms: 1.03x slower                                                                                             |
| genshi_text     | 20.6 ms                                                                                                       | 24.2 ms: 1.17x slower                                                                                             |
| genshi_xml      | 45.9 ms                                                                                                       | 54.0 ms: 1.18x slower                                                                                             |
| Geometric mean  | (ref)                                                                                                         | 1.01x slower                                                                                                      |

All benchmarks:
===============

| Benchmark                | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| scimark_sor              | 103 ms                                                                                                        | 70.1 ms: 1.47x faster                                                                                             |
| scimark_monte_carlo      | 58.2 ms                                                                                                       | 41.6 ms: 1.40x faster                                                                                             |
| nbody                    | 87.2 ms                                                                                                       | 63.2 ms: 1.38x faster                                                                                             |
| deepcopy_memo            | 22.3 us                                                                                                       | 16.2 us: 1.38x faster                                                                                             |
| mako                     | 7.83 ms                                                                                                       | 5.70 ms: 1.37x faster                                                                                             |
| spectral_norm            | 77.3 ms                                                                                                       | 57.2 ms: 1.35x faster                                                                                             |
| float                    | 61.9 ms                                                                                                       | 47.0 ms: 1.32x faster                                                                                             |
| fannkuch                 | 325 ms                                                                                                        | 249 ms: 1.30x faster                                                                                              |
| scimark_sparse_mat_mult  | 3.17 ms                                                                                                       | 2.54 ms: 1.25x faster                                                                                             |
| logging_silent           | 69.5 ns                                                                                                       | 56.0 ns: 1.24x faster                                                                                             |
| scimark_fft              | 230 ms                                                                                                        | 187 ms: 1.23x faster                                                                                              |
| pprint_pformat           | 1.37 sec                                                                                                      | 1.12 sec: 1.23x faster                                                                                            |
| pprint_safe_repr         | 662 ms                                                                                                        | 546 ms: 1.21x faster                                                                                              |
| tomli_loads              | 1.87 sec                                                                                                      | 1.56 sec: 1.20x faster                                                                                            |
| unpack_sequence          | 49.8 ns                                                                                                       | 41.7 ns: 1.20x faster                                                                                             |
| xml_etree_generate       | 66.5 ms                                                                                                       | 55.7 ms: 1.19x faster                                                                                             |
| json                     | 5.97 ms                                                                                                       | 5.03 ms: 1.19x faster                                                                                             |
| pyflate                  | 368 ms                                                                                                        | 312 ms: 1.18x faster                                                                                              |
| crypto_pyaes             | 60.0 ms                                                                                                       | 51.9 ms: 1.16x faster                                                                                             |
| json_dumps               | 9.09 ms                                                                                                       | 8.11 ms: 1.12x faster                                                                                             |
| scimark_lu               | 67.6 ms                                                                                                       | 60.6 ms: 1.12x faster                                                                                             |
| xml_etree_process        | 47.6 ms                                                                                                       | 42.8 ms: 1.11x faster                                                                                             |
| unpickle_pure_python     | 178 us                                                                                                        | 161 us: 1.10x faster                                                                                              |
| unpickle_list            | 2.98 us                                                                                                       | 2.71 us: 1.10x faster                                                                                             |
| meteor_contest           | 80.3 ms                                                                                                       | 73.3 ms: 1.10x faster                                                                                             |
| pickle_pure_python       | 265 us                                                                                                        | 246 us: 1.08x faster                                                                                              |
| xml_etree_iterparse      | 69.5 ms                                                                                                       | 64.3 ms: 1.08x faster                                                                                             |
| dulwich_log              | 52.5 ms                                                                                                       | 49.3 ms: 1.06x faster                                                                                             |
| logging_simple           | 7.95 us                                                                                                       | 7.54 us: 1.05x faster                                                                                             |
| logging_format           | 8.70 us                                                                                                       | 8.27 us: 1.05x faster                                                                                             |
| deepcopy_reduce          | 2.55 us                                                                                                       | 2.44 us: 1.04x faster                                                                                             |
| sqlite_synth             | 1.99 us                                                                                                       | 1.91 us: 1.04x faster                                                                                             |
| asyncio_tcp              | 819 ms                                                                                                        | 789 ms: 1.04x faster                                                                                              |
| xml_etree_parse          | 113 ms                                                                                                        | 109 ms: 1.04x faster                                                                                              |
| richards_super           | 47.3 ms                                                                                                       | 45.6 ms: 1.04x faster                                                                                             |
| telco                    | 6.58 ms                                                                                                       | 6.36 ms: 1.03x faster                                                                                             |
| richards                 | 41.5 ms                                                                                                       | 40.2 ms: 1.03x faster                                                                                             |
| comprehensions           | 13.4 us                                                                                                       | 13.0 us: 1.03x faster                                                                                             |
| regex_v8                 | 15.8 ms                                                                                                       | 15.4 ms: 1.03x faster                                                                                             |
| go                       | 99.5 ms                                                                                                       | 97.2 ms: 1.02x faster                                                                                             |
| async_tree_io            | 534 ms                                                                                                        | 523 ms: 1.02x faster                                                                                              |
| deepcopy                 | 242 us                                                                                                        | 238 us: 1.02x faster                                                                                              |
| async_tree_none          | 223 ms                                                                                                        | 219 ms: 1.02x faster                                                                                              |
| deltablue                | 2.68 ms                                                                                                       | 2.64 ms: 1.01x faster                                                                                             |
| sqlglot_parse            | 1.06 ms                                                                                                       | 1.05 ms: 1.01x faster                                                                                             |
| async_tree_io_tg         | 558 ms                                                                                                        | 551 ms: 1.01x faster                                                                                              |
| regex_compile            | 105 ms                                                                                                        | 104 ms: 1.01x faster                                                                                              |
| pickle                   | 8.56 us                                                                                                       | 8.60 us: 1.01x slower                                                                                             |
| mdp                      | 1.72 sec                                                                                                      | 1.73 sec: 1.01x slower                                                                                            |
| chaos                    | 55.4 ms                                                                                                       | 55.8 ms: 1.01x slower                                                                                             |
| pidigits                 | 199 ms                                                                                                        | 200 ms: 1.01x slower                                                                                              |
| python_startup_no_site   | 20.1 ms                                                                                                       | 20.3 ms: 1.01x slower                                                                                             |
| pycparser                | 825 ms                                                                                                        | 834 ms: 1.01x slower                                                                                              |
| thrift                   | 762 us                                                                                                        | 770 us: 1.01x slower                                                                                              |
| unpickle                 | 10.2 us                                                                                                       | 10.4 us: 1.01x slower                                                                                             |
| python_startup           | 26.6 ms                                                                                                       | 27.1 ms: 1.02x slower                                                                                             |
| sympy_expand             | 387 ms                                                                                                        | 394 ms: 1.02x slower                                                                                              |
| json_loads               | 20.5 us                                                                                                       | 20.8 us: 1.02x slower                                                                                             |
| nqueens                  | 74.5 ms                                                                                                       | 76.2 ms: 1.02x slower                                                                                             |
| typing_runtime_protocols | 143 us                                                                                                        | 148 us: 1.03x slower                                                                                              |
| django_template          | 32.5 ms                                                                                                       | 33.6 ms: 1.03x slower                                                                                             |
| coverage                 | 51.9 ms                                                                                                       | 53.8 ms: 1.04x slower                                                                                             |
| sqlglot_transpile        | 1.32 ms                                                                                                       | 1.37 ms: 1.04x slower                                                                                             |
| generators               | 24.1 ms                                                                                                       | 25.1 ms: 1.04x slower                                                                                             |
| coroutines               | 17.1 ms                                                                                                       | 17.8 ms: 1.04x slower                                                                                             |
| sympy_str                | 218 ms                                                                                                        | 227 ms: 1.04x slower                                                                                              |
| tornado_http             | 104 ms                                                                                                        | 109 ms: 1.05x slower                                                                                              |
| html5lib                 | 44.9 ms                                                                                                       | 47.2 ms: 1.05x slower                                                                                             |
| bench_mp_pool            | 89.0 ms                                                                                                       | 94.5 ms: 1.06x slower                                                                                             |
| hexiom                   | 5.05 ms                                                                                                       | 5.38 ms: 1.06x slower                                                                                             |
| async_generators         | 306 ms                                                                                                        | 325 ms: 1.06x slower                                                                                              |
| 2to3                     | 246 ms                                                                                                        | 264 ms: 1.07x slower                                                                                              |
| sqlglot_normalize        | 224 ms                                                                                                        | 244 ms: 1.09x slower                                                                                              |
| sympy_sum                | 107 ms                                                                                                        | 117 ms: 1.09x slower                                                                                              |
| docutils                 | 1.85 sec                                                                                                      | 2.07 sec: 1.12x slower                                                                                            |
| sphinx                   | 758 ms                                                                                                        | 852 ms: 1.12x slower                                                                                              |
| sympy_integrate          | 15.5 ms                                                                                                       | 17.5 ms: 1.13x slower                                                                                             |
| raytrace                 | 236 ms                                                                                                        | 269 ms: 1.14x slower                                                                                              |
| sqlglot_optimize         | 43.6 ms                                                                                                       | 50.3 ms: 1.15x slower                                                                                             |
| genshi_text              | 20.6 ms                                                                                                       | 24.2 ms: 1.17x slower                                                                                             |
| genshi_xml               | 45.9 ms                                                                                                       | 54.0 ms: 1.18x slower                                                                                             |
| pylint                   | 232 ms                                                                                                        | 283 ms: 1.22x slower                                                                                              |
| Geometric mean           | (ref)                                                                                                         | 1.04x faster                                                                                                      |

Benchmark hidden because not significant (14): async_tree_memoization_tg, async_tree_none_tg, pickle_list, async_tree_memoization, pickle_dict, regex_effbot, regex_dna, asyncio_tcp_ssl, pathlib, create_gc_cycles, async_tree_cpu_io_mixed_tg, gc_traversal, async_tree_cpu_io_mixed, bench_thread_pool

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 83.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown