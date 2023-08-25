
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: darwin-arm64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.01x slower \*
- HPT reliability: 85.09%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 161 ms: 1.00x faster                                       |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                     |
| html5lib       | 34.7 ms                                                | 35.9 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.7 ms: 1.03x faster                                      |
| float          | 53.0 ms                                                | 55.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.40 ms: 1.10x faster                                      |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                       |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.01x slower                                      |
| regex_compile  | 76.7 ms                                                | 77.8 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 18.0 us                                                | 17.1 us: 1.05x faster                                      |
| pickle_list          | 2.81 us                                                | 2.72 us: 1.03x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                       |
| xml_etree_iterparse  | 70.1 ms                                                | 69.2 ms: 1.01x faster                                      |
| pickle               | 7.15 us                                                | 7.07 us: 1.01x faster                                      |
| xml_etree_process    | 35.1 ms                                                | 34.8 ms: 1.01x faster                                      |
| xml_etree_generate   | 48.3 ms                                                | 48.1 ms: 1.00x faster                                      |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                      |
| json_dumps           | 7.63 ms                                                | 7.69 ms: 1.01x slower                                      |
| unpickle_list        | 2.65 us                                                | 2.69 us: 1.01x slower                                      |
| unpickle             | 9.67 us                                                | 10.0 us: 1.03x slower                                      |
| unpickle_pure_python | 159 us                                                 | 175 us: 1.10x slower                                       |
| pickle_pure_python   | 201 us                                                 | 222 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.4 ms: 1.01x faster                                      |
| python_startup_no_site | 10.2 ms                                                | 10.1 ms: 1.00x faster                                      |
| Geometric mean         | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako           | 8.53 ms                                                | 8.42 ms: 1.01x faster                                      |
| genshi_text    | 15.3 ms                                                | 15.2 ms: 1.01x faster                                      |
| genshi_xml     | 29.8 ms                                                | 30.4 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.40 ms: 1.10x faster                                      |
| scimark_sor             | 82.6 ms                                                | 76.7 ms: 1.08x faster                                      |
| unpack_sequence         | 34.1 ns                                                | 32.3 ns: 1.06x faster                                      |
| pickle_dict             | 18.0 us                                                | 17.1 us: 1.05x faster                                      |
| generators              | 28.8 ms                                                | 27.6 ms: 1.04x faster                                      |
| logging_silent          | 68.1 ns                                                | 65.5 ns: 1.04x faster                                      |
| sympy_sum               | 85.5 ms                                                | 82.8 ms: 1.03x faster                                      |
| pickle_list             | 2.81 us                                                | 2.72 us: 1.03x faster                                      |
| nbody                   | 65.6 ms                                                | 63.7 ms: 1.03x faster                                      |
| scimark_lu              | 73.3 ms                                                | 71.3 ms: 1.03x faster                                      |
| logging_simple          | 3.55 us                                                | 3.47 us: 1.02x faster                                      |
| coroutines              | 17.8 ms                                                | 17.4 ms: 1.02x faster                                      |
| nqueens                 | 59.8 ms                                                | 58.6 ms: 1.02x faster                                      |
| xml_etree_parse         | 108 ms                                                 | 106 ms: 1.02x faster                                       |
| thrift                  | 442 us                                                 | 434 us: 1.02x faster                                       |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                       |
| xml_etree_iterparse     | 70.1 ms                                                | 69.2 ms: 1.01x faster                                      |
| mako                    | 8.53 ms                                                | 8.42 ms: 1.01x faster                                      |
| bench_thread_pool       | 474 us                                                 | 469 us: 1.01x faster                                       |
| pickle                  | 7.15 us                                                | 7.07 us: 1.01x faster                                      |
| xml_etree_process       | 35.1 ms                                                | 34.8 ms: 1.01x faster                                      |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                     |
| logging_format          | 3.78 us                                                | 3.75 us: 1.01x faster                                      |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                     |
| fannkuch                | 261 ms                                                 | 260 ms: 1.01x faster                                       |
| sqlalchemy_declarative  | 62.6 ms                                                | 62.2 ms: 1.01x faster                                      |
| genshi_text             | 15.3 ms                                                | 15.2 ms: 1.01x faster                                      |
| hexiom                  | 4.72 ms                                                | 4.69 ms: 1.01x faster                                      |
| python_startup          | 12.4 ms                                                | 12.4 ms: 1.01x faster                                      |
| xml_etree_generate      | 48.3 ms                                                | 48.1 ms: 1.00x faster                                      |
| python_startup_no_site  | 10.2 ms                                                | 10.1 ms: 1.00x faster                                      |
| go                      | 109 ms                                                 | 108 ms: 1.00x faster                                       |
| spectral_norm           | 72.6 ms                                                | 72.4 ms: 1.00x faster                                      |
| 2to3                    | 161 ms                                                 | 161 ms: 1.00x faster                                       |
| gc_traversal            | 2.42 ms                                                | 2.41 ms: 1.00x faster                                      |
| raytrace                | 207 ms                                                 | 207 ms: 1.00x slower                                       |
| deltablue               | 2.81 ms                                                | 2.82 ms: 1.00x slower                                      |
| scimark_fft             | 200 ms                                                 | 200 ms: 1.00x slower                                       |
| sqlglot_normalize       | 171 ms                                                 | 171 ms: 1.00x slower                                       |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.21 ms: 1.00x slower                                      |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                      |
| sympy_expand            | 242 ms                                                 | 243 ms: 1.01x slower                                       |
| async_tree_io           | 704 ms                                                 | 710 ms: 1.01x slower                                       |
| regex_v8                | 16.1 ms                                                | 16.2 ms: 1.01x slower                                      |
| json_dumps              | 7.63 ms                                                | 7.69 ms: 1.01x slower                                      |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                      |
| async_tree_cpu_io_mixed | 533 ms                                                 | 540 ms: 1.01x slower                                       |
| async_generators        | 196 ms                                                 | 199 ms: 1.01x slower                                       |
| regex_compile           | 76.7 ms                                                | 77.8 ms: 1.01x slower                                      |
| pyflate                 | 310 ms                                                 | 314 ms: 1.01x slower                                       |
| unpickle_list           | 2.65 us                                                | 2.69 us: 1.01x slower                                      |
| sqlglot_optimize        | 31.1 ms                                                | 31.6 ms: 1.02x slower                                      |
| create_gc_cycles        | 716 us                                                 | 727 us: 1.02x slower                                       |
| async_tree_none         | 286 ms                                                 | 290 ms: 1.02x slower                                       |
| genshi_xml              | 29.8 ms                                                | 30.4 ms: 1.02x slower                                      |
| pathlib                 | 27.2 ms                                                | 27.8 ms: 1.02x slower                                      |
| json                    | 2.78 ms                                                | 2.84 ms: 1.02x slower                                      |
| richards                | 32.2 ms                                                | 33.3 ms: 1.03x slower                                      |
| unpickle                | 9.67 us                                                | 10.0 us: 1.03x slower                                      |
| html5lib                | 34.7 ms                                                | 35.9 ms: 1.03x slower                                      |
| float                   | 53.0 ms                                                | 55.0 ms: 1.04x slower                                      |
| async_tree_memoization  | 336 ms                                                 | 350 ms: 1.04x slower                                       |
| scimark_monte_carlo     | 46.5 ms                                                | 48.7 ms: 1.05x slower                                      |
| pprint_safe_repr        | 466 ms                                                 | 489 ms: 1.05x slower                                       |
| sqlite_synth            | 1.27 us                                                | 1.34 us: 1.05x slower                                      |
| pprint_pformat          | 954 ms                                                 | 1.00 sec: 1.05x slower                                     |
| meteor_contest          | 73.5 ms                                                | 77.6 ms: 1.06x slower                                      |
| deepcopy_reduce         | 1.91 us                                                | 2.04 us: 1.07x slower                                      |
| deepcopy                | 223 us                                                 | 238 us: 1.07x slower                                       |
| deepcopy_memo           | 26.3 us                                                | 28.9 us: 1.10x slower                                      |
| unpickle_pure_python    | 159 us                                                 | 175 us: 1.10x slower                                       |
| pickle_pure_python      | 201 us                                                 | 222 us: 1.11x slower                                       |
| comprehensions          | 16.1 us                                                | 18.3 us: 1.14x slower                                      |
| sqlglot_transpile       | 1.12 ms                                                | 1.35 ms: 1.20x slower                                      |
| sqlglot_parse           | 959 us                                                 | 1.19 ms: 1.24x slower                                      |
| mypy2                   | 195 ms                                                 | 249 ms: 1.27x slower                                       |
| Geometric mean          | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (17): tornado_http, bench_mp_pool, pylint, sympy_str, sqlalchemy_imperative, flaskblogging, chaos, pidigits, telco, chameleon, crypto_pyaes, django_template, pycparser, asyncio_tcp, dulwich_log, gunicorn, aiohttp
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220601-3.11.0b3-eb0004c/bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c.json: dask


# HPT report

- Reliability score: 85.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
