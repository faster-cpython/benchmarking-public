# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 322 ms                                                                       | 330 ms: 1.02x slower                                                               |
| docutils       | 3.22 sec                                                                     | 3.24 sec: 1.01x slower                                                             |
| sphinx         | 1.28 sec                                                                     | 1.30 sec: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coroutines       | 21.6 ms                                                                      | 21.5 ms: 1.01x faster                                                              |
| async_tree_io    | 855 ms                                                                       | 861 ms: 1.01x slower                                                               |
| async_tree_io_tg | 871 ms                                                                       | 878 ms: 1.01x slower                                                               |
| async_generators | 472 ms                                                                       | 479 ms: 1.01x slower                                                               |
| Geometric mean   | (ref)                                                                        | 1.01x slower                                                                       |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                       | 252 ms: 1.00x slower                                                               |
| nbody          | 81.9 ms                                                                      | 91.2 ms: 1.11x slower                                                              |
| Geometric mean | (ref)                                                                        | 1.04x slower                                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 149 ms                                                                       | 153 ms: 1.03x slower                                                               |
| regex_v8       | 25.9 ms                                                                      | 26.8 ms: 1.04x slower                                                              |
| regex_effbot   | 3.56 ms                                                                      | 3.70 ms: 1.04x slower                                                              |
| regex_dna      | 238 ms                                                                       | 257 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.05x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 149 ms                                                                       | 147 ms: 1.02x faster                                                               |
| xml_etree_iterparse  | 101 ms                                                                       | 102 ms: 1.00x slower                                                               |
| json_loads           | 24.3 us                                                                      | 24.5 us: 1.01x slower                                                              |
| json_dumps           | 11.5 ms                                                                      | 11.5 ms: 1.01x slower                                                              |
| unpickle_pure_python | 221 us                                                                       | 228 us: 1.03x slower                                                               |
| pickle_pure_python   | 341 us                                                                       | 351 us: 1.03x slower                                                               |
| tomli_loads          | 2.14 sec                                                                     | 2.22 sec: 1.04x slower                                                             |
| xml_etree_generate   | 81.7 ms                                                                      | 86.3 ms: 1.06x slower                                                              |
| xml_etree_process    | 57.7 ms                                                                      | 61.3 ms: 1.06x slower                                                              |
| Geometric mean       | (ref)                                                                        | 1.02x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                                      | 16.1 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 43.3 ms                                                                      | 44.0 ms: 1.02x slower                                                              |
| genshi_xml      | 66.5 ms                                                                      | 67.6 ms: 1.02x slower                                                              |
| genshi_text     | 29.5 ms                                                                      | 30.7 ms: 1.04x slower                                                              |
| mako            | 9.55 ms                                                                      | 10.2 ms: 1.07x slower                                                              |
| Geometric mean  | (ref)                                                                        | 1.03x slower                                                                       |

All benchmarks:
===============

