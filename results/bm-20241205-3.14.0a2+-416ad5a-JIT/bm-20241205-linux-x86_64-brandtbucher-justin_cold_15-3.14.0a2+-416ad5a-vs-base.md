# Results vs. base

- fork: brandtbucher
- ref: justin_cold_15
- machine: linux-x86_64
- commit hash: 416ad5a
- commit date: 2024-12-05
- overall geometric mean: 1.001x slower
- HPT reliability: 71.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 260 ms: 1.01x slower                                                   |
| docutils       | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                 |
| html5lib       | 64.2 ms                                                                | 65.3 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                  |
| async_generators          | 445 ms                                                                 | 448 ms: 1.01x slower                                                   |
| async_tree_memoization_tg | 313 ms                                                                 | 316 ms: 1.01x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 624 ms: 1.01x slower                                                   |
| async_tree_memoization    | 340 ms                                                                 | 345 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 500 ms: 1.02x slower                                                   |
| async_tree_none_tg        | 249 ms                                                                 | 255 ms: 1.02x slower                                                   |
| async_tree_none           | 267 ms                                                                 | 274 ms: 1.03x slower                                                   |
| async_tree_io_tg          | 600 ms                                                                 | 618 ms: 1.03x slower                                                   |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 82.8 ms                                                                | 81.4 ms: 1.02x faster                                                  |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                  |
| regex_effbot   | 3.20 ms                                                                | 3.24 ms: 1.01x slower                                                  |
| regex_dna      | 212 ms                                                                 | 220 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate  | 78.3 ms                                                                | 77.7 ms: 1.01x faster                                                  |
| json_loads          | 26.2 us                                                                | 26.1 us: 1.00x faster                                                  |
| xml_etree_iterparse | 95.2 ms                                                                | 94.9 ms: 1.00x faster                                                  |
| tomli_loads         | 1.91 sec                                                               | 1.93 sec: 1.01x slower                                                 |
| json_dumps          | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (4): xml_etree_process, pickle_pure_python, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| python_startup_no_site | 7.04 ms                                                                | 7.05 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.0 ms                                                                | 33.2 ms: 1.02x faster                                                  |
| genshi_text     | 23.9 ms                                                                | 24.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sparse_mat_mult   | 4.86 ms                                                                | 4.64 ms: 1.05x faster                                                  |
| gc_traversal              | 5.01 ms                                                                | 4.81 ms: 1.04x faster                                                  |
| scimark_lu                | 115 ms                                                                 | 110 ms: 1.04x faster                                                   |
| meteor_contest            | 110 ms                                                                 | 107 ms: 1.03x faster                                                   |
| django_template           | 34.0 ms                                                                | 33.2 ms: 1.02x faster                                                  |
| sympy_str                 | 282 ms                                                                 | 276 ms: 1.02x faster                                                   |
| coverage                  | 84.9 ms                                                                | 83.3 ms: 1.02x faster                                                  |
| hexiom                    | 7.12 ms                                                                | 7.00 ms: 1.02x faster                                                  |
| sympy_sum                 | 156 ms                                                                 | 154 ms: 1.02x faster                                                   |
| nbody                     | 82.8 ms                                                                | 81.4 ms: 1.02x faster                                                  |
| bpe_tokeniser             | 4.41 sec                                                               | 4.36 sec: 1.01x faster                                                 |
| sympy_expand              | 475 ms                                                                 | 469 ms: 1.01x faster                                                   |
| connected_components      | 438 ms                                                                 | 434 ms: 1.01x faster                                                   |
| sqlite_synth              | 2.81 us                                                                | 2.78 us: 1.01x faster                                                  |
| coroutines                | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                  |
| docutils                  | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                 |
| comprehensions            | 17.3 us                                                                | 17.2 us: 1.01x faster                                                  |
| xml_etree_generate        | 78.3 ms                                                                | 77.7 ms: 1.01x faster                                                  |
| many_optionals            | 977 us                                                                 | 970 us: 1.01x faster                                                   |
| sympy_integrate           | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                  |
| richards_super            | 43.7 ms                                                                | 43.4 ms: 1.01x faster                                                  |
| sqlglot_optimize          | 55.6 ms                                                                | 55.3 ms: 1.00x faster                                                  |
| shortest_path             | 481 ms                                                                 | 480 ms: 1.00x faster                                                   |
| json_loads                | 26.2 us                                                                | 26.1 us: 1.00x faster                                                  |
| xml_etree_iterparse       | 95.2 ms                                                                | 94.9 ms: 1.00x faster                                                  |
| regex_v8                  | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                  |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| python_startup_no_site    | 7.04 ms                                                                | 7.05 ms: 1.00x slower                                                  |
| pidigits                  | 186 ms                                                                 | 187 ms: 1.00x slower                                                   |
| sqlglot_parse             | 1.32 ms                                                                | 1.32 ms: 1.01x slower                                                  |
| bench_thread_pool         | 872 us                                                                 | 877 us: 1.01x slower                                                   |
| deltablue                 | 3.14 ms                                                                | 3.16 ms: 1.01x slower                                                  |
| genshi_text               | 23.9 ms                                                                | 24.1 ms: 1.01x slower                                                  |
| async_generators          | 445 ms                                                                 | 448 ms: 1.01x slower                                                   |
| 2to3                      | 258 ms                                                                 | 260 ms: 1.01x slower                                                   |
| go                        | 132 ms                                                                 | 134 ms: 1.01x slower                                                   |
| tomli_loads               | 1.91 sec                                                               | 1.93 sec: 1.01x slower                                                 |
| async_tree_memoization_tg | 313 ms                                                                 | 316 ms: 1.01x slower                                                   |
| deepcopy                  | 269 us                                                                 | 272 us: 1.01x slower                                                   |
| sqlalchemy_imperative     | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                                  |
| async_tree_io             | 616 ms                                                                 | 624 ms: 1.01x slower                                                   |
| regex_effbot              | 3.20 ms                                                                | 3.24 ms: 1.01x slower                                                  |
| json_dumps                | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                  |
| async_tree_memoization    | 340 ms                                                                 | 345 ms: 1.02x slower                                                   |
| html5lib                  | 64.2 ms                                                                | 65.3 ms: 1.02x slower                                                  |
| pyflate                   | 449 ms                                                                 | 457 ms: 1.02x slower                                                   |
| logging_format            | 6.30 us                                                                | 6.41 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 500 ms: 1.02x slower                                                   |
| thrift                    | 768 us                                                                 | 783 us: 1.02x slower                                                   |
| logging_simple            | 5.74 us                                                                | 5.86 us: 1.02x slower                                                  |
| async_tree_none_tg        | 249 ms                                                                 | 255 ms: 1.02x slower                                                   |
| pprint_safe_repr          | 718 ms                                                                 | 735 ms: 1.02x slower                                                   |
| async_tree_none           | 267 ms                                                                 | 274 ms: 1.03x slower                                                   |
| logging_silent            | 102 ns                                                                 | 104 ns: 1.03x slower                                                   |
| async_tree_io_tg          | 600 ms                                                                 | 618 ms: 1.03x slower                                                   |
| mdp                       | 2.58 sec                                                               | 2.67 sec: 1.03x slower                                                 |
| regex_dna                 | 212 ms                                                                 | 220 ms: 1.04x slower                                                   |
| pprint_pformat            | 1.46 sec                                                               | 1.53 sec: 1.05x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (39): djangocms, pylint, deepcopy_reduce, genshi_xml, sphinx, pycparser, subparsers, sqlglot_normalize, spectral_norm, dulwich_log, sqlglot_transpile, generators, typing_runtime_protocols, deepcopy_memo, xml_etree_process, mako, pathlib, pickle_pure_python, xml_etree_parse, fannkuch, create_gc_cycles, telco, regex_compile, asyncio_websockets, crypto_pyaes, float, scimark_fft, k_core, raytrace, sqlalchemy_declarative, scimark_monte_carlo, chaos, async_tree_cpu_io_mixed_tg, richards, bench_mp_pool, scimark_sor, json, nqueens, unpickle_pure_python

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 71.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x