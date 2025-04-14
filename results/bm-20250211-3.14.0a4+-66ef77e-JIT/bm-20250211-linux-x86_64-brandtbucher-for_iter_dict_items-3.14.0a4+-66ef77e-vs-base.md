# Results vs. base

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 66ef77e
- commit date: 2025-02-11
- overall geometric mean: 1.002x slower
- HPT reliability: 71.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                               | 2.67 sec: 1.00x slower                                                      |
| html5lib       | 60.8 ms                                                                | 61.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 632 ms                                                                 | 614 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                 | 481 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 501 ms                                                                 | 493 ms: 1.02x faster                                                        |
| async_tree_io              | 629 ms                                                                 | 620 ms: 1.01x faster                                                        |
| coroutines                 | 23.6 ms                                                                | 23.4 ms: 1.01x faster                                                       |
| async_tree_memoization     | 329 ms                                                                 | 326 ms: 1.01x faster                                                        |
| async_tree_none_tg         | 260 ms                                                                 | 258 ms: 1.01x faster                                                        |
| async_generators           | 409 ms                                                                 | 412 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                        |
| nbody          | 95.5 ms                                                                | 97.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                | 23.9 ms: 1.00x slower                                                       |
| regex_effbot   | 3.18 ms                                                                | 3.20 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 201 us                                                                 | 198 us: 1.01x faster                                                        |
| json_dumps           | 12.0 ms                                                                | 11.9 ms: 1.01x faster                                                       |
| json_loads           | 28.9 us                                                                | 28.6 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 95.4 ms                                                                | 95.8 ms: 1.00x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (5): xml_etree_generate, pickle_pure_python, tomli_loads, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                                       |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 31.7 ms: 1.01x faster                                                       |
| mako            | 9.88 ms                                                                | 9.97 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| logging_format             | 6.33 us                                                                | 6.10 us: 1.04x faster                                                       |
| logging_simple             | 5.69 us                                                                | 5.52 us: 1.03x faster                                                       |
| pprint_pformat             | 1.57 sec                                                               | 1.53 sec: 1.03x faster                                                      |
| async_tree_io_tg           | 632 ms                                                                 | 614 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                 | 481 ms: 1.02x faster                                                        |
| thrift                     | 773 us                                                                 | 759 us: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.46 ms                                                                | 4.39 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 501 ms                                                                 | 493 ms: 1.02x faster                                                        |
| richards_super             | 50.9 ms                                                                | 50.1 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 201 us                                                                 | 198 us: 1.01x faster                                                        |
| async_tree_io              | 629 ms                                                                 | 620 ms: 1.01x faster                                                        |
| json                       | 5.20 ms                                                                | 5.13 ms: 1.01x faster                                                       |
| json_dumps                 | 12.0 ms                                                                | 11.9 ms: 1.01x faster                                                       |
| coroutines                 | 23.6 ms                                                                | 23.4 ms: 1.01x faster                                                       |
| async_tree_memoization     | 329 ms                                                                 | 326 ms: 1.01x faster                                                        |
| json_loads                 | 28.9 us                                                                | 28.6 us: 1.01x faster                                                       |
| telco                      | 7.67 ms                                                                | 7.61 ms: 1.01x faster                                                       |
| async_tree_none_tg         | 260 ms                                                                 | 258 ms: 1.01x faster                                                        |
| richards                   | 44.4 ms                                                                | 44.0 ms: 1.01x faster                                                       |
| generators                 | 28.1 ms                                                                | 27.9 ms: 1.01x faster                                                       |
| scimark_fft                | 313 ms                                                                 | 311 ms: 1.01x faster                                                        |
| dulwich_log                | 66.5 ms                                                                | 66.0 ms: 1.01x faster                                                       |
| django_template            | 31.8 ms                                                                | 31.7 ms: 1.01x faster                                                       |
| many_optionals             | 957 us                                                                 | 952 us: 1.01x faster                                                        |
| crypto_pyaes               | 69.4 ms                                                                | 69.1 ms: 1.01x faster                                                       |
| mdp                        | 2.57 sec                                                               | 2.56 sec: 1.01x faster                                                      |
| fannkuch                   | 395 ms                                                                 | 394 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                        |
| create_gc_cycles           | 2.47 ms                                                                | 2.47 ms: 1.00x slower                                                       |
| sqlalchemy_declarative     | 130 ms                                                                 | 131 ms: 1.00x slower                                                        |
| shortest_path              | 482 ms                                                                 | 484 ms: 1.00x slower                                                        |
| xml_etree_iterparse        | 95.4 ms                                                                | 95.8 ms: 1.00x slower                                                       |
| regex_v8                   | 23.8 ms                                                                | 23.9 ms: 1.00x slower                                                       |
| docutils                   | 2.66 sec                                                               | 2.67 sec: 1.00x slower                                                      |
| regex_effbot               | 3.18 ms                                                                | 3.20 ms: 1.00x slower                                                       |
| python_startup_no_site     | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                                       |
| go                         | 129 ms                                                                 | 129 ms: 1.01x slower                                                        |
| spectral_norm              | 94.4 ms                                                                | 94.9 ms: 1.01x slower                                                       |
| logging_silent             | 106 ns                                                                 | 107 ns: 1.01x slower                                                        |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                       |
| bench_mp_pool              | 80.9 ms                                                                | 81.4 ms: 1.01x slower                                                       |
| pathlib                    | 16.3 ms                                                                | 16.4 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 161 us                                                                 | 162 us: 1.01x slower                                                        |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.70 us                                                                | 2.72 us: 1.01x slower                                                       |
| async_generators           | 409 ms                                                                 | 412 ms: 1.01x slower                                                        |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                       |
| mako                       | 9.88 ms                                                                | 9.97 ms: 1.01x slower                                                       |
| scimark_lu                 | 115 ms                                                                 | 116 ms: 1.01x slower                                                        |
| raytrace                   | 274 ms                                                                 | 277 ms: 1.01x slower                                                        |
| html5lib                   | 60.8 ms                                                                | 61.5 ms: 1.01x slower                                                       |
| hexiom                     | 6.84 ms                                                                | 6.93 ms: 1.01x slower                                                       |
| comprehensions             | 17.2 us                                                                | 17.4 us: 1.01x slower                                                       |
| deepcopy_memo              | 29.9 us                                                                | 30.3 us: 1.01x slower                                                       |
| deepcopy_reduce            | 2.66 us                                                                | 2.70 us: 1.01x slower                                                       |
| deepcopy                   | 257 us                                                                 | 261 us: 1.02x slower                                                        |
| scimark_sor                | 117 ms                                                                 | 120 ms: 1.02x slower                                                        |
| nbody                      | 95.5 ms                                                                | 97.4 ms: 1.02x slower                                                       |
| sympy_str                  | 275 ms                                                                 | 281 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.28 ms                                                                | 1.31 ms: 1.02x slower                                                       |
| deltablue                  | 3.34 ms                                                                | 3.43 ms: 1.03x slower                                                       |
| sympy_expand               | 468 ms                                                                 | 482 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                                | 1.63 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 53.4 ms                                                                | 55.4 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 106 ms                                                                 | 110 ms: 1.04x slower                                                        |
| gc_traversal               | 4.80 ms                                                                | 4.99 ms: 1.04x slower                                                       |
| pyflate                    | 444 ms                                                                 | 462 ms: 1.04x slower                                                        |
| sympy_sum                  | 151 ms                                                                 | 157 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (28): pycparser, async_tree_memoization_tg, nqueens, async_tree_none, subparsers, scimark_monte_carlo, xml_etree_generate, pickle_pure_python, asyncio_websockets, regex_dna, connected_components, tomli_loads, pylint, regex_compile, xml_etree_process, coverage, bpe_tokeniser, 2to3, bench_thread_pool, genshi_xml, chaos, float, sympy_integrate, xml_etree_parse, genshi_text, pprint_safe_repr, sphinx, k_core

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 71.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x