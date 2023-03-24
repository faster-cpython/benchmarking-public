
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c4e4b91
- commit date: 2022-02-03
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 267 ms: 1.26x faster                                  |
| chameleon      | 9.13 ms                                                             | 6.95 ms: 1.31x faster                                 |
| html5lib       | 86.4 ms                                                             | 67.9 ms: 1.27x faster                                 |
| tornado_http   | 129 ms                                                              | 106 ms: 1.22x faster                                  |
| Geometric mean | (ref)                                                               | 1.27x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 94.7 ms: 1.54x faster                                 |
| float          | 110 ms                                                              | 77.5 ms: 1.42x faster                                 |
| pidigits       | 190 ms                                                              | 190 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                               | 1.30x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 140 ms: 1.26x faster                                  |
| regex_v8       | 24.9 ms                                                             | 24.0 ms: 1.04x faster                                 |
| regex_effbot   | 3.22 ms                                                             | 3.14 ms: 1.02x faster                                 |
| regex_dna      | 213 ms                                                              | 213 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                               | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 334 us: 1.37x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 57.0 ms: 1.31x faster                                 |
| unpickle_pure_python | 300 us                                                              | 249 us: 1.20x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 79.6 ms: 1.19x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.2 ms: 1.12x faster                                 |
| unpickle             | 15.0 us                                                             | 13.4 us: 1.11x faster                                 |
| json_loads           | 29.3 us                                                             | 26.7 us: 1.10x faster                                 |
| xml_etree_parse      | 164 ms                                                              | 153 ms: 1.07x faster                                  |
| pickle_list          | 4.73 us                                                             | 4.47 us: 1.06x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 106 ms: 1.05x faster                                  |
| pickle               | 10.2 us                                                             | 9.93 us: 1.03x faster                                 |
| pickle_dict          | 27.8 us                                                             | 28.1 us: 1.01x slower                                 |
| unpickle_list        | 4.94 us                                                             | 5.26 us: 1.07x slower                                 |
| Geometric mean       | (ref)                                                               | 1.11x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.13 ms: 1.74x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 5.92 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                               | 1.31x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.5 ms: 1.41x faster                                 |
| django_template | 45.8 ms                                                             | 35.4 ms: 1.30x faster                                 |
| Geometric mean  | (ref)                                                               | 1.35x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 4.13 ms: 1.77x faster                                 |
| python_startup          | 14.1 ms                                                             | 8.13 ms: 1.74x faster                                 |
| nbody                   | 146 ms                                                              | 94.7 ms: 1.54x faster                                 |
| scimark_sor             | 198 ms                                                              | 129 ms: 1.53x faster                                  |
| go                      | 226 ms                                                              | 147 ms: 1.53x faster                                  |
| logging_silent          | 169 ns                                                              | 113 ns: 1.50x faster                                  |
| scimark_monte_carlo     | 109 ms                                                              | 72.6 ms: 1.50x faster                                 |
| raytrace                | 470 ms                                                              | 321 ms: 1.47x faster                                  |
| richards                | 74.2 ms                                                             | 50.8 ms: 1.46x faster                                 |
| pyflate                 | 671 ms                                                              | 459 ms: 1.46x faster                                  |
| spectral_norm           | 150 ms                                                              | 104 ms: 1.44x faster                                  |
| unpack_sequence         | 65.6 ns                                                             | 46.0 ns: 1.42x faster                                 |
| logging_format          | 9.07 us                                                             | 6.37 us: 1.42x faster                                 |
| float                   | 110 ms                                                              | 77.5 ms: 1.42x faster                                 |
| chaos                   | 106 ms                                                              | 74.9 ms: 1.41x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.84 us: 1.41x faster                                 |
| mako                    | 14.7 ms                                                             | 10.5 ms: 1.41x faster                                 |
| hexiom                  | 9.50 ms                                                             | 6.76 ms: 1.41x faster                                 |
| crypto_pyaes            | 117 ms                                                              | 83.8 ms: 1.39x faster                                 |
| pickle_pure_python      | 457 us                                                              | 334 us: 1.37x faster                                  |
| scimark_lu              | 160 ms                                                              | 120 ms: 1.33x faster                                  |
| chameleon               | 9.13 ms                                                             | 6.95 ms: 1.31x faster                                 |
| xml_etree_process       | 74.8 ms                                                             | 57.0 ms: 1.31x faster                                 |
| django_template         | 45.8 ms                                                             | 35.4 ms: 1.30x faster                                 |
| pycparser               | 1.53 sec                                                            | 1.19 sec: 1.28x faster                                |
| thrift                  | 1.04 ms                                                             | 815 us: 1.27x faster                                  |
| html5lib                | 86.4 ms                                                             | 67.9 ms: 1.27x faster                                 |
| regex_compile           | 177 ms                                                              | 140 ms: 1.26x faster                                  |
| 2to3                    | 336 ms                                                              | 267 ms: 1.26x faster                                  |
| scimark_fft             | 425 ms                                                              | 347 ms: 1.23x faster                                  |
| tornado_http            | 129 ms                                                              | 106 ms: 1.22x faster                                  |
| fannkuch                | 485 ms                                                              | 400 ms: 1.21x faster                                  |
| unpickle_pure_python    | 300 us                                                              | 249 us: 1.20x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 79.6 ms: 1.19x faster                                 |
| dulwich_log             | 76.3 ms                                                             | 65.7 ms: 1.16x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 21.3 ms: 1.14x faster                                 |
| nqueens                 | 98.8 ms                                                             | 87.2 ms: 1.13x faster                                 |
| json_dumps              | 13.7 ms                                                             | 12.2 ms: 1.12x faster                                 |
| json                    | 5.41 ms                                                             | 4.84 ms: 1.12x faster                                 |
| unpickle                | 15.0 us                                                             | 13.4 us: 1.11x faster                                 |
| sqlite_synth            | 2.97 us                                                             | 2.71 us: 1.10x faster                                 |
| json_loads              | 29.3 us                                                             | 26.7 us: 1.10x faster                                 |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.09x faster                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 5.14 ms: 1.09x faster                                 |
| sympy_sum               | 185 ms                                                              | 170 ms: 1.09x faster                                  |
| sympy_str               | 328 ms                                                              | 304 ms: 1.08x faster                                  |
| sympy_expand            | 540 ms                                                              | 503 ms: 1.07x faster                                  |
| xml_etree_parse         | 164 ms                                                              | 153 ms: 1.07x faster                                  |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                 |
| pickle_list             | 4.73 us                                                             | 4.47 us: 1.06x faster                                 |
| xml_etree_iterparse     | 111 ms                                                              | 106 ms: 1.05x faster                                  |
| regex_v8                | 24.9 ms                                                             | 24.0 ms: 1.04x faster                                 |
| pickle                  | 10.2 us                                                             | 9.93 us: 1.03x faster                                 |
| regex_effbot            | 3.22 ms                                                             | 3.14 ms: 1.02x faster                                 |
| regex_dna               | 213 ms                                                              | 213 ms: 1.00x faster                                  |
| pidigits                | 190 ms                                                              | 190 ms: 1.00x slower                                  |
| pickle_dict             | 27.8 us                                                             | 28.1 us: 1.01x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 5.92 ms: 1.02x slower                                 |
| unpickle_list           | 4.94 us                                                             | 5.26 us: 1.07x slower                                 |
| Geometric mean          | (ref)                                                               | 1.23x faster                                          |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
