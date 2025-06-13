# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.000x slower
- HPT reliability: 69.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 319 ms                                                                | 315 ms: 1.01x faster                                                          |
| coroutines                 | 26.1 ms                                                               | 25.9 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 500 ms                                                                | 496 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 491 ms                                                                | 488 ms: 1.01x faster                                                          |
| async_generators           | 431 ms                                                                | 434 ms: 1.01x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                               | 88.2 ms: 1.03x faster                                                         |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                          |
| float          | 65.3 ms                                                               | 65.9 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 196 ms: 1.06x faster                                                          |
| regex_effbot   | 3.31 ms                                                               | 3.22 ms: 1.03x faster                                                         |
| regex_v8       | 23.8 ms                                                               | 23.4 ms: 1.02x faster                                                         |
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 11.3 ms                                                               | 11.0 ms: 1.04x faster                                                         |
| pickle_pure_python   | 330 us                                                                | 325 us: 1.02x faster                                                          |
| json_loads           | 28.6 us                                                               | 28.3 us: 1.01x faster                                                         |
| unpickle_pure_python | 202 us                                                                | 203 us: 1.01x slower                                                          |
| tomli_loads          | 1.90 sec                                                              | 1.91 sec: 1.01x slower                                                        |
| xml_etree_iterparse  | 98.7 ms                                                               | 99.4 ms: 1.01x slower                                                         |
| xml_etree_process    | 55.8 ms                                                               | 56.4 ms: 1.01x slower                                                         |
| xml_etree_generate   | 79.8 ms                                                               | 81.9 ms: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.1 ms                                                               | 12.2 ms: 1.00x slower                                                         |
| python_startup_no_site | 6.91 ms                                                               | 6.93 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 51.1 ms                                                               | 49.7 ms: 1.03x faster                                                         |
| django_template | 33.0 ms                                                               | 32.7 ms: 1.01x faster                                                         |
| genshi_text     | 21.2 ms                                                               | 21.4 ms: 1.01x slower                                                         |
| mako            | 10.7 ms                                                               | 11.0 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna                  | 208 ms                                                                | 196 ms: 1.06x faster                                                          |
| json_dumps                 | 11.3 ms                                                               | 11.0 ms: 1.04x faster                                                         |
| genshi_xml                 | 51.1 ms                                                               | 49.7 ms: 1.03x faster                                                         |
| regex_effbot               | 3.31 ms                                                               | 3.22 ms: 1.03x faster                                                         |
| nbody                      | 90.7 ms                                                               | 88.2 ms: 1.03x faster                                                         |
| json                       | 5.28 ms                                                               | 5.18 ms: 1.02x faster                                                         |
| generators                 | 30.7 ms                                                               | 30.2 ms: 1.02x faster                                                         |
| regex_v8                   | 23.8 ms                                                               | 23.4 ms: 1.02x faster                                                         |
| pycparser                  | 1.18 sec                                                              | 1.16 sec: 1.02x faster                                                        |
| pickle_pure_python         | 330 us                                                                | 325 us: 1.02x faster                                                          |
| typing_runtime_protocols   | 171 us                                                                | 169 us: 1.01x faster                                                          |
| sympy_sum                  | 151 ms                                                                | 149 ms: 1.01x faster                                                          |
| coverage                   | 430 ms                                                                | 424 ms: 1.01x faster                                                          |
| subparsers                 | 24.3 ms                                                               | 23.9 ms: 1.01x faster                                                         |
| dulwich_log                | 62.2 ms                                                               | 61.4 ms: 1.01x faster                                                         |
| async_tree_memoization     | 319 ms                                                                | 315 ms: 1.01x faster                                                          |
| sqlglot_v2_normalize       | 108 ms                                                                | 106 ms: 1.01x faster                                                          |
| bpe_tokeniser              | 4.47 sec                                                              | 4.43 sec: 1.01x faster                                                        |
| sqlite_synth               | 2.82 us                                                               | 2.79 us: 1.01x faster                                                         |
| sympy_integrate            | 19.4 ms                                                               | 19.3 ms: 1.01x faster                                                         |
| scimark_sor                | 122 ms                                                                | 121 ms: 1.01x faster                                                          |
| django_template            | 33.0 ms                                                               | 32.7 ms: 1.01x faster                                                         |
| pathlib                    | 16.9 ms                                                               | 16.7 ms: 1.01x faster                                                         |
| coroutines                 | 26.1 ms                                                               | 25.9 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 500 ms                                                                | 496 ms: 1.01x faster                                                          |
| json_loads                 | 28.6 us                                                               | 28.3 us: 1.01x faster                                                         |
| logging_simple             | 6.23 us                                                               | 6.18 us: 1.01x faster                                                         |
| sqlglot_v2_transpile       | 1.61 ms                                                               | 1.59 ms: 1.01x faster                                                         |
| many_optionals             | 989 us                                                                | 981 us: 1.01x faster                                                          |
| docutils                   | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                        |
| sympy_str                  | 274 ms                                                                | 272 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 491 ms                                                                | 488 ms: 1.01x faster                                                          |
| sympy_expand               | 470 ms                                                                | 468 ms: 1.01x faster                                                          |
| deltablue                  | 3.16 ms                                                               | 3.14 ms: 1.00x faster                                                         |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.9 ms: 1.00x faster                                                         |
| create_gc_cycles           | 2.59 ms                                                               | 2.59 ms: 1.00x faster                                                         |
| python_startup             | 12.1 ms                                                               | 12.2 ms: 1.00x slower                                                         |
| deepcopy_memo              | 29.8 us                                                               | 29.9 us: 1.00x slower                                                         |
| python_startup_no_site     | 6.91 ms                                                               | 6.93 ms: 1.00x slower                                                         |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                          |
| chaos                      | 62.3 ms                                                               | 62.6 ms: 1.00x slower                                                         |
| unpickle_pure_python       | 202 us                                                                | 203 us: 1.01x slower                                                          |
| regex_compile              | 128 ms                                                                | 129 ms: 1.01x slower                                                          |
| crypto_pyaes               | 76.0 ms                                                               | 76.5 ms: 1.01x slower                                                         |
| genshi_text                | 21.2 ms                                                               | 21.4 ms: 1.01x slower                                                         |
| tomli_loads                | 1.90 sec                                                              | 1.91 sec: 1.01x slower                                                        |
| xml_etree_iterparse        | 98.7 ms                                                               | 99.4 ms: 1.01x slower                                                         |
| async_generators           | 431 ms                                                                | 434 ms: 1.01x slower                                                          |
| float                      | 65.3 ms                                                               | 65.9 ms: 1.01x slower                                                         |
| pyflate                    | 421 ms                                                                | 425 ms: 1.01x slower                                                          |
| xml_etree_process          | 55.8 ms                                                               | 56.4 ms: 1.01x slower                                                         |
| nqueens                    | 83.3 ms                                                               | 84.2 ms: 1.01x slower                                                         |
| shortest_path              | 491 ms                                                                | 497 ms: 1.01x slower                                                          |
| meteor_contest             | 106 ms                                                                | 108 ms: 1.01x slower                                                          |
| scimark_fft                | 332 ms                                                                | 336 ms: 1.01x slower                                                          |
| go                         | 123 ms                                                                | 125 ms: 1.01x slower                                                          |
| fannkuch                   | 412 ms                                                                | 418 ms: 1.02x slower                                                          |
| hexiom                     | 6.42 ms                                                               | 6.52 ms: 1.02x slower                                                         |
| logging_silent             | 472 ns                                                                | 480 ns: 1.02x slower                                                          |
| comprehensions             | 17.2 us                                                               | 17.5 us: 1.02x slower                                                         |
| telco                      | 7.75 ms                                                               | 7.91 ms: 1.02x slower                                                         |
| connected_components       | 457 ms                                                                | 467 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 2.71 us                                                               | 2.77 us: 1.02x slower                                                         |
| mako                       | 10.7 ms                                                               | 11.0 ms: 1.02x slower                                                         |
| xml_etree_generate         | 79.8 ms                                                               | 81.9 ms: 1.03x slower                                                         |
| richards                   | 34.1 ms                                                               | 35.0 ms: 1.03x slower                                                         |
| pprint_safe_repr           | 825 ms                                                                | 850 ms: 1.03x slower                                                          |
| gc_traversal               | 4.91 ms                                                               | 5.07 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 4.99 ms                                                               | 5.23 ms: 1.05x slower                                                         |
| pprint_pformat             | 1.69 sec                                                              | 1.78 sec: 1.05x slower                                                        |
| spectral_norm              | 102 ms                                                                | 109 ms: 1.07x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (21): sphinx, async_tree_memoization_tg, pylint, html5lib, scimark_lu, mdp, k_core, logging_format, scimark_monte_carlo, async_tree_none, sqlglot_v2_parse, deepcopy, 2to3, asyncio_websockets, async_tree_none_tg, thrift, raytrace, async_tree_io, async_tree_io_tg, richards_super, xml_etree_parse

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 69.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x