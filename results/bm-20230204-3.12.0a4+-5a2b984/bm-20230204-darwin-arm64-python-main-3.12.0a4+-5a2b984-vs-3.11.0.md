
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 5a2b984
- commit date: 2023-02-04
- overall geometric mean: 1.03x faster \*
- HPT reliability: 95.37%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| chameleon      | 4.60 ms                                                | 4.71 ms: 1.02x slower                                  |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.0 ms: 1.02x faster                                  |
| float          | 53.0 ms                                                | 51.9 ms: 1.02x faster                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.1 ms: 1.06x faster                                  |
| regex_dna      | 152 ms                                                 | 150 ms: 1.02x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x faster                                  |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.10 ms: 1.25x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 93.9 ms: 1.15x faster                                  |
| pickle_pure_python   | 201 us                                                 | 192 us: 1.04x faster                                   |
| xml_etree_iterparse  | 70.1 ms                                                | 67.8 ms: 1.03x faster                                  |
| xml_etree_process    | 35.1 ms                                                | 34.4 ms: 1.02x faster                                  |
| unpickle_pure_python | 159 us                                                 | 157 us: 1.02x faster                                   |
| xml_etree_generate   | 48.3 ms                                                | 47.8 ms: 1.01x faster                                  |
| pickle_dict          | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| unpickle_list        | 2.65 us                                                | 2.71 us: 1.02x slower                                  |
| unpickle             | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.57 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.35 ms: 1.38x faster                                  |
| python_startup         | 12.4 ms                                                | 9.36 ms: 1.33x faster                                  |
| Geometric mean         | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.16 ms: 1.19x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.4 ms: 1.05x faster                                  |
| django_template | 21.0 ms                                                | 20.9 ms: 1.00x faster                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 423 ms: 1.54x faster                                   |
| python_startup_no_site  | 10.2 ms                                                | 7.35 ms: 1.38x faster                                  |
| python_startup          | 12.4 ms                                                | 9.36 ms: 1.33x faster                                  |
| pathlib                 | 27.2 ms                                                | 20.8 ms: 1.31x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.10 ms: 1.25x faster                                  |
| mako                    | 8.53 ms                                                | 7.16 ms: 1.19x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 93.9 ms: 1.15x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.81 ms: 1.14x faster                                  |
| deltablue               | 2.81 ms                                                | 2.57 ms: 1.10x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.32 ms: 1.09x faster                                  |
| chaos                   | 49.4 ms                                                | 45.5 ms: 1.09x faster                                  |
| richards                | 32.2 ms                                                | 29.7 ms: 1.08x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| regex_compile           | 76.7 ms                                                | 72.1 ms: 1.06x faster                                  |
| bench_thread_pool       | 474 us                                                 | 447 us: 1.06x faster                                   |
| dulwich_log             | 30.3 ms                                                | 28.6 ms: 1.06x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.4 ms: 1.05x faster                                  |
| sympy_sum               | 85.5 ms                                                | 81.9 ms: 1.04x faster                                  |
| pickle_pure_python      | 201 us                                                 | 192 us: 1.04x faster                                   |
| pycparser               | 698 ms                                                 | 669 ms: 1.04x faster                                   |
| async_tree_memoization  | 336 ms                                                 | 322 ms: 1.04x faster                                   |
| unpack_sequence         | 34.1 ns                                                | 32.8 ns: 1.04x faster                                  |
| sympy_str               | 151 ms                                                 | 145 ms: 1.04x faster                                   |
| scimark_fft             | 200 ms                                                 | 192 ms: 1.04x faster                                   |
| logging_silent          | 68.1 ns                                                | 65.7 ns: 1.04x faster                                  |
| scimark_lu              | 73.3 ms                                                | 70.8 ms: 1.04x faster                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 67.8 ms: 1.03x faster                                  |
| create_gc_cycles        | 716 us                                                 | 696 us: 1.03x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                  |
| bench_mp_pool           | 43.9 ms                                                | 42.9 ms: 1.03x faster                                  |
| nbody                   | 65.6 ms                                                | 64.0 ms: 1.02x faster                                  |
| coverage                | 58.4 ms                                                | 57.1 ms: 1.02x faster                                  |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                   |
| float                   | 53.0 ms                                                | 51.9 ms: 1.02x faster                                  |
| async_tree_none         | 286 ms                                                 | 280 ms: 1.02x faster                                   |
| xml_etree_process       | 35.1 ms                                                | 34.4 ms: 1.02x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 157 us: 1.02x faster                                   |
| deepcopy_memo           | 26.3 us                                                | 25.9 us: 1.02x faster                                  |
| regex_dna               | 152 ms                                                 | 150 ms: 1.02x faster                                   |
| mdp                     | 1.55 sec                                               | 1.52 sec: 1.01x faster                                 |
| deepcopy                | 223 us                                                 | 220 us: 1.01x faster                                   |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| xml_etree_generate      | 48.3 ms                                                | 47.8 ms: 1.01x faster                                  |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.00x faster                                  |
| gc_traversal            | 2.42 ms                                                | 2.41 ms: 1.00x faster                                  |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x faster                                  |
| sqlglot_normalize       | 171 ms                                                 | 171 ms: 1.00x slower                                   |
| spectral_norm           | 72.6 ms                                                | 72.7 ms: 1.00x slower                                  |
| sympy_expand            | 242 ms                                                 | 243 ms: 1.00x slower                                   |
| pickle_dict             | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| go                      | 109 ms                                                 | 109 ms: 1.00x slower                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 536 ms: 1.00x slower                                   |
| regex_v8                | 16.1 ms                                                | 16.2 ms: 1.01x slower                                  |
| telco                   | 3.41 ms                                                | 3.43 ms: 1.01x slower                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                   |
| sqlglot_optimize        | 31.1 ms                                                | 31.4 ms: 1.01x slower                                  |
| pprint_safe_repr        | 466 ms                                                 | 470 ms: 1.01x slower                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                   |
| nqueens                 | 59.8 ms                                                | 60.8 ms: 1.02x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.7 ms: 1.02x slower                                  |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                  |
| chameleon               | 4.60 ms                                                | 4.71 ms: 1.02x slower                                  |
| unpickle_list           | 2.65 us                                                | 2.71 us: 1.02x slower                                  |
| unpickle                | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| logging_simple          | 3.55 us                                                | 3.64 us: 1.03x slower                                  |
| meteor_contest          | 73.5 ms                                                | 75.9 ms: 1.03x slower                                  |
| scimark_sor             | 82.6 ms                                                | 85.3 ms: 1.03x slower                                  |
| async_tree_io           | 704 ms                                                 | 732 ms: 1.04x slower                                   |
| logging_format          | 3.78 us                                                | 3.93 us: 1.04x slower                                  |
| coroutines              | 17.8 ms                                                | 18.8 ms: 1.06x slower                                  |
| pickle                  | 7.15 us                                                | 7.57 us: 1.06x slower                                  |
| raytrace                | 207 ms                                                 | 219 ms: 1.06x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                  |
| sqlglot_parse           | 959 us                                                 | 1.02 ms: 1.07x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 49.8 ms: 1.07x slower                                  |
| pyflate                 | 310 ms                                                 | 333 ms: 1.07x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                  |
| 2to3                    | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| generators              | 28.8 ms                                                | 34.1 ms: 1.19x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (6): tornado_http, deepcopy_reduce, thrift, pickle_list, pprint_pformat, html5lib
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (2) of results/bm-20230204-3.12.0a4+-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984.json: dask, mypy


# HPT report

- Reliability score: 95.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
