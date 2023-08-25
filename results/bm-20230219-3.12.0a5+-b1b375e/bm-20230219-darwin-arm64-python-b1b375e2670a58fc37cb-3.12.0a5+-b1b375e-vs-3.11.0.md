
# Results vs. 3.11.0

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: darwin-arm64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.01x faster \*
- HPT reliability: 66.29%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 4.60 ms                                                | 4.44 ms: 1.04x faster                                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                 |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                  |
| float          | 53.0 ms                                                | 52.4 ms: 1.01x faster                                                  |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.0 ms: 1.05x faster                                                  |
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 143 us: 1.12x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 97.6 ms: 1.11x faster                                                  |
| unpickle_list        | 2.65 us                                                | 2.57 us: 1.03x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 195 us: 1.03x faster                                                   |
| pickle_dict          | 18.0 us                                                | 18.1 us: 1.01x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 70.9 ms: 1.01x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 36.0 ms: 1.03x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 50.3 ms: 1.04x slower                                                  |
| pickle               | 7.15 us                                                | 7.56 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.36 ms: 1.16x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.3 ms: 1.07x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 28.3 ms: 1.05x faster                                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 441 ms: 1.48x faster                                                   |
| json_dumps              | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                  |
| mako                    | 8.53 ms                                                | 7.36 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.82 ms: 1.13x faster                                                  |
| generators              | 28.8 ms                                                | 25.5 ms: 1.13x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 143 us: 1.12x faster                                                   |
| xml_etree_parse         | 108 ms                                                 | 97.6 ms: 1.11x faster                                                  |
| hexiom                  | 4.72 ms                                                | 4.31 ms: 1.09x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.57 ms: 1.09x faster                                                  |
| richards                | 32.2 ms                                                | 30.0 ms: 1.07x faster                                                  |
| comprehensions          | 16.1 us                                                | 15.1 us: 1.07x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.3 ms: 1.07x faster                                                  |
| chaos                   | 49.4 ms                                                | 46.6 ms: 1.06x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.3 ms: 1.05x faster                                                  |
| regex_compile           | 76.7 ms                                                | 73.0 ms: 1.05x faster                                                  |
| pycparser               | 698 ms                                                 | 669 ms: 1.04x faster                                                   |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.44 ms: 1.04x faster                                                  |
| logging_silent          | 68.1 ns                                                | 65.8 ns: 1.03x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.57 us: 1.03x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 25.5 us: 1.03x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 195 us: 1.03x faster                                                   |
| scimark_fft             | 200 ms                                                 | 194 ms: 1.03x faster                                                   |
| sympy_str               | 151 ms                                                 | 147 ms: 1.03x faster                                                   |
| dulwich_log             | 30.3 ms                                                | 29.5 ms: 1.03x faster                                                  |
| nbody                   | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                  |
| regex_v8                | 16.1 ms                                                | 15.8 ms: 1.02x faster                                                  |
| sympy_sum               | 85.5 ms                                                | 83.8 ms: 1.02x faster                                                  |
| fannkuch                | 261 ms                                                 | 257 ms: 1.02x faster                                                   |
| create_gc_cycles        | 716 us                                                 | 703 us: 1.02x faster                                                   |
| bench_thread_pool       | 474 us                                                 | 466 us: 1.02x faster                                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| sympy_integrate         | 11.5 ms                                                | 11.3 ms: 1.02x faster                                                  |
| float                   | 53.0 ms                                                | 52.4 ms: 1.01x faster                                                  |
| deepcopy                | 223 us                                                 | 221 us: 1.01x faster                                                   |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.00x faster                                                 |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x faster                                                   |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 468 ms: 1.00x slower                                                   |
| go                      | 109 ms                                                 | 109 ms: 1.00x slower                                                   |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.23 ms: 1.00x slower                                                  |
| sympy_expand            | 242 ms                                                 | 243 ms: 1.01x slower                                                   |
| pickle_dict             | 18.0 us                                                | 18.1 us: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 70.9 ms: 1.01x slower                                                  |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                 |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 542 ms: 1.02x slower                                                   |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                   |
| sqlalchemy_declarative  | 62.6 ms                                                | 63.9 ms: 1.02x slower                                                  |
| nqueens                 | 59.8 ms                                                | 61.1 ms: 1.02x slower                                                  |
| telco                   | 3.41 ms                                                | 3.48 ms: 1.02x slower                                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.64 us: 1.02x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.9 ms: 1.03x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 36.0 ms: 1.03x slower                                                  |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.5 ms: 1.03x slower                                                  |
| logging_format          | 3.78 us                                                | 3.91 us: 1.03x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 75.2 ms: 1.04x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 76.3 ms: 1.04x slower                                                  |
| coverage                | 58.4 ms                                                | 60.9 ms: 1.04x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 50.3 ms: 1.04x slower                                                  |
| thrift                  | 442 us                                                 | 461 us: 1.04x slower                                                   |
| scimark_sor             | 82.6 ms                                                | 86.5 ms: 1.05x slower                                                  |
| bench_mp_pool           | 43.9 ms                                                | 46.2 ms: 1.05x slower                                                  |
| async_tree_io           | 704 ms                                                 | 745 ms: 1.06x slower                                                   |
| pickle                  | 7.15 us                                                | 7.56 us: 1.06x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                                  |
| pyflate                 | 310 ms                                                 | 328 ms: 1.06x slower                                                   |
| raytrace                | 207 ms                                                 | 223 ms: 1.08x slower                                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.22 ms: 1.09x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.05 ms: 1.10x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 52.7 ms: 1.13x slower                                                  |
| mypy2                   | 195 ms                                                 | 261 ms: 1.34x slower                                                   |
| async_generators        | 196 ms                                                 | 264 ms: 1.34x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (13): async_tree_memoization, tornado_http, pathlib, unpickle, json, scimark_lu, deepcopy_reduce, python_startup, pprint_pformat, 2to3, json_loads, async_tree_none, coroutines
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230219-3.12.0a5+-b1b375e/bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e.json: dask


# HPT report

- Reliability score: 66.29% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
