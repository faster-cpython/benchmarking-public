
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 6b312e0
- commit date: 2023-02-03
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.28 ms: 1.03x faster                                               |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 59.5 ms: 1.09x faster                                               |
| tornado_http   | 96.3 ms                                                | 94.0 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.5 ms: 1.07x faster                                               |
| pidigits       | 198 ms                                                 | 191 ms: 1.04x faster                                                |
| nbody          | 93.1 ms                                                | 96.7 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                               |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                |
| regex_v8       | 22.0 ms                                                | 22.6 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.52 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                |
| pickle_list          | 4.11 us                                                | 3.92 us: 1.05x faster                                               |
| unpickle             | 13.7 us                                                | 13.1 us: 1.05x faster                                               |
| pickle_dict          | 31.1 us                                                | 29.8 us: 1.04x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.48 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.9 ms: 1.08x faster                                               |
| mako            | 10.1 ms                                                | 9.58 ms: 1.05x faster                                               |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                               |
| django_template | 32.6 ms                                                | 32.3 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 496 ms: 1.86x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.52 ms: 1.32x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.44 ms: 1.16x faster                                               |
| deltablue               | 3.67 ms                                                | 3.18 ms: 1.15x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.52 ms: 1.14x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.98 ms: 1.13x faster                                               |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                               |
| aiohttp                 | 1.10 ms                                                | 995 us: 1.11x faster                                                |
| nqueens                 | 83.4 ms                                                | 75.8 ms: 1.10x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                               |
| richards                | 45.7 ms                                                | 41.8 ms: 1.09x faster                                               |
| logging_silent          | 101 ns                                                 | 92.7 ns: 1.09x faster                                               |
| chaos                   | 69.2 ms                                                | 63.5 ms: 1.09x faster                                               |
| html5lib                | 64.5 ms                                                | 59.5 ms: 1.09x faster                                               |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                                |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                               |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                |
| genshi_xml              | 51.8 ms                                                | 47.9 ms: 1.08x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.94 ms: 1.07x faster                                               |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                              |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                |
| async_generators        | 368 ms                                                 | 346 ms: 1.07x faster                                                |
| float                   | 77.2 ms                                                | 72.5 ms: 1.07x faster                                               |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                               |
| logging_format          | 6.68 us                                                | 6.28 us: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                               |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                              |
| logging_simple          | 6.03 us                                                | 5.70 us: 1.06x faster                                               |
| deepcopy                | 342 us                                                 | 324 us: 1.06x faster                                                |
| mako                    | 10.1 ms                                                | 9.58 ms: 1.05x faster                                               |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| pickle_list             | 4.11 us                                                | 3.92 us: 1.05x faster                                               |
| unpickle                | 13.7 us                                                | 13.1 us: 1.05x faster                                               |
| bench_thread_pool       | 819 us                                                 | 784 us: 1.04x faster                                                |
| pickle_dict             | 31.1 us                                                | 29.8 us: 1.04x faster                                               |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                               |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                              |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| pidigits                | 198 ms                                                 | 191 ms: 1.04x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                               |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                                |
| chameleon               | 6.47 ms                                                | 6.28 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| tornado_http            | 96.3 ms                                                | 94.0 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 66.5 ms: 1.02x faster                                               |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| deepcopy_reduce         | 2.94 us                                                | 2.88 us: 1.02x faster                                               |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                |
| thrift                  | 756 us                                                 | 747 us: 1.01x faster                                                |
| pyflate                 | 418 ms                                                 | 414 ms: 1.01x faster                                                |
| django_template         | 32.6 ms                                                | 32.3 ms: 1.01x faster                                               |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                               |
| generators              | 73.5 ms                                                | 74.5 ms: 1.01x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                |
| coroutines              | 25.5 ms                                                | 26.0 ms: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                              |
| unpickle_list           | 4.91 us                                                | 5.02 us: 1.02x slower                                               |
| crypto_pyaes            | 74.7 ms                                                | 76.4 ms: 1.02x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.6 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 760 ms: 1.03x slower                                                |
| spectral_norm           | 100 ms                                                 | 103 ms: 1.03x slower                                                |
| nbody                   | 93.1 ms                                                | 96.7 ms: 1.04x slower                                               |
| async_tree_memoization  | 627 ms                                                 | 652 ms: 1.04x slower                                                |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.48 ms: 1.08x slower                                               |
| unpack_sequence         | 43.1 ns                                                | 46.9 ns: 1.09x slower                                               |
| dask                    | 360 ms                                                 | 499 ms: 1.39x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (7): djangocms, pickle, sqlglot_parse, coverage, bench_mp_pool, sqlite_synth, async_tree_none
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230203-3.12.0a4+-6b312e0/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
