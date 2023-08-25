
# Results vs. 3.11.0

- fork: Fidget-Spinner
- ref: call_function_ex_inl
- machine: linux-x86_64
- commit hash: dfd6b01
- commit date: 2023-04-27
- overall geometric mean: 1.01x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                                             |
| chameleon      | 6.47 ms                                                | 6.96 ms: 1.08x slower                                                            |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                           |
| tornado_http   | 96.3 ms                                                | 105 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                            |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                             |
| float          | 77.2 ms                                                | 82.2 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                            |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                             |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.03x slower                                                            |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.1 ms: 1.25x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.05x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                                             |
| json_loads           | 26.5 us                                                | 25.9 us: 1.02x faster                                                            |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                            |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                                            |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                            |
| pickle_pure_python   | 306 us                                                 | 319 us: 1.04x slower                                                             |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                                            |
| xml_etree_process    | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                            |
| pickle_list          | 4.11 us                                                | 4.61 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.11 ms: 1.07x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.9 ms: 1.04x faster                                                            |
| genshi_text     | 21.6 ms                                                | 22.4 ms: 1.04x slower                                                            |
| django_template | 32.6 ms                                                | 34.4 ms: 1.05x slower                                                            |
| mako            | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 32.4 ms: 2.27x faster                                                            |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                             |
| json_dumps              | 12.6 ms                                                | 10.1 ms: 1.25x faster                                                            |
| mypy2                   | 420 ms                                                 | 350 ms: 1.20x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                            |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                            |
| gc_traversal            | 4.02 ms                                                | 3.60 ms: 1.12x faster                                                            |
| richards                | 45.7 ms                                                | 43.1 ms: 1.06x faster                                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                            |
| xml_etree_parse         | 158 ms                                                 | 152 ms: 1.05x faster                                                             |
| nbody                   | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 219 us: 1.04x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 49.9 ms: 1.04x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.54 ms: 1.04x faster                                                            |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.66 ms: 1.03x faster                                                            |
| json_loads              | 26.5 us                                                | 25.9 us: 1.02x faster                                                            |
| logging_silent          | 101 ns                                                 | 99.1 ns: 1.02x faster                                                            |
| nqueens                 | 83.4 ms                                                | 82.4 ms: 1.01x faster                                                            |
| fannkuch                | 388 ms                                                 | 384 ms: 1.01x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.34 ms: 1.01x faster                                                            |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.01x slower                                                             |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                             |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.02x slower                                                            |
| chaos                   | 69.2 ms                                                | 70.3 ms: 1.02x slower                                                            |
| unpickle_list           | 4.91 us                                                | 5.00 us: 1.02x slower                                                            |
| bench_thread_pool       | 819 us                                                 | 835 us: 1.02x slower                                                             |
| raytrace                | 297 ms                                                 | 304 ms: 1.02x slower                                                             |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 54.5 ms: 1.03x slower                                                            |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                           |
| docutils                | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                           |
| regex_v8                | 22.0 ms                                                | 22.8 ms: 1.03x slower                                                            |
| telco                   | 6.58 ms                                                | 6.80 ms: 1.03x slower                                                            |
| meteor_contest          | 107 ms                                                 | 110 ms: 1.04x slower                                                             |
| mdp                     | 2.62 sec                                               | 2.71 sec: 1.04x slower                                                           |
| 2to3                    | 259 ms                                                 | 269 ms: 1.04x slower                                                             |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                            |
| genshi_text             | 21.6 ms                                                | 22.4 ms: 1.04x slower                                                            |
| pickle_pure_python      | 306 us                                                 | 319 us: 1.04x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 655 ms: 1.04x slower                                                             |
| pprint_safe_repr        | 701 ms                                                 | 733 ms: 1.04x slower                                                             |
| sympy_integrate         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                            |
| sympy_expand            | 475 ms                                                 | 496 ms: 1.04x slower                                                             |
| logging_simple          | 6.03 us                                                | 6.31 us: 1.05x slower                                                            |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                                            |
| regex_compile           | 138 ms                                                 | 145 ms: 1.05x slower                                                             |
| logging_format          | 6.68 us                                                | 7.03 us: 1.05x slower                                                            |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.05x slower                                                             |
| django_template         | 32.6 ms                                                | 34.4 ms: 1.05x slower                                                            |
| scimark_sor             | 118 ms                                                 | 125 ms: 1.06x slower                                                             |
| thrift                  | 756 us                                                 | 802 us: 1.06x slower                                                             |
| deepcopy_memo           | 37.0 us                                                | 39.3 us: 1.06x slower                                                            |
| float                   | 77.2 ms                                                | 82.2 ms: 1.06x slower                                                            |
| dulwich_log             | 63.7 ms                                                | 67.8 ms: 1.06x slower                                                            |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.1 ms: 1.06x slower                                                            |
| python_startup          | 8.52 ms                                                | 9.11 ms: 1.07x slower                                                            |
| sqlite_synth            | 2.52 us                                                | 2.70 us: 1.07x slower                                                            |
| chameleon               | 6.47 ms                                                | 6.96 ms: 1.08x slower                                                            |
| deepcopy                | 342 us                                                 | 369 us: 1.08x slower                                                             |
| pyflate                 | 418 ms                                                 | 453 ms: 1.08x slower                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 73.7 ms: 1.08x slower                                                            |
| unpickle                | 13.7 us                                                | 14.8 us: 1.08x slower                                                            |
| spectral_norm           | 100 ms                                                 | 109 ms: 1.09x slower                                                             |
| sympy_sum               | 167 ms                                                 | 181 ms: 1.09x slower                                                             |
| mako                    | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.90 ms: 1.09x slower                                                            |
| xml_etree_process       | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                            |
| tornado_http            | 96.3 ms                                                | 105 ms: 1.09x slower                                                             |
| sympy_str               | 290 ms                                                 | 316 ms: 1.09x slower                                                             |
| crypto_pyaes            | 74.7 ms                                                | 81.6 ms: 1.09x slower                                                            |
| scimark_fft             | 328 ms                                                 | 364 ms: 1.11x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.68 ms: 1.11x slower                                                            |
| deepcopy_reduce         | 2.94 us                                                | 3.29 us: 1.12x slower                                                            |
| pickle_list             | 4.11 us                                                | 4.61 us: 1.12x slower                                                            |
| async_generators        | 368 ms                                                 | 439 ms: 1.19x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 52.4 ns: 1.22x slower                                                            |
| dask                    | 360 ms                                                 | 541 ms: 1.50x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (11): xml_etree_iterparse, json, async_tree_io, bench_mp_pool, coverage, pathlib, html5lib, async_tree_none, pycparser, pylint, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
