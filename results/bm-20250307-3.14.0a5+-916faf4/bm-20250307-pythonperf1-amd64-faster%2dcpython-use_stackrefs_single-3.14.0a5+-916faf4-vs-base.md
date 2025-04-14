# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: windows-amd64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.011x faster
- HPT reliability: 78.31%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 1.73 sec                                                                    | 1.69 sec: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|--------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| asyncio_websockets | 325 ms                                                                      | 315 ms: 1.03x faster                                                                  |
| async_tree_none_tg | 178 ms                                                                      | 179 ms: 1.01x slower                                                                  |
| async_tree_io_tg   | 411 ms                                                                      | 416 ms: 1.01x slower                                                                  |
| async_tree_none    | 187 ms                                                                      | 190 ms: 1.01x slower                                                                  |
| async_generators   | 224 ms                                                                      | 228 ms: 1.02x slower                                                                  |
| async_tree_io      | 418 ms                                                                      | 426 ms: 1.02x slower                                                                  |
| Geometric mean     | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, coroutines, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 73.5 ms                                                                     | 66.2 ms: 1.11x faster                                                                 |
| pidigits       | 154 ms                                                                      | 152 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 1.50 ms                                                                     | 1.42 ms: 1.05x faster                                                                 |
| regex_dna      | 118 ms                                                                      | 114 ms: 1.04x faster                                                                  |
| regex_v8       | 14.9 ms                                                                     | 14.6 ms: 1.02x faster                                                                 |
| regex_compile  | 87.3 ms                                                                     | 86.2 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 154 us                                                                      | 148 us: 1.04x faster                                                                  |
| pickle_pure_python   | 234 us                                                                      | 227 us: 1.03x faster                                                                  |
| tomli_loads          | 1.45 sec                                                                    | 1.42 sec: 1.02x faster                                                                |
| xml_etree_parse      | 91.0 ms                                                                     | 91.9 ms: 1.01x slower                                                                 |
| xml_etree_process    | 41.3 ms                                                                     | 41.7 ms: 1.01x slower                                                                 |
| json_loads           | 14.8 us                                                                     | 15.1 us: 1.01x slower                                                                 |
| xml_etree_iterparse  | 64.8 ms                                                                     | 66.1 ms: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 20.0 ms                                                                     | 19.7 ms: 1.02x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.17 ms                                                                     | 7.04 ms: 1.02x faster                                                                 |
| genshi_text     | 16.5 ms                                                                     | 16.9 ms: 1.02x slower                                                                 |
| django_template | 25.6 ms                                                                     | 26.2 ms: 1.02x slower                                                                 |
| genshi_xml      | 36.0 ms                                                                     | 37.1 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| scimark_sor              | 89.9 ms                                                                     | 77.9 ms: 1.15x faster                                                                 |
| nbody                    | 73.5 ms                                                                     | 66.2 ms: 1.11x faster                                                                 |
| scimark_lu               | 67.2 ms                                                                     | 61.0 ms: 1.10x faster                                                                 |
| scimark_monte_carlo      | 47.2 ms                                                                     | 43.1 ms: 1.10x faster                                                                 |
| deepcopy_memo            | 21.0 us                                                                     | 19.4 us: 1.08x faster                                                                 |
| logging_silent           | 63.0 ns                                                                     | 58.7 ns: 1.07x faster                                                                 |
| richards_super           | 35.5 ms                                                                     | 33.1 ms: 1.07x faster                                                                 |
| scimark_fft              | 193 ms                                                                      | 180 ms: 1.07x faster                                                                  |
| richards                 | 31.3 ms                                                                     | 29.2 ms: 1.07x faster                                                                 |
| spectral_norm            | 60.0 ms                                                                     | 56.5 ms: 1.06x faster                                                                 |
| regex_effbot             | 1.50 ms                                                                     | 1.42 ms: 1.05x faster                                                                 |
| scimark_sparse_mat_mult  | 2.67 ms                                                                     | 2.55 ms: 1.05x faster                                                                 |
| regex_dna                | 118 ms                                                                      | 114 ms: 1.04x faster                                                                  |
| unpickle_pure_python     | 154 us                                                                      | 148 us: 1.04x faster                                                                  |
| fannkuch                 | 285 ms                                                                      | 274 ms: 1.04x faster                                                                  |
| deepcopy                 | 191 us                                                                      | 184 us: 1.04x faster                                                                  |
| pyflate                  | 317 ms                                                                      | 306 ms: 1.03x faster                                                                  |
| pickle_pure_python       | 234 us                                                                      | 227 us: 1.03x faster                                                                  |
| asyncio_websockets       | 325 ms                                                                      | 315 ms: 1.03x faster                                                                  |
| json                     | 3.10 ms                                                                     | 3.01 ms: 1.03x faster                                                                 |
| meteor_contest           | 77.6 ms                                                                     | 75.6 ms: 1.03x faster                                                                 |
| crypto_pyaes             | 50.6 ms                                                                     | 49.5 ms: 1.02x faster                                                                 |
| pprint_safe_repr         | 561 ms                                                                      | 548 ms: 1.02x faster                                                                  |
| tomli_loads              | 1.45 sec                                                                    | 1.42 sec: 1.02x faster                                                                |
| pprint_pformat           | 1.13 sec                                                                    | 1.11 sec: 1.02x faster                                                                |
| regex_v8                 | 14.9 ms                                                                     | 14.6 ms: 1.02x faster                                                                 |
| mako                     | 7.17 ms                                                                     | 7.04 ms: 1.02x faster                                                                 |
| docutils                 | 1.73 sec                                                                    | 1.69 sec: 1.02x faster                                                                |
| deltablue                | 2.31 ms                                                                     | 2.27 ms: 1.02x faster                                                                 |
| gc_traversal             | 2.07 ms                                                                     | 2.04 ms: 1.02x faster                                                                 |
| python_startup_no_site   | 20.0 ms                                                                     | 19.7 ms: 1.02x faster                                                                 |
| go                       | 88.9 ms                                                                     | 87.6 ms: 1.02x faster                                                                 |
| deepcopy_reduce          | 1.99 us                                                                     | 1.97 us: 1.01x faster                                                                 |
| regex_compile            | 87.3 ms                                                                     | 86.2 ms: 1.01x faster                                                                 |
| hexiom                   | 4.40 ms                                                                     | 4.36 ms: 1.01x faster                                                                 |
| sqlite_synth             | 1.60 us                                                                     | 1.58 us: 1.01x faster                                                                 |
| pidigits                 | 154 ms                                                                      | 152 ms: 1.01x faster                                                                  |
| bpe_tokeniser            | 2.99 sec                                                                    | 2.98 sec: 1.00x faster                                                                |
| sqlglot_optimize         | 35.4 ms                                                                     | 35.6 ms: 1.01x slower                                                                 |
| sympy_str                | 176 ms                                                                      | 178 ms: 1.01x slower                                                                  |
| subparsers               | 16.4 ms                                                                     | 16.6 ms: 1.01x slower                                                                 |
| async_tree_none_tg       | 178 ms                                                                      | 179 ms: 1.01x slower                                                                  |
| xml_etree_parse          | 91.0 ms                                                                     | 91.9 ms: 1.01x slower                                                                 |
| xml_etree_process        | 41.3 ms                                                                     | 41.7 ms: 1.01x slower                                                                 |
| chaos                    | 41.7 ms                                                                     | 42.2 ms: 1.01x slower                                                                 |
| telco                    | 4.90 ms                                                                     | 4.96 ms: 1.01x slower                                                                 |
| async_tree_io_tg         | 411 ms                                                                      | 416 ms: 1.01x slower                                                                  |
| sympy_sum                | 89.5 ms                                                                     | 90.7 ms: 1.01x slower                                                                 |
| async_tree_none          | 187 ms                                                                      | 190 ms: 1.01x slower                                                                  |
| json_loads               | 14.8 us                                                                     | 15.1 us: 1.01x slower                                                                 |
| async_generators         | 224 ms                                                                      | 228 ms: 1.02x slower                                                                  |
| sqlglot_transpile        | 1.10 ms                                                                     | 1.12 ms: 1.02x slower                                                                 |
| async_tree_io            | 418 ms                                                                      | 426 ms: 1.02x slower                                                                  |
| thrift                   | 512 us                                                                      | 522 us: 1.02x slower                                                                  |
| xml_etree_iterparse      | 64.8 ms                                                                     | 66.1 ms: 1.02x slower                                                                 |
| genshi_text              | 16.5 ms                                                                     | 16.9 ms: 1.02x slower                                                                 |
| typing_runtime_protocols | 109 us                                                                      | 111 us: 1.02x slower                                                                  |
| django_template          | 25.6 ms                                                                     | 26.2 ms: 1.02x slower                                                                 |
| mdp                      | 1.57 sec                                                                    | 1.61 sec: 1.02x slower                                                                |
| sympy_expand             | 297 ms                                                                      | 306 ms: 1.03x slower                                                                  |
| connected_components     | 331 ms                                                                      | 341 ms: 1.03x slower                                                                  |
| genshi_xml               | 36.0 ms                                                                     | 37.1 ms: 1.03x slower                                                                 |
| comprehensions           | 11.4 us                                                                     | 11.8 us: 1.04x slower                                                                 |
| shortest_path            | 361 ms                                                                      | 376 ms: 1.04x slower                                                                  |
| nqueens                  | 62.8 ms                                                                     | 65.5 ms: 1.04x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (29): pycparser, float, xml_etree_generate, 2to3, k_core, raytrace, logging_format, generators, sympy_integrate, logging_simple, bench_mp_pool, python_startup, async_tree_cpu_io_mixed, many_optionals, async_tree_memoization, sqlglot_normalize, dulwich_log, coverage, sqlglot_parse, pathlib, async_tree_cpu_io_mixed_tg, coroutines, async_tree_memoization_tg, json_dumps, create_gc_cycles, sphinx, html5lib, pylint, bench_thread_pool

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 78.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown