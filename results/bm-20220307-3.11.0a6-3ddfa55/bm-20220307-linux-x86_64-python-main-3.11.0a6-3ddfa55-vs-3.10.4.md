
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 268 ms: 1.25x faster                                  |
| chameleon      | 9.13 ms                                                             | 6.93 ms: 1.32x faster                                 |
| html5lib       | 86.4 ms                                                             | 68.6 ms: 1.26x faster                                 |
| tornado_http   | 129 ms                                                              | 99.2 ms: 1.30x faster                                 |
| Geometric mean | (ref)                                                               | 1.28x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 97.7 ms: 1.49x faster                                 |
| float          | 110 ms                                                              | 78.7 ms: 1.40x faster                                 |
| pidigits       | 190 ms                                                              | 208 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                               | 1.24x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 140 ms: 1.27x faster                                  |
| regex_v8       | 24.9 ms                                                             | 23.0 ms: 1.08x faster                                 |
| regex_dna      | 213 ms                                                              | 221 ms: 1.04x slower                                  |
| regex_effbot   | 3.22 ms                                                             | 3.49 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                               | 1.05x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 335 us: 1.36x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 56.0 ms: 1.33x faster                                 |
| unpickle_pure_python | 300 us                                                              | 246 us: 1.22x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 79.6 ms: 1.19x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 105 ms: 1.06x faster                                  |
| unpickle             | 15.0 us                                                             | 14.2 us: 1.06x faster                                 |
| pickle               | 10.2 us                                                             | 9.69 us: 1.06x faster                                 |
| pickle_list          | 4.73 us                                                             | 4.51 us: 1.05x faster                                 |
| xml_etree_parse      | 164 ms                                                              | 156 ms: 1.05x faster                                  |
| json_loads           | 29.3 us                                                             | 28.1 us: 1.04x faster                                 |
| pickle_dict          | 27.8 us                                                             | 28.1 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                               | 1.11x faster                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.20 ms: 1.73x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 6.07 ms: 1.05x slower                                 |
| Geometric mean         | (ref)                                                               | 1.28x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.6 ms: 1.39x faster                                 |
| django_template | 45.8 ms                                                             | 36.0 ms: 1.27x faster                                 |
| Geometric mean  | (ref)                                                               | 1.33x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 4.16 ms: 1.75x faster                                 |
| python_startup          | 14.1 ms                                                             | 8.20 ms: 1.73x faster                                 |
| scimark_sor             | 198 ms                                                              | 123 ms: 1.60x faster                                  |
| go                      | 226 ms                                                              | 148 ms: 1.53x faster                                  |
| richards                | 74.2 ms                                                             | 48.5 ms: 1.53x faster                                 |
| logging_silent          | 169 ns                                                              | 113 ns: 1.50x faster                                  |
| nbody                   | 146 ms                                                              | 97.7 ms: 1.49x faster                                 |
| logging_format          | 9.07 us                                                             | 6.08 us: 1.49x faster                                 |
| scimark_monte_carlo     | 109 ms                                                              | 72.9 ms: 1.49x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.52 us: 1.49x faster                                 |
| pyflate                 | 671 ms                                                              | 453 ms: 1.48x faster                                  |
| raytrace                | 470 ms                                                              | 318 ms: 1.48x faster                                  |
| chaos                   | 106 ms                                                              | 73.5 ms: 1.44x faster                                 |
| spectral_norm           | 150 ms                                                              | 107 ms: 1.40x faster                                  |
| float                   | 110 ms                                                              | 78.7 ms: 1.40x faster                                 |
| mako                    | 14.7 ms                                                             | 10.6 ms: 1.39x faster                                 |
| scimark_lu              | 160 ms                                                              | 115 ms: 1.39x faster                                  |
| crypto_pyaes            | 117 ms                                                              | 84.6 ms: 1.38x faster                                 |
| pickle_pure_python      | 457 us                                                              | 335 us: 1.36x faster                                  |
| hexiom                  | 9.50 ms                                                             | 7.04 ms: 1.35x faster                                 |
| xml_etree_process       | 74.8 ms                                                             | 56.0 ms: 1.33x faster                                 |
| chameleon               | 9.13 ms                                                             | 6.93 ms: 1.32x faster                                 |
| thrift                  | 1.04 ms                                                             | 789 us: 1.31x faster                                  |
| tornado_http            | 129 ms                                                              | 99.2 ms: 1.30x faster                                 |
| django_template         | 45.8 ms                                                             | 36.0 ms: 1.27x faster                                 |
| regex_compile           | 177 ms                                                              | 140 ms: 1.27x faster                                  |
| scimark_fft             | 425 ms                                                              | 336 ms: 1.26x faster                                  |
| pycparser               | 1.53 sec                                                            | 1.21 sec: 1.26x faster                                |
| html5lib                | 86.4 ms                                                             | 68.6 ms: 1.26x faster                                 |
| 2to3                    | 336 ms                                                              | 268 ms: 1.25x faster                                  |
| unpickle_pure_python    | 300 us                                                              | 246 us: 1.22x faster                                  |
| fannkuch                | 485 ms                                                              | 398 ms: 1.22x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 79.6 ms: 1.19x faster                                 |
| sqlite_synth            | 2.97 us                                                             | 2.51 us: 1.18x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 20.9 ms: 1.16x faster                                 |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.82 ms: 1.16x faster                                 |
| dulwich_log             | 76.3 ms                                                             | 66.5 ms: 1.15x faster                                 |
| nqueens                 | 98.8 ms                                                             | 87.0 ms: 1.14x faster                                 |
| sympy_sum               | 185 ms                                                              | 163 ms: 1.13x faster                                  |
| sympy_str               | 328 ms                                                              | 289 ms: 1.13x faster                                  |
| sympy_expand            | 540 ms                                                              | 481 ms: 1.12x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                 |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                 |
| regex_v8                | 24.9 ms                                                             | 23.0 ms: 1.08x faster                                 |
| meteor_contest          | 115 ms                                                              | 106 ms: 1.08x faster                                  |
| json                    | 5.41 ms                                                             | 5.00 ms: 1.08x faster                                 |
| xml_etree_iterparse     | 111 ms                                                              | 105 ms: 1.06x faster                                  |
| unpickle                | 15.0 us                                                             | 14.2 us: 1.06x faster                                 |
| pickle                  | 10.2 us                                                             | 9.69 us: 1.06x faster                                 |
| pickle_list             | 4.73 us                                                             | 4.51 us: 1.05x faster                                 |
| xml_etree_parse         | 164 ms                                                              | 156 ms: 1.05x faster                                  |
| json_loads              | 29.3 us                                                             | 28.1 us: 1.04x faster                                 |
| pickle_dict             | 27.8 us                                                             | 28.1 us: 1.01x slower                                 |
| regex_dna               | 213 ms                                                              | 221 ms: 1.04x slower                                  |
| telco                   | 6.67 ms                                                             | 6.92 ms: 1.04x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 6.07 ms: 1.05x slower                                 |
| regex_effbot            | 3.22 ms                                                             | 3.49 ms: 1.08x slower                                 |
| pidigits                | 190 ms                                                              | 208 ms: 1.10x slower                                  |
| unpack_sequence         | 65.6 ns                                                             | 131 ns: 2.00x slower                                  |
| Geometric mean          | (ref)                                                               | 1.22x faster                                          |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
