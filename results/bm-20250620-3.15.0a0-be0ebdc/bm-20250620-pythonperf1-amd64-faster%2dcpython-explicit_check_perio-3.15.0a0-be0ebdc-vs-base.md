# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.003x slower
- HPT reliability: 97.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 222 ms: 1.01x slower                                                                 |
| docutils       | 1.63 sec                                                                   | 1.63 sec: 1.01x faster                                                               |
| html5lib       | 37.9 ms                                                                    | 38.9 ms: 1.03x slower                                                                |
| sphinx         | 640 ms                                                                     | 648 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets        | 161 ms                                                                     | 157 ms: 1.02x faster                                                                 |
| async_tree_io_tg          | 393 ms                                                                     | 389 ms: 1.01x faster                                                                 |
| coroutines                | 14.2 ms                                                                    | 14.3 ms: 1.01x slower                                                                |
| async_tree_none_tg        | 168 ms                                                                     | 170 ms: 1.01x slower                                                                 |
| async_tree_memoization_tg | 209 ms                                                                     | 212 ms: 1.02x slower                                                                 |
| async_generators          | 229 ms                                                                     | 233 ms: 1.02x slower                                                                 |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 63.3 ms                                                                    | 62.5 ms: 1.01x faster                                                                |
| float          | 42.8 ms                                                                    | 44.7 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 14.0 ms                                                                    | 13.7 ms: 1.02x faster                                                                |
| regex_compile  | 79.6 ms                                                                    | 81.1 ms: 1.02x slower                                                                |
| regex_dna      | 120 ms                                                                     | 122 ms: 1.02x slower                                                                 |
| regex_effbot   | 1.51 ms                                                                    | 1.54 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.0 ms                                                                    | 62.9 ms: 1.03x faster                                                                |
| json_loads           | 14.3 us                                                                    | 14.0 us: 1.03x faster                                                                |
| xml_etree_parse      | 89.1 ms                                                                    | 87.5 ms: 1.02x faster                                                                |
| unpickle_pure_python | 136 us                                                                     | 135 us: 1.01x faster                                                                 |
| xml_etree_process    | 38.9 ms                                                                    | 39.1 ms: 1.01x slower                                                                |
| json_dumps           | 6.33 ms                                                                    | 6.39 ms: 1.01x slower                                                                |
| pickle_pure_python   | 213 us                                                                     | 216 us: 1.01x slower                                                                 |
| tomli_loads          | 1.36 sec                                                                   | 1.40 sec: 1.03x slower                                                               |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text    | 15.2 ms                                                                    | 15.4 ms: 1.01x slower                                                                |
| genshi_xml     | 33.8 ms                                                                    | 35.1 ms: 1.04x slower                                                                |
| mako           | 6.50 ms                                                                    | 6.88 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coverage                  | 50.3 ms                                                                    | 48.2 ms: 1.04x faster                                                                |
| logging_format            | 6.99 us                                                                    | 6.73 us: 1.04x faster                                                                |
| xml_etree_iterparse       | 65.0 ms                                                                    | 62.9 ms: 1.03x faster                                                                |
| pyflate                   | 292 ms                                                                     | 284 ms: 1.03x faster                                                                 |
| logging_simple            | 6.54 us                                                                    | 6.36 us: 1.03x faster                                                                |
| json_loads                | 14.3 us                                                                    | 14.0 us: 1.03x faster                                                                |
| regex_v8                  | 14.0 ms                                                                    | 13.7 ms: 1.02x faster                                                                |
| asyncio_websockets        | 161 ms                                                                     | 157 ms: 1.02x faster                                                                 |
| scimark_fft               | 179 ms                                                                     | 175 ms: 1.02x faster                                                                 |
| scimark_monte_carlo       | 40.1 ms                                                                    | 39.3 ms: 1.02x faster                                                                |
| sqlglot_v2_transpile      | 1.04 ms                                                                    | 1.02 ms: 1.02x faster                                                                |
| xml_etree_parse           | 89.1 ms                                                                    | 87.5 ms: 1.02x faster                                                                |
| sqlglot_v2_parse          | 834 us                                                                     | 821 us: 1.01x faster                                                                 |
| chaos                     | 41.2 ms                                                                    | 40.6 ms: 1.01x faster                                                                |
| nbody                     | 63.3 ms                                                                    | 62.5 ms: 1.01x faster                                                                |
| richards                  | 27.6 ms                                                                    | 27.3 ms: 1.01x faster                                                                |
| nqueens                   | 61.0 ms                                                                    | 60.3 ms: 1.01x faster                                                                |
| async_tree_io_tg          | 393 ms                                                                     | 389 ms: 1.01x faster                                                                 |
| go                        | 76.8 ms                                                                    | 76.2 ms: 1.01x faster                                                                |
| comprehensions            | 10.7 us                                                                    | 10.7 us: 1.01x faster                                                                |
| create_gc_cycles          | 1.33 ms                                                                    | 1.32 ms: 1.01x faster                                                                |
| unpickle_pure_python      | 136 us                                                                     | 135 us: 1.01x faster                                                                 |
| scimark_sparse_mat_mult   | 2.52 ms                                                                    | 2.51 ms: 1.01x faster                                                                |
| docutils                  | 1.63 sec                                                                   | 1.63 sec: 1.01x faster                                                               |
| logging_silent            | 325 ns                                                                     | 323 ns: 1.00x faster                                                                 |
| bpe_tokeniser             | 2.97 sec                                                                   | 2.96 sec: 1.00x faster                                                               |
| mdp                       | 808 ms                                                                     | 811 ms: 1.00x slower                                                                 |
| xml_etree_process         | 38.9 ms                                                                    | 39.1 ms: 1.01x slower                                                                |
| 2to3                      | 220 ms                                                                     | 222 ms: 1.01x slower                                                                 |
| coroutines                | 14.2 ms                                                                    | 14.3 ms: 1.01x slower                                                                |
| sqlite_synth              | 1.58 us                                                                    | 1.59 us: 1.01x slower                                                                |
| typing_runtime_protocols  | 102 us                                                                     | 103 us: 1.01x slower                                                                 |
| async_tree_none_tg        | 168 ms                                                                     | 170 ms: 1.01x slower                                                                 |
| dulwich_log               | 41.0 ms                                                                    | 41.4 ms: 1.01x slower                                                                |
| json_dumps                | 6.33 ms                                                                    | 6.39 ms: 1.01x slower                                                                |
| sqlglot_v2_normalize      | 69.5 ms                                                                    | 70.3 ms: 1.01x slower                                                                |
| pickle_pure_python        | 213 us                                                                     | 216 us: 1.01x slower                                                                 |
| genshi_text               | 15.2 ms                                                                    | 15.4 ms: 1.01x slower                                                                |
| sympy_integrate           | 12.4 ms                                                                    | 12.5 ms: 1.01x slower                                                                |
| sympy_sum                 | 87.4 ms                                                                    | 88.3 ms: 1.01x slower                                                                |
| sphinx                    | 640 ms                                                                     | 648 ms: 1.01x slower                                                                 |
| many_optionals            | 439 us                                                                     | 444 us: 1.01x slower                                                                 |
| scimark_lu                | 58.0 ms                                                                    | 58.6 ms: 1.01x slower                                                                |
| sympy_str                 | 168 ms                                                                     | 170 ms: 1.01x slower                                                                 |
| async_tree_memoization_tg | 209 ms                                                                     | 212 ms: 1.02x slower                                                                 |
| async_generators          | 229 ms                                                                     | 233 ms: 1.02x slower                                                                 |
| regex_compile             | 79.6 ms                                                                    | 81.1 ms: 1.02x slower                                                                |
| regex_dna                 | 120 ms                                                                     | 122 ms: 1.02x slower                                                                 |
| fannkuch                  | 254 ms                                                                     | 260 ms: 1.02x slower                                                                 |
| spectral_norm             | 61.4 ms                                                                    | 62.6 ms: 1.02x slower                                                                |
| thrift                    | 496 us                                                                     | 507 us: 1.02x slower                                                                 |
| subparsers                | 17.0 ms                                                                    | 17.4 ms: 1.02x slower                                                                |
| deepcopy_reduce           | 1.79 us                                                                    | 1.83 us: 1.02x slower                                                                |
| regex_effbot              | 1.51 ms                                                                    | 1.54 ms: 1.02x slower                                                                |
| sympy_expand              | 286 ms                                                                     | 293 ms: 1.02x slower                                                                 |
| meteor_contest            | 72.1 ms                                                                    | 73.9 ms: 1.03x slower                                                                |
| html5lib                  | 37.9 ms                                                                    | 38.9 ms: 1.03x slower                                                                |
| tomli_loads               | 1.36 sec                                                                   | 1.40 sec: 1.03x slower                                                               |
| deepcopy                  | 168 us                                                                     | 173 us: 1.03x slower                                                                 |
| pprint_pformat            | 1.09 sec                                                                   | 1.12 sec: 1.03x slower                                                               |
| genshi_xml                | 33.8 ms                                                                    | 35.1 ms: 1.04x slower                                                                |
| pprint_safe_repr          | 530 ms                                                                     | 552 ms: 1.04x slower                                                                 |
| float                     | 42.8 ms                                                                    | 44.7 ms: 1.04x slower                                                                |
| mako                      | 6.50 ms                                                                    | 6.88 ms: 1.06x slower                                                                |
| deepcopy_memo             | 17.4 us                                                                    | 18.4 us: 1.06x slower                                                                |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (27): python_startup_no_site, python_startup, richards_super, json, pycparser, async_tree_cpu_io_mixed, shortest_path, generators, pidigits, crypto_pyaes, xml_etree_generate, connected_components, async_tree_none, scimark_sor, k_core, django_template, hexiom, telco, deltablue, async_tree_io, async_tree_cpu_io_mixed_tg, sqlglot_v2_optimize, async_tree_memoization, pathlib, gc_traversal, raytrace, pylint

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 97.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown