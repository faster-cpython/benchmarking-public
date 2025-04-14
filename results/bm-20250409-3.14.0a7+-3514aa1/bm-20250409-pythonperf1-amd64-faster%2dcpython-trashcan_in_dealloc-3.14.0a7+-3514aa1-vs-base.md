# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.009x faster
- HPT reliability: 91.70%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                                    | 1.65 sec: 1.01x slower                                                               |
| html5lib       | 38.7 ms                                                                     | 37.8 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets | 164 ms                                                                      | 159 ms: 1.04x faster                                                                 |
| async_generators   | 221 ms                                                                      | 227 ms: 1.03x slower                                                                 |
| coroutines         | 13.4 ms                                                                     | 13.9 ms: 1.04x slower                                                                |
| Geometric mean     | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 68.2 ms                                                                     | 61.3 ms: 1.11x faster                                                                |
| float          | 43.0 ms                                                                     | 42.2 ms: 1.02x faster                                                                |
| pidigits       | 149 ms                                                                      | 148 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.05x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 79.5 ms                                                                     | 78.5 ms: 1.01x faster                                                                |
| regex_dna      | 115 ms                                                                      | 116 ms: 1.01x slower                                                                 |
| regex_effbot   | 1.41 ms                                                                     | 1.45 ms: 1.03x slower                                                                |
| regex_v8       | 13.6 ms                                                                     | 14.4 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_generate | 57.0 ms                                                                     | 54.8 ms: 1.04x faster                                                                |
| xml_etree_process  | 39.6 ms                                                                     | 38.8 ms: 1.02x faster                                                                |
| pickle_pure_python | 211 us                                                                      | 208 us: 1.01x faster                                                                 |
| xml_etree_parse    | 89.0 ms                                                                     | 90.0 ms: 1.01x slower                                                                |
| tomli_loads        | 1.33 sec                                                                    | 1.36 sec: 1.02x slower                                                               |
| json_dumps         | 6.55 ms                                                                     | 6.73 ms: 1.03x slower                                                                |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 34.2 ms                                                                     | 32.7 ms: 1.05x faster                                                                |
| genshi_text     | 15.3 ms                                                                     | 14.9 ms: 1.03x faster                                                                |
| django_template | 24.0 ms                                                                     | 23.9 ms: 1.01x faster                                                                |
| Geometric mean  | (ref)                                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody                    | 68.2 ms                                                                     | 61.3 ms: 1.11x faster                                                                |
| spectral_norm            | 59.3 ms                                                                     | 53.7 ms: 1.10x faster                                                                |
| logging_silent           | 57.7 ns                                                                     | 54.2 ns: 1.07x faster                                                                |
| scimark_lu               | 60.2 ms                                                                     | 56.8 ms: 1.06x faster                                                                |
| richards                 | 28.1 ms                                                                     | 26.7 ms: 1.05x faster                                                                |
| scimark_monte_carlo      | 39.6 ms                                                                     | 37.8 ms: 1.05x faster                                                                |
| richards_super           | 32.0 ms                                                                     | 30.6 ms: 1.05x faster                                                                |
| go                       | 79.3 ms                                                                     | 75.8 ms: 1.05x faster                                                                |
| genshi_xml               | 34.2 ms                                                                     | 32.7 ms: 1.05x faster                                                                |
| xml_etree_generate       | 57.0 ms                                                                     | 54.8 ms: 1.04x faster                                                                |
| generators               | 19.7 ms                                                                     | 19.0 ms: 1.04x faster                                                                |
| asyncio_websockets       | 164 ms                                                                      | 159 ms: 1.04x faster                                                                 |
| sympy_expand             | 298 ms                                                                      | 289 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult  | 2.48 ms                                                                     | 2.41 ms: 1.03x faster                                                                |
| dulwich_log              | 41.7 ms                                                                     | 40.5 ms: 1.03x faster                                                                |
| deepcopy_reduce          | 1.82 us                                                                     | 1.77 us: 1.03x faster                                                                |
| scimark_sor              | 74.7 ms                                                                     | 72.7 ms: 1.03x faster                                                                |
| genshi_text              | 15.3 ms                                                                     | 14.9 ms: 1.03x faster                                                                |
| sympy_str                | 173 ms                                                                      | 169 ms: 1.02x faster                                                                 |
| sqlglot_v2_normalize     | 71.3 ms                                                                     | 69.7 ms: 1.02x faster                                                                |
| html5lib                 | 38.7 ms                                                                     | 37.8 ms: 1.02x faster                                                                |
| sqlglot_v2_parse         | 811 us                                                                      | 794 us: 1.02x faster                                                                 |
| xml_etree_process        | 39.6 ms                                                                     | 38.8 ms: 1.02x faster                                                                |
| nqueens                  | 60.5 ms                                                                     | 59.3 ms: 1.02x faster                                                                |
| float                    | 43.0 ms                                                                     | 42.2 ms: 1.02x faster                                                                |
| telco                    | 4.70 ms                                                                     | 4.61 ms: 1.02x faster                                                                |
| bench_thread_pool        | 860 us                                                                      | 843 us: 1.02x faster                                                                 |
| typing_runtime_protocols | 106 us                                                                      | 104 us: 1.02x faster                                                                 |
| sympy_sum                | 88.7 ms                                                                     | 87.2 ms: 1.02x faster                                                                |
| subparsers               | 15.8 ms                                                                     | 15.6 ms: 1.02x faster                                                                |
| scimark_fft              | 172 ms                                                                      | 169 ms: 1.02x faster                                                                 |
| chaos                    | 38.1 ms                                                                     | 37.4 ms: 1.02x faster                                                                |
| logging_format           | 6.74 us                                                                     | 6.64 us: 1.02x faster                                                                |
| deepcopy                 | 171 us                                                                      | 169 us: 1.01x faster                                                                 |
| sqlglot_v2_optimize      | 34.1 ms                                                                     | 33.6 ms: 1.01x faster                                                                |
| regex_compile            | 79.5 ms                                                                     | 78.5 ms: 1.01x faster                                                                |
| pickle_pure_python       | 211 us                                                                      | 208 us: 1.01x faster                                                                 |
| sympy_integrate          | 12.5 ms                                                                     | 12.4 ms: 1.01x faster                                                                |
| hexiom                   | 3.94 ms                                                                     | 3.90 ms: 1.01x faster                                                                |
| sqlglot_v2_transpile     | 1.01 ms                                                                     | 996 us: 1.01x faster                                                                 |
| logging_simple           | 6.18 us                                                                     | 6.12 us: 1.01x faster                                                                |
| meteor_contest           | 73.1 ms                                                                     | 72.5 ms: 1.01x faster                                                                |
| pidigits                 | 149 ms                                                                      | 148 ms: 1.01x faster                                                                 |
| django_template          | 24.0 ms                                                                     | 23.9 ms: 1.01x faster                                                                |
| deepcopy_memo            | 18.1 us                                                                     | 18.2 us: 1.00x slower                                                                |
| bench_mp_pool            | 86.3 ms                                                                     | 86.8 ms: 1.01x slower                                                                |
| regex_dna                | 115 ms                                                                      | 116 ms: 1.01x slower                                                                 |
| mdp                      | 777 ms                                                                      | 782 ms: 1.01x slower                                                                 |
| crypto_pyaes             | 46.4 ms                                                                     | 46.8 ms: 1.01x slower                                                                |
| raytrace                 | 171 ms                                                                      | 173 ms: 1.01x slower                                                                 |
| docutils                 | 1.63 sec                                                                    | 1.65 sec: 1.01x slower                                                               |
| xml_etree_parse          | 89.0 ms                                                                     | 90.0 ms: 1.01x slower                                                                |
| fannkuch                 | 248 ms                                                                      | 254 ms: 1.02x slower                                                                 |
| bpe_tokeniser            | 2.82 sec                                                                    | 2.88 sec: 1.02x slower                                                               |
| tomli_loads              | 1.33 sec                                                                    | 1.36 sec: 1.02x slower                                                               |
| async_generators         | 221 ms                                                                      | 227 ms: 1.03x slower                                                                 |
| json_dumps               | 6.55 ms                                                                     | 6.73 ms: 1.03x slower                                                                |
| coverage                 | 49.8 ms                                                                     | 51.3 ms: 1.03x slower                                                                |
| comprehensions           | 11.1 us                                                                     | 11.5 us: 1.03x slower                                                                |
| regex_effbot             | 1.41 ms                                                                     | 1.45 ms: 1.03x slower                                                                |
| gc_traversal             | 2.01 ms                                                                     | 2.10 ms: 1.04x slower                                                                |
| coroutines               | 13.4 ms                                                                     | 13.9 ms: 1.04x slower                                                                |
| regex_v8                 | 13.6 ms                                                                     | 14.4 ms: 1.06x slower                                                                |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (30): sphinx, pathlib, many_optionals, 2to3, mako, async_tree_none_tg, xml_etree_iterparse, python_startup, async_tree_memoization_tg, shortest_path, json_loads, pprint_pformat, python_startup_no_site, deltablue, create_gc_cycles, unpickle_pure_python, sqlite_synth, k_core, pprint_safe_repr, async_tree_cpu_io_mixed, pylint, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, pyflate, connected_components, async_tree_io_tg, async_tree_io, pycparser, json

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 91.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown