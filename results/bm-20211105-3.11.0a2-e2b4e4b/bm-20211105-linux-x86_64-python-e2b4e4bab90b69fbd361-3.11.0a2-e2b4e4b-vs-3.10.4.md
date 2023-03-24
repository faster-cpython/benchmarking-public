
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.16x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 274 ms: 1.23x faster                                                  |
| chameleon      | 9.13 ms                                                             | 7.46 ms: 1.22x faster                                                 |
| docutils       | 3.19 sec                                                            | 2.79 sec: 1.14x faster                                                |
| html5lib       | 86.4 ms                                                             | 71.5 ms: 1.21x faster                                                 |
| tornado_http   | 129 ms                                                              | 111 ms: 1.17x faster                                                  |
| Geometric mean | (ref)                                                               | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 110 ms                                                              | 83.3 ms: 1.32x faster                                                 |
| nbody          | 146 ms                                                              | 112 ms: 1.30x faster                                                  |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                               | 1.20x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.23x faster                                                  |
| regex_v8       | 24.9 ms                                                             | 23.7 ms: 1.05x faster                                                 |
| regex_effbot   | 3.22 ms                                                             | 3.26 ms: 1.01x slower                                                 |
| regex_dna      | 213 ms                                                              | 219 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 74.8 ms                                                             | 59.6 ms: 1.26x faster                                                 |
| pickle_pure_python   | 457 us                                                              | 364 us: 1.26x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 81.6 ms: 1.16x faster                                                 |
| json_loads           | 29.3 us                                                             | 25.9 us: 1.13x faster                                                 |
| json_dumps           | 13.7 ms                                                             | 12.4 ms: 1.11x faster                                                 |
| unpickle_pure_python | 300 us                                                              | 271 us: 1.11x faster                                                  |
| unpickle             | 15.0 us                                                             | 13.7 us: 1.09x faster                                                 |
| xml_etree_parse      | 164 ms                                                              | 158 ms: 1.04x faster                                                  |
| pickle               | 10.2 us                                                             | 10.1 us: 1.02x faster                                                 |
| pickle_list          | 4.73 us                                                             | 4.68 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                              | 110 ms: 1.01x faster                                                  |
| pickle_dict          | 27.8 us                                                             | 28.6 us: 1.03x slower                                                 |
| unpickle_list        | 4.94 us                                                             | 5.13 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 5.80 ms                                                             | 5.77 ms: 1.01x faster                                                 |
| python_startup         | 14.1 ms                                                             | 14.6 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 30.4 ms                                                             | 24.6 ms: 1.23x faster                                                 |
| mako            | 14.7 ms                                                             | 12.1 ms: 1.22x faster                                                 |
| django_template | 45.8 ms                                                             | 37.9 ms: 1.21x faster                                                 |
| genshi_xml      | 64.3 ms                                                             | 56.1 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                               | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpack_sequence         | 65.6 ns                                                             | 43.6 ns: 1.51x faster                                                 |
| deltablue               | 7.30 ms                                                             | 4.86 ms: 1.50x faster                                                 |
| logging_silent          | 169 ns                                                              | 117 ns: 1.45x faster                                                  |
| raytrace                | 470 ms                                                              | 326 ms: 1.44x faster                                                  |
| spectral_norm           | 150 ms                                                              | 106 ms: 1.42x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 78.4 ms: 1.38x faster                                                 |
| async_tree_none         | 713 ms                                                              | 518 ms: 1.38x faster                                                  |
| chaos                   | 106 ms                                                              | 77.1 ms: 1.37x faster                                                 |
| logging_format          | 9.07 us                                                             | 6.71 us: 1.35x faster                                                 |
| logging_simple          | 8.21 us                                                             | 6.07 us: 1.35x faster                                                 |
| go                      | 226 ms                                                              | 167 ms: 1.35x faster                                                  |
| richards                | 74.2 ms                                                             | 55.7 ms: 1.33x faster                                                 |
| float                   | 110 ms                                                              | 83.3 ms: 1.32x faster                                                 |
| generators              | 75.7 ms                                                             | 57.4 ms: 1.32x faster                                                 |
| nbody                   | 146 ms                                                              | 112 ms: 1.30x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 90.2 ms: 1.29x faster                                                 |
| deepcopy_memo           | 51.8 us                                                             | 40.4 us: 1.28x faster                                                 |
| hexiom                  | 9.50 ms                                                             | 7.42 ms: 1.28x faster                                                 |
| scimark_sor             | 198 ms                                                              | 156 ms: 1.27x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.41 sec: 1.27x faster                                                |
| thrift                  | 1.04 ms                                                             | 821 us: 1.26x faster                                                  |
| async_tree_memoization  | 853 ms                                                              | 676 ms: 1.26x faster                                                  |
| xml_etree_process       | 74.8 ms                                                             | 59.6 ms: 1.26x faster                                                 |
| pickle_pure_python      | 457 us                                                              | 364 us: 1.26x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.58 sec: 1.25x faster                                                |
| pprint_safe_repr        | 953 ms                                                              | 763 ms: 1.25x faster                                                  |
| gunicorn                | 1.43 ms                                                             | 1.15 ms: 1.24x faster                                                 |
| pyflate                 | 671 ms                                                              | 541 ms: 1.24x faster                                                  |
| genshi_text             | 30.4 ms                                                             | 24.6 ms: 1.23x faster                                                 |
| 2to3                    | 336 ms                                                              | 274 ms: 1.23x faster                                                  |
| regex_compile           | 177 ms                                                              | 145 ms: 1.23x faster                                                  |
| chameleon               | 9.13 ms                                                             | 7.46 ms: 1.22x faster                                                 |
| pycparser               | 1.53 sec                                                            | 1.26 sec: 1.22x faster                                                |
| mako                    | 14.7 ms                                                             | 12.1 ms: 1.22x faster                                                 |
| django_template         | 45.8 ms                                                             | 37.9 ms: 1.21x faster                                                 |
| html5lib                | 86.4 ms                                                             | 71.5 ms: 1.21x faster                                                 |
| scimark_fft             | 425 ms                                                              | 355 ms: 1.20x faster                                                  |
| scimark_lu              | 160 ms                                                              | 136 ms: 1.17x faster                                                  |
| tornado_http            | 129 ms                                                              | 111 ms: 1.17x faster                                                  |
| async_generators        | 420 ms                                                              | 361 ms: 1.17x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 81.6 ms: 1.16x faster                                                 |
| deepcopy_reduce         | 3.80 us                                                             | 3.27 us: 1.16x faster                                                 |
| async_tree_cpu_io_mixed | 944 ms                                                              | 818 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.86 ms: 1.15x faster                                                 |
| genshi_xml              | 64.3 ms                                                             | 56.1 ms: 1.15x faster                                                 |
| deepcopy                | 438 us                                                              | 382 us: 1.15x faster                                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 145 ms: 1.14x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.79 sec: 1.14x faster                                                |
| flaskblogging           | 8.48 ms                                                             | 7.46 ms: 1.14x faster                                                 |
| fannkuch                | 485 ms                                                              | 427 ms: 1.14x faster                                                  |
| json_loads              | 29.3 us                                                             | 25.9 us: 1.13x faster                                                 |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.8 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 135 ms                                                              | 119 ms: 1.13x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 58.4 ms: 1.12x faster                                                 |
| dulwich_log             | 76.3 ms                                                             | 68.3 ms: 1.12x faster                                                 |
| pylint                  | 521 ms                                                              | 469 ms: 1.11x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 12.4 ms: 1.11x faster                                                 |
| coroutines              | 31.8 ms                                                             | 28.8 ms: 1.11x faster                                                 |
| unpickle_pure_python    | 300 us                                                              | 271 us: 1.11x faster                                                  |
| json                    | 5.41 ms                                                             | 4.91 ms: 1.10x faster                                                 |
| sympy_integrate         | 24.3 ms                                                             | 22.2 ms: 1.09x faster                                                 |
| unpickle                | 15.0 us                                                             | 13.7 us: 1.09x faster                                                 |
| sympy_sum               | 185 ms                                                              | 170 ms: 1.09x faster                                                  |
| nqueens                 | 98.8 ms                                                             | 91.4 ms: 1.08x faster                                                 |
| sqlite_synth            | 2.97 us                                                             | 2.76 us: 1.08x faster                                                 |
| meteor_contest          | 115 ms                                                              | 106 ms: 1.08x faster                                                  |
| sympy_str               | 328 ms                                                              | 306 ms: 1.07x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 892 us: 1.07x faster                                                  |
| sympy_expand            | 540 ms                                                              | 505 ms: 1.07x faster                                                  |
| regex_v8                | 24.9 ms                                                             | 23.7 ms: 1.05x faster                                                 |
| xml_etree_parse         | 164 ms                                                              | 158 ms: 1.04x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 2.37 ms: 1.04x faster                                                 |
| pathlib                 | 19.8 ms                                                             | 19.1 ms: 1.04x faster                                                 |
| telco                   | 6.67 ms                                                             | 6.50 ms: 1.03x faster                                                 |
| pickle                  | 10.2 us                                                             | 10.1 us: 1.02x faster                                                 |
| mdp                     | 2.75 sec                                                            | 2.71 sec: 1.02x faster                                                |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                  |
| pickle_list             | 4.73 us                                                             | 4.68 us: 1.01x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                              | 110 ms: 1.01x faster                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 5.77 ms: 1.01x faster                                                 |
| regex_effbot            | 3.22 ms                                                             | 3.26 ms: 1.01x slower                                                 |
| regex_dna               | 213 ms                                                              | 219 ms: 1.03x slower                                                  |
| python_startup          | 14.1 ms                                                             | 14.6 ms: 1.03x slower                                                 |
| pickle_dict             | 27.8 us                                                             | 28.6 us: 1.03x slower                                                 |
| unpickle_list           | 4.94 us                                                             | 5.13 us: 1.04x slower                                                 |
| coverage                | 70.6 ms                                                             | 75.8 ms: 1.07x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.16x faster                                                          |

Benchmark hidden because not significant (2): sqlglot_parse, bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
