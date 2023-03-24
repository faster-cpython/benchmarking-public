
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9471106
- commit date: 2022-01-13
- overall geometric mean: 1.24x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 264 ms: 1.27x faster                                  |
| chameleon      | 9.13 ms                                                             | 7.55 ms: 1.21x faster                                 |
| html5lib       | 86.4 ms                                                             | 68.1 ms: 1.27x faster                                 |
| tornado_http   | 129 ms                                                              | 107 ms: 1.21x faster                                  |
| Geometric mean | (ref)                                                               | 1.24x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 95.1 ms: 1.53x faster                                 |
| float          | 110 ms                                                              | 78.0 ms: 1.41x faster                                 |
| pidigits       | 190 ms                                                              | 194 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                               | 1.28x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 138 ms: 1.28x faster                                  |
| regex_dna      | 213 ms                                                              | 212 ms: 1.00x faster                                  |
| regex_effbot   | 3.22 ms                                                             | 3.25 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                               | 1.06x faster                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 329 us: 1.39x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 56.9 ms: 1.32x faster                                 |
| xml_etree_generate   | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                 |
| unpickle_pure_python | 300 us                                                              | 254 us: 1.18x faster                                  |
| json_loads           | 29.3 us                                                             | 25.1 us: 1.17x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.4 ms: 1.11x faster                                 |
| pickle_list          | 4.73 us                                                             | 4.37 us: 1.08x faster                                 |
| xml_etree_parse      | 164 ms                                                              | 155 ms: 1.06x faster                                  |
| unpickle             | 15.0 us                                                             | 14.3 us: 1.05x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 107 ms: 1.04x faster                                  |
| pickle_dict          | 27.8 us                                                             | 26.8 us: 1.04x faster                                 |
| pickle               | 10.2 us                                                             | 9.95 us: 1.03x faster                                 |
| unpickle_list        | 4.94 us                                                             | 5.20 us: 1.05x slower                                 |
| Geometric mean       | (ref)                                                               | 1.12x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.07 ms: 1.75x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 5.85 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                               | 1.32x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 45.8 ms                                                             | 35.2 ms: 1.30x faster                                 |
| mako            | 14.7 ms                                                             | 11.5 ms: 1.28x faster                                 |
| Geometric mean  | (ref)                                                               | 1.29x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 4.16 ms: 1.75x faster                                 |
| python_startup          | 14.1 ms                                                             | 8.07 ms: 1.75x faster                                 |
| scimark_sor             | 198 ms                                                              | 124 ms: 1.59x faster                                  |
| nbody                   | 146 ms                                                              | 95.1 ms: 1.53x faster                                 |
| go                      | 226 ms                                                              | 148 ms: 1.52x faster                                  |
| spectral_norm           | 150 ms                                                              | 99.0 ms: 1.52x faster                                 |
| pyflate                 | 671 ms                                                              | 444 ms: 1.51x faster                                  |
| scimark_monte_carlo     | 109 ms                                                              | 72.7 ms: 1.49x faster                                 |
| logging_silent          | 169 ns                                                              | 113 ns: 1.49x faster                                  |
| raytrace                | 470 ms                                                              | 320 ms: 1.47x faster                                  |
| unpack_sequence         | 65.6 ns                                                             | 44.8 ns: 1.47x faster                                 |
| chaos                   | 106 ms                                                              | 72.7 ms: 1.46x faster                                 |
| richards                | 74.2 ms                                                             | 51.5 ms: 1.44x faster                                 |
| hexiom                  | 9.50 ms                                                             | 6.63 ms: 1.43x faster                                 |
| float                   | 110 ms                                                              | 78.0 ms: 1.41x faster                                 |
| scimark_lu              | 160 ms                                                              | 114 ms: 1.41x faster                                  |
| logging_format          | 9.07 us                                                             | 6.51 us: 1.39x faster                                 |
| crypto_pyaes            | 117 ms                                                              | 83.8 ms: 1.39x faster                                 |
| pickle_pure_python      | 457 us                                                              | 329 us: 1.39x faster                                  |
| logging_simple          | 8.21 us                                                             | 5.95 us: 1.38x faster                                 |
| xml_etree_process       | 74.8 ms                                                             | 56.9 ms: 1.32x faster                                 |
| pycparser               | 1.53 sec                                                            | 1.17 sec: 1.31x faster                                |
| django_template         | 45.8 ms                                                             | 35.2 ms: 1.30x faster                                 |
| scimark_fft             | 425 ms                                                              | 330 ms: 1.29x faster                                  |
| regex_compile           | 177 ms                                                              | 138 ms: 1.28x faster                                  |
| mako                    | 14.7 ms                                                             | 11.5 ms: 1.28x faster                                 |
| thrift                  | 1.04 ms                                                             | 812 us: 1.28x faster                                  |
| 2to3                    | 336 ms                                                              | 264 ms: 1.27x faster                                  |
| html5lib                | 86.4 ms                                                             | 68.1 ms: 1.27x faster                                 |
| fannkuch                | 485 ms                                                              | 392 ms: 1.24x faster                                  |
| chameleon               | 9.13 ms                                                             | 7.55 ms: 1.21x faster                                 |
| tornado_http            | 129 ms                                                              | 107 ms: 1.21x faster                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.69 ms: 1.20x faster                                 |
| xml_etree_generate      | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                 |
| unpickle_pure_python    | 300 us                                                              | 254 us: 1.18x faster                                  |
| nqueens                 | 98.8 ms                                                             | 84.0 ms: 1.18x faster                                 |
| json_loads              | 29.3 us                                                             | 25.1 us: 1.17x faster                                 |
| dulwich_log             | 76.3 ms                                                             | 65.8 ms: 1.16x faster                                 |
| json                    | 5.41 ms                                                             | 4.74 ms: 1.14x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 21.4 ms: 1.14x faster                                 |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.12x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.4 ms: 1.11x faster                                 |
| sympy_sum               | 185 ms                                                              | 170 ms: 1.09x faster                                  |
| sqlite_synth            | 2.97 us                                                             | 2.73 us: 1.09x faster                                 |
| sympy_str               | 328 ms                                                              | 302 ms: 1.09x faster                                  |
| pickle_list             | 4.73 us                                                             | 4.37 us: 1.08x faster                                 |
| sympy_expand            | 540 ms                                                              | 506 ms: 1.07x faster                                  |
| xml_etree_parse         | 164 ms                                                              | 155 ms: 1.06x faster                                  |
| unpickle                | 15.0 us                                                             | 14.3 us: 1.05x faster                                 |
| xml_etree_iterparse     | 111 ms                                                              | 107 ms: 1.04x faster                                  |
| pickle_dict             | 27.8 us                                                             | 26.8 us: 1.04x faster                                 |
| pathlib                 | 19.8 ms                                                             | 19.1 ms: 1.04x faster                                 |
| pickle                  | 10.2 us                                                             | 9.95 us: 1.03x faster                                 |
| regex_dna               | 213 ms                                                              | 212 ms: 1.00x faster                                  |
| regex_effbot            | 3.22 ms                                                             | 3.25 ms: 1.01x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 5.85 ms: 1.01x slower                                 |
| pidigits                | 190 ms                                                              | 194 ms: 1.02x slower                                  |
| unpickle_list           | 4.94 us                                                             | 5.20 us: 1.05x slower                                 |
| Geometric mean          | (ref)                                                               | 1.24x faster                                          |

Benchmark hidden because not significant (2): regex_v8, telco
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
