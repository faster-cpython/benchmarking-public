
# Results vs. 3.10.4

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: 7f90633
- commit date: 2023-04-28
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 268 ms: 1.25x faster                                                         |
| docutils       | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                       |
| html5lib       | 86.4 ms                                                             | 65.1 ms: 1.33x faster                                                        |
| tornado_http   | 129 ms                                                              | 105 ms: 1.23x faster                                                         |
| Geometric mean | (ref)                                                               | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.2 ms: 1.65x faster                                                        |
| float          | 110 ms                                                              | 82.1 ms: 1.34x faster                                                        |
| pidigits       | 190 ms                                                              | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                               | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 143 ms: 1.24x faster                                                         |
| regex_v8       | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                                        |
| regex_dna      | 213 ms                                                              | 205 ms: 1.04x faster                                                         |
| regex_effbot   | 3.22 ms                                                             | 3.41 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 317 us: 1.44x faster                                                         |
| unpickle_pure_python | 300 us                                                              | 217 us: 1.38x faster                                                         |
| json_dumps           | 13.7 ms                                                             | 10.2 ms: 1.35x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 58.7 ms: 1.27x faster                                                        |
| json_loads           | 29.3 us                                                             | 25.8 us: 1.14x faster                                                        |
| xml_etree_generate   | 94.9 ms                                                             | 84.2 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                              | 105 ms: 1.06x faster                                                         |
| xml_etree_parse      | 164 ms                                                              | 158 ms: 1.04x faster                                                         |
| unpickle_list        | 4.94 us                                                             | 4.91 us: 1.01x faster                                                        |
| pickle_list          | 4.73 us                                                             | 4.70 us: 1.01x faster                                                        |
| pickle               | 10.2 us                                                             | 10.8 us: 1.05x slower                                                        |
| pickle_dict          | 27.8 us                                                             | 32.6 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.11x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.08 ms: 1.56x faster                                                        |
| python_startup_no_site | 5.80 ms                                                             | 6.66 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 14.7 ms                                                             | 10.9 ms: 1.36x faster                                                        |
| genshi_text    | 30.4 ms                                                             | 22.7 ms: 1.34x faster                                                        |
| genshi_xml     | 64.3 ms                                                             | 50.8 ms: 1.27x faster                                                        |
| Geometric mean | (ref)                                                               | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.1 ms: 2.44x faster                                                        |
| deltablue               | 7.30 ms                                                             | 3.53 ms: 2.07x faster                                                        |
| asyncio_tcp             | 922 ms                                                              | 508 ms: 1.82x faster                                                         |
| logging_silent          | 169 ns                                                              | 98.2 ns: 1.72x faster                                                        |
| richards                | 74.2 ms                                                             | 43.4 ms: 1.71x faster                                                        |
| nbody                   | 146 ms                                                              | 88.2 ms: 1.65x faster                                                        |
| go                      | 226 ms                                                              | 137 ms: 1.65x faster                                                         |
| scimark_sor             | 198 ms                                                              | 123 ms: 1.61x faster                                                         |
| hexiom                  | 9.50 ms                                                             | 6.08 ms: 1.56x faster                                                        |
| raytrace                | 470 ms                                                              | 301 ms: 1.56x faster                                                         |
| python_startup          | 14.1 ms                                                             | 9.08 ms: 1.56x faster                                                        |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.55x faster                                                        |
| chaos                   | 106 ms                                                              | 68.8 ms: 1.54x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 71.3 ms: 1.52x faster                                                        |
| pyflate                 | 671 ms                                                              | 444 ms: 1.51x faster                                                         |
| crypto_pyaes            | 117 ms                                                              | 78.6 ms: 1.48x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                             | 1.66 ms: 1.48x faster                                                        |
| scimark_lu              | 160 ms                                                              | 111 ms: 1.44x faster                                                         |
| pickle_pure_python      | 457 us                                                              | 317 us: 1.44x faster                                                         |
| coroutines              | 31.8 ms                                                             | 22.4 ms: 1.42x faster                                                        |
| async_tree_io           | 1.78 sec                                                            | 1.27 sec: 1.40x faster                                                       |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.39x faster                                                         |
| unpickle_pure_python    | 300 us                                                              | 217 us: 1.38x faster                                                         |
| mako                    | 14.7 ms                                                             | 10.9 ms: 1.36x faster                                                        |
| async_tree_none         | 713 ms                                                              | 526 ms: 1.36x faster                                                         |
| json_dumps              | 13.7 ms                                                             | 10.2 ms: 1.35x faster                                                        |
| pprint_pformat          | 1.98 sec                                                            | 1.47 sec: 1.34x faster                                                       |
| genshi_text             | 30.4 ms                                                             | 22.7 ms: 1.34x faster                                                        |
| float                   | 110 ms                                                              | 82.1 ms: 1.34x faster                                                        |
| html5lib                | 86.4 ms                                                             | 65.1 ms: 1.33x faster                                                        |
| deepcopy_memo           | 51.8 us                                                             | 39.1 us: 1.33x faster                                                        |
| pprint_safe_repr        | 953 ms                                                              | 721 ms: 1.32x faster                                                         |
| logging_simple          | 8.21 us                                                             | 6.24 us: 1.32x faster                                                        |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                       |
| logging_format          | 9.07 us                                                             | 6.91 us: 1.31x faster                                                        |
| fannkuch                | 485 ms                                                              | 376 ms: 1.29x faster                                                         |
| thrift                  | 1.04 ms                                                             | 803 us: 1.29x faster                                                         |
| async_tree_memoization  | 853 ms                                                              | 661 ms: 1.29x faster                                                         |
| xml_etree_process       | 74.8 ms                                                             | 58.7 ms: 1.27x faster                                                        |
| genshi_xml              | 64.3 ms                                                             | 50.8 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 944 ms                                                              | 749 ms: 1.26x faster                                                         |
| unpack_sequence         | 65.6 ns                                                             | 52.1 ns: 1.26x faster                                                        |
| 2to3                    | 336 ms                                                              | 268 ms: 1.25x faster                                                         |
| nqueens                 | 98.8 ms                                                             | 79.3 ms: 1.25x faster                                                        |
| regex_compile           | 177 ms                                                              | 143 ms: 1.24x faster                                                         |
| tornado_http            | 129 ms                                                              | 105 ms: 1.23x faster                                                         |
| mypy2                   | 432 ms                                                              | 352 ms: 1.23x faster                                                         |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                                         |
| deepcopy                | 438 us                                                              | 365 us: 1.20x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                             | 54.4 ms: 1.20x faster                                                        |
| deepcopy_reduce         | 3.80 us                                                             | 3.17 us: 1.20x faster                                                        |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.69 ms: 1.20x faster                                                        |
| scimark_fft             | 425 ms                                                              | 355 ms: 1.20x faster                                                         |
| comprehensions          | 27.3 us                                                             | 23.1 us: 1.18x faster                                                        |
| docutils                | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                       |
| bench_thread_pool       | 954 us                                                              | 835 us: 1.14x faster                                                         |
| json_loads              | 29.3 us                                                             | 25.8 us: 1.14x faster                                                        |
| dulwich_log             | 76.3 ms                                                             | 67.3 ms: 1.13x faster                                                        |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                         |
| xml_etree_generate      | 94.9 ms                                                             | 84.2 ms: 1.13x faster                                                        |
| regex_v8                | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                                        |
| json                    | 5.41 ms                                                             | 4.88 ms: 1.11x faster                                                        |
| sqlite_synth            | 2.97 us                                                             | 2.69 us: 1.11x faster                                                        |
| pathlib                 | 19.8 ms                                                             | 17.9 ms: 1.10x faster                                                        |
| create_gc_cycles        | 1.64 ms                                                             | 1.50 ms: 1.09x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.5 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                              | 105 ms: 1.06x faster                                                         |
| mdp                     | 2.75 sec                                                            | 2.60 sec: 1.06x faster                                                       |
| regex_dna               | 213 ms                                                              | 205 ms: 1.04x faster                                                         |
| xml_etree_parse         | 164 ms                                                              | 158 ms: 1.04x faster                                                         |
| meteor_contest          | 115 ms                                                              | 112 ms: 1.03x faster                                                         |
| unpickle_list           | 4.94 us                                                             | 4.91 us: 1.01x faster                                                        |
| pickle_list             | 4.73 us                                                             | 4.70 us: 1.01x faster                                                        |
| pidigits                | 190 ms                                                              | 189 ms: 1.01x faster                                                         |
| async_generators        | 420 ms                                                              | 439 ms: 1.05x slower                                                         |
| pickle                  | 10.2 us                                                             | 10.8 us: 1.05x slower                                                        |
| regex_effbot            | 3.22 ms                                                             | 3.41 ms: 1.06x slower                                                        |
| telco                   | 6.67 ms                                                             | 7.06 ms: 1.06x slower                                                        |
| gc_traversal            | 3.53 ms                                                             | 3.94 ms: 1.12x slower                                                        |
| python_startup_no_site  | 5.80 ms                                                             | 6.66 ms: 1.15x slower                                                        |
| pickle_dict             | 27.8 us                                                             | 32.6 us: 1.17x slower                                                        |
| dask                    | 437 ms                                                              | 540 ms: 1.24x slower                                                         |
| coverage                | 70.6 ms                                                             | 100 ms: 1.42x slower                                                         |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
