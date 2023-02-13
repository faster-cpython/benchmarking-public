
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                          |
| chameleon      | 8.86 ms                                                | 6.47 ms: 1.37x faster                                         |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                        |
| html5lib       | 85.8 ms                                                | 60.6 ms: 1.42x faster                                         |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.8 ms: 1.48x faster                                         |
| nbody          | 136 ms                                                 | 94.0 ms: 1.45x faster                                         |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                         |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                          |
| regex_effbot   | 3.21 ms                                                | 3.66 ms: 1.14x slower                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 291 us: 1.56x faster                                          |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.49x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                         |
| xml_etree_process    | 74.5 ms                                                | 54.8 ms: 1.36x faster                                         |
| json_loads           | 28.9 us                                                | 23.7 us: 1.22x faster                                         |
| xml_etree_generate   | 93.3 ms                                                | 80.2 ms: 1.16x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                          |
| pickle_list          | 4.50 us                                                | 4.15 us: 1.08x faster                                         |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.08x faster                                          |
| unpickle             | 14.3 us                                                | 13.7 us: 1.04x faster                                         |
| unpickle_list        | 4.99 us                                                | 5.13 us: 1.03x slower                                         |
| pickle_dict          | 28.3 us                                                | 30.9 us: 1.09x slower                                         |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                  |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.90 ms: 1.57x faster                                         |
| python_startup_no_site | 5.76 ms                                                | 6.46 ms: 1.12x slower                                         |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                         |
| mako            | 14.3 ms                                                | 9.90 ms: 1.44x faster                                         |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                         |
| genshi_xml      | 63.6 ms                                                | 47.8 ms: 1.33x faster                                         |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.13 ms: 2.36x faster                                         |
| logging_silent          | 173 ns                                                 | 94.1 ns: 1.84x faster                                         |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                          |
| richards                | 71.4 ms                                                | 42.1 ms: 1.70x faster                                         |
| pyflate                 | 675 ms                                                 | 403 ms: 1.68x faster                                          |
| raytrace                | 461 ms                                                 | 279 ms: 1.65x faster                                          |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                          |
| chaos                   | 104 ms                                                 | 63.2 ms: 1.65x faster                                         |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.60x faster                                         |
| hexiom                  | 9.42 ms                                                | 5.87 ms: 1.60x faster                                         |
| scimark_monte_carlo     | 105 ms                                                 | 65.5 ms: 1.60x faster                                         |
| spectral_norm           | 148 ms                                                 | 93.9 ms: 1.58x faster                                         |
| python_startup          | 13.9 ms                                                | 8.90 ms: 1.57x faster                                         |
| pickle_pure_python      | 453 us                                                 | 291 us: 1.56x faster                                          |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.49x faster                                          |
| float                   | 108 ms                                                 | 72.8 ms: 1.48x faster                                         |
| deepcopy_memo           | 50.0 us                                                | 34.1 us: 1.47x faster                                         |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                          |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                         |
| nbody                   | 136 ms                                                 | 94.0 ms: 1.45x faster                                         |
| mako                    | 14.3 ms                                                | 9.90 ms: 1.44x faster                                         |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                         |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                        |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                         |
| async_tree_none         | 713 ms                                                 | 498 ms: 1.43x faster                                          |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                         |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.42x faster                                         |
| html5lib                | 85.8 ms                                                | 60.6 ms: 1.42x faster                                         |
| pprint_safe_repr        | 943 ms                                                 | 668 ms: 1.41x faster                                          |
| logging_format          | 8.92 us                                                | 6.39 us: 1.40x faster                                         |
| async_tree_memoization  | 854 ms                                                 | 612 ms: 1.40x faster                                          |
| async_tree_io           | 1.78 sec                                               | 1.27 sec: 1.39x faster                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.94 ms: 1.39x faster                                         |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.39x faster                                        |
| logging_simple          | 8.06 us                                                | 5.83 us: 1.38x faster                                         |
| chameleon               | 8.86 ms                                                | 6.47 ms: 1.37x faster                                         |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                          |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 54.8 ms: 1.36x faster                                         |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                          |
| scimark_fft             | 414 ms                                                 | 307 ms: 1.35x faster                                          |
| unpack_sequence         | 59.5 ns                                                | 44.4 ns: 1.34x faster                                         |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                         |
| sqlglot_normalize       | 135 ms                                                 | 101 ms: 1.33x faster                                          |
| genshi_xml              | 63.6 ms                                                | 47.8 ms: 1.33x faster                                         |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                         |
| deepcopy                | 429 us                                                 | 324 us: 1.33x faster                                          |
| nqueens                 | 99.3 ms                                                | 74.9 ms: 1.32x faster                                         |
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                          |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                          |
| sqlglot_optimize        | 65.3 ms                                                | 50.4 ms: 1.30x faster                                         |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 747 ms: 1.27x faster                                          |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 134 ms: 1.23x faster                                          |
| sympy_integrate         | 23.9 ms                                                | 19.5 ms: 1.23x faster                                         |
| coroutines              | 31.7 ms                                                | 25.8 ms: 1.23x faster                                         |
| sympy_str               | 324 ms                                                 | 265 ms: 1.22x faster                                          |
| sympy_expand            | 537 ms                                                 | 439 ms: 1.22x faster                                          |
| json_loads              | 28.9 us                                                | 23.7 us: 1.22x faster                                         |
| sqlalchemy_imperative   | 21.0 ms                                                | 17.4 ms: 1.21x faster                                         |
| dulwich_log             | 75.5 ms                                                | 62.6 ms: 1.21x faster                                         |
| bench_thread_pool       | 943 us                                                 | 785 us: 1.20x faster                                          |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                          |
| json                    | 5.35 ms                                                | 4.55 ms: 1.18x faster                                         |
| xml_etree_generate      | 93.3 ms                                                | 80.2 ms: 1.16x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                         |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                          |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                          |
| pickle_list             | 4.50 us                                                | 4.15 us: 1.08x faster                                         |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.08x faster                                          |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                        |
| unpickle                | 14.3 us                                                | 13.7 us: 1.04x faster                                         |
| telco                   | 6.68 ms                                                | 6.40 ms: 1.04x faster                                         |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                          |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                          |
| generators              | 75.8 ms                                                | 77.7 ms: 1.03x slower                                         |
| unpickle_list           | 4.99 us                                                | 5.13 us: 1.03x slower                                         |
| pickle_dict             | 28.3 us                                                | 30.9 us: 1.09x slower                                         |
| python_startup_no_site  | 5.76 ms                                                | 6.46 ms: 1.12x slower                                         |
| regex_effbot            | 3.21 ms                                                | 3.66 ms: 1.14x slower                                         |
| coverage                | 75.3 ms                                                | 99.3 ms: 1.32x slower                                         |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                  |

Benchmark hidden because not significant (3): bench_mp_pool, pickle, async_generators
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230210-3.12.0a5+-36b2917/bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
