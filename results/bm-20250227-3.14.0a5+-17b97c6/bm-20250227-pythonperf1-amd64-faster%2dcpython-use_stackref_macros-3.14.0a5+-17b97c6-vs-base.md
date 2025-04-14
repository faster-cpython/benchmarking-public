# Results vs. base

- fork: faster-cpython
- ref: use_stackref_macros
- machine: windows-amd64
- commit hash: 17b97c6
- commit date: 2025-02-27
- overall geometric mean: 1.017x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                      | 227 ms: 1.02x slower                                                                 |
| docutils       | 1.66 sec                                                                    | 1.69 sec: 1.02x slower                                                               |
| html5lib       | 40.0 ms                                                                     | 41.2 ms: 1.03x slower                                                                |
| sphinx         | 642 ms                                                                      | 654 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization    | 219 ms                                                                      | 223 ms: 1.01x slower                                                                 |
| asyncio_websockets        | 302 ms                                                                      | 308 ms: 1.02x slower                                                                 |
| async_tree_io_tg          | 402 ms                                                                      | 412 ms: 1.03x slower                                                                 |
| async_tree_none_tg        | 175 ms                                                                      | 180 ms: 1.03x slower                                                                 |
| async_tree_memoization_tg | 209 ms                                                                      | 216 ms: 1.03x slower                                                                 |
| async_generators          | 219 ms                                                                      | 229 ms: 1.05x slower                                                                 |
| coroutines                | 13.0 ms                                                                     | 13.8 ms: 1.06x slower                                                                |
| Geometric mean            | (ref)                                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 69.2 ms                                                                     | 65.5 ms: 1.06x faster                                                                |
| float          | 45.3 ms                                                                     | 46.8 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 114 ms                                                                      | 112 ms: 1.02x faster                                                                 |
| regex_effbot   | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                                |
| regex_compile  | 85.6 ms                                                                     | 87.2 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 89.1 ms                                                                     | 89.8 ms: 1.01x slower                                                                |
| pickle_pure_python   | 227 us                                                                      | 230 us: 1.01x slower                                                                 |
| tomli_loads          | 1.41 sec                                                                    | 1.43 sec: 1.01x slower                                                               |
| xml_etree_iterparse  | 62.5 ms                                                                     | 63.3 ms: 1.01x slower                                                                |
| json_loads           | 14.7 us                                                                     | 15.0 us: 1.02x slower                                                                |
| xml_etree_generate   | 56.1 ms                                                                     | 57.6 ms: 1.03x slower                                                                |
| xml_etree_process    | 39.9 ms                                                                     | 41.1 ms: 1.03x slower                                                                |
| json_dumps           | 6.66 ms                                                                     | 6.87 ms: 1.03x slower                                                                |
| unpickle_pure_python | 145 us                                                                      | 151 us: 1.04x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.0 ms                                                                     | 19.7 ms: 1.04x slower                                                                |
| python_startup         | 25.1 ms                                                                     | 26.1 ms: 1.04x slower                                                                |
| Geometric mean         | (ref)                                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 25.2 ms                                                                     | 26.2 ms: 1.04x slower                                                                |
| mako            | 6.75 ms                                                                     | 7.07 ms: 1.05x slower                                                                |
| genshi_text     | 16.3 ms                                                                     | 17.3 ms: 1.06x slower                                                                |
| genshi_xml      | 35.7 ms                                                                     | 38.1 ms: 1.07x slower                                                                |
| Geometric mean  | (ref)                                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody                     | 69.2 ms                                                                     | 65.5 ms: 1.06x faster                                                                |
| scimark_lu                | 62.6 ms                                                                     | 59.9 ms: 1.05x faster                                                                |
| deepcopy_memo             | 19.9 us                                                                     | 19.1 us: 1.04x faster                                                                |
| scimark_sparse_mat_mult   | 2.55 ms                                                                     | 2.46 ms: 1.04x faster                                                                |
| spectral_norm             | 58.4 ms                                                                     | 56.7 ms: 1.03x faster                                                                |
| mdp                       | 1.55 sec                                                                    | 1.50 sec: 1.03x faster                                                               |
| scimark_sor               | 82.7 ms                                                                     | 80.5 ms: 1.03x faster                                                                |
| pprint_safe_repr          | 557 ms                                                                      | 546 ms: 1.02x faster                                                                 |
| regex_dna                 | 114 ms                                                                      | 112 ms: 1.02x faster                                                                 |
| logging_silent            | 60.7 ns                                                                     | 59.7 ns: 1.02x faster                                                                |
| scimark_fft               | 186 ms                                                                      | 184 ms: 1.01x faster                                                                 |
| regex_effbot              | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                                |
| pprint_pformat            | 1.11 sec                                                                    | 1.10 sec: 1.01x faster                                                               |
| scimark_monte_carlo       | 43.9 ms                                                                     | 44.0 ms: 1.00x slower                                                                |
| xml_etree_parse           | 89.1 ms                                                                     | 89.8 ms: 1.01x slower                                                                |
| fannkuch                  | 270 ms                                                                      | 273 ms: 1.01x slower                                                                 |
| pyflate                   | 303 ms                                                                      | 306 ms: 1.01x slower                                                                 |
| sympy_str                 | 175 ms                                                                      | 177 ms: 1.01x slower                                                                 |
| pickle_pure_python        | 227 us                                                                      | 230 us: 1.01x slower                                                                 |
| many_optionals            | 435 us                                                                      | 440 us: 1.01x slower                                                                 |
| tomli_loads               | 1.41 sec                                                                    | 1.43 sec: 1.01x slower                                                               |
| logging_format            | 6.86 us                                                                     | 6.95 us: 1.01x slower                                                                |
| xml_etree_iterparse       | 62.5 ms                                                                     | 63.3 ms: 1.01x slower                                                                |
| sympy_sum                 | 89.2 ms                                                                     | 90.5 ms: 1.01x slower                                                                |
| meteor_contest            | 75.8 ms                                                                     | 76.9 ms: 1.01x slower                                                                |
| async_tree_memoization    | 219 ms                                                                      | 223 ms: 1.01x slower                                                                 |
| sqlite_synth              | 1.57 us                                                                     | 1.60 us: 1.02x slower                                                                |
| sympy_expand              | 300 ms                                                                      | 305 ms: 1.02x slower                                                                 |
| deepcopy_reduce           | 1.92 us                                                                     | 1.95 us: 1.02x slower                                                                |
| 2to3                      | 223 ms                                                                      | 227 ms: 1.02x slower                                                                 |
| deepcopy                  | 181 us                                                                      | 184 us: 1.02x slower                                                                 |
| richards_super            | 33.6 ms                                                                     | 34.1 ms: 1.02x slower                                                                |
| docutils                  | 1.66 sec                                                                    | 1.69 sec: 1.02x slower                                                               |
| sphinx                    | 642 ms                                                                      | 654 ms: 1.02x slower                                                                 |
| asyncio_websockets        | 302 ms                                                                      | 308 ms: 1.02x slower                                                                 |
| regex_compile             | 85.6 ms                                                                     | 87.2 ms: 1.02x slower                                                                |
| create_gc_cycles          | 1.21 ms                                                                     | 1.23 ms: 1.02x slower                                                                |
| bench_mp_pool             | 84.8 ms                                                                     | 86.6 ms: 1.02x slower                                                                |
| json_loads                | 14.7 us                                                                     | 15.0 us: 1.02x slower                                                                |
| sqlglot_normalize         | 191 ms                                                                      | 196 ms: 1.02x slower                                                                 |
| pylint                    | 198 ms                                                                      | 203 ms: 1.02x slower                                                                 |
| thrift                    | 514 us                                                                      | 528 us: 1.03x slower                                                                 |
| async_tree_io_tg          | 402 ms                                                                      | 412 ms: 1.03x slower                                                                 |
| json                      | 2.94 ms                                                                     | 3.02 ms: 1.03x slower                                                                |
| xml_etree_generate        | 56.1 ms                                                                     | 57.6 ms: 1.03x slower                                                                |
| shortest_path             | 354 ms                                                                      | 363 ms: 1.03x slower                                                                 |
| nqueens                   | 63.2 ms                                                                     | 65.0 ms: 1.03x slower                                                                |
| html5lib                  | 40.0 ms                                                                     | 41.2 ms: 1.03x slower                                                                |
| typing_runtime_protocols  | 106 us                                                                      | 109 us: 1.03x slower                                                                 |
| subparsers                | 16.2 ms                                                                     | 16.7 ms: 1.03x slower                                                                |
| xml_etree_process         | 39.9 ms                                                                     | 41.1 ms: 1.03x slower                                                                |
| async_tree_none_tg        | 175 ms                                                                      | 180 ms: 1.03x slower                                                                 |
| json_dumps                | 6.66 ms                                                                     | 6.87 ms: 1.03x slower                                                                |
| float                     | 45.3 ms                                                                     | 46.8 ms: 1.03x slower                                                                |
| richards                  | 29.3 ms                                                                     | 30.2 ms: 1.03x slower                                                                |
| async_tree_memoization_tg | 209 ms                                                                      | 216 ms: 1.03x slower                                                                 |
| connected_components      | 323 ms                                                                      | 334 ms: 1.03x slower                                                                 |
| coverage                  | 46.1 ms                                                                     | 47.6 ms: 1.03x slower                                                                |
| dulwich_log               | 41.9 ms                                                                     | 43.4 ms: 1.03x slower                                                                |
| python_startup_no_site    | 19.0 ms                                                                     | 19.7 ms: 1.04x slower                                                                |
| sqlglot_optimize          | 34.9 ms                                                                     | 36.2 ms: 1.04x slower                                                                |
| unpickle_pure_python      | 145 us                                                                      | 151 us: 1.04x slower                                                                 |
| python_startup            | 25.1 ms                                                                     | 26.1 ms: 1.04x slower                                                                |
| bpe_tokeniser             | 2.86 sec                                                                    | 2.97 sec: 1.04x slower                                                               |
| django_template           | 25.2 ms                                                                     | 26.2 ms: 1.04x slower                                                                |
| telco                     | 4.67 ms                                                                     | 4.88 ms: 1.04x slower                                                                |
| go                        | 85.5 ms                                                                     | 89.3 ms: 1.05x slower                                                                |
| async_generators          | 219 ms                                                                      | 229 ms: 1.05x slower                                                                 |
| sqlglot_transpile         | 1.07 ms                                                                     | 1.12 ms: 1.05x slower                                                                |
| mako                      | 6.75 ms                                                                     | 7.07 ms: 1.05x slower                                                                |
| sqlglot_parse             | 865 us                                                                      | 910 us: 1.05x slower                                                                 |
| crypto_pyaes              | 48.5 ms                                                                     | 51.3 ms: 1.06x slower                                                                |
| chaos                     | 41.7 ms                                                                     | 44.1 ms: 1.06x slower                                                                |
| genshi_text               | 16.3 ms                                                                     | 17.3 ms: 1.06x slower                                                                |
| comprehensions            | 11.4 us                                                                     | 12.1 us: 1.06x slower                                                                |
| coroutines                | 13.0 ms                                                                     | 13.8 ms: 1.06x slower                                                                |
| pathlib                   | 30.2 ms                                                                     | 32.1 ms: 1.06x slower                                                                |
| genshi_xml                | 35.7 ms                                                                     | 38.1 ms: 1.07x slower                                                                |
| deltablue                 | 2.16 ms                                                                     | 2.31 ms: 1.07x slower                                                                |
| raytrace                  | 191 ms                                                                      | 204 ms: 1.07x slower                                                                 |
| Geometric mean            | (ref)                                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (14): gc_traversal, async_tree_cpu_io_mixed, pycparser, pidigits, async_tree_cpu_io_mixed_tg, generators, async_tree_none, sympy_integrate, regex_v8, hexiom, logging_simple, k_core, async_tree_io, bench_thread_pool

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown