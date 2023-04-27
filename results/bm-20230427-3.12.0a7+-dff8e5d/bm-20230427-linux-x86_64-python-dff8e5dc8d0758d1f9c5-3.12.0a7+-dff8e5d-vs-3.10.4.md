
# Results vs. 3.10.4

- fork: python
- ref: dff8e5dc8d0758d1f9c5
- machine: linux-x86_64
- commit hash: dff8e5d
- commit date: 2023-04-27
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 267 ms: 1.26x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.90 ms: 1.32x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                 |
| html5lib       | 86.4 ms                                                             | 64.9 ms: 1.33x faster                                                  |
| tornado_http   | 129 ms                                                              | 105 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                               | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.9 ms: 1.64x faster                                                  |
| float          | 110 ms                                                              | 81.6 ms: 1.35x faster                                                  |
| pidigits       | 190 ms                                                              | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                               | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.23x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.79 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 316 us: 1.45x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 216 us: 1.39x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 10.1 ms: 1.35x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 58.6 ms: 1.28x faster                                                  |
| json_loads           | 29.3 us                                                             | 25.9 us: 1.13x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 84.7 ms: 1.12x faster                                                  |
| xml_etree_parse      | 164 ms                                                              | 151 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                   |
| pickle_list          | 4.73 us                                                             | 4.64 us: 1.02x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 4.86 us: 1.02x faster                                                  |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 32.3 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.07 ms: 1.56x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.66 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.7 ms: 1.37x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 22.4 ms: 1.36x faster                                                  |
| django_template | 45.8 ms                                                             | 35.1 ms: 1.31x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 50.2 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 30.7 ms: 2.47x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.54 ms: 2.06x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                   |
| richards                | 74.2 ms                                                             | 43.7 ms: 1.70x faster                                                  |
| nbody                   | 146 ms                                                              | 88.9 ms: 1.64x faster                                                  |
| go                      | 226 ms                                                              | 138 ms: 1.64x faster                                                   |
| logging_silent          | 169 ns                                                              | 103 ns: 1.63x faster                                                   |
| scimark_sor             | 198 ms                                                              | 126 ms: 1.57x faster                                                   |
| python_startup          | 14.1 ms                                                             | 9.07 ms: 1.56x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 6.11 ms: 1.56x faster                                                  |
| raytrace                | 470 ms                                                              | 304 ms: 1.55x faster                                                   |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.54x faster                                                  |
| chaos                   | 106 ms                                                              | 69.0 ms: 1.54x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 72.8 ms: 1.49x faster                                                  |
| pyflate                 | 671 ms                                                              | 450 ms: 1.49x faster                                                   |
| crypto_pyaes            | 117 ms                                                              | 78.5 ms: 1.49x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.65 ms: 1.49x faster                                                  |
| scimark_lu              | 160 ms                                                              | 110 ms: 1.46x faster                                                   |
| pickle_pure_python      | 457 us                                                              | 316 us: 1.45x faster                                                   |
| coroutines              | 31.8 ms                                                             | 22.3 ms: 1.43x faster                                                  |
| spectral_norm           | 150 ms                                                              | 106 ms: 1.41x faster                                                   |
| unpickle_pure_python    | 300 us                                                              | 216 us: 1.39x faster                                                   |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                                 |
| unpack_sequence         | 65.6 ns                                                             | 47.3 ns: 1.39x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.7 ms: 1.37x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.13 sec: 1.36x faster                                                 |
| genshi_text             | 30.4 ms                                                             | 22.4 ms: 1.36x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 10.1 ms: 1.35x faster                                                  |
| async_tree_none         | 713 ms                                                              | 529 ms: 1.35x faster                                                   |
| float                   | 110 ms                                                              | 81.6 ms: 1.35x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 38.9 us: 1.33x faster                                                  |
| html5lib                | 86.4 ms                                                             | 64.9 ms: 1.33x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.49 sec: 1.32x faster                                                 |
| chameleon               | 9.13 ms                                                             | 6.90 ms: 1.32x faster                                                  |
| async_tree_memoization  | 853 ms                                                              | 650 ms: 1.31x faster                                                   |
| logging_simple          | 8.21 us                                                             | 6.26 us: 1.31x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.93 us: 1.31x faster                                                  |
| django_template         | 45.8 ms                                                             | 35.1 ms: 1.31x faster                                                  |
| pprint_safe_repr        | 953 ms                                                              | 731 ms: 1.30x faster                                                   |
| fannkuch                | 485 ms                                                              | 373 ms: 1.30x faster                                                   |
| thrift                  | 1.04 ms                                                             | 801 us: 1.29x faster                                                   |
| genshi_xml              | 64.3 ms                                                             | 50.2 ms: 1.28x faster                                                  |
| xml_etree_process       | 74.8 ms                                                             | 58.6 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 749 ms: 1.26x faster                                                   |
| 2to3                    | 336 ms                                                              | 267 ms: 1.26x faster                                                   |
| mypy2                   | 432 ms                                                              | 349 ms: 1.24x faster                                                   |
| tornado_http            | 129 ms                                                              | 105 ms: 1.23x faster                                                   |
| regex_compile           | 177 ms                                                              | 145 ms: 1.23x faster                                                   |
| nqueens                 | 98.8 ms                                                             | 81.3 ms: 1.22x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.62 ms: 1.22x faster                                                  |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                                   |
| deepcopy                | 438 us                                                              | 366 us: 1.20x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 54.6 ms: 1.20x faster                                                  |
| deepcopy_reduce         | 3.80 us                                                             | 3.18 us: 1.19x faster                                                  |
| scimark_fft             | 425 ms                                                              | 359 ms: 1.19x faster                                                   |
| docutils                | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                 |
| comprehensions          | 27.3 us                                                             | 23.2 us: 1.18x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 830 us: 1.15x faster                                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 22.1 ms: 1.13x faster                                                  |
| json_loads              | 29.3 us                                                             | 25.9 us: 1.13x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 68.0 ms: 1.12x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 84.7 ms: 1.12x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 21.8 ms: 1.11x faster                                                  |
| pathlib                 | 19.8 ms                                                             | 17.8 ms: 1.11x faster                                                  |
| pylint                  | 521 ms                                                              | 470 ms: 1.11x faster                                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.50 ms: 1.09x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.4 ms: 1.09x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.73 us: 1.09x faster                                                  |
| json                    | 5.41 ms                                                             | 4.98 ms: 1.09x faster                                                  |
| xml_etree_parse         | 164 ms                                                              | 151 ms: 1.08x faster                                                   |
| djangocms               | 36.3 us                                                             | 33.7 us: 1.08x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                   |
| sympy_expand            | 540 ms                                                              | 503 ms: 1.07x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.59 sec: 1.06x faster                                                 |
| sympy_str               | 328 ms                                                              | 309 ms: 1.06x faster                                                   |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                   |
| sympy_sum               | 185 ms                                                              | 180 ms: 1.02x faster                                                   |
| pickle_list             | 4.73 us                                                             | 4.64 us: 1.02x faster                                                  |
| unpickle_list           | 4.94 us                                                             | 4.86 us: 1.02x faster                                                  |
| pidigits                | 190 ms                                                              | 189 ms: 1.01x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.89 ms: 1.03x slower                                                  |
| async_generators        | 420 ms                                                              | 440 ms: 1.05x slower                                                   |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.95 ms: 1.12x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.66 ms: 1.15x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 32.3 us: 1.16x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.79 ms: 1.18x slower                                                  |
| dask                    | 437 ms                                                              | 538 ms: 1.23x slower                                                   |
| coverage                | 70.6 ms                                                             | 101 ms: 1.44x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.23x faster                                                           |

Benchmark hidden because not significant (3): unpickle, meteor_contest, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn
