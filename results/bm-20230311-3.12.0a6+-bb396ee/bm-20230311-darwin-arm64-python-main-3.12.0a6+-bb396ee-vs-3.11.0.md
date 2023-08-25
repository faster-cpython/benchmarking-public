
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: bb396ee
- commit date: 2023-03-11
- overall geometric mean: 1.01x slower \*
- HPT reliability: 98.84%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 166 ms: 1.03x slower                                   |
| chameleon      | 4.60 ms                                                | 4.51 ms: 1.02x faster                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.02x slower                                 |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.1 ms: 1.02x faster                                  |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                   |
| float          | 53.0 ms                                                | 53.6 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.7 ms: 1.01x faster                                  |
| regex_dna      | 152 ms                                                 | 152 ms: 1.00x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.30 ms: 1.21x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 97.2 ms: 1.11x faster                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                   |
| pickle_pure_python   | 201 us                                                 | 190 us: 1.05x faster                                   |
| pickle_dict          | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| unpickle             | 9.67 us                                                | 9.76 us: 1.01x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 70.8 ms: 1.01x slower                                  |
| unpickle_list        | 2.65 us                                                | 2.69 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| pickle               | 7.15 us                                                | 7.48 us: 1.05x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 36.8 ms: 1.05x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 51.0 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.93 ms: 1.14x faster                                  |
| python_startup         | 12.4 ms                                                | 11.1 ms: 1.12x faster                                  |
| Geometric mean         | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.47 ms: 1.14x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.9 ms: 1.03x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.4 ms: 1.02x faster                                  |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 414 ms: 1.57x faster                                   |
| json_dumps              | 7.63 ms                                                | 6.30 ms: 1.21x faster                                  |
| mako                    | 8.53 ms                                                | 7.47 ms: 1.14x faster                                  |
| python_startup_no_site  | 10.2 ms                                                | 8.93 ms: 1.14x faster                                  |
| python_startup          | 12.4 ms                                                | 11.1 ms: 1.12x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 97.2 ms: 1.11x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.10x faster                                   |
| deltablue               | 2.81 ms                                                | 2.59 ms: 1.09x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.45 ms: 1.06x faster                                  |
| pickle_pure_python      | 201 us                                                 | 190 us: 1.05x faster                                   |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 32.8 ns: 1.04x faster                                  |
| chaos                   | 49.4 ms                                                | 47.9 ms: 1.03x faster                                  |
| mdp                     | 1.55 sec                                               | 1.50 sec: 1.03x faster                                 |
| pycparser               | 698 ms                                                 | 678 ms: 1.03x faster                                   |
| genshi_text             | 15.3 ms                                                | 14.9 ms: 1.03x faster                                  |
| nbody                   | 65.6 ms                                                | 64.1 ms: 1.02x faster                                  |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.02x faster                                  |
| chameleon               | 4.60 ms                                                | 4.51 ms: 1.02x faster                                  |
| generators              | 28.8 ms                                                | 28.2 ms: 1.02x faster                                  |
| scimark_fft             | 200 ms                                                 | 196 ms: 1.02x faster                                   |
| create_gc_cycles        | 716 us                                                 | 704 us: 1.02x faster                                   |
| genshi_xml              | 29.8 ms                                                | 29.4 ms: 1.02x faster                                  |
| fannkuch                | 261 ms                                                 | 257 ms: 1.02x faster                                   |
| regex_compile           | 76.7 ms                                                | 75.7 ms: 1.01x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.17 ms: 1.01x faster                                  |
| bench_thread_pool       | 474 us                                                 | 473 us: 1.00x faster                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.18 ms: 1.00x faster                                  |
| regex_dna               | 152 ms                                                 | 152 ms: 1.00x faster                                   |
| telco                   | 3.41 ms                                                | 3.40 ms: 1.00x faster                                  |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                   |
| pickle_dict             | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| meteor_contest          | 73.5 ms                                                | 73.8 ms: 1.00x slower                                  |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                  |
| unpickle                | 9.67 us                                                | 9.76 us: 1.01x slower                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 70.8 ms: 1.01x slower                                  |
| deepcopy                | 223 us                                                 | 225 us: 1.01x slower                                   |
| float                   | 53.0 ms                                                | 53.6 ms: 1.01x slower                                  |
| logging_silent          | 68.1 ns                                                | 68.9 ns: 1.01x slower                                  |
| unpickle_list           | 2.65 us                                                | 2.69 us: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| async_tree_none         | 286 ms                                                 | 290 ms: 1.01x slower                                   |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.02x slower                                 |
| coroutines              | 17.8 ms                                                | 18.1 ms: 1.02x slower                                  |
| go                      | 109 ms                                                 | 111 ms: 1.02x slower                                   |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.02x slower                                  |
| coverage                | 58.4 ms                                                | 59.7 ms: 1.02x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                   |
| scimark_lu              | 73.3 ms                                                | 75.0 ms: 1.02x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| json                    | 2.78 ms                                                | 2.84 ms: 1.02x slower                                  |
| thrift                  | 442 us                                                 | 453 us: 1.02x slower                                   |
| sympy_str               | 151 ms                                                 | 155 ms: 1.03x slower                                   |
| 2to3                    | 161 ms                                                 | 166 ms: 1.03x slower                                   |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.03x slower                                   |
| pprint_pformat          | 954 ms                                                 | 979 ms: 1.03x slower                                   |
| sqlalchemy_declarative  | 62.6 ms                                                | 64.3 ms: 1.03x slower                                  |
| logging_simple          | 3.55 us                                                | 3.64 us: 1.03x slower                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 548 ms: 1.03x slower                                   |
| bench_mp_pool           | 43.9 ms                                                | 45.2 ms: 1.03x slower                                  |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                  |
| pprint_safe_repr        | 466 ms                                                 | 481 ms: 1.03x slower                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.97 us: 1.03x slower                                  |
| spectral_norm           | 72.6 ms                                                | 75.0 ms: 1.03x slower                                  |
| sqlglot_optimize        | 31.1 ms                                                | 32.2 ms: 1.03x slower                                  |
| sympy_sum               | 85.5 ms                                                | 88.7 ms: 1.04x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.7 ms: 1.04x slower                                  |
| logging_format          | 3.78 us                                                | 3.94 us: 1.04x slower                                  |
| pickle                  | 7.15 us                                                | 7.48 us: 1.05x slower                                  |
| xml_etree_process       | 35.1 ms                                                | 36.8 ms: 1.05x slower                                  |
| nqueens                 | 59.8 ms                                                | 62.9 ms: 1.05x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 51.0 ms: 1.06x slower                                  |
| async_tree_io           | 704 ms                                                 | 745 ms: 1.06x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                  |
| scimark_sor             | 82.6 ms                                                | 88.4 ms: 1.07x slower                                  |
| pyflate                 | 310 ms                                                 | 332 ms: 1.07x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.23 ms: 1.09x slower                                  |
| sqlglot_parse           | 959 us                                                 | 1.06 ms: 1.10x slower                                  |
| raytrace                | 207 ms                                                 | 228 ms: 1.10x slower                                   |
| scimark_monte_carlo     | 46.5 ms                                                | 51.3 ms: 1.10x slower                                  |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.11x slower                                  |
| mypy2                   | 195 ms                                                 | 262 ms: 1.34x slower                                   |
| async_generators        | 196 ms                                                 | 267 ms: 1.36x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (6): tornado_http, pickle_list, regex_v8, deepcopy_memo, async_tree_memoization, pathlib
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230311-3.12.0a6+-bb396ee/bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee.json: dask


# HPT report

- Reliability score: 98.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