| Benchmark               | bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coverage                | 83.1 ms                                                                      | 78.8 ms: 1.05x faster                                                              |
| xml_etree_parse         | 149 ms                                                                       | 147 ms: 1.02x faster                                                               |
| coroutines              | 21.6 ms                                                                      | 21.5 ms: 1.01x faster                                                              |
| pidigits                | 251 ms                                                                       | 252 ms: 1.00x slower                                                               |
| xml_etree_iterparse     | 101 ms                                                                       | 102 ms: 1.00x slower                                                               |
| pathlib                 | 16.2 ms                                                                      | 16.3 ms: 1.01x slower                                                              |
| json_loads              | 24.3 us                                                                      | 24.5 us: 1.01x slower                                                              |
| sqlite_synth            | 2.83 us                                                                      | 2.85 us: 1.01x slower                                                              |
| docutils                | 3.22 sec                                                                     | 3.24 sec: 1.01x slower                                                             |
| async_tree_io           | 855 ms                                                                       | 861 ms: 1.01x slower                                                               |
| mdp                     | 2.63 sec                                                                     | 2.65 sec: 1.01x slower                                                             |
| python_startup          | 16.0 ms                                                                      | 16.1 ms: 1.01x slower                                                              |
| sqlglot_parse           | 1.51 ms                                                                      | 1.53 ms: 1.01x slower                                                              |
| json_dumps              | 11.5 ms                                                                      | 11.5 ms: 1.01x slower                                                              |
| async_tree_io_tg        | 871 ms                                                                       | 878 ms: 1.01x slower                                                               |
| json                    | 5.16 ms                                                                      | 5.21 ms: 1.01x slower                                                              |
| pylint                  | 388 ms                                                                       | 392 ms: 1.01x slower                                                               |
| raytrace                | 315 ms                                                                       | 318 ms: 1.01x slower                                                               |
| sympy_expand            | 542 ms                                                                       | 548 ms: 1.01x slower                                                               |
| dulwich_log             | 66.8 ms                                                                      | 67.6 ms: 1.01x slower                                                              |
| thrift                  | 898 us                                                                       | 909 us: 1.01x slower                                                               |
| sqlalchemy_declarative  | 168 ms                                                                       | 170 ms: 1.01x slower                                                               |
| async_generators        | 472 ms                                                                       | 479 ms: 1.01x slower                                                               |
| django_template         | 43.3 ms                                                                      | 44.0 ms: 1.02x slower                                                              |
| genshi_xml              | 66.5 ms                                                                      | 67.6 ms: 1.02x slower                                                              |
| sphinx                  | 1.28 sec                                                                     | 1.30 sec: 1.02x slower                                                             |
| sqlglot_transpile       | 2.00 ms                                                                      | 2.03 ms: 1.02x slower                                                              |
| shortest_path           | 436 ms                                                                       | 444 ms: 1.02x slower                                                               |
| sympy_integrate         | 27.6 ms                                                                      | 28.1 ms: 1.02x slower                                                              |
| connected_components    | 407 ms                                                                       | 416 ms: 1.02x slower                                                               |
| sympy_str               | 324 ms                                                                       | 332 ms: 1.02x slower                                                               |
| 2to3                    | 322 ms                                                                       | 330 ms: 1.02x slower                                                               |
| telco                   | 7.68 ms                                                                      | 7.89 ms: 1.03x slower                                                              |
| regex_compile           | 149 ms                                                                       | 153 ms: 1.03x slower                                                               |
| sympy_sum               | 176 ms                                                                       | 181 ms: 1.03x slower                                                               |
| unpickle_pure_python    | 221 us                                                                       | 228 us: 1.03x slower                                                               |
| pickle_pure_python      | 341 us                                                                       | 351 us: 1.03x slower                                                               |
| bpe_tokeniser           | 4.86 sec                                                                     | 5.01 sec: 1.03x slower                                                             |
| meteor_contest          | 131 ms                                                                       | 135 ms: 1.03x slower                                                               |
| regex_v8                | 25.9 ms                                                                      | 26.8 ms: 1.04x slower                                                              |
| scimark_lu              | 97.9 ms                                                                      | 102 ms: 1.04x slower                                                               |
| regex_effbot            | 3.56 ms                                                                      | 3.70 ms: 1.04x slower                                                              |
| deepcopy_reduce         | 3.05 us                                                                      | 3.17 us: 1.04x slower                                                              |
| genshi_text             | 29.5 ms                                                                      | 30.7 ms: 1.04x slower                                                              |
| tomli_loads             | 2.14 sec                                                                     | 2.22 sec: 1.04x slower                                                             |
| deepcopy                | 312 us                                                                       | 325 us: 1.04x slower                                                               |
| chaos                   | 68.1 ms                                                                      | 70.9 ms: 1.04x slower                                                              |
| scimark_sparse_mat_mult | 4.79 ms                                                                      | 5.00 ms: 1.04x slower                                                              |
| scimark_fft             | 313 ms                                                                       | 326 ms: 1.04x slower                                                               |
| pprint_safe_repr        | 801 ms                                                                       | 837 ms: 1.04x slower                                                               |
| scimark_monte_carlo     | 70.5 ms                                                                      | 73.8 ms: 1.05x slower                                                              |
| spectral_norm           | 96.0 ms                                                                      | 101 ms: 1.05x slower                                                               |
| xml_etree_generate      | 81.7 ms                                                                      | 86.3 ms: 1.06x slower                                                              |
| pprint_pformat          | 1.63 sec                                                                     | 1.73 sec: 1.06x slower                                                             |
| xml_etree_process       | 57.7 ms                                                                      | 61.3 ms: 1.06x slower                                                              |
| crypto_pyaes            | 73.4 ms                                                                      | 78.1 ms: 1.06x slower                                                              |
| sqlglot_optimize        | 69.7 ms                                                                      | 74.3 ms: 1.07x slower                                                              |
| mako                    | 9.55 ms                                                                      | 10.2 ms: 1.07x slower                                                              |
| pyflate                 | 478 ms                                                                       | 511 ms: 1.07x slower                                                               |
| fannkuch                | 376 ms                                                                       | 403 ms: 1.07x slower                                                               |
| nqueens                 | 102 ms                                                                       | 110 ms: 1.08x slower                                                               |
| deltablue               | 3.30 ms                                                                      | 3.55 ms: 1.08x slower                                                              |
| richards_super          | 54.5 ms                                                                      | 58.6 ms: 1.08x slower                                                              |
| regex_dna               | 238 ms                                                                       | 257 ms: 1.08x slower                                                               |
| sqlglot_normalize       | 133 ms                                                                       | 144 ms: 1.08x slower                                                               |
| go                      | 153 ms                                                                       | 165 ms: 1.08x slower                                                               |
| generators              | 39.8 ms                                                                      | 43.4 ms: 1.09x slower                                                              |
| hexiom                  | 7.24 ms                                                                      | 7.96 ms: 1.10x slower                                                              |
| logging_silent          | 91.0 ns                                                                      | 100 ns: 1.10x slower                                                               |
| comprehensions          | 19.6 us                                                                      | 21.7 us: 1.11x slower                                                              |
| nbody                   | 81.9 ms                                                                      | 91.2 ms: 1.11x slower                                                              |
| scimark_sor             | 105 ms                                                                       | 117 ms: 1.12x slower                                                               |
| richards                | 45.3 ms                                                                      | 50.8 ms: 1.12x slower                                                              |
| deepcopy_memo           | 29.9 us                                                                      | 33.8 us: 1.13x slower                                                              |
| Geometric mean          | (ref)                                                                        | 1.03x slower                                                                       |

Benchmark hidden because not significant (22): logging_format, subparsers, pycparser, gc_traversal, asyncio_websockets, python_startup_no_site, create_gc_cycles, html5lib, logging_simple, many_optionals, typing_runtime_protocols, async_tree_memoization_tg, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, k_core, float, sqlalchemy_imperative, async_tree_none_tg, async_tree_memoization, bench_mp_pool

- Geometric mean (including insignificant results): 1.028x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x