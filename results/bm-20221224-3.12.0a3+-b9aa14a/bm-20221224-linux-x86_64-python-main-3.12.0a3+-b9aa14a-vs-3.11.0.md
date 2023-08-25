
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9aa14a
- commit date: 2022-12-24
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.38 ms: 1.02x faster                                  |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                 |
| html5lib       | 64.5 ms                                                | 60.2 ms: 1.07x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.1 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 93.1 ms                                                | 96.5 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.40 ms: 1.17x faster                                  |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                  |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.42 ms: 1.34x faster                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                   |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| xml_etree_generate   | 76.2 ms                                                | 75.9 ms: 1.00x faster                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.03x slower                                  |
| pickle_list          | 4.11 us                                                | 4.25 us: 1.03x slower                                  |
| pickle_dict          | 31.1 us                                                | 32.4 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.49 ms: 1.00x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.08 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.0 ms: 1.06x faster                                  |
| mako            | 10.1 ms                                                | 9.59 ms: 1.05x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                  |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.42 ms: 1.34x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.40 ms: 1.17x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                   |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.13x faster                                   |
| deltablue               | 3.67 ms                                                | 3.27 ms: 1.12x faster                                  |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 33.4 us: 1.11x faster                                  |
| richards                | 45.7 ms                                                | 41.8 ms: 1.09x faster                                  |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                 |
| html5lib                | 64.5 ms                                                | 60.2 ms: 1.07x faster                                  |
| float                   | 77.2 ms                                                | 72.1 ms: 1.07x faster                                  |
| logging_silent          | 101 ns                                                 | 94.8 ns: 1.07x faster                                  |
| logging_simple          | 6.03 us                                                | 5.67 us: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| logging_format          | 6.68 us                                                | 6.29 us: 1.06x faster                                  |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.25 ms: 1.06x faster                                  |
| genshi_xml              | 51.8 ms                                                | 49.0 ms: 1.06x faster                                  |
| nqueens                 | 83.4 ms                                                | 79.1 ms: 1.05x faster                                  |
| telco                   | 6.58 ms                                                | 6.25 ms: 1.05x faster                                  |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                   |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                 |
| mako                    | 10.1 ms                                                | 9.59 ms: 1.05x faster                                  |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                  |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                   |
| spectral_norm           | 100 ms                                                 | 95.4 ms: 1.05x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 671 ms: 1.05x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.09 ms: 1.05x faster                                  |
| async_generators        | 368 ms                                                 | 353 ms: 1.05x faster                                   |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.9 ms: 1.04x faster                                  |
| json                    | 4.94 ms                                                | 4.74 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                   |
| scimark_fft             | 328 ms                                                 | 316 ms: 1.04x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.6 ms: 1.04x faster                                  |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                   |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                   |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                   |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                   |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                 |
| coroutines              | 25.5 ms                                                | 24.8 ms: 1.03x faster                                  |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                  |
| coverage                | 100 ms                                                 | 98.1 ms: 1.02x faster                                  |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                   |
| chameleon               | 6.47 ms                                                | 6.38 ms: 1.02x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                   |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                   |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                  |
| python_startup          | 8.52 ms                                                | 8.49 ms: 1.00x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.9 ms: 1.00x faster                                  |
| chaos                   | 69.2 ms                                                | 69.6 ms: 1.01x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 75.2 ms: 1.01x slower                                  |
| regex_dna               | 204 ms                                                 | 206 ms: 1.01x slower                                   |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.08 ms: 1.01x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 759 ms: 1.03x slower                                   |
| pickle                  | 10.1 us                                                | 10.3 us: 1.03x slower                                  |
| pickle_list             | 4.11 us                                                | 4.25 us: 1.03x slower                                  |
| nbody                   | 93.1 ms                                                | 96.5 ms: 1.04x slower                                  |
| pickle_dict             | 31.1 us                                                | 32.4 us: 1.04x slower                                  |
| generators              | 73.5 ms                                                | 77.6 ms: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (9): async_tree_memoization, djangocms, async_tree_none, sqlglot_parse, sqlglot_transpile, bench_mp_pool, unpickle_list, unpack_sequence, deepcopy_reduce
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221224-3.12.0a3+-b9aa14a/bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
