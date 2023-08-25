
# Results vs. 3.11.0

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: darwin-arm64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.02x slower \*
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.03x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.58 ms: 1.00x faster                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 36.5 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.7 ms: 1.01x faster                                                 |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 53.0 ms                                                | 56.4 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 76.0 ms: 1.01x faster                                                 |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.00x slower                                                 |
| regex_dna      | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| regex_effbot   | 2.63 ms                                                | 2.68 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.14 ms: 1.24x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 93.9 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 68.2 ms: 1.03x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.58 us: 1.03x faster                                                 |
| xml_etree_generate   | 48.3 ms                                                | 47.2 ms: 1.02x faster                                                 |
| xml_etree_process    | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.82 us: 1.00x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                                  |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                 |
| pickle_pure_python   | 201 us                                                 | 208 us: 1.04x slower                                                  |
| pickle               | 7.15 us                                                | 7.62 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.1 ms: 1.03x faster                                                 |
| python_startup_no_site | 10.2 ms                                                | 10.0 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.16 ms: 1.05x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.5 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 7.63 ms                                                | 6.14 ms: 1.24x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 93.9 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.78 ms: 1.15x faster                                                 |
| coverage                | 58.4 ms                                                | 53.1 ms: 1.10x faster                                                 |
| mako                    | 8.53 ms                                                | 8.16 ms: 1.05x faster                                                 |
| create_gc_cycles        | 716 us                                                 | 693 us: 1.03x faster                                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 68.2 ms: 1.03x faster                                                 |
| logging_silent          | 68.1 ns                                                | 66.2 ns: 1.03x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.58 us: 1.03x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.1 ms: 1.03x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.74 ms: 1.03x faster                                                 |
| telco                   | 3.41 ms                                                | 3.32 ms: 1.03x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 33.3 ns: 1.02x faster                                                 |
| xml_etree_generate      | 48.3 ms                                                | 47.2 ms: 1.02x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 72.2 ms: 1.02x faster                                                 |
| scimark_fft             | 200 ms                                                 | 197 ms: 1.02x faster                                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.0 ms: 1.01x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.52 sec: 1.01x faster                                                |
| nbody                   | 65.6 ms                                                | 64.7 ms: 1.01x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 468 us: 1.01x faster                                                  |
| regex_compile           | 76.7 ms                                                | 76.0 ms: 1.01x faster                                                 |
| chameleon               | 4.60 ms                                                | 4.58 ms: 1.00x faster                                                 |
| xml_etree_process       | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| pickle_dict             | 18.0 us                                                | 17.9 us: 1.00x faster                                                 |
| thrift                  | 442 us                                                 | 441 us: 1.00x faster                                                  |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x faster                                                  |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                                 |
| regex_v8                | 16.1 ms                                                | 16.2 ms: 1.00x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.82 us: 1.00x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 72.9 ms: 1.00x slower                                                 |
| regex_dna               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| sympy_sum               | 85.5 ms                                                | 86.4 ms: 1.01x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.5 ms: 1.01x slower                                                 |
| sympy_str               | 151 ms                                                 | 153 ms: 1.01x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                                 |
| nqueens                 | 59.8 ms                                                | 60.6 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.02x slower                                                 |
| json                    | 2.78 ms                                                | 2.82 ms: 1.02x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.02x slower                                                  |
| pathlib                 | 27.2 ms                                                | 27.7 ms: 1.02x slower                                                 |
| regex_effbot            | 2.63 ms                                                | 2.68 ms: 1.02x slower                                                 |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                 |
| sympy_expand            | 242 ms                                                 | 247 ms: 1.02x slower                                                  |
| chaos                   | 49.4 ms                                                | 50.4 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 201 ms: 1.02x slower                                                  |
| async_tree_none         | 286 ms                                                 | 292 ms: 1.02x slower                                                  |
| 2to3                    | 161 ms                                                 | 165 ms: 1.03x slower                                                  |
| fannkuch                | 261 ms                                                 | 268 ms: 1.03x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.66 us: 1.03x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 32.1 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 551 ms: 1.03x slower                                                  |
| pickle_pure_python      | 201 us                                                 | 208 us: 1.04x slower                                                  |
| django_template         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 992 ms: 1.04x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 486 ms: 1.04x slower                                                  |
| richards                | 32.2 ms                                                | 33.6 ms: 1.04x slower                                                 |
| hexiom                  | 4.72 ms                                                | 4.93 ms: 1.04x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 76.9 ms: 1.05x slower                                                 |
| comprehensions          | 16.1 us                                                | 16.9 us: 1.05x slower                                                 |
| logging_format          | 3.78 us                                                | 3.96 us: 1.05x slower                                                 |
| html5lib                | 34.7 ms                                                | 36.5 ms: 1.05x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.01 ms: 1.06x slower                                                 |
| async_tree_io           | 704 ms                                                 | 748 ms: 1.06x slower                                                  |
| float                   | 53.0 ms                                                | 56.4 ms: 1.06x slower                                                 |
| pickle                  | 7.15 us                                                | 7.62 us: 1.07x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 2.04 us: 1.07x slower                                                 |
| coroutines              | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                                  |
| deepcopy                | 223 us                                                 | 241 us: 1.08x slower                                                  |
| go                      | 109 ms                                                 | 119 ms: 1.10x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 29.1 us: 1.11x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.42 us: 1.12x slower                                                 |
| pyflate                 | 310 ms                                                 | 351 ms: 1.13x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 54.5 ms: 1.17x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 100 ms: 1.22x slower                                                  |
| mypy2                   | 195 ms                                                 | 265 ms: 1.36x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (10): async_tree_memoization, tornado_http, pylint, bench_mp_pool, asyncio_tcp, genshi_xml, dulwich_log, crypto_pyaes, unpickle, pycparser
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221025-3.12.0a1-4ae1a0e/bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e.json: dask


# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
