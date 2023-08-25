
# Results vs. 3.11.0

- fork: python
- ref: f533f216e6aaba3f3663
- machine: darwin-arm64
- commit hash: f533f21
- commit date: 2023-03-06
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.02x slower                                                   |
| chameleon      | 4.60 ms                                                | 4.57 ms: 1.01x faster                                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                 |
| html5lib       | 34.7 ms                                                | 35.5 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.7 ms: 1.03x faster                                                  |
| float          | 53.0 ms                                                | 53.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.02x faster                                                  |
| regex_v8       | 16.1 ms                                                | 16.5 ms: 1.02x slower                                                  |
| regex_effbot   | 2.63 ms                                                | 2.74 ms: 1.04x slower                                                  |
| regex_dna      | 152 ms                                                 | 159 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.19 ms: 1.23x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 97.7 ms: 1.11x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                                   |
| pickle_pure_python   | 201 us                                                 | 191 us: 1.05x faster                                                   |
| pickle_list          | 2.81 us                                                | 2.79 us: 1.01x faster                                                  |
| pickle_dict          | 18.0 us                                                | 18.0 us: 1.00x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 36.8 ms: 1.05x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 50.7 ms: 1.05x slower                                                  |
| pickle               | 7.15 us                                                | 7.54 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): unpickle, json_loads, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.4 ms: 1.00x faster                                                  |
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.46 ms: 1.14x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                  |
| django_template | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 465 ms: 1.40x faster                                                   |
| json_dumps              | 7.63 ms                                                | 6.19 ms: 1.23x faster                                                  |
| mako                    | 8.53 ms                                                | 7.46 ms: 1.14x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 97.7 ms: 1.11x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.10x faster                                                   |
| deltablue               | 2.81 ms                                                | 2.58 ms: 1.09x faster                                                  |
| hexiom                  | 4.72 ms                                                | 4.45 ms: 1.06x faster                                                  |
| richards                | 32.2 ms                                                | 30.6 ms: 1.05x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 191 us: 1.05x faster                                                   |
| unpack_sequence         | 34.1 ns                                                | 32.8 ns: 1.04x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                  |
| chaos                   | 49.4 ms                                                | 47.7 ms: 1.04x faster                                                  |
| mdp                     | 1.55 sec                                               | 1.49 sec: 1.03x faster                                                 |
| pycparser               | 698 ms                                                 | 678 ms: 1.03x faster                                                   |
| nbody                   | 65.6 ms                                                | 63.7 ms: 1.03x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                  |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.03x faster                                                  |
| generators              | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                  |
| scimark_fft             | 200 ms                                                 | 196 ms: 1.02x faster                                                   |
| regex_compile           | 76.7 ms                                                | 75.6 ms: 1.02x faster                                                  |
| create_gc_cycles        | 716 us                                                 | 705 us: 1.01x faster                                                   |
| fannkuch                | 261 ms                                                 | 258 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 470 us: 1.01x faster                                                   |
| pickle_list             | 2.81 us                                                | 2.79 us: 1.01x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.57 ms: 1.01x faster                                                  |
| meteor_contest          | 73.5 ms                                                | 73.1 ms: 1.01x faster                                                  |
| python_startup          | 12.4 ms                                                | 12.4 ms: 1.00x faster                                                  |
| pickle_dict             | 18.0 us                                                | 18.0 us: 1.00x slower                                                  |
| json                    | 2.78 ms                                                | 2.79 ms: 1.00x slower                                                  |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 26.5 us: 1.01x slower                                                  |
| telco                   | 3.41 ms                                                | 3.44 ms: 1.01x slower                                                  |
| deepcopy                | 223 us                                                 | 225 us: 1.01x slower                                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.29 ms: 1.01x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                                  |
| scimark_lu              | 73.3 ms                                                | 74.4 ms: 1.01x slower                                                  |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                 |
| float                   | 53.0 ms                                                | 53.8 ms: 1.02x slower                                                  |
| coroutines              | 17.8 ms                                                | 18.0 ms: 1.02x slower                                                  |
| go                      | 109 ms                                                 | 110 ms: 1.02x slower                                                   |
| async_tree_none         | 286 ms                                                 | 290 ms: 1.02x slower                                                   |
| pathlib                 | 27.2 ms                                                | 27.7 ms: 1.02x slower                                                  |
| sympy_str               | 151 ms                                                 | 154 ms: 1.02x slower                                                   |
| sympy_expand            | 242 ms                                                 | 247 ms: 1.02x slower                                                   |
| 2to3                    | 161 ms                                                 | 165 ms: 1.02x slower                                                   |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| regex_v8                | 16.1 ms                                                | 16.5 ms: 1.02x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 64.0 ms: 1.02x slower                                                  |
| html5lib                | 34.7 ms                                                | 35.5 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                   |
| pprint_pformat          | 954 ms                                                 | 978 ms: 1.03x slower                                                   |
| sympy_sum               | 85.5 ms                                                | 87.8 ms: 1.03x slower                                                  |
| coverage                | 58.4 ms                                                | 60.0 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 549 ms: 1.03x slower                                                   |
| django_template         | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.2 ms: 1.03x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 480 ms: 1.03x slower                                                   |
| logging_simple          | 3.55 us                                                | 3.66 us: 1.03x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 75.0 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 32.2 ms: 1.03x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.98 us: 1.04x slower                                                  |
| regex_effbot            | 2.63 ms                                                | 2.74 ms: 1.04x slower                                                  |
| logging_format          | 3.78 us                                                | 3.94 us: 1.04x slower                                                  |
| thrift                  | 442 us                                                 | 461 us: 1.04x slower                                                   |
| regex_dna               | 152 ms                                                 | 159 ms: 1.05x slower                                                   |
| xml_etree_process       | 35.1 ms                                                | 36.8 ms: 1.05x slower                                                  |
| bench_mp_pool           | 43.9 ms                                                | 46.1 ms: 1.05x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 50.7 ms: 1.05x slower                                                  |
| pickle                  | 7.15 us                                                | 7.54 us: 1.06x slower                                                  |
| async_tree_io           | 704 ms                                                 | 744 ms: 1.06x slower                                                   |
| nqueens                 | 59.8 ms                                                | 63.3 ms: 1.06x slower                                                  |
| scimark_sor             | 82.6 ms                                                | 88.0 ms: 1.07x slower                                                  |
| pyflate                 | 310 ms                                                 | 331 ms: 1.07x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.38 us: 1.08x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.22 ms: 1.09x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 50.7 ms: 1.09x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.05 ms: 1.10x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.8 us: 1.10x slower                                                  |
| raytrace                | 207 ms                                                 | 228 ms: 1.10x slower                                                   |
| mypy2                   | 195 ms                                                 | 262 ms: 1.34x slower                                                   |
| async_generators        | 196 ms                                                 | 270 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (8): tornado_http, unpickle, logging_silent, json_loads, pidigits, unpickle_list, async_tree_memoization, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230306-3.12.0a5+-f533f21/bm-20230306-darwin-arm64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21.json: dask


# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
