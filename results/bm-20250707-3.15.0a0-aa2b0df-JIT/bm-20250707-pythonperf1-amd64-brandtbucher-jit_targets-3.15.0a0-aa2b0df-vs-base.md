# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.003x slower
- HPT reliability: 89.28%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                                   | 1.65 sec: 1.01x slower                                                  |
| html5lib       | 38.4 ms                                                                    | 37.9 ms: 1.01x faster                                                   |
| sphinx         | 635 ms                                                                     | 644 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|---------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization    | 204 ms                                                                     | 206 ms: 1.01x slower                                                    |
| async_tree_none           | 168 ms                                                                     | 169 ms: 1.01x slower                                                    |
| async_tree_memoization_tg | 206 ms                                                                     | 210 ms: 1.02x slower                                                    |
| async_tree_none_tg        | 167 ms                                                                     | 170 ms: 1.02x slower                                                    |
| async_tree_io_tg          | 384 ms                                                                     | 391 ms: 1.02x slower                                                    |
| asyncio_websockets        | 158 ms                                                                     | 165 ms: 1.05x slower                                                    |
| Geometric mean            | (ref)                                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (5): coroutines, async_tree_cpu_io_mixed, async_generators, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 43.7 ms                                                                    | 44.9 ms: 1.03x slower                                                   |
| nbody          | 55.0 ms                                                                    | 59.8 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                      | 1.04x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                                    | 78.8 ms: 1.01x slower                                                   |
| regex_effbot   | 1.55 ms                                                                    | 1.62 ms: 1.05x slower                                                   |
| regex_dna      | 115 ms                                                                     | 121 ms: 1.05x slower                                                    |
| regex_v8       | 13.5 ms                                                                    | 14.2 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                      | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 108 us                                                                     | 105 us: 1.03x faster                                                    |
| xml_etree_generate   | 49.8 ms                                                                    | 49.2 ms: 1.01x faster                                                   |
| tomli_loads          | 1.13 sec                                                                   | 1.12 sec: 1.01x faster                                                  |
| xml_etree_process    | 35.0 ms                                                                    | 34.8 ms: 1.01x faster                                                   |
| xml_etree_parse      | 87.8 ms                                                                    | 88.5 ms: 1.01x slower                                                   |
| pickle_pure_python   | 202 us                                                                     | 207 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 34.9 ms                                                                    | 35.2 ms: 1.01x slower                                                   |
| genshi_text     | 15.4 ms                                                                    | 15.7 ms: 1.02x slower                                                   |
| django_template | 23.9 ms                                                                    | 25.0 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|---------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_safe_repr          | 460 ms                                                                     | 434 ms: 1.06x faster                                                    |
| spectral_norm             | 68.2 ms                                                                    | 64.5 ms: 1.06x faster                                                   |
| pprint_pformat            | 931 ms                                                                     | 881 ms: 1.06x faster                                                    |
| coverage                  | 51.0 ms                                                                    | 49.3 ms: 1.04x faster                                                   |
| unpickle_pure_python      | 108 us                                                                     | 105 us: 1.03x faster                                                    |
| scimark_lu                | 60.1 ms                                                                    | 58.8 ms: 1.02x faster                                                   |
| comprehensions            | 10.5 us                                                                    | 10.3 us: 1.02x faster                                                   |
| json                      | 2.98 ms                                                                    | 2.93 ms: 1.02x faster                                                   |
| html5lib                  | 38.4 ms                                                                    | 37.9 ms: 1.01x faster                                                   |
| sqlglot_v2_normalize      | 71.2 ms                                                                    | 70.2 ms: 1.01x faster                                                   |
| xml_etree_generate        | 49.8 ms                                                                    | 49.2 ms: 1.01x faster                                                   |
| connected_components      | 326 ms                                                                     | 322 ms: 1.01x faster                                                    |
| deepcopy_reduce           | 1.83 us                                                                    | 1.81 us: 1.01x faster                                                   |
| tomli_loads               | 1.13 sec                                                                   | 1.12 sec: 1.01x faster                                                  |
| crypto_pyaes              | 46.4 ms                                                                    | 45.9 ms: 1.01x faster                                                   |
| sqlglot_v2_optimize       | 34.5 ms                                                                    | 34.1 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 2.58 sec                                                                   | 2.55 sec: 1.01x faster                                                  |
| sympy_expand              | 294 ms                                                                     | 291 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult   | 2.27 ms                                                                    | 2.25 ms: 1.01x faster                                                   |
| hexiom                    | 4.15 ms                                                                    | 4.12 ms: 1.01x faster                                                   |
| sympy_sum                 | 87.4 ms                                                                    | 86.9 ms: 1.01x faster                                                   |
| deepcopy_memo             | 17.9 us                                                                    | 17.8 us: 1.01x faster                                                   |
| xml_etree_process         | 35.0 ms                                                                    | 34.8 ms: 1.01x faster                                                   |
| nqueens                   | 59.3 ms                                                                    | 59.0 ms: 1.01x faster                                                   |
| deepcopy                  | 170 us                                                                     | 169 us: 1.01x faster                                                    |
| generators                | 19.6 ms                                                                    | 19.5 ms: 1.00x faster                                                   |
| sqlglot_v2_parse          | 781 us                                                                     | 778 us: 1.00x faster                                                    |
| sqlglot_v2_transpile      | 986 us                                                                     | 991 us: 1.01x slower                                                    |
| dulwich_log               | 40.9 ms                                                                    | 41.1 ms: 1.01x slower                                                   |
| meteor_contest            | 70.4 ms                                                                    | 70.8 ms: 1.01x slower                                                   |
| sympy_integrate           | 12.6 ms                                                                    | 12.7 ms: 1.01x slower                                                   |
| regex_compile             | 78.3 ms                                                                    | 78.8 ms: 1.01x slower                                                   |
| many_optionals            | 444 us                                                                     | 447 us: 1.01x slower                                                    |
| xml_etree_parse           | 87.8 ms                                                                    | 88.5 ms: 1.01x slower                                                   |
| genshi_xml                | 34.9 ms                                                                    | 35.2 ms: 1.01x slower                                                   |
| scimark_sor               | 77.2 ms                                                                    | 77.9 ms: 1.01x slower                                                   |
| async_tree_memoization    | 204 ms                                                                     | 206 ms: 1.01x slower                                                    |
| async_tree_none           | 168 ms                                                                     | 169 ms: 1.01x slower                                                    |
| deltablue                 | 2.19 ms                                                                    | 2.21 ms: 1.01x slower                                                   |
| gc_traversal              | 2.11 ms                                                                    | 2.13 ms: 1.01x slower                                                   |
| docutils                  | 1.63 sec                                                                   | 1.65 sec: 1.01x slower                                                  |
| logging_format            | 6.51 us                                                                    | 6.58 us: 1.01x slower                                                   |
| sphinx                    | 635 ms                                                                     | 644 ms: 1.01x slower                                                    |
| go                        | 76.2 ms                                                                    | 77.4 ms: 1.02x slower                                                   |
| async_tree_memoization_tg | 206 ms                                                                     | 210 ms: 1.02x slower                                                    |
| async_tree_none_tg        | 167 ms                                                                     | 170 ms: 1.02x slower                                                    |
| genshi_text               | 15.4 ms                                                                    | 15.7 ms: 1.02x slower                                                   |
| async_tree_io_tg          | 384 ms                                                                     | 391 ms: 1.02x slower                                                    |
| richards_super            | 29.9 ms                                                                    | 30.6 ms: 1.02x slower                                                   |
| logging_simple            | 6.02 us                                                                    | 6.16 us: 1.02x slower                                                   |
| richards                  | 26.3 ms                                                                    | 26.9 ms: 1.02x slower                                                   |
| pickle_pure_python        | 202 us                                                                     | 207 us: 1.02x slower                                                    |
| scimark_monte_carlo       | 39.9 ms                                                                    | 40.9 ms: 1.03x slower                                                   |
| thrift                    | 484 us                                                                     | 496 us: 1.03x slower                                                    |
| float                     | 43.7 ms                                                                    | 44.9 ms: 1.03x slower                                                   |
| raytrace                  | 177 ms                                                                     | 183 ms: 1.04x slower                                                    |
| django_template           | 23.9 ms                                                                    | 25.0 ms: 1.04x slower                                                   |
| fannkuch                  | 222 ms                                                                     | 232 ms: 1.05x slower                                                    |
| regex_effbot              | 1.55 ms                                                                    | 1.62 ms: 1.05x slower                                                   |
| asyncio_websockets        | 158 ms                                                                     | 165 ms: 1.05x slower                                                    |
| regex_dna                 | 115 ms                                                                     | 121 ms: 1.05x slower                                                    |
| regex_v8                  | 13.5 ms                                                                    | 14.2 ms: 1.05x slower                                                   |
| nbody                     | 55.0 ms                                                                    | 59.8 ms: 1.09x slower                                                   |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (29): python_startup_no_site, json_loads, k_core, scimark_fft, python_startup, mako, sympy_str, 2to3, mdp, logging_silent, subparsers, shortest_path, coroutines, pathlib, xml_etree_iterparse, pyflate, create_gc_cycles, pylint, typing_runtime_protocols, sqlite_synth, pidigits, async_tree_cpu_io_mixed, async_generators, pycparser, chaos, telco, async_tree_cpu_io_mixed_tg, json_dumps, async_tree_io

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 89.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown