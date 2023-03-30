
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 256 ms: 1.31x faster                                       |
| chameleon      | 9.13 ms                                                             | 6.42 ms: 1.42x faster                                      |
| docutils       | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                     |
| html5lib       | 86.4 ms                                                             | 62.8 ms: 1.37x faster                                      |
| tornado_http   | 129 ms                                                              | 94.7 ms: 1.36x faster                                      |
| Geometric mean | (ref)                                                               | 1.34x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 146 ms                                                              | 94.9 ms: 1.54x faster                                      |
| float          | 110 ms                                                              | 73.9 ms: 1.49x faster                                      |
| pidigits       | 190 ms                                                              | 194 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                               | 1.31x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 136 ms: 1.30x faster                                       |
| regex_v8       | 24.9 ms                                                             | 21.4 ms: 1.16x faster                                      |
| regex_effbot   | 3.22 ms                                                             | 2.92 ms: 1.10x faster                                      |
| regex_dna      | 213 ms                                                              | 194 ms: 1.10x faster                                       |
| Geometric mean | (ref)                                                               | 1.16x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 301 us: 1.52x faster                                       |
| xml_etree_process    | 74.8 ms                                                             | 53.6 ms: 1.40x faster                                      |
| unpickle_pure_python | 300 us                                                              | 227 us: 1.32x faster                                       |
| xml_etree_generate   | 94.9 ms                                                             | 76.7 ms: 1.24x faster                                      |
| json_loads           | 29.3 us                                                             | 24.9 us: 1.18x faster                                      |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.12x faster                                      |
| pickle_list          | 4.73 us                                                             | 4.27 us: 1.11x faster                                      |
| pickle               | 10.2 us                                                             | 9.37 us: 1.09x faster                                      |
| json_dumps           | 13.7 ms                                                             | 12.7 ms: 1.08x faster                                      |
| pickle_dict          | 27.8 us                                                             | 26.0 us: 1.07x faster                                      |
| xml_etree_parse      | 164 ms                                                              | 158 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 111 ms                                                              | 108 ms: 1.03x faster                                       |
| Geometric mean       | (ref)                                                               | 1.16x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.51 ms: 1.66x faster                                      |
| python_startup_no_site | 5.80 ms                                                             | 6.01 ms: 1.04x slower                                      |
| Geometric mean         | (ref)                                                               | 1.27x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                      |
| django_template | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                      |
| genshi_text     | 30.4 ms                                                             | 22.0 ms: 1.38x faster                                      |
| genshi_xml      | 64.3 ms                                                             | 52.3 ms: 1.23x faster                                      |
| Geometric mean  | (ref)                                                               | 1.36x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.65 ms: 2.00x faster                                      |
| scimark_sor             | 198 ms                                                              | 114 ms: 1.73x faster                                       |
| logging_silent          | 169 ns                                                              | 101 ns: 1.67x faster                                       |
| python_startup          | 14.1 ms                                                             | 8.51 ms: 1.66x faster                                      |
| pyflate                 | 671 ms                                                              | 409 ms: 1.64x faster                                       |
| richards                | 74.2 ms                                                             | 45.3 ms: 1.64x faster                                      |
| scimark_monte_carlo     | 109 ms                                                              | 66.6 ms: 1.63x faster                                      |
| go                      | 226 ms                                                              | 139 ms: 1.62x faster                                       |
| raytrace                | 470 ms                                                              | 292 ms: 1.61x faster                                       |
| crypto_pyaes            | 117 ms                                                              | 73.6 ms: 1.58x faster                                      |
| chaos                   | 106 ms                                                              | 68.2 ms: 1.55x faster                                      |
| spectral_norm           | 150 ms                                                              | 97.5 ms: 1.54x faster                                      |
| nbody                   | 146 ms                                                              | 94.9 ms: 1.54x faster                                      |
| pickle_pure_python      | 457 us                                                              | 301 us: 1.52x faster                                       |
| hexiom                  | 9.50 ms                                                             | 6.36 ms: 1.49x faster                                      |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.49x faster                                       |
| float                   | 110 ms                                                              | 73.9 ms: 1.49x faster                                      |
| mako                    | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                      |
| logging_format          | 9.07 us                                                             | 6.35 us: 1.43x faster                                      |
| chameleon               | 9.13 ms                                                             | 6.42 ms: 1.42x faster                                      |
| logging_simple          | 8.21 us                                                             | 5.82 us: 1.41x faster                                      |
| deepcopy_memo           | 51.8 us                                                             | 36.9 us: 1.40x faster                                      |
| xml_etree_process       | 74.8 ms                                                             | 53.6 ms: 1.40x faster                                      |
| django_template         | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                      |
| genshi_text             | 30.4 ms                                                             | 22.0 ms: 1.38x faster                                      |
| html5lib                | 86.4 ms                                                             | 62.8 ms: 1.37x faster                                      |
| pprint_safe_repr        | 953 ms                                                              | 694 ms: 1.37x faster                                       |
| unpack_sequence         | 65.6 ns                                                             | 48.0 ns: 1.37x faster                                      |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                     |
| pprint_pformat          | 1.98 sec                                                            | 1.45 sec: 1.37x faster                                     |
| tornado_http            | 129 ms                                                              | 94.7 ms: 1.36x faster                                      |
| thrift                  | 1.04 ms                                                             | 763 us: 1.36x faster                                       |
| async_tree_none         | 713 ms                                                              | 525 ms: 1.36x faster                                       |
| async_tree_memoization  | 853 ms                                                              | 636 ms: 1.34x faster                                       |
| unpickle_pure_python    | 300 us                                                              | 227 us: 1.32x faster                                       |
| 2to3                    | 336 ms                                                              | 256 ms: 1.31x faster                                       |
| pycparser               | 1.53 sec                                                            | 1.18 sec: 1.30x faster                                     |
| regex_compile           | 177 ms                                                              | 136 ms: 1.30x faster                                       |
| scimark_fft             | 425 ms                                                              | 328 ms: 1.30x faster                                       |
| deepcopy                | 438 us                                                              | 340 us: 1.29x faster                                       |
| async_tree_cpu_io_mixed | 944 ms                                                              | 735 ms: 1.28x faster                                       |
| gunicorn                | 1.43 ms                                                             | 1.12 ms: 1.28x faster                                      |
| deepcopy_reduce         | 3.80 us                                                             | 2.98 us: 1.27x faster                                      |
| aiohttp                 | 1.35 ms                                                             | 1.06 ms: 1.27x faster                                      |
| docutils                | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                     |
| xml_etree_generate      | 94.9 ms                                                             | 76.7 ms: 1.24x faster                                      |
| fannkuch                | 485 ms                                                              | 393 ms: 1.24x faster                                       |
| sqlglot_normalize       | 135 ms                                                              | 109 ms: 1.23x faster                                       |
| genshi_xml              | 64.3 ms                                                             | 52.3 ms: 1.23x faster                                      |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.57 ms: 1.23x faster                                      |
| coroutines              | 31.8 ms                                                             | 26.0 ms: 1.22x faster                                      |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.21x faster                                       |
| dulwich_log             | 76.3 ms                                                             | 63.0 ms: 1.21x faster                                      |
| sqlglot_optimize        | 65.3 ms                                                             | 54.0 ms: 1.21x faster                                      |
| flaskblogging           | 8.48 ms                                                             | 7.04 ms: 1.21x faster                                      |
| sqlglot_transpile       | 2.45 ms                                                             | 2.04 ms: 1.20x faster                                      |
| dask                    | 437 ms                                                              | 368 ms: 1.19x faster                                       |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.8 ms: 1.19x faster                                      |
| async_generators        | 420 ms                                                              | 356 ms: 1.18x faster                                       |
| sqlglot_parse           | 2.07 ms                                                             | 1.75 ms: 1.18x faster                                      |
| nqueens                 | 98.8 ms                                                             | 83.8 ms: 1.18x faster                                      |
| json_loads              | 29.3 us                                                             | 24.9 us: 1.18x faster                                      |
| sqlite_synth            | 2.97 us                                                             | 2.53 us: 1.17x faster                                      |
| sympy_integrate         | 24.3 ms                                                             | 20.7 ms: 1.17x faster                                      |
| bench_thread_pool       | 954 us                                                              | 816 us: 1.17x faster                                       |
| regex_v8                | 24.9 ms                                                             | 21.4 ms: 1.16x faster                                      |
| sympy_str               | 328 ms                                                              | 285 ms: 1.15x faster                                       |
| sympy_expand            | 540 ms                                                              | 469 ms: 1.15x faster                                       |
| sympy_sum               | 185 ms                                                              | 162 ms: 1.14x faster                                       |
| json                    | 5.41 ms                                                             | 4.74 ms: 1.14x faster                                      |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.12x faster                                      |
| pylint                  | 521 ms                                                              | 465 ms: 1.12x faster                                       |
| pickle_list             | 4.73 us                                                             | 4.27 us: 1.11x faster                                      |
| regex_effbot            | 3.22 ms                                                             | 2.92 ms: 1.10x faster                                      |
| regex_dna               | 213 ms                                                              | 194 ms: 1.10x faster                                       |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.09x faster                                       |
| djangocms               | 36.3 us                                                             | 33.2 us: 1.09x faster                                      |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.09x faster                                      |
| pickle                  | 10.2 us                                                             | 9.37 us: 1.09x faster                                      |
| create_gc_cycles        | 1.64 ms                                                             | 1.51 ms: 1.09x faster                                      |
| json_dumps              | 13.7 ms                                                             | 12.7 ms: 1.08x faster                                      |
| pickle_dict             | 27.8 us                                                             | 26.0 us: 1.07x faster                                      |
| comprehensions          | 27.3 us                                                             | 25.9 us: 1.05x faster                                      |
| asyncio_tcp             | 922 ms                                                              | 888 ms: 1.04x faster                                       |
| xml_etree_parse         | 164 ms                                                              | 158 ms: 1.03x faster                                       |
| xml_etree_iterparse     | 111 ms                                                              | 108 ms: 1.03x faster                                       |
| generators              | 75.7 ms                                                             | 73.8 ms: 1.03x faster                                      |
| mdp                     | 2.75 sec                                                            | 2.69 sec: 1.02x faster                                     |
| telco                   | 6.67 ms                                                             | 6.59 ms: 1.01x faster                                      |
| pidigits                | 190 ms                                                              | 194 ms: 1.02x slower                                       |
| python_startup_no_site  | 5.80 ms                                                             | 6.01 ms: 1.04x slower                                      |
| gc_traversal            | 3.53 ms                                                             | 3.79 ms: 1.08x slower                                      |
| Geometric mean          | (ref)                                                               | 1.26x faster                                               |

Benchmark hidden because not significant (3): mypy2, bench_mp_pool, unpickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: coverage
