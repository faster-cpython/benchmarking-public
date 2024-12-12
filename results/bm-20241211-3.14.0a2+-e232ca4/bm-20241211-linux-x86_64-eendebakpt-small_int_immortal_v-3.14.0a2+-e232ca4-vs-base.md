# Results vs. base

- fork: eendebakpt
- ref: small_int_immortal_v
- machine: linux-x86_64
- commit hash: e232ca4
- commit date: 2024-12-11
- overall geometric mean: 1.003x slower
- HPT reliability: 99.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                                       |
| docutils       | 2.59 sec                                                               | 2.62 sec: 1.01x slower                                                     |
| html5lib       | 61.9 ms                                                                | 63.5 ms: 1.02x slower                                                      |
| sphinx         | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 314 ms                                                                 | 317 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 507 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 489 ms: 1.02x slower                                                       |
| coroutines                 | 22.7 ms                                                                | 23.2 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (7): async_tree_none_tg, asyncio_websockets, async_generators, async_tree_none, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 95.7 ms                                                                | 94.0 ms: 1.02x faster                                                      |
| float          | 77.5 ms                                                                | 76.3 ms: 1.02x faster                                                      |
| pidigits       | 189 ms                                                                 | 187 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| regex_v8       | 25.4 ms                                                                | 25.9 ms: 1.02x slower                                                      |
| regex_dna      | 219 ms                                                                 | 227 ms: 1.03x slower                                                       |
| regex_effbot   | 3.23 ms                                                                | 3.52 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                      |
| json_loads           | 26.6 us                                                                | 26.8 us: 1.01x slower                                                      |
| tomli_loads          | 2.08 sec                                                               | 2.09 sec: 1.01x slower                                                     |
| xml_etree_process    | 60.0 ms                                                                | 60.6 ms: 1.01x slower                                                      |
| unpickle_pure_python | 217 us                                                                 | 221 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.01 ms: 1.00x faster                                                      |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.7 ms                                                                | 11.7 ms: 1.00x slower                                                      |
| genshi_xml     | 49.2 ms                                                                | 50.2 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2+-e8f4e27 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mdp                        | 2.68 sec                                                               | 2.55 sec: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 5.12 ms                                                                | 4.90 ms: 1.04x faster                                                      |
| crypto_pyaes               | 72.8 ms                                                                | 70.4 ms: 1.03x faster                                                      |
| djangocms                  | 22.5 us                                                                | 21.8 us: 1.03x faster                                                      |
| pycparser                  | 1.18 sec                                                               | 1.15 sec: 1.02x faster                                                     |
| nbody                      | 95.7 ms                                                                | 94.0 ms: 1.02x faster                                                      |
| spectral_norm              | 114 ms                                                                 | 112 ms: 1.02x faster                                                       |
| float                      | 77.5 ms                                                                | 76.3 ms: 1.02x faster                                                      |
| pidigits                   | 189 ms                                                                 | 187 ms: 1.01x faster                                                       |
| json_dumps                 | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                      |
| many_optionals             | 953 us                                                                 | 944 us: 1.01x faster                                                       |
| chaos                      | 61.6 ms                                                                | 61.1 ms: 1.01x faster                                                      |
| raytrace                   | 275 ms                                                                 | 273 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 2.67 us                                                                | 2.66 us: 1.01x faster                                                      |
| sqlalchemy_declarative     | 127 ms                                                                 | 127 ms: 1.00x faster                                                       |
| bench_thread_pool          | 858 us                                                                 | 857 us: 1.00x faster                                                       |
| sympy_integrate            | 19.9 ms                                                                | 19.9 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.02 ms                                                                | 7.01 ms: 1.00x faster                                                      |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                      |
| mako                       | 11.7 ms                                                                | 11.7 ms: 1.00x slower                                                      |
| fannkuch                   | 403 ms                                                                 | 405 ms: 1.00x slower                                                       |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                      |
| deepcopy                   | 258 us                                                                 | 259 us: 1.00x slower                                                       |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.00x slower                                                       |
| deltablue                  | 3.25 ms                                                                | 3.27 ms: 1.00x slower                                                      |
| json_loads                 | 26.6 us                                                                | 26.8 us: 1.01x slower                                                      |
| pyflate                    | 493 ms                                                                 | 496 ms: 1.01x slower                                                       |
| tomli_loads                | 2.08 sec                                                               | 2.09 sec: 1.01x slower                                                     |
| sqlite_synth               | 2.84 us                                                                | 2.87 us: 1.01x slower                                                      |
| pprint_safe_repr           | 725 ms                                                                 | 731 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.49 sec                                                               | 1.50 sec: 1.01x slower                                                     |
| deepcopy_memo              | 30.6 us                                                                | 30.9 us: 1.01x slower                                                      |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| async_tree_memoization_tg  | 314 ms                                                                 | 317 ms: 1.01x slower                                                       |
| xml_etree_process          | 60.0 ms                                                                | 60.6 ms: 1.01x slower                                                      |
| subparsers                 | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                                      |
| docutils                   | 2.59 sec                                                               | 2.62 sec: 1.01x slower                                                     |
| sphinx                     | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                                     |
| nqueens                    | 79.3 ms                                                                | 80.7 ms: 1.02x slower                                                      |
| hexiom                     | 6.16 ms                                                                | 6.27 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 507 ms: 1.02x slower                                                       |
| pathlib                    | 16.2 ms                                                                | 16.5 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 489 ms: 1.02x slower                                                       |
| json                       | 5.03 ms                                                                | 5.13 ms: 1.02x slower                                                      |
| regex_v8                   | 25.4 ms                                                                | 25.9 ms: 1.02x slower                                                      |
| genshi_xml                 | 49.2 ms                                                                | 50.2 ms: 1.02x slower                                                      |
| coroutines                 | 22.7 ms                                                                | 23.2 ms: 1.02x slower                                                      |
| scimark_fft                | 368 ms                                                                 | 376 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 217 us                                                                 | 221 us: 1.02x slower                                                       |
| html5lib                   | 61.9 ms                                                                | 63.5 ms: 1.02x slower                                                      |
| scimark_lu                 | 115 ms                                                                 | 119 ms: 1.03x slower                                                       |
| regex_dna                  | 219 ms                                                                 | 227 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 163 us                                                                 | 169 us: 1.04x slower                                                       |
| gc_traversal               | 4.57 ms                                                                | 4.76 ms: 1.04x slower                                                      |
| regex_effbot               | 3.23 ms                                                                | 3.52 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (42): scimark_monte_carlo, async_tree_none_tg, meteor_contest, scimark_sor, richards_super, coverage, logging_simple, sqlglot_normalize, xml_etree_parse, genshi_text, asyncio_websockets, k_core, async_generators, sympy_str, pickle_pure_python, logging_silent, sqlglot_transpile, pylint, go, xml_etree_iterparse, sqlglot_parse, django_template, async_tree_none, sympy_sum, richards, bench_mp_pool, dulwich_log, mypy2, sqlglot_optimize, generators, bpe_tokeniser, sympy_expand, xml_etree_generate, thrift, logging_format, connected_components, comprehensions, telco, async_tree_io, async_tree_memoization, shortest_path, async_tree_io_tg

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x