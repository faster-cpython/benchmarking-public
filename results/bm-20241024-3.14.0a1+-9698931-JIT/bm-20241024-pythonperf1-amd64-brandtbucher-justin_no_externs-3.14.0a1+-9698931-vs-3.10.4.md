# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.133x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 258 ms: 1.05x slower                                                           |
| docutils       | 1.92 sec                                                    | 1.94 sec: 1.01x slower                                                         |
| html5lib       | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                          |
| tornado_http   | 108 ms                                                      | 100 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 564 ms: 1.96x faster                                                           |
| async_tree_none         | 435 ms                                                      | 224 ms: 1.94x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 284 ms: 1.85x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 388 ms: 1.64x faster                                                           |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                                          |
| nbody          | 71.3 ms                                                     | 57.3 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                           |
| regex_compile  | 106 ms                                                      | 98.9 ms: 1.07x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                          |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.71 ms: 1.37x faster                                                          |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                           |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                         |
| xml_etree_process    | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                          |
| xml_etree_parse      | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                          |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.8 ms: 1.20x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 9.03 ms                                                     | 5.60 ms: 1.61x faster                                                          |
| genshi_text    | 19.8 ms                                                     | 20.9 ms: 1.06x slower                                                          |
| genshi_xml     | 41.0 ms                                                     | 49.5 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 123 us: 2.72x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 564 ms: 1.96x faster                                                           |
| async_tree_none          | 435 ms                                                      | 224 ms: 1.94x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 284 ms: 1.85x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.43 ms: 1.72x faster                                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 388 ms: 1.64x faster                                                           |
| deepcopy_memo            | 28.8 us                                                     | 17.6 us: 1.63x faster                                                          |
| mako                     | 9.03 ms                                                     | 5.60 ms: 1.61x faster                                                          |
| scimark_sor              | 106 ms                                                      | 71.8 ms: 1.48x faster                                                          |
| scimark_lu               | 85.8 ms                                                     | 58.4 ms: 1.47x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 56.3 ms: 1.37x faster                                                          |
| go                       | 139 ms                                                      | 102 ms: 1.37x faster                                                           |
| json_dumps               | 9.16 ms                                                     | 6.71 ms: 1.37x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 69.4 ns: 1.36x faster                                                          |
| generators               | 32.4 ms                                                     | 23.7 ms: 1.36x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                                          |
| float                    | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                                          |
| sqlglot_parse            | 1.22 ms                                                     | 940 us: 1.29x faster                                                           |
| chaos                    | 61.7 ms                                                     | 47.8 ms: 1.29x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 39.4 ms: 1.28x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.0 ms: 1.27x faster                                                          |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                          |
| nbody                    | 71.3 ms                                                     | 57.3 ms: 1.24x faster                                                          |
| raytrace                 | 273 ms                                                      | 221 ms: 1.24x faster                                                           |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                           |
| richards_super           | 52.2 ms                                                     | 42.5 ms: 1.23x faster                                                          |
| pycparser                | 930 ms                                                      | 758 ms: 1.23x faster                                                           |
| pylint                   | 350 ms                                                      | 287 ms: 1.22x faster                                                           |
| comprehensions           | 16.5 us                                                     | 13.5 us: 1.22x faster                                                          |
| deepcopy                 | 255 us                                                      | 210 us: 1.22x faster                                                           |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                           |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                         |
| sqlglot_transpile        | 1.48 ms                                                     | 1.25 ms: 1.18x faster                                                          |
| thrift                   | 617 us                                                      | 529 us: 1.17x faster                                                           |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.38 ms: 1.14x faster                                                          |
| bench_thread_pool        | 958 us                                                      | 844 us: 1.13x faster                                                           |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                          |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                         |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                         |
| richards                 | 42.4 ms                                                     | 38.6 ms: 1.10x faster                                                          |
| pprint_safe_repr         | 592 ms                                                      | 539 ms: 1.10x faster                                                           |
| xml_etree_process        | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 2.03 us: 1.08x faster                                                          |
| tornado_http             | 108 ms                                                      | 100 ms: 1.08x faster                                                           |
| regex_compile            | 106 ms                                                      | 98.9 ms: 1.07x faster                                                          |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                           |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                          |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                          |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                          |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                          |
| fannkuch                 | 256 ms                                                      | 253 ms: 1.01x faster                                                           |
| docutils                 | 1.92 sec                                                    | 1.94 sec: 1.01x slower                                                         |
| logging_simple           | 6.22 us                                                     | 6.30 us: 1.01x slower                                                          |
| sympy_str                | 194 ms                                                      | 199 ms: 1.02x slower                                                           |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                          |
| hexiom                   | 5.74 ms                                                     | 5.95 ms: 1.04x slower                                                          |
| 2to3                     | 246 ms                                                      | 258 ms: 1.05x slower                                                           |
| genshi_text              | 19.8 ms                                                     | 20.9 ms: 1.06x slower                                                          |
| pathlib                  | 75.7 ms                                                     | 80.2 ms: 1.06x slower                                                          |
| sympy_expand             | 314 ms                                                      | 337 ms: 1.07x slower                                                           |
| sympy_integrate          | 15.3 ms                                                     | 16.5 ms: 1.08x slower                                                          |
| meteor_contest           | 75.9 ms                                                     | 81.9 ms: 1.08x slower                                                          |
| nqueens                  | 66.6 ms                                                     | 72.8 ms: 1.09x slower                                                          |
| sqlglot_normalize        | 205 ms                                                      | 228 ms: 1.11x slower                                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 46.1 ms: 1.16x slower                                                          |
| async_generators         | 222 ms                                                      | 265 ms: 1.20x slower                                                           |
| python_startup           | 20.6 ms                                                     | 24.8 ms: 1.20x slower                                                          |
| genshi_xml               | 41.0 ms                                                     | 49.5 ms: 1.21x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                          |
| telco                    | 3.94 ms                                                     | 4.90 ms: 1.24x slower                                                          |
| coverage                 | 39.0 ms                                                     | 49.6 ms: 1.27x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 89.7 ms: 1.45x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.39 ms: 1.74x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                   |

Benchmark hidden because not significant (4): django_template, sympy_sum, pidigits, xml_etree_generate
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.133x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown