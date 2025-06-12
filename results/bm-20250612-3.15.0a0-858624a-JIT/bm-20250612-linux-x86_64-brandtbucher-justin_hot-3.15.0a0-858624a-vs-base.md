# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 262 ms                                                | 260 ms: 1.01x faster                                              |
| docutils       | 2.66 sec                                              | 2.65 sec: 1.01x faster                                            |
| Geometric mean | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| async_generators | 434 ms                                                | 431 ms: 1.01x faster                                              |
| Geometric mean   | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (10): async_tree_io_tg, async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 94.6 ms                                               | 93.5 ms: 1.01x faster                                             |
| float          | 65.9 ms                                               | 65.2 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                               | 23.7 ms: 1.04x slower                                             |
| regex_effbot   | 3.25 ms                                               | 3.45 ms: 1.06x slower                                             |
| regex_dna      | 199 ms                                                | 219 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                 | 1.05x slower                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 201 us                                                | 194 us: 1.04x faster                                              |
| xml_etree_process    | 56.3 ms                                               | 54.7 ms: 1.03x faster                                             |
| xml_etree_generate   | 81.0 ms                                               | 79.0 ms: 1.03x faster                                             |
| tomli_loads          | 1.90 sec                                              | 1.87 sec: 1.02x faster                                            |
| json_loads           | 28.5 us                                               | 28.1 us: 1.02x faster                                             |
| pickle_pure_python   | 326 us                                                | 321 us: 1.01x faster                                              |
| json_dumps           | 11.2 ms                                               | 11.3 ms: 1.00x slower                                             |
| Geometric mean       | (ref)                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                               | 6.93 ms: 1.00x faster                                             |
| python_startup         | 12.2 ms                                               | 12.2 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                 | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 33.1 ms                                               | 32.4 ms: 1.02x faster                                             |
| genshi_xml      | 50.6 ms                                               | 49.9 ms: 1.01x faster                                             |
| mako            | 10.7 ms                                               | 10.6 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|--------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| go                       | 124 ms                                                | 117 ms: 1.06x faster                                              |
| pprint_pformat           | 1.69 sec                                              | 1.61 sec: 1.05x faster                                            |
| richards                 | 34.3 ms                                               | 32.9 ms: 1.04x faster                                             |
| deepcopy_reduce          | 2.80 us                                               | 2.69 us: 1.04x faster                                             |
| unpickle_pure_python     | 201 us                                                | 194 us: 1.04x faster                                              |
| fannkuch                 | 418 ms                                                | 404 ms: 1.03x faster                                              |
| comprehensions           | 17.0 us                                               | 16.5 us: 1.03x faster                                             |
| richards_super           | 39.6 ms                                               | 38.3 ms: 1.03x faster                                             |
| scimark_monte_carlo      | 67.3 ms                                               | 65.3 ms: 1.03x faster                                             |
| xml_etree_process        | 56.3 ms                                               | 54.7 ms: 1.03x faster                                             |
| xml_etree_generate       | 81.0 ms                                               | 79.0 ms: 1.03x faster                                             |
| crypto_pyaes             | 76.8 ms                                               | 74.9 ms: 1.03x faster                                             |
| typing_runtime_protocols | 172 us                                                | 168 us: 1.03x faster                                              |
| scimark_sor              | 124 ms                                                | 121 ms: 1.02x faster                                              |
| deltablue                | 3.13 ms                                               | 3.06 ms: 1.02x faster                                             |
| django_template          | 33.1 ms                                               | 32.4 ms: 1.02x faster                                             |
| hexiom                   | 6.41 ms                                               | 6.27 ms: 1.02x faster                                             |
| raytrace                 | 280 ms                                                | 274 ms: 1.02x faster                                              |
| pprint_safe_repr         | 815 ms                                                | 800 ms: 1.02x faster                                              |
| pyflate                  | 424 ms                                                | 416 ms: 1.02x faster                                              |
| chaos                    | 63.7 ms                                               | 62.6 ms: 1.02x faster                                             |
| tomli_loads              | 1.90 sec                                              | 1.87 sec: 1.02x faster                                            |
| json                     | 5.30 ms                                               | 5.21 ms: 1.02x faster                                             |
| sqlglot_v2_parse         | 1.28 ms                                               | 1.26 ms: 1.02x faster                                             |
| json_loads               | 28.5 us                                               | 28.1 us: 1.02x faster                                             |
| genshi_xml               | 50.6 ms                                               | 49.9 ms: 1.01x faster                                             |
| pathlib                  | 17.2 ms                                               | 17.0 ms: 1.01x faster                                             |
| sqlglot_v2_transpile     | 1.60 ms                                               | 1.58 ms: 1.01x faster                                             |
| bpe_tokeniser            | 4.43 sec                                              | 4.37 sec: 1.01x faster                                            |
| pickle_pure_python       | 326 us                                                | 321 us: 1.01x faster                                              |
| sqlglot_v2_normalize     | 108 ms                                                | 106 ms: 1.01x faster                                              |
| nbody                    | 94.6 ms                                               | 93.5 ms: 1.01x faster                                             |
| sympy_integrate          | 19.5 ms                                               | 19.3 ms: 1.01x faster                                             |
| sympy_sum                | 151 ms                                                | 149 ms: 1.01x faster                                              |
| mdp                      | 1.25 sec                                              | 1.24 sec: 1.01x faster                                            |
| float                    | 65.9 ms                                               | 65.2 ms: 1.01x faster                                             |
| dulwich_log              | 62.1 ms                                               | 61.5 ms: 1.01x faster                                             |
| mako                     | 10.7 ms                                               | 10.6 ms: 1.01x faster                                             |
| nqueens                  | 83.6 ms                                               | 82.9 ms: 1.01x faster                                             |
| subparsers               | 23.8 ms                                               | 23.6 ms: 1.01x faster                                             |
| async_generators         | 434 ms                                                | 431 ms: 1.01x faster                                              |
| logging_format           | 6.84 us                                               | 6.79 us: 1.01x faster                                             |
| generators               | 30.6 ms                                               | 30.4 ms: 1.01x faster                                             |
| many_optionals           | 986 us                                                | 979 us: 1.01x faster                                              |
| docutils                 | 2.66 sec                                              | 2.65 sec: 1.01x faster                                            |
| 2to3                     | 262 ms                                                | 260 ms: 1.01x faster                                              |
| sqlglot_v2_optimize      | 53.2 ms                                               | 52.9 ms: 1.01x faster                                             |
| scimark_fft              | 332 ms                                                | 330 ms: 1.01x faster                                              |
| sympy_str                | 273 ms                                                | 272 ms: 1.00x faster                                              |
| python_startup_no_site   | 6.96 ms                                               | 6.93 ms: 1.00x faster                                             |
| create_gc_cycles         | 2.60 ms                                               | 2.59 ms: 1.00x faster                                             |
| deepcopy_memo            | 29.7 us                                               | 29.6 us: 1.00x faster                                             |
| shortest_path            | 496 ms                                                | 495 ms: 1.00x faster                                              |
| python_startup           | 12.2 ms                                               | 12.2 ms: 1.00x faster                                             |
| sympy_expand             | 468 ms                                                | 469 ms: 1.00x slower                                              |
| json_dumps               | 11.2 ms                                               | 11.3 ms: 1.00x slower                                             |
| connected_components     | 456 ms                                                | 459 ms: 1.01x slower                                              |
| spectral_norm            | 102 ms                                                | 103 ms: 1.01x slower                                              |
| sqlite_synth             | 2.79 us                                               | 2.82 us: 1.01x slower                                             |
| logging_simple           | 6.16 us                                               | 6.24 us: 1.01x slower                                             |
| scimark_lu               | 120 ms                                                | 121 ms: 1.01x slower                                              |
| gc_traversal             | 5.01 ms                                               | 5.14 ms: 1.03x slower                                             |
| pycparser                | 1.14 sec                                              | 1.17 sec: 1.03x slower                                            |
| regex_v8                 | 22.6 ms                                               | 23.7 ms: 1.04x slower                                             |
| regex_effbot             | 3.25 ms                                               | 3.45 ms: 1.06x slower                                             |
| regex_dna                | 199 ms                                                | 219 ms: 1.10x slower                                              |
| Geometric mean           | (ref)                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (26): telco, k_core, async_tree_io_tg, async_tree_none_tg, coroutines, pylint, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, genshi_text, deepcopy, sphinx, asyncio_websockets, logging_silent, pidigits, async_tree_memoization_tg, meteor_contest, regex_compile, xml_etree_iterparse, async_tree_memoization, coverage, html5lib, xml_etree_parse, thrift

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x