
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.02x faster \*
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                               |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 61.6 ms: 1.05x faster                                               |
| tornado_http   | 96.3 ms                                                | 95.3 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.8 ms: 1.05x faster                                               |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                |
| nbody          | 93.1 ms                                                | 96.3 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                               |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                                |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                               |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.50 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| json_loads           | 26.5 us                                                | 24.7 us: 1.07x faster                                               |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 53.6 ms: 1.00x faster                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                               |
| unpickle             | 13.7 us                                                | 14.0 us: 1.03x slower                                               |
| pickle_list          | 4.11 us                                                | 4.23 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.4 ms: 1.09x faster                                               |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.04x faster                                               |
| mako            | 10.1 ms                                                | 9.80 ms: 1.03x faster                                               |
| django_template | 32.6 ms                                                | 33.1 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 498 ms: 1.85x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.50 ms: 1.32x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.47 ms: 1.15x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                               |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.09x faster                                               |
| nqueens                 | 83.4 ms                                                | 76.2 ms: 1.09x faster                                               |
| logging_silent          | 101 ns                                                 | 92.4 ns: 1.09x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                               |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| fannkuch                | 388 ms                                                 | 360 ms: 1.08x faster                                                |
| chaos                   | 69.2 ms                                                | 64.4 ms: 1.07x faster                                               |
| json_loads              | 26.5 us                                                | 24.7 us: 1.07x faster                                               |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                |
| sympy_str               | 290 ms                                                 | 271 ms: 1.07x faster                                                |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.07x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                              |
| deepcopy_memo           | 37.0 us                                                | 34.9 us: 1.06x faster                                               |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                               |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                              |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.06x faster                                               |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                               |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                               |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| pprint_safe_repr        | 701 ms                                                 | 669 ms: 1.05x faster                                                |
| html5lib                | 64.5 ms                                                | 61.6 ms: 1.05x faster                                               |
| float                   | 77.2 ms                                                | 73.8 ms: 1.05x faster                                               |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                               |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.04x faster                                               |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                               |
| logging_simple          | 6.03 us                                                | 5.79 us: 1.04x faster                                               |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                                |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.03x faster                                              |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                                |
| mako                    | 10.1 ms                                                | 9.80 ms: 1.03x faster                                               |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                |
| scimark_monte_carlo     | 68.1 ms                                                | 66.4 ms: 1.02x faster                                               |
| telco                   | 6.58 ms                                                | 6.43 ms: 1.02x faster                                               |
| bench_thread_pool       | 819 us                                                 | 801 us: 1.02x faster                                                |
| raytrace                | 297 ms                                                 | 291 ms: 1.02x faster                                                |
| chameleon               | 6.47 ms                                                | 6.37 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| tornado_http            | 96.3 ms                                                | 95.3 ms: 1.01x faster                                               |
| unpack_sequence         | 43.1 ns                                                | 42.7 ns: 1.01x faster                                               |
| coroutines              | 25.5 ms                                                | 25.3 ms: 1.01x faster                                               |
| thrift                  | 756 us                                                 | 751 us: 1.01x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                               |
| xml_etree_process       | 53.9 ms                                                | 53.6 ms: 1.00x faster                                               |
| dulwich_log             | 63.7 ms                                                | 64.4 ms: 1.01x slower                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.55 ms: 1.01x slower                                               |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.01x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.4 ms: 1.02x slower                                               |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                |
| pickle_dict             | 31.1 us                                                | 31.8 us: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                              |
| unpickle                | 13.7 us                                                | 14.0 us: 1.03x slower                                               |
| deepcopy_reduce         | 2.94 us                                                | 3.02 us: 1.03x slower                                               |
| pickle_list             | 4.11 us                                                | 4.23 us: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 761 ms: 1.03x slower                                                |
| nbody                   | 93.1 ms                                                | 96.3 ms: 1.03x slower                                               |
| pathlib                 | 18.2 ms                                                | 18.9 ms: 1.04x slower                                               |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                                |
| sqlglot_transpile       | 1.70 ms                                                | 1.78 ms: 1.05x slower                                               |
| async_tree_memoization  | 627 ms                                                 | 659 ms: 1.05x slower                                                |
| python_startup          | 8.52 ms                                                | 8.97 ms: 1.05x slower                                               |
| sqlglot_parse           | 1.40 ms                                                | 1.48 ms: 1.06x slower                                               |
| sqlite_synth            | 2.52 us                                                | 2.68 us: 1.06x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                               |
| pyflate                 | 418 ms                                                 | 461 ms: 1.10x slower                                                |
| generators              | 73.5 ms                                                | 83.5 ms: 1.14x slower                                               |
| scimark_fft             | 328 ms                                                 | 390 ms: 1.19x slower                                                |
| crypto_pyaes            | 74.7 ms                                                | 90.0 ms: 1.20x slower                                               |
| spectral_norm           | 100 ms                                                 | 138 ms: 1.38x slower                                                |
| dask                    | 360 ms                                                 | 525 ms: 1.46x slower                                                |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (6): bench_mp_pool, async_generators, async_tree_none, unpickle_list, djangocms, pickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230131-3.12.0a4+-8a6e6a3/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3.json: mypy


# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
