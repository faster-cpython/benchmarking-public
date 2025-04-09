# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.002x slower
- HPT reliability: 79.75%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                                    | 1.63 sec: 1.00x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none_tg     | 170 ms                                                                      | 168 ms: 1.01x faster                                                                 |
| async_tree_memoization | 205 ms                                                                      | 203 ms: 1.01x faster                                                                 |
| async_generators       | 228 ms                                                                      | 226 ms: 1.01x faster                                                                 |
| coroutines             | 13.3 ms                                                                     | 13.2 ms: 1.01x faster                                                                |
| async_tree_none        | 178 ms                                                                      | 177 ms: 1.01x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 42.4 ms                                                                     | 41.9 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 14.1 ms                                                                     | 13.8 ms: 1.02x faster                                                                |
| regex_dna      | 117 ms                                                                      | 116 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                      | 131 us: 1.02x faster                                                                 |
| pickle_pure_python   | 210 us                                                                      | 207 us: 1.01x faster                                                                 |
| xml_etree_iterparse  | 63.6 ms                                                                     | 63.0 ms: 1.01x faster                                                                |
| xml_etree_generate   | 55.4 ms                                                                     | 55.8 ms: 1.01x slower                                                                |
| xml_etree_process    | 39.0 ms                                                                     | 39.3 ms: 1.01x slower                                                                |
| json_loads           | 14.9 us                                                                     | 15.2 us: 1.02x slower                                                                |
| json_dumps           | 6.45 ms                                                                     | 6.81 ms: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 25.2 ms                                                                     | 25.0 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 24.6 ms                                                                     | 24.0 ms: 1.02x faster                                                                |
| genshi_xml      | 33.9 ms                                                                     | 33.6 ms: 1.01x faster                                                                |
| genshi_text     | 15.4 ms                                                                     | 15.3 ms: 1.01x faster                                                                |
| mako            | 6.31 ms                                                                     | 6.50 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coverage                 | 51.2 ms                                                                     | 49.8 ms: 1.03x faster                                                                |
| scimark_lu               | 59.0 ms                                                                     | 57.4 ms: 1.03x faster                                                                |
| logging_format           | 6.67 us                                                                     | 6.51 us: 1.02x faster                                                                |
| regex_v8                 | 14.1 ms                                                                     | 13.8 ms: 1.02x faster                                                                |
| logging_simple           | 6.15 us                                                                     | 6.01 us: 1.02x faster                                                                |
| django_template          | 24.6 ms                                                                     | 24.0 ms: 1.02x faster                                                                |
| unpickle_pure_python     | 134 us                                                                      | 131 us: 1.02x faster                                                                 |
| sympy_expand             | 296 ms                                                                      | 291 ms: 1.02x faster                                                                 |
| richards                 | 27.1 ms                                                                     | 26.7 ms: 1.02x faster                                                                |
| logging_silent           | 55.3 ns                                                                     | 54.5 ns: 1.01x faster                                                                |
| float                    | 42.4 ms                                                                     | 41.9 ms: 1.01x faster                                                                |
| pickle_pure_python       | 210 us                                                                      | 207 us: 1.01x faster                                                                 |
| richards_super           | 30.9 ms                                                                     | 30.5 ms: 1.01x faster                                                                |
| go                       | 76.4 ms                                                                     | 75.5 ms: 1.01x faster                                                                |
| async_tree_none_tg       | 170 ms                                                                      | 168 ms: 1.01x faster                                                                 |
| xml_etree_iterparse      | 63.6 ms                                                                     | 63.0 ms: 1.01x faster                                                                |
| async_tree_memoization   | 205 ms                                                                      | 203 ms: 1.01x faster                                                                 |
| generators               | 19.0 ms                                                                     | 18.8 ms: 1.01x faster                                                                |
| async_generators         | 228 ms                                                                      | 226 ms: 1.01x faster                                                                 |
| python_startup           | 25.2 ms                                                                     | 25.0 ms: 1.01x faster                                                                |
| raytrace                 | 175 ms                                                                      | 174 ms: 1.01x faster                                                                 |
| sympy_str                | 172 ms                                                                      | 171 ms: 1.01x faster                                                                 |
| regex_dna                | 117 ms                                                                      | 116 ms: 1.01x faster                                                                 |
| genshi_xml               | 33.9 ms                                                                     | 33.6 ms: 1.01x faster                                                                |
| coroutines               | 13.3 ms                                                                     | 13.2 ms: 1.01x faster                                                                |
| genshi_text              | 15.4 ms                                                                     | 15.3 ms: 1.01x faster                                                                |
| async_tree_none          | 178 ms                                                                      | 177 ms: 1.01x faster                                                                 |
| sympy_integrate          | 12.5 ms                                                                     | 12.5 ms: 1.00x slower                                                                |
| docutils                 | 1.63 sec                                                                    | 1.63 sec: 1.00x slower                                                               |
| sqlite_synth             | 1.57 us                                                                     | 1.58 us: 1.00x slower                                                                |
| nqueens                  | 60.2 ms                                                                     | 60.6 ms: 1.01x slower                                                                |
| pprint_safe_repr         | 487 ms                                                                      | 490 ms: 1.01x slower                                                                 |
| xml_etree_generate       | 55.4 ms                                                                     | 55.8 ms: 1.01x slower                                                                |
| shortest_path            | 352 ms                                                                      | 354 ms: 1.01x slower                                                                 |
| xml_etree_process        | 39.0 ms                                                                     | 39.3 ms: 1.01x slower                                                                |
| pprint_pformat           | 997 ms                                                                      | 1.01 sec: 1.01x slower                                                               |
| create_gc_cycles         | 1.22 ms                                                                     | 1.23 ms: 1.01x slower                                                                |
| fannkuch                 | 245 ms                                                                      | 248 ms: 1.01x slower                                                                 |
| deepcopy_reduce          | 1.78 us                                                                     | 1.81 us: 1.02x slower                                                                |
| json_loads               | 14.9 us                                                                     | 15.2 us: 1.02x slower                                                                |
| typing_runtime_protocols | 104 us                                                                      | 106 us: 1.02x slower                                                                 |
| telco                    | 4.56 ms                                                                     | 4.64 ms: 1.02x slower                                                                |
| scimark_sor              | 72.2 ms                                                                     | 73.8 ms: 1.02x slower                                                                |
| bpe_tokeniser            | 2.86 sec                                                                    | 2.93 sec: 1.02x slower                                                               |
| scimark_sparse_mat_mult  | 2.49 ms                                                                     | 2.55 ms: 1.02x slower                                                                |
| json                     | 3.08 ms                                                                     | 3.16 ms: 1.02x slower                                                                |
| deepcopy                 | 167 us                                                                      | 171 us: 1.03x slower                                                                 |
| mako                     | 6.31 ms                                                                     | 6.50 ms: 1.03x slower                                                                |
| scimark_fft              | 174 ms                                                                      | 179 ms: 1.03x slower                                                                 |
| mdp                      | 772 ms                                                                      | 797 ms: 1.03x slower                                                                 |
| spectral_norm            | 56.2 ms                                                                     | 58.0 ms: 1.03x slower                                                                |
| crypto_pyaes             | 45.6 ms                                                                     | 47.6 ms: 1.04x slower                                                                |
| gc_traversal             | 2.01 ms                                                                     | 2.10 ms: 1.04x slower                                                                |
| json_dumps               | 6.45 ms                                                                     | 6.81 ms: 1.06x slower                                                                |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (39): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, dulwich_log, subparsers, comprehensions, scimark_monte_carlo, tomli_loads, xml_etree_parse, sympy_sum, sphinx, pycparser, async_tree_cpu_io_mixed_tg, many_optionals, pathlib, pidigits, deepcopy_memo, asyncio_websockets, 2to3, nbody, sqlglot_v2_normalize, connected_components, pylint, regex_compile, python_startup_no_site, chaos, bench_mp_pool, meteor_contest, html5lib, async_tree_cpu_io_mixed, deltablue, sqlglot_v2_parse, sqlglot_v2_optimize, k_core, sqlglot_v2_transpile, hexiom, pyflate, bench_thread_pool, regex_effbot

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 79.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown