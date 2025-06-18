# Results vs. base

- fork: faster-cpython
- ref: specialize_for_compa
- machine: windows-amd64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.010x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 222 ms                                                                     | 221 ms: 1.01x faster                                                                 |
| html5lib       | 39.0 ms                                                                    | 38.4 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|--------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none    | 174 ms                                                                     | 171 ms: 1.02x faster                                                                 |
| async_generators   | 231 ms                                                                     | 233 ms: 1.01x slower                                                                 |
| coroutines         | 14.1 ms                                                                    | 14.3 ms: 1.01x slower                                                                |
| asyncio_websockets | 157 ms                                                                     | 161 ms: 1.02x slower                                                                 |
| Geometric mean     | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 61.8 ms                                                                    | 64.7 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.61 ms                                                                    | 1.54 ms: 1.04x faster                                                                |
| regex_dna      | 122 ms                                                                     | 120 ms: 1.02x faster                                                                 |
| regex_compile  | 78.9 ms                                                                    | 80.8 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_process    | 39.3 ms                                                                    | 39.6 ms: 1.01x slower                                                                |
| unpickle_pure_python | 133 us                                                                     | 134 us: 1.01x slower                                                                 |
| xml_etree_generate   | 56.2 ms                                                                    | 56.6 ms: 1.01x slower                                                                |
| xml_etree_parse      | 88.5 ms                                                                    | 89.2 ms: 1.01x slower                                                                |
| pickle_pure_python   | 207 us                                                                     | 213 us: 1.03x slower                                                                 |
| tomli_loads          | 1.37 sec                                                                   | 1.43 sec: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): json_dumps, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.73 ms                                                                    | 6.59 ms: 1.02x faster                                                                |
| django_template | 24.1 ms                                                                    | 24.0 ms: 1.01x faster                                                                |
| genshi_text     | 15.4 ms                                                                    | 15.3 ms: 1.01x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| shortest_path            | 381 ms                                                                     | 365 ms: 1.05x faster                                                                 |
| regex_effbot             | 1.61 ms                                                                    | 1.54 ms: 1.04x faster                                                                |
| logging_silent           | 342 ns                                                                     | 329 ns: 1.04x faster                                                                 |
| gc_traversal             | 2.17 ms                                                                    | 2.12 ms: 1.02x faster                                                                |
| deepcopy_reduce          | 1.86 us                                                                    | 1.82 us: 1.02x faster                                                                |
| mako                     | 6.73 ms                                                                    | 6.59 ms: 1.02x faster                                                                |
| generators               | 19.8 ms                                                                    | 19.5 ms: 1.02x faster                                                                |
| async_tree_none          | 174 ms                                                                     | 171 ms: 1.02x faster                                                                 |
| html5lib                 | 39.0 ms                                                                    | 38.4 ms: 1.02x faster                                                                |
| regex_dna                | 122 ms                                                                     | 120 ms: 1.02x faster                                                                 |
| thrift                   | 500 us                                                                     | 492 us: 1.02x faster                                                                 |
| pathlib                  | 32.1 ms                                                                    | 31.7 ms: 1.01x faster                                                                |
| scimark_sparse_mat_mult  | 2.52 ms                                                                    | 2.49 ms: 1.01x faster                                                                |
| create_gc_cycles         | 1.34 ms                                                                    | 1.32 ms: 1.01x faster                                                                |
| dulwich_log              | 41.3 ms                                                                    | 40.9 ms: 1.01x faster                                                                |
| deepcopy                 | 170 us                                                                     | 168 us: 1.01x faster                                                                 |
| django_template          | 24.1 ms                                                                    | 24.0 ms: 1.01x faster                                                                |
| genshi_text              | 15.4 ms                                                                    | 15.3 ms: 1.01x faster                                                                |
| sqlite_synth             | 1.59 us                                                                    | 1.58 us: 1.01x faster                                                                |
| 2to3                     | 222 ms                                                                     | 221 ms: 1.01x faster                                                                 |
| crypto_pyaes             | 47.1 ms                                                                    | 47.3 ms: 1.00x slower                                                                |
| xml_etree_process        | 39.3 ms                                                                    | 39.6 ms: 1.01x slower                                                                |
| unpickle_pure_python     | 133 us                                                                     | 134 us: 1.01x slower                                                                 |
| xml_etree_generate       | 56.2 ms                                                                    | 56.6 ms: 1.01x slower                                                                |
| pprint_safe_repr         | 537 ms                                                                     | 541 ms: 1.01x slower                                                                 |
| xml_etree_parse          | 88.5 ms                                                                    | 89.2 ms: 1.01x slower                                                                |
| bpe_tokeniser            | 2.97 sec                                                                   | 2.99 sec: 1.01x slower                                                               |
| async_generators         | 231 ms                                                                     | 233 ms: 1.01x slower                                                                 |
| comprehensions           | 10.8 us                                                                    | 10.9 us: 1.01x slower                                                                |
| sympy_integrate          | 12.4 ms                                                                    | 12.5 ms: 1.01x slower                                                                |
| coroutines               | 14.1 ms                                                                    | 14.3 ms: 1.01x slower                                                                |
| nqueens                  | 60.9 ms                                                                    | 61.7 ms: 1.01x slower                                                                |
| sympy_str                | 168 ms                                                                     | 170 ms: 1.01x slower                                                                 |
| pprint_pformat           | 1.09 sec                                                                   | 1.11 sec: 1.02x slower                                                               |
| telco                    | 4.55 ms                                                                    | 4.63 ms: 1.02x slower                                                                |
| mdp                      | 800 ms                                                                     | 813 ms: 1.02x slower                                                                 |
| sqlglot_v2_parse         | 822 us                                                                     | 837 us: 1.02x slower                                                                 |
| sympy_expand             | 286 ms                                                                     | 292 ms: 1.02x slower                                                                 |
| pyflate                  | 289 ms                                                                     | 295 ms: 1.02x slower                                                                 |
| sqlglot_v2_transpile     | 1.02 ms                                                                    | 1.04 ms: 1.02x slower                                                                |
| typing_runtime_protocols | 101 us                                                                     | 103 us: 1.02x slower                                                                 |
| regex_compile            | 78.9 ms                                                                    | 80.8 ms: 1.02x slower                                                                |
| asyncio_websockets       | 157 ms                                                                     | 161 ms: 1.02x slower                                                                 |
| deepcopy_memo            | 17.6 us                                                                    | 18.1 us: 1.03x slower                                                                |
| deltablue                | 2.17 ms                                                                    | 2.23 ms: 1.03x slower                                                                |
| raytrace                 | 177 ms                                                                     | 182 ms: 1.03x slower                                                                 |
| scimark_lu               | 58.0 ms                                                                    | 59.6 ms: 1.03x slower                                                                |
| pickle_pure_python       | 207 us                                                                     | 213 us: 1.03x slower                                                                 |
| go                       | 74.9 ms                                                                    | 77.4 ms: 1.03x slower                                                                |
| richards                 | 26.8 ms                                                                    | 27.7 ms: 1.03x slower                                                                |
| spectral_norm            | 62.1 ms                                                                    | 64.3 ms: 1.04x slower                                                                |
| richards_super           | 30.5 ms                                                                    | 31.6 ms: 1.04x slower                                                                |
| chaos                    | 39.9 ms                                                                    | 41.6 ms: 1.04x slower                                                                |
| hexiom                   | 4.02 ms                                                                    | 4.19 ms: 1.04x slower                                                                |
| logging_format           | 6.77 us                                                                    | 7.06 us: 1.04x slower                                                                |
| json                     | 2.97 ms                                                                    | 3.10 ms: 1.04x slower                                                                |
| tomli_loads              | 1.37 sec                                                                   | 1.43 sec: 1.04x slower                                                               |
| logging_simple           | 6.28 us                                                                    | 6.56 us: 1.04x slower                                                                |
| scimark_sor              | 75.0 ms                                                                    | 78.4 ms: 1.04x slower                                                                |
| nbody                    | 61.8 ms                                                                    | 64.7 ms: 1.05x slower                                                                |
| fannkuch                 | 257 ms                                                                     | 269 ms: 1.05x slower                                                                 |
| coverage                 | 49.0 ms                                                                    | 51.5 ms: 1.05x slower                                                                |
| scimark_monte_carlo      | 40.6 ms                                                                    | 42.8 ms: 1.05x slower                                                                |
| scimark_fft              | 172 ms                                                                     | 188 ms: 1.09x slower                                                                 |
| Geometric mean           | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (28): async_tree_io, python_startup_no_site, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, sphinx, async_tree_cpu_io_mixed, json_dumps, pidigits, genshi_xml, json_loads, many_optionals, connected_components, pylint, meteor_contest, sqlglot_v2_optimize, subparsers, python_startup, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, k_core, sqlglot_v2_normalize, docutils, sympy_sum, regex_v8, pycparser, float, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown