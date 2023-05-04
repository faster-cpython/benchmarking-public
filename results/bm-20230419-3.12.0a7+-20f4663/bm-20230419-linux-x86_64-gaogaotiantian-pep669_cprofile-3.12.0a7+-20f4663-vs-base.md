
# Results vs. base

- fork: gaogaotiantian
- ref: pep669_cprofile
- machine: linux-x86_64
- commit hash: 20f4663
- commit date: 2023-04-19
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| chameleon      | 6.36 ms                                                                | 6.26 ms: 1.02x faster                                                     |
| docutils       | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                                | 21.3 ms: 1.06x faster                                                     |
| regex_compile  | 130 ms                                                                 | 131 ms: 1.01x slower                                                      |
| regex_effbot   | 3.49 ms                                                                | 3.53 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                                 | 207 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_list          | 4.38 us                                                                | 4.24 us: 1.03x faster                                                     |
| json_dumps           | 9.65 ms                                                                | 9.37 ms: 1.03x faster                                                     |
| pickle_dict          | 33.5 us                                                                | 32.6 us: 1.03x faster                                                     |
| json_loads           | 24.4 us                                                                | 24.1 us: 1.01x faster                                                     |
| xml_etree_parse      | 149 ms                                                                 | 147 ms: 1.01x faster                                                      |
| pickle_pure_python   | 285 us                                                                 | 283 us: 1.01x faster                                                      |
| unpickle_pure_python | 200 us                                                                 | 201 us: 1.01x slower                                                      |
| pickle               | 10.8 us                                                                | 10.9 us: 1.01x slower                                                     |
| unpickle_list        | 4.88 us                                                                | 4.97 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_generate, unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.88 ms                                                                | 8.87 ms: 1.00x faster                                                     |
| python_startup_no_site | 6.58 ms                                                                | 6.57 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 46.8 ms                                                                | 46.2 ms: 1.01x faster                                                     |
| django_template | 32.8 ms                                                                | 32.6 ms: 1.01x faster                                                     |
| mako            | 9.98 ms                                                                | 9.94 ms: 1.00x faster                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230413-linux-x86_64-python-7b95d23591f605fc05d4-3.12.0a7+-7b95d23 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                | 22.6 ms                                                                | 21.3 ms: 1.06x faster                                                     |
| spectral_norm           | 94.3 ms                                                                | 90.9 ms: 1.04x faster                                                     |
| pycparser               | 1.14 sec                                                               | 1.10 sec: 1.04x faster                                                    |
| scimark_fft             | 310 ms                                                                 | 300 ms: 1.03x faster                                                      |
| pickle_list             | 4.38 us                                                                | 4.24 us: 1.03x faster                                                     |
| chaos                   | 67.0 ms                                                                | 65.0 ms: 1.03x faster                                                     |
| json_dumps              | 9.65 ms                                                                | 9.37 ms: 1.03x faster                                                     |
| pickle_dict             | 33.5 us                                                                | 32.6 us: 1.03x faster                                                     |
| raytrace                | 283 ms                                                                 | 276 ms: 1.03x faster                                                      |
| nqueens                 | 81.3 ms                                                                | 79.5 ms: 1.02x faster                                                     |
| scimark_monte_carlo     | 67.2 ms                                                                | 66.0 ms: 1.02x faster                                                     |
| json                    | 4.73 ms                                                                | 4.65 ms: 1.02x faster                                                     |
| scimark_sor             | 110 ms                                                                 | 109 ms: 1.02x faster                                                      |
| chameleon               | 6.36 ms                                                                | 6.26 ms: 1.02x faster                                                     |
| scimark_lu              | 107 ms                                                                 | 106 ms: 1.02x faster                                                      |
| coverage                | 98.1 ms                                                                | 96.8 ms: 1.01x faster                                                     |
| pyflate                 | 418 ms                                                                 | 413 ms: 1.01x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                                | 1.47 ms: 1.01x faster                                                     |
| genshi_xml              | 46.8 ms                                                                | 46.2 ms: 1.01x faster                                                     |
| sqlglot_normalize       | 104 ms                                                                 | 102 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed | 727 ms                                                                 | 718 ms: 1.01x faster                                                      |
| sqlite_synth            | 2.63 us                                                                | 2.60 us: 1.01x faster                                                     |
| json_loads              | 24.4 us                                                                | 24.1 us: 1.01x faster                                                     |
| sqlglot_optimize        | 51.4 ms                                                                | 50.8 ms: 1.01x faster                                                     |
| dask                    | 492 ms                                                                 | 487 ms: 1.01x faster                                                      |
| xml_etree_parse         | 149 ms                                                                 | 147 ms: 1.01x faster                                                      |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                                     |
| pickle_pure_python      | 285 us                                                                 | 283 us: 1.01x faster                                                      |
| bench_thread_pool       | 786 us                                                                 | 781 us: 1.01x faster                                                      |
| pathlib                 | 17.1 ms                                                                | 17.0 ms: 1.01x faster                                                     |
| django_template         | 32.8 ms                                                                | 32.6 ms: 1.01x faster                                                     |
| asyncio_tcp             | 503 ms                                                                 | 500 ms: 1.00x faster                                                      |
| logging_silent          | 94.7 ns                                                                | 94.2 ns: 1.00x faster                                                     |
| hexiom                  | 5.98 ms                                                                | 5.96 ms: 1.00x faster                                                     |
| mako                    | 9.98 ms                                                                | 9.94 ms: 1.00x faster                                                     |
| python_startup          | 8.88 ms                                                                | 8.87 ms: 1.00x faster                                                     |
| python_startup_no_site  | 6.58 ms                                                                | 6.57 ms: 1.00x faster                                                     |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                      |
| sympy_integrate         | 20.2 ms                                                                | 20.3 ms: 1.00x slower                                                     |
| docutils                | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                                    |
| pprint_safe_repr        | 682 ms                                                                 | 685 ms: 1.00x slower                                                      |
| sympy_expand            | 452 ms                                                                 | 455 ms: 1.00x slower                                                      |
| unpickle_pure_python    | 200 us                                                                 | 201 us: 1.01x slower                                                      |
| logging_simple          | 5.71 us                                                                | 5.74 us: 1.01x slower                                                     |
| fannkuch                | 380 ms                                                                 | 383 ms: 1.01x slower                                                      |
| generators              | 28.1 ms                                                                | 28.3 ms: 1.01x slower                                                     |
| regex_compile           | 130 ms                                                                 | 131 ms: 1.01x slower                                                      |
| deepcopy_reduce         | 2.95 us                                                                | 2.97 us: 1.01x slower                                                     |
| regex_effbot            | 3.49 ms                                                                | 3.53 ms: 1.01x slower                                                     |
| pickle                  | 10.8 us                                                                | 10.9 us: 1.01x slower                                                     |
| crypto_pyaes            | 73.7 ms                                                                | 74.5 ms: 1.01x slower                                                     |
| sympy_str               | 277 ms                                                                 | 280 ms: 1.01x slower                                                      |
| coroutines              | 21.9 ms                                                                | 22.1 ms: 1.01x slower                                                     |
| pprint_pformat          | 1.40 sec                                                               | 1.41 sec: 1.01x slower                                                    |
| deepcopy                | 327 us                                                                 | 332 us: 1.01x slower                                                      |
| logging_format          | 6.31 us                                                                | 6.41 us: 1.02x slower                                                     |
| thrift                  | 778 us                                                                 | 791 us: 1.02x slower                                                      |
| unpickle_list           | 4.88 us                                                                | 4.97 us: 1.02x slower                                                     |
| regex_dna               | 204 ms                                                                 | 207 ms: 1.02x slower                                                      |
| gc_traversal            | 3.98 ms                                                                | 4.06 ms: 1.02x slower                                                     |
| mdp                     | 2.48 sec                                                               | 2.60 sec: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (34): djangocms, genshi_text, xml_etree_iterparse, deltablue, pylint, go, telco, sqlglot_parse, mypy2, sqlalchemy_declarative, bench_mp_pool, xml_etree_generate, float, async_tree_io, dulwich_log, richards, tornado_http, 2to3, deepcopy_memo, unpickle, sympy_sum, async_tree_memoization, async_generators, async_tree_none, aiohttp, html5lib, comprehensions, xml_etree_process, scimark_sparse_mat_mult, sqlglot_transpile, sqlalchemy_imperative, nbody, meteor_contest, unpack_sequence
