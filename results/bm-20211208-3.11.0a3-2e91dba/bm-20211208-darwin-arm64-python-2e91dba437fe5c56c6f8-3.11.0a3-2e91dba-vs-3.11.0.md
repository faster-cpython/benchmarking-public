
# Results vs. 3.11.0

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: darwin-arm64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.06x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 168 ms: 1.04x slower                                                  |
| chameleon      | 4.60 ms                                                | 5.16 ms: 1.12x slower                                                 |
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                                |
| html5lib       | 34.7 ms                                                | 37.0 ms: 1.07x slower                                                 |
| tornado_http   | 71.5 ms                                                | 79.1 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 65.3 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 56.7 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_compile  | 76.7 ms                                                | 78.8 ms: 1.03x slower                                                 |
| regex_dna      | 152 ms                                                 | 159 ms: 1.05x slower                                                  |
| regex_v8       | 16.1 ms                                                | 17.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 99.0 ms: 1.09x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.51 us: 1.06x faster                                                 |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                                 |
| json_loads           | 16.1 us                                                | 16.6 us: 1.03x slower                                                 |
| pickle               | 7.15 us                                                | 7.42 us: 1.04x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 50.3 ms: 1.04x slower                                                 |
| unpickle             | 9.67 us                                                | 10.1 us: 1.04x slower                                                 |
| json_dumps           | 7.63 ms                                                | 7.99 ms: 1.05x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 37.7 ms: 1.07x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 176 us: 1.11x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 224 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.23 ms: 1.10x faster                                                 |
| python_startup         | 12.4 ms                                                | 15.4 ms: 1.24x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 16.3 ms: 1.07x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 32.3 ms: 1.08x slower                                                 |
| django_template | 21.0 ms                                                | 22.9 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 58.4 ms                                                | 45.6 ms: 1.28x faster                                                 |
| python_startup_no_site  | 10.2 ms                                                | 9.23 ms: 1.10x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 99.0 ms: 1.09x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 32.0 ns: 1.07x faster                                                 |
| generators              | 28.8 ms                                                | 27.1 ms: 1.06x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.51 us: 1.06x faster                                                 |
| logging_simple          | 3.55 us                                                | 3.52 us: 1.01x faster                                                 |
| nbody                   | 65.6 ms                                                | 65.3 ms: 1.00x faster                                                 |
| pickle_dict             | 18.0 us                                                | 17.9 us: 1.00x faster                                                 |
| hexiom                  | 4.72 ms                                                | 4.70 ms: 1.00x faster                                                 |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 73.7 ms: 1.00x slower                                                 |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                                 |
| async_generators        | 196 ms                                                 | 198 ms: 1.01x slower                                                  |
| logging_format          | 3.78 us                                                | 3.83 us: 1.01x slower                                                 |
| scimark_fft             | 200 ms                                                 | 202 ms: 1.01x slower                                                  |
| chaos                   | 49.4 ms                                                | 50.3 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                 |
| nqueens                 | 59.8 ms                                                | 61.1 ms: 1.02x slower                                                 |
| mdp                     | 1.55 sec                                               | 1.58 sec: 1.02x slower                                                |
| create_gc_cycles        | 716 us                                                 | 733 us: 1.02x slower                                                  |
| regex_compile           | 76.7 ms                                                | 78.8 ms: 1.03x slower                                                 |
| json_loads              | 16.1 us                                                | 16.6 us: 1.03x slower                                                 |
| fannkuch                | 261 ms                                                 | 270 ms: 1.04x slower                                                  |
| pickle                  | 7.15 us                                                | 7.42 us: 1.04x slower                                                 |
| 2to3                    | 161 ms                                                 | 168 ms: 1.04x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 50.3 ms: 1.04x slower                                                 |
| unpickle                | 9.67 us                                                | 10.1 us: 1.04x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 86.2 ms: 1.04x slower                                                 |
| coroutines              | 17.8 ms                                                | 18.6 ms: 1.04x slower                                                 |
| json_dumps              | 7.63 ms                                                | 7.99 ms: 1.05x slower                                                 |
| sympy_sum               | 85.5 ms                                                | 89.6 ms: 1.05x slower                                                 |
| flaskblogging           | 2.43 ms                                                | 2.54 ms: 1.05x slower                                                 |
| regex_dna               | 152 ms                                                 | 159 ms: 1.05x slower                                                  |
| telco                   | 3.41 ms                                                | 3.57 ms: 1.05x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 179 ms: 1.05x slower                                                  |
| dulwich_log             | 30.3 ms                                                | 31.8 ms: 1.05x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| pylint                  | 272 ms                                                 | 287 ms: 1.06x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 76.8 ms: 1.06x slower                                                 |
| regex_v8                | 16.1 ms                                                | 17.1 ms: 1.06x slower                                                 |
| thrift                  | 442 us                                                 | 470 us: 1.06x slower                                                  |
| genshi_text             | 15.3 ms                                                | 16.3 ms: 1.07x slower                                                 |
| docutils                | 1.47 sec                                               | 1.57 sec: 1.07x slower                                                |
| html5lib                | 34.7 ms                                                | 37.0 ms: 1.07x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.1 us: 1.07x slower                                                 |
| async_tree_none         | 286 ms                                                 | 305 ms: 1.07x slower                                                  |
| sympy_str               | 151 ms                                                 | 162 ms: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.04 us: 1.07x slower                                                 |
| float                   | 53.0 ms                                                | 56.7 ms: 1.07x slower                                                 |
| scimark_lu              | 73.3 ms                                                | 78.6 ms: 1.07x slower                                                 |
| xml_etree_process       | 35.1 ms                                                | 37.7 ms: 1.07x slower                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                | 67.3 ms: 1.08x slower                                                 |
| deepcopy                | 223 us                                                 | 240 us: 1.08x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.08x slower                                                 |
| json                    | 2.78 ms                                                | 2.99 ms: 1.08x slower                                                 |
| sympy_expand            | 242 ms                                                 | 261 ms: 1.08x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 505 ms: 1.08x slower                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.80 ms: 1.08x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 32.3 ms: 1.08x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.03 sec: 1.08x slower                                                |
| django_template         | 21.0 ms                                                | 22.9 ms: 1.09x slower                                                 |
| pycparser               | 698 ms                                                 | 759 ms: 1.09x slower                                                  |
| bench_thread_pool       | 474 us                                                 | 517 us: 1.09x slower                                                  |
| go                      | 109 ms                                                 | 119 ms: 1.10x slower                                                  |
| raytrace                | 207 ms                                                 | 227 ms: 1.10x slower                                                  |
| deltablue               | 2.81 ms                                                | 3.10 ms: 1.10x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 587 ms: 1.10x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 51.4 ms: 1.11x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 34.4 ms: 1.11x slower                                                 |
| tornado_http            | 71.5 ms                                                | 79.1 ms: 1.11x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 176 us: 1.11x slower                                                  |
| pyflate                 | 310 ms                                                 | 346 ms: 1.11x slower                                                  |
| pickle_pure_python      | 201 us                                                 | 224 us: 1.12x slower                                                  |
| comprehensions          | 16.1 us                                                | 18.0 us: 1.12x slower                                                 |
| chameleon               | 4.60 ms                                                | 5.16 ms: 1.12x slower                                                 |
| richards                | 32.2 ms                                                | 36.2 ms: 1.12x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 59.7 ms: 1.15x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 400 ms: 1.19x slower                                                  |
| logging_silent          | 68.1 ns                                                | 81.6 ns: 1.20x slower                                                 |
| async_tree_io           | 704 ms                                                 | 855 ms: 1.21x slower                                                  |
| python_startup          | 12.4 ms                                                | 15.4 ms: 1.24x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.47 ms: 1.31x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.29 ms: 1.35x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (5): bench_mp_pool, xml_etree_iterparse, mako, pickle_list, pathlib
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20211208-3.11.0a3-2e91dba/bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x
