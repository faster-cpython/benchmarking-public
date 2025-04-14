# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.001x slower
- HPT reliability: 88.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.41 sec                                                               | 1.41 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines     | 15.9 ms                                                                | 15.9 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (18): async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager, async_tree_none_tg, async_generators, async_tree_eager_cpu_io_mixed_tg, async_tree_none, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 46.6 ms                                                                | 46.9 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 17.2 ms                                                                | 17.1 ms: 1.00x faster                                                  |
| regex_compile  | 66.9 ms                                                                | 67.1 ms: 1.00x slower                                                  |
| regex_dna      | 141 ms                                                                 | 144 ms: 1.02x slower                                                   |
| regex_effbot   | 2.27 ms                                                                | 2.36 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 71.2 ms                                                                | 70.4 ms: 1.01x faster                                                  |
| unpickle_pure_python | 142 us                                                                 | 143 us: 1.00x slower                                                   |
| xml_etree_generate   | 53.1 ms                                                                | 53.4 ms: 1.00x slower                                                  |
| tomli_loads          | 1.19 sec                                                               | 1.20 sec: 1.01x slower                                                 |
| xml_etree_parse      | 98.7 ms                                                                | 102 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (4): json_loads, pickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.1 ms                                                                | 18.6 ms: 1.03x faster                                                  |
| python_startup_no_site | 14.1 ms                                                                | 13.7 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 20.9 ms                                                                | 20.8 ms: 1.00x faster                                                  |
| mako            | 7.39 ms                                                                | 7.37 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup           | 19.1 ms                                                                | 18.6 ms: 1.03x faster                                                  |
| python_startup_no_site   | 14.1 ms                                                                | 13.7 ms: 1.02x faster                                                  |
| bench_mp_pool            | 60.4 ms                                                                | 59.2 ms: 1.02x faster                                                  |
| typing_runtime_protocols | 93.8 us                                                                | 92.4 us: 1.02x faster                                                  |
| xml_etree_iterparse      | 71.2 ms                                                                | 70.4 ms: 1.01x faster                                                  |
| bpe_tokeniser            | 2.91 sec                                                               | 2.89 sec: 1.01x faster                                                 |
| connected_components     | 299 ms                                                                 | 297 ms: 1.01x faster                                                   |
| generators               | 23.0 ms                                                                | 22.9 ms: 1.01x faster                                                  |
| pprint_pformat           | 936 ms                                                                 | 931 ms: 1.01x faster                                                   |
| chaos                    | 39.0 ms                                                                | 38.9 ms: 1.00x faster                                                  |
| regex_v8                 | 17.2 ms                                                                | 17.1 ms: 1.00x faster                                                  |
| django_template          | 20.9 ms                                                                | 20.8 ms: 1.00x faster                                                  |
| mako                     | 7.39 ms                                                                | 7.37 ms: 1.00x faster                                                  |
| coroutines               | 15.9 ms                                                                | 15.9 ms: 1.00x faster                                                  |
| scimark_monte_carlo      | 42.6 ms                                                                | 42.7 ms: 1.00x slower                                                  |
| dask                     | 768 ms                                                                 | 769 ms: 1.00x slower                                                   |
| dulwich_log              | 27.3 ms                                                                | 27.3 ms: 1.00x slower                                                  |
| raytrace                 | 171 ms                                                                 | 171 ms: 1.00x slower                                                   |
| regex_compile            | 66.9 ms                                                                | 67.1 ms: 1.00x slower                                                  |
| logging_simple           | 3.18 us                                                                | 3.19 us: 1.00x slower                                                  |
| unpickle_pure_python     | 142 us                                                                 | 143 us: 1.00x slower                                                   |
| xml_etree_generate       | 53.1 ms                                                                | 53.4 ms: 1.00x slower                                                  |
| docutils                 | 1.41 sec                                                               | 1.41 sec: 1.01x slower                                                 |
| float                    | 46.6 ms                                                                | 46.9 ms: 1.01x slower                                                  |
| go                       | 79.1 ms                                                                | 79.6 ms: 1.01x slower                                                  |
| bench_thread_pool        | 488 us                                                                 | 491 us: 1.01x slower                                                   |
| pathlib                  | 22.7 ms                                                                | 22.9 ms: 1.01x slower                                                  |
| telco                    | 4.52 ms                                                                | 4.55 ms: 1.01x slower                                                  |
| tomli_loads              | 1.19 sec                                                               | 1.20 sec: 1.01x slower                                                 |
| deepcopy_memo            | 18.2 us                                                                | 18.4 us: 1.01x slower                                                  |
| k_core                   | 1.48 sec                                                               | 1.51 sec: 1.02x slower                                                 |
| regex_dna                | 141 ms                                                                 | 144 ms: 1.02x slower                                                   |
| xml_etree_parse          | 98.7 ms                                                                | 102 ms: 1.03x slower                                                   |
| regex_effbot             | 2.27 ms                                                                | 2.36 ms: 1.04x slower                                                  |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (71): sympy_sum, async_tree_eager_io_tg, gc_traversal, json_loads, sqlalchemy_imperative, async_tree_eager_memoization, async_tree_eager, spectral_norm, async_tree_none_tg, meteor_contest, scimark_sor, scimark_lu, mdp, async_generators, deepcopy, pycparser, sqlglot_normalize, async_tree_eager_cpu_io_mixed_tg, html5lib, pickle_pure_python, subparsers, async_tree_none, pyflate, richards_super, richards, hexiom, comprehensions, async_tree_eager_tg, create_gc_cycles, nqueens, sympy_integrate, thrift, xml_etree_process, pprint_safe_repr, sympy_str, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, pidigits, json, sympy_expand, sqlglot_optimize, json_dumps, genshi_text, asyncio_websockets, deltablue, scimark_fft, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io, scimark_sparse_mat_mult, crypto_pyaes, sqlglot_transpile, sqlalchemy_declarative, async_tree_io_tg, shortest_path, sqlite_synth, async_tree_memoization_tg, logging_silent, sphinx, logging_format, genshi_xml, 2to3, fannkuch, nbody, many_optionals, deepcopy_reduce, sqlglot_parse, coverage, pylint, async_tree_io
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 88.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x