# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.65 sec                                                                   | 1.62 sec: 1.02x faster                                                               |
| html5lib       | 39.1 ms                                                                    | 38.6 ms: 1.01x faster                                                                |
| sphinx         | 644 ms                                                                     | 637 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines                 | 14.6 ms                                                                    | 13.9 ms: 1.05x faster                                                                |
| async_tree_none            | 179 ms                                                                     | 170 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 334 ms                                                                     | 330 ms: 1.01x faster                                                                 |
| async_tree_memoization_tg  | 212 ms                                                                     | 210 ms: 1.01x faster                                                                 |
| async_tree_memoization     | 210 ms                                                                     | 208 ms: 1.01x faster                                                                 |
| async_tree_io_tg           | 395 ms                                                                     | 391 ms: 1.01x faster                                                                 |
| async_generators           | 231 ms                                                                     | 229 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                     | 345 ms: 1.01x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 65.2 ms                                                                    | 61.8 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 14.0 ms                                                                    | 13.9 ms: 1.01x faster                                                                |
| regex_compile  | 80.2 ms                                                                    | 80.9 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 137 us                                                                     | 134 us: 1.03x faster                                                                 |
| tomli_loads          | 1.39 sec                                                                   | 1.36 sec: 1.03x faster                                                               |
| xml_etree_iterparse  | 65.7 ms                                                                    | 64.1 ms: 1.03x faster                                                                |
| xml_etree_generate   | 56.7 ms                                                                    | 55.8 ms: 1.02x faster                                                                |
| pickle_pure_python   | 214 us                                                                     | 212 us: 1.01x faster                                                                 |
| xml_etree_process    | 39.6 ms                                                                    | 39.3 ms: 1.01x faster                                                                |
| xml_etree_parse      | 89.3 ms                                                                    | 90.2 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 26.0 ms                                                                    | 25.7 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 24.4 ms                                                                    | 23.7 ms: 1.03x faster                                                                |
| genshi_text     | 15.4 ms                                                                    | 15.1 ms: 1.02x faster                                                                |
| genshi_xml      | 34.6 ms                                                                    | 34.1 ms: 1.02x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody                      | 65.2 ms                                                                    | 61.8 ms: 1.06x faster                                                                |
| coroutines                 | 14.6 ms                                                                    | 13.9 ms: 1.05x faster                                                                |
| async_tree_none            | 179 ms                                                                     | 170 ms: 1.05x faster                                                                 |
| pyflate                    | 289 ms                                                                     | 280 ms: 1.03x faster                                                                 |
| chaos                      | 39.9 ms                                                                    | 38.7 ms: 1.03x faster                                                                |
| sqlglot_v2_optimize        | 34.6 ms                                                                    | 33.6 ms: 1.03x faster                                                                |
| django_template            | 24.4 ms                                                                    | 23.7 ms: 1.03x faster                                                                |
| richards                   | 27.7 ms                                                                    | 26.9 ms: 1.03x faster                                                                |
| json                       | 3.07 ms                                                                    | 2.98 ms: 1.03x faster                                                                |
| logging_simple             | 6.46 us                                                                    | 6.29 us: 1.03x faster                                                                |
| unpickle_pure_python       | 137 us                                                                     | 134 us: 1.03x faster                                                                 |
| sqlglot_v2_normalize       | 71.9 ms                                                                    | 70.0 ms: 1.03x faster                                                                |
| tomli_loads                | 1.39 sec                                                                   | 1.36 sec: 1.03x faster                                                               |
| xml_etree_iterparse        | 65.7 ms                                                                    | 64.1 ms: 1.03x faster                                                                |
| coverage                   | 296 ms                                                                     | 289 ms: 1.02x faster                                                                 |
| sympy_expand               | 295 ms                                                                     | 289 ms: 1.02x faster                                                                 |
| generators                 | 19.9 ms                                                                    | 19.5 ms: 1.02x faster                                                                |
| logging_format             | 6.91 us                                                                    | 6.77 us: 1.02x faster                                                                |
| richards_super             | 31.5 ms                                                                    | 30.8 ms: 1.02x faster                                                                |
| sqlglot_v2_transpile       | 1.04 ms                                                                    | 1.02 ms: 1.02x faster                                                                |
| genshi_text                | 15.4 ms                                                                    | 15.1 ms: 1.02x faster                                                                |
| raytrace                   | 184 ms                                                                     | 180 ms: 1.02x faster                                                                 |
| sympy_str                  | 172 ms                                                                     | 169 ms: 1.02x faster                                                                 |
| go                         | 77.5 ms                                                                    | 76.1 ms: 1.02x faster                                                                |
| hexiom                     | 4.15 ms                                                                    | 4.08 ms: 1.02x faster                                                                |
| deltablue                  | 2.26 ms                                                                    | 2.22 ms: 1.02x faster                                                                |
| sqlglot_v2_parse           | 830 us                                                                     | 816 us: 1.02x faster                                                                 |
| comprehensions             | 11.0 us                                                                    | 10.8 us: 1.02x faster                                                                |
| docutils                   | 1.65 sec                                                                   | 1.62 sec: 1.02x faster                                                               |
| xml_etree_generate         | 56.7 ms                                                                    | 55.8 ms: 1.02x faster                                                                |
| meteor_contest             | 72.7 ms                                                                    | 71.6 ms: 1.02x faster                                                                |
| genshi_xml                 | 34.6 ms                                                                    | 34.1 ms: 1.02x faster                                                                |
| logging_silent             | 321 ns                                                                     | 316 ns: 1.01x faster                                                                 |
| typing_runtime_protocols   | 105 us                                                                     | 103 us: 1.01x faster                                                                 |
| scimark_sparse_mat_mult    | 2.55 ms                                                                    | 2.51 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed    | 334 ms                                                                     | 330 ms: 1.01x faster                                                                 |
| html5lib                   | 39.1 ms                                                                    | 38.6 ms: 1.01x faster                                                                |
| sympy_sum                  | 88.3 ms                                                                    | 87.2 ms: 1.01x faster                                                                |
| python_startup             | 26.0 ms                                                                    | 25.7 ms: 1.01x faster                                                                |
| bpe_tokeniser              | 2.98 sec                                                                   | 2.95 sec: 1.01x faster                                                               |
| regex_v8                   | 14.0 ms                                                                    | 13.9 ms: 1.01x faster                                                                |
| async_tree_memoization_tg  | 212 ms                                                                     | 210 ms: 1.01x faster                                                                 |
| sqlite_synth               | 1.59 us                                                                    | 1.58 us: 1.01x faster                                                                |
| async_tree_memoization     | 210 ms                                                                     | 208 ms: 1.01x faster                                                                 |
| deepcopy_memo              | 18.4 us                                                                    | 18.2 us: 1.01x faster                                                                |
| sphinx                     | 644 ms                                                                     | 637 ms: 1.01x faster                                                                 |
| scimark_lu                 | 59.5 ms                                                                    | 58.8 ms: 1.01x faster                                                                |
| pprint_pformat             | 1.12 sec                                                                   | 1.11 sec: 1.01x faster                                                               |
| pickle_pure_python         | 214 us                                                                     | 212 us: 1.01x faster                                                                 |
| async_tree_io_tg           | 395 ms                                                                     | 391 ms: 1.01x faster                                                                 |
| nqueens                    | 61.2 ms                                                                    | 60.6 ms: 1.01x faster                                                                |
| xml_etree_process          | 39.6 ms                                                                    | 39.3 ms: 1.01x faster                                                                |
| async_generators           | 231 ms                                                                     | 229 ms: 1.01x faster                                                                 |
| crypto_pyaes               | 47.0 ms                                                                    | 46.6 ms: 1.01x faster                                                                |
| scimark_fft                | 182 ms                                                                     | 182 ms: 1.01x faster                                                                 |
| mdp                        | 808 ms                                                                     | 805 ms: 1.00x faster                                                                 |
| shortest_path              | 365 ms                                                                     | 367 ms: 1.01x slower                                                                 |
| regex_compile              | 80.2 ms                                                                    | 80.9 ms: 1.01x slower                                                                |
| xml_etree_parse            | 89.3 ms                                                                    | 90.2 ms: 1.01x slower                                                                |
| scimark_sor                | 76.1 ms                                                                    | 76.9 ms: 1.01x slower                                                                |
| dulwich_log                | 41.1 ms                                                                    | 41.5 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                     | 345 ms: 1.01x slower                                                                 |
| create_gc_cycles           | 1.32 ms                                                                    | 1.34 ms: 1.01x slower                                                                |
| pathlib                    | 32.0 ms                                                                    | 32.4 ms: 1.01x slower                                                                |
| spectral_norm              | 59.2 ms                                                                    | 60.0 ms: 1.01x slower                                                                |
| deepcopy_reduce            | 1.83 us                                                                    | 1.85 us: 1.01x slower                                                                |
| scimark_monte_carlo        | 40.4 ms                                                                    | 41.9 ms: 1.04x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (25): pycparser, pylint, python_startup_no_site, float, 2to3, k_core, sympy_integrate, deepcopy, fannkuch, pidigits, many_optionals, pprint_safe_repr, telco, async_tree_none_tg, regex_effbot, mako, async_tree_io, regex_dna, thrift, connected_components, json_loads, gc_traversal, asyncio_websockets, json_dumps, subparsers

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown