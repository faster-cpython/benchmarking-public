
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: d3ca042
- commit date: 2023-03-06
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.12%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 164 ms: 1.02x slower                                   |
| chameleon      | 4.60 ms                                                | 4.42 ms: 1.04x faster                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                 |
| html5lib       | 34.7 ms                                                | 35.6 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.1 ms: 1.02x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| float          | 53.0 ms                                                | 53.6 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.4 ms: 1.02x faster                                  |
| regex_v8       | 16.1 ms                                                | 16.5 ms: 1.02x slower                                  |
| regex_effbot   | 2.63 ms                                                | 2.85 ms: 1.09x slower                                  |
| regex_dna      | 152 ms                                                 | 166 ms: 1.09x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.17 ms: 1.24x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 97.7 ms: 1.11x faster                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                   |
| pickle_pure_python   | 201 us                                                 | 190 us: 1.05x faster                                   |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 71.0 ms: 1.01x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 36.7 ms: 1.05x slower                                  |
| pickle               | 7.15 us                                                | 7.50 us: 1.05x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 51.3 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (4): json_loads, unpickle_list, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.74 ms: 1.16x faster                                  |
| python_startup         | 12.4 ms                                                | 10.8 ms: 1.15x faster                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.46 ms: 1.14x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.2 ms: 1.02x faster                                  |
| django_template | 21.0 ms                                                | 21.6 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 428 ms: 1.52x faster                                   |
| json_dumps              | 7.63 ms                                                | 6.17 ms: 1.24x faster                                  |
| python_startup_no_site  | 10.2 ms                                                | 8.74 ms: 1.16x faster                                  |
| python_startup          | 12.4 ms                                                | 10.8 ms: 1.15x faster                                  |
| mako                    | 8.53 ms                                                | 7.46 ms: 1.14x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 97.7 ms: 1.11x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.10x faster                                   |
| deltablue               | 2.81 ms                                                | 2.59 ms: 1.09x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.46 ms: 1.06x faster                                  |
| richards                | 32.2 ms                                                | 30.5 ms: 1.06x faster                                  |
| pickle_pure_python      | 201 us                                                 | 190 us: 1.05x faster                                   |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                  |
| chameleon               | 4.60 ms                                                | 4.42 ms: 1.04x faster                                  |
| chaos                   | 49.4 ms                                                | 47.8 ms: 1.03x faster                                  |
| mdp                     | 1.55 sec                                               | 1.50 sec: 1.03x faster                                 |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| pycparser               | 698 ms                                                 | 679 ms: 1.03x faster                                   |
| dulwich_log             | 30.3 ms                                                | 29.5 ms: 1.03x faster                                  |
| nbody                   | 65.6 ms                                                | 64.1 ms: 1.02x faster                                  |
| genshi_xml              | 29.8 ms                                                | 29.2 ms: 1.02x faster                                  |
| scimark_fft             | 200 ms                                                 | 196 ms: 1.02x faster                                   |
| create_gc_cycles        | 716 us                                                 | 703 us: 1.02x faster                                   |
| regex_compile           | 76.7 ms                                                | 75.4 ms: 1.02x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.16 ms: 1.01x faster                                  |
| fannkuch                | 261 ms                                                 | 259 ms: 1.01x faster                                   |
| generators              | 28.8 ms                                                | 28.5 ms: 1.01x faster                                  |
| meteor_contest          | 73.5 ms                                                | 73.4 ms: 1.00x faster                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                  |
| telco                   | 3.41 ms                                                | 3.43 ms: 1.01x slower                                  |
| deepcopy                | 223 us                                                 | 225 us: 1.01x slower                                   |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                 |
| float                   | 53.0 ms                                                | 53.6 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 71.0 ms: 1.01x slower                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 63.4 ms: 1.01x slower                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                  |
| scimark_lu              | 73.3 ms                                                | 74.5 ms: 1.02x slower                                  |
| sympy_expand            | 242 ms                                                 | 246 ms: 1.02x slower                                   |
| 2to3                    | 161 ms                                                 | 164 ms: 1.02x slower                                   |
| pprint_pformat          | 954 ms                                                 | 972 ms: 1.02x slower                                   |
| coverage                | 58.4 ms                                                | 59.5 ms: 1.02x slower                                  |
| go                      | 109 ms                                                 | 111 ms: 1.02x slower                                   |
| coroutines              | 17.8 ms                                                | 18.1 ms: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 544 ms: 1.02x slower                                   |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                   |
| pprint_safe_repr        | 466 ms                                                 | 477 ms: 1.02x slower                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.37 ms: 1.02x slower                                  |
| regex_v8                | 16.1 ms                                                | 16.5 ms: 1.02x slower                                  |
| sympy_str               | 151 ms                                                 | 155 ms: 1.02x slower                                   |
| logging_simple          | 3.55 us                                                | 3.64 us: 1.02x slower                                  |
| html5lib                | 34.7 ms                                                | 35.6 ms: 1.03x slower                                  |
| sympy_sum               | 85.5 ms                                                | 87.8 ms: 1.03x slower                                  |
| django_template         | 21.0 ms                                                | 21.6 ms: 1.03x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.97 us: 1.03x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.3 ms: 1.03x slower                                  |
| spectral_norm           | 72.6 ms                                                | 74.9 ms: 1.03x slower                                  |
| sqlglot_optimize        | 31.1 ms                                                | 32.1 ms: 1.03x slower                                  |
| thrift                  | 442 us                                                 | 458 us: 1.04x slower                                   |
| logging_format          | 3.78 us                                                | 3.94 us: 1.04x slower                                  |
| async_tree_io           | 704 ms                                                 | 736 ms: 1.04x slower                                   |
| xml_etree_process       | 35.1 ms                                                | 36.7 ms: 1.05x slower                                  |
| pickle                  | 7.15 us                                                | 7.50 us: 1.05x slower                                  |
| nqueens                 | 59.8 ms                                                | 63.1 ms: 1.06x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 51.3 ms: 1.06x slower                                  |
| scimark_sor             | 82.6 ms                                                | 88.1 ms: 1.07x slower                                  |
| pyflate                 | 310 ms                                                 | 332 ms: 1.07x slower                                   |
| regex_effbot            | 2.63 ms                                                | 2.85 ms: 1.09x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.22 ms: 1.09x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.38 us: 1.09x slower                                  |
| regex_dna               | 152 ms                                                 | 166 ms: 1.09x slower                                   |
| sqlglot_parse           | 959 us                                                 | 1.05 ms: 1.10x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 50.9 ms: 1.10x slower                                  |
| comprehensions          | 16.1 us                                                | 17.7 us: 1.10x slower                                  |
| raytrace                | 207 ms                                                 | 228 ms: 1.10x slower                                   |
| mypy2                   | 195 ms                                                 | 262 ms: 1.34x slower                                   |
| async_generators        | 196 ms                                                 | 270 ms: 1.38x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (13): tornado_http, async_tree_memoization, bench_thread_pool, pathlib, json, json_loads, unpickle_list, logging_silent, pickle_dict, deepcopy_memo, unpickle, bench_mp_pool, async_tree_none
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230306-3.12.0a5+-d3ca042/bm-20230306-darwin-arm64-python-main-3.12.0a5+-d3ca042.json: dask


# HPT report

- Reliability score: 99.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
