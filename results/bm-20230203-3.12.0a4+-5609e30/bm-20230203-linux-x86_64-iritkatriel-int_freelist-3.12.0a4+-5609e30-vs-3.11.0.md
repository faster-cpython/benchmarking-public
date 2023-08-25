
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.21 ms: 1.04x faster                                               |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 59.9 ms: 1.08x faster                                               |
| tornado_http   | 96.3 ms                                                | 93.6 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.1 ms: 1.06x faster                                               |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                |
| nbody          | 93.1 ms                                                | 96.7 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| regex_effbot   | 3.99 ms                                                | 3.77 ms: 1.06x faster                                               |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                               |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.41 ms: 1.34x faster                                               |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                |
| json_loads           | 26.5 us                                                | 23.4 us: 1.13x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 145 ms: 1.09x faster                                                |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                               |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                               |
| pickle_list          | 4.11 us                                                | 4.22 us: 1.03x slower                                               |
| unpickle_list        | 4.91 us                                                | 5.15 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.5 ms: 1.09x faster                                               |
| mako            | 10.1 ms                                                | 9.47 ms: 1.07x faster                                               |
| django_template | 32.6 ms                                                | 32.1 ms: 1.02x faster                                               |
| genshi_text     | 21.6 ms                                                | 21.3 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 492 ms: 1.87x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.41 ms: 1.34x faster                                               |
| deltablue               | 3.67 ms                                                | 3.18 ms: 1.16x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                |
| json_loads              | 26.5 us                                                | 23.4 us: 1.13x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.04 ms: 1.11x faster                                               |
| aiohttp                 | 1.10 ms                                                | 995 us: 1.11x faster                                                |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                               |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 145 ms: 1.09x faster                                                |
| genshi_xml              | 51.8 ms                                                | 47.5 ms: 1.09x faster                                               |
| logging_silent          | 101 ns                                                 | 92.8 ns: 1.09x faster                                               |
| chaos                   | 69.2 ms                                                | 63.7 ms: 1.09x faster                                               |
| nqueens                 | 83.4 ms                                                | 77.2 ms: 1.08x faster                                               |
| scimark_fft             | 328 ms                                                 | 304 ms: 1.08x faster                                                |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                               |
| html5lib                | 64.5 ms                                                | 59.9 ms: 1.08x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.93 ms: 1.07x faster                                               |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                               |
| mako                    | 10.1 ms                                                | 9.47 ms: 1.07x faster                                               |
| logging_simple          | 6.03 us                                                | 5.67 us: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.77 ms: 1.06x faster                                               |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                |
| float                   | 77.2 ms                                                | 73.1 ms: 1.06x faster                                               |
| coroutines              | 25.5 ms                                                | 24.1 ms: 1.06x faster                                               |
| coverage                | 100 ms                                                 | 94.8 ms: 1.06x faster                                               |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                                |
| bench_thread_pool       | 819 us                                                 | 777 us: 1.05x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                              |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                |
| async_generators        | 368 ms                                                 | 353 ms: 1.04x faster                                                |
| chameleon               | 6.47 ms                                                | 6.21 ms: 1.04x faster                                               |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                              |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                              |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                               |
| sqlglot_optimize        | 53.1 ms                                                | 51.1 ms: 1.04x faster                                               |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                |
| spectral_norm           | 100 ms                                                 | 96.6 ms: 1.04x faster                                               |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                |
| tornado_http            | 96.3 ms                                                | 93.6 ms: 1.03x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                               |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.03x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.93 ms: 1.02x faster                                               |
| thrift                  | 756 us                                                 | 740 us: 1.02x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pyflate                 | 418 ms                                                 | 410 ms: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| dulwich_log             | 63.7 ms                                                | 62.4 ms: 1.02x faster                                               |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                |
| django_template         | 32.6 ms                                                | 32.1 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 67.0 ms: 1.02x faster                                               |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                               |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                               |
| sqlite_synth            | 2.52 us                                                | 2.54 us: 1.01x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                               |
| crypto_pyaes            | 74.7 ms                                                | 76.1 ms: 1.02x slower                                               |
| pickle_dict             | 31.1 us                                                | 31.8 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 754 ms: 1.02x slower                                                |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                              |
| pickle_list             | 4.11 us                                                | 4.22 us: 1.03x slower                                               |
| nbody                   | 93.1 ms                                                | 96.7 ms: 1.04x slower                                               |
| unpickle_list           | 4.91 us                                                | 5.15 us: 1.05x slower                                               |
| async_tree_memoization  | 627 ms                                                 | 660 ms: 1.05x slower                                                |
| python_startup          | 8.52 ms                                                | 8.97 ms: 1.05x slower                                               |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                               |
| regex_dna               | 204 ms                                                 | 217 ms: 1.06x slower                                                |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                               |
| dask                    | 360 ms                                                 | 494 ms: 1.37x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (6): unpack_sequence, async_tree_none, bench_mp_pool, sqlglot_parse, djangocms, pickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230203-3.12.0a4+-5609e30/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
