# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.040x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 384 ms                                                                   | 401 ms: 1.04x slower                                                        |
| docutils       | 3.64 sec                                                                 | 3.74 sec: 1.03x slower                                                      |
| html5lib       | 71.8 ms                                                                  | 73.0 ms: 1.02x slower                                                       |
| sphinx         | 1.47 sec                                                                 | 1.49 sec: 1.02x slower                                                      |
| tornado_http   | 145 ms                                                                   | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators | 514 ms                                                                   | 505 ms: 1.02x faster                                                        |
| Geometric mean   | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (10): async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 96.4 ms                                                                  | 98.7 ms: 1.02x slower                                                       |
| nbody          | 115 ms                                                                   | 132 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.05x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.1 ms                                                                  | 30.9 ms: 1.04x faster                                                       |
| regex_dna      | 249 ms                                                                   | 251 ms: 1.01x slower                                                        |
| regex_compile  | 173 ms                                                                   | 183 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 190 ms                                                                   | 189 ms: 1.01x faster                                                        |
| json_dumps           | 14.1 ms                                                                  | 14.2 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 149 ms                                                                   | 151 ms: 1.02x slower                                                        |
| unpickle_pure_python | 269 us                                                                   | 275 us: 1.02x slower                                                        |
| xml_etree_generate   | 113 ms                                                                   | 117 ms: 1.04x slower                                                        |
| xml_etree_process    | 81.8 ms                                                                  | 86.3 ms: 1.06x slower                                                       |
| tomli_loads          | 2.62 sec                                                                 | 2.93 sec: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                                    | 1.03x slower                                                                |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.5 ms                                                                  | 14.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.68 ms                                                                  | 8.78 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 34.2 ms                                                                  | 35.2 ms: 1.03x slower                                                       |
| genshi_xml      | 81.8 ms                                                                  | 86.4 ms: 1.06x slower                                                       |
| mako            | 13.3 ms                                                                  | 14.2 ms: 1.07x slower                                                       |
| django_template | 50.9 ms                                                                  | 55.3 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                                    | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 59.0 ms                                                                  | 55.2 ms: 1.07x faster                                                       |
| regex_v8                | 32.1 ms                                                                  | 30.9 ms: 1.04x faster                                                       |
| gc_traversal            | 6.39 ms                                                                  | 6.16 ms: 1.04x faster                                                       |
| async_generators        | 514 ms                                                                   | 505 ms: 1.02x faster                                                        |
| xml_etree_parse         | 190 ms                                                                   | 189 ms: 1.01x faster                                                        |
| python_startup          | 14.5 ms                                                                  | 14.6 ms: 1.00x slower                                                       |
| regex_dna               | 249 ms                                                                   | 251 ms: 1.01x slower                                                        |
| json_dumps              | 14.1 ms                                                                  | 14.2 ms: 1.01x slower                                                       |
| python_startup_no_site  | 8.68 ms                                                                  | 8.78 ms: 1.01x slower                                                       |
| mdp                     | 3.51 sec                                                                 | 3.55 sec: 1.01x slower                                                      |
| logging_simple          | 7.51 us                                                                  | 7.63 us: 1.02x slower                                                       |
| create_gc_cycles        | 3.61 ms                                                                  | 3.67 ms: 1.02x slower                                                       |
| html5lib                | 71.8 ms                                                                  | 73.0 ms: 1.02x slower                                                       |
| xml_etree_iterparse     | 149 ms                                                                   | 151 ms: 1.02x slower                                                        |
| sphinx                  | 1.47 sec                                                                 | 1.49 sec: 1.02x slower                                                      |
| unpickle_pure_python    | 269 us                                                                   | 275 us: 1.02x slower                                                        |
| float                   | 96.4 ms                                                                  | 98.7 ms: 1.02x slower                                                       |
| sympy_str               | 361 ms                                                                   | 370 ms: 1.03x slower                                                        |
| docutils                | 3.64 sec                                                                 | 3.74 sec: 1.03x slower                                                      |
| genshi_text             | 34.2 ms                                                                  | 35.2 ms: 1.03x slower                                                       |
| sympy_integrate         | 29.3 ms                                                                  | 30.3 ms: 1.03x slower                                                       |
| sympy_expand            | 584 ms                                                                   | 603 ms: 1.03x slower                                                        |
| sympy_sum               | 215 ms                                                                   | 222 ms: 1.03x slower                                                        |
| deepcopy                | 378 us                                                                   | 392 us: 1.04x slower                                                        |
| xml_etree_generate      | 113 ms                                                                   | 117 ms: 1.04x slower                                                        |
| scimark_lu              | 152 ms                                                                   | 158 ms: 1.04x slower                                                        |
| pycparser               | 1.52 sec                                                                 | 1.58 sec: 1.04x slower                                                      |
| sqlalchemy_declarative  | 186 ms                                                                   | 193 ms: 1.04x slower                                                        |
| logging_silent          | 147 ns                                                                   | 153 ns: 1.04x slower                                                        |
| 2to3                    | 384 ms                                                                   | 401 ms: 1.04x slower                                                        |
| deepcopy_reduce         | 4.00 us                                                                  | 4.19 us: 1.05x slower                                                       |
| raytrace                | 352 ms                                                                   | 368 ms: 1.05x slower                                                        |
| tornado_http            | 145 ms                                                                   | 152 ms: 1.05x slower                                                        |
| sqlalchemy_imperative   | 18.2 ms                                                                  | 19.2 ms: 1.05x slower                                                       |
| xml_etree_process       | 81.8 ms                                                                  | 86.3 ms: 1.06x slower                                                       |
| genshi_xml              | 81.8 ms                                                                  | 86.4 ms: 1.06x slower                                                       |
| scimark_sor             | 157 ms                                                                   | 166 ms: 1.06x slower                                                        |
| sqlglot_normalize       | 155 ms                                                                   | 163 ms: 1.06x slower                                                        |
| bpe_tokeniser           | 5.95 sec                                                                 | 6.29 sec: 1.06x slower                                                      |
| sqlglot_optimize        | 81.4 ms                                                                  | 86.1 ms: 1.06x slower                                                       |
| scimark_fft             | 455 ms                                                                   | 481 ms: 1.06x slower                                                        |
| regex_compile           | 173 ms                                                                   | 183 ms: 1.06x slower                                                        |
| dulwich_log             | 76.7 ms                                                                  | 81.7 ms: 1.06x slower                                                       |
| meteor_contest          | 125 ms                                                                   | 133 ms: 1.07x slower                                                        |
| sqlglot_transpile       | 2.18 ms                                                                  | 2.33 ms: 1.07x slower                                                       |
| scimark_sparse_mat_mult | 7.20 ms                                                                  | 7.70 ms: 1.07x slower                                                       |
| mako                    | 13.3 ms                                                                  | 14.2 ms: 1.07x slower                                                       |
| comprehensions          | 25.4 us                                                                  | 27.3 us: 1.07x slower                                                       |
| spectral_norm           | 156 ms                                                                   | 167 ms: 1.07x slower                                                        |
| sqlglot_parse           | 1.70 ms                                                                  | 1.82 ms: 1.07x slower                                                       |
| telco                   | 9.29 ms                                                                  | 10.0 ms: 1.08x slower                                                       |
| deepcopy_memo           | 39.2 us                                                                  | 42.3 us: 1.08x slower                                                       |
| deltablue               | 4.47 ms                                                                  | 4.83 ms: 1.08x slower                                                       |
| django_template         | 50.9 ms                                                                  | 55.3 ms: 1.09x slower                                                       |
| fannkuch                | 503 ms                                                                   | 547 ms: 1.09x slower                                                        |
| nqueens                 | 126 ms                                                                   | 139 ms: 1.10x slower                                                        |
| go                      | 182 ms                                                                   | 203 ms: 1.11x slower                                                        |
| crypto_pyaes            | 88.7 ms                                                                  | 99.1 ms: 1.12x slower                                                       |
| tomli_loads             | 2.62 sec                                                                 | 2.93 sec: 1.12x slower                                                      |
| chaos                   | 85.4 ms                                                                  | 95.6 ms: 1.12x slower                                                       |
| scimark_monte_carlo     | 90.3 ms                                                                  | 101 ms: 1.12x slower                                                        |
| richards_super          | 71.7 ms                                                                  | 80.8 ms: 1.13x slower                                                       |
| hexiom                  | 10.2 ms                                                                  | 11.5 ms: 1.13x slower                                                       |
| pprint_pformat          | 2.52 sec                                                                 | 2.85 sec: 1.13x slower                                                      |
| pprint_safe_repr        | 1.21 sec                                                                 | 1.37 sec: 1.14x slower                                                      |
| nbody                   | 115 ms                                                                   | 132 ms: 1.14x slower                                                        |
| richards                | 67.7 ms                                                                  | 79.8 ms: 1.18x slower                                                       |
| pyflate                 | 612 ms                                                                   | 725 ms: 1.18x slower                                                        |
| bench_mp_pool           | 1.44 sec                                                                 | 2.46 sec: 1.70x slower                                                      |
| Geometric mean          | (ref)                                                                    | 1.05x slower                                                                |

Benchmark hidden because not significant (22): async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, pathlib, thrift, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, regex_effbot, async_tree_io, async_tree_none, pidigits, async_tree_io_tg, pylint, coverage, bench_thread_pool, async_tree_cpu_io_mixed, json, json_loads, logging_format, typing_runtime_protocols, pickle_pure_python

- Geometric mean (including insignificant results): 1.040x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x