# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-amd64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.002x slower
- HPT reliability: 64.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                      | 222 ms: 1.02x faster                                                          |
| docutils       | 1.80 sec                                                                    | 1.75 sec: 1.03x faster                                                        |
| html5lib       | 39.3 ms                                                                     | 39.6 ms: 1.01x slower                                                         |
| sphinx         | 694 ms                                                                      | 687 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| coroutines         | 14.0 ms                                                                     | 13.6 ms: 1.03x faster                                                         |
| async_tree_none    | 208 ms                                                                      | 214 ms: 1.03x slower                                                          |
| async_generators   | 263 ms                                                                      | 270 ms: 1.03x slower                                                          |
| asyncio_websockets | 303 ms                                                                      | 320 ms: 1.05x slower                                                          |
| Geometric mean     | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 147 ms: 1.00x faster                                                          |
| nbody          | 53.6 ms                                                                     | 56.4 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 15.9 ms                                                                     | 14.8 ms: 1.07x faster                                                         |
| regex_effbot   | 1.50 ms                                                                     | 1.42 ms: 1.06x faster                                                         |
| regex_dna      | 119 ms                                                                      | 114 ms: 1.05x faster                                                          |
| regex_compile  | 84.5 ms                                                                     | 82.2 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                                       | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                                     | 14.0 us: 1.02x faster                                                         |
| json_dumps           | 6.36 ms                                                                     | 6.27 ms: 1.02x faster                                                         |
| xml_etree_process    | 36.1 ms                                                                     | 35.7 ms: 1.01x faster                                                         |
| tomli_loads          | 1.27 sec                                                                    | 1.29 sec: 1.01x slower                                                        |
| unpickle_pure_python | 108 us                                                                      | 111 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                  |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 17.4 ms                                                                     | 17.6 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 26.0 ms                                                                     | 27.6 ms: 1.06x slower                                                         |
| genshi_text     | 18.2 ms                                                                     | 19.6 ms: 1.08x slower                                                         |
| genshi_xml      | 44.1 ms                                                                     | 48.0 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                                       | 1.06x slower                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| fannkuch                | 262 ms                                                                      | 240 ms: 1.10x faster                                                          |
| thrift                  | 595 us                                                                      | 543 us: 1.09x faster                                                          |
| regex_v8                | 15.9 ms                                                                     | 14.8 ms: 1.07x faster                                                         |
| regex_effbot            | 1.50 ms                                                                     | 1.42 ms: 1.06x faster                                                         |
| regex_dna               | 119 ms                                                                      | 114 ms: 1.05x faster                                                          |
| many_optionals          | 482 us                                                                      | 461 us: 1.04x faster                                                          |
| pylint                  | 207 ms                                                                      | 198 ms: 1.04x faster                                                          |
| coroutines              | 14.0 ms                                                                     | 13.6 ms: 1.03x faster                                                         |
| regex_compile           | 84.5 ms                                                                     | 82.2 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult | 2.14 ms                                                                     | 2.08 ms: 1.03x faster                                                         |
| docutils                | 1.80 sec                                                                    | 1.75 sec: 1.03x faster                                                        |
| sympy_sum               | 93.9 ms                                                                     | 91.5 ms: 1.03x faster                                                         |
| json_loads              | 14.3 us                                                                     | 14.0 us: 1.02x faster                                                         |
| sympy_integrate         | 13.9 ms                                                                     | 13.7 ms: 1.02x faster                                                         |
| bpe_tokeniser           | 2.74 sec                                                                    | 2.69 sec: 1.02x faster                                                        |
| go                      | 91.5 ms                                                                     | 89.7 ms: 1.02x faster                                                         |
| sqlglot_transpile       | 1.13 ms                                                                     | 1.11 ms: 1.02x faster                                                         |
| sqlglot_parse           | 878 us                                                                      | 863 us: 1.02x faster                                                          |
| spectral_norm           | 53.5 ms                                                                     | 52.6 ms: 1.02x faster                                                         |
| shortest_path           | 349 ms                                                                      | 344 ms: 1.02x faster                                                          |
| sympy_str               | 180 ms                                                                      | 178 ms: 1.02x faster                                                          |
| 2to3                    | 225 ms                                                                      | 222 ms: 1.02x faster                                                          |
| json_dumps              | 6.36 ms                                                                     | 6.27 ms: 1.02x faster                                                         |
| telco                   | 4.34 ms                                                                     | 4.28 ms: 1.01x faster                                                         |
| scimark_lu              | 53.7 ms                                                                     | 53.0 ms: 1.01x faster                                                         |
| scimark_sor             | 62.8 ms                                                                     | 62.1 ms: 1.01x faster                                                         |
| sympy_expand            | 310 ms                                                                      | 307 ms: 1.01x faster                                                          |
| sphinx                  | 694 ms                                                                      | 687 ms: 1.01x faster                                                          |
| xml_etree_process       | 36.1 ms                                                                     | 35.7 ms: 1.01x faster                                                         |
| deltablue               | 2.36 ms                                                                     | 2.34 ms: 1.01x faster                                                         |
| hexiom                  | 5.01 ms                                                                     | 4.98 ms: 1.01x faster                                                         |
| pidigits                | 147 ms                                                                      | 147 ms: 1.00x faster                                                          |
| mdp                     | 1.50 sec                                                                    | 1.50 sec: 1.01x slower                                                        |
| html5lib                | 39.3 ms                                                                     | 39.6 ms: 1.01x slower                                                         |
| sqlite_synth            | 1.56 us                                                                     | 1.58 us: 1.01x slower                                                         |
| tomli_loads             | 1.27 sec                                                                    | 1.29 sec: 1.01x slower                                                        |
| python_startup_no_site  | 17.4 ms                                                                     | 17.6 ms: 1.01x slower                                                         |
| json                    | 2.88 ms                                                                     | 2.91 ms: 1.01x slower                                                         |
| chaos                   | 40.4 ms                                                                     | 41.1 ms: 1.02x slower                                                         |
| deepcopy_reduce         | 1.84 us                                                                     | 1.87 us: 1.02x slower                                                         |
| pycparser               | 702 ms                                                                      | 717 ms: 1.02x slower                                                          |
| scimark_monte_carlo     | 36.4 ms                                                                     | 37.1 ms: 1.02x slower                                                         |
| meteor_contest          | 72.2 ms                                                                     | 73.8 ms: 1.02x slower                                                         |
| unpickle_pure_python    | 108 us                                                                      | 111 us: 1.02x slower                                                          |
| sqlglot_normalize       | 203 ms                                                                      | 208 ms: 1.02x slower                                                          |
| sqlglot_optimize        | 37.9 ms                                                                     | 38.9 ms: 1.03x slower                                                         |
| async_tree_none         | 208 ms                                                                      | 214 ms: 1.03x slower                                                          |
| async_generators        | 263 ms                                                                      | 270 ms: 1.03x slower                                                          |
| logging_simple          | 6.13 us                                                                     | 6.32 us: 1.03x slower                                                         |
| logging_format          | 6.61 us                                                                     | 6.82 us: 1.03x slower                                                         |
| raytrace                | 206 ms                                                                      | 212 ms: 1.03x slower                                                          |
| generators              | 22.6 ms                                                                     | 23.4 ms: 1.03x slower                                                         |
| deepcopy                | 187 us                                                                      | 193 us: 1.03x slower                                                          |
| pprint_pformat          | 949 ms                                                                      | 988 ms: 1.04x slower                                                          |
| deepcopy_memo           | 16.1 us                                                                     | 16.8 us: 1.04x slower                                                         |
| nbody                   | 53.6 ms                                                                     | 56.4 ms: 1.05x slower                                                         |
| asyncio_websockets      | 303 ms                                                                      | 320 ms: 1.05x slower                                                          |
| pprint_safe_repr        | 469 ms                                                                      | 497 ms: 1.06x slower                                                          |
| django_template         | 26.0 ms                                                                     | 27.6 ms: 1.06x slower                                                         |
| richards                | 33.0 ms                                                                     | 35.1 ms: 1.07x slower                                                         |
| richards_super          | 37.1 ms                                                                     | 39.7 ms: 1.07x slower                                                         |
| genshi_text             | 18.2 ms                                                                     | 19.6 ms: 1.08x slower                                                         |
| genshi_xml              | 44.1 ms                                                                     | 48.0 ms: 1.09x slower                                                         |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                                  |

Benchmark hidden because not significant (31): bench_thread_pool, k_core, async_tree_io, create_gc_cycles, xml_etree_generate, subparsers, pickle_pure_python, connected_components, typing_runtime_protocols, gc_traversal, async_tree_none_tg, scimark_fft, async_tree_cpu_io_mixed, nqueens, async_tree_io_tg, dulwich_log, python_startup, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, bench_mp_pool, pyflate, xml_etree_iterparse, pathlib, xml_etree_parse, crypto_pyaes, float, coverage, async_tree_memoization, comprehensions, mako, logging_silent

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 64.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown