
# Results vs. 3.10.4

- fork: faster_cpython
- ref: nogil
- machine: linux-x86_64
- commit hash: 258cab1
- commit date: 2022-12-21
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 382 ms: 1.15x slower                                         |
| chameleon      | 8.86 ms                                                | 8.19 ms: 1.08x faster                                        |
| docutils       | 3.18 sec                                               | 5.22 sec: 1.64x slower                                       |
| html5lib       | 85.8 ms                                                | 82.2 ms: 1.04x faster                                        |
| tornado_http   | 128 ms                                                 | 124 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 108 ms                                                 | 104 ms: 1.03x faster                                         |
| nbody          | 136 ms                                                 | 170 ms: 1.25x slower                                         |
| pidigits       | 190 ms                                                 | 186 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 186 ms: 1.07x slower                                         |
| regex_dna      | 214 ms                                                 | 221 ms: 1.04x slower                                         |
| regex_effbot   | 3.21 ms                                                | 3.30 ms: 1.03x slower                                        |
| regex_v8       | 25.0 ms                                                | 24.4 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 28.9 us                                                | 32.4 us: 1.12x slower                                        |
| pickle               | 10.1 us                                                | 9.95 us: 1.02x faster                                        |
| pickle_dict          | 28.3 us                                                | 26.5 us: 1.07x faster                                        |
| pickle_list          | 4.50 us                                                | 4.23 us: 1.06x faster                                        |
| pickle_pure_python   | 453 us                                                 | 339 us: 1.34x faster                                         |
| unpickle             | 14.3 us                                                | 18.7 us: 1.31x slower                                        |
| unpickle_list        | 4.99 us                                                | 5.78 us: 1.16x slower                                        |
| unpickle_pure_python | 297 us                                                 | 263 us: 1.13x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 110 ms                                                 | 95.8 ms: 1.15x faster                                        |
| xml_etree_generate   | 93.3 ms                                                | 88.8 ms: 1.05x faster                                        |
| xml_etree_process    | 74.5 ms                                                | 72.0 ms: 1.03x faster                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 9.42 ms: 1.48x faster                                        |
| python_startup_no_site | 5.76 ms                                                | 5.92 ms: 1.03x slower                                        |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 42.2 ms: 1.10x faster                                        |
| genshi_text     | 30.6 ms                                                | 52.4 ms: 1.71x slower                                        |
| genshi_xml      | 63.6 ms                                                | 74.0 ms: 1.16x slower                                        |
| mako            | 14.3 ms                                                | 16.4 ms: 1.15x slower                                        |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 382 ms: 1.15x slower                                         |
| aiohttp                 | 1.34 ms                                                | 1.44 ms: 1.07x slower                                        |
| async_generators        | 428 ms                                                 | 623 ms: 1.46x slower                                         |
| async_tree_none         | 713 ms                                                 | 371 ms: 1.92x faster                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 616 ms: 1.54x faster                                         |
| async_tree_io           | 1.78 sec                                               | 827 ms: 2.15x faster                                         |
| async_tree_memoization  | 854 ms                                                 | 457 ms: 1.87x faster                                         |
| chameleon               | 8.86 ms                                                | 8.19 ms: 1.08x faster                                        |
| chaos                   | 104 ms                                                 | 101 ms: 1.03x faster                                         |
| bench_mp_pool           | 24.0 ms                                                | 23.9 ms: 1.01x faster                                        |
| bench_thread_pool       | 943 us                                                 | 1.18 ms: 1.25x slower                                        |
| coroutines              | 31.7 ms                                                | 72.4 ms: 2.29x slower                                        |
| coverage                | 75.3 ms                                                | 533 ms: 7.08x slower                                         |
| crypto_pyaes            | 118 ms                                                 | 121 ms: 1.03x slower                                         |
| deepcopy                | 429 us                                                 | 394 us: 1.09x faster                                         |
| deepcopy_reduce         | 3.75 us                                                | 3.65 us: 1.03x faster                                        |
| deepcopy_memo           | 50.0 us                                                | 40.0 us: 1.25x faster                                        |
| deltablue               | 7.39 ms                                                | 5.41 ms: 1.37x faster                                        |
| django_template         | 46.3 ms                                                | 42.2 ms: 1.10x faster                                        |
| docutils                | 3.18 sec                                               | 5.22 sec: 1.64x slower                                       |
| dulwich_log             | 75.5 ms                                                | 77.8 ms: 1.03x slower                                        |
| fannkuch                | 477 ms                                                 | 491 ms: 1.03x slower                                         |
| flaskblogging           | 8.38 ms                                                | 12.2 ms: 1.46x slower                                        |
| float                   | 108 ms                                                 | 104 ms: 1.03x faster                                         |
| generators              | 75.8 ms                                                | 81.3 ms: 1.07x slower                                        |
| genshi_text             | 30.6 ms                                                | 52.4 ms: 1.71x slower                                        |
| genshi_xml              | 63.6 ms                                                | 74.0 ms: 1.16x slower                                        |
| go                      | 226 ms                                                 | 159 ms: 1.43x faster                                         |
| gunicorn                | 1.43 ms                                                | 1.52 ms: 1.06x slower                                        |
| hexiom                  | 9.42 ms                                                | 7.69 ms: 1.22x faster                                        |
| html5lib                | 85.8 ms                                                | 82.2 ms: 1.04x faster                                        |
| json                    | 5.35 ms                                                | 5.44 ms: 1.02x slower                                        |
| json_loads              | 28.9 us                                                | 32.4 us: 1.12x slower                                        |
| logging_format          | 8.92 us                                                | 7.50 us: 1.19x faster                                        |
| logging_silent          | 173 ns                                                 | 96.4 ns: 1.80x faster                                        |
| logging_simple          | 8.06 us                                                | 6.85 us: 1.18x faster                                        |
| mako                    | 14.3 ms                                                | 16.4 ms: 1.15x slower                                        |
| mdp                     | 2.82 sec                                               | 3.04 sec: 1.08x slower                                       |
| meteor_contest          | 114 ms                                                 | 129 ms: 1.13x slower                                         |
| mypy                    | 1.01 sec                                               | 1.13 sec: 1.11x slower                                       |
| nbody                   | 136 ms                                                 | 170 ms: 1.25x slower                                         |
| nqueens                 | 99.3 ms                                                | 110 ms: 1.11x slower                                         |
| pathlib                 | 20.0 ms                                                | 20.4 ms: 1.02x slower                                        |
| pickle                  | 10.1 us                                                | 9.95 us: 1.02x faster                                        |
| pickle_dict             | 28.3 us                                                | 26.5 us: 1.07x faster                                        |
| pickle_list             | 4.50 us                                                | 4.23 us: 1.06x faster                                        |
| pickle_pure_python      | 453 us                                                 | 339 us: 1.34x faster                                         |
| pidigits                | 190 ms                                                 | 186 ms: 1.02x faster                                         |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                       |
| pycparser               | 1.51 sec                                               | 1.33 sec: 1.14x faster                                       |
| pyflate                 | 675 ms                                                 | 638 ms: 1.06x faster                                         |
| pylint                  | 519 ms                                                 | 633 ms: 1.22x slower                                         |
| python_startup          | 13.9 ms                                                | 9.42 ms: 1.48x faster                                        |
| python_startup_no_site  | 5.76 ms                                                | 5.92 ms: 1.03x slower                                        |
| raytrace                | 461 ms                                                 | 413 ms: 1.12x faster                                         |
| regex_compile           | 174 ms                                                 | 186 ms: 1.07x slower                                         |
| regex_dna               | 214 ms                                                 | 221 ms: 1.04x slower                                         |
| regex_effbot            | 3.21 ms                                                | 3.30 ms: 1.03x slower                                        |
| regex_v8                | 25.0 ms                                                | 24.4 ms: 1.02x faster                                        |
| richards                | 71.4 ms                                                | 39.1 ms: 1.83x faster                                        |
| scimark_fft             | 414 ms                                                 | 429 ms: 1.04x slower                                         |
| scimark_lu              | 158 ms                                                 | 151 ms: 1.05x faster                                         |
| scimark_monte_carlo     | 105 ms                                                 | 102 ms: 1.03x faster                                         |
| scimark_sor             | 193 ms                                                 | 147 ms: 1.31x faster                                         |
| scimark_sparse_mat_mult | 5.48 ms                                                | 6.10 ms: 1.11x slower                                        |
| spectral_norm           | 148 ms                                                 | 142 ms: 1.04x faster                                         |
| sqlglot_parse           | 2.04 ms                                                | 2.22 ms: 1.09x slower                                        |
| sqlglot_transpile       | 2.42 ms                                                | 2.58 ms: 1.07x slower                                        |
| sqlglot_optimize        | 65.3 ms                                                | 69.5 ms: 1.06x slower                                        |
| sqlglot_normalize       | 135 ms                                                 | 145 ms: 1.07x slower                                         |
| sqlite_synth            | 2.90 us                                                | 3.31 us: 1.14x slower                                        |
| sympy_integrate         | 23.9 ms                                                | 25.3 ms: 1.06x slower                                        |
| sympy_sum               | 183 ms                                                 | 211 ms: 1.15x slower                                         |
| sympy_str               | 324 ms                                                 | 333 ms: 1.03x slower                                         |
| telco                   | 6.68 ms                                                | 7.24 ms: 1.08x slower                                        |
| thrift                  | 1.03 ms                                                | 988 us: 1.04x faster                                         |
| tornado_http            | 128 ms                                                 | 124 ms: 1.04x faster                                         |
| unpack_sequence         | 59.5 ns                                                | 52.6 ns: 1.13x faster                                        |
| unpickle                | 14.3 us                                                | 18.7 us: 1.31x slower                                        |
| unpickle_list           | 4.99 us                                                | 5.78 us: 1.16x slower                                        |
| unpickle_pure_python    | 297 us                                                 | 263 us: 1.13x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                         |
| xml_etree_iterparse     | 110 ms                                                 | 95.8 ms: 1.15x faster                                        |
| xml_etree_generate      | 93.3 ms                                                | 88.8 ms: 1.05x faster                                        |
| xml_etree_process       | 74.5 ms                                                | 72.0 ms: 1.03x faster                                        |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): json_dumps, sympy_expand
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.9.10-258cab1/bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json: djangocms
