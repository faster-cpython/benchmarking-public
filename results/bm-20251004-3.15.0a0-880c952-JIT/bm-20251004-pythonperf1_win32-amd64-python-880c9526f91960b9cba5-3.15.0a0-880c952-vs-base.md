# Results vs. base

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                                                                                     | 213 ms: 1.02x faster                                                                                                           |
| html5lib       | 37.6 ms                                                                                                                    | 37.1 ms: 1.02x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| coroutines              | 14.8 ms                                                                                                                    | 14.2 ms: 1.04x faster                                                                                                          |
| async_tree_io_tg        | 388 ms                                                                                                                     | 376 ms: 1.03x faster                                                                                                           |
| async_tree_none         | 175 ms                                                                                                                     | 170 ms: 1.03x faster                                                                                                           |
| async_tree_none_tg      | 169 ms                                                                                                                     | 164 ms: 1.03x faster                                                                                                           |
| async_tree_memoization  | 204 ms                                                                                                                     | 200 ms: 1.02x faster                                                                                                           |
| async_tree_cpu_io_mixed | 327 ms                                                                                                                     | 336 ms: 1.03x slower                                                                                                           |
| async_generators        | 230 ms                                                                                                                     | 240 ms: 1.04x slower                                                                                                           |
| asyncio_websockets      | 161 ms                                                                                                                     | 168 ms: 1.04x slower                                                                                                           |
| asyncio_tcp_ssl         | 1.24 sec                                                                                                                   | 1.39 sec: 1.12x slower                                                                                                         |
| asyncio_tcp             | 416 ms                                                                                                                     | 496 ms: 1.19x slower                                                                                                           |
| Geometric mean          | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.5 ms                                                                                                                    | 53.6 ms: 1.18x faster                                                                                                          |
| float          | 43.4 ms                                                                                                                    | 43.0 ms: 1.01x faster                                                                                                          |
| pidigits       | 146 ms                                                                                                                     | 148 ms: 1.01x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                                                                     | 114 ms: 1.05x faster                                                                                                           |
| regex_compile  | 80.1 ms                                                                                                                    | 76.4 ms: 1.05x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 135 us                                                                                                                     | 105 us: 1.29x faster                                                                                                           |
| tomli_loads          | 1.37 sec                                                                                                                   | 1.08 sec: 1.27x faster                                                                                                         |
| xml_etree_generate   | 55.2 ms                                                                                                                    | 48.8 ms: 1.13x faster                                                                                                          |
| xml_etree_process    | 38.6 ms                                                                                                                    | 34.5 ms: 1.12x faster                                                                                                          |
| unpickle_list        | 2.84 us                                                                                                                    | 2.70 us: 1.05x faster                                                                                                          |
| pickle_pure_python   | 210 us                                                                                                                     | 201 us: 1.05x faster                                                                                                           |
| xml_etree_iterparse  | 62.7 ms                                                                                                                    | 60.3 ms: 1.04x faster                                                                                                          |
| json_dumps           | 5.50 ms                                                                                                                    | 5.38 ms: 1.02x faster                                                                                                          |
| json_loads           | 14.0 us                                                                                                                    | 13.9 us: 1.01x faster                                                                                                          |
| pickle_list          | 3.24 us                                                                                                                    | 3.28 us: 1.01x slower                                                                                                          |
| pickle_dict          | 19.3 us                                                                                                                    | 19.6 us: 1.01x slower                                                                                                          |
| pickle               | 7.71 us                                                                                                                    | 7.83 us: 1.02x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.80 ms                                                                                                                    | 5.33 ms: 1.28x faster                                                                                                          |
| genshi_xml     | 34.5 ms                                                                                                                    | 33.9 ms: 1.02x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python     | 135 us                                                                                                                     | 105 us: 1.29x faster                                                                                                           |
| mako                     | 6.80 ms                                                                                                                    | 5.33 ms: 1.28x faster                                                                                                          |
| tomli_loads              | 1.37 sec                                                                                                                   | 1.08 sec: 1.27x faster                                                                                                         |
| scimark_fft              | 168 ms                                                                                                                     | 136 ms: 1.23x faster                                                                                                           |
| fannkuch                 | 267 ms                                                                                                                     | 217 ms: 1.23x faster                                                                                                           |
| bpe_tokeniser            | 2.99 sec                                                                                                                   | 2.47 sec: 1.21x faster                                                                                                         |
| pprint_safe_repr         | 488 ms                                                                                                                     | 409 ms: 1.19x faster                                                                                                           |
| nbody                    | 63.5 ms                                                                                                                    | 53.6 ms: 1.18x faster                                                                                                          |
| pprint_pformat           | 986 ms                                                                                                                     | 835 ms: 1.18x faster                                                                                                           |
| pyflate                  | 287 ms                                                                                                                     | 246 ms: 1.16x faster                                                                                                           |
| xml_etree_generate       | 55.2 ms                                                                                                                    | 48.8 ms: 1.13x faster                                                                                                          |
| xml_etree_process        | 38.6 ms                                                                                                                    | 34.5 ms: 1.12x faster                                                                                                          |
| scimark_sparse_mat_mult  | 2.43 ms                                                                                                                    | 2.23 ms: 1.09x faster                                                                                                          |
| sqlglot_v2_parse         | 825 us                                                                                                                     | 762 us: 1.08x faster                                                                                                           |
| crypto_pyaes             | 47.7 ms                                                                                                                    | 44.1 ms: 1.08x faster                                                                                                          |
| sqlglot_v2_transpile     | 1.03 ms                                                                                                                    | 957 us: 1.08x faster                                                                                                           |
| telco                    | 4.18 ms                                                                                                                    | 3.90 ms: 1.07x faster                                                                                                          |
| k_core                   | 1.67 sec                                                                                                                   | 1.58 sec: 1.06x faster                                                                                                         |
| pycparser                | 712 ms                                                                                                                     | 676 ms: 1.05x faster                                                                                                           |
| regex_dna                | 120 ms                                                                                                                     | 114 ms: 1.05x faster                                                                                                           |
| comprehensions           | 11.0 us                                                                                                                    | 10.5 us: 1.05x faster                                                                                                          |
| unpickle_list            | 2.84 us                                                                                                                    | 2.70 us: 1.05x faster                                                                                                          |
| regex_compile            | 80.1 ms                                                                                                                    | 76.4 ms: 1.05x faster                                                                                                          |
| pickle_pure_python       | 210 us                                                                                                                     | 201 us: 1.05x faster                                                                                                           |
| nqueens                  | 62.3 ms                                                                                                                    | 59.7 ms: 1.04x faster                                                                                                          |
| coroutines               | 14.8 ms                                                                                                                    | 14.2 ms: 1.04x faster                                                                                                          |
| xml_etree_iterparse      | 62.7 ms                                                                                                                    | 60.3 ms: 1.04x faster                                                                                                          |
| typing_runtime_protocols | 105 us                                                                                                                     | 101 us: 1.04x faster                                                                                                           |
| deepcopy_memo            | 16.7 us                                                                                                                    | 16.1 us: 1.04x faster                                                                                                          |
| async_tree_io_tg         | 388 ms                                                                                                                     | 376 ms: 1.03x faster                                                                                                           |
| bench_thread_pool        | 846 us                                                                                                                     | 818 us: 1.03x faster                                                                                                           |
| logging_simple           | 5.92 us                                                                                                                    | 5.73 us: 1.03x faster                                                                                                          |
| go                       | 77.6 ms                                                                                                                    | 75.2 ms: 1.03x faster                                                                                                          |
| async_tree_none          | 175 ms                                                                                                                     | 170 ms: 1.03x faster                                                                                                           |
| deepcopy_reduce          | 1.81 us                                                                                                                    | 1.76 us: 1.03x faster                                                                                                          |
| raytrace                 | 179 ms                                                                                                                     | 174 ms: 1.03x faster                                                                                                           |
| async_tree_none_tg       | 169 ms                                                                                                                     | 164 ms: 1.03x faster                                                                                                           |
| deepcopy                 | 167 us                                                                                                                     | 162 us: 1.03x faster                                                                                                           |
| spectral_norm            | 66.9 ms                                                                                                                    | 65.0 ms: 1.03x faster                                                                                                          |
| dulwich_log              | 39.1 ms                                                                                                                    | 38.2 ms: 1.02x faster                                                                                                          |
| sqlite_synth             | 1.57 us                                                                                                                    | 1.53 us: 1.02x faster                                                                                                          |
| async_tree_memoization   | 204 ms                                                                                                                     | 200 ms: 1.02x faster                                                                                                           |
| json_dumps               | 5.50 ms                                                                                                                    | 5.38 ms: 1.02x faster                                                                                                          |
| logging_format           | 6.43 us                                                                                                                    | 6.29 us: 1.02x faster                                                                                                          |
| connected_components     | 320 ms                                                                                                                     | 314 ms: 1.02x faster                                                                                                           |
| scimark_monte_carlo      | 40.6 ms                                                                                                                    | 39.9 ms: 1.02x faster                                                                                                          |
| 2to3                     | 217 ms                                                                                                                     | 213 ms: 1.02x faster                                                                                                           |
| mdp                      | 798 ms                                                                                                                     | 784 ms: 1.02x faster                                                                                                           |
| hexiom                   | 4.10 ms                                                                                                                    | 4.03 ms: 1.02x faster                                                                                                          |
| genshi_xml               | 34.5 ms                                                                                                                    | 33.9 ms: 1.02x faster                                                                                                          |
| coverage                 | 49.0 ms                                                                                                                    | 48.3 ms: 1.02x faster                                                                                                          |
| html5lib                 | 37.6 ms                                                                                                                    | 37.1 ms: 1.02x faster                                                                                                          |
| sympy_sum                | 84.9 ms                                                                                                                    | 83.9 ms: 1.01x faster                                                                                                          |
| chaos                    | 40.5 ms                                                                                                                    | 40.0 ms: 1.01x faster                                                                                                          |
| scimark_lu               | 58.9 ms                                                                                                                    | 58.3 ms: 1.01x faster                                                                                                          |
| shortest_path            | 351 ms                                                                                                                     | 347 ms: 1.01x faster                                                                                                           |
| bench_mp_pool            | 89.5 ms                                                                                                                    | 88.5 ms: 1.01x faster                                                                                                          |
| float                    | 43.4 ms                                                                                                                    | 43.0 ms: 1.01x faster                                                                                                          |
| richards                 | 27.2 ms                                                                                                                    | 27.0 ms: 1.01x faster                                                                                                          |
| subparsers               | 30.9 ms                                                                                                                    | 30.6 ms: 1.01x faster                                                                                                          |
| json_loads               | 14.0 us                                                                                                                    | 13.9 us: 1.01x faster                                                                                                          |
| sympy_str                | 165 ms                                                                                                                     | 166 ms: 1.01x slower                                                                                                           |
| sqlglot_v2_normalize     | 69.9 ms                                                                                                                    | 70.6 ms: 1.01x slower                                                                                                          |
| sympy_integrate          | 12.2 ms                                                                                                                    | 12.3 ms: 1.01x slower                                                                                                          |
| sympy_expand             | 282 ms                                                                                                                     | 285 ms: 1.01x slower                                                                                                           |
| pickle_list              | 3.24 us                                                                                                                    | 3.28 us: 1.01x slower                                                                                                          |
| pidigits                 | 146 ms                                                                                                                     | 148 ms: 1.01x slower                                                                                                           |
| pathlib                  | 29.1 ms                                                                                                                    | 29.4 ms: 1.01x slower                                                                                                          |
| pickle_dict              | 19.3 us                                                                                                                    | 19.6 us: 1.01x slower                                                                                                          |
| pickle                   | 7.71 us                                                                                                                    | 7.83 us: 1.02x slower                                                                                                          |
| sqlglot_v2_optimize      | 33.8 ms                                                                                                                    | 34.6 ms: 1.02x slower                                                                                                          |
| async_tree_cpu_io_mixed  | 327 ms                                                                                                                     | 336 ms: 1.03x slower                                                                                                           |
| async_generators         | 230 ms                                                                                                                     | 240 ms: 1.04x slower                                                                                                           |
| asyncio_websockets       | 161 ms                                                                                                                     | 168 ms: 1.04x slower                                                                                                           |
| deltablue                | 2.19 ms                                                                                                                    | 2.30 ms: 1.05x slower                                                                                                          |
| unpack_sequence          | 32.0 ns                                                                                                                    | 35.6 ns: 1.11x slower                                                                                                          |
| asyncio_tcp_ssl          | 1.24 sec                                                                                                                   | 1.39 sec: 1.12x slower                                                                                                         |
| asyncio_tcp              | 416 ms                                                                                                                     | 496 ms: 1.19x slower                                                                                                           |
| Geometric mean           | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (24): regex_v8, async_tree_io, python_startup_no_site, logging_silent, scimark_sor, gc_traversal, many_optionals, regex_effbot, generators, richards_super, sphinx, json, genshi_text, django_template, async_tree_cpu_io_mixed_tg, unpickle, xml_etree_parse, thrift, pylint, meteor_contest, async_tree_memoization_tg, python_startup, docutils, create_gc_cycles

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown