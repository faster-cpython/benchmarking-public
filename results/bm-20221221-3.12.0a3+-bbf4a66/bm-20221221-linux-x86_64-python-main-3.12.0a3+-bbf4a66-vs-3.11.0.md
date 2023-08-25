
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bbf4a66
- commit date: 2022-12-21
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.35 ms: 1.02x faster                                  |
| docutils       | 2.63 sec                                               | 2.49 sec: 1.05x faster                                 |
| html5lib       | 64.5 ms                                                | 59.2 ms: 1.09x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.9 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nbody          | 93.1 ms                                                | 94.4 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                  |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.49 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                   |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.08x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 54.2 ms: 1.01x slower                                  |
| pickle_list          | 4.11 us                                                | 4.17 us: 1.01x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.41 ms: 1.01x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.07 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.3 ms: 1.12x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.0 ms: 1.08x faster                                  |
| mako            | 10.1 ms                                                | 9.46 ms: 1.07x faster                                  |
| django_template | 32.6 ms                                                | 32.3 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.49 ms: 1.33x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.47 ms: 1.15x faster                                  |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                  |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                   |
| genshi_xml              | 51.8 ms                                                | 46.3 ms: 1.12x faster                                  |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.10 ms: 1.10x faster                                  |
| richards                | 45.7 ms                                                | 41.7 ms: 1.10x faster                                  |
| html5lib                | 64.5 ms                                                | 59.2 ms: 1.09x faster                                  |
| logging_silent          | 101 ns                                                 | 93.0 ns: 1.09x faster                                  |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                 |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.08x faster                                   |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                  |
| genshi_text             | 21.6 ms                                                | 20.0 ms: 1.08x faster                                  |
| float                   | 77.2 ms                                                | 71.9 ms: 1.07x faster                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                   |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                   |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                   |
| spectral_norm           | 100 ms                                                 | 93.6 ms: 1.07x faster                                  |
| mako                    | 10.1 ms                                                | 9.46 ms: 1.07x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 49.9 ms: 1.06x faster                                  |
| sympy_expand            | 475 ms                                                 | 447 ms: 1.06x faster                                   |
| nqueens                 | 83.4 ms                                                | 78.6 ms: 1.06x faster                                  |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                  |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                   |
| pyflate                 | 418 ms                                                 | 395 ms: 1.06x faster                                   |
| telco                   | 6.58 ms                                                | 6.23 ms: 1.06x faster                                  |
| bench_thread_pool       | 819 us                                                 | 775 us: 1.06x faster                                   |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                  |
| docutils                | 2.63 sec                                               | 2.49 sec: 1.05x faster                                 |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                 |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                   |
| sympy_str               | 290 ms                                                 | 277 ms: 1.05x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.09 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                  |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                 |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.04x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                   |
| chaos                   | 69.2 ms                                                | 66.6 ms: 1.04x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 675 ms: 1.04x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                  |
| sympy_sum               | 167 ms                                                 | 161 ms: 1.04x faster                                   |
| async_generators        | 368 ms                                                 | 356 ms: 1.04x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.6 ms: 1.03x faster                                  |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.88 us: 1.02x faster                                  |
| chameleon               | 6.47 ms                                                | 6.35 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| thrift                  | 756 us                                                 | 744 us: 1.02x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.38 ms: 1.01x faster                                  |
| python_startup          | 8.52 ms                                                | 8.41 ms: 1.01x faster                                  |
| django_template         | 32.6 ms                                                | 32.3 ms: 1.01x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 54.2 ms: 1.01x slower                                  |
| coroutines              | 25.5 ms                                                | 25.8 ms: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.07 ms: 1.01x slower                                  |
| nbody                   | 93.1 ms                                                | 94.4 ms: 1.01x slower                                  |
| pickle_list             | 4.11 us                                                | 4.17 us: 1.01x slower                                  |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                   |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                  |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                 |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 763 ms: 1.03x slower                                   |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                   |
| generators              | 73.5 ms                                                | 78.3 ms: 1.07x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (5): bench_mp_pool, crypto_pyaes, unpack_sequence, coverage, unpickle
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.12.0a3+-bbf4a66/bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
