# Results vs. 3.13.0

- fork: python
- ref: v3.13.1
- machine: linux-x86_64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.008x slower
- HPT reliability: 96.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 293 ms: 1.00x slower                                         |
| docutils       | 2.81 sec                                                     | 2.82 sec: 1.01x slower                                       |
| html5lib       | 72.9 ms                                                      | 73.3 ms: 1.01x slower                                        |
| sphinx         | 1.11 sec                                                     | 1.12 sec: 1.01x slower                                       |
| tornado_http   | 119 ms                                                       | 120 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                        |
| async_tree_none_tg         | 342 ms                                                       | 337 ms: 1.01x faster                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 452 ms: 1.01x faster                                         |
| async_tree_none            | 370 ms                                                       | 374 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 604 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 607 ms: 1.06x slower                                         |
| async_generators           | 364 ms                                                       | 445 ms: 1.23x slower                                         |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 88.6 ms: 1.04x faster                                        |
| float          | 81.6 ms                                                      | 79.7 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 143 ms: 1.00x slower                                         |
| regex_v8       | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                        |
| regex_dna      | 238 ms                                                       | 250 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.25 sec: 1.08x faster                                       |
| unpickle_pure_python | 216 us                                                       | 211 us: 1.02x faster                                         |
| xml_etree_process    | 60.7 ms                                                      | 61.5 ms: 1.01x slower                                        |
| pickle_pure_python   | 322 us                                                       | 326 us: 1.01x slower                                         |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.02x slower                                         |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                        |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                        |
| xml_etree_generate   | 85.2 ms                                                      | 87.5 ms: 1.03x slower                                        |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.04x slower                                         |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                        |
| python_startup         | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                        |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.9 ms                                                      | 36.3 ms: 1.07x faster                                        |
| mako            | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                        |
| genshi_xml      | 58.0 ms                                                      | 59.5 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads                | 2.43 sec                                                     | 2.25 sec: 1.08x faster                                       |
| django_template            | 38.9 ms                                                      | 36.3 ms: 1.07x faster                                        |
| nqueens                    | 92.3 ms                                                      | 87.4 ms: 1.06x faster                                        |
| shortest_path              | 477 ms                                                       | 458 ms: 1.04x faster                                         |
| nbody                      | 92.1 ms                                                      | 88.6 ms: 1.04x faster                                        |
| fannkuch                   | 384 ms                                                       | 370 ms: 1.04x faster                                         |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.04x faster                                       |
| generators                 | 33.9 ms                                                      | 32.8 ms: 1.03x faster                                        |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                        |
| go                         | 167 ms                                                       | 162 ms: 1.03x faster                                         |
| unpickle_pure_python       | 216 us                                                       | 211 us: 1.02x faster                                         |
| float                      | 81.6 ms                                                      | 79.7 ms: 1.02x faster                                        |
| chaos                      | 60.6 ms                                                      | 59.2 ms: 1.02x faster                                        |
| coverage                   | 84.5 ms                                                      | 82.7 ms: 1.02x faster                                        |
| richards_super             | 60.2 ms                                                      | 58.9 ms: 1.02x faster                                        |
| connected_components       | 443 ms                                                       | 435 ms: 1.02x faster                                         |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.02x faster                                       |
| hexiom                     | 6.47 ms                                                      | 6.38 ms: 1.01x faster                                        |
| async_tree_none_tg         | 342 ms                                                       | 337 ms: 1.01x faster                                         |
| json                       | 5.62 ms                                                      | 5.54 ms: 1.01x faster                                        |
| logging_silent             | 97.5 ns                                                      | 96.2 ns: 1.01x faster                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 452 ms: 1.01x faster                                         |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                        |
| thrift                     | 918 us                                                       | 908 us: 1.01x faster                                         |
| richards                   | 52.5 ms                                                      | 52.0 ms: 1.01x faster                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                         |
| meteor_contest             | 130 ms                                                       | 130 ms: 1.00x faster                                         |
| 2to3                       | 293 ms                                                       | 293 ms: 1.00x slower                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.77 ms: 1.00x slower                                        |
| regex_compile              | 143 ms                                                       | 143 ms: 1.00x slower                                         |
| pyflate                    | 493 ms                                                       | 495 ms: 1.00x slower                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 5.12 sec: 1.01x slower                                       |
| html5lib                   | 72.9 ms                                                      | 73.3 ms: 1.01x slower                                        |
| docutils                   | 2.81 sec                                                     | 2.82 sec: 1.01x slower                                       |
| mako                       | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 65.8 ms: 1.01x slower                                        |
| pathlib                    | 17.4 ms                                                      | 17.6 ms: 1.01x slower                                        |
| sympy_str                  | 297 ms                                                       | 299 ms: 1.01x slower                                         |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.3 ms: 1.01x slower                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                        |
| tornado_http               | 119 ms                                                       | 120 ms: 1.01x slower                                         |
| sphinx                     | 1.11 sec                                                     | 1.12 sec: 1.01x slower                                       |
| async_tree_none            | 370 ms                                                       | 374 ms: 1.01x slower                                         |
| sympy_expand               | 506 ms                                                       | 512 ms: 1.01x slower                                         |
| create_gc_cycles           | 2.65 ms                                                      | 2.68 ms: 1.01x slower                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 59.4 ms: 1.01x slower                                        |
| xml_etree_process          | 60.7 ms                                                      | 61.5 ms: 1.01x slower                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.72 sec: 1.01x slower                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 604 ms: 1.01x slower                                         |
| pickle_pure_python         | 322 us                                                       | 326 us: 1.01x slower                                         |
| sympy_sum                  | 154 ms                                                       | 156 ms: 1.02x slower                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.02x slower                                         |
| telco                      | 8.77 ms                                                      | 8.93 ms: 1.02x slower                                        |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                        |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                        |
| dulwich_log                | 65.5 ms                                                      | 66.8 ms: 1.02x slower                                        |
| deepcopy_memo              | 38.9 us                                                      | 39.8 us: 1.02x slower                                        |
| genshi_xml                 | 58.0 ms                                                      | 59.5 ms: 1.02x slower                                        |
| scimark_lu                 | 97.4 ms                                                      | 99.8 ms: 1.02x slower                                        |
| python_startup             | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                        |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                        |
| deepcopy_reduce            | 3.49 us                                                      | 3.58 us: 1.03x slower                                        |
| xml_etree_generate         | 85.2 ms                                                      | 87.5 ms: 1.03x slower                                        |
| deepcopy                   | 388 us                                                       | 401 us: 1.03x slower                                         |
| logging_format             | 6.95 us                                                      | 7.22 us: 1.04x slower                                        |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.04x slower                                         |
| regex_v8                   | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                        |
| regex_dna                  | 238 ms                                                       | 250 ms: 1.05x slower                                         |
| bench_mp_pool              | 4.82 ms                                                      | 5.08 ms: 1.05x slower                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 607 ms: 1.06x slower                                         |
| logging_simple             | 6.28 us                                                      | 6.65 us: 1.06x slower                                        |
| scimark_fft                | 298 ms                                                       | 326 ms: 1.10x slower                                         |
| gc_traversal               | 4.48 ms                                                      | 4.94 ms: 1.10x slower                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.76 ms: 1.13x slower                                        |
| gevent_hub                 | 1.07 ns                                                      | 1.21 ns: 1.14x slower                                        |
| async_generators           | 364 ms                                                       | 445 ms: 1.23x slower                                         |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (20): asyncio_websockets, typing_runtime_protocols, deltablue, chameleon, scimark_sor, crypto_pyaes, sqlglot_normalize, sqlglot_parse, regex_effbot, raytrace, pprint_safe_repr, pidigits, bench_thread_pool, async_tree_io_tg, sympy_integrate, k_core, genshi_text, async_tree_io, pylint, async_tree_memoization
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: mypy2
Ignored benchmarks (5) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451.json: djangocms, gunicorn, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 96.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x