
# Results vs. 3.10.4

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 257 ms: 1.31x faster                                   |
| chameleon      | 9.13 ms                                                             | 6.49 ms: 1.41x faster                                  |
| docutils       | 3.19 sec                                                            | 2.55 sec: 1.25x faster                                 |
| html5lib       | 86.4 ms                                                             | 64.0 ms: 1.35x faster                                  |
| tornado_http   | 129 ms                                                              | 96.1 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                               | 1.33x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 146 ms                                                              | 93.0 ms: 1.57x faster                                  |
| float          | 110 ms                                                              | 76.6 ms: 1.43x faster                                  |
| Geometric mean | (ref)                                                               | 1.31x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 138 ms: 1.28x faster                                   |
| regex_v8       | 24.9 ms                                                             | 21.3 ms: 1.17x faster                                  |
| regex_dna      | 213 ms                                                              | 192 ms: 1.11x faster                                   |
| regex_effbot   | 3.22 ms                                                             | 3.39 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                               | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 305 us: 1.50x faster                                   |
| xml_etree_process    | 74.8 ms                                                             | 53.8 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                              | 228 us: 1.31x faster                                   |
| xml_etree_generate   | 94.9 ms                                                             | 76.5 ms: 1.24x faster                                  |
| pickle_list          | 4.73 us                                                             | 4.16 us: 1.14x faster                                  |
| unpickle             | 15.0 us                                                             | 13.2 us: 1.13x faster                                  |
| json_loads           | 29.3 us                                                             | 26.2 us: 1.12x faster                                  |
| json_dumps           | 13.7 ms                                                             | 12.5 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 164 ms                                                              | 159 ms: 1.03x faster                                   |
| pickle               | 10.2 us                                                             | 10.00 us: 1.02x faster                                 |
| pickle_dict          | 27.8 us                                                             | 31.4 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                               | 1.14x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.47 ms: 1.67x faster                                  |
| python_startup_no_site | 5.80 ms                                                             | 5.97 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                               | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.83 ms: 1.50x faster                                  |
| genshi_text     | 30.4 ms                                                             | 21.7 ms: 1.40x faster                                  |
| django_template | 45.8 ms                                                             | 32.7 ms: 1.40x faster                                  |
| genshi_xml      | 64.3 ms                                                             | 51.5 ms: 1.25x faster                                  |
| Geometric mean  | (ref)                                                               | 1.38x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.68 ms: 1.99x faster                                  |
| scimark_sor             | 198 ms                                                              | 115 ms: 1.72x faster                                   |
| logging_silent          | 169 ns                                                              | 99.8 ns: 1.69x faster                                  |
| python_startup          | 14.1 ms                                                             | 8.47 ms: 1.67x faster                                  |
| richards                | 74.2 ms                                                             | 45.6 ms: 1.63x faster                                  |
| raytrace                | 470 ms                                                              | 291 ms: 1.62x faster                                   |
| pyflate                 | 671 ms                                                              | 417 ms: 1.61x faster                                   |
| scimark_monte_carlo     | 109 ms                                                              | 67.7 ms: 1.60x faster                                  |
| go                      | 226 ms                                                              | 141 ms: 1.60x faster                                   |
| crypto_pyaes            | 117 ms                                                              | 73.8 ms: 1.58x faster                                  |
| nbody                   | 146 ms                                                              | 93.0 ms: 1.57x faster                                  |
| chaos                   | 106 ms                                                              | 68.2 ms: 1.55x faster                                  |
| spectral_norm           | 150 ms                                                              | 98.4 ms: 1.53x faster                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.38 ms: 1.50x faster                                  |
| mako                    | 14.7 ms                                                             | 9.83 ms: 1.50x faster                                  |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.50x faster                                   |
| pickle_pure_python      | 457 us                                                              | 305 us: 1.50x faster                                   |
| hexiom                  | 9.50 ms                                                             | 6.36 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.67 ms: 1.47x faster                                  |
| float                   | 110 ms                                                              | 76.6 ms: 1.43x faster                                  |
| deepcopy_memo           | 51.8 us                                                             | 36.8 us: 1.41x faster                                  |
| chameleon               | 9.13 ms                                                             | 6.49 ms: 1.41x faster                                  |
| genshi_text             | 30.4 ms                                                             | 21.7 ms: 1.40x faster                                  |
| django_template         | 45.8 ms                                                             | 32.7 ms: 1.40x faster                                  |
| logging_format          | 9.07 us                                                             | 6.49 us: 1.40x faster                                  |
| xml_etree_process       | 74.8 ms                                                             | 53.8 ms: 1.39x faster                                  |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.38x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.97 us: 1.38x faster                                  |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                 |
| pprint_safe_repr        | 953 ms                                                              | 697 ms: 1.37x faster                                   |
| pprint_pformat          | 1.98 sec                                                            | 1.45 sec: 1.37x faster                                 |
| async_tree_none         | 713 ms                                                              | 524 ms: 1.36x faster                                   |
| async_tree_memoization  | 853 ms                                                              | 628 ms: 1.36x faster                                   |
| html5lib                | 86.4 ms                                                             | 64.0 ms: 1.35x faster                                  |
| thrift                  | 1.04 ms                                                             | 770 us: 1.35x faster                                   |
| unpack_sequence         | 65.6 ns                                                             | 48.8 ns: 1.34x faster                                  |
| tornado_http            | 129 ms                                                              | 96.1 ms: 1.34x faster                                  |
| unpickle_pure_python    | 300 us                                                              | 228 us: 1.31x faster                                   |
| 2to3                    | 336 ms                                                              | 257 ms: 1.31x faster                                   |
| scimark_fft             | 425 ms                                                              | 327 ms: 1.30x faster                                   |
| aiohttp                 | 1.35 ms                                                             | 1.05 ms: 1.29x faster                                  |
| regex_compile           | 177 ms                                                              | 138 ms: 1.28x faster                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 740 ms: 1.28x faster                                   |
| gunicorn                | 1.43 ms                                                             | 1.13 ms: 1.27x faster                                  |
| deepcopy                | 438 us                                                              | 348 us: 1.26x faster                                   |
| docutils                | 3.19 sec                                                            | 2.55 sec: 1.25x faster                                 |
| deepcopy_reduce         | 3.80 us                                                             | 3.04 us: 1.25x faster                                  |
| genshi_xml              | 64.3 ms                                                             | 51.5 ms: 1.25x faster                                  |
| coroutines              | 31.8 ms                                                             | 25.6 ms: 1.24x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 76.5 ms: 1.24x faster                                  |
| sqlglot_normalize       | 135 ms                                                              | 109 ms: 1.24x faster                                   |
| fannkuch                | 485 ms                                                              | 392 ms: 1.24x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 53.3 ms: 1.23x faster                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.63 ms: 1.21x faster                                  |
| flaskblogging           | 8.48 ms                                                             | 7.02 ms: 1.21x faster                                  |
| sqlite_synth            | 2.97 us                                                             | 2.46 us: 1.21x faster                                  |
| dask                    | 437 ms                                                              | 365 ms: 1.20x faster                                   |
| dulwich_log             | 76.3 ms                                                             | 63.7 ms: 1.20x faster                                  |
| nqueens                 | 98.8 ms                                                             | 83.1 ms: 1.19x faster                                  |
| async_generators        | 420 ms                                                              | 357 ms: 1.18x faster                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 141 ms: 1.18x faster                                   |
| bench_thread_pool       | 954 us                                                              | 812 us: 1.17x faster                                   |
| regex_v8                | 24.9 ms                                                             | 21.3 ms: 1.17x faster                                  |
| sympy_integrate         | 24.3 ms                                                             | 20.8 ms: 1.17x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.2 ms: 1.16x faster                                  |
| sympy_expand            | 540 ms                                                              | 468 ms: 1.15x faster                                   |
| sympy_str               | 328 ms                                                              | 288 ms: 1.14x faster                                   |
| pickle_list             | 4.73 us                                                             | 4.16 us: 1.14x faster                                  |
| unpickle                | 15.0 us                                                             | 13.2 us: 1.13x faster                                  |
| djangocms               | 36.3 us                                                             | 32.3 us: 1.12x faster                                  |
| json_loads              | 29.3 us                                                             | 26.2 us: 1.12x faster                                  |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.12x faster                                   |
| pathlib                 | 19.8 ms                                                             | 17.8 ms: 1.11x faster                                  |
| regex_dna               | 213 ms                                                              | 192 ms: 1.11x faster                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.5 ms: 1.10x faster                                  |
| json                    | 5.41 ms                                                             | 4.92 ms: 1.10x faster                                  |
| pylint                  | 521 ms                                                              | 475 ms: 1.10x faster                                   |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                   |
| asyncio_tcp             | 922 ms                                                              | 884 ms: 1.04x faster                                   |
| xml_etree_parse         | 164 ms                                                              | 159 ms: 1.03x faster                                   |
| pickle                  | 10.2 us                                                             | 10.00 us: 1.02x faster                                 |
| generators              | 75.7 ms                                                             | 74.1 ms: 1.02x faster                                  |
| telco                   | 6.67 ms                                                             | 6.59 ms: 1.01x faster                                  |
| mdp                     | 2.75 sec                                                            | 2.77 sec: 1.01x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 5.97 ms: 1.03x slower                                  |
| regex_effbot            | 3.22 ms                                                             | 3.39 ms: 1.05x slower                                  |
| pickle_dict             | 27.8 us                                                             | 31.4 us: 1.13x slower                                  |
| gc_traversal            | 3.53 ms                                                             | 4.15 ms: 1.18x slower                                  |
| coverage                | 70.6 ms                                                             | 103 ms: 1.46x slower                                   |
| Geometric mean          | (ref)                                                               | 1.25x faster                                           |

Benchmark hidden because not significant (4): mypy2, unpickle_list, pidigits, bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: comprehensions
