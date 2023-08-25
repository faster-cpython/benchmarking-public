
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 174 ms: 1.08x slower                                   |
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 69.4 ms: 1.06x slower                                  |
| float          | 53.0 ms                                                | 59.6 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| regex_v8       | 16.1 ms                                                | 16.3 ms: 1.01x slower                                  |
| regex_compile  | 76.7 ms                                                | 78.7 ms: 1.03x slower                                  |
| regex_effbot   | 2.63 ms                                                | 2.70 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.95 ms: 1.10x faster                                  |
| unpickle_pure_python | 159 us                                                 | 151 us: 1.06x faster                                   |
| pickle_pure_python   | 201 us                                                 | 194 us: 1.03x faster                                   |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| unpickle             | 9.67 us                                                | 10.1 us: 1.05x slower                                  |
| pickle_dict          | 18.0 us                                                | 18.9 us: 1.05x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 75.2 ms: 1.07x slower                                  |
| json_loads           | 16.1 us                                                | 17.8 us: 1.11x slower                                  |
| pickle               | 7.15 us                                                | 7.95 us: 1.11x slower                                  |
| pickle_list          | 2.81 us                                                | 3.17 us: 1.13x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 40.4 ms: 1.15x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 58.6 ms: 1.22x slower                                  |
| unpickle_list        | 2.65 us                                                | 3.24 us: 1.22x slower                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.6 ms: 1.01x slower                                  |
| python_startup_no_site | 10.2 ms                                                | 10.5 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.79 ms: 1.10x faster                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 461 ms: 1.41x faster                                   |
| unpack_sequence         | 34.1 ns                                                | 28.0 ns: 1.22x faster                                  |
| generators              | 28.8 ms                                                | 24.9 ms: 1.16x faster                                  |
| deltablue               | 2.81 ms                                                | 2.47 ms: 1.14x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.95 ms: 1.10x faster                                  |
| mako                    | 8.53 ms                                                | 7.79 ms: 1.10x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.33 ms: 1.09x faster                                  |
| sqlglot_parse           | 959 us                                                 | 902 us: 1.06x faster                                   |
| unpickle_pure_python    | 159 us                                                 | 151 us: 1.06x faster                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| pickle_pure_python      | 201 us                                                 | 194 us: 1.03x faster                                   |
| chaos                   | 49.4 ms                                                | 48.0 ms: 1.03x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.6 us: 1.03x faster                                  |
| create_gc_cycles        | 716 us                                                 | 698 us: 1.02x faster                                   |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| meteor_contest          | 73.5 ms                                                | 73.4 ms: 1.00x faster                                  |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                  |
| go                      | 109 ms                                                 | 109 ms: 1.00x slower                                   |
| xml_etree_parse         | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 538 ms: 1.01x slower                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.27 ms: 1.01x slower                                  |
| coverage                | 58.4 ms                                                | 59.1 ms: 1.01x slower                                  |
| regex_v8                | 16.1 ms                                                | 16.3 ms: 1.01x slower                                  |
| dulwich_log             | 30.3 ms                                                | 30.7 ms: 1.01x slower                                  |
| coroutines              | 17.8 ms                                                | 18.0 ms: 1.01x slower                                  |
| python_startup          | 12.4 ms                                                | 12.6 ms: 1.01x slower                                  |
| mdp                     | 1.55 sec                                               | 1.57 sec: 1.02x slower                                 |
| async_tree_io           | 704 ms                                                 | 716 ms: 1.02x slower                                   |
| logging_silent          | 68.1 ns                                                | 69.6 ns: 1.02x slower                                  |
| regex_compile           | 76.7 ms                                                | 78.7 ms: 1.03x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.70 ms: 1.03x slower                                  |
| pathlib                 | 27.2 ms                                                | 28.1 ms: 1.03x slower                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.5 ms: 1.04x slower                                  |
| unpickle                | 9.67 us                                                | 10.1 us: 1.05x slower                                  |
| scimark_sor             | 82.6 ms                                                | 86.6 ms: 1.05x slower                                  |
| bench_thread_pool       | 474 us                                                 | 497 us: 1.05x slower                                   |
| logging_simple          | 3.55 us                                                | 3.72 us: 1.05x slower                                  |
| pickle_dict             | 18.0 us                                                | 18.9 us: 1.05x slower                                  |
| scimark_fft             | 200 ms                                                 | 210 ms: 1.05x slower                                   |
| fannkuch                | 261 ms                                                 | 276 ms: 1.05x slower                                   |
| nbody                   | 65.6 ms                                                | 69.4 ms: 1.06x slower                                  |
| logging_format          | 3.78 us                                                | 4.02 us: 1.06x slower                                  |
| nqueens                 | 59.8 ms                                                | 63.6 ms: 1.06x slower                                  |
| docutils                | 1.47 sec                                               | 1.57 sec: 1.07x slower                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 75.2 ms: 1.07x slower                                  |
| deepcopy                | 223 us                                                 | 240 us: 1.08x slower                                   |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.44 ms: 1.08x slower                                  |
| 2to3                    | 161 ms                                                 | 174 ms: 1.08x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 55.9 ms: 1.08x slower                                  |
| pprint_pformat          | 954 ms                                                 | 1.04 sec: 1.09x slower                                 |
| spectral_norm           | 72.6 ms                                                | 79.1 ms: 1.09x slower                                  |
| bench_mp_pool           | 43.9 ms                                                | 48.1 ms: 1.09x slower                                  |
| pprint_safe_repr        | 466 ms                                                 | 511 ms: 1.09x slower                                   |
| json                    | 2.78 ms                                                | 3.04 ms: 1.10x slower                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 68.6 ms: 1.10x slower                                  |
| json_loads              | 16.1 us                                                | 17.8 us: 1.11x slower                                  |
| pyflate                 | 310 ms                                                 | 343 ms: 1.11x slower                                   |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.11x slower                                  |
| pickle                  | 7.15 us                                                | 7.95 us: 1.11x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.14 us: 1.12x slower                                  |
| scimark_lu              | 73.3 ms                                                | 82.2 ms: 1.12x slower                                  |
| float                   | 53.0 ms                                                | 59.6 ms: 1.12x slower                                  |
| pickle_list             | 2.81 us                                                | 3.17 us: 1.13x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 52.7 ms: 1.13x slower                                  |
| xml_etree_process       | 35.1 ms                                                | 40.4 ms: 1.15x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 200 ms: 1.17x slower                                   |
| sqlglot_optimize        | 31.1 ms                                                | 36.6 ms: 1.18x slower                                  |
| telco                   | 3.41 ms                                                | 4.04 ms: 1.19x slower                                  |
| raytrace                | 207 ms                                                 | 250 ms: 1.21x slower                                   |
| xml_etree_generate      | 48.3 ms                                                | 58.6 ms: 1.22x slower                                  |
| unpickle_list           | 2.65 us                                                | 3.24 us: 1.22x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.58 us: 1.25x slower                                  |
| mypy2                   | 195 ms                                                 | 267 ms: 1.37x slower                                   |
| async_generators        | 196 ms                                                 | 316 ms: 1.61x slower                                   |
| Geometric mean          | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (6): tornado_http, pidigits, richards, async_tree_none, pycparser, async_tree_memoization
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230506-3.12.0a7+-42f54d1/bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
