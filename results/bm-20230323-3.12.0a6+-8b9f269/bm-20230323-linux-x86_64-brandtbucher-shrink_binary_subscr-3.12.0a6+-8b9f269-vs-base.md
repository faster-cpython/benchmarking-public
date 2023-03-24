
# Results vs. base

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: 8b9f269
- commit date: 2023-03-23
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 251 ms: 1.01x faster                                                         |
| chameleon      | 6.57 ms                                                                | 6.41 ms: 1.03x faster                                                        |
| docutils       | 2.54 sec                                                               | 2.53 sec: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                                | 87.5 ms: 1.00x faster                                                        |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                                        |
| regex_dna      | 202 ms                                                                 | 205 ms: 1.02x slower                                                         |
| regex_effbot   | 3.41 ms                                                                | 3.50 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process    | 57.0 ms                                                                | 55.7 ms: 1.02x faster                                                        |
| xml_etree_generate   | 82.1 ms                                                                | 80.8 ms: 1.02x faster                                                        |
| unpickle_list        | 5.06 us                                                                | 4.99 us: 1.01x faster                                                        |
| unpickle_pure_python | 202 us                                                                 | 199 us: 1.01x faster                                                         |
| pickle_list          | 4.39 us                                                                | 4.36 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                                | 99.3 ms: 1.01x faster                                                        |
| pickle               | 10.3 us                                                                | 10.5 us: 1.02x slower                                                        |
| json_dumps           | 9.50 ms                                                                | 9.65 ms: 1.02x slower                                                        |
| json_loads           | 23.9 us                                                                | 24.4 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (4): unpickle, pickle_pure_python, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.49 ms: 1.00x faster                                                        |
| python_startup         | 8.80 ms                                                                | 8.79 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.7 ms                                                                | 33.3 ms: 1.01x faster                                                        |
| genshi_xml      | 48.0 ms                                                                | 47.7 ms: 1.01x faster                                                        |
| mako            | 9.91 ms                                                                | 9.99 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 4.06 ms                                                                | 3.66 ms: 1.11x faster                                                        |
| mdp                     | 2.63 sec                                                               | 2.52 sec: 1.04x faster                                                       |
| chameleon               | 6.57 ms                                                                | 6.41 ms: 1.03x faster                                                        |
| xml_etree_process       | 57.0 ms                                                                | 55.7 ms: 1.02x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                                 | 136 ms: 1.02x faster                                                         |
| xml_etree_generate      | 82.1 ms                                                                | 80.8 ms: 1.02x faster                                                        |
| unpickle_list           | 5.06 us                                                                | 4.99 us: 1.01x faster                                                        |
| scimark_sparse_mat_mult | 4.24 ms                                                                | 4.18 ms: 1.01x faster                                                        |
| scimark_lu              | 110 ms                                                                 | 109 ms: 1.01x faster                                                         |
| unpickle_pure_python    | 202 us                                                                 | 199 us: 1.01x faster                                                         |
| django_template         | 33.7 ms                                                                | 33.3 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 685 ms                                                                 | 678 ms: 1.01x faster                                                         |
| sqlglot_normalize       | 107 ms                                                                 | 106 ms: 1.01x faster                                                         |
| pycparser               | 1.12 sec                                                               | 1.11 sec: 1.01x faster                                                       |
| coverage                | 96.5 ms                                                                | 95.7 ms: 1.01x faster                                                        |
| sqlite_synth            | 2.64 us                                                                | 2.62 us: 1.01x faster                                                        |
| asyncio_tcp             | 509 ms                                                                 | 506 ms: 1.01x faster                                                         |
| 2to3                    | 253 ms                                                                 | 251 ms: 1.01x faster                                                         |
| pickle_list             | 4.39 us                                                                | 4.36 us: 1.01x faster                                                        |
| genshi_xml              | 48.0 ms                                                                | 47.7 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.47 ms                                                                | 1.46 ms: 1.01x faster                                                        |
| xml_etree_iterparse     | 99.8 ms                                                                | 99.3 ms: 1.01x faster                                                        |
| gunicorn                | 1.09 ms                                                                | 1.08 ms: 1.00x faster                                                        |
| nbody                   | 87.8 ms                                                                | 87.5 ms: 1.00x faster                                                        |
| docutils                | 2.54 sec                                                               | 2.53 sec: 1.00x faster                                                       |
| python_startup_no_site  | 6.50 ms                                                                | 6.49 ms: 1.00x faster                                                        |
| python_startup          | 8.80 ms                                                                | 8.79 ms: 1.00x faster                                                        |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| sympy_expand            | 460 ms                                                                 | 463 ms: 1.01x slower                                                         |
| meteor_contest          | 102 ms                                                                 | 102 ms: 1.01x slower                                                         |
| dulwich_log             | 63.4 ms                                                                | 63.8 ms: 1.01x slower                                                        |
| async_generators        | 412 ms                                                                 | 415 ms: 1.01x slower                                                         |
| regex_v8                | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                                        |
| mako                    | 9.91 ms                                                                | 9.99 ms: 1.01x slower                                                        |
| comprehensions          | 23.7 us                                                                | 24.0 us: 1.01x slower                                                        |
| pathlib                 | 18.0 ms                                                                | 18.2 ms: 1.01x slower                                                        |
| deepcopy_memo           | 34.1 us                                                                | 34.4 us: 1.01x slower                                                        |
| sympy_integrate         | 20.4 ms                                                                | 20.6 ms: 1.01x slower                                                        |
| richards                | 43.9 ms                                                                | 44.3 ms: 1.01x slower                                                        |
| json                    | 4.62 ms                                                                | 4.70 ms: 1.02x slower                                                        |
| regex_dna               | 202 ms                                                                 | 205 ms: 1.02x slower                                                         |
| pickle                  | 10.3 us                                                                | 10.5 us: 1.02x slower                                                        |
| json_dumps              | 9.50 ms                                                                | 9.65 ms: 1.02x slower                                                        |
| scimark_monte_carlo     | 67.2 ms                                                                | 68.3 ms: 1.02x slower                                                        |
| telco                   | 6.38 ms                                                                | 6.49 ms: 1.02x slower                                                        |
| spectral_norm           | 92.7 ms                                                                | 94.4 ms: 1.02x slower                                                        |
| json_loads              | 23.9 us                                                                | 24.4 us: 1.02x slower                                                        |
| coroutines              | 22.8 ms                                                                | 23.4 ms: 1.03x slower                                                        |
| regex_effbot            | 3.41 ms                                                                | 3.50 ms: 1.03x slower                                                        |
| fannkuch                | 376 ms                                                                 | 388 ms: 1.03x slower                                                         |
| go                      | 138 ms                                                                 | 142 ms: 1.03x slower                                                         |
| generators              | 28.9 ms                                                                | 29.9 ms: 1.04x slower                                                        |
| chaos                   | 65.6 ms                                                                | 68.2 ms: 1.04x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (41): html5lib, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, logging_silent, dask, sqlalchemy_imperative, unpickle, raytrace, unpack_sequence, pprint_pformat, thrift, float, logging_simple, scimark_sor, pickle_pure_python, xml_etree_parse, async_tree_io, aiohttp, tornado_http, pickle_dict, genshi_text, sympy_sum, sympy_str, djangocms, hexiom, bench_thread_pool, scimark_fft, bench_mp_pool, deepcopy, pyflate, mypy2, sqlglot_optimize, deepcopy_reduce, sqlglot_parse, deltablue, regex_compile, nqueens, crypto_pyaes, sqlglot_transpile, logging_format
