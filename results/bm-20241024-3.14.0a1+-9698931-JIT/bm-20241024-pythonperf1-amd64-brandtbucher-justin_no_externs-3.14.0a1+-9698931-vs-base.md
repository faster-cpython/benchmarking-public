# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 247 ms                                                                      | 258 ms: 1.05x slower                                                           |
| docutils       | 1.91 sec                                                                    | 1.94 sec: 1.02x slower                                                         |
| html5lib       | 38.9 ms                                                                     | 40.5 ms: 1.04x slower                                                          |
| sphinx         | 777 ms                                                                      | 798 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators   | 263 ms                                                                      | 265 ms: 1.01x slower                                                           |
| async_tree_none_tg | 210 ms                                                                      | 214 ms: 1.02x slower                                                           |
| async_tree_io_tg   | 631 ms                                                                      | 646 ms: 1.02x slower                                                           |
| coroutines         | 13.6 ms                                                                     | 14.1 ms: 1.04x slower                                                          |
| async_tree_none    | 216 ms                                                                      | 224 ms: 1.04x slower                                                           |
| async_tree_io      | 542 ms                                                                      | 564 ms: 1.04x slower                                                           |
| Geometric mean     | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 56.2 ms                                                                     | 57.3 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                      | 118 ms: 1.01x slower                                                           |
| regex_effbot   | 1.56 ms                                                                     | 1.58 ms: 1.02x slower                                                          |
| regex_v8       | 14.7 ms                                                                     | 15.0 ms: 1.02x slower                                                          |
| regex_compile  | 91.2 ms                                                                     | 98.9 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 96.1 ms                                                                     | 95.0 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 63.4 ms                                                                     | 63.9 ms: 1.01x slower                                                          |
| unpickle_pure_python | 144 us                                                                      | 151 us: 1.05x slower                                                           |
| json_dumps           | 6.22 ms                                                                     | 6.71 ms: 1.08x slower                                                          |
| pickle_pure_python   | 199 us                                                                      | 219 us: 1.10x slower                                                           |
| tomli_loads          | 1.28 sec                                                                    | 1.41 sec: 1.10x slower                                                         |
| xml_etree_generate   | 50.5 ms                                                                     | 55.8 ms: 1.11x slower                                                          |
| xml_etree_process    | 35.8 ms                                                                     | 40.7 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.6 ms                                                                     | 18.9 ms: 1.02x slower                                                          |
| python_startup         | 24.4 ms                                                                     | 24.8 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 28.0 ms                                                                     | 28.8 ms: 1.03x slower                                                          |
| genshi_xml      | 47.2 ms                                                                     | 49.5 ms: 1.05x slower                                                          |
| genshi_text     | 19.2 ms                                                                     | 20.9 ms: 1.09x slower                                                          |
| mako            | 4.96 ms                                                                     | 5.60 ms: 1.13x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.07x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| dulwich_log              | 40.7 ms                                                                     | 39.4 ms: 1.03x faster                                                          |
| xml_etree_parse          | 96.1 ms                                                                     | 95.0 ms: 1.01x faster                                                          |
| logging_format           | 6.74 us                                                                     | 6.68 us: 1.01x faster                                                          |
| pathlib                  | 80.9 ms                                                                     | 80.2 ms: 1.01x faster                                                          |
| async_generators         | 263 ms                                                                      | 265 ms: 1.01x slower                                                           |
| bench_mp_pool            | 89.1 ms                                                                     | 89.7 ms: 1.01x slower                                                          |
| xml_etree_iterparse      | 63.4 ms                                                                     | 63.9 ms: 1.01x slower                                                          |
| mdp                      | 1.58 sec                                                                    | 1.59 sec: 1.01x slower                                                         |
| regex_dna                | 116 ms                                                                      | 118 ms: 1.01x slower                                                           |
| docutils                 | 1.91 sec                                                                    | 1.94 sec: 1.02x slower                                                         |
| async_tree_none_tg       | 210 ms                                                                      | 214 ms: 1.02x slower                                                           |
| regex_effbot             | 1.56 ms                                                                     | 1.58 ms: 1.02x slower                                                          |
| python_startup_no_site   | 18.6 ms                                                                     | 18.9 ms: 1.02x slower                                                          |
| python_startup           | 24.4 ms                                                                     | 24.8 ms: 1.02x slower                                                          |
| logging_simple           | 6.19 us                                                                     | 6.30 us: 1.02x slower                                                          |
| nbody                    | 56.2 ms                                                                     | 57.3 ms: 1.02x slower                                                          |
| regex_v8                 | 14.7 ms                                                                     | 15.0 ms: 1.02x slower                                                          |
| generators               | 23.2 ms                                                                     | 23.7 ms: 1.02x slower                                                          |
| async_tree_io_tg         | 631 ms                                                                      | 646 ms: 1.02x slower                                                           |
| django_template          | 28.0 ms                                                                     | 28.8 ms: 1.03x slower                                                          |
| sphinx                   | 777 ms                                                                      | 798 ms: 1.03x slower                                                           |
| raytrace                 | 214 ms                                                                      | 221 ms: 1.03x slower                                                           |
| thrift                   | 513 us                                                                      | 529 us: 1.03x slower                                                           |
| sympy_sum                | 103 ms                                                                      | 107 ms: 1.04x slower                                                           |
| sympy_str                | 192 ms                                                                      | 199 ms: 1.04x slower                                                           |
| coroutines               | 13.6 ms                                                                     | 14.1 ms: 1.04x slower                                                          |
| pycparser                | 730 ms                                                                      | 758 ms: 1.04x slower                                                           |
| async_tree_none          | 216 ms                                                                      | 224 ms: 1.04x slower                                                           |
| html5lib                 | 38.9 ms                                                                     | 40.5 ms: 1.04x slower                                                          |
| sqlglot_parse            | 903 us                                                                      | 940 us: 1.04x slower                                                           |
| sympy_expand             | 324 ms                                                                      | 337 ms: 1.04x slower                                                           |
| async_tree_io            | 542 ms                                                                      | 564 ms: 1.04x slower                                                           |
| json                     | 2.94 ms                                                                     | 3.06 ms: 1.04x slower                                                          |
| spectral_norm            | 54.0 ms                                                                     | 56.3 ms: 1.04x slower                                                          |
| 2to3                     | 247 ms                                                                      | 258 ms: 1.05x slower                                                           |
| unpickle_pure_python     | 144 us                                                                      | 151 us: 1.05x slower                                                           |
| genshi_xml               | 47.2 ms                                                                     | 49.5 ms: 1.05x slower                                                          |
| telco                    | 4.67 ms                                                                     | 4.90 ms: 1.05x slower                                                          |
| deltablue                | 2.32 ms                                                                     | 2.43 ms: 1.05x slower                                                          |
| sqlglot_transpile        | 1.18 ms                                                                     | 1.25 ms: 1.06x slower                                                          |
| sympy_integrate          | 15.5 ms                                                                     | 16.5 ms: 1.06x slower                                                          |
| coverage                 | 46.6 ms                                                                     | 49.6 ms: 1.06x slower                                                          |
| sqlglot_optimize         | 43.3 ms                                                                     | 46.1 ms: 1.06x slower                                                          |
| deepcopy_memo            | 16.5 us                                                                     | 17.6 us: 1.07x slower                                                          |
| json_dumps               | 6.22 ms                                                                     | 6.71 ms: 1.08x slower                                                          |
| fannkuch                 | 234 ms                                                                      | 253 ms: 1.08x slower                                                           |
| regex_compile            | 91.2 ms                                                                     | 98.9 ms: 1.08x slower                                                          |
| deepcopy_reduce          | 1.88 us                                                                     | 2.03 us: 1.08x slower                                                          |
| deepcopy                 | 193 us                                                                      | 210 us: 1.09x slower                                                           |
| typing_runtime_protocols | 114 us                                                                      | 123 us: 1.09x slower                                                           |
| genshi_text              | 19.2 ms                                                                     | 20.9 ms: 1.09x slower                                                          |
| sqlglot_normalize        | 208 ms                                                                      | 228 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult  | 2.17 ms                                                                     | 2.38 ms: 1.10x slower                                                          |
| meteor_contest           | 74.5 ms                                                                     | 81.9 ms: 1.10x slower                                                          |
| pickle_pure_python       | 199 us                                                                      | 219 us: 1.10x slower                                                           |
| tomli_loads              | 1.28 sec                                                                    | 1.41 sec: 1.10x slower                                                         |
| scimark_lu               | 52.8 ms                                                                     | 58.4 ms: 1.11x slower                                                          |
| xml_etree_generate       | 50.5 ms                                                                     | 55.8 ms: 1.11x slower                                                          |
| richards_super           | 38.4 ms                                                                     | 42.5 ms: 1.11x slower                                                          |
| scimark_fft              | 156 ms                                                                      | 175 ms: 1.12x slower                                                           |
| mako                     | 4.96 ms                                                                     | 5.60 ms: 1.13x slower                                                          |
| go                       | 90.0 ms                                                                     | 102 ms: 1.13x slower                                                           |
| pyflate                  | 285 ms                                                                      | 324 ms: 1.14x slower                                                           |
| xml_etree_process        | 35.8 ms                                                                     | 40.7 ms: 1.14x slower                                                          |
| scimark_sor              | 62.9 ms                                                                     | 71.8 ms: 1.14x slower                                                          |
| nqueens                  | 63.7 ms                                                                     | 72.8 ms: 1.14x slower                                                          |
| richards                 | 33.7 ms                                                                     | 38.6 ms: 1.14x slower                                                          |
| comprehensions           | 11.8 us                                                                     | 13.5 us: 1.15x slower                                                          |
| hexiom                   | 5.15 ms                                                                     | 5.95 ms: 1.16x slower                                                          |
| chaos                    | 41.2 ms                                                                     | 47.8 ms: 1.16x slower                                                          |
| crypto_pyaes             | 40.7 ms                                                                     | 47.2 ms: 1.16x slower                                                          |
| pprint_pformat           | 928 ms                                                                      | 1.10 sec: 1.19x slower                                                         |
| pprint_safe_repr         | 450 ms                                                                      | 539 ms: 1.20x slower                                                           |
| scimark_monte_carlo      | 37.3 ms                                                                     | 45.0 ms: 1.21x slower                                                          |
| logging_silent           | 52.3 ns                                                                     | 69.4 ns: 1.33x slower                                                          |
| Geometric mean           | (ref)                                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (12): create_gc_cycles, float, gc_traversal, async_tree_cpu_io_mixed, pidigits, json_loads, tornado_http, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, bench_thread_pool, pylint, async_tree_memoization

- Geometric mean (including insignificant results): 1.054x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown