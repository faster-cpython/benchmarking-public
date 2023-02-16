
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                          |
| chameleon      | 9.17 ms                                                | 6.47 ms: 1.42x faster                                         |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                        |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                         |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.0 ms: 1.53x faster                                         |
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                         |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.31x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                         |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                          |
| regex_effbot   | 3.19 ms                                                | 3.66 ms: 1.15x slower                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 291 us: 1.55x faster                                          |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                          |
| json_dumps           | 13.4 ms                                                | 9.39 ms: 1.43x faster                                         |
| xml_etree_process    | 74.5 ms                                                | 54.8 ms: 1.36x faster                                         |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                         |
| xml_etree_generate   | 93.8 ms                                                | 80.2 ms: 1.17x faster                                         |
| pickle_list          | 4.72 us                                                | 4.15 us: 1.14x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                          |
| unpickle             | 14.2 us                                                | 13.7 us: 1.04x faster                                         |
| unpickle_list        | 4.92 us                                                | 5.13 us: 1.04x slower                                         |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                         |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                  |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.90 ms: 1.58x faster                                         |
| python_startup_no_site | 5.78 ms                                                | 6.46 ms: 1.12x slower                                         |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.90 ms: 1.48x faster                                         |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                         |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                         |
| genshi_xml      | 63.7 ms                                                | 47.8 ms: 1.33x faster                                         |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.13 ms: 2.32x faster                                         |
| logging_silent          | 176 ns                                                 | 94.1 ns: 1.87x faster                                         |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                          |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.84x faster                                          |
| richards                | 75.2 ms                                                | 42.1 ms: 1.79x faster                                         |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                          |
| raytrace                | 467 ms                                                 | 279 ms: 1.67x faster                                          |
| chaos                   | 106 ms                                                 | 63.2 ms: 1.67x faster                                         |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                         |
| go                      | 226 ms                                                 | 137 ms: 1.64x faster                                          |
| hexiom                  | 9.43 ms                                                | 5.87 ms: 1.61x faster                                         |
| spectral_norm           | 150 ms                                                 | 93.9 ms: 1.59x faster                                         |
| crypto_pyaes            | 117 ms                                                 | 73.3 ms: 1.59x faster                                         |
| python_startup          | 14.1 ms                                                | 8.90 ms: 1.58x faster                                         |
| pickle_pure_python      | 452 us                                                 | 291 us: 1.55x faster                                          |
| nbody                   | 144 ms                                                 | 94.0 ms: 1.53x faster                                         |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                          |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.51x faster                                         |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                         |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                          |
| mako                    | 14.7 ms                                                | 9.90 ms: 1.48x faster                                         |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                         |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                         |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                        |
| json_dumps              | 13.4 ms                                                | 9.39 ms: 1.43x faster                                         |
| async_tree_none         | 711 ms                                                 | 498 ms: 1.43x faster                                          |
| pprint_safe_repr        | 953 ms                                                 | 668 ms: 1.43x faster                                          |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                         |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                         |
| chameleon               | 9.17 ms                                                | 6.47 ms: 1.42x faster                                         |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                         |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                        |
| async_tree_memoization  | 855 ms                                                 | 612 ms: 1.40x faster                                          |
| async_tree_io           | 1.78 sec                                               | 1.27 sec: 1.40x faster                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                          |
| logging_simple          | 8.10 us                                                | 5.83 us: 1.39x faster                                         |
| logging_format          | 8.85 us                                                | 6.39 us: 1.39x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.94 ms: 1.38x faster                                         |
| scimark_fft             | 421 ms                                                 | 307 ms: 1.37x faster                                          |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                         |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                          |
| xml_etree_process       | 74.5 ms                                                | 54.8 ms: 1.36x faster                                         |
| deepcopy                | 438 us                                                 | 324 us: 1.35x faster                                          |
| unpack_sequence         | 59.4 ns                                                | 44.4 ns: 1.34x faster                                         |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                          |
| mypy2                   | 430 ms                                                 | 322 ms: 1.34x faster                                          |
| nqueens                 | 100 ms                                                 | 74.9 ms: 1.34x faster                                         |
| genshi_xml              | 63.7 ms                                                | 47.8 ms: 1.33x faster                                         |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                         |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                         |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                          |
| sqlglot_normalize       | 134 ms                                                 | 101 ms: 1.33x faster                                          |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                         |
| sqlglot_optimize        | 65.2 ms                                                | 50.4 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 747 ms: 1.27x faster                                          |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                        |
| sympy_integrate         | 24.0 ms                                                | 19.5 ms: 1.24x faster                                         |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.4 ms: 1.23x faster                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 134 ms: 1.23x faster                                          |
| coroutines              | 31.6 ms                                                | 25.8 ms: 1.23x faster                                         |
| sympy_str               | 325 ms                                                 | 265 ms: 1.23x faster                                          |
| sympy_expand            | 534 ms                                                 | 439 ms: 1.22x faster                                          |
| dulwich_log             | 75.8 ms                                                | 62.6 ms: 1.21x faster                                         |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                         |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.21x faster                                          |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                          |
| json                    | 5.35 ms                                                | 4.55 ms: 1.17x faster                                         |
| xml_etree_generate      | 93.8 ms                                                | 80.2 ms: 1.17x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                         |
| pickle_list             | 4.72 us                                                | 4.15 us: 1.14x faster                                         |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                         |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                         |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                          |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                          |
| telco                   | 6.73 ms                                                | 6.40 ms: 1.05x faster                                         |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                          |
| unpickle                | 14.2 us                                                | 13.7 us: 1.04x faster                                         |
| mdp                     | 2.74 sec                                               | 2.66 sec: 1.03x faster                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                          |
| gc_traversal            | 3.53 ms                                                | 3.58 ms: 1.02x slower                                         |
| generators              | 76.4 ms                                                | 77.7 ms: 1.02x slower                                         |
| unpickle_list           | 4.92 us                                                | 5.13 us: 1.04x slower                                         |
| python_startup_no_site  | 5.78 ms                                                | 6.46 ms: 1.12x slower                                         |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                         |
| regex_effbot            | 3.19 ms                                                | 3.66 ms: 1.15x slower                                         |
| coverage                | 74.7 ms                                                | 99.3 ms: 1.33x slower                                         |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                  |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, async_generators
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
