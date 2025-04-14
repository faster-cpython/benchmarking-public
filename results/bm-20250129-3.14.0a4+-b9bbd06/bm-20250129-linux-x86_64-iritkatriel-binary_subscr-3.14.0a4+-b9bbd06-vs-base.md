# Results vs. base

- fork: iritkatriel
- ref: binary_subscr
- machine: linux-x86_64
- commit hash: b9bbd06
- commit date: 2025-01-29
- overall geometric mean: 1.005x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 257 ms: 1.01x slower                                                 |
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                | 23.6 ms                                                                | 23.7 ms: 1.00x slower                                                |
| async_tree_memoization    | 324 ms                                                                 | 326 ms: 1.01x slower                                                 |
| async_tree_memoization_tg | 313 ms                                                                 | 316 ms: 1.01x slower                                                 |
| async_tree_none_tg        | 253 ms                                                                 | 258 ms: 1.02x slower                                                 |
| async_generators          | 378 ms                                                                 | 385 ms: 1.02x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (6): async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                                | 3.13 ms: 1.06x faster                                                |
| regex_dna      | 210 ms                                                                 | 212 ms: 1.01x slower                                                 |
| regex_compile  | 127 ms                                                                 | 129 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 326 us                                                                 | 321 us: 1.02x faster                                                 |
| xml_etree_generate   | 85.4 ms                                                                | 84.7 ms: 1.01x faster                                                |
| xml_etree_process    | 60.0 ms                                                                | 59.6 ms: 1.01x faster                                                |
| xml_etree_iterparse  | 97.6 ms                                                                | 97.0 ms: 1.01x faster                                                |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.00x faster                                                 |
| json_loads           | 28.6 us                                                                | 29.0 us: 1.01x slower                                                |
| unpickle_pure_python | 218 us                                                                 | 222 us: 1.02x slower                                                 |
| json_dumps           | 11.6 ms                                                                | 11.8 ms: 1.02x slower                                                |
| tomli_loads          | 1.93 sec                                                               | 2.08 sec: 1.07x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                |
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.2 ms: 1.01x faster                                                |
| genshi_xml      | 49.5 ms                                                                | 49.3 ms: 1.01x faster                                                |
| mako            | 10.8 ms                                                                | 11.4 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot              | 3.32 ms                                                                | 3.13 ms: 1.06x faster                                                |
| spectral_norm             | 101 ms                                                                 | 98.7 ms: 1.03x faster                                                |
| gc_traversal              | 4.91 ms                                                                | 4.81 ms: 1.02x faster                                                |
| pycparser                 | 1.16 sec                                                               | 1.14 sec: 1.02x faster                                               |
| coverage                  | 91.4 ms                                                                | 89.9 ms: 1.02x faster                                                |
| pickle_pure_python        | 326 us                                                                 | 321 us: 1.02x faster                                                 |
| logging_format            | 6.22 us                                                                | 6.13 us: 1.01x faster                                                |
| django_template           | 32.6 ms                                                                | 32.2 ms: 1.01x faster                                                |
| telco                     | 7.99 ms                                                                | 7.91 ms: 1.01x faster                                                |
| scimark_fft               | 350 ms                                                                 | 346 ms: 1.01x faster                                                 |
| xml_etree_generate        | 85.4 ms                                                                | 84.7 ms: 1.01x faster                                                |
| deepcopy_memo             | 30.9 us                                                                | 30.7 us: 1.01x faster                                                |
| deepcopy                  | 260 us                                                                 | 258 us: 1.01x faster                                                 |
| logging_silent            | 108 ns                                                                 | 107 ns: 1.01x faster                                                 |
| xml_etree_process         | 60.0 ms                                                                | 59.6 ms: 1.01x faster                                                |
| xml_etree_iterparse       | 97.6 ms                                                                | 97.0 ms: 1.01x faster                                                |
| deepcopy_reduce           | 2.70 us                                                                | 2.68 us: 1.01x faster                                                |
| genshi_xml                | 49.5 ms                                                                | 49.3 ms: 1.01x faster                                                |
| sqlalchemy_imperative     | 16.5 ms                                                                | 16.4 ms: 1.00x faster                                                |
| pprint_pformat            | 1.49 sec                                                               | 1.49 sec: 1.00x faster                                               |
| xml_etree_parse           | 140 ms                                                                 | 139 ms: 1.00x faster                                                 |
| docutils                  | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                               |
| create_gc_cycles          | 2.47 ms                                                                | 2.46 ms: 1.00x faster                                                |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                |
| meteor_contest            | 107 ms                                                                 | 107 ms: 1.00x slower                                                 |
| python_startup_no_site    | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                |
| sqlglot_normalize         | 105 ms                                                                 | 105 ms: 1.00x slower                                                 |
| raytrace                  | 273 ms                                                                 | 274 ms: 1.00x slower                                                 |
| bench_thread_pool         | 861 us                                                                 | 864 us: 1.00x slower                                                 |
| pidigits                  | 186 ms                                                                 | 187 ms: 1.00x slower                                                 |
| dulwich_log               | 64.3 ms                                                                | 64.6 ms: 1.00x slower                                                |
| generators                | 27.6 ms                                                                | 27.7 ms: 1.00x slower                                                |
| coroutines                | 23.6 ms                                                                | 23.7 ms: 1.00x slower                                                |
| scimark_sparse_mat_mult   | 4.67 ms                                                                | 4.69 ms: 1.01x slower                                                |
| scimark_sor               | 122 ms                                                                 | 123 ms: 1.01x slower                                                 |
| async_tree_memoization    | 324 ms                                                                 | 326 ms: 1.01x slower                                                 |
| pyflate                   | 472 ms                                                                 | 476 ms: 1.01x slower                                                 |
| deltablue                 | 3.21 ms                                                                | 3.23 ms: 1.01x slower                                                |
| subparsers                | 20.5 ms                                                                | 20.7 ms: 1.01x slower                                                |
| sympy_str                 | 266 ms                                                                 | 268 ms: 1.01x slower                                                 |
| pathlib                   | 15.7 ms                                                                | 15.9 ms: 1.01x slower                                                |
| sympy_integrate           | 19.7 ms                                                                | 19.9 ms: 1.01x slower                                                |
| async_tree_memoization_tg | 313 ms                                                                 | 316 ms: 1.01x slower                                                 |
| comprehensions            | 16.7 us                                                                | 16.9 us: 1.01x slower                                                |
| richards_super            | 50.2 ms                                                                | 50.7 ms: 1.01x slower                                                |
| richards                  | 44.1 ms                                                                | 44.6 ms: 1.01x slower                                                |
| sympy_expand              | 451 ms                                                                 | 456 ms: 1.01x slower                                                 |
| json_loads                | 28.6 us                                                                | 29.0 us: 1.01x slower                                                |
| sqlglot_transpile         | 1.56 ms                                                                | 1.58 ms: 1.01x slower                                                |
| 2to3                      | 254 ms                                                                 | 257 ms: 1.01x slower                                                 |
| regex_dna                 | 210 ms                                                                 | 212 ms: 1.01x slower                                                 |
| scimark_lu                | 116 ms                                                                 | 118 ms: 1.01x slower                                                 |
| sqlglot_parse             | 1.26 ms                                                                | 1.28 ms: 1.02x slower                                                |
| regex_compile             | 127 ms                                                                 | 129 ms: 1.02x slower                                                 |
| scimark_monte_carlo       | 67.3 ms                                                                | 68.4 ms: 1.02x slower                                                |
| connected_components      | 436 ms                                                                 | 443 ms: 1.02x slower                                                 |
| unpickle_pure_python      | 218 us                                                                 | 222 us: 1.02x slower                                                 |
| json_dumps                | 11.6 ms                                                                | 11.8 ms: 1.02x slower                                                |
| async_tree_none_tg        | 253 ms                                                                 | 258 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 4.49 sec                                                               | 4.58 sec: 1.02x slower                                               |
| async_generators          | 378 ms                                                                 | 385 ms: 1.02x slower                                                 |
| go                        | 117 ms                                                                 | 120 ms: 1.02x slower                                                 |
| fannkuch                  | 408 ms                                                                 | 421 ms: 1.03x slower                                                 |
| nqueens                   | 81.1 ms                                                                | 83.8 ms: 1.03x slower                                                |
| chaos                     | 58.3 ms                                                                | 60.5 ms: 1.04x slower                                                |
| mako                      | 10.8 ms                                                                | 11.4 ms: 1.05x slower                                                |
| hexiom                    | 6.23 ms                                                                | 6.59 ms: 1.06x slower                                                |
| crypto_pyaes              | 71.7 ms                                                                | 76.9 ms: 1.07x slower                                                |
| tomli_loads               | 1.93 sec                                                               | 2.08 sec: 1.07x slower                                               |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (27): json, sphinx, genshi_text, html5lib, logging_simple, sqlglot_optimize, regex_v8, shortest_path, typing_runtime_protocols, thrift, pprint_safe_repr, sympy_sum, async_tree_io_tg, many_optionals, mdp, bench_mp_pool, sqlalchemy_declarative, asyncio_websockets, pylint, sqlite_synth, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, k_core, float, async_tree_io, nbody

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x