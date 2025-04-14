# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-amd64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.031x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                      | 227 ms: 1.02x slower                                                              |
| docutils       | 1.72 sec                                                                    | 1.77 sec: 1.03x slower                                                            |
| sphinx         | 646 ms                                                                      | 653 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| coroutines              | 13.1 ms                                                                     | 12.9 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed | 337 ms                                                                      | 340 ms: 1.01x slower                                                              |
| async_tree_io           | 408 ms                                                                      | 414 ms: 1.01x slower                                                              |
| async_tree_none_tg      | 174 ms                                                                      | 176 ms: 1.01x slower                                                              |
| async_tree_none         | 183 ms                                                                      | 185 ms: 1.02x slower                                                              |
| async_tree_io_tg        | 403 ms                                                                      | 411 ms: 1.02x slower                                                              |
| async_generators        | 238 ms                                                                      | 251 ms: 1.05x slower                                                              |
| asyncio_websockets      | 300 ms                                                                      | 317 ms: 1.06x slower                                                              |
| Geometric mean          | (ref)                                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 59.4 ms                                                                     | 55.0 ms: 1.08x faster                                                             |
| float          | 46.0 ms                                                                     | 45.4 ms: 1.01x faster                                                             |
| pidigits       | 151 ms                                                                      | 150 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                                     | 14.2 ms: 1.03x faster                                                             |
| regex_effbot   | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                             |
| regex_compile  | 81.8 ms                                                                     | 88.6 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 88.7 ms                                                                     | 89.7 ms: 1.01x slower                                                             |
| json_loads           | 15.2 us                                                                     | 15.4 us: 1.01x slower                                                             |
| xml_etree_iterparse  | 60.2 ms                                                                     | 62.9 ms: 1.04x slower                                                             |
| xml_etree_generate   | 49.7 ms                                                                     | 52.1 ms: 1.05x slower                                                             |
| pickle_pure_python   | 208 us                                                                      | 220 us: 1.06x slower                                                              |
| xml_etree_process    | 35.8 ms                                                                     | 38.1 ms: 1.06x slower                                                             |
| tomli_loads          | 1.19 sec                                                                    | 1.33 sec: 1.12x slower                                                            |
| unpickle_pure_python | 113 us                                                                      | 138 us: 1.22x slower                                                              |
| Geometric mean       | (ref)                                                                       | 1.06x slower                                                                      |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 35.3 ms                                                                     | 34.9 ms: 1.01x faster                                                             |
| django_template | 25.3 ms                                                                     | 25.6 ms: 1.01x slower                                                             |
| mako            | 5.25 ms                                                                     | 5.89 ms: 1.12x slower                                                             |
| Geometric mean  | (ref)                                                                       | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo           | 20.2 us                                                                     | 18.5 us: 1.09x faster                                                             |
| nbody                   | 59.4 ms                                                                     | 55.0 ms: 1.08x faster                                                             |
| scimark_lu              | 60.6 ms                                                                     | 57.8 ms: 1.05x faster                                                             |
| scimark_sor             | 83.6 ms                                                                     | 80.3 ms: 1.04x faster                                                             |
| regex_v8                | 14.7 ms                                                                     | 14.2 ms: 1.03x faster                                                             |
| deepcopy_reduce         | 1.97 us                                                                     | 1.91 us: 1.03x faster                                                             |
| scimark_monte_carlo     | 43.9 ms                                                                     | 43.0 ms: 1.02x faster                                                             |
| logging_silent          | 58.0 ns                                                                     | 56.8 ns: 1.02x faster                                                             |
| logging_simple          | 6.27 us                                                                     | 6.17 us: 1.02x faster                                                             |
| float                   | 46.0 ms                                                                     | 45.4 ms: 1.01x faster                                                             |
| json                    | 3.14 ms                                                                     | 3.10 ms: 1.01x faster                                                             |
| regex_effbot            | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                             |
| coroutines              | 13.1 ms                                                                     | 12.9 ms: 1.01x faster                                                             |
| spectral_norm           | 58.4 ms                                                                     | 57.7 ms: 1.01x faster                                                             |
| genshi_xml              | 35.3 ms                                                                     | 34.9 ms: 1.01x faster                                                             |
| deepcopy                | 184 us                                                                      | 182 us: 1.01x faster                                                              |
| coverage                | 47.4 ms                                                                     | 47.0 ms: 1.01x faster                                                             |
| richards_super          | 32.7 ms                                                                     | 32.5 ms: 1.01x faster                                                             |
| pidigits                | 151 ms                                                                      | 150 ms: 1.00x faster                                                              |
| sqlite_synth            | 1.53 us                                                                     | 1.54 us: 1.01x slower                                                             |
| sqlglot_normalize       | 200 ms                                                                      | 202 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed | 337 ms                                                                      | 340 ms: 1.01x slower                                                              |
| sphinx                  | 646 ms                                                                      | 653 ms: 1.01x slower                                                              |
| django_template         | 25.3 ms                                                                     | 25.6 ms: 1.01x slower                                                             |
| xml_etree_parse         | 88.7 ms                                                                     | 89.7 ms: 1.01x slower                                                             |
| richards                | 28.5 ms                                                                     | 28.8 ms: 1.01x slower                                                             |
| json_loads              | 15.2 us                                                                     | 15.4 us: 1.01x slower                                                             |
| async_tree_io           | 408 ms                                                                      | 414 ms: 1.01x slower                                                              |
| chaos                   | 41.4 ms                                                                     | 42.0 ms: 1.01x slower                                                             |
| async_tree_none_tg      | 174 ms                                                                      | 176 ms: 1.01x slower                                                              |
| async_tree_none         | 183 ms                                                                      | 185 ms: 1.02x slower                                                              |
| generators              | 19.8 ms                                                                     | 20.1 ms: 1.02x slower                                                             |
| pyflate                 | 273 ms                                                                      | 278 ms: 1.02x slower                                                              |
| telco                   | 4.49 ms                                                                     | 4.57 ms: 1.02x slower                                                             |
| async_tree_io_tg        | 403 ms                                                                      | 411 ms: 1.02x slower                                                              |
| 2to3                    | 223 ms                                                                      | 227 ms: 1.02x slower                                                              |
| deltablue               | 2.29 ms                                                                     | 2.34 ms: 1.02x slower                                                             |
| sympy_integrate         | 13.4 ms                                                                     | 13.7 ms: 1.02x slower                                                             |
| thrift                  | 513 us                                                                      | 525 us: 1.02x slower                                                              |
| k_core                  | 1.62 sec                                                                    | 1.66 sec: 1.02x slower                                                            |
| many_optionals          | 452 us                                                                      | 463 us: 1.03x slower                                                              |
| shortest_path           | 344 ms                                                                      | 353 ms: 1.03x slower                                                              |
| connected_components    | 311 ms                                                                      | 320 ms: 1.03x slower                                                              |
| sqlglot_optimize        | 37.0 ms                                                                     | 38.2 ms: 1.03x slower                                                             |
| docutils                | 1.72 sec                                                                    | 1.77 sec: 1.03x slower                                                            |
| subparsers              | 15.9 ms                                                                     | 16.5 ms: 1.03x slower                                                             |
| dulwich_log             | 41.5 ms                                                                     | 43.0 ms: 1.04x slower                                                             |
| go                      | 85.9 ms                                                                     | 89.5 ms: 1.04x slower                                                             |
| sympy_str               | 175 ms                                                                      | 183 ms: 1.04x slower                                                              |
| xml_etree_iterparse     | 60.2 ms                                                                     | 62.9 ms: 1.04x slower                                                             |
| sympy_sum               | 89.5 ms                                                                     | 93.6 ms: 1.05x slower                                                             |
| xml_etree_generate      | 49.7 ms                                                                     | 52.1 ms: 1.05x slower                                                             |
| sympy_expand            | 304 ms                                                                      | 320 ms: 1.05x slower                                                              |
| async_generators        | 238 ms                                                                      | 251 ms: 1.05x slower                                                              |
| asyncio_websockets      | 300 ms                                                                      | 317 ms: 1.06x slower                                                              |
| bpe_tokeniser           | 2.58 sec                                                                    | 2.73 sec: 1.06x slower                                                            |
| pickle_pure_python      | 208 us                                                                      | 220 us: 1.06x slower                                                              |
| xml_etree_process       | 35.8 ms                                                                     | 38.1 ms: 1.06x slower                                                             |
| hexiom                  | 4.38 ms                                                                     | 4.68 ms: 1.07x slower                                                             |
| sqlglot_transpile       | 1.06 ms                                                                     | 1.14 ms: 1.07x slower                                                             |
| pycparser               | 703 ms                                                                      | 760 ms: 1.08x slower                                                              |
| regex_compile           | 81.8 ms                                                                     | 88.6 ms: 1.08x slower                                                             |
| sqlglot_parse           | 838 us                                                                      | 911 us: 1.09x slower                                                              |
| crypto_pyaes            | 45.6 ms                                                                     | 49.7 ms: 1.09x slower                                                             |
| mdp                     | 1.59 sec                                                                    | 1.75 sec: 1.10x slower                                                            |
| meteor_contest          | 74.9 ms                                                                     | 82.3 ms: 1.10x slower                                                             |
| comprehensions          | 11.1 us                                                                     | 12.3 us: 1.11x slower                                                             |
| nqueens                 | 61.1 ms                                                                     | 67.8 ms: 1.11x slower                                                             |
| scimark_fft             | 147 ms                                                                      | 163 ms: 1.11x slower                                                              |
| tomli_loads             | 1.19 sec                                                                    | 1.33 sec: 1.12x slower                                                            |
| mako                    | 5.25 ms                                                                     | 5.89 ms: 1.12x slower                                                             |
| scimark_sparse_mat_mult | 2.10 ms                                                                     | 2.44 ms: 1.16x slower                                                             |
| unpickle_pure_python    | 113 us                                                                      | 138 us: 1.22x slower                                                              |
| pprint_safe_repr        | 505 ms                                                                      | 637 ms: 1.26x slower                                                              |
| fannkuch                | 228 ms                                                                      | 298 ms: 1.31x slower                                                              |
| pprint_pformat          | 987 ms                                                                      | 1.29 sec: 1.31x slower                                                            |
| Geometric mean          | (ref)                                                                       | 1.03x slower                                                                      |

Benchmark hidden because not significant (18): async_tree_memoization_tg, genshi_text, create_gc_cycles, pathlib, gc_traversal, python_startup_no_site, json_dumps, logging_format, regex_dna, python_startup, raytrace, bench_mp_pool, async_tree_cpu_io_mixed_tg, html5lib, typing_runtime_protocols, async_tree_memoization, pylint, bench_thread_pool

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown