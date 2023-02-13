
# Results vs. base

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 251 ms: 1.00x slower                                          |
| chameleon      | 6.54 ms                                                                | 6.47 ms: 1.01x faster                                         |
| docutils       | 2.54 sec                                                               | 2.53 sec: 1.00x faster                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 94.7 ms                                                                | 94.0 ms: 1.01x faster                                         |
| pidigits       | 190 ms                                                                 | 193 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 21.2 ms                                                                | 21.6 ms: 1.02x slower                                         |
| regex_effbot   | 3.32 ms                                                                | 3.66 ms: 1.10x slower                                         |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                  |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_dict          | 31.8 us                                                                | 30.9 us: 1.03x faster                                         |
| xml_etree_iterparse  | 105 ms                                                                 | 103 ms: 1.03x faster                                          |
| json_dumps           | 9.61 ms                                                                | 9.39 ms: 1.02x faster                                         |
| xml_etree_parse      | 149 ms                                                                 | 148 ms: 1.01x faster                                          |
| pickle               | 10.2 us                                                                | 10.1 us: 1.01x faster                                         |
| json_loads           | 23.9 us                                                                | 23.7 us: 1.01x faster                                         |
| xml_etree_generate   | 80.5 ms                                                                | 80.2 ms: 1.00x faster                                         |
| pickle_list          | 4.12 us                                                                | 4.15 us: 1.01x slower                                         |
| unpickle_pure_python | 196 us                                                                 | 198 us: 1.01x slower                                          |
| pickle_pure_python   | 284 us                                                                 | 291 us: 1.03x slower                                          |
| unpickle_list        | 4.97 us                                                                | 5.13 us: 1.03x slower                                         |
| unpickle             | 13.1 us                                                                | 13.7 us: 1.04x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.92 ms                                                                | 8.90 ms: 1.00x faster                                         |
| python_startup_no_site | 6.47 ms                                                                | 6.46 ms: 1.00x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 33.2 ms                                                                | 32.6 ms: 1.02x faster                                         |
| mako            | 9.94 ms                                                                | 9.90 ms: 1.00x faster                                         |
| genshi_text     | 20.5 ms                                                                | 20.9 ms: 1.02x slower                                         |
| genshi_xml      | 46.1 ms                                                                | 47.8 ms: 1.04x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                  |

All benchmarks:
===============

