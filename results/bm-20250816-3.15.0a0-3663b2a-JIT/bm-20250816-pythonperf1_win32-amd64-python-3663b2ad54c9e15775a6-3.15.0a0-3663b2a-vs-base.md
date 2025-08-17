# Results vs. base

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.026x faster
- HPT reliability: 92.46%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                                                                                     | 216 ms: 1.01x faster                                                                                                           |
| docutils       | 1.59 sec                                                                                                                   | 1.62 sec: 1.02x slower                                                                                                         |
| html5lib       | 37.3 ms                                                                                                                    | 37.8 ms: 1.01x slower                                                                                                          |
| sphinx         | 615 ms                                                                                                                     | 626 ms: 1.02x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| coroutines                | 14.6 ms                                                                                                                    | 13.8 ms: 1.06x faster                                                                                                          |
| async_tree_io_tg          | 386 ms                                                                                                                     | 382 ms: 1.01x faster                                                                                                           |
| asyncio_tcp_ssl           | 1.23 sec                                                                                                                   | 1.25 sec: 1.01x slower                                                                                                         |
| async_tree_io             | 383 ms                                                                                                                     | 389 ms: 1.01x slower                                                                                                           |
| async_tree_memoization_tg | 208 ms                                                                                                                     | 213 ms: 1.02x slower                                                                                                           |
| async_generators          | 227 ms                                                                                                                     | 238 ms: 1.05x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.00x slower                                                                                                                   |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.5 ms                                                                                                                    | 54.6 ms: 1.16x faster                                                                                                          |
| pidigits       | 144 ms                                                                                                                     | 145 ms: 1.01x slower                                                                                                           |
| float          | 42.6 ms                                                                                                                    | 43.9 ms: 1.03x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 13.9 ms                                                                                                                    | 13.1 ms: 1.06x faster                                                                                                          |
| regex_dna      | 118 ms                                                                                                                     | 114 ms: 1.04x faster                                                                                                           |
| regex_compile  | 79.0 ms                                                                                                                    | 78.0 ms: 1.01x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.42 sec                                                                                                                   | 1.10 sec: 1.28x faster                                                                                                         |
| unpickle_pure_python | 133 us                                                                                                                     | 105 us: 1.26x faster                                                                                                           |
| xml_etree_generate   | 56.6 ms                                                                                                                    | 50.2 ms: 1.13x faster                                                                                                          |
| xml_etree_process    | 38.8 ms                                                                                                                    | 35.2 ms: 1.10x faster                                                                                                          |
| pickle               | 7.93 us                                                                                                                    | 7.43 us: 1.07x faster                                                                                                          |
| pickle_pure_python   | 212 us                                                                                                                     | 199 us: 1.06x faster                                                                                                           |
| xml_etree_iterparse  | 64.3 ms                                                                                                                    | 61.1 ms: 1.05x faster                                                                                                          |
| unpickle_list        | 2.88 us                                                                                                                    | 2.75 us: 1.05x faster                                                                                                          |
| pickle_list          | 3.27 us                                                                                                                    | 3.21 us: 1.02x faster                                                                                                          |
| unpickle             | 8.50 us                                                                                                                    | 8.39 us: 1.01x faster                                                                                                          |
| json_dumps           | 5.43 ms                                                                                                                    | 5.39 ms: 1.01x faster                                                                                                          |
| json_loads           | 13.9 us                                                                                                                    | 14.2 us: 1.02x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.58 ms                                                                                                                    | 5.20 ms: 1.27x faster                                                                                                          |
| django_template | 24.5 ms                                                                                                                    | 23.9 ms: 1.02x faster                                                                                                          |
| genshi_text     | 15.3 ms                                                                                                                    | 15.7 ms: 1.02x slower                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads               | 1.42 sec                                                                                                                   | 1.10 sec: 1.28x faster                                                                                                         |
| fannkuch                  | 262 ms                                                                                                                     | 207 ms: 1.27x faster                                                                                                           |
| mako                      | 6.58 ms                                                                                                                    | 5.20 ms: 1.27x faster                                                                                                          |
| unpickle_pure_python      | 133 us                                                                                                                     | 105 us: 1.26x faster                                                                                                           |
| scimark_fft               | 179 ms                                                                                                                     | 149 ms: 1.20x faster                                                                                                           |
| bpe_tokeniser             | 2.91 sec                                                                                                                   | 2.49 sec: 1.17x faster                                                                                                         |
| nbody                     | 63.5 ms                                                                                                                    | 54.6 ms: 1.16x faster                                                                                                          |
| xml_etree_generate        | 56.6 ms                                                                                                                    | 50.2 ms: 1.13x faster                                                                                                          |
| pprint_safe_repr          | 489 ms                                                                                                                     | 436 ms: 1.12x faster                                                                                                           |
| pprint_pformat            | 998 ms                                                                                                                     | 891 ms: 1.12x faster                                                                                                           |
| telco                     | 4.40 ms                                                                                                                    | 3.94 ms: 1.12x faster                                                                                                          |
| scimark_sparse_mat_mult   | 2.47 ms                                                                                                                    | 2.21 ms: 1.11x faster                                                                                                          |
| pyflate                   | 289 ms                                                                                                                     | 260 ms: 1.11x faster                                                                                                           |
| xml_etree_process         | 38.8 ms                                                                                                                    | 35.2 ms: 1.10x faster                                                                                                          |
| sqlglot_v2_parse          | 831 us                                                                                                                     | 773 us: 1.07x faster                                                                                                           |
| sqlglot_v2_transpile      | 1.04 ms                                                                                                                    | 969 us: 1.07x faster                                                                                                           |
| pickle                    | 7.93 us                                                                                                                    | 7.43 us: 1.07x faster                                                                                                          |
| regex_v8                  | 13.9 ms                                                                                                                    | 13.1 ms: 1.06x faster                                                                                                          |
| pickle_pure_python        | 212 us                                                                                                                     | 199 us: 1.06x faster                                                                                                           |
| coroutines                | 14.6 ms                                                                                                                    | 13.8 ms: 1.06x faster                                                                                                          |
| comprehensions            | 11.1 us                                                                                                                    | 10.5 us: 1.06x faster                                                                                                          |
| xml_etree_iterparse       | 64.3 ms                                                                                                                    | 61.1 ms: 1.05x faster                                                                                                          |
| unpickle_list             | 2.88 us                                                                                                                    | 2.75 us: 1.05x faster                                                                                                          |
| sqlite_synth              | 1.57 us                                                                                                                    | 1.51 us: 1.04x faster                                                                                                          |
| regex_dna                 | 118 ms                                                                                                                     | 114 ms: 1.04x faster                                                                                                           |
| k_core                    | 1.65 sec                                                                                                                   | 1.59 sec: 1.03x faster                                                                                                         |
| deepcopy_memo             | 18.3 us                                                                                                                    | 17.8 us: 1.03x faster                                                                                                          |
| crypto_pyaes              | 46.0 ms                                                                                                                    | 44.8 ms: 1.03x faster                                                                                                          |
| meteor_contest            | 70.9 ms                                                                                                                    | 69.1 ms: 1.03x faster                                                                                                          |
| generators                | 19.3 ms                                                                                                                    | 18.9 ms: 1.03x faster                                                                                                          |
| django_template           | 24.5 ms                                                                                                                    | 23.9 ms: 1.02x faster                                                                                                          |
| pickle_list               | 3.27 us                                                                                                                    | 3.21 us: 1.02x faster                                                                                                          |
| connected_components      | 322 ms                                                                                                                     | 317 ms: 1.02x faster                                                                                                           |
| sqlglot_v2_normalize      | 69.9 ms                                                                                                                    | 68.9 ms: 1.02x faster                                                                                                          |
| json                      | 2.93 ms                                                                                                                    | 2.89 ms: 1.01x faster                                                                                                          |
| unpickle                  | 8.50 us                                                                                                                    | 8.39 us: 1.01x faster                                                                                                          |
| regex_compile             | 79.0 ms                                                                                                                    | 78.0 ms: 1.01x faster                                                                                                          |
| async_tree_io_tg          | 386 ms                                                                                                                     | 382 ms: 1.01x faster                                                                                                           |
| shortest_path             | 353 ms                                                                                                                     | 350 ms: 1.01x faster                                                                                                           |
| 2to3                      | 218 ms                                                                                                                     | 216 ms: 1.01x faster                                                                                                           |
| nqueens                   | 60.6 ms                                                                                                                    | 60.0 ms: 1.01x faster                                                                                                          |
| json_dumps                | 5.43 ms                                                                                                                    | 5.39 ms: 1.01x faster                                                                                                          |
| deepcopy                  | 169 us                                                                                                                     | 168 us: 1.01x faster                                                                                                           |
| sqlglot_v2_optimize       | 33.7 ms                                                                                                                    | 33.8 ms: 1.00x slower                                                                                                          |
| dulwich_log               | 38.5 ms                                                                                                                    | 38.7 ms: 1.00x slower                                                                                                          |
| logging_silent            | 55.0 ns                                                                                                                    | 55.2 ns: 1.00x slower                                                                                                          |
| pidigits                  | 144 ms                                                                                                                     | 145 ms: 1.01x slower                                                                                                           |
| richards                  | 26.7 ms                                                                                                                    | 26.9 ms: 1.01x slower                                                                                                          |
| mdp                       | 794 ms                                                                                                                     | 801 ms: 1.01x slower                                                                                                           |
| sympy_str                 | 167 ms                                                                                                                     | 168 ms: 1.01x slower                                                                                                           |
| asyncio_tcp_ssl           | 1.23 sec                                                                                                                   | 1.25 sec: 1.01x slower                                                                                                         |
| bench_mp_pool             | 91.7 ms                                                                                                                    | 92.8 ms: 1.01x slower                                                                                                          |
| html5lib                  | 37.3 ms                                                                                                                    | 37.8 ms: 1.01x slower                                                                                                          |
| async_tree_io             | 383 ms                                                                                                                     | 389 ms: 1.01x slower                                                                                                           |
| spectral_norm             | 64.6 ms                                                                                                                    | 65.7 ms: 1.02x slower                                                                                                          |
| sphinx                    | 615 ms                                                                                                                     | 626 ms: 1.02x slower                                                                                                           |
| scimark_lu                | 57.6 ms                                                                                                                    | 58.6 ms: 1.02x slower                                                                                                          |
| sympy_integrate           | 12.2 ms                                                                                                                    | 12.4 ms: 1.02x slower                                                                                                          |
| pathlib                   | 28.5 ms                                                                                                                    | 29.1 ms: 1.02x slower                                                                                                          |
| raytrace                  | 174 ms                                                                                                                     | 178 ms: 1.02x slower                                                                                                           |
| async_tree_memoization_tg | 208 ms                                                                                                                     | 213 ms: 1.02x slower                                                                                                           |
| deltablue                 | 2.18 ms                                                                                                                    | 2.22 ms: 1.02x slower                                                                                                          |
| genshi_text               | 15.3 ms                                                                                                                    | 15.7 ms: 1.02x slower                                                                                                          |
| json_loads                | 13.9 us                                                                                                                    | 14.2 us: 1.02x slower                                                                                                          |
| docutils                  | 1.59 sec                                                                                                                   | 1.62 sec: 1.02x slower                                                                                                         |
| sympy_expand              | 282 ms                                                                                                                     | 290 ms: 1.03x slower                                                                                                           |
| scimark_sor               | 76.0 ms                                                                                                                    | 78.2 ms: 1.03x slower                                                                                                          |
| float                     | 42.6 ms                                                                                                                    | 43.9 ms: 1.03x slower                                                                                                          |
| logging_format            | 6.26 us                                                                                                                    | 6.47 us: 1.03x slower                                                                                                          |
| logging_simple            | 5.83 us                                                                                                                    | 6.04 us: 1.04x slower                                                                                                          |
| create_gc_cycles          | 1.26 ms                                                                                                                    | 1.31 ms: 1.04x slower                                                                                                          |
| async_generators          | 227 ms                                                                                                                     | 238 ms: 1.05x slower                                                                                                           |
| scimark_monte_carlo       | 39.8 ms                                                                                                                    | 42.1 ms: 1.06x slower                                                                                                          |
| gc_traversal              | 2.06 ms                                                                                                                    | 2.20 ms: 1.07x slower                                                                                                          |
| Geometric mean            | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (28): thrift, pycparser, python_startup_no_site, bench_thread_pool, hexiom, async_tree_cpu_io_mixed_tg, async_tree_none, typing_runtime_protocols, chaos, async_tree_none_tg, async_tree_memoization, coverage, xml_etree_parse, subparsers, sympy_sum, deepcopy_reduce, python_startup, regex_effbot, richards_super, pickle_dict, async_tree_cpu_io_mixed, pylint, go, asyncio_tcp, many_optionals, genshi_xml, unpack_sequence, asyncio_websockets

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 92.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown