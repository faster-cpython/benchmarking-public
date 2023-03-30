
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 256 ms: 1.31x faster                                  |
| chameleon      | 9.13 ms                                                             | 6.59 ms: 1.39x faster                                 |
| html5lib       | 86.4 ms                                                             | 63.8 ms: 1.35x faster                                 |
| tornado_http   | 129 ms                                                              | 93.8 ms: 1.37x faster                                 |
| Geometric mean | (ref)                                                               | 1.36x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 90.9 ms: 1.60x faster                                 |
| float          | 110 ms                                                              | 72.8 ms: 1.51x faster                                 |
| pidigits       | 190 ms                                                              | 190 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                               | 1.34x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 136 ms: 1.30x faster                                  |
| regex_v8       | 24.9 ms                                                             | 21.5 ms: 1.16x faster                                 |
| regex_dna      | 213 ms                                                              | 196 ms: 1.08x faster                                  |
| regex_effbot   | 3.22 ms                                                             | 3.02 ms: 1.07x faster                                 |
| Geometric mean | (ref)                                                               | 1.15x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 302 us: 1.51x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 53.3 ms: 1.40x faster                                 |
| unpickle_pure_python | 300 us                                                              | 227 us: 1.32x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 75.8 ms: 1.25x faster                                 |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.21x faster                                 |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.12x faster                                 |
| pickle_list          | 4.73 us                                                             | 4.30 us: 1.10x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                  |
| pickle_dict          | 27.8 us                                                             | 25.9 us: 1.07x faster                                 |
| pickle               | 10.2 us                                                             | 9.61 us: 1.06x faster                                 |
| xml_etree_parse      | 164 ms                                                              | 157 ms: 1.04x faster                                  |
| unpickle_list        | 4.94 us                                                             | 4.98 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                               | 1.16x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.33 ms: 1.70x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 6.17 ms: 1.06x slower                                 |
| Geometric mean         | (ref)                                                               | 1.26x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.71 ms: 1.52x faster                                 |
| django_template | 45.8 ms                                                             | 32.4 ms: 1.42x faster                                 |
| Geometric mean  | (ref)                                                               | 1.47x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.60 ms: 2.03x faster                                 |
| logging_silent          | 169 ns                                                              | 98.1 ns: 1.72x faster                                 |
| scimark_sor             | 198 ms                                                              | 115 ms: 1.72x faster                                  |
| python_startup          | 14.1 ms                                                             | 8.33 ms: 1.70x faster                                 |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                  |
| pyflate                 | 671 ms                                                              | 410 ms: 1.64x faster                                  |
| richards                | 74.2 ms                                                             | 45.3 ms: 1.64x faster                                 |
| scimark_monte_carlo     | 109 ms                                                              | 66.5 ms: 1.63x faster                                 |
| raytrace                | 470 ms                                                              | 291 ms: 1.61x faster                                  |
| nbody                   | 146 ms                                                              | 90.9 ms: 1.60x faster                                 |
| crypto_pyaes            | 117 ms                                                              | 73.8 ms: 1.58x faster                                 |
| chaos                   | 106 ms                                                              | 67.8 ms: 1.56x faster                                 |
| spectral_norm           | 150 ms                                                              | 96.3 ms: 1.56x faster                                 |
| unpack_sequence         | 65.6 ns                                                             | 43.2 ns: 1.52x faster                                 |
| mako                    | 14.7 ms                                                             | 9.71 ms: 1.52x faster                                 |
| pickle_pure_python      | 457 us                                                              | 302 us: 1.51x faster                                  |
| float                   | 110 ms                                                              | 72.8 ms: 1.51x faster                                 |
| hexiom                  | 9.50 ms                                                             | 6.32 ms: 1.50x faster                                 |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.49x faster                                  |
| django_template         | 45.8 ms                                                             | 32.4 ms: 1.42x faster                                 |
| logging_format          | 9.07 us                                                             | 6.42 us: 1.41x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.82 us: 1.41x faster                                 |
| xml_etree_process       | 74.8 ms                                                             | 53.3 ms: 1.40x faster                                 |
| pycparser               | 1.53 sec                                                            | 1.10 sec: 1.39x faster                                |
| chameleon               | 9.13 ms                                                             | 6.59 ms: 1.39x faster                                 |
| tornado_http            | 129 ms                                                              | 93.8 ms: 1.37x faster                                 |
| thrift                  | 1.04 ms                                                             | 756 us: 1.37x faster                                  |
| html5lib                | 86.4 ms                                                             | 63.8 ms: 1.35x faster                                 |
| unpickle_pure_python    | 300 us                                                              | 227 us: 1.32x faster                                  |
| scimark_fft             | 425 ms                                                              | 324 ms: 1.31x faster                                  |
| 2to3                    | 336 ms                                                              | 256 ms: 1.31x faster                                  |
| regex_compile           | 177 ms                                                              | 136 ms: 1.30x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 75.8 ms: 1.25x faster                                 |
| fannkuch                | 485 ms                                                              | 394 ms: 1.23x faster                                  |
| dulwich_log             | 76.3 ms                                                             | 62.6 ms: 1.22x faster                                 |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.21x faster                                 |
| nqueens                 | 98.8 ms                                                             | 82.4 ms: 1.20x faster                                 |
| sqlite_synth            | 2.97 us                                                             | 2.50 us: 1.19x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                 |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.79 ms: 1.17x faster                                 |
| sympy_expand            | 540 ms                                                              | 465 ms: 1.16x faster                                  |
| sympy_sum               | 185 ms                                                              | 159 ms: 1.16x faster                                  |
| regex_v8                | 24.9 ms                                                             | 21.5 ms: 1.16x faster                                 |
| sympy_str               | 328 ms                                                              | 284 ms: 1.15x faster                                  |
| json                    | 5.41 ms                                                             | 4.72 ms: 1.15x faster                                 |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.12x faster                                 |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                  |
| pickle_list             | 4.73 us                                                             | 4.30 us: 1.10x faster                                 |
| json_dumps              | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                 |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.08x faster                                 |
| regex_dna               | 213 ms                                                              | 196 ms: 1.08x faster                                  |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                  |
| pickle_dict             | 27.8 us                                                             | 25.9 us: 1.07x faster                                 |
| regex_effbot            | 3.22 ms                                                             | 3.02 ms: 1.07x faster                                 |
| pickle                  | 10.2 us                                                             | 9.61 us: 1.06x faster                                 |
| xml_etree_parse         | 164 ms                                                              | 157 ms: 1.04x faster                                  |
| pidigits                | 190 ms                                                              | 190 ms: 1.00x faster                                  |
| unpickle_list           | 4.94 us                                                             | 4.98 us: 1.01x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 6.17 ms: 1.06x slower                                 |
| Geometric mean          | (ref)                                                               | 1.31x faster                                          |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
