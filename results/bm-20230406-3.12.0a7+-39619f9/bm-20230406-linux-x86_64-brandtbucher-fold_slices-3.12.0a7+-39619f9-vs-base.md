
# Results vs. base

- fork: brandtbucher
- ref: fold_slices
- machine: linux-x86_64
- commit hash: 39619f9
- commit date: 2023-04-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.00x faster                                                |
| chameleon      | 6.27 ms                                                                | 6.49 ms: 1.04x slower                                               |
| docutils       | 2.53 sec                                                               | 2.54 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.48 ms                                                                | 3.45 ms: 1.01x faster                                               |
| regex_v8       | 22.5 ms                                                                | 22.4 ms: 1.01x faster                                               |
| regex_compile  | 133 ms                                                                 | 134 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list       | 5.11 us                                                                | 4.92 us: 1.04x faster                                               |
| json_loads          | 24.2 us                                                                | 24.1 us: 1.00x faster                                               |
| json_dumps          | 9.47 ms                                                                | 9.53 ms: 1.01x slower                                               |
| pickle              | 10.7 us                                                                | 10.9 us: 1.01x slower                                               |
| xml_etree_process   | 55.2 ms                                                                | 56.2 ms: 1.02x slower                                               |
| xml_etree_parse     | 146 ms                                                                 | 150 ms: 1.03x slower                                                |
| xml_etree_iterparse | 99.3 ms                                                                | 103 ms: 1.04x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (6): unpickle, unpickle_pure_python, pickle_dict, pickle_list, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.81 ms                                                                | 8.84 ms: 1.00x slower                                               |
| python_startup_no_site | 6.51 ms                                                                | 6.53 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.9 ms                                                                | 21.0 ms: 1.04x faster                                               |
| genshi_xml      | 47.0 ms                                                                | 47.6 ms: 1.01x slower                                               |
| mako            | 9.89 ms                                                                | 10.1 ms: 1.02x slower                                               |
| django_template | 32.7 ms                                                                | 33.4 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                        |

All benchmarks:
===============

