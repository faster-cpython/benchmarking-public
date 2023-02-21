
# Results vs. base

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: cf0df30
- commit date: 2023-02-21
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| chameleon      | 6.50 ms                                                                | 6.38 ms: 1.02x faster                                                      |
| docutils       | 2.54 sec                                                               | 2.60 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 97.1 ms                                                                | 94.2 ms: 1.03x faster                                                      |
| pidigits       | 197 ms                                                                 | 192 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 205 ms: 1.02x faster                                                       |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                       |
| regex_v8       | 22.0 ms                                                                | 22.5 ms: 1.02x slower                                                      |
| regex_effbot   | 3.29 ms                                                                | 3.63 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle            | 13.8 us                                                                | 13.1 us: 1.05x faster                                                      |
| json_dumps          | 9.56 ms                                                                | 9.40 ms: 1.02x faster                                                      |
| xml_etree_process   | 55.0 ms                                                                | 54.5 ms: 1.01x faster                                                      |
| xml_etree_generate  | 80.8 ms                                                                | 80.0 ms: 1.01x faster                                                      |
| pickle_pure_python  | 284 us                                                                 | 282 us: 1.00x faster                                                       |
| pickle_dict         | 30.4 us                                                                | 30.4 us: 1.00x faster                                                      |
| pickle              | 10.1 us                                                                | 10.2 us: 1.01x slower                                                      |
| unpickle_list       | 4.97 us                                                                | 5.03 us: 1.01x slower                                                      |
| pickle_list         | 4.02 us                                                                | 4.13 us: 1.03x slower                                                      |
| xml_etree_iterparse | 98.9 ms                                                                | 103 ms: 1.04x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): json_loads, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 9.01 ms: 1.00x slower                                                      |
| python_startup_no_site | 6.51 ms                                                                | 6.54 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 47.4 ms                                                                | 46.5 ms: 1.02x faster                                                      |
| genshi_text     | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                      |
| django_template | 32.9 ms                                                                | 33.3 ms: 1.01x slower                                                      |
| mako            | 9.75 ms                                                                | 9.99 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle                | 13.8 us                                                                | 13.1 us: 1.05x faster                                                      |
| async_tree_memoization  | 635 ms                                                                 | 610 ms: 1.04x faster                                                       |
| nbody                   | 97.1 ms                                                                | 94.2 ms: 1.03x faster                                                      |
| coroutines              | 22.5 ms                                                                | 21.9 ms: 1.03x faster                                                      |
| pidigits                | 197 ms                                                                 | 192 ms: 1.03x faster                                                       |
| regex_dna               | 210 ms                                                                 | 205 ms: 1.02x faster                                                       |
| genshi_xml              | 47.4 ms                                                                | 46.5 ms: 1.02x faster                                                      |
| chameleon               | 6.50 ms                                                                | 6.38 ms: 1.02x faster                                                      |
| spectral_norm           | 96.3 ms                                                                | 94.5 ms: 1.02x faster                                                      |
| async_tree_io           | 1.32 sec                                                               | 1.30 sec: 1.02x faster                                                     |
| json_dumps              | 9.56 ms                                                                | 9.40 ms: 1.02x faster                                                      |
| crypto_pyaes            | 73.4 ms                                                                | 72.3 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.40 sec                                                               | 1.38 sec: 1.01x faster                                                     |
| scimark_monte_carlo     | 67.8 ms                                                                | 66.9 ms: 1.01x faster                                                      |
| json                    | 4.64 ms                                                                | 4.58 ms: 1.01x faster                                                      |
| genshi_text             | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                      |
| generators              | 30.2 ms                                                                | 29.9 ms: 1.01x faster                                                      |
| xml_etree_process       | 55.0 ms                                                                | 54.5 ms: 1.01x faster                                                      |
| xml_etree_generate      | 80.8 ms                                                                | 80.0 ms: 1.01x faster                                                      |
| scimark_sor             | 106 ms                                                                 | 106 ms: 1.01x faster                                                       |
| logging_format          | 6.31 us                                                                | 6.26 us: 1.01x faster                                                      |
| gunicorn                | 1.09 ms                                                                | 1.08 ms: 1.01x faster                                                      |
| aiohttp                 | 1.01 ms                                                                | 1.00 ms: 1.01x faster                                                      |
| fannkuch                | 360 ms                                                                 | 359 ms: 1.01x faster                                                       |
| pickle_pure_python      | 284 us                                                                 | 282 us: 1.00x faster                                                       |
| pickle_dict             | 30.4 us                                                                | 30.4 us: 1.00x faster                                                      |
| regex_compile           | 128 ms                                                                 | 128 ms: 1.00x slower                                                       |
| hexiom                  | 6.01 ms                                                                | 6.03 ms: 1.00x slower                                                      |
| python_startup          | 8.98 ms                                                                | 9.01 ms: 1.00x slower                                                      |
| python_startup_no_site  | 6.51 ms                                                                | 6.54 ms: 1.00x slower                                                      |
| mdp                     | 2.44 sec                                                               | 2.45 sec: 1.00x slower                                                     |
| go                      | 132 ms                                                                 | 133 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.70 ms                                                                | 1.71 ms: 1.01x slower                                                      |
| sqlglot_optimize        | 50.3 ms                                                                | 50.7 ms: 1.01x slower                                                      |
| pathlib                 | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                                      |
| scimark_lu              | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| coverage                | 96.3 ms                                                                | 97.2 ms: 1.01x slower                                                      |
| raytrace                | 278 ms                                                                 | 281 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.01x slower                                                      |
| sqlglot_parse           | 1.41 ms                                                                | 1.42 ms: 1.01x slower                                                      |
| create_gc_cycles        | 1.48 ms                                                                | 1.49 ms: 1.01x slower                                                      |
| telco                   | 6.34 ms                                                                | 6.42 ms: 1.01x slower                                                      |
| unpickle_list           | 4.97 us                                                                | 5.03 us: 1.01x slower                                                      |
| richards                | 42.1 ms                                                                | 42.6 ms: 1.01x slower                                                      |
| django_template         | 32.9 ms                                                                | 33.3 ms: 1.01x slower                                                      |
| deepcopy                | 329 us                                                                 | 333 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult | 3.98 ms                                                                | 4.03 ms: 1.01x slower                                                      |
| deepcopy_reduce         | 2.93 us                                                                | 2.98 us: 1.02x slower                                                      |
| gc_traversal            | 3.54 ms                                                                | 3.61 ms: 1.02x slower                                                      |
| sqlalchemy_declarative  | 136 ms                                                                 | 139 ms: 1.02x slower                                                       |
| chaos                   | 64.8 ms                                                                | 66.2 ms: 1.02x slower                                                      |
| docutils                | 2.54 sec                                                               | 2.60 sec: 1.02x slower                                                     |
| regex_v8                | 22.0 ms                                                                | 22.5 ms: 1.02x slower                                                      |
| mako                    | 9.75 ms                                                                | 9.99 ms: 1.02x slower                                                      |
| pickle_list             | 4.02 us                                                                | 4.13 us: 1.03x slower                                                      |
| deepcopy_memo           | 34.2 us                                                                | 35.2 us: 1.03x slower                                                      |
| pycparser               | 1.10 sec                                                               | 1.14 sec: 1.04x slower                                                     |
| xml_etree_iterparse     | 98.9 ms                                                                | 103 ms: 1.04x slower                                                       |
| unpack_sequence         | 42.2 ns                                                                | 44.7 ns: 1.06x slower                                                      |
| regex_effbot            | 3.29 ms                                                                | 3.63 ms: 1.10x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (33): async_tree_none, logging_silent, async_tree_cpu_io_mixed, sqlite_synth, dask, sympy_str, sympy_expand, mypy2, sympy_sum, sympy_integrate, deltablue, json_loads, asyncio_tcp, nqueens, pprint_safe_repr, async_generators, bench_mp_pool, 2to3, logging_simple, bench_thread_pool, pyflate, html5lib, unpickle_pure_python, dulwich_log, tornado_http, sqlglot_normalize, thrift, xml_etree_parse, meteor_contest, float, scimark_fft, sqlalchemy_imperative, djangocms
