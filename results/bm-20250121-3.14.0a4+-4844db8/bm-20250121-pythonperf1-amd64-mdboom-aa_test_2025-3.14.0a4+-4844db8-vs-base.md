# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: windows-amd64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.004x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 1.68 sec                                                                    | 1.69 sec: 1.01x slower                                              |
| html5lib       | 39.9 ms                                                                     | 40.6 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                        |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_websockets      | 312 ms                                                                      | 284 ms: 1.10x faster                                                |
| coroutines              | 14.8 ms                                                                     | 14.8 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed | 344 ms                                                                      | 348 ms: 1.01x slower                                                |
| async_tree_none         | 183 ms                                                                      | 186 ms: 1.02x slower                                                |
| async_generators        | 227 ms                                                                      | 231 ms: 1.02x slower                                                |
| Geometric mean          | (ref)                                                                       | 1.00x faster                                                        |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 146 ms: 1.00x faster                                                |
| float          | 51.2 ms                                                                     | 51.6 ms: 1.01x slower                                               |
| nbody          | 73.6 ms                                                                     | 74.5 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                                     | 14.8 ms: 1.09x faster                                               |
| regex_dna      | 116 ms                                                                      | 115 ms: 1.01x faster                                                |
| regex_compile  | 88.7 ms                                                                     | 87.9 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 240 us                                                                      | 238 us: 1.01x faster                                                |
| json_dumps           | 6.82 ms                                                                     | 6.89 ms: 1.01x slower                                               |
| unpickle_pure_python | 160 us                                                                      | 162 us: 1.01x slower                                                |
| xml_etree_generate   | 59.4 ms                                                                     | 60.3 ms: 1.02x slower                                               |
| tomli_loads          | 1.38 sec                                                                    | 1.40 sec: 1.02x slower                                              |
| xml_etree_parse      | 87.7 ms                                                                     | 89.4 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                        |