| Benchmark              | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| richards               | 44.4 ms                                                                | 42.5 ms: 1.05x faster                                               |
| genshi_text            | 21.9 ms                                                                | 21.0 ms: 1.04x faster                                               |
| unpickle_list          | 5.11 us                                                                | 4.92 us: 1.04x faster                                               |
| thrift                 | 800 us                                                                 | 780 us: 1.03x faster                                                |
| go                     | 138 ms                                                                 | 134 ms: 1.02x faster                                                |
| coverage               | 98.7 ms                                                                | 96.7 ms: 1.02x faster                                               |
| telco                  | 6.44 ms                                                                | 6.32 ms: 1.02x faster                                               |
| pyflate                | 422 ms                                                                 | 414 ms: 1.02x faster                                                |
| unpack_sequence        | 44.6 ns                                                                | 43.9 ns: 1.02x faster                                               |
| async_generators       | 414 ms                                                                 | 408 ms: 1.02x faster                                                |
| chaos                  | 66.9 ms                                                                | 65.9 ms: 1.02x faster                                               |
| asyncio_tcp            | 507 ms                                                                 | 500 ms: 1.01x faster                                                |
| async_tree_none        | 522 ms                                                                 | 515 ms: 1.01x faster                                                |
| async_tree_io          | 1.30 sec                                                               | 1.28 sec: 1.01x faster                                              |
| pathlib                | 18.3 ms                                                                | 18.2 ms: 1.01x faster                                               |
| regex_effbot           | 3.48 ms                                                                | 3.45 ms: 1.01x faster                                               |
| aiohttp                | 1.01 ms                                                                | 1.01 ms: 1.01x faster                                               |
| gunicorn               | 1.09 ms                                                                | 1.09 ms: 1.01x faster                                               |
| regex_v8               | 22.5 ms                                                                | 22.4 ms: 1.01x faster                                               |
| json_loads             | 24.2 us                                                                | 24.1 us: 1.00x faster                                               |
| sqlglot_transpile      | 1.51 ms                                                                | 1.50 ms: 1.00x faster                                               |
| 2to3                   | 251 ms                                                                 | 250 ms: 1.00x faster                                                |
| python_startup         | 8.81 ms                                                                | 8.84 ms: 1.00x slower                                               |
| sqlglot_normalize      | 104 ms                                                                 | 105 ms: 1.00x slower                                                |
| python_startup_no_site | 6.51 ms                                                                | 6.53 ms: 1.00x slower                                               |
| sympy_sum              | 165 ms                                                                 | 166 ms: 1.01x slower                                                |
| docutils               | 2.53 sec                                                               | 2.54 sec: 1.01x slower                                              |
| deepcopy               | 324 us                                                                 | 326 us: 1.01x slower                                                |
| json_dumps             | 9.47 ms                                                                | 9.53 ms: 1.01x slower                                               |
| pprint_safe_repr       | 685 ms                                                                 | 690 ms: 1.01x slower                                                |
| regex_compile          | 133 ms                                                                 | 134 ms: 1.01x slower                                                |
| sympy_str              | 282 ms                                                                 | 285 ms: 1.01x slower                                                |
| sympy_integrate        | 20.3 ms                                                                | 20.5 ms: 1.01x slower                                               |
| json                   | 4.58 ms                                                                | 4.63 ms: 1.01x slower                                               |
| deepcopy_memo          | 33.9 us                                                                | 34.2 us: 1.01x slower                                               |
| dask                   | 502 ms                                                                 | 507 ms: 1.01x slower                                                |
| pickle                 | 10.7 us                                                                | 10.9 us: 1.01x slower                                               |
| genshi_xml             | 47.0 ms                                                                | 47.6 ms: 1.01x slower                                               |
| pprint_pformat         | 1.40 sec                                                               | 1.42 sec: 1.01x slower                                              |
| deepcopy_reduce        | 2.94 us                                                                | 2.99 us: 1.02x slower                                               |
| fannkuch               | 374 ms                                                                 | 380 ms: 1.02x slower                                                |
| nqueens                | 79.6 ms                                                                | 81.0 ms: 1.02x slower                                               |
| crypto_pyaes           | 72.2 ms                                                                | 73.5 ms: 1.02x slower                                               |
| scimark_sor            | 110 ms                                                                 | 112 ms: 1.02x slower                                                |
| sqlalchemy_imperative  | 17.6 ms                                                                | 17.9 ms: 1.02x slower                                               |
| xml_etree_process      | 55.2 ms                                                                | 56.2 ms: 1.02x slower                                               |
| deltablue              | 3.24 ms                                                                | 3.30 ms: 1.02x slower                                               |
| mako                   | 9.89 ms                                                                | 10.1 ms: 1.02x slower                                               |
| django_template        | 32.7 ms                                                                | 33.4 ms: 1.02x slower                                               |
| sympy_expand           | 456 ms                                                                 | 467 ms: 1.02x slower                                                |
| scimark_monte_carlo    | 66.8 ms                                                                | 68.3 ms: 1.02x slower                                               |
| xml_etree_parse        | 146 ms                                                                 | 150 ms: 1.03x slower                                                |
| logging_silent         | 94.9 ns                                                                | 97.7 ns: 1.03x slower                                               |
| chameleon              | 6.27 ms                                                                | 6.49 ms: 1.04x slower                                               |
| xml_etree_iterparse    | 99.3 ms                                                                | 103 ms: 1.04x slower                                                |
| create_gc_cycles       | 1.46 ms                                                                | 1.51 ms: 1.04x slower                                               |
| scimark_lu             | 107 ms                                                                 | 111 ms: 1.04x slower                                                |
| spectral_norm          | 91.3 ms                                                                | 96.1 ms: 1.05x slower                                               |
| gc_traversal           | 3.65 ms                                                                | 4.10 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (35): async_tree_memoization, unpickle, scimark_sparse_mat_mult, html5lib, mypy2, sqlalchemy_declarative, unpickle_pure_python, sqlite_synth, nbody, pycparser, meteor_contest, scimark_fft, mdp, pickle_dict, hexiom, logging_simple, dulwich_log, pickle_list, pidigits, async_tree_cpu_io_mixed, bench_mp_pool, sqlglot_optimize, tornado_http, bench_thread_pool, raytrace, float, coroutines, comprehensions, regex_dna, sqlglot_parse, xml_etree_generate, pickle_pure_python, generators, logging_format, djangocms
