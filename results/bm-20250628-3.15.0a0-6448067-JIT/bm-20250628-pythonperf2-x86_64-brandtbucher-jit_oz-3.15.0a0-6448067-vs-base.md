# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: linux-x86_64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| html5lib       | 66.7 ms                                                                     | 68.2 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                        |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                | 22.4 ms                                                                     | 22.3 ms: 1.00x faster                                               |
| async_tree_none_tg        | 270 ms                                                                      | 272 ms: 1.01x slower                                                |
| async_tree_memoization_tg | 328 ms                                                                      | 330 ms: 1.01x slower                                                |
| async_generators          | 443 ms                                                                      | 448 ms: 1.01x slower                                                |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                        |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 257 ms                                                                      | 258 ms: 1.00x slower                                                |
| float          | 64.7 ms                                                                     | 66.0 ms: 1.02x slower                                               |
| nbody          | 99.6 ms                                                                     | 102 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.55 ms                                                                     | 3.49 ms: 1.02x faster                                               |
| regex_dna      | 223 ms                                                                      | 220 ms: 1.01x faster                                                |
| regex_v8       | 23.1 ms                                                                     | 23.0 ms: 1.00x faster                                               |
| regex_compile  | 132 ms                                                                      | 137 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 11.3 ms                                                                     | 11.2 ms: 1.01x faster                                               |
| xml_etree_parse      | 133 ms                                                                      | 136 ms: 1.02x slower                                                |
| xml_etree_process    | 56.8 ms                                                                     | 58.0 ms: 1.02x slower                                               |
| xml_etree_generate   | 80.2 ms                                                                     | 82.9 ms: 1.03x slower                                               |
| tomli_loads          | 1.94 sec                                                                    | 2.11 sec: 1.09x slower                                              |
| unpickle_pure_python | 194 us                                                                      | 215 us: 1.11x slower                                                |
| Geometric mean       | (ref)                                                                       | 1.03x slower                                                        |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                     | 15.3 ms: 1.00x slower                                               |
| python_startup_no_site | 8.82 ms                                                                     | 8.85 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 23.4 ms                                                                     | 23.0 ms: 1.01x faster                                               |
| genshi_xml      | 54.4 ms                                                                     | 55.4 ms: 1.02x slower                                               |
| django_template | 35.6 ms                                                                     | 36.2 ms: 1.02x slower                                               |
| mako            | 10.3 ms                                                                     | 11.0 ms: 1.07x slower                                               |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot              | 3.55 ms                                                                     | 3.49 ms: 1.02x faster                                               |
| genshi_text               | 23.4 ms                                                                     | 23.0 ms: 1.01x faster                                               |
| regex_dna                 | 223 ms                                                                      | 220 ms: 1.01x faster                                                |
| scimark_lu                | 96.9 ms                                                                     | 95.7 ms: 1.01x faster                                               |
| dulwich_log               | 59.4 ms                                                                     | 58.7 ms: 1.01x faster                                               |
| chaos                     | 60.2 ms                                                                     | 59.6 ms: 1.01x faster                                               |
| sqlite_synth              | 2.83 us                                                                     | 2.81 us: 1.01x faster                                               |
| sqlglot_v2_normalize      | 116 ms                                                                      | 115 ms: 1.01x faster                                                |
| json_dumps                | 11.3 ms                                                                     | 11.2 ms: 1.01x faster                                               |
| many_optionals            | 1.06 ms                                                                     | 1.05 ms: 1.01x faster                                               |
| scimark_sor               | 103 ms                                                                      | 103 ms: 1.00x faster                                                |
| regex_v8                  | 23.1 ms                                                                     | 23.0 ms: 1.00x faster                                               |
| coroutines                | 22.4 ms                                                                     | 22.3 ms: 1.00x faster                                               |
| python_startup            | 15.3 ms                                                                     | 15.3 ms: 1.00x slower                                               |
| pidigits                  | 257 ms                                                                      | 258 ms: 1.00x slower                                                |
| sympy_str                 | 292 ms                                                                      | 292 ms: 1.00x slower                                                |
| python_startup_no_site    | 8.82 ms                                                                     | 8.85 ms: 1.00x slower                                               |
| sympy_sum                 | 152 ms                                                                      | 152 ms: 1.00x slower                                                |
| pathlib                   | 17.0 ms                                                                     | 17.0 ms: 1.00x slower                                               |
| coverage                  | 78.5 ms                                                                     | 78.9 ms: 1.01x slower                                               |
| async_tree_none_tg        | 270 ms                                                                      | 272 ms: 1.01x slower                                                |
| sympy_integrate           | 22.4 ms                                                                     | 22.5 ms: 1.01x slower                                               |
| async_tree_memoization_tg | 328 ms                                                                      | 330 ms: 1.01x slower                                                |
| gc_traversal              | 6.42 ms                                                                     | 6.47 ms: 1.01x slower                                               |
| json                      | 5.27 ms                                                                     | 5.31 ms: 1.01x slower                                               |
| thrift                    | 832 us                                                                      | 840 us: 1.01x slower                                                |
| deepcopy_memo             | 28.0 us                                                                     | 28.3 us: 1.01x slower                                               |
| pycparser                 | 1.24 sec                                                                    | 1.26 sec: 1.01x slower                                              |
| async_generators          | 443 ms                                                                      | 448 ms: 1.01x slower                                                |
| mdp                       | 1.30 sec                                                                    | 1.31 sec: 1.01x slower                                              |
| shortest_path             | 443 ms                                                                      | 449 ms: 1.01x slower                                                |
| deepcopy_reduce           | 2.95 us                                                                     | 2.99 us: 1.01x slower                                               |
| raytrace                  | 284 ms                                                                      | 288 ms: 1.01x slower                                                |
| logging_simple            | 5.96 us                                                                     | 6.05 us: 1.02x slower                                               |
| logging_format            | 6.52 us                                                                     | 6.62 us: 1.02x slower                                               |
| genshi_xml                | 54.4 ms                                                                     | 55.4 ms: 1.02x slower                                               |
| django_template           | 35.6 ms                                                                     | 36.2 ms: 1.02x slower                                               |
| sqlglot_v2_transpile      | 1.72 ms                                                                     | 1.75 ms: 1.02x slower                                               |
| go                        | 129 ms                                                                      | 131 ms: 1.02x slower                                                |
| connected_components      | 407 ms                                                                      | 415 ms: 1.02x slower                                                |
| richards                  | 35.1 ms                                                                     | 35.8 ms: 1.02x slower                                               |
| float                     | 64.7 ms                                                                     | 66.0 ms: 1.02x slower                                               |
| scimark_monte_carlo       | 63.0 ms                                                                     | 64.3 ms: 1.02x slower                                               |
| sqlglot_v2_parse          | 1.33 ms                                                                     | 1.36 ms: 1.02x slower                                               |
| deepcopy                  | 275 us                                                                      | 281 us: 1.02x slower                                                |
| xml_etree_parse           | 133 ms                                                                      | 136 ms: 1.02x slower                                                |
| xml_etree_process         | 56.8 ms                                                                     | 58.0 ms: 1.02x slower                                               |
| html5lib                  | 66.7 ms                                                                     | 68.2 ms: 1.02x slower                                               |
| k_core                    | 2.01 sec                                                                    | 2.06 sec: 1.02x slower                                              |
| nbody                     | 99.6 ms                                                                     | 102 ms: 1.02x slower                                                |
| typing_runtime_protocols  | 168 us                                                                      | 172 us: 1.02x slower                                                |
| xml_etree_generate        | 80.2 ms                                                                     | 82.9 ms: 1.03x slower                                               |
| meteor_contest            | 122 ms                                                                      | 126 ms: 1.03x slower                                                |
| regex_compile             | 132 ms                                                                      | 137 ms: 1.03x slower                                                |
| deltablue                 | 2.89 ms                                                                     | 3.01 ms: 1.04x slower                                               |
| nqueens                   | 92.7 ms                                                                     | 96.6 ms: 1.04x slower                                               |
| pyflate                   | 407 ms                                                                      | 425 ms: 1.05x slower                                                |
| telco                     | 7.79 ms                                                                     | 8.14 ms: 1.05x slower                                               |
| pprint_pformat            | 1.55 sec                                                                    | 1.64 sec: 1.05x slower                                              |
| comprehensions            | 17.4 us                                                                     | 18.4 us: 1.06x slower                                               |
| pprint_safe_repr          | 764 ms                                                                      | 808 ms: 1.06x slower                                                |
| hexiom                    | 6.12 ms                                                                     | 6.52 ms: 1.06x slower                                               |
| crypto_pyaes              | 78.1 ms                                                                     | 83.3 ms: 1.07x slower                                               |
| mako                      | 10.3 ms                                                                     | 11.0 ms: 1.07x slower                                               |
| scimark_sparse_mat_mult   | 5.01 ms                                                                     | 5.44 ms: 1.09x slower                                               |
| tomli_loads               | 1.94 sec                                                                    | 2.11 sec: 1.09x slower                                              |
| bpe_tokeniser             | 4.60 sec                                                                    | 5.02 sec: 1.09x slower                                              |
| unpickle_pure_python      | 194 us                                                                      | 215 us: 1.11x slower                                                |
| scimark_fft               | 303 ms                                                                      | 343 ms: 1.13x slower                                                |
| fannkuch                  | 372 ms                                                                      | 437 ms: 1.17x slower                                                |
| spectral_norm             | 81.1 ms                                                                     | 102 ms: 1.26x slower                                                |
| Geometric mean            | (ref)                                                                       | 1.02x slower                                                        |

Benchmark hidden because not significant (22): asyncio_websockets, richards_super, pylint, subparsers, generators, djangocms, docutils, sympy_expand, 2to3, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, sqlglot_v2_optimize, pickle_pure_python, async_tree_none, xml_etree_iterparse, json_loads, async_tree_io, sphinx, create_gc_cycles, async_tree_memoization, async_tree_io_tg, logging_silent

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x