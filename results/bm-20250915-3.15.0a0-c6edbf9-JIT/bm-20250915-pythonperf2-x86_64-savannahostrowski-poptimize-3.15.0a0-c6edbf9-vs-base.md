# Results vs. base

- fork: savannahostrowski
- ref: poptimize
- machine: linux-x86_64
- commit hash: c6edbf9
- commit date: 2025-09-15
- overall geometric mean: 1.003x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                      | 286 ms: 1.01x slower                                                        |
| docutils       | 2.90 sec                                                                    | 2.91 sec: 1.01x slower                                                      |
| html5lib       | 65.9 ms                                                                     | 66.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 22.5 ms                                                                     | 22.6 ms: 1.00x slower                                                       |
| async_generators | 392 ms                                                                      | 445 ms: 1.13x slower                                                        |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                      | 96.6 ms: 1.04x faster                                                       |
| pidigits       | 254 ms                                                                      | 255 ms: 1.00x slower                                                        |
| float          | 66.7 ms                                                                     | 67.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.76 ms                                                                     | 3.64 ms: 1.04x faster                                                       |
| regex_dna      | 231 ms                                                                      | 226 ms: 1.03x faster                                                        |
| regex_compile  | 131 ms                                                                      | 132 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|---------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse | 98.3 ms                                                                     | 97.4 ms: 1.01x faster                                                       |
| tomli_loads         | 1.88 sec                                                                    | 1.89 sec: 1.01x slower                                                      |
| xml_etree_generate  | 79.0 ms                                                                     | 79.7 ms: 1.01x slower                                                       |
| xml_etree_process   | 55.0 ms                                                                     | 56.0 ms: 1.02x slower                                                       |
| json_dumps          | 9.87 ms                                                                     | 10.1 ms: 1.02x slower                                                       |
| Geometric mean      | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                                     | 15.3 ms: 1.00x faster                                                       |
| python_startup_no_site | 8.87 ms                                                                     | 8.85 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 54.2 ms                                                                     | 53.7 ms: 1.01x faster                                                       |
| mako           | 9.65 ms                                                                     | 9.62 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 5.12 ms                                                                     | 4.87 ms: 1.05x faster                                                       |
| pyflate                  | 414 ms                                                                      | 397 ms: 1.04x faster                                                        |
| nbody                    | 101 ms                                                                      | 96.6 ms: 1.04x faster                                                       |
| regex_effbot             | 3.76 ms                                                                     | 3.64 ms: 1.04x faster                                                       |
| regex_dna                | 231 ms                                                                      | 226 ms: 1.03x faster                                                        |
| hexiom                   | 6.04 ms                                                                     | 5.90 ms: 1.03x faster                                                       |
| generators               | 29.9 ms                                                                     | 29.5 ms: 1.01x faster                                                       |
| json                     | 5.52 ms                                                                     | 5.45 ms: 1.01x faster                                                       |
| bpe_tokeniser            | 4.63 sec                                                                    | 4.58 sec: 1.01x faster                                                      |
| scimark_fft              | 301 ms                                                                      | 298 ms: 1.01x faster                                                        |
| subparsers               | 43.5 ms                                                                     | 43.1 ms: 1.01x faster                                                       |
| logging_silent           | 92.7 ns                                                                     | 91.9 ns: 1.01x faster                                                       |
| xml_etree_iterparse      | 98.3 ms                                                                     | 97.4 ms: 1.01x faster                                                       |
| genshi_xml               | 54.2 ms                                                                     | 53.7 ms: 1.01x faster                                                       |
| comprehensions           | 17.6 us                                                                     | 17.4 us: 1.01x faster                                                       |
| pathlib                  | 15.9 ms                                                                     | 15.8 ms: 1.01x faster                                                       |
| python_startup           | 15.4 ms                                                                     | 15.3 ms: 1.00x faster                                                       |
| sqlite_synth             | 2.81 us                                                                     | 2.80 us: 1.00x faster                                                       |
| mako                     | 9.65 ms                                                                     | 9.62 ms: 1.00x faster                                                       |
| python_startup_no_site   | 8.87 ms                                                                     | 8.85 ms: 1.00x faster                                                       |
| shortest_path            | 445 ms                                                                      | 445 ms: 1.00x slower                                                        |
| connected_components     | 410 ms                                                                      | 411 ms: 1.00x slower                                                        |
| pidigits                 | 254 ms                                                                      | 255 ms: 1.00x slower                                                        |
| deepcopy                 | 261 us                                                                      | 262 us: 1.00x slower                                                        |
| richards_super           | 50.3 ms                                                                     | 50.5 ms: 1.00x slower                                                       |
| coroutines               | 22.5 ms                                                                     | 22.6 ms: 1.00x slower                                                       |
| sympy_integrate          | 22.3 ms                                                                     | 22.4 ms: 1.01x slower                                                       |
| 2to3                     | 285 ms                                                                      | 286 ms: 1.01x slower                                                        |
| logging_simple           | 5.83 us                                                                     | 5.86 us: 1.01x slower                                                       |
| docutils                 | 2.90 sec                                                                    | 2.91 sec: 1.01x slower                                                      |
| sympy_expand             | 495 ms                                                                      | 498 ms: 1.01x slower                                                        |
| sympy_str                | 289 ms                                                                      | 291 ms: 1.01x slower                                                        |
| scimark_lu               | 93.6 ms                                                                     | 94.1 ms: 1.01x slower                                                       |
| logging_format           | 6.41 us                                                                     | 6.44 us: 1.01x slower                                                       |
| tomli_loads              | 1.88 sec                                                                    | 1.89 sec: 1.01x slower                                                      |
| sqlglot_v2_optimize      | 57.7 ms                                                                     | 58.1 ms: 1.01x slower                                                       |
| deltablue                | 3.16 ms                                                                     | 3.18 ms: 1.01x slower                                                       |
| deepcopy_reduce          | 2.91 us                                                                     | 2.94 us: 1.01x slower                                                       |
| html5lib                 | 65.9 ms                                                                     | 66.4 ms: 1.01x slower                                                       |
| sqlglot_v2_transpile     | 1.68 ms                                                                     | 1.69 ms: 1.01x slower                                                       |
| meteor_contest           | 122 ms                                                                      | 123 ms: 1.01x slower                                                        |
| xml_etree_generate       | 79.0 ms                                                                     | 79.7 ms: 1.01x slower                                                       |
| mdp                      | 1.28 sec                                                                    | 1.29 sec: 1.01x slower                                                      |
| regex_compile            | 131 ms                                                                      | 132 ms: 1.01x slower                                                        |
| sqlglot_v2_parse         | 1.29 ms                                                                     | 1.30 ms: 1.01x slower                                                       |
| pprint_safe_repr         | 727 ms                                                                      | 734 ms: 1.01x slower                                                        |
| go                       | 118 ms                                                                      | 120 ms: 1.01x slower                                                        |
| pprint_pformat           | 1.48 sec                                                                    | 1.49 sec: 1.01x slower                                                      |
| spectral_norm            | 78.7 ms                                                                     | 79.6 ms: 1.01x slower                                                       |
| thrift                   | 844 us                                                                      | 854 us: 1.01x slower                                                        |
| sqlglot_v2_normalize     | 114 ms                                                                      | 115 ms: 1.01x slower                                                        |
| chaos                    | 58.4 ms                                                                     | 59.2 ms: 1.01x slower                                                       |
| typing_runtime_protocols | 168 us                                                                      | 171 us: 1.01x slower                                                        |
| float                    | 66.7 ms                                                                     | 67.7 ms: 1.02x slower                                                       |
| xml_etree_process        | 55.0 ms                                                                     | 56.0 ms: 1.02x slower                                                       |
| scimark_monte_carlo      | 61.0 ms                                                                     | 62.2 ms: 1.02x slower                                                       |
| telco                    | 156 ms                                                                      | 160 ms: 1.02x slower                                                        |
| json_dumps               | 9.87 ms                                                                     | 10.1 ms: 1.02x slower                                                       |
| raytrace                 | 272 ms                                                                      | 278 ms: 1.02x slower                                                        |
| nqueens                  | 91.0 ms                                                                     | 93.3 ms: 1.03x slower                                                       |
| pycparser                | 1.19 sec                                                                    | 1.23 sec: 1.03x slower                                                      |
| coverage                 | 79.8 ms                                                                     | 82.6 ms: 1.03x slower                                                       |
| deepcopy_memo            | 25.1 us                                                                     | 26.1 us: 1.04x slower                                                       |
| fannkuch                 | 366 ms                                                                      | 380 ms: 1.04x slower                                                        |
| async_generators         | 392 ms                                                                      | 445 ms: 1.13x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (28): async_tree_none_tg, async_tree_memoization, k_core, async_tree_cpu_io_mixed_tg, scimark_sor, crypto_pyaes, many_optionals, async_tree_memoization_tg, async_tree_cpu_io_mixed, xml_etree_parse, djangocms, django_template, dulwich_log, pickle_pure_python, sphinx, gc_traversal, richards, create_gc_cycles, sympy_sum, async_tree_none, regex_v8, json_loads, async_tree_io, genshi_text, pylint, unpickle_pure_python, asyncio_websockets, async_tree_io_tg

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x