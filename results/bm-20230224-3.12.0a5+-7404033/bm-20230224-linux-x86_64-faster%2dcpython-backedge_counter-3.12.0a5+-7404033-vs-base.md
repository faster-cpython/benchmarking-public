
# Results vs. base

- fork: faster-cpython
- ref: backedge_counter
- machine: linux-x86_64
- commit hash: 7404033
- commit date: 2023-02-24
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 248 ms: 1.00x faster                                                         |
| chameleon      | 6.34 ms                                                                | 6.48 ms: 1.02x slower                                                        |
| docutils       | 2.56 sec                                                               | 2.65 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 96.5 ms                                                                | 93.1 ms: 1.04x faster                                                        |
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                                         |
| float          | 73.7 ms                                                                | 72.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.38 ms                                                                | 3.27 ms: 1.03x faster                                                        |
| regex_compile  | 132 ms                                                                 | 131 ms: 1.01x faster                                                         |
| regex_v8       | 22.3 ms                                                                | 22.3 ms: 1.00x slower                                                        |
| regex_dna      | 210 ms                                                                 | 213 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 31.4 us                                                                | 30.3 us: 1.04x faster                                                        |
| pickle_list          | 4.16 us                                                                | 4.00 us: 1.04x faster                                                        |
| json_loads           | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| xml_etree_process    | 55.4 ms                                                                | 55.7 ms: 1.01x slower                                                        |
| unpickle_pure_python | 196 us                                                                 | 198 us: 1.01x slower                                                         |
| xml_etree_generate   | 80.2 ms                                                                | 81.2 ms: 1.01x slower                                                        |
| json_dumps           | 9.33 ms                                                                | 9.47 ms: 1.02x slower                                                        |
| pickle_pure_python   | 283 us                                                                 | 289 us: 1.02x slower                                                         |
| xml_etree_iterparse  | 99.4 ms                                                                | 104 ms: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (4): pickle, xml_etree_parse, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.00 ms                                                                | 9.00 ms: 1.00x slower                                                        |
| python_startup_no_site | 6.53 ms                                                                | 6.55 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 9.93 ms: 1.02x faster                                                        |
| django_template | 33.1 ms                                                                | 32.9 ms: 1.00x faster                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines             | 23.6 ms                                                                | 22.3 ms: 1.06x faster                                                        |
| pyflate                | 414 ms                                                                 | 397 ms: 1.04x faster                                                         |
| pickle_dict            | 31.4 us                                                                | 30.3 us: 1.04x faster                                                        |
| pickle_list            | 4.16 us                                                                | 4.00 us: 1.04x faster                                                        |
| nbody                  | 96.5 ms                                                                | 93.1 ms: 1.04x faster                                                        |
| regex_effbot           | 3.38 ms                                                                | 3.27 ms: 1.03x faster                                                        |
| djangocms              | 32.6 us                                                                | 31.7 us: 1.03x faster                                                        |
| scimark_fft            | 322 ms                                                                 | 313 ms: 1.03x faster                                                         |
| scimark_monte_carlo    | 67.0 ms                                                                | 65.4 ms: 1.02x faster                                                        |
| spectral_norm          | 94.5 ms                                                                | 92.4 ms: 1.02x faster                                                        |
| hexiom                 | 6.11 ms                                                                | 5.98 ms: 1.02x faster                                                        |
| coverage               | 99.0 ms                                                                | 97.1 ms: 1.02x faster                                                        |
| pprint_safe_repr       | 680 ms                                                                 | 667 ms: 1.02x faster                                                         |
| mako                   | 10.1 ms                                                                | 9.93 ms: 1.02x faster                                                        |
| unpack_sequence        | 44.2 ns                                                                | 43.5 ns: 1.02x faster                                                        |
| nqueens                | 80.9 ms                                                                | 79.4 ms: 1.02x faster                                                        |
| pidigits               | 193 ms                                                                 | 189 ms: 1.02x faster                                                         |
| float                  | 73.7 ms                                                                | 72.5 ms: 1.02x faster                                                        |
| logging_silent         | 94.7 ns                                                                | 93.2 ns: 1.02x faster                                                        |
| create_gc_cycles       | 1.50 ms                                                                | 1.48 ms: 1.02x faster                                                        |
| dulwich_log            | 63.7 ms                                                                | 62.8 ms: 1.01x faster                                                        |
| pathlib                | 18.3 ms                                                                | 18.1 ms: 1.01x faster                                                        |
| sqlglot_normalize      | 105 ms                                                                 | 104 ms: 1.01x faster                                                         |
| regex_compile          | 132 ms                                                                 | 131 ms: 1.01x faster                                                         |
| pprint_pformat         | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                       |
| raytrace               | 283 ms                                                                 | 280 ms: 1.01x faster                                                         |
| sympy_integrate        | 20.5 ms                                                                | 20.3 ms: 1.01x faster                                                        |
| sqlglot_transpile      | 1.72 ms                                                                | 1.71 ms: 1.01x faster                                                        |
| telco                  | 6.48 ms                                                                | 6.43 ms: 1.01x faster                                                        |
| mdp                    | 2.53 sec                                                               | 2.52 sec: 1.01x faster                                                       |
| crypto_pyaes           | 74.9 ms                                                                | 74.5 ms: 1.01x faster                                                        |
| chaos                  | 67.0 ms                                                                | 66.6 ms: 1.01x faster                                                        |
| sympy_sum              | 167 ms                                                                 | 166 ms: 1.01x faster                                                         |
| django_template        | 33.1 ms                                                                | 32.9 ms: 1.00x faster                                                        |
| sympy_str              | 284 ms                                                                 | 283 ms: 1.00x faster                                                         |
| mypy2                  | 333 ms                                                                 | 332 ms: 1.00x faster                                                         |
| sqlglot_parse          | 1.43 ms                                                                | 1.42 ms: 1.00x faster                                                        |
| sympy_expand           | 457 ms                                                                 | 455 ms: 1.00x faster                                                         |
| 2to3                   | 249 ms                                                                 | 248 ms: 1.00x faster                                                         |
| deepcopy               | 330 us                                                                 | 329 us: 1.00x faster                                                         |
| bench_thread_pool      | 789 us                                                                 | 786 us: 1.00x faster                                                         |
| aiohttp                | 1.01 ms                                                                | 1.00 ms: 1.00x faster                                                        |
| python_startup         | 9.00 ms                                                                | 9.00 ms: 1.00x slower                                                        |
| python_startup_no_site | 6.53 ms                                                                | 6.55 ms: 1.00x slower                                                        |
| regex_v8               | 22.3 ms                                                                | 22.3 ms: 1.00x slower                                                        |
| go                     | 134 ms                                                                 | 135 ms: 1.00x slower                                                         |
| json_loads             | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| xml_etree_process      | 55.4 ms                                                                | 55.7 ms: 1.01x slower                                                        |
| sqlglot_optimize       | 50.8 ms                                                                | 51.1 ms: 1.01x slower                                                        |
| gunicorn               | 1.08 ms                                                                | 1.09 ms: 1.01x slower                                                        |
| asyncio_tcp            | 502 ms                                                                 | 506 ms: 1.01x slower                                                         |
| generators             | 29.7 ms                                                                | 30.0 ms: 1.01x slower                                                        |
| deepcopy_memo          | 34.0 us                                                                | 34.4 us: 1.01x slower                                                        |
| meteor_contest         | 102 ms                                                                 | 103 ms: 1.01x slower                                                         |
| unpickle_pure_python   | 196 us                                                                 | 198 us: 1.01x slower                                                         |
| regex_dna              | 210 ms                                                                 | 213 ms: 1.01x slower                                                         |
| async_generators       | 417 ms                                                                 | 422 ms: 1.01x slower                                                         |
| xml_etree_generate     | 80.2 ms                                                                | 81.2 ms: 1.01x slower                                                        |
| logging_simple         | 5.71 us                                                                | 5.78 us: 1.01x slower                                                        |
| json_dumps             | 9.33 ms                                                                | 9.47 ms: 1.02x slower                                                        |
| fannkuch               | 359 ms                                                                 | 366 ms: 1.02x slower                                                         |
| scimark_lu             | 108 ms                                                                 | 110 ms: 1.02x slower                                                         |
| chameleon              | 6.34 ms                                                                | 6.48 ms: 1.02x slower                                                        |
| pickle_pure_python     | 283 us                                                                 | 289 us: 1.02x slower                                                         |
| richards               | 42.0 ms                                                                | 43.2 ms: 1.03x slower                                                        |
| docutils               | 2.56 sec                                                               | 2.65 sec: 1.04x slower                                                       |
| xml_etree_iterparse    | 99.4 ms                                                                | 104 ms: 1.05x slower                                                         |
| gc_traversal           | 3.83 ms                                                                | 4.07 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (25): async_tree_memoization, html5lib, dask, json, sqlalchemy_imperative, async_tree_none, scimark_sparse_mat_mult, async_tree_io, sqlalchemy_declarative, pycparser, sqlite_synth, genshi_xml, tornado_http, logging_format, pickle, genshi_text, bench_mp_pool, xml_etree_parse, deepcopy_reduce, deltablue, scimark_sor, unpickle_list, async_tree_cpu_io_mixed, unpickle, thrift
