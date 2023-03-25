
# Results vs. 3.10.4

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 258 ms: 1.30x faster                                   |
| chameleon      | 9.13 ms                                                             | 6.63 ms: 1.38x faster                                  |
| docutils       | 3.19 sec                                                            | 2.57 sec: 1.24x faster                                 |
| html5lib       | 86.4 ms                                                             | 63.4 ms: 1.36x faster                                  |
| tornado_http   | 129 ms                                                              | 99.8 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                               | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 146 ms                                                              | 95.4 ms: 1.53x faster                                  |
| float          | 110 ms                                                              | 76.0 ms: 1.45x faster                                  |
| Geometric mean | (ref)                                                               | 1.30x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 137 ms: 1.29x faster                                   |
| regex_v8       | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                  |
| regex_dna      | 213 ms                                                              | 200 ms: 1.06x faster                                   |
| regex_effbot   | 3.22 ms                                                             | 3.31 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 310 us: 1.48x faster                                   |
| xml_etree_process    | 74.8 ms                                                             | 53.7 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                              | 229 us: 1.31x faster                                   |
| xml_etree_generate   | 94.9 ms                                                             | 76.6 ms: 1.24x faster                                  |
| json_loads           | 29.3 us                                                             | 24.0 us: 1.22x faster                                  |
| pickle_list          | 4.73 us                                                             | 4.17 us: 1.13x faster                                  |
| unpickle             | 15.0 us                                                             | 13.4 us: 1.12x faster                                  |
| json_dumps           | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                   |
| pickle               | 10.2 us                                                             | 9.72 us: 1.05x faster                                  |
| xml_etree_parse      | 164 ms                                                              | 158 ms: 1.04x faster                                   |
| pickle_dict          | 27.8 us                                                             | 31.1 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                               | 1.15x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.49 ms: 1.66x faster                                  |
| python_startup_no_site | 5.80 ms                                                             | 5.98 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                               | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.92 ms: 1.49x faster                                  |
| django_template | 45.8 ms                                                             | 33.2 ms: 1.38x faster                                  |
| genshi_text     | 30.4 ms                                                             | 22.1 ms: 1.37x faster                                  |
| genshi_xml      | 64.3 ms                                                             | 52.5 ms: 1.23x faster                                  |
| Geometric mean  | (ref)                                                               | 1.36x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.67 ms: 1.99x faster                                  |
| scimark_sor             | 198 ms                                                              | 116 ms: 1.71x faster                                   |
| python_startup          | 14.1 ms                                                             | 8.49 ms: 1.66x faster                                  |
| logging_silent          | 169 ns                                                              | 102 ns: 1.66x faster                                   |
| go                      | 226 ms                                                              | 140 ms: 1.62x faster                                   |
| pyflate                 | 671 ms                                                              | 415 ms: 1.61x faster                                   |
| crypto_pyaes            | 117 ms                                                              | 72.6 ms: 1.61x faster                                  |
| raytrace                | 470 ms                                                              | 294 ms: 1.60x faster                                   |
| scimark_monte_carlo     | 109 ms                                                              | 68.4 ms: 1.59x faster                                  |
| richards                | 74.2 ms                                                             | 46.9 ms: 1.58x faster                                  |
| nbody                   | 146 ms                                                              | 95.4 ms: 1.53x faster                                  |
| chaos                   | 106 ms                                                              | 69.6 ms: 1.52x faster                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.38 ms: 1.50x faster                                  |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.49x faster                                   |
| mako                    | 14.7 ms                                                             | 9.92 ms: 1.49x faster                                  |
| spectral_norm           | 150 ms                                                              | 101 ms: 1.48x faster                                   |
| pickle_pure_python      | 457 us                                                              | 310 us: 1.48x faster                                   |
| hexiom                  | 9.50 ms                                                             | 6.46 ms: 1.47x faster                                  |
| unpack_sequence         | 65.6 ns                                                             | 44.6 ns: 1.47x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.68 ms: 1.46x faster                                  |
| float                   | 110 ms                                                              | 76.0 ms: 1.45x faster                                  |
| deepcopy_memo           | 51.8 us                                                             | 37.2 us: 1.39x faster                                  |
| xml_etree_process       | 74.8 ms                                                             | 53.7 ms: 1.39x faster                                  |
| logging_format          | 9.07 us                                                             | 6.54 us: 1.39x faster                                  |
| django_template         | 45.8 ms                                                             | 33.2 ms: 1.38x faster                                  |
| logging_simple          | 8.21 us                                                             | 5.95 us: 1.38x faster                                  |
| chameleon               | 9.13 ms                                                             | 6.63 ms: 1.38x faster                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.44 sec: 1.38x faster                                 |
| genshi_text             | 30.4 ms                                                             | 22.1 ms: 1.37x faster                                  |
| html5lib                | 86.4 ms                                                             | 63.4 ms: 1.36x faster                                  |
| async_tree_io           | 1.78 sec                                                            | 1.31 sec: 1.36x faster                                 |
| pprint_safe_repr        | 953 ms                                                              | 700 ms: 1.36x faster                                   |
| async_tree_none         | 713 ms                                                              | 523 ms: 1.36x faster                                   |
| async_tree_memoization  | 853 ms                                                              | 627 ms: 1.36x faster                                   |
| thrift                  | 1.04 ms                                                             | 765 us: 1.35x faster                                   |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                 |
| unpickle_pure_python    | 300 us                                                              | 229 us: 1.31x faster                                   |
| 2to3                    | 336 ms                                                              | 258 ms: 1.30x faster                                   |
| scimark_fft             | 425 ms                                                              | 327 ms: 1.30x faster                                   |
| regex_compile           | 177 ms                                                              | 137 ms: 1.29x faster                                   |
| tornado_http            | 129 ms                                                              | 99.8 ms: 1.29x faster                                  |
| aiohttp                 | 1.35 ms                                                             | 1.05 ms: 1.29x faster                                  |
| gunicorn                | 1.43 ms                                                             | 1.13 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 742 ms: 1.27x faster                                   |
| fannkuch                | 485 ms                                                              | 384 ms: 1.26x faster                                   |
| coroutines              | 31.8 ms                                                             | 25.3 ms: 1.26x faster                                  |
| deepcopy                | 438 us                                                              | 349 us: 1.26x faster                                   |
| docutils                | 3.19 sec                                                            | 2.57 sec: 1.24x faster                                 |
| sqlglot_normalize       | 135 ms                                                              | 108 ms: 1.24x faster                                   |
| xml_etree_generate      | 94.9 ms                                                             | 76.6 ms: 1.24x faster                                  |
| deepcopy_reduce         | 3.80 us                                                             | 3.09 us: 1.23x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 53.3 ms: 1.23x faster                                  |
| genshi_xml              | 64.3 ms                                                             | 52.5 ms: 1.23x faster                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.59 ms: 1.22x faster                                  |
| json_loads              | 29.3 us                                                             | 24.0 us: 1.22x faster                                  |
| sqlite_synth            | 2.97 us                                                             | 2.47 us: 1.20x faster                                  |
| dulwich_log             | 76.3 ms                                                             | 63.5 ms: 1.20x faster                                  |
| flaskblogging           | 8.48 ms                                                             | 7.07 ms: 1.20x faster                                  |
| dask                    | 437 ms                                                              | 365 ms: 1.20x faster                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 141 ms: 1.18x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.0 ms: 1.18x faster                                  |
| async_generators        | 420 ms                                                              | 358 ms: 1.17x faster                                   |
| bench_thread_pool       | 954 us                                                              | 813 us: 1.17x faster                                   |
| json                    | 5.41 ms                                                             | 4.63 ms: 1.17x faster                                  |
| nqueens                 | 98.8 ms                                                             | 85.0 ms: 1.16x faster                                  |
| sympy_integrate         | 24.3 ms                                                             | 21.0 ms: 1.16x faster                                  |
| sympy_expand            | 540 ms                                                              | 472 ms: 1.14x faster                                   |
| pickle_list             | 4.73 us                                                             | 4.17 us: 1.13x faster                                  |
| sympy_str               | 328 ms                                                              | 289 ms: 1.13x faster                                   |
| pylint                  | 521 ms                                                              | 461 ms: 1.13x faster                                   |
| unpickle                | 15.0 us                                                             | 13.4 us: 1.12x faster                                  |
| regex_v8                | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                  |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                  |
| djangocms               | 36.3 us                                                             | 33.1 us: 1.10x faster                                  |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.09x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                  |
| meteor_contest          | 115 ms                                                              | 106 ms: 1.08x faster                                   |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                   |
| regex_dna               | 213 ms                                                              | 200 ms: 1.06x faster                                   |
| pickle                  | 10.2 us                                                             | 9.72 us: 1.05x faster                                  |
| mdp                     | 2.75 sec                                                            | 2.64 sec: 1.04x faster                                 |
| xml_etree_parse         | 164 ms                                                              | 158 ms: 1.04x faster                                   |
| asyncio_tcp             | 922 ms                                                              | 889 ms: 1.04x faster                                   |
| generators              | 75.7 ms                                                             | 73.3 ms: 1.03x faster                                  |
| regex_effbot            | 3.22 ms                                                             | 3.31 ms: 1.03x slower                                  |
| python_startup_no_site  | 5.80 ms                                                             | 5.98 ms: 1.03x slower                                  |
| pickle_dict             | 27.8 us                                                             | 31.1 us: 1.12x slower                                  |
| gc_traversal            | 3.53 ms                                                             | 4.26 ms: 1.21x slower                                  |
| coverage                | 70.6 ms                                                             | 104 ms: 1.47x slower                                   |
| Geometric mean          | (ref)                                                               | 1.25x faster                                           |

Benchmark hidden because not significant (5): mypy2, telco, bench_mp_pool, pidigits, unpickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: comprehensions
