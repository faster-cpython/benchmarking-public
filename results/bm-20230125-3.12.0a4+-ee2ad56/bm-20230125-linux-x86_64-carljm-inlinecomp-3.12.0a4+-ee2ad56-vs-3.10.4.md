
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
| 2to3           | 332 ms                                                 | 249 ms: 1.33x faster                                         |
| chameleon      | 8.86 ms                                                | 6.35 ms: 1.39x faster                                        |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                       |
| html5lib       | 85.8 ms                                                | 60.1 ms: 1.43x faster                                        |
| tornado_http   | 128 ms                                                 | 94.5 ms: 1.36x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.0 ms: 1.50x faster                                        |
| nbody          | 136 ms                                                 | 93.9 ms: 1.45x faster                                        |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                         |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                         |
| regex_effbot   | 3.21 ms                                                | 3.42 ms: 1.07x slower                                        |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.57 ms: 1.41x faster                                        |
| json_loads           | 28.9 us                                                | 24.2 us: 1.19x faster                                        |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                        |
| pickle_dict          | 28.3 us                                                | 32.4 us: 1.14x slower                                        |
| pickle_list          | 4.50 us                                                | 4.29 us: 1.05x faster                                        |
| pickle_pure_python   | 453 us                                                 | 288 us: 1.57x faster                                         |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                        |
| unpickle_list        | 4.99 us                                                | 5.05 us: 1.01x slower                                        |
| unpickle_pure_python | 297 us                                                 | 201 us: 1.48x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                         |
| xml_etree_generate   | 93.3 ms                                                | 78.2 ms: 1.19x faster                                        |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.38x faster                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.89 ms: 1.57x faster                                        |
| python_startup_no_site | 5.76 ms                                                | 6.44 ms: 1.12x slower                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                        |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                        |
| genshi_xml      | 63.6 ms                                                | 46.8 ms: 1.36x faster                                        |
| mako            | 14.3 ms                                                | 9.70 ms: 1.47x faster                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 249 ms: 1.33x faster                                         |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.34x faster                                         |
| async_generators        | 428 ms                                                 | 355 ms: 1.20x faster                                         |
| async_tree_none         | 713 ms                                                 | 521 ms: 1.37x faster                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                         |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                       |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                         |
| chameleon               | 8.86 ms                                                | 6.35 ms: 1.39x faster                                        |
| chaos                   | 104 ms                                                 | 64.6 ms: 1.61x faster                                        |
| bench_thread_pool       | 943 us                                                 | 781 us: 1.21x faster                                         |
| coroutines              | 31.7 ms                                                | 25.6 ms: 1.24x faster                                        |
| coverage                | 75.3 ms                                                | 97.3 ms: 1.29x slower                                        |
| crypto_pyaes            | 118 ms                                                 | 72.9 ms: 1.61x faster                                        |
| deepcopy                | 429 us                                                 | 328 us: 1.31x faster                                         |
| deepcopy_reduce         | 3.75 us                                                | 2.96 us: 1.27x faster                                        |
| deepcopy_memo           | 50.0 us                                                | 34.6 us: 1.45x faster                                        |
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                        |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                        |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                       |
| dulwich_log             | 75.5 ms                                                | 62.2 ms: 1.21x faster                                        |
| fannkuch                | 477 ms                                                 | 369 ms: 1.29x faster                                         |
| float                   | 108 ms                                                 | 72.0 ms: 1.50x faster                                        |
| generators              | 75.8 ms                                                | 75.9 ms: 1.00x slower                                        |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                        |
| genshi_xml              | 63.6 ms                                                | 46.8 ms: 1.36x faster                                        |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                         |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                        |
| hexiom                  | 9.42 ms                                                | 5.99 ms: 1.57x faster                                        |
| html5lib                | 85.8 ms                                                | 60.1 ms: 1.43x faster                                        |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                        |
| json_dumps              | 13.5 ms                                                | 9.57 ms: 1.41x faster                                        |
| json_loads              | 28.9 us                                                | 24.2 us: 1.19x faster                                        |
| logging_format          | 8.92 us                                                | 6.31 us: 1.41x faster                                        |
| logging_silent          | 173 ns                                                 | 91.7 ns: 1.89x faster                                        |
| logging_simple          | 8.06 us                                                | 5.80 us: 1.39x faster                                        |
| mako                    | 14.3 ms                                                | 9.70 ms: 1.47x faster                                        |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                       |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                         |
| mypy                    | 1.01 sec                                               | 802 ms: 1.26x faster                                         |
| nbody                   | 136 ms                                                 | 93.9 ms: 1.45x faster                                        |
| nqueens                 | 99.3 ms                                                | 76.9 ms: 1.29x faster                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                        |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                        |
| pickle_dict             | 28.3 us                                                | 32.4 us: 1.14x slower                                        |
| pickle_list             | 4.50 us                                                | 4.29 us: 1.05x faster                                        |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.57x faster                                         |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                         |
| pprint_safe_repr        | 943 ms                                                 | 684 ms: 1.38x faster                                         |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                       |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.39x faster                                       |
| pyflate                 | 675 ms                                                 | 400 ms: 1.69x faster                                         |
| python_startup          | 13.9 ms                                                | 8.89 ms: 1.57x faster                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.44 ms: 1.12x slower                                        |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                         |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                         |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                         |
| regex_effbot            | 3.21 ms                                                | 3.42 ms: 1.07x slower                                        |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                        |
| richards                | 71.4 ms                                                | 42.6 ms: 1.68x faster                                        |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                         |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.49x faster                                         |
| scimark_monte_carlo     | 105 ms                                                 | 64.7 ms: 1.62x faster                                        |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                         |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.99 ms: 1.37x faster                                        |
| spectral_norm           | 148 ms                                                 | 96.2 ms: 1.54x faster                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                        |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                        |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                         |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                        |
| sympy_expand            | 537 ms                                                 | 450 ms: 1.19x faster                                         |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.22x faster                                        |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                         |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                         |
| telco                   | 6.68 ms                                                | 6.46 ms: 1.03x faster                                        |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                         |
| tornado_http            | 128 ms                                                 | 94.5 ms: 1.36x faster                                        |
| unpack_sequence         | 59.5 ns                                                | 44.4 ns: 1.34x faster                                        |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                        |
| unpickle_list           | 4.99 us                                                | 5.05 us: 1.01x slower                                        |
| unpickle_pure_python    | 297 us                                                 | 201 us: 1.48x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                         |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                         |
| xml_etree_generate      | 93.3 ms                                                | 78.2 ms: 1.19x faster                                        |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.38x faster                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230125-3.12.0a4+-ee2ad56/bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
