
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.00x slower \*
- HPT reliability: 93.44%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.2 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.6 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 81.3 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.67 ms: 1.09x faster                                  |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.99 ms: 1.26x faster                                  |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                   |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                  |
| pickle_pure_python   | 306 us                                                 | 314 us: 1.03x slower                                   |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                  |
| unpickle             | 13.7 us                                                | 14.7 us: 1.08x slower                                  |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.1 ms: 1.10x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.07 ms: 1.06x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.65 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 50.2 ms: 1.03x faster                                  |
| genshi_text    | 21.6 ms                                                | 22.4 ms: 1.04x slower                                  |
| mako           | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.7 ms: 2.39x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 509 ms: 1.81x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.99 ms: 1.26x faster                                  |
| mypy2                   | 420 ms                                                 | 351 ms: 1.20x faster                                   |
| coroutines              | 25.5 ms                                                | 22.1 ms: 1.15x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.67 ms: 1.09x faster                                  |
| async_tree_none         | 526 ms                                                 | 495 ms: 1.06x faster                                   |
| async_tree_io           | 1.30 sec                                               | 1.22 sec: 1.06x faster                                 |
| unpickle_pure_python    | 228 us                                                 | 216 us: 1.06x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.33 ms: 1.05x faster                                  |
| nbody                   | 93.1 ms                                                | 88.6 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                   |
| richards                | 45.7 ms                                                | 43.7 ms: 1.05x faster                                  |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                 |
| sqlglot_transpile       | 1.70 ms                                                | 1.65 ms: 1.03x faster                                  |
| genshi_xml              | 51.8 ms                                                | 50.2 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 718 ms: 1.03x faster                                   |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                   |
| json_loads              | 26.5 us                                                | 25.8 us: 1.03x faster                                  |
| deltablue               | 3.67 ms                                                | 3.57 ms: 1.03x faster                                  |
| async_tree_memoization  | 627 ms                                                 | 611 ms: 1.03x faster                                   |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.22 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                  |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                  |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                 |
| gc_traversal            | 4.02 ms                                                | 4.06 ms: 1.01x slower                                  |
| spectral_norm           | 100 ms                                                 | 101 ms: 1.01x slower                                   |
| bench_thread_pool       | 819 us                                                 | 836 us: 1.02x slower                                   |
| scimark_lu              | 110 ms                                                 | 112 ms: 1.02x slower                                   |
| pickle_dict             | 31.1 us                                                | 31.8 us: 1.02x slower                                  |
| raytrace                | 297 ms                                                 | 303 ms: 1.02x slower                                   |
| logging_silent          | 101 ns                                                 | 104 ns: 1.03x slower                                   |
| pickle_pure_python      | 306 us                                                 | 314 us: 1.03x slower                                   |
| sqlglot_optimize        | 53.1 ms                                                | 54.7 ms: 1.03x slower                                  |
| tornado_http            | 96.3 ms                                                | 99.2 ms: 1.03x slower                                  |
| logging_simple          | 6.03 us                                                | 6.22 us: 1.03x slower                                  |
| 2to3                    | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| pprint_pformat          | 1.46 sec                                               | 1.51 sec: 1.03x slower                                 |
| deepcopy_memo           | 37.0 us                                                | 38.4 us: 1.04x slower                                  |
| logging_format          | 6.68 us                                                | 6.93 us: 1.04x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 112 ms: 1.04x slower                                   |
| genshi_text             | 21.6 ms                                                | 22.4 ms: 1.04x slower                                  |
| docutils                | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                  |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                   |
| telco                   | 6.58 ms                                                | 6.88 ms: 1.05x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.71 ms: 1.05x slower                                  |
| regex_compile           | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| float                   | 77.2 ms                                                | 81.3 ms: 1.05x slower                                  |
| pprint_safe_repr        | 701 ms                                                 | 738 ms: 1.05x slower                                   |
| pickle                  | 10.1 us                                                | 10.6 us: 1.05x slower                                  |
| thrift                  | 756 us                                                 | 797 us: 1.05x slower                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.06x slower                                   |
| deepcopy                | 342 us                                                 | 364 us: 1.06x slower                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.1 ms: 1.06x slower                                  |
| python_startup          | 8.52 ms                                                | 9.07 ms: 1.06x slower                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 72.6 ms: 1.07x slower                                  |
| mako                    | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 79.7 ms: 1.07x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.70 us: 1.07x slower                                  |
| dulwich_log             | 63.7 ms                                                | 68.3 ms: 1.07x slower                                  |
| pyflate                 | 418 ms                                                 | 450 ms: 1.08x slower                                   |
| unpickle                | 13.7 us                                                | 14.7 us: 1.08x slower                                  |
| scimark_fft             | 328 ms                                                 | 357 ms: 1.09x slower                                   |
| meteor_contest          | 107 ms                                                 | 116 ms: 1.09x slower                                   |
| deepcopy_reduce         | 2.94 us                                                | 3.21 us: 1.09x slower                                  |
| pickle_list             | 4.11 us                                                | 4.51 us: 1.10x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 59.1 ms: 1.10x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.65 ms: 1.11x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 84.6 ms: 1.11x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 47.9 ns: 1.11x slower                                  |
| async_generators        | 368 ms                                                 | 434 ms: 1.18x slower                                   |
| dask                    | 360 ms                                                 | 539 ms: 1.50x slower                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (8): regex_v8, json, bench_mp_pool, coverage, nqueens, chaos, unpickle_list, html5lib
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 93.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
