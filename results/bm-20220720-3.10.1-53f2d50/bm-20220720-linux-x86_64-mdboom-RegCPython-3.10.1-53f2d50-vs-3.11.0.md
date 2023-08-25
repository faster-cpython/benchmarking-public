
# Results vs. 3.11.0

- fork: mdboom
- ref: RegCPython
- machine: linux-x86_64
- commit hash: 53f2d50
- commit date: 2022-07-20
- overall geometric mean: 1.18x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 313 ms: 1.21x slower                                      |
| chameleon      | 6.47 ms                                                | 8.49 ms: 1.31x slower                                     |
| docutils       | 2.63 sec                                               | 3.10 sec: 1.18x slower                                    |
| html5lib       | 64.5 ms                                                | 76.8 ms: 1.19x slower                                     |
| tornado_http   | 96.3 ms                                                | 123 ms: 1.28x slower                                      |
| Geometric mean | (ref)                                                  | 1.23x slower                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                      |
| nbody          | 93.1 ms                                                | 101 ms: 1.08x slower                                      |
| float          | 77.2 ms                                                | 94.9 ms: 1.23x slower                                     |
| Geometric mean | (ref)                                                  | 1.08x slower                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.31 ms: 1.21x faster                                     |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                      |
| regex_compile  | 138 ms                                                 | 157 ms: 1.14x slower                                      |
| regex_v8       | 22.0 ms                                                | 25.3 ms: 1.15x slower                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 27.2 us: 1.14x faster                                     |
| unpickle_list        | 4.91 us                                                | 4.86 us: 1.01x faster                                     |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                      |
| unpickle             | 13.7 us                                                | 14.3 us: 1.05x slower                                     |
| json_dumps           | 12.6 ms                                                | 13.4 ms: 1.06x slower                                     |
| json_loads           | 26.5 us                                                | 29.0 us: 1.10x slower                                     |
| pickle_list          | 4.11 us                                                | 4.65 us: 1.13x slower                                     |
| xml_etree_generate   | 76.2 ms                                                | 86.2 ms: 1.13x slower                                     |
| unpickle_pure_python | 228 us                                                 | 279 us: 1.22x slower                                      |
| xml_etree_process    | 53.9 ms                                                | 68.9 ms: 1.28x slower                                     |
| pickle_pure_python   | 306 us                                                 | 432 us: 1.41x slower                                      |
| Geometric mean       | (ref)                                                  | 1.09x slower                                              |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.80 ms: 1.04x faster                                     |
| python_startup         | 8.52 ms                                                | 15.2 ms: 1.78x slower                                     |
| Geometric mean         | (ref)                                                  | 1.31x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 60.6 ms: 1.17x slower                                     |
| mako            | 10.1 ms                                                | 13.1 ms: 1.30x slower                                     |
| genshi_text     | 21.6 ms                                                | 29.0 ms: 1.34x slower                                     |
| django_template | 32.6 ms                                                | 48.4 ms: 1.48x slower                                     |
| Geometric mean  | (ref)                                                  | 1.32x slower                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| generators              | 73.5 ms                                                | 56.3 ms: 1.31x faster                                     |
| regex_effbot            | 3.99 ms                                                | 3.31 ms: 1.21x faster                                     |
| pickle_dict             | 31.1 us                                                | 27.2 us: 1.14x faster                                     |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                      |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                     |
| telco                   | 6.58 ms                                                | 6.27 ms: 1.05x faster                                     |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.29 ms: 1.05x faster                                     |
| asyncio_tcp             | 922 ms                                                 | 885 ms: 1.04x faster                                      |
| python_startup_no_site  | 6.01 ms                                                | 5.80 ms: 1.04x faster                                     |
| unpickle_list           | 4.91 us                                                | 4.86 us: 1.01x faster                                     |
| meteor_contest          | 107 ms                                                 | 108 ms: 1.01x slower                                      |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                      |
| scimark_fft             | 328 ms                                                 | 337 ms: 1.03x slower                                      |
| unpickle                | 13.7 us                                                | 14.3 us: 1.05x slower                                     |
| mdp                     | 2.62 sec                                               | 2.74 sec: 1.05x slower                                    |
| regex_dna               | 204 ms                                                 | 216 ms: 1.06x slower                                      |
| json_dumps              | 12.6 ms                                                | 13.4 ms: 1.06x slower                                     |
| nqueens                 | 83.4 ms                                                | 88.6 ms: 1.06x slower                                     |
| nbody                   | 93.1 ms                                                | 101 ms: 1.08x slower                                      |
| json                    | 4.94 ms                                                | 5.37 ms: 1.09x slower                                     |
| sympy_sum               | 167 ms                                                 | 181 ms: 1.09x slower                                      |
| sympy_str               | 290 ms                                                 | 316 ms: 1.09x slower                                      |
| sympy_integrate         | 21.0 ms                                                | 22.9 ms: 1.09x slower                                     |
| json_loads              | 26.5 us                                                | 29.0 us: 1.10x slower                                     |
| pylint                  | 465 ms                                                 | 512 ms: 1.10x slower                                      |
| pathlib                 | 18.2 ms                                                | 20.1 ms: 1.10x slower                                     |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.9 ms: 1.11x slower                                     |
| djangocms               | 32.4 us                                                | 36.2 us: 1.12x slower                                     |
| dulwich_log             | 63.7 ms                                                | 71.2 ms: 1.12x slower                                     |
| sympy_expand            | 475 ms                                                 | 533 ms: 1.12x slower                                      |
| coroutines              | 25.5 ms                                                | 28.6 ms: 1.12x slower                                     |
| gunicorn                | 1.18 ms                                                | 1.33 ms: 1.13x slower                                     |
| pickle_list             | 4.11 us                                                | 4.65 us: 1.13x slower                                     |
| xml_etree_generate      | 76.2 ms                                                | 86.2 ms: 1.13x slower                                     |
| flaskblogging           | 7.12 ms                                                | 8.07 ms: 1.13x slower                                     |
| aiohttp                 | 1.10 ms                                                | 1.25 ms: 1.14x slower                                     |
| regex_compile           | 138 ms                                                 | 157 ms: 1.14x slower                                      |
| create_gc_cycles        | 1.49 ms                                                | 1.69 ms: 1.14x slower                                     |
| regex_v8                | 22.0 ms                                                | 25.3 ms: 1.15x slower                                     |
| bench_thread_pool       | 819 us                                                 | 947 us: 1.16x slower                                      |
| pycparser               | 1.18 sec                                               | 1.37 sec: 1.16x slower                                    |
| sqlite_synth            | 2.52 us                                                | 2.93 us: 1.16x slower                                     |
| genshi_xml              | 51.8 ms                                                | 60.6 ms: 1.17x slower                                     |
| docutils                | 2.63 sec                                               | 3.10 sec: 1.18x slower                                    |
| deepcopy                | 342 us                                                 | 404 us: 1.18x slower                                      |
| sqlalchemy_declarative  | 138 ms                                                 | 164 ms: 1.18x slower                                      |
| html5lib                | 64.5 ms                                                | 76.8 ms: 1.19x slower                                     |
| deepcopy_reduce         | 2.94 us                                                | 3.55 us: 1.21x slower                                     |
| 2to3                    | 259 ms                                                 | 313 ms: 1.21x slower                                      |
| deepcopy_memo           | 37.0 us                                                | 45.1 us: 1.22x slower                                     |
| unpickle_pure_python    | 228 us                                                 | 279 us: 1.22x slower                                      |
| unpack_sequence         | 43.1 ns                                                | 52.8 ns: 1.23x slower                                     |
| float                   | 77.2 ms                                                | 94.9 ms: 1.23x slower                                     |
| spectral_norm           | 100 ms                                                 | 124 ms: 1.24x slower                                      |
| async_tree_io           | 1.30 sec                                               | 1.61 sec: 1.24x slower                                    |
| sqlglot_optimize        | 53.1 ms                                                | 66.5 ms: 1.25x slower                                     |
| scimark_monte_carlo     | 68.1 ms                                                | 85.8 ms: 1.26x slower                                     |
| logging_format          | 6.68 us                                                | 8.42 us: 1.26x slower                                     |
| tornado_http            | 96.3 ms                                                | 123 ms: 1.28x slower                                      |
| xml_etree_process       | 53.9 ms                                                | 68.9 ms: 1.28x slower                                     |
| pprint_pformat          | 1.46 sec                                               | 1.88 sec: 1.29x slower                                    |
| sqlglot_normalize       | 108 ms                                                 | 139 ms: 1.29x slower                                      |
| mako                    | 10.1 ms                                                | 13.1 ms: 1.30x slower                                     |
| pprint_safe_repr        | 701 ms                                                 | 914 ms: 1.30x slower                                      |
| logging_simple          | 6.03 us                                                | 7.90 us: 1.31x slower                                     |
| chameleon               | 6.47 ms                                                | 8.49 ms: 1.31x slower                                     |
| async_tree_cpu_io_mixed | 739 ms                                                 | 970 ms: 1.31x slower                                      |
| chaos                   | 69.2 ms                                                | 91.1 ms: 1.32x slower                                     |
| hexiom                  | 6.37 ms                                                | 8.43 ms: 1.32x slower                                     |
| async_tree_memoization  | 627 ms                                                 | 839 ms: 1.34x slower                                      |
| async_generators        | 368 ms                                                 | 495 ms: 1.34x slower                                      |
| genshi_text             | 21.6 ms                                                | 29.0 ms: 1.34x slower                                     |
| sqlglot_transpile       | 1.70 ms                                                | 2.31 ms: 1.35x slower                                     |
| thrift                  | 756 us                                                 | 1.03 ms: 1.36x slower                                     |
| async_tree_none         | 526 ms                                                 | 724 ms: 1.37x slower                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.93 ms: 1.38x slower                                     |
| pyflate                 | 418 ms                                                 | 580 ms: 1.39x slower                                      |
| scimark_lu              | 110 ms                                                 | 153 ms: 1.39x slower                                      |
| pickle_pure_python      | 306 us                                                 | 432 us: 1.41x slower                                      |
| crypto_pyaes            | 74.7 ms                                                | 106 ms: 1.42x slower                                      |
| go                      | 140 ms                                                 | 203 ms: 1.45x slower                                      |
| richards                | 45.7 ms                                                | 67.6 ms: 1.48x slower                                     |
| django_template         | 32.6 ms                                                | 48.4 ms: 1.48x slower                                     |
| raytrace                | 297 ms                                                 | 440 ms: 1.48x slower                                      |
| scimark_sor             | 118 ms                                                 | 176 ms: 1.49x slower                                      |
| python_startup          | 8.52 ms                                                | 15.2 ms: 1.78x slower                                     |
| logging_silent          | 101 ns                                                 | 194 ns: 1.92x slower                                      |
| deltablue               | 3.67 ms                                                | 7.24 ms: 1.97x slower                                     |
| Geometric mean          | (ref)                                                  | 1.18x slower                                              |

Benchmark hidden because not significant (3): xml_etree_parse, bench_mp_pool, pickle
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, coverage, dask, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220720-3.10.1-53f2d50/bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50.json: mypy


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.13x
