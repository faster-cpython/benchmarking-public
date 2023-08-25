
# Results vs. 3.11.0

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: darwin-arm64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.00x slower \*
- HPT reliability: 98.50%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 164 ms: 1.01x slower                                                   |
| chameleon      | 4.60 ms                                                | 4.41 ms: 1.04x faster                                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                 |
| html5lib       | 34.7 ms                                                | 35.7 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.9 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.2 ms: 1.02x faster                                                  |
| regex_v8       | 16.1 ms                                                | 16.0 ms: 1.00x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.22 ms: 1.23x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 142 us: 1.12x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 96.7 ms: 1.12x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 195 us: 1.03x faster                                                   |
| json_loads           | 16.1 us                                                | 15.9 us: 1.01x faster                                                  |
| pickle_dict          | 18.0 us                                                | 18.1 us: 1.01x slower                                                  |
| unpickle_list        | 2.65 us                                                | 2.69 us: 1.01x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 50.7 ms: 1.05x slower                                                  |
| pickle               | 7.15 us                                                | 7.54 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.5 ms: 1.01x slower                                                  |
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.43 ms: 1.15x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.4 ms: 1.06x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 28.4 ms: 1.05x faster                                                  |
| django_template | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 448 ms: 1.45x faster                                                   |
| json_dumps              | 7.63 ms                                                | 6.22 ms: 1.23x faster                                                  |
| mako                    | 8.53 ms                                                | 7.43 ms: 1.15x faster                                                  |
| generators              | 28.8 ms                                                | 25.5 ms: 1.13x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 142 us: 1.12x faster                                                   |
| xml_etree_parse         | 108 ms                                                 | 96.7 ms: 1.12x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                                  |
| hexiom                  | 4.72 ms                                                | 4.35 ms: 1.09x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.4 ms: 1.06x faster                                                  |
| richards                | 32.2 ms                                                | 30.4 ms: 1.06x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.4 ms: 1.05x faster                                                  |
| pycparser               | 698 ms                                                 | 668 ms: 1.04x faster                                                   |
| chameleon               | 4.60 ms                                                | 4.41 ms: 1.04x faster                                                  |
| chaos                   | 49.4 ms                                                | 47.6 ms: 1.04x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 195 us: 1.03x faster                                                   |
| unpack_sequence         | 34.1 ns                                                | 33.2 ns: 1.03x faster                                                  |
| nbody                   | 65.6 ms                                                | 63.9 ms: 1.03x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 25.7 us: 1.02x faster                                                  |
| fannkuch                | 261 ms                                                 | 255 ms: 1.02x faster                                                   |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.02x faster                                                  |
| regex_compile           | 76.7 ms                                                | 75.2 ms: 1.02x faster                                                  |
| create_gc_cycles        | 716 us                                                 | 702 us: 1.02x faster                                                   |
| bench_thread_pool       | 474 us                                                 | 466 us: 1.02x faster                                                   |
| logging_silent          | 68.1 ns                                                | 66.9 ns: 1.02x faster                                                  |
| scimark_fft             | 200 ms                                                 | 197 ms: 1.01x faster                                                   |
| json_loads              | 16.1 us                                                | 15.9 us: 1.01x faster                                                  |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.01x faster                                                 |
| coroutines              | 17.8 ms                                                | 17.7 ms: 1.00x faster                                                  |
| regex_v8                | 16.1 ms                                                | 16.0 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.19 ms: 1.00x faster                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.22 ms: 1.00x slower                                                  |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                                  |
| python_startup          | 12.4 ms                                                | 12.5 ms: 1.01x slower                                                  |
| pickle_dict             | 18.0 us                                                | 18.1 us: 1.01x slower                                                  |
| go                      | 109 ms                                                 | 109 ms: 1.01x slower                                                   |
| async_tree_none         | 286 ms                                                 | 288 ms: 1.01x slower                                                   |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                  |
| pprint_pformat          | 954 ms                                                 | 964 ms: 1.01x slower                                                   |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                                   |
| pprint_safe_repr        | 466 ms                                                 | 473 ms: 1.01x slower                                                   |
| sympy_expand            | 242 ms                                                 | 245 ms: 1.01x slower                                                   |
| unpickle_list           | 2.65 us                                                | 2.69 us: 1.01x slower                                                  |
| 2to3                    | 161 ms                                                 | 164 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 542 ms: 1.02x slower                                                   |
| django_template         | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.61 us: 1.02x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 63.8 ms: 1.02x slower                                                  |
| sympy_str               | 151 ms                                                 | 154 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 31.1 ms                                                | 31.7 ms: 1.02x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.95 us: 1.02x slower                                                  |
| regex_effbot            | 2.63 ms                                                | 2.69 ms: 1.02x slower                                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| telco                   | 3.41 ms                                                | 3.49 ms: 1.02x slower                                                  |
| thrift                  | 442 us                                                 | 454 us: 1.03x slower                                                   |
| html5lib                | 34.7 ms                                                | 35.7 ms: 1.03x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 88.2 ms: 1.03x slower                                                  |
| coverage                | 58.4 ms                                                | 60.3 ms: 1.03x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                  |
| logging_format          | 3.78 us                                                | 3.91 us: 1.03x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 76.1 ms: 1.04x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.6 ms: 1.04x slower                                                  |
| nqueens                 | 59.8 ms                                                | 61.9 ms: 1.04x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 75.5 ms: 1.04x slower                                                  |
| async_tree_io           | 704 ms                                                 | 738 ms: 1.05x slower                                                   |
| scimark_sor             | 82.6 ms                                                | 86.7 ms: 1.05x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 50.7 ms: 1.05x slower                                                  |
| bench_mp_pool           | 43.9 ms                                                | 46.3 ms: 1.05x slower                                                  |
| pickle                  | 7.15 us                                                | 7.54 us: 1.06x slower                                                  |
| pyflate                 | 310 ms                                                 | 328 ms: 1.06x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                                  |
| raytrace                | 207 ms                                                 | 223 ms: 1.08x slower                                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.23 ms: 1.09x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.06 ms: 1.11x slower                                                  |
| comprehensions          | 16.1 us                                                | 18.2 us: 1.13x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 53.2 ms: 1.14x slower                                                  |
| mypy2                   | 195 ms                                                 | 263 ms: 1.35x slower                                                   |
| async_generators        | 196 ms                                                 | 266 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (12): async_tree_memoization, tornado_http, deepcopy, pathlib, regex_dna, pidigits, xml_etree_iterparse, json, float, pickle_list, scimark_lu, unpickle
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230226-3.12.0a5+-f3cb15c/bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c.json: dask


# HPT report

- Reliability score: 98.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
