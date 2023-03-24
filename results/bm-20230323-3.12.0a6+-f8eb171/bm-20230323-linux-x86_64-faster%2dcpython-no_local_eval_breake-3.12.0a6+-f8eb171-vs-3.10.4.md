
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 254 ms: 1.32x faster                                                             |
| chameleon      | 9.13 ms                                                             | 6.44 ms: 1.42x faster                                                            |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                           |
| html5lib       | 86.4 ms                                                             | 62.5 ms: 1.38x faster                                                            |
| tornado_http   | 129 ms                                                              | 91.1 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                               | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.6 ms: 1.66x faster                                                            |
| float          | 110 ms                                                              | 75.2 ms: 1.46x faster                                                            |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.31x faster                                                             |
| regex_v8       | 24.9 ms                                                             | 21.9 ms: 1.14x faster                                                            |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                             |
| regex_effbot   | 3.22 ms                                                             | 3.50 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                               | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 288 us: 1.58x faster                                                             |
| unpickle_pure_python | 300 us                                                              | 203 us: 1.48x faster                                                             |
| json_dumps           | 13.7 ms                                                             | 9.61 ms: 1.43x faster                                                            |
| xml_etree_process    | 74.8 ms                                                             | 56.5 ms: 1.32x faster                                                            |
| json_loads           | 29.3 us                                                             | 24.1 us: 1.22x faster                                                            |
| xml_etree_generate   | 94.9 ms                                                             | 81.8 ms: 1.16x faster                                                            |
| pickle_list          | 4.73 us                                                             | 4.21 us: 1.12x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                              | 100 ms: 1.11x faster                                                             |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                             |
| unpickle             | 15.0 us                                                             | 13.6 us: 1.10x faster                                                            |
| pickle               | 10.2 us                                                             | 10.3 us: 1.01x slower                                                            |
| unpickle_list        | 4.94 us                                                             | 5.00 us: 1.01x slower                                                            |
| pickle_dict          | 27.8 us                                                             | 31.1 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                                            |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                                            |
| genshi_text     | 30.4 ms                                                             | 21.6 ms: 1.41x faster                                                            |
| django_template | 45.8 ms                                                             | 33.6 ms: 1.36x faster                                                            |
| genshi_xml      | 64.3 ms                                                             | 48.2 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                               | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.3 ms: 2.58x faster                                                            |
| deltablue               | 7.30 ms                                                             | 3.26 ms: 2.24x faster                                                            |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                             |
| scimark_sor             | 198 ms                                                              | 112 ms: 1.76x faster                                                             |
| logging_silent          | 169 ns                                                              | 98.2 ns: 1.72x faster                                                            |
| nbody                   | 146 ms                                                              | 87.6 ms: 1.66x faster                                                            |
| richards                | 74.2 ms                                                             | 44.7 ms: 1.66x faster                                                            |
| go                      | 226 ms                                                              | 137 ms: 1.65x faster                                                             |
| raytrace                | 470 ms                                                              | 285 ms: 1.65x faster                                                             |
| spectral_norm           | 150 ms                                                              | 92.1 ms: 1.63x faster                                                            |
| scimark_monte_carlo     | 109 ms                                                              | 67.1 ms: 1.62x faster                                                            |
| chaos                   | 106 ms                                                              | 66.1 ms: 1.60x faster                                                            |
| python_startup          | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                                            |
| pyflate                 | 671 ms                                                              | 423 ms: 1.59x faster                                                             |
| pickle_pure_python      | 457 us                                                              | 288 us: 1.58x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 74.8 ms: 1.56x faster                                                            |
| hexiom                  | 9.50 ms                                                             | 6.14 ms: 1.55x faster                                                            |
| deepcopy_memo           | 51.8 us                                                             | 34.8 us: 1.49x faster                                                            |
| mako                    | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                                            |
| unpickle_pure_python    | 300 us                                                              | 203 us: 1.48x faster                                                             |
| float                   | 110 ms                                                              | 75.2 ms: 1.46x faster                                                            |
| scimark_lu              | 160 ms                                                              | 110 ms: 1.45x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.43 ms: 1.45x faster                                                            |
| logging_format          | 9.07 us                                                             | 6.30 us: 1.44x faster                                                            |
| logging_simple          | 8.21 us                                                             | 5.71 us: 1.44x faster                                                            |
| json_dumps              | 13.7 ms                                                             | 9.61 ms: 1.43x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                             | 1.72 ms: 1.42x faster                                                            |
| chameleon               | 9.13 ms                                                             | 6.44 ms: 1.42x faster                                                            |
| tornado_http            | 129 ms                                                              | 91.1 ms: 1.42x faster                                                            |
| unpack_sequence         | 65.6 ns                                                             | 46.5 ns: 1.41x faster                                                            |
| pprint_pformat          | 1.98 sec                                                            | 1.40 sec: 1.41x faster                                                           |
| genshi_text             | 30.4 ms                                                             | 21.6 ms: 1.41x faster                                                            |
| pprint_safe_repr        | 953 ms                                                              | 683 ms: 1.40x faster                                                             |
| scimark_fft             | 425 ms                                                              | 307 ms: 1.39x faster                                                             |
| html5lib                | 86.4 ms                                                             | 62.5 ms: 1.38x faster                                                            |
| coroutines              | 31.8 ms                                                             | 23.1 ms: 1.38x faster                                                            |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                           |
| pycparser               | 1.53 sec                                                            | 1.12 sec: 1.37x faster                                                           |
| django_template         | 45.8 ms                                                             | 33.6 ms: 1.36x faster                                                            |
| async_tree_none         | 713 ms                                                              | 523 ms: 1.36x faster                                                             |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                            |
| genshi_xml              | 64.3 ms                                                             | 48.2 ms: 1.33x faster                                                            |
| xml_etree_process       | 74.8 ms                                                             | 56.5 ms: 1.32x faster                                                            |
| 2to3                    | 336 ms                                                              | 254 ms: 1.32x faster                                                             |
| thrift                  | 1.04 ms                                                             | 786 us: 1.32x faster                                                             |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.32x faster                                                            |
| deepcopy                | 438 us                                                              | 333 us: 1.32x faster                                                             |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.28 ms: 1.31x faster                                                            |
| regex_compile           | 177 ms                                                              | 135 ms: 1.31x faster                                                             |
| fannkuch                | 485 ms                                                              | 370 ms: 1.31x faster                                                             |
| async_tree_memoization  | 853 ms                                                              | 656 ms: 1.30x faster                                                             |
| mypy2                   | 432 ms                                                              | 334 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 743 ms: 1.27x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                             | 51.5 ms: 1.27x faster                                                            |
| sqlglot_normalize       | 135 ms                                                              | 106 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.80 us                                                             | 3.02 us: 1.26x faster                                                            |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                           |
| nqueens                 | 98.8 ms                                                             | 80.6 ms: 1.23x faster                                                            |
| json_loads              | 29.3 us                                                             | 24.1 us: 1.22x faster                                                            |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.21x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 791 us: 1.21x faster                                                             |
| dulwich_log             | 76.3 ms                                                             | 63.3 ms: 1.21x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.8 ms: 1.19x faster                                                            |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.18x faster                                                            |
| sympy_expand            | 540 ms                                                              | 460 ms: 1.17x faster                                                             |
| json                    | 5.41 ms                                                             | 4.63 ms: 1.17x faster                                                            |
| xml_etree_generate      | 94.9 ms                                                             | 81.8 ms: 1.16x faster                                                            |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                            |
| sympy_str               | 328 ms                                                              | 285 ms: 1.15x faster                                                             |
| regex_v8                | 24.9 ms                                                             | 21.9 ms: 1.14x faster                                                            |
| sqlite_synth            | 2.97 us                                                             | 2.61 us: 1.14x faster                                                            |
| djangocms               | 36.3 us                                                             | 32.2 us: 1.13x faster                                                            |
| pickle_list             | 4.73 us                                                             | 4.21 us: 1.12x faster                                                            |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.12x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                              | 100 ms: 1.11x faster                                                             |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.11x faster                                                             |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                            |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                             |
| unpickle                | 15.0 us                                                             | 13.6 us: 1.10x faster                                                            |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.09x faster                                                            |
| mdp                     | 2.75 sec                                                            | 2.52 sec: 1.09x faster                                                           |
| telco                   | 6.67 ms                                                             | 6.39 ms: 1.04x faster                                                            |
| async_generators        | 420 ms                                                              | 407 ms: 1.03x faster                                                             |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                             |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                             |
| pickle                  | 10.2 us                                                             | 10.3 us: 1.01x slower                                                            |
| unpickle_list           | 4.94 us                                                             | 5.00 us: 1.01x slower                                                            |
| gc_traversal            | 3.53 ms                                                             | 3.82 ms: 1.08x slower                                                            |
| regex_effbot            | 3.22 ms                                                             | 3.50 ms: 1.09x slower                                                            |
| pickle_dict             | 27.8 us                                                             | 31.1 us: 1.12x slower                                                            |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                            |
| dask                    | 437 ms                                                              | 512 ms: 1.17x slower                                                             |
| coverage                | 70.6 ms                                                             | 97.5 ms: 1.38x slower                                                            |
| Geometric mean          | (ref)                                                               | 1.29x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
