
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: linux-x86_64
- commit hash: 47a7094
- commit date: 2023-04-06
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                             |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                            |
| html5lib       | 64.5 ms                                                | 61.2 ms: 1.05x faster                                                             |
| tornado_http   | 96.3 ms                                                | 90.3 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 83.6 ms: 1.11x faster                                                             |
| float          | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                             |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                             |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                                              |
| regex_v8       | 22.0 ms                                                | 22.6 ms: 1.02x slower                                                             |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                                              |
| json_loads           | 26.5 us                                                | 24.5 us: 1.08x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                              |
| pickle_pure_python   | 306 us                                                 | 292 us: 1.05x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 99.4 ms: 1.05x faster                                                             |
| unpickle_list        | 4.91 us                                                | 4.87 us: 1.01x faster                                                             |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                             |
| pickle_dict          | 31.1 us                                                | 32.3 us: 1.04x slower                                                             |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.43 us: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.87 ms: 1.04x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.55 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.3 ms: 1.09x faster                                                             |
| genshi_text     | 21.6 ms                                                | 21.1 ms: 1.02x faster                                                             |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                             |
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                             |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.20 ms: 1.17x faster                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.48 ms: 1.15x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.01 ms: 1.12x faster                                                             |
| nbody                   | 93.1 ms                                                | 83.6 ms: 1.11x faster                                                             |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 33.6 us: 1.10x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 47.3 ms: 1.09x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.5 us: 1.08x faster                                                             |
| logging_silent          | 101 ns                                                 | 93.5 ns: 1.08x faster                                                             |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                                              |
| raytrace                | 297 ms                                                 | 275 ms: 1.08x faster                                                              |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                              |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                             |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                              |
| spectral_norm           | 100 ms                                                 | 93.2 ms: 1.07x faster                                                             |
| chaos                   | 69.2 ms                                                | 64.7 ms: 1.07x faster                                                             |
| tornado_http            | 96.3 ms                                                | 90.3 ms: 1.07x faster                                                             |
| float                   | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                             |
| richards                | 45.7 ms                                                | 43.1 ms: 1.06x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                                             |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.06x faster                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 50.3 ms: 1.06x faster                                                             |
| deepcopy                | 342 us                                                 | 324 us: 1.06x faster                                                              |
| html5lib                | 64.5 ms                                                | 61.2 ms: 1.05x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.05 ms: 1.05x faster                                                             |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.05x faster                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                            |
| nqueens                 | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 292 us: 1.05x faster                                                              |
| comprehensions          | 22.4 us                                                | 21.4 us: 1.05x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 99.4 ms: 1.05x faster                                                             |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                                              |
| pprint_safe_repr        | 701 ms                                                 | 671 ms: 1.04x faster                                                              |
| json                    | 4.94 ms                                                | 4.73 ms: 1.04x faster                                                             |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                            |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                              |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                              |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                            |
| async_tree_memoization  | 627 ms                                                 | 605 ms: 1.04x faster                                                              |
| coverage                | 100 ms                                                 | 96.6 ms: 1.04x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 65.7 ms: 1.04x faster                                                             |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 715 ms: 1.03x faster                                                              |
| go                      | 140 ms                                                 | 135 ms: 1.03x faster                                                              |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                             |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                              |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                              |
| async_tree_none         | 526 ms                                                 | 512 ms: 1.03x faster                                                              |
| unpack_sequence         | 43.1 ns                                                | 42.1 ns: 1.02x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                                            |
| genshi_text             | 21.6 ms                                                | 21.1 ms: 1.02x faster                                                             |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                             |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                             |
| telco                   | 6.58 ms                                                | 6.48 ms: 1.02x faster                                                             |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                             |
| mako                    | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                             |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                              |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                             |
| unpickle_list           | 4.91 us                                                | 4.87 us: 1.01x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                             |
| pyflate                 | 418 ms                                                 | 416 ms: 1.01x faster                                                              |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                             |
| regex_v8                | 22.0 ms                                                | 22.6 ms: 1.02x slower                                                             |
| mdp                     | 2.62 sec                                               | 2.68 sec: 1.03x slower                                                            |
| pickle_dict             | 31.1 us                                                | 32.3 us: 1.04x slower                                                             |
| thrift                  | 756 us                                                 | 787 us: 1.04x slower                                                              |
| python_startup          | 8.52 ms                                                | 8.87 ms: 1.04x slower                                                             |
| gc_traversal            | 4.02 ms                                                | 4.19 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.05x slower                                                             |
| regex_dna               | 204 ms                                                 | 214 ms: 1.05x slower                                                              |
| pickle                  | 10.1 us                                                | 10.6 us: 1.05x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.43 us: 1.08x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.55 ms: 1.09x slower                                                             |
| async_generators        | 368 ms                                                 | 409 ms: 1.11x slower                                                              |
| dask                    | 360 ms                                                 | 499 ms: 1.39x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                      |

Benchmark hidden because not significant (7): unpickle, djangocms, crypto_pyaes, deepcopy_reduce, bench_mp_pool, pathlib, sqlalchemy_declarative
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
