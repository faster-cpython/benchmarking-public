
# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: call_function_ex_inl
- machine: linux-x86_64
- commit hash: dfd6b01
- commit date: 2023-04-27
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.96 ms: 1.30x faster                                                            |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                           |
| html5lib       | 85.9 ms                                                | 64.7 ms: 1.33x faster                                                            |
| tornado_http   | 127 ms                                                 | 105 ms: 1.21x faster                                                             |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.2 ms: 1.59x faster                                                            |
| float          | 111 ms                                                 | 82.2 ms: 1.34x faster                                                            |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                             |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                                            |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 319 us: 1.43x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                                             |
| json_dumps           | 13.5 ms                                                | 10.1 ms: 1.35x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                            |
| json_loads           | 28.8 us                                                | 25.9 us: 1.11x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.61 us: 1.01x slower                                                            |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                            |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                            |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.11 ms: 1.55x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 30.3 ms                                                | 22.4 ms: 1.35x faster                                                            |
| mako            | 14.8 ms                                                | 11.0 ms: 1.35x faster                                                            |
| django_template | 45.9 ms                                                | 34.4 ms: 1.34x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 49.9 ms: 1.27x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 32.4 ms: 2.37x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.54 ms: 2.09x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                             |
| logging_silent          | 175 ns                                                 | 99.1 ns: 1.77x faster                                                            |
| richards                | 74.9 ms                                                | 43.1 ms: 1.74x faster                                                            |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                             |
| nbody                   | 142 ms                                                 | 89.2 ms: 1.59x faster                                                            |
| scimark_sor             | 197 ms                                                 | 125 ms: 1.58x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.11 ms: 1.55x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                            |
| raytrace                | 464 ms                                                 | 304 ms: 1.53x faster                                                             |
| chaos                   | 106 ms                                                 | 70.3 ms: 1.51x faster                                                            |
| hexiom                  | 9.53 ms                                                | 6.34 ms: 1.50x faster                                                            |
| pyflate                 | 673 ms                                                 | 453 ms: 1.49x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.66 ms: 1.48x faster                                                            |
| scimark_monte_carlo     | 108 ms                                                 | 73.7 ms: 1.47x faster                                                            |
| crypto_pyaes            | 118 ms                                                 | 81.6 ms: 1.45x faster                                                            |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.45x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 319 us: 1.43x faster                                                             |
| coroutines              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                            |
| spectral_norm           | 150 ms                                                 | 109 ms: 1.38x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                           |
| unpickle_pure_python    | 300 us                                                 | 219 us: 1.37x faster                                                             |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                             |
| genshi_text             | 30.3 ms                                                | 22.4 ms: 1.35x faster                                                            |
| mako                    | 14.8 ms                                                | 11.0 ms: 1.35x faster                                                            |
| json_dumps              | 13.5 ms                                                | 10.1 ms: 1.35x faster                                                            |
| float                   | 111 ms                                                 | 82.2 ms: 1.34x faster                                                            |
| django_template         | 45.9 ms                                                | 34.4 ms: 1.34x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 39.3 us: 1.33x faster                                                            |
| html5lib                | 85.9 ms                                                | 64.7 ms: 1.33x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.32x faster                                                           |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 733 ms: 1.30x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.96 ms: 1.30x faster                                                            |
| thrift                  | 1.03 ms                                                | 802 us: 1.29x faster                                                             |
| logging_simple          | 8.07 us                                                | 6.31 us: 1.28x faster                                                            |
| xml_etree_process       | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                            |
| genshi_xml              | 63.3 ms                                                | 49.9 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                                             |
| logging_format          | 8.91 us                                                | 7.03 us: 1.27x faster                                                            |
| fannkuch                | 486 ms                                                 | 384 ms: 1.26x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.19 sec: 1.26x faster                                                           |
| 2to3                    | 336 ms                                                 | 269 ms: 1.25x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 52.4 ns: 1.23x faster                                                            |
| mypy2                   | 428 ms                                                 | 350 ms: 1.22x faster                                                             |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.22x faster                                                             |
| tornado_http            | 127 ms                                                 | 105 ms: 1.21x faster                                                             |
| nqueens                 | 100 ms                                                 | 82.4 ms: 1.21x faster                                                            |
| sqlglot_optimize        | 65.3 ms                                                | 54.5 ms: 1.20x faster                                                            |
| deepcopy                | 442 us                                                 | 369 us: 1.20x faster                                                             |
| docutils                | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                           |
| scimark_fft             | 424 ms                                                 | 364 ms: 1.16x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.29 us: 1.16x faster                                                            |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.14x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 835 us: 1.13x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 67.8 ms: 1.12x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.90 ms: 1.11x faster                                                            |
| json_loads              | 28.8 us                                                | 25.9 us: 1.11x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                            |
| pylint                  | 525 ms                                                 | 472 ms: 1.11x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.1 ms: 1.11x faster                                                            |
| sympy_integrate         | 24.3 ms                                                | 21.9 ms: 1.11x faster                                                            |
| json                    | 5.42 ms                                                | 4.92 ms: 1.10x faster                                                            |
| regex_v8                | 25.0 ms                                                | 22.8 ms: 1.10x faster                                                            |
| sympy_expand            | 545 ms                                                 | 496 ms: 1.10x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                            |
| djangocms               | 35.9 us                                                | 33.0 us: 1.09x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.08x faster                                                             |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.60 ms: 1.07x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.71 sec: 1.04x faster                                                           |
| meteor_contest          | 115 ms                                                 | 110 ms: 1.04x faster                                                             |
| sympy_str               | 328 ms                                                 | 316 ms: 1.04x faster                                                             |
| sympy_sum               | 185 ms                                                 | 181 ms: 1.02x faster                                                             |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                            |
| pickle_list             | 4.56 us                                                | 4.61 us: 1.01x slower                                                            |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                            |
| async_generators        | 425 ms                                                 | 439 ms: 1.03x slower                                                             |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                             |
| telco                   | 6.54 ms                                                | 6.80 ms: 1.04x slower                                                            |
| unpickle                | 14.1 us                                                | 14.8 us: 1.05x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.68 ms: 1.15x slower                                                            |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                            |
| dask                    | 423 ms                                                 | 541 ms: 1.28x slower                                                             |
| coverage                | 72.8 ms                                                | 100 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                                     |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x
