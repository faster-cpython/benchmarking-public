
# Results vs. 3.11.0

- fork: python
- ref: f9774e57d84162ff0cba
- machine: darwin-arm64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.02x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.48 ms: 1.03x faster                                                 |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 35.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 53.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.01x slower                                                 |
| regex_dna      | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.18 ms: 1.23x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 97.9 ms: 1.10x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 191 us: 1.05x faster                                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 71.1 ms: 1.01x slower                                                 |
| pickle               | 7.15 us                                                | 7.47 us: 1.05x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 37.0 ms: 1.05x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 51.1 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (4): pickle_dict, unpickle_list, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.5 ms: 1.00x slower                                                 |
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.44 ms: 1.15x faster                                                 |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 29.2 ms: 1.02x faster                                                 |
| django_template | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 473 ms: 1.38x faster                                                  |
| json_dumps              | 7.63 ms                                                | 6.18 ms: 1.23x faster                                                 |
| mako                    | 8.53 ms                                                | 7.44 ms: 1.15x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 97.9 ms: 1.10x faster                                                 |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.10x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.59 ms: 1.09x faster                                                 |
| hexiom                  | 4.72 ms                                                | 4.46 ms: 1.06x faster                                                 |
| richards                | 32.2 ms                                                | 30.5 ms: 1.06x faster                                                 |
| pickle_pure_python      | 201 us                                                 | 191 us: 1.05x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 32.9 ns: 1.04x faster                                                 |
| pycparser               | 698 ms                                                 | 674 ms: 1.03x faster                                                  |
| chaos                   | 49.4 ms                                                | 47.8 ms: 1.03x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.50 sec: 1.03x faster                                                |
| generators              | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| chameleon               | 4.60 ms                                                | 4.48 ms: 1.03x faster                                                 |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.03x faster                                                 |
| scimark_fft             | 200 ms                                                 | 196 ms: 1.02x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 29.2 ms: 1.02x faster                                                 |
| create_gc_cycles        | 716 us                                                 | 702 us: 1.02x faster                                                  |
| regex_compile           | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| fannkuch                | 261 ms                                                 | 258 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.17 ms: 1.01x faster                                                 |
| meteor_contest          | 73.5 ms                                                | 72.9 ms: 1.01x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 472 us: 1.01x faster                                                  |
| python_startup          | 12.4 ms                                                | 12.5 ms: 1.00x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 26.4 us: 1.00x slower                                                 |
| regex_v8                | 16.1 ms                                                | 16.2 ms: 1.01x slower                                                 |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| regex_dna               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| float                   | 53.0 ms                                                | 53.5 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                                 |
| scimark_lu              | 73.3 ms                                                | 74.2 ms: 1.01x slower                                                 |
| async_tree_none         | 286 ms                                                 | 289 ms: 1.01x slower                                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 71.1 ms: 1.01x slower                                                 |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                |
| pprint_pformat          | 954 ms                                                 | 970 ms: 1.02x slower                                                  |
| logging_silent          | 68.1 ns                                                | 69.3 ns: 1.02x slower                                                 |
| go                      | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 63.8 ms: 1.02x slower                                                 |
| 2to3                    | 161 ms                                                 | 165 ms: 1.02x slower                                                  |
| coroutines              | 17.8 ms                                                | 18.1 ms: 1.02x slower                                                 |
| coverage                | 58.4 ms                                                | 59.6 ms: 1.02x slower                                                 |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                 |
| html5lib                | 34.7 ms                                                | 35.4 ms: 1.02x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 477 ms: 1.02x slower                                                  |
| sympy_str               | 151 ms                                                 | 155 ms: 1.02x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.95 us: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                  |
| regex_effbot            | 2.63 ms                                                | 2.69 ms: 1.02x slower                                                 |
| telco                   | 3.41 ms                                                | 3.49 ms: 1.02x slower                                                 |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.02x slower                                                  |
| thrift                  | 442 us                                                 | 453 us: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 547 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                 |
| sympy_sum               | 85.5 ms                                                | 88.2 ms: 1.03x slower                                                 |
| logging_simple          | 3.55 us                                                | 3.66 us: 1.03x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 74.9 ms: 1.03x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 32.1 ms: 1.03x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 53.5 ms: 1.03x slower                                                 |
| pickle                  | 7.15 us                                                | 7.47 us: 1.05x slower                                                 |
| logging_format          | 3.78 us                                                | 3.95 us: 1.05x slower                                                 |
| xml_etree_process       | 35.1 ms                                                | 37.0 ms: 1.05x slower                                                 |
| async_tree_io           | 704 ms                                                 | 744 ms: 1.06x slower                                                  |
| nqueens                 | 59.8 ms                                                | 63.1 ms: 1.06x slower                                                 |
| bench_mp_pool           | 43.9 ms                                                | 46.5 ms: 1.06x slower                                                 |
| xml_etree_generate      | 48.3 ms                                                | 51.1 ms: 1.06x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 87.7 ms: 1.06x slower                                                 |
| pyflate                 | 310 ms                                                 | 331 ms: 1.07x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.08x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.22 ms: 1.09x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.05 ms: 1.09x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 51.0 ms: 1.10x slower                                                 |
| comprehensions          | 16.1 us                                                | 17.7 us: 1.10x slower                                                 |
| raytrace                | 207 ms                                                 | 229 ms: 1.10x slower                                                  |
| mypy2                   | 195 ms                                                 | 262 ms: 1.35x slower                                                  |
| async_generators        | 196 ms                                                 | 272 ms: 1.38x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (12): tornado_http, deepcopy, pickle_dict, unpickle_list, pidigits, async_tree_memoization, json_loads, sqlalchemy_imperative, unpickle, json, nbody, pathlib
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230307-3.12.0a6-f9774e5/bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5.json: dask


# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
