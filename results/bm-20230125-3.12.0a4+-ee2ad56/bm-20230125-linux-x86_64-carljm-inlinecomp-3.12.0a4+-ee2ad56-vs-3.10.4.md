
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp
- machine: linux-x86_64
- commit hash: ee2ad56
- commit date: 2023-01-25
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.34x faster                                         |
| chameleon      | 9.17 ms                                                | 6.35 ms: 1.44x faster                                        |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                       |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                        |
| tornado_http   | 128 ms                                                 | 94.5 ms: 1.36x faster                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.9 ms: 1.53x faster                                        |
| float          | 109 ms                                                 | 72.0 ms: 1.51x faster                                        |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                         |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                        |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                         |
| regex_effbot   | 3.19 ms                                                | 3.42 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                         |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                         |
| json_dumps           | 13.4 ms                                                | 9.57 ms: 1.41x faster                                        |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.39x faster                                        |
| xml_etree_generate   | 93.8 ms                                                | 78.2 ms: 1.20x faster                                        |
| json_loads           | 28.7 us                                                | 24.2 us: 1.18x faster                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                         |
| pickle_list          | 4.72 us                                                | 4.29 us: 1.10x faster                                        |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                        |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                         |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                        |
| unpickle_list        | 4.92 us                                                | 5.05 us: 1.03x slower                                        |
| pickle_dict          | 27.6 us                                                | 32.4 us: 1.17x slower                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.89 ms: 1.59x faster                                        |
| python_startup_no_site | 5.78 ms                                                | 6.44 ms: 1.12x slower                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.70 ms: 1.51x faster                                        |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                        |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                        |
| genshi_xml      | 63.7 ms                                                | 46.8 ms: 1.36x faster                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                        |
| logging_silent          | 176 ns                                                 | 91.7 ns: 1.92x faster                                        |
| asyncio_tcp             | 914 ms                                                 | 492 ms: 1.86x faster                                         |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                         |
| richards                | 75.2 ms                                                | 42.6 ms: 1.77x faster                                        |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                         |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                         |
| scimark_monte_carlo     | 109 ms                                                 | 64.7 ms: 1.68x faster                                        |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                         |
| chaos                   | 106 ms                                                 | 64.6 ms: 1.63x faster                                        |
| crypto_pyaes            | 117 ms                                                 | 72.9 ms: 1.60x faster                                        |
| python_startup          | 14.1 ms                                                | 8.89 ms: 1.59x faster                                        |
| hexiom                  | 9.43 ms                                                | 5.99 ms: 1.57x faster                                        |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                         |
| spectral_norm           | 150 ms                                                 | 96.2 ms: 1.55x faster                                        |
| nbody                   | 144 ms                                                 | 93.9 ms: 1.53x faster                                        |
| float                   | 109 ms                                                 | 72.0 ms: 1.51x faster                                        |
| mako                    | 14.7 ms                                                | 9.70 ms: 1.51x faster                                        |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                         |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                         |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                        |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                        |
| chameleon               | 9.17 ms                                                | 6.35 ms: 1.44x faster                                        |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                        |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                       |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                        |
| json_dumps              | 13.4 ms                                                | 9.57 ms: 1.41x faster                                        |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                       |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                        |
| logging_simple          | 8.10 us                                                | 5.80 us: 1.40x faster                                        |
| pprint_safe_repr        | 953 ms                                                 | 684 ms: 1.39x faster                                         |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.39x faster                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                         |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                        |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.36x faster                                         |
| genshi_xml              | 63.7 ms                                                | 46.8 ms: 1.36x faster                                        |
| tornado_http            | 128 ms                                                 | 94.5 ms: 1.36x faster                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                       |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                         |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                        |
| 2to3                    | 335 ms                                                 | 249 ms: 1.34x faster                                         |
| unpack_sequence         | 59.4 ns                                                | 44.4 ns: 1.34x faster                                        |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                         |
| fannkuch                | 488 ms                                                 | 369 ms: 1.32x faster                                         |
| async_tree_memoization  | 855 ms                                                 | 656 ms: 1.30x faster                                         |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                        |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.30x faster                                         |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                        |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                         |
| coroutines              | 31.6 ms                                                | 25.6 ms: 1.24x faster                                        |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                        |
| dulwich_log             | 75.8 ms                                                | 62.2 ms: 1.22x faster                                        |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                         |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                         |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                         |
| xml_etree_generate      | 93.8 ms                                                | 78.2 ms: 1.20x faster                                        |
| sympy_expand            | 534 ms                                                 | 450 ms: 1.19x faster                                         |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                         |
| json_loads              | 28.7 us                                                | 24.2 us: 1.18x faster                                        |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                        |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.14x faster                                        |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                        |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                         |
| pickle_list             | 4.72 us                                                | 4.29 us: 1.10x faster                                        |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                       |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                         |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                        |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                         |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                         |
| telco                   | 6.73 ms                                                | 6.46 ms: 1.04x faster                                        |
| generators              | 76.4 ms                                                | 75.9 ms: 1.01x faster                                        |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                         |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                        |
| unpickle_list           | 4.92 us                                                | 5.05 us: 1.03x slower                                        |
| gc_traversal            | 3.53 ms                                                | 3.64 ms: 1.03x slower                                        |
| regex_effbot            | 3.19 ms                                                | 3.42 ms: 1.07x slower                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.44 ms: 1.12x slower                                        |
| dask                    | 436 ms                                                 | 500 ms: 1.15x slower                                         |
| pickle_dict             | 27.6 us                                                | 32.4 us: 1.17x slower                                        |
| coverage                | 74.7 ms                                                | 97.3 ms: 1.30x slower                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230125-3.12.0a4+-ee2ad56/bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56.json: mypy