Benchmark hidden because not significant (3): xml_etree_process, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                                     | 16.5 ms: 1.02x faster                                               |
| django_template | 25.0 ms                                                                     | 25.9 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                        |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_websockets       | 312 ms                                                                      | 284 ms: 1.10x faster                                                |
| regex_v8                 | 16.1 ms                                                                     | 14.8 ms: 1.09x faster                                               |
| coverage                 | 50.3 ms                                                                     | 48.3 ms: 1.04x faster                                               |
| logging_silent           | 72.3 ns                                                                     | 69.9 ns: 1.03x faster                                               |
| subparsers               | 16.4 ms                                                                     | 16.0 ms: 1.03x faster                                               |
| genshi_text              | 16.9 ms                                                                     | 16.5 ms: 1.02x faster                                               |
| many_optionals           | 446 us                                                                      | 437 us: 1.02x faster                                                |
| scimark_sor              | 91.2 ms                                                                     | 89.6 ms: 1.02x faster                                               |
| sqlite_synth             | 1.63 us                                                                     | 1.60 us: 1.02x faster                                               |
| bpe_tokeniser            | 3.07 sec                                                                    | 3.04 sec: 1.01x faster                                              |
| crypto_pyaes             | 49.3 ms                                                                     | 48.7 ms: 1.01x faster                                               |
| json                     | 2.96 ms                                                                     | 2.93 ms: 1.01x faster                                               |
| regex_dna                | 116 ms                                                                      | 115 ms: 1.01x faster                                                |
| pickle_pure_python       | 240 us                                                                      | 238 us: 1.01x faster                                                |
| regex_compile            | 88.7 ms                                                                     | 87.9 ms: 1.01x faster                                               |
| pprint_safe_repr         | 540 ms                                                                      | 535 ms: 1.01x faster                                                |
| meteor_contest           | 76.6 ms                                                                     | 76.0 ms: 1.01x faster                                               |
| gc_traversal             | 2.00 ms                                                                     | 1.99 ms: 1.01x faster                                               |
| coroutines               | 14.8 ms                                                                     | 14.8 ms: 1.01x faster                                               |
| pidigits                 | 147 ms                                                                      | 146 ms: 1.00x faster                                                |
| pprint_pformat           | 1.10 sec                                                                    | 1.09 sec: 1.00x faster                                              |
| spectral_norm            | 63.9 ms                                                                     | 63.7 ms: 1.00x faster                                               |
| docutils                 | 1.68 sec                                                                    | 1.69 sec: 1.01x slower                                              |
| nqueens                  | 64.9 ms                                                                     | 65.2 ms: 1.01x slower                                               |
| sqlglot_optimize         | 36.1 ms                                                                     | 36.3 ms: 1.01x slower                                               |
| logging_simple           | 6.39 us                                                                     | 6.43 us: 1.01x slower                                               |
| sqlglot_parse            | 885 us                                                                      | 891 us: 1.01x slower                                                |
| float                    | 51.2 ms                                                                     | 51.6 ms: 1.01x slower                                               |
| shortest_path            | 351 ms                                                                      | 354 ms: 1.01x slower                                                |
| telco                    | 4.77 ms                                                                     | 4.81 ms: 1.01x slower                                               |
| json_dumps               | 6.82 ms                                                                     | 6.89 ms: 1.01x slower                                               |
| sympy_sum                | 90.2 ms                                                                     | 91.2 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed  | 344 ms                                                                      | 348 ms: 1.01x slower                                                |
| nbody                    | 73.6 ms                                                                     | 74.5 ms: 1.01x slower                                               |
| unpickle_pure_python     | 160 us                                                                      | 162 us: 1.01x slower                                                |
| richards_super           | 35.9 ms                                                                     | 36.3 ms: 1.01x slower                                               |
| pyflate                  | 309 ms                                                                      | 312 ms: 1.01x slower                                                |
| hexiom                   | 4.54 ms                                                                     | 4.60 ms: 1.01x slower                                               |
| xml_etree_generate       | 59.4 ms                                                                     | 60.3 ms: 1.02x slower                                               |
| fannkuch                 | 273 ms                                                                      | 277 ms: 1.02x slower                                                |
| async_tree_none          | 183 ms                                                                      | 186 ms: 1.02x slower                                                |
| sympy_str                | 178 ms                                                                      | 180 ms: 1.02x slower                                                |
| tomli_loads              | 1.38 sec                                                                    | 1.40 sec: 1.02x slower                                              |
| html5lib                 | 39.9 ms                                                                     | 40.6 ms: 1.02x slower                                               |
| async_generators         | 227 ms                                                                      | 231 ms: 1.02x slower                                                |
| xml_etree_parse          | 87.7 ms                                                                     | 89.4 ms: 1.02x slower                                               |
| comprehensions           | 12.3 us                                                                     | 12.6 us: 1.02x slower                                               |
| scimark_lu               | 68.4 ms                                                                     | 69.8 ms: 1.02x slower                                               |
| scimark_sparse_mat_mult  | 2.51 ms                                                                     | 2.56 ms: 1.02x slower                                               |
| sympy_expand             | 303 ms                                                                      | 310 ms: 1.02x slower                                                |
| raytrace                 | 209 ms                                                                      | 214 ms: 1.02x slower                                                |
| richards                 | 31.6 ms                                                                     | 32.3 ms: 1.02x slower                                               |
| deepcopy_reduce          | 1.85 us                                                                     | 1.89 us: 1.02x slower                                               |
| typing_runtime_protocols | 112 us                                                                      | 115 us: 1.03x slower                                                |
| scimark_fft              | 192 ms                                                                      | 198 ms: 1.03x slower                                                |
| deepcopy                 | 182 us                                                                      | 189 us: 1.04x slower                                                |
| django_template          | 25.0 ms                                                                     | 25.9 ms: 1.04x slower                                               |
| deepcopy_memo            | 19.6 us                                                                     | 20.3 us: 1.04x slower                                               |
| scimark_monte_carlo      | 48.0 ms                                                                     | 49.9 ms: 1.04x slower                                               |
| mdp                      | 1.46 sec                                                                    | 1.56 sec: 1.07x slower                                              |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                        |

Benchmark hidden because not significant (34): genshi_xml, thrift, xml_etree_process, go, async_tree_none_tg, json_loads, create_gc_cycles, dulwich_log, sqlglot_normalize, async_tree_io_tg, generators, sqlglot_transpile, sympy_integrate, connected_components, logging_format, chaos, deltablue, k_core, async_tree_memoization_tg, bench_mp_pool, 2to3, regex_effbot, mako, xml_etree_iterparse, pathlib, async_tree_cpu_io_mixed_tg, sphinx, pylint, python_startup, python_startup_no_site, async_tree_memoization, async_tree_io, pycparser, bench_thread_pool

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown