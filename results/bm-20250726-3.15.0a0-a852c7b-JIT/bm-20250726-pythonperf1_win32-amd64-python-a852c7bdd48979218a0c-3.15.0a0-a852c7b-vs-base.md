# Results vs. base

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.64 sec                                                                                                                   | 1.67 sec: 1.02x slower                                                                                                         |
| sphinx         | 653 ms                                                                                                                     | 644 ms: 1.01x faster                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.00x slower                                                                                                                   |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg        | 178 ms                                                                                                                     | 167 ms: 1.06x faster                                                                                                           |
| asyncio_websockets        | 172 ms                                                                                                                     | 163 ms: 1.06x faster                                                                                                           |
| async_tree_memoization    | 213 ms                                                                                                                     | 203 ms: 1.05x faster                                                                                                           |
| async_tree_memoization_tg | 221 ms                                                                                                                     | 212 ms: 1.04x faster                                                                                                           |
| async_tree_io             | 394 ms                                                                                                                     | 401 ms: 1.02x slower                                                                                                           |
| async_generators          | 241 ms                                                                                                                     | 255 ms: 1.06x slower                                                                                                           |
| asyncio_tcp_ssl           | 1.31 sec                                                                                                                   | 1.42 sec: 1.09x slower                                                                                                         |
| asyncio_tcp               | 396 ms                                                                                                                     | 519 ms: 1.31x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (5): async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 67.9 ms                                                                                                                    | 57.7 ms: 1.18x faster                                                                                                          |
| float          | 44.9 ms                                                                                                                    | 43.1 ms: 1.04x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                                                                                     | 121 ms: 1.04x faster                                                                                                           |
| regex_compile  | 81.5 ms                                                                                                                    | 79.7 ms: 1.02x faster                                                                                                          |
| regex_effbot   | 1.55 ms                                                                                                                    | 1.65 ms: 1.07x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.00x slower                                                                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.44 sec                                                                                                                   | 1.13 sec: 1.28x faster                                                                                                         |
| unpickle_pure_python | 136 us                                                                                                                     | 108 us: 1.26x faster                                                                                                           |
| xml_etree_process    | 40.2 ms                                                                                                                    | 35.9 ms: 1.12x faster                                                                                                          |
| xml_etree_generate   | 57.8 ms                                                                                                                    | 52.4 ms: 1.10x faster                                                                                                          |
| pickle_pure_python   | 223 us                                                                                                                     | 208 us: 1.07x faster                                                                                                           |
| pickle               | 8.31 us                                                                                                                    | 7.77 us: 1.07x faster                                                                                                          |
| xml_etree_iterparse  | 66.7 ms                                                                                                                    | 62.8 ms: 1.06x faster                                                                                                          |
| json_loads           | 15.0 us                                                                                                                    | 14.3 us: 1.05x faster                                                                                                          |
| json_dumps           | 6.52 ms                                                                                                                    | 6.36 ms: 1.02x faster                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_dict, unpickle_list, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 26.6 ms                                                                                                                    | 27.3 ms: 1.03x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.84 ms                                                                                                                    | 5.32 ms: 1.29x faster                                                                                                          |
| django_template | 25.4 ms                                                                                                                    | 24.5 ms: 1.04x faster                                                                                                          |
| genshi_text     | 15.6 ms                                                                                                                    | 16.0 ms: 1.03x slower                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako                      | 6.84 ms                                                                                                                    | 5.32 ms: 1.29x faster                                                                                                          |
| tomli_loads               | 1.44 sec                                                                                                                   | 1.13 sec: 1.28x faster                                                                                                         |
| unpickle_pure_python      | 136 us                                                                                                                     | 108 us: 1.26x faster                                                                                                           |
| scimark_fft               | 190 ms                                                                                                                     | 154 ms: 1.23x faster                                                                                                           |
| fannkuch                  | 261 ms                                                                                                                     | 215 ms: 1.22x faster                                                                                                           |
| nbody                     | 67.9 ms                                                                                                                    | 57.7 ms: 1.18x faster                                                                                                          |
| bpe_tokeniser             | 2.97 sec                                                                                                                   | 2.57 sec: 1.16x faster                                                                                                         |
| scimark_sparse_mat_mult   | 2.59 ms                                                                                                                    | 2.30 ms: 1.13x faster                                                                                                          |
| xml_etree_process         | 40.2 ms                                                                                                                    | 35.9 ms: 1.12x faster                                                                                                          |
| unpack_sequence           | 37.6 ns                                                                                                                    | 33.7 ns: 1.12x faster                                                                                                          |
| pprint_pformat            | 1.01 sec                                                                                                                   | 911 ms: 1.11x faster                                                                                                           |
| comprehensions            | 11.5 us                                                                                                                    | 10.4 us: 1.11x faster                                                                                                          |
| xml_etree_generate        | 57.8 ms                                                                                                                    | 52.4 ms: 1.10x faster                                                                                                          |
| pyflate                   | 286 ms                                                                                                                     | 260 ms: 1.10x faster                                                                                                           |
| telco                     | 4.78 ms                                                                                                                    | 4.43 ms: 1.08x faster                                                                                                          |
| pickle_pure_python        | 223 us                                                                                                                     | 208 us: 1.07x faster                                                                                                           |
| pickle                    | 8.31 us                                                                                                                    | 7.77 us: 1.07x faster                                                                                                          |
| xml_etree_iterparse       | 66.7 ms                                                                                                                    | 62.8 ms: 1.06x faster                                                                                                          |
| chaos                     | 42.7 ms                                                                                                                    | 40.3 ms: 1.06x faster                                                                                                          |
| async_tree_none_tg        | 178 ms                                                                                                                     | 167 ms: 1.06x faster                                                                                                           |
| pprint_safe_repr          | 496 ms                                                                                                                     | 469 ms: 1.06x faster                                                                                                           |
| meteor_contest            | 75.5 ms                                                                                                                    | 71.4 ms: 1.06x faster                                                                                                          |
| asyncio_websockets        | 172 ms                                                                                                                     | 163 ms: 1.06x faster                                                                                                           |
| k_core                    | 1.72 sec                                                                                                                   | 1.63 sec: 1.05x faster                                                                                                         |
| nqueens                   | 63.8 ms                                                                                                                    | 60.7 ms: 1.05x faster                                                                                                          |
| async_tree_memoization    | 213 ms                                                                                                                     | 203 ms: 1.05x faster                                                                                                           |
| logging_silent            | 57.9 ns                                                                                                                    | 55.2 ns: 1.05x faster                                                                                                          |
| json_loads                | 15.0 us                                                                                                                    | 14.3 us: 1.05x faster                                                                                                          |
| scimark_lu                | 63.2 ms                                                                                                                    | 60.4 ms: 1.05x faster                                                                                                          |
| logging_format            | 6.79 us                                                                                                                    | 6.49 us: 1.05x faster                                                                                                          |
| async_tree_memoization_tg | 221 ms                                                                                                                     | 212 ms: 1.04x faster                                                                                                           |
| float                     | 44.9 ms                                                                                                                    | 43.1 ms: 1.04x faster                                                                                                          |
| deepcopy_memo             | 19.0 us                                                                                                                    | 18.2 us: 1.04x faster                                                                                                          |
| django_template           | 25.4 ms                                                                                                                    | 24.5 ms: 1.04x faster                                                                                                          |
| regex_dna                 | 126 ms                                                                                                                     | 121 ms: 1.04x faster                                                                                                           |
| crypto_pyaes              | 47.8 ms                                                                                                                    | 46.1 ms: 1.03x faster                                                                                                          |
| connected_components      | 335 ms                                                                                                                     | 324 ms: 1.03x faster                                                                                                           |
| coverage                  | 50.5 ms                                                                                                                    | 49.0 ms: 1.03x faster                                                                                                          |
| deepcopy_reduce           | 1.87 us                                                                                                                    | 1.81 us: 1.03x faster                                                                                                          |
| deltablue                 | 2.29 ms                                                                                                                    | 2.22 ms: 1.03x faster                                                                                                          |
| logging_simple            | 6.27 us                                                                                                                    | 6.10 us: 1.03x faster                                                                                                          |
| mdp                       | 819 ms                                                                                                                     | 797 ms: 1.03x faster                                                                                                           |
| json_dumps                | 6.52 ms                                                                                                                    | 6.36 ms: 1.02x faster                                                                                                          |
| pathlib                   | 33.5 ms                                                                                                                    | 32.8 ms: 1.02x faster                                                                                                          |
| shortest_path             | 364 ms                                                                                                                     | 356 ms: 1.02x faster                                                                                                           |
| regex_compile             | 81.5 ms                                                                                                                    | 79.7 ms: 1.02x faster                                                                                                          |
| deepcopy                  | 173 us                                                                                                                     | 169 us: 1.02x faster                                                                                                           |
| sqlglot_v2_parse          | 828 us                                                                                                                     | 811 us: 1.02x faster                                                                                                           |
| pycparser                 | 717 ms                                                                                                                     | 703 ms: 1.02x faster                                                                                                           |
| gc_traversal              | 2.20 ms                                                                                                                    | 2.16 ms: 1.02x faster                                                                                                          |
| sqlglot_v2_normalize      | 72.1 ms                                                                                                                    | 70.8 ms: 1.02x faster                                                                                                          |
| scimark_sor               | 78.6 ms                                                                                                                    | 77.3 ms: 1.02x faster                                                                                                          |
| sphinx                    | 653 ms                                                                                                                     | 644 ms: 1.01x faster                                                                                                           |
| sqlglot_v2_transpile      | 1.03 ms                                                                                                                    | 1.02 ms: 1.01x faster                                                                                                          |
| dulwich_log               | 40.8 ms                                                                                                                    | 41.4 ms: 1.01x slower                                                                                                          |
| docutils                  | 1.64 sec                                                                                                                   | 1.67 sec: 1.02x slower                                                                                                         |
| async_tree_io             | 394 ms                                                                                                                     | 401 ms: 1.02x slower                                                                                                           |
| generators                | 19.7 ms                                                                                                                    | 20.1 ms: 1.02x slower                                                                                                          |
| sympy_integrate           | 12.6 ms                                                                                                                    | 12.9 ms: 1.02x slower                                                                                                          |
| subparsers                | 30.7 ms                                                                                                                    | 31.4 ms: 1.03x slower                                                                                                          |
| python_startup            | 26.6 ms                                                                                                                    | 27.3 ms: 1.03x slower                                                                                                          |
| genshi_text               | 15.6 ms                                                                                                                    | 16.0 ms: 1.03x slower                                                                                                          |
| sympy_str                 | 173 ms                                                                                                                     | 178 ms: 1.03x slower                                                                                                           |
| go                        | 77.6 ms                                                                                                                    | 79.7 ms: 1.03x slower                                                                                                          |
| scimark_monte_carlo       | 41.2 ms                                                                                                                    | 42.3 ms: 1.03x slower                                                                                                          |
| sqlite_synth              | 1.58 us                                                                                                                    | 1.63 us: 1.03x slower                                                                                                          |
| many_optionals            | 568 us                                                                                                                     | 596 us: 1.05x slower                                                                                                           |
| async_generators          | 241 ms                                                                                                                     | 255 ms: 1.06x slower                                                                                                           |
| sympy_expand              | 287 ms                                                                                                                     | 305 ms: 1.06x slower                                                                                                           |
| regex_effbot              | 1.55 ms                                                                                                                    | 1.65 ms: 1.07x slower                                                                                                          |
| asyncio_tcp_ssl           | 1.31 sec                                                                                                                   | 1.42 sec: 1.09x slower                                                                                                         |
| asyncio_tcp               | 396 ms                                                                                                                     | 519 ms: 1.31x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (30): richards_super, thrift, bench_thread_pool, xml_etree_parse, 2to3, python_startup_no_site, json, pidigits, async_tree_none, pickle_dict, regex_v8, unpickle_list, richards, bench_mp_pool, async_tree_io_tg, async_tree_cpu_io_mixed, coroutines, spectral_norm, sympy_sum, create_gc_cycles, hexiom, html5lib, raytrace, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, sqlglot_v2_optimize, pickle_list, unpickle, genshi_xml, pylint

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown