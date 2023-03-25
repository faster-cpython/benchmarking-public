
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 256 ms: 1.31x faster                                  |
| chameleon      | 9.13 ms                                                             | 6.57 ms: 1.39x faster                                 |
| html5lib       | 86.4 ms                                                             | 60.1 ms: 1.44x faster                                 |
| tornado_http   | 129 ms                                                              | 94.6 ms: 1.36x faster                                 |
| Geometric mean | (ref)                                                               | 1.37x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 93.1 ms: 1.57x faster                                 |
| float          | 110 ms                                                              | 72.5 ms: 1.51x faster                                 |
| Geometric mean | (ref)                                                               | 1.33x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.32x faster                                  |
| regex_v8       | 24.9 ms                                                             | 21.6 ms: 1.15x faster                                 |
| regex_effbot   | 3.22 ms                                                             | 2.93 ms: 1.10x faster                                 |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                               | 1.15x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 305 us: 1.50x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 53.6 ms: 1.40x faster                                 |
| unpickle_pure_python | 300 us                                                              | 229 us: 1.31x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 76.5 ms: 1.24x faster                                 |
| json_loads           | 29.3 us                                                             | 25.4 us: 1.15x faster                                 |
| unpickle             | 15.0 us                                                             | 13.4 us: 1.12x faster                                 |
| pickle_list          | 4.73 us                                                             | 4.26 us: 1.11x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.4 ms: 1.11x faster                                 |
| pickle_dict          | 27.8 us                                                             | 25.6 us: 1.08x faster                                 |
| pickle               | 10.2 us                                                             | 9.56 us: 1.07x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                  |
| xml_etree_parse      | 164 ms                                                              | 157 ms: 1.04x faster                                  |
| unpickle_list        | 4.94 us                                                             | 5.05 us: 1.02x slower                                 |
| Geometric mean       | (ref)                                                               | 1.16x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.25 ms: 1.71x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 6.16 ms: 1.06x slower                                 |
| Geometric mean         | (ref)                                                               | 1.27x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.88 ms: 1.49x faster                                 |
| django_template | 45.8 ms                                                             | 32.8 ms: 1.40x faster                                 |
| Geometric mean  | (ref)                                                               | 1.44x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.61 ms: 2.02x faster                                 |
| scimark_sor             | 198 ms                                                              | 115 ms: 1.72x faster                                  |
| logging_silent          | 169 ns                                                              | 98.2 ns: 1.72x faster                                 |
| python_startup          | 14.1 ms                                                             | 8.25 ms: 1.71x faster                                 |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                  |
| pyflate                 | 671 ms                                                              | 411 ms: 1.63x faster                                  |
| scimark_monte_carlo     | 109 ms                                                              | 66.5 ms: 1.63x faster                                 |
| raytrace                | 470 ms                                                              | 294 ms: 1.60x faster                                  |
| richards                | 74.2 ms                                                             | 46.4 ms: 1.60x faster                                 |
| crypto_pyaes            | 117 ms                                                              | 74.3 ms: 1.57x faster                                 |
| nbody                   | 146 ms                                                              | 93.1 ms: 1.57x faster                                 |
| chaos                   | 106 ms                                                              | 68.6 ms: 1.54x faster                                 |
| spectral_norm           | 150 ms                                                              | 97.6 ms: 1.54x faster                                 |
| float                   | 110 ms                                                              | 72.5 ms: 1.51x faster                                 |
| hexiom                  | 9.50 ms                                                             | 6.29 ms: 1.51x faster                                 |
| pickle_pure_python      | 457 us                                                              | 305 us: 1.50x faster                                  |
| mako                    | 14.7 ms                                                             | 9.88 ms: 1.49x faster                                 |
| unpack_sequence         | 65.6 ns                                                             | 44.3 ns: 1.48x faster                                 |
| scimark_lu              | 160 ms                                                              | 109 ms: 1.47x faster                                  |
| html5lib                | 86.4 ms                                                             | 60.1 ms: 1.44x faster                                 |
| logging_format          | 9.07 us                                                             | 6.44 us: 1.41x faster                                 |
| thrift                  | 1.04 ms                                                             | 741 us: 1.40x faster                                  |
| django_template         | 45.8 ms                                                             | 32.8 ms: 1.40x faster                                 |
| xml_etree_process       | 74.8 ms                                                             | 53.6 ms: 1.40x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.89 us: 1.39x faster                                 |
| chameleon               | 9.13 ms                                                             | 6.57 ms: 1.39x faster                                 |
| tornado_http            | 129 ms                                                              | 94.6 ms: 1.36x faster                                 |
| regex_compile           | 177 ms                                                              | 135 ms: 1.32x faster                                  |
| unpickle_pure_python    | 300 us                                                              | 229 us: 1.31x faster                                  |
| 2to3                    | 336 ms                                                              | 256 ms: 1.31x faster                                  |
| scimark_fft             | 425 ms                                                              | 325 ms: 1.31x faster                                  |
| pycparser               | 1.53 sec                                                            | 1.18 sec: 1.29x faster                                |
| fannkuch                | 485 ms                                                              | 385 ms: 1.26x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 76.5 ms: 1.24x faster                                 |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.57 ms: 1.23x faster                                 |
| dulwich_log             | 76.3 ms                                                             | 62.8 ms: 1.22x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                 |
| sqlite_synth            | 2.97 us                                                             | 2.53 us: 1.18x faster                                 |
| nqueens                 | 98.8 ms                                                             | 84.7 ms: 1.17x faster                                 |
| sympy_str               | 328 ms                                                              | 284 ms: 1.16x faster                                  |
| json_loads              | 29.3 us                                                             | 25.4 us: 1.15x faster                                 |
| regex_v8                | 24.9 ms                                                             | 21.6 ms: 1.15x faster                                 |
| sympy_expand            | 540 ms                                                              | 468 ms: 1.15x faster                                  |
| sympy_sum               | 185 ms                                                              | 161 ms: 1.15x faster                                  |
| unpickle                | 15.0 us                                                             | 13.4 us: 1.12x faster                                 |
| pickle_list             | 4.73 us                                                             | 4.26 us: 1.11x faster                                 |
| json_dumps              | 13.7 ms                                                             | 12.4 ms: 1.11x faster                                 |
| pathlib                 | 19.8 ms                                                             | 17.9 ms: 1.11x faster                                 |
| json                    | 5.41 ms                                                             | 4.91 ms: 1.10x faster                                 |
| regex_effbot            | 3.22 ms                                                             | 2.93 ms: 1.10x faster                                 |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.10x faster                                  |
| pickle_dict             | 27.8 us                                                             | 25.6 us: 1.08x faster                                 |
| pickle                  | 10.2 us                                                             | 9.56 us: 1.07x faster                                 |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                  |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                  |
| xml_etree_parse         | 164 ms                                                              | 157 ms: 1.04x faster                                  |
| unpickle_list           | 4.94 us                                                             | 5.05 us: 1.02x slower                                 |
| telco                   | 6.67 ms                                                             | 6.84 ms: 1.02x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 6.16 ms: 1.06x slower                                 |
| Geometric mean          | (ref)                                                               | 1.30x faster                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
