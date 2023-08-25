
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_deep_freeze
- machine: linux-x86_64
- commit hash: 76326f3
- commit date: 2023-03-16
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                      |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                     |
| html5lib       | 64.5 ms                                                | 59.2 ms: 1.09x faster                                                      |
| tornado_http   | 96.3 ms                                                | 90.9 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.2 ms: 1.06x faster                                                      |
| float          | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                      |
| pidigits       | 198 ms                                                 | 189 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                      |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                       |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x slower                                                       |
| regex_v8       | 22.0 ms                                                | 25.6 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                       |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 99.7 ms: 1.04x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.0 us: 1.04x faster                                                      |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                      |
| pickle_list          | 4.11 us                                                | 4.21 us: 1.02x slower                                                      |
| xml_etree_process    | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                      |
| unpickle             | 13.7 us                                                | 14.5 us: 1.06x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.32 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 6.48 ms: 1.08x slower                                                      |
| python_startup         | 8.52 ms                                                | 9.51 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.7 ms: 1.09x faster                                                      |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                      |
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                      |
| django_template | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.45x faster                                                      |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.15 ms: 1.17x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                       |
| coroutines              | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                      |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                       |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                      |
| spectral_norm           | 100 ms                                                 | 90.6 ms: 1.10x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 996 us: 1.10x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.68 ms: 1.09x faster                                                      |
| coverage                | 100 ms                                                 | 91.6 ms: 1.09x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.40 sec: 1.09x faster                                                     |
| html5lib                | 64.5 ms                                                | 59.2 ms: 1.09x faster                                                      |
| json                    | 4.94 ms                                                | 4.54 ms: 1.09x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 47.7 ms: 1.09x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                       |
| logging_silent          | 101 ns                                                 | 93.4 ns: 1.08x faster                                                      |
| scimark_fft             | 328 ms                                                 | 304 ms: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| richards                | 45.7 ms                                                | 42.6 ms: 1.07x faster                                                      |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                                      |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                       |
| tornado_http            | 96.3 ms                                                | 90.9 ms: 1.06x faster                                                      |
| nbody                   | 93.1 ms                                                | 88.2 ms: 1.06x faster                                                      |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                      |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                       |
| float                   | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                      |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.05x faster                                                      |
| pidigits                | 198 ms                                                 | 189 ms: 1.04x faster                                                       |
| fannkuch                | 388 ms                                                 | 371 ms: 1.04x faster                                                       |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 99.7 ms: 1.04x faster                                                      |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                                       |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                       |
| pickle_dict             | 31.1 us                                                | 30.0 us: 1.04x faster                                                      |
| chaos                   | 69.2 ms                                                | 66.7 ms: 1.04x faster                                                      |
| async_tree_memoization  | 627 ms                                                 | 606 ms: 1.04x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.04x faster                                                       |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.37 ms: 1.03x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                      |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| nqueens                 | 83.4 ms                                                | 81.1 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                      |
| sympy_expand            | 475 ms                                                 | 464 ms: 1.02x faster                                                       |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 701 ms                                                 | 687 ms: 1.02x faster                                                       |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                       |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                      |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 67.0 ms: 1.02x faster                                                      |
| unpack_sequence         | 43.1 ns                                                | 42.8 ns: 1.01x faster                                                      |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.00x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.4 ms: 1.00x faster                                                      |
| regex_dna               | 204 ms                                                 | 204 ms: 1.00x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.30 sec: 1.01x slower                                                     |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                                      |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                      |
| pyflate                 | 418 ms                                                 | 423 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                      |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                                      |
| async_tree_none         | 526 ms                                                 | 535 ms: 1.02x slower                                                       |
| thrift                  | 756 us                                                 | 772 us: 1.02x slower                                                       |
| pickle_list             | 4.11 us                                                | 4.21 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 770 ms: 1.04x slower                                                       |
| xml_etree_process       | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.65 us: 1.05x slower                                                      |
| comprehensions          | 22.4 us                                                | 23.6 us: 1.05x slower                                                      |
| unpickle                | 13.7 us                                                | 14.5 us: 1.06x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.48 ms: 1.08x slower                                                      |
| unpickle_list           | 4.91 us                                                | 5.32 us: 1.08x slower                                                      |
| python_startup          | 8.52 ms                                                | 9.51 ms: 1.12x slower                                                      |
| async_generators        | 368 ms                                                 | 411 ms: 1.12x slower                                                       |
| regex_v8                | 22.0 ms                                                | 25.6 ms: 1.16x slower                                                      |
| dask                    | 360 ms                                                 | 503 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (8): pycparser, telco, sqlalchemy_imperative, create_gc_cycles, djangocms, bench_mp_pool, sqlglot_transpile, mypy2
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
