
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: ae0bd02
- commit date: 2023-02-13
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 245 ms: 1.37x faster                                          |
| chameleon      | 9.17 ms                                                | 6.44 ms: 1.42x faster                                         |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                        |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                         |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.7 ms: 1.50x faster                                         |
| nbody          | 144 ms                                                 | 99.9 ms: 1.44x faster                                         |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                         |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                          |
| regex_effbot   | 3.19 ms                                                | 3.50 ms: 1.10x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                          |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                          |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                         |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                         |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                         |
| xml_etree_generate   | 93.8 ms                                                | 80.4 ms: 1.17x faster                                         |
| pickle_list          | 4.72 us                                                | 4.13 us: 1.14x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 99.8 ms: 1.11x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                         |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                         |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                         |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                         |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.89 ms: 1.58x faster                                         |
| python_startup_no_site | 5.78 ms                                                | 6.45 ms: 1.12x slower                                         |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                         |
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                         |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                         |
| genshi_xml      | 63.7 ms                                                | 46.8 ms: 1.36x faster                                         |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                         |
| deltablue               | 7.28 ms                                                | 3.18 ms: 2.29x faster                                         |
| logging_silent          | 176 ns                                                 | 93.8 ns: 1.88x faster                                         |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                          |
| asyncio_tcp             | 914 ms                                                 | 502 ms: 1.82x faster                                          |
| richards                | 75.2 ms                                                | 43.1 ms: 1.74x faster                                         |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                          |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                         |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                          |
| chaos                   | 106 ms                                                 | 65.2 ms: 1.62x faster                                         |
| go                      | 226 ms                                                 | 139 ms: 1.62x faster                                          |
| spectral_norm           | 150 ms                                                 | 93.5 ms: 1.60x faster                                         |
| crypto_pyaes            | 117 ms                                                 | 73.4 ms: 1.59x faster                                         |
| python_startup          | 14.1 ms                                                | 8.89 ms: 1.58x faster                                         |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                          |
| hexiom                  | 9.43 ms                                                | 6.12 ms: 1.54x faster                                         |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                          |
| float                   | 109 ms                                                 | 72.7 ms: 1.50x faster                                         |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                         |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                          |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                         |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                         |
| nbody                   | 144 ms                                                 | 99.9 ms: 1.44x faster                                         |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                         |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                        |
| chameleon               | 9.17 ms                                                | 6.44 ms: 1.42x faster                                         |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                         |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                         |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                         |
| pprint_safe_repr        | 953 ms                                                 | 679 ms: 1.40x faster                                          |
| scimark_fft             | 421 ms                                                 | 300 ms: 1.40x faster                                          |
| async_tree_none         | 711 ms                                                 | 507 ms: 1.40x faster                                          |
| async_tree_io           | 1.78 sec                                               | 1.27 sec: 1.40x faster                                        |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                         |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                         |
| logging_simple          | 8.10 us                                                | 5.82 us: 1.39x faster                                         |
| async_tree_memoization  | 855 ms                                                 | 615 ms: 1.39x faster                                          |
| coroutines              | 31.6 ms                                                | 22.9 ms: 1.38x faster                                         |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                        |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                          |
| thrift                  | 1.03 ms                                                | 754 us: 1.37x faster                                          |
| 2to3                    | 335 ms                                                 | 245 ms: 1.37x faster                                          |
| genshi_xml              | 63.7 ms                                                | 46.8 ms: 1.36x faster                                         |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                         |
| sqlglot_normalize       | 134 ms                                                 | 99.7 ms: 1.35x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                         |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                         |
| mypy2                   | 430 ms                                                 | 325 ms: 1.32x faster                                          |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                         |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                          |
| sqlglot_optimize        | 65.2 ms                                                | 49.9 ms: 1.31x faster                                         |
| unpack_sequence         | 59.4 ns                                                | 45.5 ns: 1.31x faster                                         |
| fannkuch                | 488 ms                                                 | 376 ms: 1.30x faster                                          |
| async_tree_cpu_io_mixed | 949 ms                                                 | 743 ms: 1.28x faster                                          |
| nqueens                 | 100 ms                                                 | 79.7 ms: 1.26x faster                                         |
| deepcopy_reduce         | 3.79 us                                                | 3.03 us: 1.25x faster                                         |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.4 ms: 1.24x faster                                         |
| sympy_integrate         | 24.0 ms                                                | 19.6 ms: 1.23x faster                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.22x faster                                          |
| sympy_str               | 325 ms                                                 | 268 ms: 1.21x faster                                          |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                         |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                          |
| sympy_expand            | 534 ms                                                 | 446 ms: 1.20x faster                                          |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                         |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.17x faster                                          |
| xml_etree_generate      | 93.8 ms                                                | 80.4 ms: 1.17x faster                                         |
| pickle_list             | 4.72 us                                                | 4.13 us: 1.14x faster                                         |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.14x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                         |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.11x faster                                         |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                         |
| xml_etree_iterparse     | 111 ms                                                 | 99.8 ms: 1.11x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| json                    | 5.35 ms                                                | 4.85 ms: 1.10x faster                                         |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                          |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.09x faster                                        |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                         |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                          |
| telco                   | 6.73 ms                                                | 6.33 ms: 1.06x faster                                         |
| async_generators        | 426 ms                                                 | 414 ms: 1.03x faster                                          |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                         |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                          |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                         |
| regex_effbot            | 3.19 ms                                                | 3.50 ms: 1.10x slower                                         |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                         |
| python_startup_no_site  | 5.78 ms                                                | 6.45 ms: 1.12x slower                                         |
| gc_traversal            | 3.53 ms                                                | 4.04 ms: 1.15x slower                                         |
| coverage                | 74.7 ms                                                | 98.2 ms: 1.31x slower                                         |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