| Benchmark              | bm-20230210-linux-x86_64-python-61f2be08661949e2f6df-3.12.0a5+-61f2be0 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| gc_traversal           | 3.91 ms                                                                | 3.58 ms: 1.09x faster                                         |
| async_tree_none        | 522 ms                                                                 | 498 ms: 1.05x faster                                          |
| sympy_expand           | 458 ms                                                                 | 439 ms: 1.04x faster                                          |
| async_tree_io          | 1.32 sec                                                               | 1.27 sec: 1.04x faster                                        |
| meteor_contest         | 107 ms                                                                 | 104 ms: 1.03x faster                                          |
| pickle_dict            | 31.8 us                                                                | 30.9 us: 1.03x faster                                         |
| xml_etree_iterparse    | 105 ms                                                                 | 103 ms: 1.03x faster                                          |
| sympy_integrate        | 20.0 ms                                                                | 19.5 ms: 1.03x faster                                         |
| pprint_safe_repr       | 685 ms                                                                 | 668 ms: 1.03x faster                                          |
| sympy_sum              | 159 ms                                                                 | 155 ms: 1.03x faster                                          |
| sqlglot_normalize      | 104 ms                                                                 | 101 ms: 1.02x faster                                          |
| json_dumps             | 9.61 ms                                                                | 9.39 ms: 1.02x faster                                         |
| sqlalchemy_imperative  | 17.8 ms                                                                | 17.4 ms: 1.02x faster                                         |
| sympy_str              | 271 ms                                                                 | 265 ms: 1.02x faster                                          |
| nqueens                | 76.6 ms                                                                | 74.9 ms: 1.02x faster                                         |
| chaos                  | 64.6 ms                                                                | 63.2 ms: 1.02x faster                                         |
| django_template        | 33.2 ms                                                                | 32.6 ms: 1.02x faster                                         |
| sqlalchemy_declarative | 137 ms                                                                 | 134 ms: 1.02x faster                                          |
| hexiom                 | 5.99 ms                                                                | 5.87 ms: 1.02x faster                                         |
| mypy2                  | 328 ms                                                                 | 322 ms: 1.02x faster                                          |
| deepcopy_memo          | 34.8 us                                                                | 34.1 us: 1.02x faster                                         |
| generators             | 79.1 ms                                                                | 77.7 ms: 1.02x faster                                         |
| pprint_pformat         | 1.40 sec                                                               | 1.37 sec: 1.02x faster                                        |
| deepcopy_reduce        | 2.95 us                                                                | 2.90 us: 1.02x faster                                         |
| deepcopy               | 328 us                                                                 | 324 us: 1.01x faster                                          |
| raytrace               | 282 ms                                                                 | 279 ms: 1.01x faster                                          |
| chameleon              | 6.54 ms                                                                | 6.47 ms: 1.01x faster                                         |
| xml_etree_parse        | 149 ms                                                                 | 148 ms: 1.01x faster                                          |
| gunicorn               | 1.09 ms                                                                | 1.07 ms: 1.01x faster                                         |
| spectral_norm          | 94.9 ms                                                                | 93.9 ms: 1.01x faster                                         |
| telco                  | 6.47 ms                                                                | 6.40 ms: 1.01x faster                                         |
| pathlib                | 17.7 ms                                                                | 17.5 ms: 1.01x faster                                         |
| pickle                 | 10.2 us                                                                | 10.1 us: 1.01x faster                                         |
| dulwich_log            | 63.2 ms                                                                | 62.6 ms: 1.01x faster                                         |
| json_loads             | 23.9 us                                                                | 23.7 us: 1.01x faster                                         |
| nbody                  | 94.7 ms                                                                | 94.0 ms: 1.01x faster                                         |
| create_gc_cycles       | 1.49 ms                                                                | 1.48 ms: 1.01x faster                                         |
| sqlglot_optimize       | 50.7 ms                                                                | 50.4 ms: 1.01x faster                                         |
| sqlglot_parse          | 1.42 ms                                                                | 1.41 ms: 1.01x faster                                         |
| asyncio_tcp            | 500 ms                                                                 | 498 ms: 1.00x faster                                          |
| mako                   | 9.94 ms                                                                | 9.90 ms: 1.00x faster                                         |
| docutils               | 2.54 sec                                                               | 2.53 sec: 1.00x faster                                        |
| xml_etree_generate     | 80.5 ms                                                                | 80.2 ms: 1.00x faster                                         |
| python_startup         | 8.92 ms                                                                | 8.90 ms: 1.00x faster                                         |
| python_startup_no_site | 6.47 ms                                                                | 6.46 ms: 1.00x faster                                         |
| scimark_fft            | 306 ms                                                                 | 307 ms: 1.00x slower                                          |
| 2to3                   | 250 ms                                                                 | 251 ms: 1.00x slower                                          |
| pickle_list            | 4.12 us                                                                | 4.15 us: 1.01x slower                                         |
| logging_format         | 6.34 us                                                                | 6.39 us: 1.01x slower                                         |
| scimark_monte_carlo    | 65.0 ms                                                                | 65.5 ms: 1.01x slower                                         |
| pyflate                | 399 ms                                                                 | 403 ms: 1.01x slower                                          |
| logging_simple         | 5.78 us                                                                | 5.83 us: 1.01x slower                                         |
| scimark_sor            | 106 ms                                                                 | 106 ms: 1.01x slower                                          |
| coverage               | 98.5 ms                                                                | 99.3 ms: 1.01x slower                                         |
| unpickle_pure_python   | 196 us                                                                 | 198 us: 1.01x slower                                          |
| thrift                 | 752 us                                                                 | 760 us: 1.01x slower                                          |
| pidigits               | 190 ms                                                                 | 193 ms: 1.02x slower                                          |
| regex_v8               | 21.2 ms                                                                | 21.6 ms: 1.02x slower                                         |
| fannkuch               | 359 ms                                                                 | 366 ms: 1.02x slower                                          |
| genshi_text            | 20.5 ms                                                                | 20.9 ms: 1.02x slower                                         |
| logging_silent         | 91.8 ns                                                                | 94.1 ns: 1.03x slower                                         |
| pickle_pure_python     | 284 us                                                                 | 291 us: 1.03x slower                                          |
| unpickle_list          | 4.97 us                                                                | 5.13 us: 1.03x slower                                         |
| genshi_xml             | 46.1 ms                                                                | 47.8 ms: 1.04x slower                                         |
| unpickle               | 13.1 us                                                                | 13.7 us: 1.04x slower                                         |
| go                     | 132 ms                                                                 | 137 ms: 1.04x slower                                          |
| unpack_sequence        | 42.5 ns                                                                | 44.4 ns: 1.05x slower                                         |
| mdp                    | 2.52 sec                                                               | 2.66 sec: 1.06x slower                                        |
| regex_effbot           | 3.32 ms                                                                | 3.66 ms: 1.10x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (23): html5lib, async_tree_memoization, coroutines, json, float, tornado_http, sqlglot_transpile, xml_etree_process, async_generators, regex_dna, scimark_sparse_mat_mult, bench_thread_pool, bench_mp_pool, regex_compile, sqlite_synth, async_tree_cpu_io_mixed, aiohttp, deltablue, crypto_pyaes, scimark_lu, richards, pycparser, djangocms
