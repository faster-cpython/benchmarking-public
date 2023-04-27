
# Results vs. 3.11.0

- fork: Fidget-Spinner
- ref: call_function_ex_inl
- machine: linux-x86_64
- commit hash: dfd6b01
- commit date: 2023-04-27
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 269 ms: 1.05x slower                                                             |
| chameleon      | 6.52 ms                                                             | 6.96 ms: 1.07x slower                                                            |
| docutils       | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                           |
| tornado_http   | 96.7 ms                                                             | 105 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 89.2 ms: 1.08x faster                                                            |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x slower                                                             |
| float          | 76.0 ms                                                             | 82.2 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.8 ms: 1.04x slower                                                            |
| regex_effbot   | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                                            |
| regex_dna      | 196 ms                                                              | 207 ms: 1.05x slower                                                             |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.1 ms: 1.25x faster                                                            |
| xml_etree_parse      | 162 ms                                                              | 152 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.04x faster                                                             |
| unpickle_pure_python | 228 us                                                              | 219 us: 1.04x faster                                                             |
| json_loads           | 26.2 us                                                             | 25.9 us: 1.01x faster                                                            |
| unpickle_list        | 4.96 us                                                             | 5.00 us: 1.01x slower                                                            |
| pickle_dict          | 30.9 us                                                             | 31.6 us: 1.02x slower                                                            |
| pickle_pure_python   | 307 us                                                              | 319 us: 1.04x slower                                                             |
| pickle               | 9.79 us                                                             | 10.5 us: 1.07x slower                                                            |
| xml_etree_process    | 54.1 ms                                                             | 58.7 ms: 1.08x slower                                                            |
| xml_etree_generate   | 76.5 ms                                                             | 84.6 ms: 1.11x slower                                                            |
| unpickle             | 13.2 us                                                             | 14.8 us: 1.12x slower                                                            |
| pickle_list          | 4.03 us                                                             | 4.61 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.11 ms: 1.07x slower                                                            |
| python_startup_no_site | 5.98 ms                                                             | 6.68 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 49.9 ms: 1.04x faster                                                            |
| genshi_text     | 21.8 ms                                                             | 22.4 ms: 1.03x slower                                                            |
| django_template | 32.9 ms                                                             | 34.4 ms: 1.05x slower                                                            |
| mako            | 9.82 ms                                                             | 11.0 ms: 1.12x slower                                                            |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 32.4 ms: 2.26x faster                                                            |
| asyncio_tcp             | 888 ms                                                              | 506 ms: 1.75x faster                                                             |
| json_dumps              | 12.5 ms                                                             | 10.1 ms: 1.25x faster                                                            |
| mypy2                   | 422 ms                                                              | 350 ms: 1.20x faster                                                             |
| coroutines              | 26.3 ms                                                             | 22.4 ms: 1.17x faster                                                            |
| nbody                   | 96.7 ms                                                             | 89.2 ms: 1.08x faster                                                            |
| xml_etree_parse         | 162 ms                                                              | 152 ms: 1.07x faster                                                             |
| richards                | 45.7 ms                                                             | 43.1 ms: 1.06x faster                                                            |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.04x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 219 us: 1.04x faster                                                             |
| genshi_xml              | 51.8 ms                                                             | 49.9 ms: 1.04x faster                                                            |
| deltablue               | 3.66 ms                                                             | 3.54 ms: 1.03x faster                                                            |
| hexiom                  | 6.48 ms                                                             | 6.34 ms: 1.02x faster                                                            |
| nqueens                 | 84.0 ms                                                             | 82.4 ms: 1.02x faster                                                            |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                            |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                                             |
| json_loads              | 26.2 us                                                             | 25.9 us: 1.01x faster                                                            |
| coverage                | 101 ms                                                              | 100 ms: 1.01x faster                                                             |
| gc_traversal            | 3.63 ms                                                             | 3.60 ms: 1.01x faster                                                            |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x slower                                                             |
| logging_silent          | 98.7 ns                                                             | 99.1 ns: 1.00x slower                                                            |
| unpickle_list           | 4.96 us                                                             | 5.00 us: 1.01x slower                                                            |
| json                    | 4.86 ms                                                             | 4.92 ms: 1.01x slower                                                            |
| create_gc_cycles        | 1.48 ms                                                             | 1.50 ms: 1.01x slower                                                            |
| bench_thread_pool       | 820 us                                                              | 835 us: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 750 ms: 1.02x slower                                                             |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.02x slower                                                             |
| sqlglot_optimize        | 53.4 ms                                                             | 54.5 ms: 1.02x slower                                                            |
| pickle_dict             | 30.9 us                                                             | 31.6 us: 1.02x slower                                                            |
| genshi_text             | 21.8 ms                                                             | 22.4 ms: 1.03x slower                                                            |
| mdp                     | 2.64 sec                                                            | 2.71 sec: 1.03x slower                                                           |
| telco                   | 6.59 ms                                                             | 6.80 ms: 1.03x slower                                                            |
| pprint_pformat          | 1.45 sec                                                            | 1.50 sec: 1.03x slower                                                           |
| chaos                   | 68.0 ms                                                             | 70.3 ms: 1.04x slower                                                            |
| logging_simple          | 6.09 us                                                             | 6.31 us: 1.04x slower                                                            |
| regex_v8                | 22.0 ms                                                             | 22.8 ms: 1.04x slower                                                            |
| pickle_pure_python      | 307 us                                                              | 319 us: 1.04x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                                            |
| raytrace                | 292 ms                                                              | 304 ms: 1.04x slower                                                             |
| scimark_lu              | 108 ms                                                              | 113 ms: 1.04x slower                                                             |
| meteor_contest          | 106 ms                                                              | 110 ms: 1.04x slower                                                             |
| sympy_expand            | 477 ms                                                              | 496 ms: 1.04x slower                                                             |
| pycparser               | 1.14 sec                                                            | 1.19 sec: 1.04x slower                                                           |
| sympy_integrate         | 21.0 ms                                                             | 21.9 ms: 1.04x slower                                                            |
| pprint_safe_repr        | 701 ms                                                              | 733 ms: 1.04x slower                                                             |
| django_template         | 32.9 ms                                                             | 34.4 ms: 1.05x slower                                                            |
| 2to3                    | 257 ms                                                              | 269 ms: 1.05x slower                                                             |
| docutils                | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                           |
| thrift                  | 766 us                                                              | 802 us: 1.05x slower                                                             |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.05x slower                                                             |
| regex_dna               | 196 ms                                                              | 207 ms: 1.05x slower                                                             |
| async_tree_memoization  | 621 ms                                                              | 655 ms: 1.05x slower                                                             |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                            |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.1 ms: 1.06x slower                                                            |
| logging_format          | 6.64 us                                                             | 7.03 us: 1.06x slower                                                            |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                                             |
| unpack_sequence         | 49.5 ns                                                             | 52.4 ns: 1.06x slower                                                            |
| dulwich_log             | 63.6 ms                                                             | 67.8 ms: 1.07x slower                                                            |
| chameleon               | 6.52 ms                                                             | 6.96 ms: 1.07x slower                                                            |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.07x slower                                                            |
| python_startup          | 8.49 ms                                                             | 9.11 ms: 1.07x slower                                                            |
| sqlite_synth            | 2.51 us                                                             | 2.70 us: 1.07x slower                                                            |
| deepcopy_memo           | 36.4 us                                                             | 39.3 us: 1.08x slower                                                            |
| sympy_sum               | 167 ms                                                              | 181 ms: 1.08x slower                                                             |
| float                   | 76.0 ms                                                             | 82.2 ms: 1.08x slower                                                            |
| xml_etree_process       | 54.1 ms                                                             | 58.7 ms: 1.08x slower                                                            |
| tornado_http            | 96.7 ms                                                             | 105 ms: 1.09x slower                                                             |
| sympy_str               | 291 ms                                                              | 316 ms: 1.09x slower                                                             |
| scimark_sor             | 115 ms                                                              | 125 ms: 1.09x slower                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.7 ms: 1.09x slower                                                            |
| deepcopy                | 339 us                                                              | 369 us: 1.09x slower                                                             |
| spectral_norm           | 99.5 ms                                                             | 109 ms: 1.09x slower                                                             |
| pyflate                 | 414 ms                                                              | 453 ms: 1.10x slower                                                             |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.90 ms: 1.10x slower                                                            |
| xml_etree_generate      | 76.5 ms                                                             | 84.6 ms: 1.11x slower                                                            |
| crypto_pyaes            | 73.8 ms                                                             | 81.6 ms: 1.11x slower                                                            |
| scimark_fft             | 328 ms                                                              | 364 ms: 1.11x slower                                                             |
| deepcopy_reduce         | 2.96 us                                                             | 3.29 us: 1.11x slower                                                            |
| mako                    | 9.82 ms                                                             | 11.0 ms: 1.12x slower                                                            |
| python_startup_no_site  | 5.98 ms                                                             | 6.68 ms: 1.12x slower                                                            |
| unpickle                | 13.2 us                                                             | 14.8 us: 1.12x slower                                                            |
| pickle_list             | 4.03 us                                                             | 4.61 us: 1.14x slower                                                            |
| async_generators        | 361 ms                                                              | 439 ms: 1.21x slower                                                             |
| dask                    | 368 ms                                                              | 541 ms: 1.47x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                                     |

Benchmark hidden because not significant (9): pylint, bench_mp_pool, fannkuch, pathlib, sqlglot_transpile, async_tree_none, async_tree_io, html5lib, djangocms
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn
