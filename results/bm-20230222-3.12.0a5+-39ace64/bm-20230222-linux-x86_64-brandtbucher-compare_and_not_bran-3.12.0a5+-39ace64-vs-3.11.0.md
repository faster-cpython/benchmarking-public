
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 39ace64
- commit date: 2023-02-22
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                        |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.4 ms: 1.05x faster                                                        |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                         |
| nbody          | 93.1 ms                                                | 96.7 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                        |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                         |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                         |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.5 ms: 1.04x faster                                                        |
| pickle_list          | 4.11 us                                                | 4.03 us: 1.02x faster                                                        |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                                        |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 54.6 ms: 1.01x slower                                                        |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.7 ms: 1.11x faster                                                        |
| genshi_text    | 21.6 ms                                                | 20.7 ms: 1.04x faster                                                        |
| mako           | 10.1 ms                                                | 9.80 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.6 ms: 2.49x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                                         |
| deltablue               | 3.67 ms                                                | 3.14 ms: 1.17x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                         |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.02 ms: 1.12x faster                                                        |
| logging_silent          | 101 ns                                                 | 90.4 ns: 1.12x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 46.7 ms: 1.11x faster                                                        |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.09x faster                                                         |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.08x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                       |
| hexiom                  | 6.37 ms                                                | 5.90 ms: 1.08x faster                                                        |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                        |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                                        |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                         |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                         |
| nqueens                 | 83.4 ms                                                | 78.1 ms: 1.07x faster                                                        |
| fannkuch                | 388 ms                                                 | 364 ms: 1.07x faster                                                         |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 50.2 ms: 1.06x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.06x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.05x faster                                                         |
| float                   | 77.2 ms                                                | 73.4 ms: 1.05x faster                                                        |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                                        |
| spectral_norm           | 100 ms                                                 | 95.4 ms: 1.05x faster                                                        |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                         |
| gc_traversal            | 4.02 ms                                                | 3.85 ms: 1.05x faster                                                        |
| html5lib                | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 99.5 ms: 1.04x faster                                                        |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                       |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                                        |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                                       |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                         |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                         |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                         |
| chaos                   | 69.2 ms                                                | 67.0 ms: 1.03x faster                                                        |
| telco                   | 6.58 ms                                                | 6.39 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| mako                    | 10.1 ms                                                | 9.80 ms: 1.03x faster                                                        |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                         |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 66.2 ms: 1.03x faster                                                        |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                         |
| crypto_pyaes            | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                        |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| pickle_list             | 4.11 us                                                | 4.03 us: 1.02x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 688 ms: 1.02x faster                                                         |
| coverage                | 100 ms                                                 | 98.2 ms: 1.02x faster                                                        |
| tornado_http            | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                        |
| pyflate                 | 418 ms                                                 | 412 ms: 1.02x faster                                                         |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                         |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                                        |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                         |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.00x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                        |
| thrift                  | 756 us                                                 | 761 us: 1.01x slower                                                         |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 54.6 ms: 1.01x slower                                                        |
| unpickle_list           | 4.91 us                                                | 5.02 us: 1.02x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.03x slower                                                        |
| nbody                   | 93.1 ms                                                | 96.7 ms: 1.04x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.05x slower                                                        |
| regex_dna               | 204 ms                                                 | 216 ms: 1.06x slower                                                         |
| python_startup          | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 666 ms: 1.06x slower                                                         |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                        |
| async_generators        | 368 ms                                                 | 409 ms: 1.11x slower                                                         |
| dask                    | 360 ms                                                 | 503 ms: 1.40x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (9): unpickle, deepcopy_reduce, bench_mp_pool, regex_v8, django_template, async_tree_none, sqlalchemy_imperative, djangocms, async_tree_cpu_io_mixed
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
