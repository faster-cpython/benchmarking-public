# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.091x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                      | 247 ms: 1.10x slower                                                           |
| docutils       | 1.71 sec                                                                    | 1.77 sec: 1.04x slower                                                         |
| html5lib       | 40.1 ms                                                                     | 45.0 ms: 1.12x slower                                                          |
| sphinx         | 668 ms                                                                      | 705 ms: 1.05x slower                                                           |
| tornado_http   | 92.9 ms                                                                     | 96.4 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg          | 634 ms                                                                      | 660 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed   | 383 ms                                                                      | 402 ms: 1.05x slower                                                           |
| async_tree_memoization    | 279 ms                                                                      | 294 ms: 1.06x slower                                                           |
| async_tree_io             | 559 ms                                                                      | 592 ms: 1.06x slower                                                           |
| async_tree_none_tg        | 211 ms                                                                      | 224 ms: 1.06x slower                                                           |
| async_tree_memoization_tg | 258 ms                                                                      | 276 ms: 1.07x slower                                                           |
| async_tree_none           | 220 ms                                                                      | 237 ms: 1.08x slower                                                           |
| coroutines                | 13.6 ms                                                                     | 15.1 ms: 1.12x slower                                                          |
| async_generators          | 238 ms                                                                      | 273 ms: 1.15x slower                                                           |
| Geometric mean            | (ref)                                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 148 ms: 1.00x slower                                                           |
| float          | 55.0 ms                                                                     | 61.5 ms: 1.12x slower                                                          |
| nbody          | 76.9 ms                                                                     | 89.4 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                      | 114 ms: 1.08x faster                                                           |
| regex_v8       | 15.2 ms                                                                     | 15.1 ms: 1.00x faster                                                          |
| regex_effbot   | 1.55 ms                                                                     | 1.58 ms: 1.02x slower                                                          |
| regex_compile  | 90.6 ms                                                                     | 99.9 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.7 ms                                                                     | 69.9 ms: 1.06x slower                                                          |
| json_dumps           | 6.62 ms                                                                     | 7.13 ms: 1.08x slower                                                          |
| xml_etree_generate   | 57.1 ms                                                                     | 63.6 ms: 1.11x slower                                                          |
| tomli_loads          | 1.58 sec                                                                    | 1.77 sec: 1.12x slower                                                         |
| xml_etree_process    | 40.2 ms                                                                     | 45.9 ms: 1.14x slower                                                          |
| pickle_pure_python   | 217 us                                                                      | 249 us: 1.15x slower                                                           |
| unpickle_pure_python | 151 us                                                                      | 183 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                                       | 1.10x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 17.9 ms                                                                     | 17.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 25.7 ms                                                                     | 28.4 ms: 1.11x slower                                                          |
| genshi_xml      | 36.5 ms                                                                     | 42.6 ms: 1.17x slower                                                          |
| genshi_text     | 17.1 ms                                                                     | 20.1 ms: 1.17x slower                                                          |
| mako            | 6.64 ms                                                                     | 8.02 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.16x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna                 | 123 ms                                                                      | 114 ms: 1.08x faster                                                           |
| python_startup_no_site    | 17.9 ms                                                                     | 17.7 ms: 1.01x faster                                                          |
| regex_v8                  | 15.2 ms                                                                     | 15.1 ms: 1.00x faster                                                          |
| pidigits                  | 147 ms                                                                      | 148 ms: 1.00x slower                                                           |
| bench_mp_pool             | 83.1 ms                                                                     | 84.0 ms: 1.01x slower                                                          |
| pathlib                   | 78.6 ms                                                                     | 79.7 ms: 1.01x slower                                                          |
| regex_effbot              | 1.55 ms                                                                     | 1.58 ms: 1.02x slower                                                          |
| sqlite_synth              | 1.63 us                                                                     | 1.66 us: 1.02x slower                                                          |
| k_core                    | 2.52 sec                                                                    | 2.59 sec: 1.03x slower                                                         |
| tornado_http              | 92.9 ms                                                                     | 96.4 ms: 1.04x slower                                                          |
| docutils                  | 1.71 sec                                                                    | 1.77 sec: 1.04x slower                                                         |
| async_tree_io_tg          | 634 ms                                                                      | 660 ms: 1.04x slower                                                           |
| json                      | 3.11 ms                                                                     | 3.24 ms: 1.04x slower                                                          |
| bench_thread_pool         | 811 us                                                                      | 851 us: 1.05x slower                                                           |
| async_tree_cpu_io_mixed   | 383 ms                                                                      | 402 ms: 1.05x slower                                                           |
| dulwich_log               | 42.5 ms                                                                     | 44.7 ms: 1.05x slower                                                          |
| telco                     | 4.91 ms                                                                     | 5.17 ms: 1.05x slower                                                          |
| sphinx                    | 668 ms                                                                      | 705 ms: 1.05x slower                                                           |
| async_tree_memoization    | 279 ms                                                                      | 294 ms: 1.06x slower                                                           |
| async_tree_io             | 559 ms                                                                      | 592 ms: 1.06x slower                                                           |
| shortest_path             | 356 ms                                                                      | 379 ms: 1.06x slower                                                           |
| async_tree_none_tg        | 211 ms                                                                      | 224 ms: 1.06x slower                                                           |
| xml_etree_iterparse       | 65.7 ms                                                                     | 69.9 ms: 1.06x slower                                                          |
| coverage                  | 45.8 ms                                                                     | 48.8 ms: 1.07x slower                                                          |
| async_tree_memoization_tg | 258 ms                                                                      | 276 ms: 1.07x slower                                                           |
| meteor_contest            | 75.8 ms                                                                     | 81.5 ms: 1.07x slower                                                          |
| sympy_sum                 | 89.2 ms                                                                     | 95.9 ms: 1.08x slower                                                          |
| sqlglot_normalize         | 199 ms                                                                      | 214 ms: 1.08x slower                                                           |
| json_dumps                | 6.62 ms                                                                     | 7.13 ms: 1.08x slower                                                          |
| connected_components      | 322 ms                                                                      | 348 ms: 1.08x slower                                                           |
| sympy_str                 | 177 ms                                                                      | 191 ms: 1.08x slower                                                           |
| async_tree_none           | 220 ms                                                                      | 237 ms: 1.08x slower                                                           |
| sympy_expand              | 304 ms                                                                      | 329 ms: 1.08x slower                                                           |
| sympy_integrate           | 13.3 ms                                                                     | 14.4 ms: 1.08x slower                                                          |
| sqlglot_optimize          | 37.2 ms                                                                     | 40.3 ms: 1.08x slower                                                          |
| 2to3                      | 224 ms                                                                      | 247 ms: 1.10x slower                                                           |
| regex_compile             | 90.6 ms                                                                     | 99.9 ms: 1.10x slower                                                          |
| thrift                    | 518 us                                                                      | 572 us: 1.11x slower                                                           |
| django_template           | 25.7 ms                                                                     | 28.4 ms: 1.11x slower                                                          |
| xml_etree_generate        | 57.1 ms                                                                     | 63.6 ms: 1.11x slower                                                          |
| coroutines                | 13.6 ms                                                                     | 15.1 ms: 1.12x slower                                                          |
| raytrace                  | 198 ms                                                                      | 220 ms: 1.12x slower                                                           |
| sqlglot_transpile         | 1.12 ms                                                                     | 1.25 ms: 1.12x slower                                                          |
| logging_format            | 6.82 us                                                                     | 7.61 us: 1.12x slower                                                          |
| tomli_loads               | 1.58 sec                                                                    | 1.77 sec: 1.12x slower                                                         |
| float                     | 55.0 ms                                                                     | 61.5 ms: 1.12x slower                                                          |
| bpe_tokeniser             | 3.04 sec                                                                    | 3.42 sec: 1.12x slower                                                         |
| typing_runtime_protocols  | 112 us                                                                      | 126 us: 1.12x slower                                                           |
| html5lib                  | 40.1 ms                                                                     | 45.0 ms: 1.12x slower                                                          |
| sqlglot_parse             | 910 us                                                                      | 1.02 ms: 1.12x slower                                                          |
| logging_simple            | 6.35 us                                                                     | 7.15 us: 1.12x slower                                                          |
| deepcopy_reduce           | 1.94 us                                                                     | 2.19 us: 1.13x slower                                                          |
| deltablue                 | 2.31 ms                                                                     | 2.60 ms: 1.13x slower                                                          |
| richards_super            | 36.6 ms                                                                     | 41.4 ms: 1.13x slower                                                          |
| deepcopy                  | 187 us                                                                      | 212 us: 1.13x slower                                                           |
| pycparser                 | 721 ms                                                                      | 820 ms: 1.14x slower                                                           |
| pyflate                   | 315 ms                                                                      | 358 ms: 1.14x slower                                                           |
| xml_etree_process         | 40.2 ms                                                                     | 45.9 ms: 1.14x slower                                                          |
| mdp                       | 1.43 sec                                                                    | 1.64 sec: 1.14x slower                                                         |
| richards                  | 32.3 ms                                                                     | 36.9 ms: 1.14x slower                                                          |
| generators                | 22.0 ms                                                                     | 25.2 ms: 1.14x slower                                                          |
| pprint_pformat            | 1.09 sec                                                                    | 1.25 sec: 1.15x slower                                                         |
| pprint_safe_repr          | 535 ms                                                                      | 614 ms: 1.15x slower                                                           |
| async_generators          | 238 ms                                                                      | 273 ms: 1.15x slower                                                           |
| scimark_fft               | 196 ms                                                                      | 226 ms: 1.15x slower                                                           |
| pickle_pure_python        | 217 us                                                                      | 249 us: 1.15x slower                                                           |
| logging_silent            | 61.7 ns                                                                     | 71.3 ns: 1.16x slower                                                          |
| scimark_sparse_mat_mult   | 2.75 ms                                                                     | 3.18 ms: 1.16x slower                                                          |
| nbody                     | 76.9 ms                                                                     | 89.4 ms: 1.16x slower                                                          |
| genshi_xml                | 36.5 ms                                                                     | 42.6 ms: 1.17x slower                                                          |
| scimark_monte_carlo       | 46.7 ms                                                                     | 54.7 ms: 1.17x slower                                                          |
| genshi_text               | 17.1 ms                                                                     | 20.1 ms: 1.17x slower                                                          |
| nqueens                   | 62.4 ms                                                                     | 73.3 ms: 1.17x slower                                                          |
| scimark_sor               | 88.0 ms                                                                     | 103 ms: 1.17x slower                                                           |
| hexiom                    | 4.35 ms                                                                     | 5.14 ms: 1.18x slower                                                          |
| crypto_pyaes              | 47.9 ms                                                                     | 57.4 ms: 1.20x slower                                                          |
| chaos                     | 43.3 ms                                                                     | 52.0 ms: 1.20x slower                                                          |
| mako                      | 6.64 ms                                                                     | 8.02 ms: 1.21x slower                                                          |
| unpickle_pure_python      | 151 us                                                                      | 183 us: 1.22x slower                                                           |
| scimark_lu                | 61.3 ms                                                                     | 74.6 ms: 1.22x slower                                                          |
| comprehensions            | 11.8 us                                                                     | 14.6 us: 1.23x slower                                                          |
| spectral_norm             | 64.7 ms                                                                     | 80.7 ms: 1.25x slower                                                          |
| fannkuch                  | 265 ms                                                                      | 330 ms: 1.25x slower                                                           |
| go                        | 86.7 ms                                                                     | 110 ms: 1.26x slower                                                           |
| deepcopy_memo             | 19.5 us                                                                     | 24.9 us: 1.27x slower                                                          |
| Geometric mean            | (ref)                                                                       | 1.10x slower                                                                   |

Benchmark hidden because not significant (8): xml_etree_parse, create_gc_cycles, gc_traversal, python_startup, asyncio_websockets, async_tree_cpu_io_mixed_tg, json_loads, pylint

- Geometric mean (including insignificant results): 1.091x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown