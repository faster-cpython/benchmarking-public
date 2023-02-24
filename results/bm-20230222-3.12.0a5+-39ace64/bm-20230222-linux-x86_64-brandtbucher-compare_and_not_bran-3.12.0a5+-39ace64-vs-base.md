
# Results vs. base

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 39ace64
- commit date: 2023-02-22
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                 | 249 ms: 1.00x slower                                                         |
| chameleon      | 6.50 ms                                                                | 6.43 ms: 1.01x faster                                                        |
| docutils       | 2.54 sec                                                               | 2.55 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                 | 193 ms: 1.03x faster                                                         |
| float          | 72.0 ms                                                                | 73.4 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                                | 22.0 ms: 1.00x slower                                                        |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                         |
| regex_dna      | 210 ms                                                                 | 216 ms: 1.02x slower                                                         |
| regex_effbot   | 3.29 ms                                                                | 3.52 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps          | 9.56 ms                                                                | 9.43 ms: 1.01x faster                                                        |
| xml_etree_process   | 55.0 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| json_loads          | 24.1 us                                                                | 24.0 us: 1.01x faster                                                        |
| xml_etree_generate  | 80.8 ms                                                                | 80.4 ms: 1.00x faster                                                        |
| xml_etree_iterparse | 98.9 ms                                                                | 99.5 ms: 1.01x slower                                                        |
| pickle_pure_python  | 284 us                                                                 | 286 us: 1.01x slower                                                         |
| pickle              | 10.1 us                                                                | 10.2 us: 1.01x slower                                                        |
| unpickle_list       | 4.97 us                                                                | 5.02 us: 1.01x slower                                                        |
| pickle_dict         | 30.4 us                                                                | 30.9 us: 1.02x slower                                                        |
| xml_etree_parse     | 148 ms                                                                 | 150 ms: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): unpickle, pickle_list, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.51 ms                                                                | 6.54 ms: 1.00x slower                                                        |
| python_startup         | 8.98 ms                                                                | 9.02 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 47.4 ms                                                                | 46.7 ms: 1.02x faster                                                        |
| django_template | 32.9 ms                                                                | 32.6 ms: 1.01x faster                                                        |
| mako            | 9.75 ms                                                                | 9.80 ms: 1.00x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits               | 197 ms                                                                 | 193 ms: 1.03x faster                                                         |
| scimark_monte_carlo    | 67.8 ms                                                                | 66.2 ms: 1.02x faster                                                        |
| generators             | 30.2 ms                                                                | 29.6 ms: 1.02x faster                                                        |
| hexiom                 | 6.01 ms                                                                | 5.90 ms: 1.02x faster                                                        |
| logging_silent         | 91.9 ns                                                                | 90.4 ns: 1.02x faster                                                        |
| genshi_xml             | 47.4 ms                                                                | 46.7 ms: 1.02x faster                                                        |
| json_dumps             | 9.56 ms                                                                | 9.43 ms: 1.01x faster                                                        |
| sqlite_synth           | 2.64 us                                                                | 2.61 us: 1.01x faster                                                        |
| json                   | 4.64 ms                                                                | 4.58 ms: 1.01x faster                                                        |
| chameleon              | 6.50 ms                                                                | 6.43 ms: 1.01x faster                                                        |
| sqlglot_transpile      | 1.70 ms                                                                | 1.68 ms: 1.01x faster                                                        |
| sqlglot_parse          | 1.41 ms                                                                | 1.39 ms: 1.01x faster                                                        |
| xml_etree_process      | 55.0 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| django_template        | 32.9 ms                                                                | 32.6 ms: 1.01x faster                                                        |
| async_tree_io          | 1.32 sec                                                               | 1.31 sec: 1.01x faster                                                       |
| json_loads             | 24.1 us                                                                | 24.0 us: 1.01x faster                                                        |
| sqlglot_normalize      | 103 ms                                                                 | 102 ms: 1.00x faster                                                         |
| xml_etree_generate     | 80.8 ms                                                                | 80.4 ms: 1.00x faster                                                        |
| gunicorn               | 1.09 ms                                                                | 1.08 ms: 1.00x faster                                                        |
| sympy_sum              | 166 ms                                                                 | 165 ms: 1.00x faster                                                         |
| sympy_integrate        | 20.3 ms                                                                | 20.4 ms: 1.00x slower                                                        |
| bench_thread_pool      | 787 us                                                                 | 790 us: 1.00x slower                                                         |
| python_startup_no_site | 6.51 ms                                                                | 6.54 ms: 1.00x slower                                                        |
| regex_v8               | 22.0 ms                                                                | 22.0 ms: 1.00x slower                                                        |
| sympy_expand           | 454 ms                                                                 | 455 ms: 1.00x slower                                                         |
| async_generators       | 407 ms                                                                 | 409 ms: 1.00x slower                                                         |
| python_startup         | 8.98 ms                                                                | 9.02 ms: 1.00x slower                                                        |
| 2to3                   | 248 ms                                                                 | 249 ms: 1.00x slower                                                         |
| mako                   | 9.75 ms                                                                | 9.80 ms: 1.00x slower                                                        |
| regex_compile          | 128 ms                                                                 | 128 ms: 1.00x slower                                                         |
| deepcopy               | 329 us                                                                 | 330 us: 1.00x slower                                                         |
| sympy_str              | 282 ms                                                                 | 284 ms: 1.01x slower                                                         |
| meteor_contest         | 102 ms                                                                 | 103 ms: 1.01x slower                                                         |
| docutils               | 2.54 sec                                                               | 2.55 sec: 1.01x slower                                                       |
| xml_etree_iterparse    | 98.9 ms                                                                | 99.5 ms: 1.01x slower                                                        |
| telco                  | 6.34 ms                                                                | 6.39 ms: 1.01x slower                                                        |
| logging_format         | 6.31 us                                                                | 6.36 us: 1.01x slower                                                        |
| nqueens                | 77.5 ms                                                                | 78.1 ms: 1.01x slower                                                        |
| pickle_pure_python     | 284 us                                                                 | 286 us: 1.01x slower                                                         |
| richards               | 42.1 ms                                                                | 42.4 ms: 1.01x slower                                                        |
| logging_simple         | 5.75 us                                                                | 5.80 us: 1.01x slower                                                        |
| fannkuch               | 360 ms                                                                 | 364 ms: 1.01x slower                                                         |
| pickle                 | 10.1 us                                                                | 10.2 us: 1.01x slower                                                        |
| unpickle_list          | 4.97 us                                                                | 5.02 us: 1.01x slower                                                        |
| create_gc_cycles       | 1.48 ms                                                                | 1.50 ms: 1.01x slower                                                        |
| pathlib                | 17.8 ms                                                                | 18.1 ms: 1.01x slower                                                        |
| pickle_dict            | 30.4 us                                                                | 30.9 us: 1.02x slower                                                        |
| raytrace               | 278 ms                                                                 | 283 ms: 1.02x slower                                                         |
| xml_etree_parse        | 148 ms                                                                 | 150 ms: 1.02x slower                                                         |
| pprint_safe_repr       | 675 ms                                                                 | 688 ms: 1.02x slower                                                         |
| coverage               | 96.3 ms                                                                | 98.2 ms: 1.02x slower                                                        |
| float                  | 72.0 ms                                                                | 73.4 ms: 1.02x slower                                                        |
| scimark_sor            | 106 ms                                                                 | 109 ms: 1.02x slower                                                         |
| regex_dna              | 210 ms                                                                 | 216 ms: 1.02x slower                                                         |
| pyflate                | 401 ms                                                                 | 412 ms: 1.03x slower                                                         |
| mdp                    | 2.44 sec                                                               | 2.52 sec: 1.03x slower                                                       |
| chaos                  | 64.8 ms                                                                | 67.0 ms: 1.03x slower                                                        |
| go                     | 132 ms                                                                 | 137 ms: 1.04x slower                                                         |
| async_tree_memoization | 635 ms                                                                 | 666 ms: 1.05x slower                                                         |
| regex_effbot           | 3.29 ms                                                                | 3.52 ms: 1.07x slower                                                        |
| gc_traversal           | 3.54 ms                                                                | 3.85 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (32): unpickle, spectral_norm, scimark_lu, pycparser, crypto_pyaes, genshi_text, nbody, coroutines, sqlglot_optimize, deepcopy_memo, asyncio_tcp, scimark_fft, aiohttp, dulwich_log, bench_mp_pool, mypy2, deepcopy_reduce, deltablue, pprint_pformat, tornado_http, async_tree_none, sqlalchemy_declarative, pickle_list, unpickle_pure_python, async_tree_cpu_io_mixed, thrift, unpack_sequence, dask, djangocms, scimark_sparse_mat_mult, sqlalchemy_imperative, html5lib
