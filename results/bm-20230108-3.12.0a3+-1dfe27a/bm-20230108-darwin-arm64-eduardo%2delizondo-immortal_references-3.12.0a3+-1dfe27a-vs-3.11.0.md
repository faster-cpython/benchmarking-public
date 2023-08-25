
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: darwin-arm64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 178 ms: 1.11x slower                                                              |
| chameleon      | 4.60 ms                                                | 4.51 ms: 1.02x faster                                                             |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                            |
| html5lib       | 34.7 ms                                                | 33.6 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                             |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                              |
| nbody          | 65.6 ms                                                | 66.3 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 69.8 ms: 1.10x faster                                                             |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                              |
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                             |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 5.95 ms: 1.28x faster                                                             |
| xml_etree_parse      | 108 ms                                                 | 94.7 ms: 1.14x faster                                                             |
| unpickle_pure_python | 159 us                                                 | 143 us: 1.12x faster                                                              |
| pickle_pure_python   | 201 us                                                 | 187 us: 1.07x faster                                                              |
| xml_etree_iterparse  | 70.1 ms                                                | 66.3 ms: 1.06x faster                                                             |
| xml_etree_process    | 35.1 ms                                                | 35.0 ms: 1.00x faster                                                             |
| unpickle_list        | 2.65 us                                                | 2.66 us: 1.00x slower                                                             |
| pickle_dict          | 18.0 us                                                | 18.1 us: 1.01x slower                                                             |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                             |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                                             |
| xml_etree_generate   | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                             |
| unpickle             | 9.67 us                                                | 10.2 us: 1.05x slower                                                             |
| pickle               | 7.15 us                                                | 7.69 us: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.31 ms: 1.39x faster                                                             |
| python_startup         | 12.4 ms                                                | 9.33 ms: 1.33x faster                                                             |
| Geometric mean         | (ref)                                                  | 1.36x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 14.4 ms: 1.06x faster                                                             |
| genshi_xml      | 29.8 ms                                                | 28.5 ms: 1.04x faster                                                             |
| django_template | 21.0 ms                                                | 20.9 ms: 1.01x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 412 ms: 1.58x faster                                                              |
| python_startup_no_site  | 10.2 ms                                                | 7.31 ms: 1.39x faster                                                             |
| python_startup          | 12.4 ms                                                | 9.33 ms: 1.33x faster                                                             |
| pathlib                 | 27.2 ms                                                | 20.8 ms: 1.31x faster                                                             |
| json_dumps              | 7.63 ms                                                | 5.95 ms: 1.28x faster                                                             |
| unpack_sequence         | 34.1 ns                                                | 28.8 ns: 1.19x faster                                                             |
| xml_etree_parse         | 108 ms                                                 | 94.7 ms: 1.14x faster                                                             |
| fannkuch                | 261 ms                                                 | 232 ms: 1.12x faster                                                              |
| unpickle_pure_python    | 159 us                                                 | 143 us: 1.12x faster                                                              |
| richards                | 32.2 ms                                                | 28.9 ms: 1.11x faster                                                             |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.90 ms: 1.10x faster                                                             |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                                             |
| regex_compile           | 76.7 ms                                                | 69.8 ms: 1.10x faster                                                             |
| dulwich_log             | 30.3 ms                                                | 27.9 ms: 1.09x faster                                                             |
| logging_simple          | 3.55 us                                                | 3.30 us: 1.07x faster                                                             |
| pickle_pure_python      | 201 us                                                 | 187 us: 1.07x faster                                                              |
| chaos                   | 49.4 ms                                                | 46.1 ms: 1.07x faster                                                             |
| bench_thread_pool       | 474 us                                                 | 443 us: 1.07x faster                                                              |
| nqueens                 | 59.8 ms                                                | 55.9 ms: 1.07x faster                                                             |
| logging_silent          | 68.1 ns                                                | 63.7 ns: 1.07x faster                                                             |
| genshi_text             | 15.3 ms                                                | 14.4 ms: 1.06x faster                                                             |
| hexiom                  | 4.72 ms                                                | 4.44 ms: 1.06x faster                                                             |
| coroutines              | 17.8 ms                                                | 16.8 ms: 1.06x faster                                                             |
| xml_etree_iterparse     | 70.1 ms                                                | 66.3 ms: 1.06x faster                                                             |
| async_tree_memoization  | 336 ms                                                 | 317 ms: 1.06x faster                                                              |
| create_gc_cycles        | 716 us                                                 | 677 us: 1.06x faster                                                              |
| go                      | 109 ms                                                 | 103 ms: 1.06x faster                                                              |
| logging_format          | 3.78 us                                                | 3.59 us: 1.05x faster                                                             |
| pprint_pformat          | 954 ms                                                 | 910 ms: 1.05x faster                                                              |
| pycparser               | 698 ms                                                 | 667 ms: 1.05x faster                                                              |
| sympy_str               | 151 ms                                                 | 145 ms: 1.05x faster                                                              |
| genshi_xml              | 29.8 ms                                                | 28.5 ms: 1.04x faster                                                             |
| sympy_expand            | 242 ms                                                 | 232 ms: 1.04x faster                                                              |
| pprint_safe_repr        | 466 ms                                                 | 448 ms: 1.04x faster                                                              |
| coverage                | 58.4 ms                                                | 56.2 ms: 1.04x faster                                                             |
| deepcopy                | 223 us                                                 | 215 us: 1.04x faster                                                              |
| async_tree_none         | 286 ms                                                 | 276 ms: 1.04x faster                                                              |
| html5lib                | 34.7 ms                                                | 33.6 ms: 1.03x faster                                                             |
| mdp                     | 1.55 sec                                               | 1.50 sec: 1.03x faster                                                            |
| deepcopy_reduce         | 1.91 us                                                | 1.85 us: 1.03x faster                                                             |
| sympy_sum               | 85.5 ms                                                | 83.2 ms: 1.03x faster                                                             |
| deepcopy_memo           | 26.3 us                                                | 25.6 us: 1.03x faster                                                             |
| bench_mp_pool           | 43.9 ms                                                | 42.9 ms: 1.03x faster                                                             |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.02x faster                                                             |
| thrift                  | 442 us                                                 | 431 us: 1.02x faster                                                              |
| chameleon               | 4.60 ms                                                | 4.51 ms: 1.02x faster                                                             |
| float                   | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                             |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                              |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                            |
| async_tree_cpu_io_mixed | 533 ms                                                 | 530 ms: 1.01x faster                                                              |
| gc_traversal            | 2.42 ms                                                | 2.40 ms: 1.01x faster                                                             |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 46.5 ms                                                | 46.2 ms: 1.01x faster                                                             |
| sqlglot_normalize       | 171 ms                                                 | 170 ms: 1.00x faster                                                              |
| scimark_fft             | 200 ms                                                 | 199 ms: 1.00x faster                                                              |
| xml_etree_process       | 35.1 ms                                                | 35.0 ms: 1.00x faster                                                             |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                             |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x faster                                                             |
| async_generators        | 196 ms                                                 | 197 ms: 1.00x slower                                                              |
| unpickle_list           | 2.65 us                                                | 2.66 us: 1.00x slower                                                             |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                              |
| spectral_norm           | 72.6 ms                                                | 73.0 ms: 1.01x slower                                                             |
| crypto_pyaes            | 51.7 ms                                                | 52.0 ms: 1.01x slower                                                             |
| pickle_dict             | 18.0 us                                                | 18.1 us: 1.01x slower                                                             |
| nbody                   | 65.6 ms                                                | 66.3 ms: 1.01x slower                                                             |
| meteor_contest          | 73.5 ms                                                | 74.3 ms: 1.01x slower                                                             |
| telco                   | 3.41 ms                                                | 3.45 ms: 1.01x slower                                                             |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                             |
| scimark_sor             | 82.6 ms                                                | 84.0 ms: 1.02x slower                                                             |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                                             |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                                             |
| async_tree_io           | 704 ms                                                 | 720 ms: 1.02x slower                                                              |
| xml_etree_generate      | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                             |
| sqlglot_transpile       | 1.12 ms                                                | 1.15 ms: 1.02x slower                                                             |
| pyflate                 | 310 ms                                                 | 319 ms: 1.03x slower                                                              |
| scimark_lu              | 73.3 ms                                                | 75.7 ms: 1.03x slower                                                             |
| sqlglot_parse           | 959 us                                                 | 991 us: 1.03x slower                                                              |
| unpickle                | 9.67 us                                                | 10.2 us: 1.05x slower                                                             |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                                              |
| pickle                  | 7.15 us                                                | 7.69 us: 1.08x slower                                                             |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                                             |
| 2to3                    | 161 ms                                                 | 178 ms: 1.11x slower                                                              |
| generators              | 28.8 ms                                                | 33.7 ms: 1.17x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (2): mako, sqlglot_optimize
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (2) of results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: dask, mypy


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
