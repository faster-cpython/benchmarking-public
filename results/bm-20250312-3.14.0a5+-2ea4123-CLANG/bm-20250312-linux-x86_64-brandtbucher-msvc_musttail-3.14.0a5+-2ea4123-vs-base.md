# Results vs. base

- fork: brandtbucher
- ref: msvc_musttail
- machine: linux-x86_64
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.002x slower
- HPT reliability: 96.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 251 ms: 1.00x slower                                                  |
| docutils       | 2.57 sec                                                               | 2.61 sec: 1.01x slower                                                |
| html5lib       | 61.1 ms                                                                | 57.3 ms: 1.07x faster                                                 |
| sphinx         | 988 ms                                                                 | 1.00 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators           | 382 ms                                                                 | 368 ms: 1.04x faster                                                  |
| async_tree_memoization     | 305 ms                                                                 | 306 ms: 1.00x slower                                                  |
| coroutines                 | 21.6 ms                                                                | 22.1 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 517 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 476 ms                                                                 | 504 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 67.9 ms                                                                | 66.8 ms: 1.02x faster                                                 |
| nbody          | 84.7 ms                                                                | 86.4 ms: 1.02x slower                                                 |
| pidigits       | 205 ms                                                                 | 219 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.44 ms                                                                | 3.28 ms: 1.05x faster                                                 |
| regex_dna      | 200 ms                                                                 | 196 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 313 us                                                                 | 306 us: 1.02x faster                                                  |
| json_dumps           | 12.5 ms                                                                | 12.5 ms: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                                 | 217 us: 1.00x faster                                                  |
| xml_etree_parse      | 162 ms                                                                 | 163 ms: 1.00x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                                 | 103 ms: 1.01x slower                                                  |
| xml_etree_generate   | 84.8 ms                                                                | 86.8 ms: 1.02x slower                                                 |
| xml_etree_process    | 57.3 ms                                                                | 58.7 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.02 ms: 1.01x faster                                                 |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                 |
| django_template | 30.2 ms                                                                | 30.6 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| html5lib                   | 61.1 ms                                                                | 57.3 ms: 1.07x faster                                                 |
| regex_effbot               | 3.44 ms                                                                | 3.28 ms: 1.05x faster                                                 |
| async_generators           | 382 ms                                                                 | 368 ms: 1.04x faster                                                  |
| logging_silent             | 89.9 ns                                                                | 87.1 ns: 1.03x faster                                                 |
| mdp                        | 2.73 sec                                                               | 2.65 sec: 1.03x faster                                                |
| deepcopy_memo              | 30.2 us                                                                | 29.4 us: 1.03x faster                                                 |
| logging_simple             | 5.39 us                                                                | 5.26 us: 1.02x faster                                                 |
| deepcopy_reduce            | 2.59 us                                                                | 2.53 us: 1.02x faster                                                 |
| pickle_pure_python         | 313 us                                                                 | 306 us: 1.02x faster                                                  |
| typing_runtime_protocols   | 151 us                                                                 | 148 us: 1.02x faster                                                  |
| regex_dna                  | 200 ms                                                                 | 196 ms: 1.02x faster                                                  |
| logging_format             | 5.96 us                                                                | 5.86 us: 1.02x faster                                                 |
| gc_traversal               | 5.06 ms                                                                | 4.97 ms: 1.02x faster                                                 |
| subparsers                 | 20.5 ms                                                                | 20.2 ms: 1.02x faster                                                 |
| float                      | 67.9 ms                                                                | 66.8 ms: 1.02x faster                                                 |
| meteor_contest             | 112 ms                                                                 | 111 ms: 1.02x faster                                                  |
| chaos                      | 54.1 ms                                                                | 53.3 ms: 1.01x faster                                                 |
| scimark_lu                 | 108 ms                                                                 | 107 ms: 1.01x faster                                                  |
| deepcopy                   | 247 us                                                                 | 244 us: 1.01x faster                                                  |
| thrift                     | 746 us                                                                 | 737 us: 1.01x faster                                                  |
| pyflate                    | 414 ms                                                                 | 410 ms: 1.01x faster                                                  |
| hexiom                     | 5.81 ms                                                                | 5.74 ms: 1.01x faster                                                 |
| scimark_sor                | 108 ms                                                                 | 107 ms: 1.01x faster                                                  |
| sympy_expand               | 444 ms                                                                 | 440 ms: 1.01x faster                                                  |
| pathlib                    | 15.0 ms                                                                | 14.9 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.08 ms                                                                | 7.02 ms: 1.01x faster                                                 |
| raytrace                   | 257 ms                                                                 | 255 ms: 1.01x faster                                                  |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                 |
| json_dumps                 | 12.5 ms                                                                | 12.5 ms: 1.01x faster                                                 |
| sqlalchemy_declarative     | 126 ms                                                                 | 126 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                                 | 217 us: 1.00x faster                                                  |
| bpe_tokeniser              | 4.41 sec                                                               | 4.39 sec: 1.00x faster                                                |
| bench_mp_pool              | 81.3 ms                                                                | 80.9 ms: 1.00x faster                                                 |
| create_gc_cycles           | 2.55 ms                                                                | 2.54 ms: 1.00x faster                                                 |
| many_optionals             | 927 us                                                                 | 924 us: 1.00x faster                                                  |
| sympy_str                  | 259 ms                                                                 | 258 ms: 1.00x faster                                                  |
| bench_thread_pool          | 829 us                                                                 | 831 us: 1.00x slower                                                  |
| sqlglot_v2_transpile       | 1.49 ms                                                                | 1.50 ms: 1.00x slower                                                 |
| xml_etree_parse            | 162 ms                                                                 | 163 ms: 1.00x slower                                                  |
| pprint_pformat             | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                                |
| 2to3                       | 250 ms                                                                 | 251 ms: 1.00x slower                                                  |
| async_tree_memoization     | 305 ms                                                                 | 306 ms: 1.00x slower                                                  |
| coverage                   | 79.2 ms                                                                | 79.6 ms: 1.00x slower                                                 |
| sqlglot_v2_parse           | 1.19 ms                                                                | 1.20 ms: 1.01x slower                                                 |
| crypto_pyaes               | 72.0 ms                                                                | 72.5 ms: 1.01x slower                                                 |
| generators                 | 28.4 ms                                                                | 28.6 ms: 1.01x slower                                                 |
| mako                       | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                 |
| shortest_path              | 476 ms                                                                 | 480 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 102 ms                                                                 | 103 ms: 1.01x slower                                                  |
| deltablue                  | 2.99 ms                                                                | 3.01 ms: 1.01x slower                                                 |
| django_template            | 30.2 ms                                                                | 30.6 ms: 1.01x slower                                                 |
| sqlglot_v2_optimize        | 51.5 ms                                                                | 52.2 ms: 1.01x slower                                                 |
| docutils                   | 2.57 sec                                                               | 2.61 sec: 1.01x slower                                                |
| sqlglot_v2_normalize       | 103 ms                                                                 | 104 ms: 1.02x slower                                                  |
| sphinx                     | 988 ms                                                                 | 1.00 sec: 1.02x slower                                                |
| nbody                      | 84.7 ms                                                                | 86.4 ms: 1.02x slower                                                 |
| coroutines                 | 21.6 ms                                                                | 22.1 ms: 1.02x slower                                                 |
| xml_etree_generate         | 84.8 ms                                                                | 86.8 ms: 1.02x slower                                                 |
| xml_etree_process          | 57.3 ms                                                                | 58.7 ms: 1.03x slower                                                 |
| scimark_fft                | 281 ms                                                                 | 289 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 3.98 ms                                                                | 4.14 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 517 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 476 ms                                                                 | 504 ms: 1.06x slower                                                  |
| pidigits                   | 205 ms                                                                 | 219 ms: 1.07x slower                                                  |
| richards                   | 41.6 ms                                                                | 47.4 ms: 1.14x slower                                                 |
| richards_super             | 48.2 ms                                                                | 55.6 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (30): spectral_norm, scimark_monte_carlo, go, genshi_text, sympy_sum, nqueens, asyncio_websockets, dulwich_log, sqlalchemy_imperative, json, fannkuch, sympy_integrate, comprehensions, regex_v8, regex_compile, connected_components, pprint_safe_repr, k_core, json_loads, genshi_xml, async_tree_io, sqlite_synth, pycparser, telco, tomli_loads, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 96.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x