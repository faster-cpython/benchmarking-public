
# Results vs. 3.11.0

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: darwin-arm64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.02x slower \*
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.00x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.64 ms: 1.01x slower                                                 |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                                |
| html5lib       | 34.7 ms                                                | 33.8 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                 |
| float          | 53.0 ms                                                | 54.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.06 ms: 1.27x faster                                                 |
| regex_dna      | 152 ms                                                 | 142 ms: 1.07x faster                                                  |
| regex_v8       | 16.1 ms                                                | 15.1 ms: 1.06x faster                                                 |
| regex_compile  | 76.7 ms                                                | 77.9 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 18.0 us                                                | 17.2 us: 1.05x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.74 us: 1.03x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 69.0 ms: 1.02x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.63 us: 1.01x faster                                                 |
| pickle               | 7.15 us                                                | 7.16 us: 1.00x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 48.6 ms: 1.01x slower                                                 |
| json_dumps           | 7.63 ms                                                | 7.69 ms: 1.01x slower                                                 |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 35.5 ms: 1.01x slower                                                 |
| unpickle             | 9.67 us                                                | 9.90 us: 1.02x slower                                                 |
| pickle_pure_python   | 201 us                                                 | 219 us: 1.09x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 179 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.86 ms: 1.03x faster                                                 |
| python_startup         | 12.4 ms                                                | 12.1 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.45 ms: 1.01x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                 |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.06 ms: 1.27x faster                                                 |
| scimark_sor             | 82.6 ms                                                | 76.6 ms: 1.08x faster                                                 |
| regex_dna               | 152 ms                                                 | 142 ms: 1.07x faster                                                  |
| regex_v8                | 16.1 ms                                                | 15.1 ms: 1.06x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 32.4 ns: 1.05x faster                                                 |
| pickle_dict             | 18.0 us                                                | 17.2 us: 1.05x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.69 ms: 1.04x faster                                                 |
| python_startup_no_site  | 10.2 ms                                                | 9.86 ms: 1.03x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.8 ms: 1.03x faster                                                 |
| go                      | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| pickle_list             | 2.81 us                                                | 2.74 us: 1.03x faster                                                 |
| generators              | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.1 ms: 1.02x faster                                                 |
| nbody                   | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                                |
| xml_etree_iterparse     | 70.1 ms                                                | 69.0 ms: 1.02x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 72.2 ms: 1.02x faster                                                 |
| spectral_norm           | 72.6 ms                                                | 71.7 ms: 1.01x faster                                                 |
| logging_simple          | 3.55 us                                                | 3.51 us: 1.01x faster                                                 |
| raytrace                | 207 ms                                                 | 205 ms: 1.01x faster                                                  |
| sympy_sum               | 85.5 ms                                                | 84.6 ms: 1.01x faster                                                 |
| mako                    | 8.53 ms                                                | 8.45 ms: 1.01x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.63 us: 1.01x faster                                                 |
| telco                   | 3.41 ms                                                | 3.39 ms: 1.00x faster                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                | 62.5 ms: 1.00x faster                                                 |
| pickle                  | 7.15 us                                                | 7.16 us: 1.00x slower                                                 |
| thrift                  | 442 us                                                 | 443 us: 1.00x slower                                                  |
| 2to3                    | 161 ms                                                 | 162 ms: 1.00x slower                                                  |
| dulwich_log             | 30.3 ms                                                | 30.5 ms: 1.01x slower                                                 |
| logging_format          | 3.78 us                                                | 3.80 us: 1.01x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| mdp                     | 1.55 sec                                               | 1.56 sec: 1.01x slower                                                |
| xml_etree_generate      | 48.3 ms                                                | 48.6 ms: 1.01x slower                                                 |
| async_tree_io           | 704 ms                                                 | 710 ms: 1.01x slower                                                  |
| scimark_fft             | 200 ms                                                 | 201 ms: 1.01x slower                                                  |
| json_dumps              | 7.63 ms                                                | 7.69 ms: 1.01x slower                                                 |
| chameleon               | 4.60 ms                                                | 4.64 ms: 1.01x slower                                                 |
| create_gc_cycles        | 716 us                                                 | 723 us: 1.01x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.3 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| xml_etree_process       | 35.1 ms                                                | 35.5 ms: 1.01x slower                                                 |
| chaos                   | 49.4 ms                                                | 50.1 ms: 1.01x slower                                                 |
| coroutines              | 17.8 ms                                                | 18.0 ms: 1.01x slower                                                 |
| fannkuch                | 261 ms                                                 | 265 ms: 1.01x slower                                                  |
| regex_compile           | 76.7 ms                                                | 77.9 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 542 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.24 ms: 1.02x slower                                                 |
| pycparser               | 698 ms                                                 | 710 ms: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.02x slower                                                 |
| hexiom                  | 4.72 ms                                                | 4.82 ms: 1.02x slower                                                 |
| sympy_str               | 151 ms                                                 | 154 ms: 1.02x slower                                                  |
| float                   | 53.0 ms                                                | 54.1 ms: 1.02x slower                                                 |
| unpickle                | 9.67 us                                                | 9.90 us: 1.02x slower                                                 |
| async_tree_none         | 286 ms                                                 | 292 ms: 1.02x slower                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.38 ms: 1.02x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                 |
| nqueens                 | 59.8 ms                                                | 61.3 ms: 1.03x slower                                                 |
| json                    | 2.78 ms                                                | 2.85 ms: 1.03x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                                  |
| sympy_expand            | 242 ms                                                 | 250 ms: 1.03x slower                                                  |
| pyflate                 | 310 ms                                                 | 320 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                 |
| gunicorn                | 1.11 ms                                                | 1.15 ms: 1.04x slower                                                 |
| logging_silent          | 68.1 ns                                                | 70.7 ns: 1.04x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 76.6 ms: 1.04x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 32.4 ms: 1.04x slower                                                 |
| bench_thread_pool       | 474 us                                                 | 499 us: 1.05x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.34 us: 1.05x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 49.3 ms: 1.06x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 357 ms: 1.06x slower                                                  |
| richards                | 32.2 ms                                                | 34.3 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 499 ms: 1.07x slower                                                  |
| pprint_pformat          | 954 ms                                                 | 1.03 sec: 1.08x slower                                                |
| pickle_pure_python      | 201 us                                                 | 219 us: 1.09x slower                                                  |
| deepcopy                | 223 us                                                 | 244 us: 1.10x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.11 us: 1.10x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 29.1 us: 1.11x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 179 us: 1.12x slower                                                  |
| comprehensions          | 16.1 us                                                | 19.2 us: 1.19x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.38 ms: 1.23x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.21 ms: 1.26x slower                                                 |
| mypy2                   | 195 ms                                                 | 251 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (9): bench_mp_pool, pathlib, tornado_http, gc_traversal, asyncio_tcp, pidigits, flaskblogging, pylint, aiohttp
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220506-3.11.0b1-8d32a5c/bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json: dask


# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
