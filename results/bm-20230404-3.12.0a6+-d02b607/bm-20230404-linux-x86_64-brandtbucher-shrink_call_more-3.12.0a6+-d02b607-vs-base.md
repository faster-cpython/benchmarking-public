
# Results vs. base

- fork: brandtbucher
- ref: shrink_call_more
- machine: linux-x86_64
- commit hash: d02b607
- commit date: 2023-04-04
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.00x faster                                                     |
| chameleon      | 6.57 ms                                                                | 6.67 ms: 1.01x slower                                                    |
| docutils       | 2.53 sec                                                               | 2.54 sec: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 74.6 ms                                                                | 74.1 ms: 1.01x faster                                                    |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                                                | 21.7 ms: 1.01x faster                                                    |
| regex_compile  | 133 ms                                                                 | 132 ms: 1.01x faster                                                     |
| regex_effbot   | 3.41 ms                                                                | 3.69 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict         | 32.5 us                                                                | 31.4 us: 1.04x faster                                                    |
| unpickle            | 13.7 us                                                                | 13.4 us: 1.02x faster                                                    |
| xml_etree_iterparse | 102 ms                                                                 | 99.9 ms: 1.02x faster                                                    |
| pickle              | 10.6 us                                                                | 10.5 us: 1.01x faster                                                    |
| pickle_pure_python  | 288 us                                                                 | 284 us: 1.01x faster                                                     |
| xml_etree_parse     | 149 ms                                                                 | 148 ms: 1.01x faster                                                     |
| pickle_list         | 4.33 us                                                                | 4.36 us: 1.01x slower                                                    |
| unpickle_list       | 5.13 us                                                                | 5.17 us: 1.01x slower                                                    |
| json_loads          | 24.1 us                                                                | 24.3 us: 1.01x slower                                                    |
| xml_etree_process   | 55.8 ms                                                                | 56.4 ms: 1.01x slower                                                    |
| xml_etree_generate  | 80.8 ms                                                                | 82.1 ms: 1.02x slower                                                    |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.87 ms                                                                | 8.78 ms: 1.01x faster                                                    |
| python_startup_no_site | 6.55 ms                                                                | 6.49 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                                | 21.2 ms: 1.01x faster                                                    |
| mako            | 9.97 ms                                                                | 10.2 ms: 1.02x slower                                                    |
| genshi_xml      | 47.1 ms                                                                | 48.0 ms: 1.02x slower                                                    |
| django_template | 32.9 ms                                                                | 33.8 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                     | 2.69 sec                                                               | 2.55 sec: 1.06x faster                                                   |
| pycparser               | 1.15 sec                                                               | 1.09 sec: 1.05x faster                                                   |
| unpack_sequence         | 44.2 ns                                                                | 42.4 ns: 1.04x faster                                                    |
| pickle_dict             | 32.5 us                                                                | 31.4 us: 1.04x faster                                                    |
| json                    | 4.76 ms                                                                | 4.61 ms: 1.03x faster                                                    |
| chaos                   | 67.5 ms                                                                | 65.8 ms: 1.02x faster                                                    |
| unpickle                | 13.7 us                                                                | 13.4 us: 1.02x faster                                                    |
| xml_etree_iterparse     | 102 ms                                                                 | 99.9 ms: 1.02x faster                                                    |
| raytrace                | 283 ms                                                                 | 279 ms: 1.01x faster                                                     |
| pickle                  | 10.6 us                                                                | 10.5 us: 1.01x faster                                                    |
| pickle_pure_python      | 288 us                                                                 | 284 us: 1.01x faster                                                     |
| create_gc_cycles        | 1.49 ms                                                                | 1.48 ms: 1.01x faster                                                    |
| genshi_text             | 21.5 ms                                                                | 21.2 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult | 4.18 ms                                                                | 4.13 ms: 1.01x faster                                                    |
| python_startup          | 8.87 ms                                                                | 8.78 ms: 1.01x faster                                                    |
| python_startup_no_site  | 6.55 ms                                                                | 6.49 ms: 1.01x faster                                                    |
| go                      | 138 ms                                                                 | 137 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 3.01 us                                                                | 2.99 us: 1.01x faster                                                    |
| float                   | 74.6 ms                                                                | 74.1 ms: 1.01x faster                                                    |
| regex_v8                | 21.9 ms                                                                | 21.7 ms: 1.01x faster                                                    |
| coverage                | 96.7 ms                                                                | 96.1 ms: 1.01x faster                                                    |
| xml_etree_parse         | 149 ms                                                                 | 148 ms: 1.01x faster                                                     |
| logging_simple          | 5.79 us                                                                | 5.76 us: 1.01x faster                                                    |
| regex_compile           | 133 ms                                                                 | 132 ms: 1.01x faster                                                     |
| 2to3                    | 252 ms                                                                 | 251 ms: 1.00x faster                                                     |
| gunicorn                | 1.08 ms                                                                | 1.08 ms: 1.00x faster                                                    |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                     |
| sympy_integrate         | 20.4 ms                                                                | 20.5 ms: 1.00x slower                                                    |
| docutils                | 2.53 sec                                                               | 2.54 sec: 1.00x slower                                                   |
| sqlglot_normalize       | 105 ms                                                                 | 105 ms: 1.00x slower                                                     |
| comprehensions          | 23.7 us                                                                | 23.8 us: 1.01x slower                                                    |
| sqlglot_optimize        | 51.3 ms                                                                | 51.6 ms: 1.01x slower                                                    |
| sympy_str               | 283 ms                                                                 | 284 ms: 1.01x slower                                                     |
| pprint_safe_repr        | 690 ms                                                                 | 695 ms: 1.01x slower                                                     |
| deepcopy_memo           | 34.1 us                                                                | 34.4 us: 1.01x slower                                                    |
| pickle_list             | 4.33 us                                                                | 4.36 us: 1.01x slower                                                    |
| unpickle_list           | 5.13 us                                                                | 5.17 us: 1.01x slower                                                    |
| sympy_expand            | 460 ms                                                                 | 464 ms: 1.01x slower                                                     |
| async_generators        | 414 ms                                                                 | 417 ms: 1.01x slower                                                     |
| json_loads              | 24.1 us                                                                | 24.3 us: 1.01x slower                                                    |
| sympy_sum               | 165 ms                                                                 | 166 ms: 1.01x slower                                                     |
| telco                   | 6.51 ms                                                                | 6.57 ms: 1.01x slower                                                    |
| xml_etree_process       | 55.8 ms                                                                | 56.4 ms: 1.01x slower                                                    |
| pathlib                 | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                                    |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                     |
| crypto_pyaes            | 74.3 ms                                                                | 75.3 ms: 1.01x slower                                                    |
| chameleon               | 6.57 ms                                                                | 6.67 ms: 1.01x slower                                                    |
| spectral_norm           | 93.1 ms                                                                | 94.5 ms: 1.01x slower                                                    |
| deepcopy                | 328 us                                                                 | 333 us: 1.01x slower                                                     |
| sqlite_synth            | 2.62 us                                                                | 2.66 us: 1.02x slower                                                    |
| generators              | 28.8 ms                                                                | 29.3 ms: 1.02x slower                                                    |
| xml_etree_generate      | 80.8 ms                                                                | 82.1 ms: 1.02x slower                                                    |
| scimark_fft             | 304 ms                                                                 | 309 ms: 1.02x slower                                                     |
| deltablue               | 3.19 ms                                                                | 3.25 ms: 1.02x slower                                                    |
| sqlglot_transpile       | 1.72 ms                                                                | 1.75 ms: 1.02x slower                                                    |
| mako                    | 9.97 ms                                                                | 10.2 ms: 1.02x slower                                                    |
| sqlglot_parse           | 1.43 ms                                                                | 1.45 ms: 1.02x slower                                                    |
| genshi_xml              | 47.1 ms                                                                | 48.0 ms: 1.02x slower                                                    |
| hexiom                  | 6.03 ms                                                                | 6.16 ms: 1.02x slower                                                    |
| fannkuch                | 380 ms                                                                 | 388 ms: 1.02x slower                                                     |
| scimark_monte_carlo     | 66.9 ms                                                                | 68.6 ms: 1.03x slower                                                    |
| django_template         | 32.9 ms                                                                | 33.8 ms: 1.03x slower                                                    |
| nqueens                 | 80.0 ms                                                                | 82.7 ms: 1.03x slower                                                    |
| scimark_sor             | 111 ms                                                                 | 116 ms: 1.04x slower                                                     |
| pyflate                 | 419 ms                                                                 | 441 ms: 1.05x slower                                                     |
| regex_effbot            | 3.41 ms                                                                | 3.69 ms: 1.08x slower                                                    |
| gc_traversal            | 3.83 ms                                                                | 4.32 ms: 1.13x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (27): html5lib, logging_format, async_tree_cpu_io_mixed, tornado_http, thrift, mypy2, sqlalchemy_imperative, asyncio_tcp, json_dumps, richards, coroutines, async_tree_none, sqlalchemy_declarative, unpickle_pure_python, scimark_lu, pprint_pformat, djangocms, async_tree_io, bench_mp_pool, bench_thread_pool, regex_dna, dask, aiohttp, nbody, async_tree_memoization, dulwich_log, logging_silent
