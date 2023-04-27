
# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: call_function_ex_inl
- machine: linux-x86_64
- commit hash: dfd6b01
- commit date: 2023-04-27
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 269 ms: 1.25x faster                                                             |
| chameleon      | 9.13 ms                                                             | 6.96 ms: 1.31x faster                                                            |
| docutils       | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                           |
| html5lib       | 86.4 ms                                                             | 64.7 ms: 1.33x faster                                                            |
| tornado_http   | 129 ms                                                              | 105 ms: 1.23x faster                                                             |
| Geometric mean | (ref)                                                               | 1.26x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 89.2 ms: 1.63x faster                                                            |
| float          | 110 ms                                                              | 82.2 ms: 1.34x faster                                                            |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                               | 1.28x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.23x faster                                                             |
| regex_v8       | 24.9 ms                                                             | 22.8 ms: 1.10x faster                                                            |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                             |
| regex_effbot   | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                               | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 319 us: 1.43x faster                                                             |
| unpickle_pure_python | 300 us                                                              | 219 us: 1.37x faster                                                             |
| json_dumps           | 13.7 ms                                                             | 10.1 ms: 1.36x faster                                                            |
| xml_etree_process    | 74.8 ms                                                             | 58.7 ms: 1.27x faster                                                            |
| json_loads           | 29.3 us                                                             | 25.9 us: 1.13x faster                                                            |
| xml_etree_generate   | 94.9 ms                                                             | 84.6 ms: 1.12x faster                                                            |
| xml_etree_parse      | 164 ms                                                              | 152 ms: 1.08x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                             |
| pickle_list          | 4.73 us                                                             | 4.61 us: 1.03x faster                                                            |
| unpickle             | 15.0 us                                                             | 14.8 us: 1.01x faster                                                            |
| unpickle_list        | 4.94 us                                                             | 5.00 us: 1.01x slower                                                            |
| pickle               | 10.2 us                                                             | 10.5 us: 1.02x slower                                                            |
| pickle_dict          | 27.8 us                                                             | 31.6 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.11 ms: 1.55x faster                                                            |
| python_startup_no_site | 5.80 ms                                                             | 6.68 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 30.4 ms                                                             | 22.4 ms: 1.36x faster                                                            |
| mako            | 14.7 ms                                                             | 11.0 ms: 1.34x faster                                                            |
| django_template | 45.8 ms                                                             | 34.4 ms: 1.33x faster                                                            |
| genshi_xml      | 64.3 ms                                                             | 49.9 ms: 1.29x faster                                                            |
| Geometric mean  | (ref)                                                               | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 32.4 ms: 2.33x faster                                                            |
| deltablue               | 7.30 ms                                                             | 3.54 ms: 2.06x faster                                                            |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                             |
| richards                | 74.2 ms                                                             | 43.1 ms: 1.72x faster                                                            |
| logging_silent          | 169 ns                                                              | 99.1 ns: 1.70x faster                                                            |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                                             |
| nbody                   | 146 ms                                                              | 89.2 ms: 1.63x faster                                                            |
| scimark_sor             | 198 ms                                                              | 125 ms: 1.58x faster                                                             |
| python_startup          | 14.1 ms                                                             | 9.11 ms: 1.55x faster                                                            |
| raytrace                | 470 ms                                                              | 304 ms: 1.55x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.55x faster                                                            |
| chaos                   | 106 ms                                                              | 70.3 ms: 1.51x faster                                                            |
| hexiom                  | 9.50 ms                                                             | 6.34 ms: 1.50x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                             | 1.66 ms: 1.48x faster                                                            |
| pyflate                 | 671 ms                                                              | 453 ms: 1.48x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                              | 73.7 ms: 1.47x faster                                                            |
| pickle_pure_python      | 457 us                                                              | 319 us: 1.43x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 81.6 ms: 1.43x faster                                                            |
| scimark_lu              | 160 ms                                                              | 113 ms: 1.42x faster                                                             |
| coroutines              | 31.8 ms                                                             | 22.4 ms: 1.42x faster                                                            |
| spectral_norm           | 150 ms                                                              | 109 ms: 1.38x faster                                                             |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                                           |
| unpickle_pure_python    | 300 us                                                              | 219 us: 1.37x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 10.1 ms: 1.36x faster                                                            |
| genshi_text             | 30.4 ms                                                             | 22.4 ms: 1.36x faster                                                            |
| async_tree_none         | 713 ms                                                              | 528 ms: 1.35x faster                                                             |
| mako                    | 14.7 ms                                                             | 11.0 ms: 1.34x faster                                                            |
| float                   | 110 ms                                                              | 82.2 ms: 1.34x faster                                                            |
| html5lib                | 86.4 ms                                                             | 64.7 ms: 1.33x faster                                                            |
| django_template         | 45.8 ms                                                             | 34.4 ms: 1.33x faster                                                            |
| pprint_pformat          | 1.98 sec                                                            | 1.50 sec: 1.32x faster                                                           |
| deepcopy_memo           | 51.8 us                                                             | 39.3 us: 1.32x faster                                                            |
| chameleon               | 9.13 ms                                                             | 6.96 ms: 1.31x faster                                                            |
| async_tree_memoization  | 853 ms                                                              | 655 ms: 1.30x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 733 ms: 1.30x faster                                                             |
| logging_simple          | 8.21 us                                                             | 6.31 us: 1.30x faster                                                            |
| thrift                  | 1.04 ms                                                             | 802 us: 1.29x faster                                                             |
| logging_format          | 9.07 us                                                             | 7.03 us: 1.29x faster                                                            |
| genshi_xml              | 64.3 ms                                                             | 49.9 ms: 1.29x faster                                                            |
| pycparser               | 1.53 sec                                                            | 1.19 sec: 1.29x faster                                                           |
| xml_etree_process       | 74.8 ms                                                             | 58.7 ms: 1.27x faster                                                            |
| fannkuch                | 485 ms                                                              | 384 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 750 ms: 1.26x faster                                                             |
| unpack_sequence         | 65.6 ns                                                             | 52.4 ns: 1.25x faster                                                            |
| 2to3                    | 336 ms                                                              | 269 ms: 1.25x faster                                                             |
| mypy2                   | 432 ms                                                              | 350 ms: 1.23x faster                                                             |
| tornado_http            | 129 ms                                                              | 105 ms: 1.23x faster                                                             |
| regex_compile           | 177 ms                                                              | 145 ms: 1.23x faster                                                             |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                                             |
| nqueens                 | 98.8 ms                                                             | 82.4 ms: 1.20x faster                                                            |
| sqlglot_optimize        | 65.3 ms                                                             | 54.5 ms: 1.20x faster                                                            |
| deepcopy                | 438 us                                                              | 369 us: 1.19x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                           |
| scimark_fft             | 425 ms                                                              | 364 ms: 1.17x faster                                                             |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                            |
| deepcopy_reduce         | 3.80 us                                                             | 3.29 us: 1.15x faster                                                            |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.90 ms: 1.15x faster                                                            |
| bench_thread_pool       | 954 us                                                              | 835 us: 1.14x faster                                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                             |
| json_loads              | 29.3 us                                                             | 25.9 us: 1.13x faster                                                            |
| dulwich_log             | 76.3 ms                                                             | 67.8 ms: 1.13x faster                                                            |
| xml_etree_generate      | 94.9 ms                                                             | 84.6 ms: 1.12x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.1 ms: 1.11x faster                                                            |
| sympy_integrate         | 24.3 ms                                                             | 21.9 ms: 1.11x faster                                                            |
| pylint                  | 521 ms                                                              | 472 ms: 1.10x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.70 us: 1.10x faster                                                            |
| json                    | 5.41 ms                                                             | 4.92 ms: 1.10x faster                                                            |
| djangocms               | 36.3 us                                                             | 33.0 us: 1.10x faster                                                            |
| regex_v8                | 24.9 ms                                                             | 22.8 ms: 1.10x faster                                                            |
| create_gc_cycles        | 1.64 ms                                                             | 1.50 ms: 1.09x faster                                                            |
| sympy_expand            | 540 ms                                                              | 496 ms: 1.09x faster                                                             |
| pathlib                 | 19.8 ms                                                             | 18.3 ms: 1.08x faster                                                            |
| xml_etree_parse         | 164 ms                                                              | 152 ms: 1.08x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                             |
| meteor_contest          | 115 ms                                                              | 110 ms: 1.04x faster                                                             |
| sympy_str               | 328 ms                                                              | 316 ms: 1.04x faster                                                             |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                             |
| pickle_list             | 4.73 us                                                             | 4.61 us: 1.03x faster                                                            |
| sympy_sum               | 185 ms                                                              | 181 ms: 1.02x faster                                                             |
| mdp                     | 2.75 sec                                                            | 2.71 sec: 1.01x faster                                                           |
| unpickle                | 15.0 us                                                             | 14.8 us: 1.01x faster                                                            |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                            |
| unpickle_list           | 4.94 us                                                             | 5.00 us: 1.01x slower                                                            |
| telco                   | 6.67 ms                                                             | 6.80 ms: 1.02x slower                                                            |
| gc_traversal            | 3.53 ms                                                             | 3.60 ms: 1.02x slower                                                            |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.02x slower                                                            |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                             |
| async_generators        | 420 ms                                                              | 439 ms: 1.05x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                                            |
| pickle_dict             | 27.8 us                                                             | 31.6 us: 1.14x slower                                                            |
| python_startup_no_site  | 5.80 ms                                                             | 6.68 ms: 1.15x slower                                                            |
| dask                    | 437 ms                                                              | 541 ms: 1.24x slower                                                             |
| coverage                | 70.6 ms                                                             | 100 ms: 1.42x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.23x faster                                                                     |
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn
