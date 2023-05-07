
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: immortalize_empty_ke
- machine: linux-x86_64
- commit hash: e472d94
- commit date: 2023-05-06
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 270 ms: 1.24x faster                                                              |
| docutils       | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                            |
| tornado_http   | 129 ms                                                              | 103 ms: 1.25x faster                                                              |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 93.1 ms: 1.57x faster                                                             |
| float          | 110 ms                                                              | 82.0 ms: 1.34x faster                                                             |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                               | 1.26x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.21x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.8 ms: 1.10x faster                                                             |
| regex_dna      | 213 ms                                                              | 211 ms: 1.01x faster                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.74 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                               | 1.04x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 318 us: 1.44x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 218 us: 1.38x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 9.99 ms: 1.37x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 59.9 ms: 1.25x faster                                                             |
| json_loads           | 29.3 us                                                             | 25.5 us: 1.15x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 85.9 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                              |
| xml_etree_parse      | 164 ms                                                              | 156 ms: 1.05x faster                                                              |
| pickle_list          | 4.73 us                                                             | 4.58 us: 1.03x faster                                                             |
| unpickle             | 15.0 us                                                             | 15.7 us: 1.05x slower                                                             |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 31.4 us: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.19 ms: 1.54x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.70 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.15x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.6 ms: 1.39x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.1 ms: 2.43x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.58 ms: 2.04x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 513 ms: 1.80x faster                                                              |
| richards                | 74.2 ms                                                             | 44.3 ms: 1.67x faster                                                             |
| go                      | 226 ms                                                              | 137 ms: 1.64x faster                                                              |
| scimark_sor             | 198 ms                                                              | 123 ms: 1.61x faster                                                              |
| logging_silent          | 169 ns                                                              | 106 ns: 1.59x faster                                                              |
| nbody                   | 146 ms                                                              | 93.1 ms: 1.57x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.55x faster                                                             |
| chaos                   | 106 ms                                                              | 68.6 ms: 1.54x faster                                                             |
| python_startup          | 14.1 ms                                                             | 9.19 ms: 1.54x faster                                                             |
| hexiom                  | 9.50 ms                                                             | 6.21 ms: 1.53x faster                                                             |
| raytrace                | 470 ms                                                              | 310 ms: 1.52x faster                                                              |
| pyflate                 | 671 ms                                                              | 443 ms: 1.51x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                              | 73.0 ms: 1.49x faster                                                             |
| spectral_norm           | 150 ms                                                              | 101 ms: 1.48x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                             | 1.66 ms: 1.48x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 79.6 ms: 1.47x faster                                                             |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                                            |
| pickle_pure_python      | 457 us                                                              | 318 us: 1.44x faster                                                              |
| coroutines              | 31.8 ms                                                             | 22.4 ms: 1.42x faster                                                             |
| async_tree_none         | 713 ms                                                              | 504 ms: 1.41x faster                                                              |
| scimark_lu              | 160 ms                                                              | 115 ms: 1.39x faster                                                              |
| mako                    | 14.7 ms                                                             | 10.6 ms: 1.39x faster                                                             |
| async_tree_memoization  | 853 ms                                                              | 615 ms: 1.39x faster                                                              |
| unpickle_pure_python    | 300 us                                                              | 218 us: 1.38x faster                                                              |
| deepcopy_memo           | 51.8 us                                                             | 37.8 us: 1.37x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 9.99 ms: 1.37x faster                                                             |
| unpack_sequence         | 65.6 ns                                                             | 47.9 ns: 1.37x faster                                                             |
| float                   | 110 ms                                                              | 82.0 ms: 1.34x faster                                                             |
| fannkuch                | 485 ms                                                              | 372 ms: 1.30x faster                                                              |
| async_tree_cpu_io_mixed | 944 ms                                                              | 725 ms: 1.30x faster                                                              |
| pprint_pformat          | 1.98 sec                                                            | 1.53 sec: 1.29x faster                                                            |
| pprint_safe_repr        | 953 ms                                                              | 744 ms: 1.28x faster                                                              |
| pycparser               | 1.53 sec                                                            | 1.21 sec: 1.26x faster                                                            |
| tornado_http            | 129 ms                                                              | 103 ms: 1.25x faster                                                              |
| xml_etree_process       | 74.8 ms                                                             | 59.9 ms: 1.25x faster                                                             |
| 2to3                    | 336 ms                                                              | 270 ms: 1.24x faster                                                              |
| logging_simple          | 8.21 us                                                             | 6.61 us: 1.24x faster                                                             |
| logging_format          | 9.07 us                                                             | 7.31 us: 1.24x faster                                                             |
| nqueens                 | 98.8 ms                                                             | 80.1 ms: 1.23x faster                                                             |
| mypy2                   | 432 ms                                                              | 354 ms: 1.22x faster                                                              |
| deepcopy                | 438 us                                                              | 361 us: 1.21x faster                                                              |
| regex_compile           | 177 ms                                                              | 146 ms: 1.21x faster                                                              |
| scimark_fft             | 425 ms                                                              | 355 ms: 1.20x faster                                                              |
| deepcopy_reduce         | 3.80 us                                                             | 3.17 us: 1.20x faster                                                             |
| sqlglot_normalize       | 135 ms                                                              | 112 ms: 1.20x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 55.1 ms: 1.19x faster                                                             |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.74 ms: 1.18x faster                                                             |
| comprehensions          | 27.3 us                                                             | 23.2 us: 1.17x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                            |
| json_loads              | 29.3 us                                                             | 25.5 us: 1.15x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 834 us: 1.14x faster                                                              |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                              |
| json                    | 5.41 ms                                                             | 4.81 ms: 1.13x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.9 ms: 1.12x faster                                                             |
| dulwich_log             | 76.3 ms                                                             | 68.4 ms: 1.12x faster                                                             |
| xml_etree_generate      | 94.9 ms                                                             | 85.9 ms: 1.10x faster                                                             |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                             |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.10x faster                                                              |
| regex_v8                | 24.9 ms                                                             | 22.8 ms: 1.10x faster                                                             |
| mdp                     | 2.75 sec                                                            | 2.56 sec: 1.07x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                              |
| sqlite_synth            | 2.97 us                                                             | 2.78 us: 1.07x faster                                                             |
| xml_etree_parse         | 164 ms                                                              | 156 ms: 1.05x faster                                                              |
| pickle_list             | 4.73 us                                                             | 4.58 us: 1.03x faster                                                             |
| pathlib                 | 19.8 ms                                                             | 19.3 ms: 1.03x faster                                                             |
| regex_dna               | 213 ms                                                              | 211 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                              |
| unpickle                | 15.0 us                                                             | 15.7 us: 1.05x slower                                                             |
| telco                   | 6.67 ms                                                             | 7.00 ms: 1.05x slower                                                             |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                             |
| async_generators        | 420 ms                                                              | 449 ms: 1.07x slower                                                              |
| gc_traversal            | 3.53 ms                                                             | 3.97 ms: 1.13x slower                                                             |
| pickle_dict             | 27.8 us                                                             | 31.4 us: 1.13x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.70 ms: 1.16x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.74 ms: 1.16x slower                                                             |
| dask                    | 437 ms                                                              | 538 ms: 1.23x slower                                                              |
| coverage                | 70.6 ms                                                             | 102 ms: 1.44x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
