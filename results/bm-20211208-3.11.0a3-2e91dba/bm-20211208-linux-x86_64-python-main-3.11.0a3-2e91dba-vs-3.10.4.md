
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 264 ms: 1.27x faster                                  |
| chameleon      | 9.13 ms                                                             | 7.44 ms: 1.23x faster                                 |
| html5lib       | 86.4 ms                                                             | 68.5 ms: 1.26x faster                                 |
| tornado_http   | 129 ms                                                              | 108 ms: 1.20x faster                                  |
| Geometric mean | (ref)                                                               | 1.24x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 96.1 ms: 1.52x faster                                 |
| float          | 110 ms                                                              | 79.2 ms: 1.39x faster                                 |
| pidigits       | 190 ms                                                              | 198 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                               | 1.26x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 139 ms: 1.28x faster                                  |
| regex_v8       | 24.9 ms                                                             | 24.5 ms: 1.02x faster                                 |
| regex_dna      | 213 ms                                                              | 212 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                               | 1.07x faster                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 347 us: 1.32x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 57.8 ms: 1.29x faster                                 |
| unpickle_pure_python | 300 us                                                              | 251 us: 1.19x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 80.8 ms: 1.17x faster                                 |
| json_loads           | 29.3 us                                                             | 25.6 us: 1.14x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 105 ms: 1.06x faster                                  |
| xml_etree_parse      | 164 ms                                                              | 156 ms: 1.05x faster                                  |
| pickle               | 10.2 us                                                             | 9.95 us: 1.03x faster                                 |
| unpickle             | 15.0 us                                                             | 14.6 us: 1.03x faster                                 |
| pickle_list          | 4.73 us                                                             | 4.68 us: 1.01x faster                                 |
| pickle_dict          | 27.8 us                                                             | 27.7 us: 1.00x faster                                 |
| unpickle_list        | 4.94 us                                                             | 5.21 us: 1.05x slower                                 |
| Geometric mean       | (ref)                                                               | 1.10x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.00 ms: 1.77x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 5.78 ms: 1.00x faster                                 |
| Geometric mean         | (ref)                                                               | 1.33x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 45.8 ms                                                             | 36.5 ms: 1.26x faster                                 |
| mako            | 14.7 ms                                                             | 11.9 ms: 1.24x faster                                 |
| Geometric mean  | (ref)                                                               | 1.25x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup          | 14.1 ms                                                             | 8.00 ms: 1.77x faster                                 |
| deltablue               | 7.30 ms                                                             | 4.54 ms: 1.61x faster                                 |
| logging_silent          | 169 ns                                                              | 110 ns: 1.53x faster                                  |
| nbody                   | 146 ms                                                              | 96.1 ms: 1.52x faster                                 |
| scimark_sor             | 198 ms                                                              | 130 ms: 1.52x faster                                  |
| scimark_monte_carlo     | 109 ms                                                              | 74.0 ms: 1.47x faster                                 |
| spectral_norm           | 150 ms                                                              | 104 ms: 1.45x faster                                  |
| scimark_lu              | 160 ms                                                              | 112 ms: 1.43x faster                                  |
| chaos                   | 106 ms                                                              | 73.9 ms: 1.43x faster                                 |
| go                      | 226 ms                                                              | 158 ms: 1.43x faster                                  |
| raytrace                | 470 ms                                                              | 333 ms: 1.41x faster                                  |
| pyflate                 | 671 ms                                                              | 477 ms: 1.41x faster                                  |
| hexiom                  | 9.50 ms                                                             | 6.77 ms: 1.40x faster                                 |
| logging_format          | 9.07 us                                                             | 6.49 us: 1.40x faster                                 |
| float                   | 110 ms                                                              | 79.2 ms: 1.39x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.97 us: 1.38x faster                                 |
| richards                | 74.2 ms                                                             | 54.5 ms: 1.36x faster                                 |
| unpack_sequence         | 65.6 ns                                                             | 49.2 ns: 1.33x faster                                 |
| crypto_pyaes            | 117 ms                                                              | 88.1 ms: 1.32x faster                                 |
| pickle_pure_python      | 457 us                                                              | 347 us: 1.32x faster                                  |
| xml_etree_process       | 74.8 ms                                                             | 57.8 ms: 1.29x faster                                 |
| scimark_fft             | 425 ms                                                              | 332 ms: 1.28x faster                                  |
| regex_compile           | 177 ms                                                              | 139 ms: 1.28x faster                                  |
| thrift                  | 1.04 ms                                                             | 814 us: 1.27x faster                                  |
| 2to3                    | 336 ms                                                              | 264 ms: 1.27x faster                                  |
| html5lib                | 86.4 ms                                                             | 68.5 ms: 1.26x faster                                 |
| fannkuch                | 485 ms                                                              | 386 ms: 1.26x faster                                  |
| django_template         | 45.8 ms                                                             | 36.5 ms: 1.26x faster                                 |
| pycparser               | 1.53 sec                                                            | 1.24 sec: 1.24x faster                                |
| mako                    | 14.7 ms                                                             | 11.9 ms: 1.24x faster                                 |
| chameleon               | 9.13 ms                                                             | 7.44 ms: 1.23x faster                                 |
| tornado_http            | 129 ms                                                              | 108 ms: 1.20x faster                                  |
| unpickle_pure_python    | 300 us                                                              | 251 us: 1.19x faster                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.77 ms: 1.18x faster                                 |
| xml_etree_generate      | 94.9 ms                                                             | 80.8 ms: 1.17x faster                                 |
| nqueens                 | 98.8 ms                                                             | 84.6 ms: 1.17x faster                                 |
| json_loads              | 29.3 us                                                             | 25.6 us: 1.14x faster                                 |
| dulwich_log             | 76.3 ms                                                             | 67.2 ms: 1.14x faster                                 |
| json                    | 5.41 ms                                                             | 4.83 ms: 1.12x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 21.7 ms: 1.12x faster                                 |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                 |
| sqlite_synth            | 2.97 us                                                             | 2.74 us: 1.09x faster                                 |
| sympy_sum               | 185 ms                                                              | 172 ms: 1.08x faster                                  |
| sympy_str               | 328 ms                                                              | 308 ms: 1.06x faster                                  |
| sympy_expand            | 540 ms                                                              | 509 ms: 1.06x faster                                  |
| xml_etree_iterparse     | 111 ms                                                              | 105 ms: 1.06x faster                                  |
| xml_etree_parse         | 164 ms                                                              | 156 ms: 1.05x faster                                  |
| pickle                  | 10.2 us                                                             | 9.95 us: 1.03x faster                                 |
| unpickle                | 15.0 us                                                             | 14.6 us: 1.03x faster                                 |
| pathlib                 | 19.8 ms                                                             | 19.4 ms: 1.02x faster                                 |
| regex_v8                | 24.9 ms                                                             | 24.5 ms: 1.02x faster                                 |
| telco                   | 6.67 ms                                                             | 6.56 ms: 1.02x faster                                 |
| pickle_list             | 4.73 us                                                             | 4.68 us: 1.01x faster                                 |
| regex_dna               | 213 ms                                                              | 212 ms: 1.01x faster                                  |
| pickle_dict             | 27.8 us                                                             | 27.7 us: 1.00x faster                                 |
| python_startup_no_site  | 5.80 ms                                                             | 5.78 ms: 1.00x faster                                 |
| pidigits                | 190 ms                                                              | 198 ms: 1.05x slower                                  |
| unpickle_list           | 4.94 us                                                             | 5.21 us: 1.05x slower                                 |
| Geometric mean          | (ref)                                                               | 1.22x faster                                          |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
