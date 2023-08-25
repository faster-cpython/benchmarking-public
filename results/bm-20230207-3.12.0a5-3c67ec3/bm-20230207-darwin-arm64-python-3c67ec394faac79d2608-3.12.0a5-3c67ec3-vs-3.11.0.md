
# Results vs. 3.11.0

- fork: python
- ref: 3c67ec394faac79d2608
- machine: darwin-arm64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.01x faster \*
- HPT reliability: 80.37%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                 |
| float          | 53.0 ms                                                | 52.1 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.3 ms: 1.06x faster                                                 |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.10 ms: 1.25x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.4 ms: 1.12x faster                                                 |
| pickle_pure_python   | 201 us                                                 | 192 us: 1.04x faster                                                  |
| pickle_list          | 2.81 us                                                | 2.76 us: 1.02x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 157 us: 1.02x faster                                                  |
| xml_etree_process    | 35.1 ms                                                | 34.6 ms: 1.01x faster                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| unpickle_list        | 2.65 us                                                | 2.68 us: 1.01x slower                                                 |
| unpickle             | 9.67 us                                                | 9.82 us: 1.01x slower                                                 |
| pickle               | 7.15 us                                                | 7.47 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): pickle_dict, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.4 ms: 1.00x faster                                                 |
| python_startup_no_site | 10.2 ms                                                | 10.3 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.19 ms: 1.19x faster                                                 |
| genshi_text     | 15.3 ms                                                | 14.2 ms: 1.08x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                 |
| django_template | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 436 ms: 1.49x faster                                                  |
| json_dumps              | 7.63 ms                                                | 6.10 ms: 1.25x faster                                                 |
| mako                    | 8.53 ms                                                | 7.19 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.80 ms: 1.14x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.4 ms: 1.12x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.57 ms: 1.09x faster                                                 |
| hexiom                  | 4.72 ms                                                | 4.32 ms: 1.09x faster                                                 |
| richards                | 32.2 ms                                                | 29.8 ms: 1.08x faster                                                 |
| chaos                   | 49.4 ms                                                | 45.7 ms: 1.08x faster                                                 |
| genshi_text             | 15.3 ms                                                | 14.2 ms: 1.08x faster                                                 |
| comprehensions          | 16.1 us                                                | 15.1 us: 1.07x faster                                                 |
| regex_compile           | 76.7 ms                                                | 72.3 ms: 1.06x faster                                                 |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                 |
| pycparser               | 698 ms                                                 | 664 ms: 1.05x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 192 us: 1.04x faster                                                  |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                 |
| sympy_sum               | 85.5 ms                                                | 82.1 ms: 1.04x faster                                                 |
| scimark_fft             | 200 ms                                                 | 192 ms: 1.04x faster                                                  |
| logging_silent          | 68.1 ns                                                | 65.8 ns: 1.04x faster                                                 |
| sympy_str               | 151 ms                                                 | 146 ms: 1.03x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 70.9 ms: 1.03x faster                                                 |
| dulwich_log             | 30.3 ms                                                | 29.4 ms: 1.03x faster                                                 |
| create_gc_cycles        | 716 us                                                 | 695 us: 1.03x faster                                                  |
| coverage                | 58.4 ms                                                | 56.8 ms: 1.03x faster                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                                 |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.01 ms: 1.03x faster                                                 |
| async_tree_memoization  | 336 ms                                                 | 327 ms: 1.03x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 463 us: 1.02x faster                                                  |
| nbody                   | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                 |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                                  |
| pickle_list             | 2.81 us                                                | 2.76 us: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| float                   | 53.0 ms                                                | 52.1 ms: 1.02x faster                                                 |
| unpickle_pure_python    | 159 us                                                 | 157 us: 1.02x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 26.0 us: 1.01x faster                                                 |
| xml_etree_process       | 35.1 ms                                                | 34.6 ms: 1.01x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                                |
| deepcopy                | 223 us                                                 | 220 us: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| regex_effbot            | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.4 ms: 1.00x faster                                                 |
| spectral_norm           | 72.6 ms                                                | 72.5 ms: 1.00x faster                                                 |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                                 |
| django_template         | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.00x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 469 ms: 1.00x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 62.9 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| json                    | 2.78 ms                                                | 2.79 ms: 1.01x slower                                                 |
| telco                   | 3.41 ms                                                | 3.43 ms: 1.01x slower                                                 |
| 2to3                    | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| sympy_expand            | 242 ms                                                 | 244 ms: 1.01x slower                                                  |
| go                      | 109 ms                                                 | 110 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 538 ms: 1.01x slower                                                  |
| pprint_pformat          | 954 ms                                                 | 963 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.93 us: 1.01x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 31.4 ms: 1.01x slower                                                 |
| unpickle_list           | 2.65 us                                                | 2.68 us: 1.01x slower                                                 |
| nqueens                 | 59.8 ms                                                | 60.6 ms: 1.01x slower                                                 |
| python_startup_no_site  | 10.2 ms                                                | 10.3 ms: 1.01x slower                                                 |
| unpickle                | 9.67 us                                                | 9.82 us: 1.01x slower                                                 |
| bench_mp_pool           | 43.9 ms                                                | 44.6 ms: 1.02x slower                                                 |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.8 ms: 1.02x slower                                                 |
| logging_simple          | 3.55 us                                                | 3.64 us: 1.03x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 75.6 ms: 1.03x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 85.3 ms: 1.03x slower                                                 |
| logging_format          | 3.78 us                                                | 3.91 us: 1.03x slower                                                 |
| pickle                  | 7.15 us                                                | 7.47 us: 1.05x slower                                                 |
| async_tree_io           | 704 ms                                                 | 742 ms: 1.05x slower                                                  |
| coroutines              | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.02 ms: 1.06x slower                                                 |
| pyflate                 | 310 ms                                                 | 331 ms: 1.07x slower                                                  |
| raytrace                | 207 ms                                                 | 221 ms: 1.07x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.08x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 50.0 ms: 1.08x slower                                                 |
| generators              | 28.8 ms                                                | 34.3 ms: 1.19x slower                                                 |
| mypy2                   | 195 ms                                                 | 260 ms: 1.33x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (10): tornado_http, async_tree_none, pickle_dict, xml_etree_iterparse, pidigits, chameleon, thrift, xml_etree_generate, html5lib, pathlib
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230207-3.12.0a5-3c67ec3/bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3.json: dask


# HPT report

- Reliability score: 80.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
