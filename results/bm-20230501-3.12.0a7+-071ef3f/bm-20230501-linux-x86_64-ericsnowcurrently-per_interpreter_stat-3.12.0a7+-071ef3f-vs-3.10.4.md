
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_stat
- machine: linux-x86_64
- commit hash: 071ef3f
- commit date: 2023-05-01
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 271 ms: 1.24x faster                                                              |
| docutils       | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                            |
| html5lib       | 86.4 ms                                                             | 64.9 ms: 1.33x faster                                                             |
| tornado_http   | 129 ms                                                              | 102 ms: 1.26x faster                                                              |
| Geometric mean | (ref)                                                               | 1.25x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.4 ms: 1.67x faster                                                             |
| float          | 110 ms                                                              | 81.2 ms: 1.35x faster                                                             |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                               | 1.31x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 144 ms: 1.23x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                                             |
| regex_dna      | 213 ms                                                              | 209 ms: 1.02x faster                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.40 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 316 us: 1.45x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 218 us: 1.37x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 10.1 ms: 1.36x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 60.4 ms: 1.24x faster                                                             |
| json_loads           | 29.3 us                                                             | 25.9 us: 1.13x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 85.8 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                              |
| xml_etree_parse      | 164 ms                                                              | 153 ms: 1.07x faster                                                              |
| unpickle             | 15.0 us                                                             | 14.4 us: 1.04x faster                                                             |
| pickle_list          | 4.73 us                                                             | 4.60 us: 1.03x faster                                                             |
| pickle               | 10.2 us                                                             | 10.8 us: 1.06x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 32.4 us: 1.17x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.15 ms: 1.55x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.71 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 14.7 ms                                                             | 10.7 ms: 1.38x faster                                                             |
| genshi_text    | 30.4 ms                                                             | 22.3 ms: 1.37x faster                                                             |
| genshi_xml     | 64.3 ms                                                             | 50.8 ms: 1.27x faster                                                             |
| Geometric mean | (ref)                                                               | 1.34x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 30.7 ms: 2.47x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.47 ms: 2.10x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 513 ms: 1.80x faster                                                              |
| richards                | 74.2 ms                                                             | 43.2 ms: 1.72x faster                                                             |
| logging_silent          | 169 ns                                                              | 99.0 ns: 1.71x faster                                                             |
| nbody                   | 146 ms                                                              | 87.4 ms: 1.67x faster                                                             |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                                              |
| scimark_sor             | 198 ms                                                              | 121 ms: 1.63x faster                                                              |
| raytrace                | 470 ms                                                              | 302 ms: 1.56x faster                                                              |
| hexiom                  | 9.50 ms                                                             | 6.12 ms: 1.55x faster                                                             |
| python_startup          | 14.1 ms                                                             | 9.15 ms: 1.55x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.54x faster                                                             |
| chaos                   | 106 ms                                                              | 69.3 ms: 1.53x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                              | 72.5 ms: 1.50x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 77.9 ms: 1.50x faster                                                             |
| pyflate                 | 671 ms                                                              | 449 ms: 1.49x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                             | 1.67 ms: 1.47x faster                                                             |
| spectral_norm           | 150 ms                                                              | 104 ms: 1.45x faster                                                              |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                                            |
| pickle_pure_python      | 457 us                                                              | 316 us: 1.45x faster                                                              |
| scimark_lu              | 160 ms                                                              | 112 ms: 1.43x faster                                                              |
| async_tree_none         | 713 ms                                                              | 499 ms: 1.43x faster                                                              |
| coroutines              | 31.8 ms                                                             | 22.4 ms: 1.42x faster                                                             |
| async_tree_memoization  | 853 ms                                                              | 612 ms: 1.39x faster                                                              |
| mako                    | 14.7 ms                                                             | 10.7 ms: 1.38x faster                                                             |
| unpickle_pure_python    | 300 us                                                              | 218 us: 1.37x faster                                                              |
| genshi_text             | 30.4 ms                                                             | 22.3 ms: 1.37x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 10.1 ms: 1.36x faster                                                             |
| deepcopy_memo           | 51.8 us                                                             | 38.3 us: 1.35x faster                                                             |
| float                   | 110 ms                                                              | 81.2 ms: 1.35x faster                                                             |
| html5lib                | 86.4 ms                                                             | 64.9 ms: 1.33x faster                                                             |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                            |
| logging_simple          | 8.21 us                                                             | 6.25 us: 1.31x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 720 ms: 1.31x faster                                                              |
| pprint_pformat          | 1.98 sec                                                            | 1.51 sec: 1.31x faster                                                            |
| thrift                  | 1.04 ms                                                             | 797 us: 1.30x faster                                                              |
| logging_format          | 9.07 us                                                             | 6.98 us: 1.30x faster                                                             |
| unpack_sequence         | 65.6 ns                                                             | 50.6 ns: 1.30x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 738 ms: 1.29x faster                                                              |
| fannkuch                | 485 ms                                                              | 381 ms: 1.27x faster                                                              |
| genshi_xml              | 64.3 ms                                                             | 50.8 ms: 1.27x faster                                                             |
| tornado_http            | 129 ms                                                              | 102 ms: 1.26x faster                                                              |
| 2to3                    | 336 ms                                                              | 271 ms: 1.24x faster                                                              |
| xml_etree_process       | 74.8 ms                                                             | 60.4 ms: 1.24x faster                                                             |
| nqueens                 | 98.8 ms                                                             | 80.0 ms: 1.24x faster                                                             |
| regex_compile           | 177 ms                                                              | 144 ms: 1.23x faster                                                              |
| mypy2                   | 432 ms                                                              | 352 ms: 1.23x faster                                                              |
| scimark_fft             | 425 ms                                                              | 355 ms: 1.20x faster                                                              |
| deepcopy                | 438 us                                                              | 367 us: 1.19x faster                                                              |
| sqlglot_normalize       | 135 ms                                                              | 113 ms: 1.19x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 55.7 ms: 1.17x faster                                                             |
| deepcopy_reduce         | 3.80 us                                                             | 3.24 us: 1.17x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                            |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                             |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.86 ms: 1.16x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 834 us: 1.14x faster                                                              |
| json_loads              | 29.3 us                                                             | 25.9 us: 1.13x faster                                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                              |
| dulwich_log             | 76.3 ms                                                             | 68.3 ms: 1.12x faster                                                             |
| regex_v8                | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.67 us: 1.11x faster                                                             |
| pathlib                 | 19.8 ms                                                             | 17.9 ms: 1.11x faster                                                             |
| xml_etree_generate      | 94.9 ms                                                             | 85.8 ms: 1.10x faster                                                             |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.3 ms: 1.10x faster                                                             |
| json                    | 5.41 ms                                                             | 4.93 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                              |
| xml_etree_parse         | 164 ms                                                              | 153 ms: 1.07x faster                                                              |
| mdp                     | 2.75 sec                                                            | 2.60 sec: 1.06x faster                                                            |
| unpickle                | 15.0 us                                                             | 14.4 us: 1.04x faster                                                             |
| pickle_list             | 4.73 us                                                             | 4.60 us: 1.03x faster                                                             |
| regex_dna               | 213 ms                                                              | 209 ms: 1.02x faster                                                              |
| meteor_contest          | 115 ms                                                              | 113 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                                              |
| telco                   | 6.67 ms                                                             | 6.88 ms: 1.03x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.40 ms: 1.06x slower                                                             |
| pickle                  | 10.2 us                                                             | 10.8 us: 1.06x slower                                                             |
| async_generators        | 420 ms                                                              | 451 ms: 1.07x slower                                                              |
| python_startup_no_site  | 5.80 ms                                                             | 6.71 ms: 1.16x slower                                                             |
| pickle_dict             | 27.8 us                                                             | 32.4 us: 1.17x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 4.19 ms: 1.19x slower                                                             |
| dask                    | 437 ms                                                              | 540 ms: 1.24x slower                                                              |
| coverage                | 70.6 ms                                                             | 103 ms: 1.46x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.25x faster                                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
