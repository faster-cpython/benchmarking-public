
# Results vs. 3.11.0

- fork: python
- ref: 2b428a1faed88f148ede
- machine: darwin-arm64
- commit hash: 2b428a1
- commit date: 2022-09-26
- overall geometric mean: 1.00x slower \*
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.67 ms: 1.02x slower                                                 |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.8 ms: 1.01x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 56.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| regex_dna      | 152 ms                                                 | 152 ms: 1.00x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                 |
| regex_v8       | 16.1 ms                                                | 16.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.09 ms: 1.25x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.6 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 65.2 ms: 1.08x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.54 us: 1.04x faster                                                 |
| xml_etree_generate   | 48.3 ms                                                | 47.6 ms: 1.01x faster                                                 |
| xml_etree_process    | 35.1 ms                                                | 35.0 ms: 1.00x faster                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.01x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                                 |
| pickle_pure_python   | 201 us                                                 | 205 us: 1.02x slower                                                  |
| pickle               | 7.15 us                                                | 7.55 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.15 ms: 1.42x faster                                                 |
| python_startup         | 12.4 ms                                                | 9.08 ms: 1.37x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.16 ms: 1.05x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.2 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.15 ms: 1.42x faster                                                 |
| python_startup          | 12.4 ms                                                | 9.08 ms: 1.37x faster                                                 |
| pathlib                 | 27.2 ms                                                | 20.6 ms: 1.32x faster                                                 |
| json_dumps              | 7.63 ms                                                | 6.09 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.83 ms: 1.13x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.6 ms: 1.12x faster                                                 |
| flaskblogging           | 2.43 ms                                                | 2.22 ms: 1.09x faster                                                 |
| coverage                | 58.4 ms                                                | 53.7 ms: 1.09x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 65.2 ms: 1.08x faster                                                 |
| bench_mp_pool           | 43.9 ms                                                | 41.2 ms: 1.07x faster                                                 |
| mako                    | 8.53 ms                                                | 8.16 ms: 1.05x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.54 us: 1.04x faster                                                 |
| dulwich_log             | 30.3 ms                                                | 29.1 ms: 1.04x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 455 us: 1.04x faster                                                  |
| pylint                  | 272 ms                                                 | 264 ms: 1.03x faster                                                  |
| logging_silent          | 68.1 ns                                                | 66.2 ns: 1.03x faster                                                 |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.00 ms: 1.03x faster                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                | 61.3 ms: 1.02x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.52 sec: 1.01x faster                                                |
| regex_compile           | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| telco                   | 3.41 ms                                                | 3.36 ms: 1.01x faster                                                 |
| xml_etree_generate      | 48.3 ms                                                | 47.6 ms: 1.01x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 72.3 ms: 1.01x faster                                                 |
| nbody                   | 65.6 ms                                                | 64.8 ms: 1.01x faster                                                 |
| xml_etree_process       | 35.1 ms                                                | 35.0 ms: 1.00x faster                                                 |
| regex_dna               | 152 ms                                                 | 152 ms: 1.00x faster                                                  |
| scimark_fft             | 200 ms                                                 | 199 ms: 1.00x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                 |
| thrift                  | 442 us                                                 | 442 us: 1.00x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 51.8 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 85.9 ms: 1.00x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 72.9 ms: 1.00x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.83 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.2 ms: 1.01x slower                                                 |
| json                    | 2.78 ms                                                | 2.81 ms: 1.01x slower                                                 |
| sympy_str               | 151 ms                                                 | 153 ms: 1.01x slower                                                  |
| regex_v8                | 16.1 ms                                                | 16.3 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.01x slower                                                  |
| chameleon               | 4.60 ms                                                | 4.67 ms: 1.02x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                                 |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| pycparser               | 698 ms                                                 | 713 ms: 1.02x slower                                                  |
| pickle_pure_python      | 201 us                                                 | 205 us: 1.02x slower                                                  |
| nqueens                 | 59.8 ms                                                | 61.2 ms: 1.02x slower                                                 |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.9 ms: 1.03x slower                                                 |
| chaos                   | 49.4 ms                                                | 50.9 ms: 1.03x slower                                                 |
| richards                | 32.2 ms                                                | 33.2 ms: 1.03x slower                                                 |
| fannkuch                | 261 ms                                                 | 270 ms: 1.03x slower                                                  |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| raytrace                | 207 ms                                                 | 214 ms: 1.03x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.67 us: 1.04x slower                                                 |
| django_template         | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1000 us: 1.04x slower                                                 |
| hexiom                  | 4.72 ms                                                | 4.92 ms: 1.04x slower                                                 |
| logging_format          | 3.78 us                                                | 3.95 us: 1.04x slower                                                 |
| async_tree_io           | 704 ms                                                 | 736 ms: 1.04x slower                                                  |
| pprint_pformat          | 954 ms                                                 | 1.00 sec: 1.05x slower                                                |
| pickle                  | 7.15 us                                                | 7.55 us: 1.06x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 495 ms: 1.06x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 78.2 ms: 1.06x slower                                                 |
| float                   | 53.0 ms                                                | 56.5 ms: 1.07x slower                                                 |
| deepcopy                | 223 us                                                 | 241 us: 1.08x slower                                                  |
| go                      | 109 ms                                                 | 118 ms: 1.08x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.08 us: 1.09x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.7 us: 1.09x slower                                                 |
| coroutines              | 17.8 ms                                                | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 310 ms                                                 | 351 ms: 1.13x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 383 ms: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.46 us: 1.15x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 54.3 ms: 1.17x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 102 ms: 1.23x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (7): tornado_http, async_tree_none, async_tree_cpu_io_mixed, unpack_sequence, pickle_dict, docutils, unpickle
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220926-3.12.0a0-2b428a1/bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1.json: mypy


# HPT report

- Reliability score: 98.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
