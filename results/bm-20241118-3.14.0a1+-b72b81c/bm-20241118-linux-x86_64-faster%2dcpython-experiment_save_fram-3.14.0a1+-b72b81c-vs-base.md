# Results vs. base

- fork: faster-cpython
- ref: experiment_save_fram
- machine: linux-x86_64
- commit hash: b72b81c
- commit date: 2024-11-18
- overall geometric mean: 1.001x slower
- HPT reliability: 86.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 256 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines                 | 24.0 ms                                                                | 23.4 ms: 1.03x faster                                                            |
| async_generators           | 429 ms                                                                 | 434 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                 | 575 ms: 1.02x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.2 ms                                                                | 96.7 ms: 1.01x faster                                                            |
| pidigits       | 188 ms                                                                 | 187 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                                | 3.58 ms: 1.07x faster                                                            |
| regex_dna      | 225 ms                                                                 | 219 ms: 1.03x faster                                                             |
| regex_v8       | 24.6 ms                                                                | 24.2 ms: 1.01x faster                                                            |
| regex_compile  | 130 ms                                                                 | 130 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python | 329 us                                                                 | 326 us: 1.01x faster                                                             |
| json_loads         | 26.8 us                                                                | 27.1 us: 1.01x slower                                                            |
| json_dumps         | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                            |
| xml_etree_generate | 85.5 ms                                                                | 86.8 ms: 1.01x slower                                                            |
| xml_etree_process  | 59.2 ms                                                                | 60.1 ms: 1.02x slower                                                            |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.04 ms: 1.00x slower                                                            |
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                            |
| genshi_xml     | 50.4 ms                                                                | 51.3 ms: 1.02x slower                                                            |
| genshi_text    | 22.3 ms                                                                | 23.2 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot               | 3.83 ms                                                                | 3.58 ms: 1.07x faster                                                            |
| generators                 | 28.8 ms                                                                | 27.8 ms: 1.04x faster                                                            |
| deltablue                  | 3.37 ms                                                                | 3.26 ms: 1.03x faster                                                            |
| go                         | 123 ms                                                                 | 119 ms: 1.03x faster                                                             |
| coroutines                 | 24.0 ms                                                                | 23.4 ms: 1.03x faster                                                            |
| crypto_pyaes               | 73.8 ms                                                                | 71.9 ms: 1.03x faster                                                            |
| regex_dna                  | 225 ms                                                                 | 219 ms: 1.03x faster                                                             |
| fannkuch                   | 410 ms                                                                 | 404 ms: 1.02x faster                                                             |
| regex_v8                   | 24.6 ms                                                                | 24.2 ms: 1.01x faster                                                            |
| shortest_path              | 478 ms                                                                 | 472 ms: 1.01x faster                                                             |
| deepcopy_memo              | 30.4 us                                                                | 30.2 us: 1.01x faster                                                            |
| pickle_pure_python         | 329 us                                                                 | 326 us: 1.01x faster                                                             |
| logging_silent             | 105 ns                                                                 | 104 ns: 1.01x faster                                                             |
| dulwich_log                | 65.8 ms                                                                | 65.3 ms: 1.01x faster                                                            |
| coverage                   | 84.6 ms                                                                | 84.0 ms: 1.01x faster                                                            |
| logging_format             | 6.18 us                                                                | 6.14 us: 1.01x faster                                                            |
| sqlglot_parse              | 1.30 ms                                                                | 1.30 ms: 1.01x faster                                                            |
| nbody                      | 97.2 ms                                                                | 96.7 ms: 1.01x faster                                                            |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x faster                                                             |
| comprehensions             | 17.1 us                                                                | 17.0 us: 1.00x faster                                                            |
| hexiom                     | 6.35 ms                                                                | 6.33 ms: 1.00x faster                                                            |
| pprint_safe_repr           | 726 ms                                                                 | 724 ms: 1.00x faster                                                             |
| regex_compile              | 130 ms                                                                 | 130 ms: 1.00x faster                                                             |
| mdp                        | 2.68 sec                                                               | 2.67 sec: 1.00x faster                                                           |
| many_optionals             | 947 us                                                                 | 944 us: 1.00x faster                                                             |
| sympy_integrate            | 20.0 ms                                                                | 19.9 ms: 1.00x faster                                                            |
| pidigits                   | 188 ms                                                                 | 187 ms: 1.00x faster                                                             |
| python_startup_no_site     | 7.02 ms                                                                | 7.04 ms: 1.00x slower                                                            |
| sqlglot_normalize          | 107 ms                                                                 | 107 ms: 1.00x slower                                                             |
| python_startup             | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                            |
| 2to3                       | 256 ms                                                                 | 256 ms: 1.00x slower                                                             |
| subparsers                 | 20.8 ms                                                                | 20.9 ms: 1.00x slower                                                            |
| sympy_sum                  | 147 ms                                                                 | 148 ms: 1.01x slower                                                             |
| sqlglot_optimize           | 53.4 ms                                                                | 53.7 ms: 1.01x slower                                                            |
| scimark_sor                | 129 ms                                                                 | 130 ms: 1.01x slower                                                             |
| sqlite_synth               | 2.84 us                                                                | 2.86 us: 1.01x slower                                                            |
| pyflate                    | 467 ms                                                                 | 470 ms: 1.01x slower                                                             |
| logging_simple             | 5.55 us                                                                | 5.59 us: 1.01x slower                                                            |
| deepcopy_reduce            | 2.70 us                                                                | 2.72 us: 1.01x slower                                                            |
| json                       | 4.99 ms                                                                | 5.03 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 4.78 sec                                                               | 4.82 sec: 1.01x slower                                                           |
| json_loads                 | 26.8 us                                                                | 27.1 us: 1.01x slower                                                            |
| mako                       | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                            |
| async_generators           | 429 ms                                                                 | 434 ms: 1.01x slower                                                             |
| json_dumps                 | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                            |
| xml_etree_generate         | 85.5 ms                                                                | 86.8 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 69.3 ms                                                                | 70.3 ms: 1.01x slower                                                            |
| xml_etree_process          | 59.2 ms                                                                | 60.1 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                 | 575 ms: 1.02x slower                                                             |
| spectral_norm              | 115 ms                                                                 | 117 ms: 1.02x slower                                                             |
| genshi_xml                 | 50.4 ms                                                                | 51.3 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 161 us                                                                 | 164 us: 1.02x slower                                                             |
| nqueens                    | 79.8 ms                                                                | 81.6 ms: 1.02x slower                                                            |
| gc_traversal               | 4.61 ms                                                                | 4.72 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 5.00 ms                                                                | 5.13 ms: 1.03x slower                                                            |
| deepcopy                   | 259 us                                                                 | 266 us: 1.03x slower                                                             |
| pycparser                  | 1.14 sec                                                               | 1.17 sec: 1.03x slower                                                           |
| meteor_contest             | 107 ms                                                                 | 110 ms: 1.04x slower                                                             |
| genshi_text                | 22.3 ms                                                                | 23.2 ms: 1.04x slower                                                            |
| scimark_fft                | 363 ms                                                                 | 379 ms: 1.04x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (37): async_tree_io_tg, sqlalchemy_imperative, connected_components, async_tree_io, richards_super, unpickle_pure_python, sympy_str, float, raytrace, xml_etree_parse, html5lib, create_gc_cycles, k_core, sphinx, xml_etree_iterparse, bench_thread_pool, sympy_expand, sqlglot_transpile, docutils, pylint, async_tree_none, telco, scimark_lu, asyncio_websockets, richards, django_template, pprint_pformat, thrift, chaos, async_tree_memoization, pathlib, bench_mp_pool, tomli_loads, async_tree_none_tg, async_tree_memoization_tg, djangocms, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 86.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x