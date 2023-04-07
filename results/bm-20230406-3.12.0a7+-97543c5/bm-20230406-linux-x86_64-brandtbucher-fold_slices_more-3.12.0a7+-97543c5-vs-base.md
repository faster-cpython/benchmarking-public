
# Results vs. base

- fork: brandtbucher
- ref: fold_slices_more
- machine: linux-x86_64
- commit hash: 97543c5
- commit date: 2023-04-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 6.27 ms                                                                | 6.41 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                     |
| float          | 73.5 ms                                                                | 74.7 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 22.5 ms                                                                | 21.6 ms: 1.04x faster                                                    |
| regex_effbot   | 3.48 ms                                                                | 3.41 ms: 1.02x faster                                                    |
| regex_compile  | 133 ms                                                                 | 132 ms: 1.00x faster                                                     |
| regex_dna      | 204 ms                                                                 | 204 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict        | 32.6 us                                                                | 31.9 us: 1.02x faster                                                    |
| pickle             | 10.7 us                                                                | 10.6 us: 1.01x faster                                                    |
| unpickle_list      | 5.11 us                                                                | 5.05 us: 1.01x faster                                                    |
| json_dumps         | 9.47 ms                                                                | 9.37 ms: 1.01x faster                                                    |
| pickle_pure_python | 289 us                                                                 | 287 us: 1.01x faster                                                     |
| xml_etree_parse    | 146 ms                                                                 | 147 ms: 1.01x slower                                                     |
| pickle_list        | 4.35 us                                                                | 4.43 us: 1.02x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (6): unpickle_pure_python, json_loads, xml_etree_generate, xml_etree_iterparse, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.81 ms                                                                | 8.82 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.51 ms                                                                | 6.52 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.9 ms                                                                | 21.1 ms: 1.04x faster                                                    |
| django_template | 32.7 ms                                                                | 32.4 ms: 1.01x faster                                                    |
| mako            | 9.89 ms                                                                | 10.1 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| richards                | 44.4 ms                                                                | 41.4 ms: 1.07x faster                                                    |
| regex_v8                | 22.5 ms                                                                | 21.6 ms: 1.04x faster                                                    |
| genshi_text             | 21.9 ms                                                                | 21.1 ms: 1.04x faster                                                    |
| unpack_sequence         | 44.6 ns                                                                | 43.5 ns: 1.03x faster                                                    |
| coverage                | 98.7 ms                                                                | 96.3 ms: 1.03x faster                                                    |
| pickle_dict             | 32.6 us                                                                | 31.9 us: 1.02x faster                                                    |
| chaos                   | 66.9 ms                                                                | 65.4 ms: 1.02x faster                                                    |
| thrift                  | 800 us                                                                 | 782 us: 1.02x faster                                                     |
| regex_effbot            | 3.48 ms                                                                | 3.41 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult | 4.34 ms                                                                | 4.27 ms: 1.02x faster                                                    |
| asyncio_tcp             | 507 ms                                                                 | 500 ms: 1.01x faster                                                     |
| pickle                  | 10.7 us                                                                | 10.6 us: 1.01x faster                                                    |
| unpickle_list           | 5.11 us                                                                | 5.05 us: 1.01x faster                                                    |
| hexiom                  | 5.99 ms                                                                | 5.92 ms: 1.01x faster                                                    |
| pathlib                 | 18.3 ms                                                                | 18.1 ms: 1.01x faster                                                    |
| pycparser               | 1.16 sec                                                               | 1.15 sec: 1.01x faster                                                   |
| json_dumps              | 9.47 ms                                                                | 9.37 ms: 1.01x faster                                                    |
| sqlglot_optimize        | 50.9 ms                                                                | 50.4 ms: 1.01x faster                                                    |
| sqlalchemy_declarative  | 137 ms                                                                 | 136 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.94 us                                                                | 2.92 us: 1.01x faster                                                    |
| django_template         | 32.7 ms                                                                | 32.4 ms: 1.01x faster                                                    |
| pickle_pure_python      | 289 us                                                                 | 287 us: 1.01x faster                                                     |
| sqlglot_transpile       | 1.51 ms                                                                | 1.50 ms: 1.01x faster                                                    |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.01x faster                                                    |
| gunicorn                | 1.09 ms                                                                | 1.09 ms: 1.00x faster                                                    |
| regex_compile           | 133 ms                                                                 | 132 ms: 1.00x faster                                                     |
| mypy2                   | 336 ms                                                                 | 334 ms: 1.00x faster                                                     |
| raytrace                | 284 ms                                                                 | 283 ms: 1.00x faster                                                     |
| dulwich_log             | 63.3 ms                                                                | 63.1 ms: 1.00x faster                                                    |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                     |
| python_startup          | 8.81 ms                                                                | 8.82 ms: 1.00x slower                                                    |
| python_startup_no_site  | 6.51 ms                                                                | 6.52 ms: 1.00x slower                                                    |
| regex_dna               | 204 ms                                                                 | 204 ms: 1.00x slower                                                     |
| go                      | 138 ms                                                                 | 138 ms: 1.00x slower                                                     |
| sympy_str               | 282 ms                                                                 | 284 ms: 1.00x slower                                                     |
| sympy_integrate         | 20.3 ms                                                                | 20.4 ms: 1.01x slower                                                    |
| meteor_contest          | 102 ms                                                                 | 103 ms: 1.01x slower                                                     |
| deepcopy                | 324 us                                                                 | 326 us: 1.01x slower                                                     |
| scimark_fft             | 312 ms                                                                 | 314 ms: 1.01x slower                                                     |
| mdp                     | 2.51 sec                                                               | 2.53 sec: 1.01x slower                                                   |
| sympy_expand            | 456 ms                                                                 | 460 ms: 1.01x slower                                                     |
| json                    | 4.58 ms                                                                | 4.63 ms: 1.01x slower                                                    |
| pyflate                 | 422 ms                                                                 | 425 ms: 1.01x slower                                                     |
| xml_etree_parse         | 146 ms                                                                 | 147 ms: 1.01x slower                                                     |
| pprint_pformat          | 1.40 sec                                                               | 1.42 sec: 1.01x slower                                                   |
| deepcopy_memo           | 33.9 us                                                                | 34.3 us: 1.01x slower                                                    |
| pprint_safe_repr        | 685 ms                                                                 | 694 ms: 1.01x slower                                                     |
| float                   | 73.5 ms                                                                | 74.7 ms: 1.02x slower                                                    |
| mako                    | 9.89 ms                                                                | 10.1 ms: 1.02x slower                                                    |
| pickle_list             | 4.35 us                                                                | 4.43 us: 1.02x slower                                                    |
| scimark_sor             | 110 ms                                                                 | 113 ms: 1.02x slower                                                     |
| scimark_monte_carlo     | 66.8 ms                                                                | 68.2 ms: 1.02x slower                                                    |
| scimark_lu              | 107 ms                                                                 | 109 ms: 1.02x slower                                                     |
| chameleon               | 6.27 ms                                                                | 6.41 ms: 1.02x slower                                                    |
| crypto_pyaes            | 72.2 ms                                                                | 73.9 ms: 1.02x slower                                                    |
| fannkuch                | 374 ms                                                                 | 383 ms: 1.02x slower                                                     |
| comprehensions          | 21.4 us                                                                | 21.9 us: 1.03x slower                                                    |
| generators              | 29.1 ms                                                                | 29.9 ms: 1.03x slower                                                    |
| nqueens                 | 79.6 ms                                                                | 82.6 ms: 1.04x slower                                                    |
| spectral_norm           | 91.3 ms                                                                | 95.1 ms: 1.04x slower                                                    |
| create_gc_cycles        | 1.46 ms                                                                | 1.52 ms: 1.05x slower                                                    |
| gc_traversal            | 3.65 ms                                                                | 3.97 ms: 1.09x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (32): async_tree_memoization, html5lib, logging_simple, async_tree_io, logging_format, async_tree_cpu_io_mixed, unpickle_pure_python, async_generators, sqlglot_normalize, tornado_http, genshi_xml, deltablue, json_loads, sqlalchemy_imperative, sqlite_synth, 2to3, xml_etree_generate, nbody, bench_mp_pool, async_tree_none, sympy_sum, djangocms, bench_thread_pool, logging_silent, docutils, xml_etree_iterparse, sqlglot_parse, xml_etree_process, dask, coroutines, telco, unpickle
