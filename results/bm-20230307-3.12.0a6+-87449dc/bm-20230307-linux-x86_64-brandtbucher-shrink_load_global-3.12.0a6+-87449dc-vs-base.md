
# Results vs. base

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 87449dc
- commit date: 2023-03-07
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| chameleon      | 6.36 ms                                                                | 6.43 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                                | 91.6 ms: 1.02x faster                                                      |
| pidigits       | 189 ms                                                                 | 197 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 205 ms                                                                 | 201 ms: 1.02x faster                                                       |
| regex_effbot   | 3.56 ms                                                                | 3.54 ms: 1.01x faster                                                      |
| regex_v8       | 21.9 ms                                                                | 21.8 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.62 ms                                                                | 9.49 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                                 | 99.3 ms: 1.01x faster                                                      |
| unpickle_pure_python | 204 us                                                                 | 201 us: 1.01x faster                                                       |
| pickle_list          | 4.16 us                                                                | 4.18 us: 1.01x slower                                                      |
| pickle_dict          | 31.0 us                                                                | 31.2 us: 1.01x slower                                                      |
| pickle_pure_python   | 286 us                                                                 | 290 us: 1.01x slower                                                       |
| unpickle             | 13.2 us                                                                | 13.4 us: 1.01x slower                                                      |
| unpickle_list        | 4.97 us                                                                | 5.13 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (5): json_loads, pickle, xml_etree_process, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.54 ms                                                                | 6.52 ms: 1.00x faster                                                      |
| python_startup         | 9.01 ms                                                                | 8.99 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.95 ms                                                                | 10.1 ms: 1.01x slower                                                      |
| django_template | 33.0 ms                                                                | 33.6 ms: 1.02x slower                                                      |
| genshi_xml      | 48.0 ms                                                                | 48.9 ms: 1.02x slower                                                      |
| genshi_text     | 21.5 ms                                                                | 21.9 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mdp                     | 2.55 sec                                                               | 2.47 sec: 1.03x faster                                                     |
| scimark_monte_carlo     | 68.3 ms                                                                | 66.8 ms: 1.02x faster                                                      |
| pycparser               | 1.13 sec                                                               | 1.11 sec: 1.02x faster                                                     |
| crypto_pyaes            | 74.2 ms                                                                | 72.8 ms: 1.02x faster                                                      |
| regex_dna               | 205 ms                                                                 | 201 ms: 1.02x faster                                                       |
| nbody                   | 93.1 ms                                                                | 91.6 ms: 1.02x faster                                                      |
| deltablue               | 3.27 ms                                                                | 3.23 ms: 1.01x faster                                                      |
| json_dumps              | 9.62 ms                                                                | 9.49 ms: 1.01x faster                                                      |
| logging_simple          | 5.96 us                                                                | 5.88 us: 1.01x faster                                                      |
| xml_etree_iterparse     | 101 ms                                                                 | 99.3 ms: 1.01x faster                                                      |
| unpickle_pure_python    | 204 us                                                                 | 201 us: 1.01x faster                                                       |
| scimark_sparse_mat_mult | 4.55 ms                                                                | 4.50 ms: 1.01x faster                                                      |
| sqlalchemy_declarative  | 139 ms                                                                 | 137 ms: 1.01x faster                                                       |
| chaos                   | 68.7 ms                                                                | 68.0 ms: 1.01x faster                                                      |
| coroutines              | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                      |
| deepcopy_memo           | 35.0 us                                                                | 34.7 us: 1.01x faster                                                      |
| hexiom                  | 6.26 ms                                                                | 6.20 ms: 1.01x faster                                                      |
| json                    | 4.63 ms                                                                | 4.60 ms: 1.01x faster                                                      |
| scimark_sor             | 108 ms                                                                 | 107 ms: 1.01x faster                                                       |
| gunicorn                | 1.09 ms                                                                | 1.08 ms: 1.01x faster                                                      |
| regex_effbot            | 3.56 ms                                                                | 3.54 ms: 1.01x faster                                                      |
| regex_v8                | 21.9 ms                                                                | 21.8 ms: 1.00x faster                                                      |
| richards                | 43.6 ms                                                                | 43.4 ms: 1.00x faster                                                      |
| python_startup_no_site  | 6.54 ms                                                                | 6.52 ms: 1.00x faster                                                      |
| python_startup          | 9.01 ms                                                                | 8.99 ms: 1.00x faster                                                      |
| bench_thread_pool       | 791 us                                                                 | 794 us: 1.00x slower                                                       |
| raytrace                | 288 ms                                                                 | 289 ms: 1.00x slower                                                       |
| sympy_sum               | 167 ms                                                                 | 168 ms: 1.00x slower                                                       |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.01x slower                                                      |
| pickle_list             | 4.16 us                                                                | 4.18 us: 1.01x slower                                                      |
| sympy_integrate         | 20.6 ms                                                                | 20.7 ms: 1.01x slower                                                      |
| thrift                  | 778 us                                                                 | 784 us: 1.01x slower                                                       |
| pickle_dict             | 31.0 us                                                                | 31.2 us: 1.01x slower                                                      |
| sqlglot_optimize        | 51.0 ms                                                                | 51.4 ms: 1.01x slower                                                      |
| deepcopy_reduce         | 3.01 us                                                                | 3.04 us: 1.01x slower                                                      |
| sympy_expand            | 462 ms                                                                 | 466 ms: 1.01x slower                                                       |
| spectral_norm           | 94.3 ms                                                                | 95.2 ms: 1.01x slower                                                      |
| generators              | 30.6 ms                                                                | 30.9 ms: 1.01x slower                                                      |
| chameleon               | 6.36 ms                                                                | 6.43 ms: 1.01x slower                                                      |
| mako                    | 9.95 ms                                                                | 10.1 ms: 1.01x slower                                                      |
| pickle_pure_python      | 286 us                                                                 | 290 us: 1.01x slower                                                       |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.01x slower                                                       |
| unpickle                | 13.2 us                                                                | 13.4 us: 1.01x slower                                                      |
| django_template         | 33.0 ms                                                                | 33.6 ms: 1.02x slower                                                      |
| go                      | 140 ms                                                                 | 142 ms: 1.02x slower                                                       |
| genshi_xml              | 48.0 ms                                                                | 48.9 ms: 1.02x slower                                                      |
| genshi_text             | 21.5 ms                                                                | 21.9 ms: 1.02x slower                                                      |
| sqlglot_transpile       | 1.73 ms                                                                | 1.77 ms: 1.02x slower                                                      |
| sqlglot_parse           | 1.44 ms                                                                | 1.47 ms: 1.02x slower                                                      |
| pprint_safe_repr        | 686 ms                                                                 | 700 ms: 1.02x slower                                                       |
| fannkuch                | 359 ms                                                                 | 367 ms: 1.02x slower                                                       |
| pprint_pformat          | 1.40 sec                                                               | 1.43 sec: 1.02x slower                                                     |
| pyflate                 | 407 ms                                                                 | 418 ms: 1.03x slower                                                       |
| logging_silent          | 93.6 ns                                                                | 96.4 ns: 1.03x slower                                                      |
| unpickle_list           | 4.97 us                                                                | 5.13 us: 1.03x slower                                                      |
| nqueens                 | 80.2 ms                                                                | 83.0 ms: 1.03x slower                                                      |
| pidigits                | 189 ms                                                                 | 197 ms: 1.04x slower                                                       |
| unpack_sequence         | 43.0 ns                                                                | 45.2 ns: 1.05x slower                                                      |
| gc_traversal            | 3.55 ms                                                                | 3.81 ms: 1.07x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (35): scimark_lu, html5lib, json_loads, async_tree_io, sympy_str, pickle, xml_etree_process, sqlite_synth, create_gc_cycles, coverage, mypy2, async_tree_memoization, docutils, deepcopy, dulwich_log, 2to3, bench_mp_pool, xml_etree_generate, scimark_fft, float, telco, asyncio_tcp, tornado_http, regex_compile, pathlib, xml_etree_parse, comprehensions, logging_format, meteor_contest, async_generators, dask, async_tree_none, sqlalchemy_imperative, djangocms, async_tree_cpu_io_mixed
