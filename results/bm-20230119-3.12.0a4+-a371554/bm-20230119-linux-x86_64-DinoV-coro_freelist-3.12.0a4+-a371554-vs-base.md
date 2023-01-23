
# Results vs. base

- fork: DinoV
- ref: coro_freelist
- machine: linux-x86_64
- commit hash: a371554
- commit date: 2023-01-19
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.01x faster                                           |
| chameleon      | 6.40 ms                                                                | 6.31 ms: 1.01x faster                                          |
| docutils       | 2.48 sec                                                               | 2.47 sec: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 72.6 ms                                                                | 71.7 ms: 1.01x faster                                          |
| pidigits       | 198 ms                                                                 | 190 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 203 ms                                                                 | 201 ms: 1.01x faster                                           |
| regex_effbot   | 3.40 ms                                                                | 3.36 ms: 1.01x faster                                          |
| regex_v8       | 21.7 ms                                                                | 21.2 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle              | 10.2 us                                                                | 10.1 us: 1.01x faster                                          |
| pickle_dict         | 30.8 us                                                                | 29.7 us: 1.03x faster                                          |
| pickle_list         | 4.22 us                                                                | 4.03 us: 1.05x faster                                          |
| pickle_pure_python  | 284 us                                                                 | 282 us: 1.01x faster                                           |
| unpickle            | 13.0 us                                                                | 13.2 us: 1.01x slower                                          |
| unpickle_list       | 4.91 us                                                                | 4.96 us: 1.01x slower                                          |
| xml_etree_iterparse | 106 ms                                                                 | 102 ms: 1.03x faster                                           |
| xml_etree_generate  | 76.8 ms                                                                | 77.1 ms: 1.00x slower                                          |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (5): json_dumps, json_loads, unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.84 ms                                                                | 8.86 ms: 1.00x slower                                          |
| python_startup_no_site | 6.40 ms                                                                | 6.42 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text    | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                          |
| genshi_xml     | 46.4 ms                                                                | 47.3 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20230118-linux-x86_64-python-a1e051a23736fdf3da81-3.12.0a4+-a1e051a | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3                   | 251 ms                                                                 | 250 ms: 1.01x faster                                           |
| async_generators       | 352 ms                                                                 | 357 ms: 1.01x slower                                           |
| chameleon              | 6.40 ms                                                                | 6.31 ms: 1.01x faster                                          |
| chaos                  | 66.8 ms                                                                | 67.9 ms: 1.02x slower                                          |
| bench_thread_pool      | 779 us                                                                 | 783 us: 1.00x slower                                           |
| coroutines             | 25.4 ms                                                                | 23.2 ms: 1.09x faster                                          |
| coverage               | 93.3 ms                                                                | 93.9 ms: 1.01x slower                                          |
| crypto_pyaes           | 76.0 ms                                                                | 74.5 ms: 1.02x faster                                          |
| deepcopy_reduce        | 2.91 us                                                                | 2.95 us: 1.01x slower                                          |
| deepcopy_memo          | 34.4 us                                                                | 33.4 us: 1.03x faster                                          |
| docutils               | 2.48 sec                                                               | 2.47 sec: 1.00x faster                                         |
| dulwich_log            | 62.2 ms                                                                | 62.0 ms: 1.00x faster                                          |
| fannkuch               | 368 ms                                                                 | 362 ms: 1.02x faster                                           |
| float                  | 72.6 ms                                                                | 71.7 ms: 1.01x faster                                          |
| create_gc_cycles       | 1.44 ms                                                                | 1.44 ms: 1.01x slower                                          |
| gc_traversal           | 4.03 ms                                                                | 4.29 ms: 1.07x slower                                          |
| generators             | 74.8 ms                                                                | 76.7 ms: 1.03x slower                                          |
| genshi_text            | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                          |
| genshi_xml             | 46.4 ms                                                                | 47.3 ms: 1.02x slower                                          |
| go                     | 138 ms                                                                 | 140 ms: 1.02x slower                                           |
| hexiom                 | 6.08 ms                                                                | 6.03 ms: 1.01x faster                                          |
| json                   | 4.66 ms                                                                | 4.59 ms: 1.02x faster                                          |
| logging_format         | 6.25 us                                                                | 6.34 us: 1.02x slower                                          |
| logging_silent         | 90.1 ns                                                                | 91.6 ns: 1.02x slower                                          |
| logging_simple         | 5.64 us                                                                | 5.74 us: 1.02x slower                                          |
| mdp                    | 2.51 sec                                                               | 2.52 sec: 1.00x slower                                         |
| meteor_contest         | 104 ms                                                                 | 106 ms: 1.02x slower                                           |
| nqueens                | 78.3 ms                                                                | 77.1 ms: 1.02x faster                                          |
| pathlib                | 17.9 ms                                                                | 18.1 ms: 1.01x slower                                          |
| pickle                 | 10.2 us                                                                | 10.1 us: 1.01x faster                                          |
| pickle_dict            | 30.8 us                                                                | 29.7 us: 1.03x faster                                          |
| pickle_list            | 4.22 us                                                                | 4.03 us: 1.05x faster                                          |
| pickle_pure_python     | 284 us                                                                 | 282 us: 1.01x faster                                           |
| pidigits               | 198 ms                                                                 | 190 ms: 1.04x faster                                           |
| pprint_safe_repr       | 677 ms                                                                 | 663 ms: 1.02x faster                                           |
| pprint_pformat         | 1.41 sec                                                               | 1.36 sec: 1.03x faster                                         |
| pycparser              | 1.09 sec                                                               | 1.08 sec: 1.01x faster                                         |
| pyflate                | 395 ms                                                                 | 402 ms: 1.02x slower                                           |
| python_startup         | 8.84 ms                                                                | 8.86 ms: 1.00x slower                                          |
| python_startup_no_site | 6.40 ms                                                                | 6.42 ms: 1.00x slower                                          |
| raytrace               | 280 ms                                                                 | 283 ms: 1.01x slower                                           |
| regex_dna              | 203 ms                                                                 | 201 ms: 1.01x faster                                           |
| regex_effbot           | 3.40 ms                                                                | 3.36 ms: 1.01x faster                                          |
| regex_v8               | 21.7 ms                                                                | 21.2 ms: 1.03x faster                                          |
| richards               | 43.1 ms                                                                | 42.2 ms: 1.02x faster                                          |
| scimark_fft            | 309 ms                                                                 | 314 ms: 1.02x slower                                           |
| scimark_monte_carlo    | 64.7 ms                                                                | 65.8 ms: 1.02x slower                                          |
| scimark_sor            | 106 ms                                                                 | 107 ms: 1.01x slower                                           |
| spectral_norm          | 96.2 ms                                                                | 93.8 ms: 1.03x faster                                          |
| sqlglot_optimize       | 50.7 ms                                                                | 50.6 ms: 1.00x faster                                          |
| sympy_expand           | 457 ms                                                                 | 453 ms: 1.01x faster                                           |
| sympy_sum              | 164 ms                                                                 | 163 ms: 1.01x faster                                           |
| sympy_str              | 283 ms                                                                 | 280 ms: 1.01x faster                                           |
| telco                  | 6.25 ms                                                                | 6.33 ms: 1.01x slower                                          |
| unpack_sequence        | 41.9 ns                                                                | 41.5 ns: 1.01x faster                                          |
| unpickle               | 13.0 us                                                                | 13.2 us: 1.01x slower                                          |
| unpickle_list          | 4.91 us                                                                | 4.96 us: 1.01x slower                                          |
| xml_etree_iterparse    | 106 ms                                                                 | 102 ms: 1.03x faster                                           |
| xml_etree_generate     | 76.8 ms                                                                | 77.1 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (32): aiohttp, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, asyncio_tcp, bench_mp_pool, dask, deepcopy, deltablue, django_template, djangocms, gunicorn, html5lib, json_dumps, json_loads, mako, mypy, nbody, regex_compile, scimark_lu, scimark_sparse_mat_mult, sqlglot_parse, sqlglot_transpile, sqlglot_normalize, sqlite_synth, sympy_integrate, thrift, tornado_http, unpickle_pure_python, xml_etree_parse, xml_etree_process
