
# Results vs. 3.11.0

- fork: python
- ref: a7715ccfba5b86ab09f8
- machine: linux-x86_64
- commit hash: a7715cc
- commit date: 2022-12-21
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                  |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| html5lib       | 64.5 ms                                                | 59.5 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.8 ms: 1.08x faster                                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                  |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                  |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                   |
| json_loads           | 26.5 us                                                | 23.6 us: 1.12x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                   |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                                  |
| pickle_list          | 4.11 us                                                | 3.98 us: 1.03x faster                                                  |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.43 ms: 1.01x faster                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.09 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.6 ms: 1.09x faster                                                  |
| mako            | 10.1 ms                                                | 9.47 ms: 1.07x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.4 ms: 1.05x faster                                                  |
| django_template | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                  |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.12x faster                                                   |
| json_loads              | 26.5 us                                                | 23.6 us: 1.12x faster                                                  |
| logging_silent          | 101 ns                                                 | 90.4 ns: 1.12x faster                                                  |
| richards                | 45.7 ms                                                | 41.4 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.10 ms: 1.10x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 47.6 ms: 1.09x faster                                                  |
| html5lib                | 64.5 ms                                                | 59.5 ms: 1.09x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                   |
| float                   | 77.2 ms                                                | 71.8 ms: 1.08x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                                 |
| logging_format          | 6.68 us                                                | 6.22 us: 1.07x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                                 |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                  |
| mako                    | 10.1 ms                                                | 9.47 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.68 us: 1.06x faster                                                  |
| nqueens                 | 83.4 ms                                                | 78.5 ms: 1.06x faster                                                  |
| pprint_safe_repr        | 701 ms                                                 | 661 ms: 1.06x faster                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 64.2 ms: 1.06x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.1 ms: 1.06x faster                                                  |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                   |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                                  |
| spectral_norm           | 100 ms                                                 | 94.8 ms: 1.06x faster                                                  |
| pyflate                 | 418 ms                                                 | 396 ms: 1.05x faster                                                   |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                                   |
| telco                   | 6.58 ms                                                | 6.29 ms: 1.05x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                                   |
| unpack_sequence         | 43.1 ns                                                | 41.3 ns: 1.04x faster                                                  |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                                  |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                  |
| async_generators        | 368 ms                                                 | 356 ms: 1.04x faster                                                   |
| sympy_str               | 290 ms                                                 | 280 ms: 1.03x faster                                                   |
| pickle_list             | 4.11 us                                                | 3.98 us: 1.03x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                 |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| thrift                  | 756 us                                                 | 741 us: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                  |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                                  |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.6 ms: 1.02x faster                                                  |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.02x faster                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                  |
| python_startup          | 8.52 ms                                                | 8.43 ms: 1.01x faster                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.01x faster                                                  |
| chaos                   | 69.2 ms                                                | 68.7 ms: 1.01x faster                                                  |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| django_template         | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.4 ms: 1.00x faster                                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                   |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.09 ms: 1.01x slower                                                  |
| async_tree_none         | 526 ms                                                 | 535 ms: 1.02x slower                                                   |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 644 ms: 1.03x slower                                                   |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 765 ms: 1.04x slower                                                   |
| generators              | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (3): nbody, bench_mp_pool, unpickle_list
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.12.0a3+-a7715cc/bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
