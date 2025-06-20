# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.003x slower
- HPT reliability: 98.33%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                     | 221 ms: 1.01x faster                                                                 |
| sphinx         | 640 ms                                                                     | 649 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 331 ms                                                                     | 333 ms: 1.01x slower                                                                 |
| coroutines                 | 14.4 ms                                                                    | 14.5 ms: 1.01x slower                                                                |
| async_tree_memoization     | 211 ms                                                                     | 214 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 342 ms                                                                     | 347 ms: 1.01x slower                                                                 |
| async_tree_memoization_tg  | 215 ms                                                                     | 218 ms: 1.01x slower                                                                 |
| async_tree_none            | 174 ms                                                                     | 177 ms: 1.02x slower                                                                 |
| async_tree_io_tg           | 397 ms                                                                     | 406 ms: 1.02x slower                                                                 |
| async_tree_none_tg         | 170 ms                                                                     | 174 ms: 1.02x slower                                                                 |
| async_tree_io              | 400 ms                                                                     | 415 ms: 1.04x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                                    | 65.2 ms: 1.02x faster                                                                |
| float          | 44.9 ms                                                                    | 44.5 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.53 ms                                                                    | 1.52 ms: 1.01x faster                                                                |
| regex_compile  | 81.2 ms                                                                    | 82.0 ms: 1.01x slower                                                                |
| regex_dna      | 119 ms                                                                     | 121 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.45 sec                                                                   | 1.43 sec: 1.01x faster                                                               |
| unpickle_pure_python | 137 us                                                                     | 138 us: 1.01x slower                                                                 |
| json_loads           | 14.4 us                                                                    | 14.6 us: 1.01x slower                                                                |
| pickle_pure_python   | 215 us                                                                     | 219 us: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, xml_etree_generate, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text    | 15.4 ms                                                                    | 15.7 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| deepcopy_memo              | 20.0 us                                                                    | 18.8 us: 1.06x faster                                                                |
| logging_silent             | 327 ns                                                                     | 318 ns: 1.03x faster                                                                 |
| chaos                      | 41.4 ms                                                                    | 40.5 ms: 1.02x faster                                                                |
| nbody                      | 66.3 ms                                                                    | 65.2 ms: 1.02x faster                                                                |
| pprint_pformat             | 1.13 sec                                                                   | 1.11 sec: 1.02x faster                                                               |
| logging_simple             | 6.46 us                                                                    | 6.36 us: 1.02x faster                                                                |
| tomli_loads                | 1.45 sec                                                                   | 1.43 sec: 1.01x faster                                                               |
| logging_format             | 6.90 us                                                                    | 6.81 us: 1.01x faster                                                                |
| shortest_path              | 366 ms                                                                     | 362 ms: 1.01x faster                                                                 |
| sqlglot_v2_optimize        | 34.4 ms                                                                    | 34.0 ms: 1.01x faster                                                                |
| pprint_safe_repr           | 555 ms                                                                     | 548 ms: 1.01x faster                                                                 |
| connected_components       | 335 ms                                                                     | 332 ms: 1.01x faster                                                                 |
| sqlglot_v2_transpile       | 1.04 ms                                                                    | 1.03 ms: 1.01x faster                                                                |
| regex_effbot               | 1.53 ms                                                                    | 1.52 ms: 1.01x faster                                                                |
| float                      | 44.9 ms                                                                    | 44.5 ms: 1.01x faster                                                                |
| coverage                   | 49.0 ms                                                                    | 48.7 ms: 1.01x faster                                                                |
| 2to3                       | 223 ms                                                                     | 221 ms: 1.01x faster                                                                 |
| go                         | 77.4 ms                                                                    | 77.8 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed    | 331 ms                                                                     | 333 ms: 1.01x slower                                                                 |
| unpickle_pure_python       | 137 us                                                                     | 138 us: 1.01x slower                                                                 |
| pathlib                    | 31.6 ms                                                                    | 31.8 ms: 1.01x slower                                                                |
| coroutines                 | 14.4 ms                                                                    | 14.5 ms: 1.01x slower                                                                |
| generators                 | 19.4 ms                                                                    | 19.6 ms: 1.01x slower                                                                |
| regex_compile              | 81.2 ms                                                                    | 82.0 ms: 1.01x slower                                                                |
| sympy_sum                  | 87.9 ms                                                                    | 88.8 ms: 1.01x slower                                                                |
| deepcopy                   | 174 us                                                                     | 176 us: 1.01x slower                                                                 |
| sympy_integrate            | 12.5 ms                                                                    | 12.7 ms: 1.01x slower                                                                |
| deepcopy_reduce            | 1.83 us                                                                    | 1.85 us: 1.01x slower                                                                |
| sympy_expand               | 289 ms                                                                     | 292 ms: 1.01x slower                                                                 |
| scimark_fft                | 181 ms                                                                     | 183 ms: 1.01x slower                                                                 |
| dulwich_log                | 41.1 ms                                                                    | 41.6 ms: 1.01x slower                                                                |
| meteor_contest             | 73.5 ms                                                                    | 74.4 ms: 1.01x slower                                                                |
| json_loads                 | 14.4 us                                                                    | 14.6 us: 1.01x slower                                                                |
| bpe_tokeniser              | 2.95 sec                                                                   | 2.99 sec: 1.01x slower                                                               |
| async_tree_memoization     | 211 ms                                                                     | 214 ms: 1.01x slower                                                                 |
| sphinx                     | 640 ms                                                                     | 649 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 342 ms                                                                     | 347 ms: 1.01x slower                                                                 |
| async_tree_memoization_tg  | 215 ms                                                                     | 218 ms: 1.01x slower                                                                 |
| pycparser                  | 707 ms                                                                     | 717 ms: 1.01x slower                                                                 |
| fannkuch                   | 261 ms                                                                     | 265 ms: 1.01x slower                                                                 |
| sympy_str                  | 170 ms                                                                     | 172 ms: 1.01x slower                                                                 |
| async_tree_none            | 174 ms                                                                     | 177 ms: 1.02x slower                                                                 |
| scimark_lu                 | 59.0 ms                                                                    | 59.9 ms: 1.02x slower                                                                |
| pickle_pure_python         | 215 us                                                                     | 219 us: 1.02x slower                                                                 |
| genshi_text                | 15.4 ms                                                                    | 15.7 ms: 1.02x slower                                                                |
| regex_dna                  | 119 ms                                                                     | 121 ms: 1.02x slower                                                                 |
| deltablue                  | 2.24 ms                                                                    | 2.29 ms: 1.02x slower                                                                |
| hexiom                     | 4.13 ms                                                                    | 4.22 ms: 1.02x slower                                                                |
| async_tree_io_tg           | 397 ms                                                                     | 406 ms: 1.02x slower                                                                 |
| async_tree_none_tg         | 170 ms                                                                     | 174 ms: 1.02x slower                                                                 |
| richards                   | 27.4 ms                                                                    | 28.2 ms: 1.03x slower                                                                |
| richards_super             | 31.0 ms                                                                    | 31.9 ms: 1.03x slower                                                                |
| scimark_monte_carlo        | 39.7 ms                                                                    | 41.0 ms: 1.03x slower                                                                |
| async_tree_io              | 400 ms                                                                     | 415 ms: 1.04x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (38): gc_traversal, mako, create_gc_cycles, xml_etree_parse, sqlglot_v2_parse, scimark_sor, raytrace, spectral_norm, xml_etree_process, pidigits, mdp, comprehensions, xml_etree_generate, pyflate, html5lib, sqlite_synth, xml_etree_iterparse, python_startup, scimark_sparse_mat_mult, pylint, thrift, docutils, nqueens, many_optionals, json_dumps, sqlglot_v2_normalize, telco, k_core, crypto_pyaes, django_template, json, python_startup_no_site, asyncio_websockets, async_generators, typing_runtime_protocols, subparsers, regex_v8, genshi_xml

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 98.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown