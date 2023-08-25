
# Results vs. 3.11.0

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: linux-x86_64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                                         |
| chameleon      | 7.67 ms                                                      | 6.83 ms: 1.12x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                                       |
| html5lib       | 72.9 ms                                                      | 67.1 ms: 1.09x faster                                                        |
| tornado_http   | 122 ms                                                       | 117 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 72.5 ms: 1.02x faster                                                        |
| nbody          | 90.7 ms                                                      | 94.5 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 147 ms: 1.07x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.31 ms: 1.06x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| regex_dna      | 227 ms                                                       | 222 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.33x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.1 us: 1.19x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.17x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 144 ms: 1.10x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 310 us: 1.03x faster                                                         |
| unpickle_list        | 4.53 us                                                      | 4.43 us: 1.02x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.2 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                                         |
| pickle               | 9.64 us                                                      | 9.80 us: 1.02x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 31.3 us: 1.02x slower                                                        |
| pickle_list          | 3.83 us                                                      | 3.92 us: 1.02x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.2 ms: 1.03x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 84.2 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.87 ms: 1.11x faster                                                        |
| genshi_xml      | 58.5 ms                                                      | 55.8 ms: 1.05x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 25.1 ms: 1.04x faster                                                        |
| django_template | 40.2 ms                                                      | 41.1 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 387 ms: 1.94x faster                                                         |
| generators              | 56.0 ms                                                      | 38.6 ms: 1.45x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.1 ms: 1.33x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.35 ms: 1.19x faster                                                        |
| json_loads              | 28.7 us                                                      | 24.1 us: 1.19x faster                                                        |
| mypy2                   | 451 ms                                                       | 381 ms: 1.19x faster                                                         |
| unpickle_pure_python    | 241 us                                                       | 205 us: 1.17x faster                                                         |
| chaos                   | 80.9 ms                                                      | 71.0 ms: 1.14x faster                                                        |
| json                    | 5.65 ms                                                      | 4.98 ms: 1.13x faster                                                        |
| coroutines              | 27.6 ms                                                      | 24.4 ms: 1.13x faster                                                        |
| chameleon               | 7.67 ms                                                      | 6.83 ms: 1.12x faster                                                        |
| mako                    | 11.0 ms                                                      | 9.87 ms: 1.11x faster                                                        |
| scimark_lu              | 115 ms                                                       | 104 ms: 1.10x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 144 ms: 1.10x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 6.53 ms: 1.09x faster                                                        |
| go                      | 164 ms                                                       | 150 ms: 1.09x faster                                                         |
| html5lib                | 72.9 ms                                                      | 67.1 ms: 1.09x faster                                                        |
| regex_compile           | 158 ms                                                       | 147 ms: 1.07x faster                                                         |
| raytrace                | 317 ms                                                       | 298 ms: 1.06x faster                                                         |
| fannkuch                | 429 ms                                                       | 404 ms: 1.06x faster                                                         |
| deepcopy_memo           | 38.8 us                                                      | 36.6 us: 1.06x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.31 ms: 1.06x faster                                                        |
| logging_silent          | 101 ns                                                       | 95.3 ns: 1.06x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                         |
| dulwich_log             | 68.4 ms                                                      | 65.0 ms: 1.05x faster                                                        |
| genshi_xml              | 58.5 ms                                                      | 55.8 ms: 1.05x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| richards                | 48.3 ms                                                      | 46.4 ms: 1.04x faster                                                        |
| genshi_text             | 26.1 ms                                                      | 25.1 ms: 1.04x faster                                                        |
| meteor_contest          | 131 ms                                                       | 126 ms: 1.04x faster                                                         |
| pycparser               | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                                       |
| tornado_http            | 122 ms                                                       | 117 ms: 1.04x faster                                                         |
| nqueens                 | 103 ms                                                       | 99.1 ms: 1.04x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.57 sec: 1.04x faster                                                       |
| pyflate                 | 449 ms                                                       | 434 ms: 1.03x faster                                                         |
| pprint_safe_repr        | 784 ms                                                       | 759 ms: 1.03x faster                                                         |
| pickle_pure_python      | 319 us                                                       | 310 us: 1.03x faster                                                         |
| scimark_sor             | 111 ms                                                       | 108 ms: 1.03x faster                                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.89 us: 1.03x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 985 us: 1.03x faster                                                         |
| async_tree_memoization  | 630 ms                                                       | 615 ms: 1.02x faster                                                         |
| float                   | 74.2 ms                                                      | 72.5 ms: 1.02x faster                                                        |
| unpickle_list           | 4.53 us                                                      | 4.43 us: 1.02x faster                                                        |
| regex_dna               | 227 ms                                                       | 222 ms: 1.02x faster                                                         |
| unpickle                | 13.4 us                                                      | 13.2 us: 1.02x faster                                                        |
| pathlib                 | 19.1 ms                                                      | 18.8 ms: 1.02x faster                                                        |
| sympy_expand            | 555 ms                                                       | 546 ms: 1.02x faster                                                         |
| scimark_fft             | 285 ms                                                       | 281 ms: 1.02x faster                                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.4 ms: 1.02x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.71 sec: 1.01x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                                       |
| deepcopy_reduce         | 3.51 us                                                      | 3.47 us: 1.01x faster                                                        |
| logging_simple          | 7.19 us                                                      | 7.11 us: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.01x faster                                                         |
| 2to3                    | 288 ms                                                       | 285 ms: 1.01x faster                                                         |
| sympy_str               | 337 ms                                                       | 336 ms: 1.00x faster                                                         |
| telco                   | 6.86 ms                                                      | 6.83 ms: 1.00x faster                                                        |
| coverage                | 84.8 ms                                                      | 85.2 ms: 1.00x slower                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.18 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 756 ms: 1.01x slower                                                         |
| crypto_pyaes            | 83.4 ms                                                      | 84.8 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.95 ms: 1.02x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.80 us: 1.02x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.3 us: 1.02x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.4 ms: 1.02x slower                                                        |
| sympy_sum               | 185 ms                                                       | 188 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.13 ms: 1.02x slower                                                        |
| thrift                  | 925 us                                                       | 945 us: 1.02x slower                                                         |
| django_template         | 40.2 ms                                                      | 41.1 ms: 1.02x slower                                                        |
| pickle_list             | 3.83 us                                                      | 3.92 us: 1.02x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.57 us: 1.03x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 58.2 ms: 1.03x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 96.4 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.58 ms: 1.03x slower                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.99 ms: 1.04x slower                                                        |
| nbody                   | 90.7 ms                                                      | 94.5 ms: 1.04x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.68 ms: 1.04x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 84.2 ms: 1.05x slower                                                        |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| bench_mp_pool           | 4.62 ms                                                      | 4.96 ms: 1.07x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                        |
| comprehensions          | 24.6 us                                                      | 27.4 us: 1.11x slower                                                        |
| async_generators        | 316 ms                                                       | 393 ms: 1.25x slower                                                         |
| dask                    | 410 ms                                                       | 563 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): unpack_sequence, deepcopy, pidigits, async_tree_none
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
