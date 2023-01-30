
# Results vs. base

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                        |
| docutils       | 2.51 sec                                                               | 2.50 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 189 ms: 1.04x faster                                                        |
| float          | 72.1 ms                                                                | 73.0 ms: 1.01x slower                                                       |
| nbody          | 92.9 ms                                                                | 94.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 207 ms: 1.02x faster                                                        |
| regex_v8       | 22.6 ms                                                                | 22.4 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.46 ms                                                                | 9.35 ms: 1.01x faster                                                       |
| xml_etree_generate   | 78.6 ms                                                                | 78.0 ms: 1.01x faster                                                       |
| pickle_dict          | 30.1 us                                                                | 29.9 us: 1.01x faster                                                       |
| unpickle_list        | 5.01 us                                                                | 5.06 us: 1.01x slower                                                       |
| xml_etree_parse      | 148 ms                                                                 | 149 ms: 1.01x slower                                                        |
| pickle_pure_python   | 284 us                                                                 | 288 us: 1.02x slower                                                        |
| unpickle_pure_python | 196 us                                                                 | 204 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (6): json_loads, pickle_list, pickle, xml_etree_process, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.46 ms                                                                | 6.42 ms: 1.01x faster                                                       |
| python_startup         | 8.93 ms                                                                | 8.89 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                       |
| mako            | 9.61 ms                                                                | 9.65 ms: 1.00x slower                                                       |
| genshi_xml      | 47.2 ms                                                                | 47.4 ms: 1.01x slower                                                       |
| genshi_text     | 20.6 ms                                                                | 20.9 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits               | 198 ms                                                                 | 189 ms: 1.04x faster                                                        |
| unpack_sequence        | 42.8 ns                                                                | 41.4 ns: 1.03x faster                                                       |
| coverage               | 96.2 ms                                                                | 93.1 ms: 1.03x faster                                                       |
| meteor_contest         | 108 ms                                                                 | 104 ms: 1.03x faster                                                        |
| scimark_monte_carlo    | 66.8 ms                                                                | 65.2 ms: 1.03x faster                                                       |
| django_template        | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                       |
| mdp                    | 2.61 sec                                                               | 2.56 sec: 1.02x faster                                                      |
| regex_dna              | 210 ms                                                                 | 207 ms: 1.02x faster                                                        |
| json_dumps             | 9.46 ms                                                                | 9.35 ms: 1.01x faster                                                       |
| thrift                 | 746 us                                                                 | 739 us: 1.01x faster                                                        |
| pathlib                | 17.9 ms                                                                | 17.7 ms: 1.01x faster                                                       |
| regex_v8               | 22.6 ms                                                                | 22.4 ms: 1.01x faster                                                       |
| xml_etree_generate     | 78.6 ms                                                                | 78.0 ms: 1.01x faster                                                       |
| crypto_pyaes           | 73.8 ms                                                                | 73.2 ms: 1.01x faster                                                       |
| pickle_dict            | 30.1 us                                                                | 29.9 us: 1.01x faster                                                       |
| coroutines             | 25.0 ms                                                                | 24.8 ms: 1.01x faster                                                       |
| spectral_norm          | 94.4 ms                                                                | 93.8 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.46 ms                                                                | 6.42 ms: 1.01x faster                                                       |
| docutils               | 2.51 sec                                                               | 2.50 sec: 1.01x faster                                                      |
| python_startup         | 8.93 ms                                                                | 8.89 ms: 1.00x faster                                                       |
| asyncio_tcp            | 497 ms                                                                 | 496 ms: 1.00x faster                                                        |
| 2to3                   | 251 ms                                                                 | 252 ms: 1.00x slower                                                        |
| bench_thread_pool      | 776 us                                                                 | 778 us: 1.00x slower                                                        |
| aiohttp                | 997 us                                                                 | 1.00 ms: 1.00x slower                                                       |
| mako                   | 9.61 ms                                                                | 9.65 ms: 1.00x slower                                                       |
| pprint_pformat         | 1.38 sec                                                               | 1.38 sec: 1.00x slower                                                      |
| chaos                  | 64.0 ms                                                                | 64.3 ms: 1.00x slower                                                       |
| sympy_integrate        | 19.7 ms                                                                | 19.8 ms: 1.01x slower                                                       |
| genshi_xml             | 47.2 ms                                                                | 47.4 ms: 1.01x slower                                                       |
| sqlglot_optimize       | 50.6 ms                                                                | 51.0 ms: 1.01x slower                                                       |
| sympy_expand           | 451 ms                                                                 | 454 ms: 1.01x slower                                                        |
| sqlglot_normalize      | 104 ms                                                                 | 105 ms: 1.01x slower                                                        |
| pycparser              | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                                      |
| unpickle_list          | 5.01 us                                                                | 5.06 us: 1.01x slower                                                       |
| async_tree_io          | 1.31 sec                                                               | 1.32 sec: 1.01x slower                                                      |
| genshi_text            | 20.6 ms                                                                | 20.9 ms: 1.01x slower                                                       |
| xml_etree_parse        | 148 ms                                                                 | 149 ms: 1.01x slower                                                        |
| logging_silent         | 90.1 ns                                                                | 91.2 ns: 1.01x slower                                                       |
| go                     | 136 ms                                                                 | 138 ms: 1.01x slower                                                        |
| float                  | 72.1 ms                                                                | 73.0 ms: 1.01x slower                                                       |
| deepcopy_reduce        | 2.90 us                                                                | 2.95 us: 1.01x slower                                                       |
| create_gc_cycles       | 1.45 ms                                                                | 1.47 ms: 1.02x slower                                                       |
| nqueens                | 75.4 ms                                                                | 76.6 ms: 1.02x slower                                                       |
| nbody                  | 92.9 ms                                                                | 94.5 ms: 1.02x slower                                                       |
| telco                  | 6.24 ms                                                                | 6.35 ms: 1.02x slower                                                       |
| logging_simple         | 5.73 us                                                                | 5.82 us: 1.02x slower                                                       |
| pickle_pure_python     | 284 us                                                                 | 288 us: 1.02x slower                                                        |
| logging_format         | 6.33 us                                                                | 6.45 us: 1.02x slower                                                       |
| generators             | 75.0 ms                                                                | 76.6 ms: 1.02x slower                                                       |
| richards               | 42.0 ms                                                                | 43.0 ms: 1.02x slower                                                       |
| pyflate                | 393 ms                                                                 | 404 ms: 1.03x slower                                                        |
| gc_traversal           | 4.16 ms                                                                | 4.29 ms: 1.03x slower                                                       |
| scimark_fft            | 297 ms                                                                 | 306 ms: 1.03x slower                                                        |
| fannkuch               | 363 ms                                                                 | 376 ms: 1.04x slower                                                        |
| unpickle_pure_python   | 196 us                                                                 | 204 us: 1.04x slower                                                        |
| async_tree_memoization | 616 ms                                                                 | 659 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (35): scimark_sparse_mat_mult, html5lib, djangocms, chameleon, sqlite_synth, deltablue, json_loads, bench_mp_pool, regex_effbot, async_tree_none, hexiom, sympy_str, pickle_list, sympy_sum, pprint_safe_repr, async_generators, dulwich_log, regex_compile, tornado_http, sqlglot_transpile, gunicorn, deepcopy, async_tree_cpu_io_mixed, mypy, dask, sqlglot_parse, pickle, xml_etree_process, scimark_lu, raytrace, deepcopy_memo, scimark_sor, unpickle, xml_etree_iterparse, json
