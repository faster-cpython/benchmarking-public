# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.003x slower
- HPT reliability: 97.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 331 ms                                                                     | 326 ms: 1.01x faster                                                                 |
| async_tree_none_tg      | 169 ms                                                                     | 170 ms: 1.01x slower                                                                 |
| coroutines              | 13.8 ms                                                                    | 14.0 ms: 1.02x slower                                                                |
| async_tree_io_tg        | 392 ms                                                                     | 398 ms: 1.02x slower                                                                 |
| Geometric mean          | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_generators, async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 44.1 ms                                                                    | 45.6 ms: 1.03x slower                                                                |
| nbody          | 63.1 ms                                                                    | 65.7 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.55 ms                                                                    | 1.51 ms: 1.03x faster                                                                |
| regex_dna      | 120 ms                                                                     | 121 ms: 1.01x slower                                                                 |
| regex_compile  | 80.4 ms                                                                    | 82.2 ms: 1.02x slower                                                                |
| regex_v8       | 14.3 ms                                                                    | 14.8 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|---------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse | 65.1 ms                                                                    | 63.7 ms: 1.02x faster                                                                |
| pickle_pure_python  | 217 us                                                                     | 215 us: 1.01x faster                                                                 |
| xml_etree_process   | 39.6 ms                                                                    | 39.4 ms: 1.01x faster                                                                |
| tomli_loads         | 1.39 sec                                                                   | 1.39 sec: 1.01x slower                                                               |
| xml_etree_parse     | 88.4 ms                                                                    | 89.1 ms: 1.01x slower                                                                |
| Geometric mean      | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (4): json_loads, unpickle_pure_python, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 25.9 ms                                                                    | 25.6 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 34.3 ms                                                                    | 34.0 ms: 1.01x faster                                                                |
| mako            | 6.60 ms                                                                    | 6.67 ms: 1.01x slower                                                                |
| django_template | 23.9 ms                                                                    | 24.4 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pyflate                  | 292 ms                                                                     | 280 ms: 1.04x faster                                                                 |
| regex_effbot             | 1.55 ms                                                                    | 1.51 ms: 1.03x faster                                                                |
| bpe_tokeniser            | 3.01 sec                                                                   | 2.93 sec: 1.03x faster                                                               |
| xml_etree_iterparse      | 65.1 ms                                                                    | 63.7 ms: 1.02x faster                                                                |
| coverage                 | 299 ms                                                                     | 293 ms: 1.02x faster                                                                 |
| chaos                    | 39.6 ms                                                                    | 39.0 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed  | 331 ms                                                                     | 326 ms: 1.01x faster                                                                 |
| pickle_pure_python       | 217 us                                                                     | 215 us: 1.01x faster                                                                 |
| typing_runtime_protocols | 104 us                                                                     | 103 us: 1.01x faster                                                                 |
| logging_simple           | 6.38 us                                                                    | 6.30 us: 1.01x faster                                                                |
| sympy_expand             | 290 ms                                                                     | 287 ms: 1.01x faster                                                                 |
| logging_format           | 6.86 us                                                                    | 6.78 us: 1.01x faster                                                                |
| python_startup           | 25.9 ms                                                                    | 25.6 ms: 1.01x faster                                                                |
| crypto_pyaes             | 47.8 ms                                                                    | 47.3 ms: 1.01x faster                                                                |
| telco                    | 4.67 ms                                                                    | 4.62 ms: 1.01x faster                                                                |
| deepcopy                 | 174 us                                                                     | 172 us: 1.01x faster                                                                 |
| shortest_path            | 368 ms                                                                     | 364 ms: 1.01x faster                                                                 |
| scimark_monte_carlo      | 41.3 ms                                                                    | 40.9 ms: 1.01x faster                                                                |
| connected_components     | 337 ms                                                                     | 334 ms: 1.01x faster                                                                 |
| xml_etree_process        | 39.6 ms                                                                    | 39.4 ms: 1.01x faster                                                                |
| genshi_xml               | 34.3 ms                                                                    | 34.0 ms: 1.01x faster                                                                |
| tomli_loads              | 1.39 sec                                                                   | 1.39 sec: 1.01x slower                                                               |
| subparsers               | 17.0 ms                                                                    | 17.1 ms: 1.01x slower                                                                |
| xml_etree_parse          | 88.4 ms                                                                    | 89.1 ms: 1.01x slower                                                                |
| async_tree_none_tg       | 169 ms                                                                     | 170 ms: 1.01x slower                                                                 |
| sqlglot_v2_optimize      | 33.9 ms                                                                    | 34.2 ms: 1.01x slower                                                                |
| pprint_pformat           | 1.12 sec                                                                   | 1.13 sec: 1.01x slower                                                               |
| nqueens                  | 62.3 ms                                                                    | 62.8 ms: 1.01x slower                                                                |
| pathlib                  | 32.0 ms                                                                    | 32.3 ms: 1.01x slower                                                                |
| pprint_safe_repr         | 548 ms                                                                     | 553 ms: 1.01x slower                                                                 |
| dulwich_log              | 41.3 ms                                                                    | 41.7 ms: 1.01x slower                                                                |
| mako                     | 6.60 ms                                                                    | 6.67 ms: 1.01x slower                                                                |
| spectral_norm            | 58.7 ms                                                                    | 59.4 ms: 1.01x slower                                                                |
| generators               | 19.3 ms                                                                    | 19.6 ms: 1.01x slower                                                                |
| regex_dna                | 120 ms                                                                     | 121 ms: 1.01x slower                                                                 |
| coroutines               | 13.8 ms                                                                    | 14.0 ms: 1.02x slower                                                                |
| async_tree_io_tg         | 392 ms                                                                     | 398 ms: 1.02x slower                                                                 |
| gc_traversal             | 2.14 ms                                                                    | 2.18 ms: 1.02x slower                                                                |
| meteor_contest           | 73.0 ms                                                                    | 74.3 ms: 1.02x slower                                                                |
| scimark_sor              | 77.8 ms                                                                    | 79.1 ms: 1.02x slower                                                                |
| hexiom                   | 4.07 ms                                                                    | 4.14 ms: 1.02x slower                                                                |
| deepcopy_reduce          | 1.84 us                                                                    | 1.88 us: 1.02x slower                                                                |
| sqlglot_v2_normalize     | 70.0 ms                                                                    | 71.5 ms: 1.02x slower                                                                |
| django_template          | 23.9 ms                                                                    | 24.4 ms: 1.02x slower                                                                |
| regex_compile            | 80.4 ms                                                                    | 82.2 ms: 1.02x slower                                                                |
| scimark_fft              | 175 ms                                                                     | 179 ms: 1.02x slower                                                                 |
| mdp                      | 807 ms                                                                     | 826 ms: 1.02x slower                                                                 |
| deepcopy_memo            | 18.5 us                                                                    | 19.0 us: 1.03x slower                                                                |
| raytrace                 | 181 ms                                                                     | 186 ms: 1.03x slower                                                                 |
| scimark_lu               | 57.6 ms                                                                    | 59.3 ms: 1.03x slower                                                                |
| comprehensions           | 10.8 us                                                                    | 11.2 us: 1.03x slower                                                                |
| float                    | 44.1 ms                                                                    | 45.6 ms: 1.03x slower                                                                |
| regex_v8                 | 14.3 ms                                                                    | 14.8 ms: 1.04x slower                                                                |
| nbody                    | 63.1 ms                                                                    | 65.7 ms: 1.04x slower                                                                |
| scimark_sparse_mat_mult  | 2.47 ms                                                                    | 2.66 ms: 1.08x slower                                                                |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (37): json, async_tree_cpu_io_mixed_tg, sympy_sum, sqlglot_v2_parse, sqlite_synth, thrift, logging_silent, html5lib, json_loads, pylint, many_optionals, k_core, fannkuch, python_startup_no_site, sqlglot_v2_transpile, async_tree_memoization, sympy_integrate, pidigits, async_generators, docutils, sympy_str, unpickle_pure_python, async_tree_memoization_tg, xml_etree_generate, deltablue, richards_super, 2to3, go, genshi_text, richards, sphinx, pycparser, create_gc_cycles, async_tree_io, asyncio_websockets, async_tree_none, json_dumps

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 97.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown