# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.004x slower
- HPT reliability: 94.47%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 1.64 sec                                                                   | 1.63 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 161 ms                                                                     | 158 ms: 1.02x faster                                                    |
| async_tree_none            | 169 ms                                                                     | 165 ms: 1.02x faster                                                    |
| async_tree_none_tg         | 168 ms                                                                     | 165 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 336 ms                                                                     | 333 ms: 1.01x faster                                                    |
| async_tree_memoization     | 202 ms                                                                     | 203 ms: 1.01x slower                                                    |
| coroutines                 | 14.3 ms                                                                    | 14.6 ms: 1.02x slower                                                   |
| async_generators           | 241 ms                                                                     | 252 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 55.4 ms                                                                    | 53.2 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 1.55 ms                                                                    | 1.57 ms: 1.01x slower                                                   |
| regex_compile  | 77.8 ms                                                                    | 78.7 ms: 1.01x slower                                                   |
| regex_v8       | 13.8 ms                                                                    | 14.2 ms: 1.03x slower                                                   |
| regex_dna      | 117 ms                                                                     | 121 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|---------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 50.6 ms                                                                    | 49.7 ms: 1.02x faster                                                   |
| tomli_loads         | 1.13 sec                                                                   | 1.12 sec: 1.01x faster                                                  |
| json_loads          | 14.5 us                                                                    | 14.4 us: 1.01x faster                                                   |
| xml_etree_parse     | 87.0 ms                                                                    | 87.5 ms: 1.01x slower                                                   |
| xml_etree_iterparse | 62.0 ms                                                                    | 62.9 ms: 1.01x slower                                                   |
| Geometric mean      | (ref)                                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                                    | 15.6 ms: 1.02x slower                                                   |
| django_template | 23.9 ms                                                                    | 24.6 ms: 1.03x slower                                                   |
| genshi_xml      | 33.6 ms                                                                    | 34.8 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 514 us                                                                     | 483 us: 1.06x faster                                                    |
| nbody                      | 55.4 ms                                                                    | 53.2 ms: 1.04x faster                                                   |
| telco                      | 4.43 ms                                                                    | 4.26 ms: 1.04x faster                                                   |
| comprehensions             | 10.7 us                                                                    | 10.4 us: 1.03x faster                                                   |
| typing_runtime_protocols   | 106 us                                                                     | 103 us: 1.02x faster                                                    |
| pprint_pformat             | 914 ms                                                                     | 895 ms: 1.02x faster                                                    |
| asyncio_websockets         | 161 ms                                                                     | 158 ms: 1.02x faster                                                    |
| async_tree_none            | 169 ms                                                                     | 165 ms: 1.02x faster                                                    |
| xml_etree_generate         | 50.6 ms                                                                    | 49.7 ms: 1.02x faster                                                   |
| meteor_contest             | 71.9 ms                                                                    | 70.6 ms: 1.02x faster                                                   |
| k_core                     | 1.62 sec                                                                   | 1.59 sec: 1.02x faster                                                  |
| async_tree_none_tg         | 168 ms                                                                     | 165 ms: 1.02x faster                                                    |
| many_optionals             | 451 us                                                                     | 444 us: 1.02x faster                                                    |
| subparsers                 | 17.3 ms                                                                    | 17.1 ms: 1.02x faster                                                   |
| sqlite_synth               | 1.58 us                                                                    | 1.56 us: 1.02x faster                                                   |
| tomli_loads                | 1.13 sec                                                                   | 1.12 sec: 1.01x faster                                                  |
| pprint_safe_repr           | 442 ms                                                                     | 437 ms: 1.01x faster                                                    |
| hexiom                     | 4.13 ms                                                                    | 4.09 ms: 1.01x faster                                                   |
| sqlglot_v2_parse           | 782 us                                                                     | 775 us: 1.01x faster                                                    |
| json_loads                 | 14.5 us                                                                    | 14.4 us: 1.01x faster                                                   |
| shortest_path              | 357 ms                                                                     | 354 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 336 ms                                                                     | 333 ms: 1.01x faster                                                    |
| docutils                   | 1.64 sec                                                                   | 1.63 sec: 1.01x faster                                                  |
| richards                   | 26.5 ms                                                                    | 26.4 ms: 1.01x faster                                                   |
| xml_etree_parse            | 87.0 ms                                                                    | 87.5 ms: 1.01x slower                                                   |
| sympy_sum                  | 87.3 ms                                                                    | 87.9 ms: 1.01x slower                                                   |
| sympy_str                  | 170 ms                                                                     | 171 ms: 1.01x slower                                                    |
| dulwich_log                | 39.8 ms                                                                    | 40.1 ms: 1.01x slower                                                   |
| async_tree_memoization     | 202 ms                                                                     | 203 ms: 1.01x slower                                                    |
| regex_effbot               | 1.55 ms                                                                    | 1.57 ms: 1.01x slower                                                   |
| create_gc_cycles           | 1.30 ms                                                                    | 1.31 ms: 1.01x slower                                                   |
| scimark_sor                | 75.7 ms                                                                    | 76.5 ms: 1.01x slower                                                   |
| regex_compile              | 77.8 ms                                                                    | 78.7 ms: 1.01x slower                                                   |
| deepcopy_memo              | 17.7 us                                                                    | 17.9 us: 1.01x slower                                                   |
| raytrace                   | 177 ms                                                                     | 180 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 62.0 ms                                                                    | 62.9 ms: 1.01x slower                                                   |
| deepcopy                   | 168 us                                                                     | 171 us: 1.01x slower                                                    |
| sqlglot_v2_normalize       | 69.3 ms                                                                    | 70.3 ms: 1.01x slower                                                   |
| nqueens                    | 59.3 ms                                                                    | 60.3 ms: 1.02x slower                                                   |
| json                       | 2.95 ms                                                                    | 3.00 ms: 1.02x slower                                                   |
| sympy_expand               | 292 ms                                                                     | 297 ms: 1.02x slower                                                    |
| generators                 | 19.3 ms                                                                    | 19.6 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 2.58 sec                                                                   | 2.63 sec: 1.02x slower                                                  |
| genshi_text                | 15.3 ms                                                                    | 15.6 ms: 1.02x slower                                                   |
| deepcopy_reduce            | 1.81 us                                                                    | 1.85 us: 1.02x slower                                                   |
| scimark_fft                | 151 ms                                                                     | 154 ms: 1.02x slower                                                    |
| logging_format             | 6.53 us                                                                    | 6.67 us: 1.02x slower                                                   |
| chaos                      | 40.4 ms                                                                    | 41.3 ms: 1.02x slower                                                   |
| coroutines                 | 14.3 ms                                                                    | 14.6 ms: 1.02x slower                                                   |
| django_template            | 23.9 ms                                                                    | 24.6 ms: 1.03x slower                                                   |
| regex_v8                   | 13.8 ms                                                                    | 14.2 ms: 1.03x slower                                                   |
| gc_traversal               | 2.07 ms                                                                    | 2.14 ms: 1.03x slower                                                   |
| genshi_xml                 | 33.6 ms                                                                    | 34.8 ms: 1.04x slower                                                   |
| logging_simple             | 6.02 us                                                                    | 6.24 us: 1.04x slower                                                   |
| regex_dna                  | 117 ms                                                                     | 121 ms: 1.04x slower                                                    |
| scimark_monte_carlo        | 39.9 ms                                                                    | 41.5 ms: 1.04x slower                                                   |
| async_generators           | 241 ms                                                                     | 252 ms: 1.05x slower                                                    |
| scimark_lu                 | 60.8 ms                                                                    | 64.5 ms: 1.06x slower                                                   |
| spectral_norm              | 66.1 ms                                                                    | 70.3 ms: 1.06x slower                                                   |
| coverage                   | 48.1 ms                                                                    | 52.2 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (32): pathlib, html5lib, async_tree_memoization_tg, 2to3, pycparser, scimark_sparse_mat_mult, sympy_integrate, mako, connected_components, pickle_pure_python, python_startup, sqlglot_v2_optimize, pylint, unpickle_pure_python, deltablue, go, mdp, logging_silent, xml_etree_process, sphinx, richards_super, pyflate, pidigits, sqlglot_v2_transpile, crypto_pyaes, fannkuch, python_startup_no_site, json_dumps, async_tree_cpu_io_mixed, float, async_tree_io, async_tree_io_tg

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 94.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown