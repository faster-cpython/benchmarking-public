
# Results vs. 3.11.0

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.01x slower \*
- HPT reliability: 57.22%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.00x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.55 ms: 1.01x faster                                                 |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                | 33.8 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 66.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| regex_compile  | 76.7 ms                                                | 75.5 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 171 ms: 1.13x slower                                                  |
| regex_v8       | 16.1 ms                                                | 19.8 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 67.3 ms: 1.04x faster                                                 |
| pickle_dict          | 18.0 us                                                | 17.6 us: 1.02x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 157 us: 1.01x faster                                                  |
| json_loads           | 16.1 us                                                | 15.9 us: 1.01x faster                                                 |
| pickle_pure_python   | 201 us                                                 | 199 us: 1.01x faster                                                  |
| xml_etree_process    | 35.1 ms                                                | 35.2 ms: 1.00x slower                                                 |
| json_dumps           | 7.63 ms                                                | 7.68 ms: 1.01x slower                                                 |
| unpickle             | 9.67 us                                                | 9.87 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_list, unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.78 ms: 1.04x faster                                                 |
| python_startup         | 12.4 ms                                                | 12.1 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.21 ms: 1.04x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| django_template | 21.0 ms                                                | 21.2 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 32.0 ns: 1.07x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.69 ms: 1.05x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 67.3 ms: 1.04x faster                                                 |
| mako                    | 8.53 ms                                                | 8.21 ms: 1.04x faster                                                 |
| logging_simple          | 3.55 us                                                | 3.41 us: 1.04x faster                                                 |
| python_startup_no_site  | 10.2 ms                                                | 9.78 ms: 1.04x faster                                                 |
| async_tree_memoization  | 336 ms                                                 | 323 ms: 1.04x faster                                                  |
| sympy_sum               | 85.5 ms                                                | 82.6 ms: 1.04x faster                                                 |
| logging_format          | 3.78 us                                                | 3.65 us: 1.03x faster                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                                 |
| coroutines              | 17.8 ms                                                | 17.3 ms: 1.03x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.1 ms: 1.03x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.8 ms: 1.03x faster                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 45.3 ms: 1.03x faster                                                 |
| thrift                  | 442 us                                                 | 432 us: 1.02x faster                                                  |
| sympy_str               | 151 ms                                                 | 148 ms: 1.02x faster                                                  |
| pickle_dict             | 18.0 us                                                | 17.6 us: 1.02x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 25.8 us: 1.02x faster                                                 |
| pprint_safe_repr        | 466 ms                                                 | 457 ms: 1.02x faster                                                  |
| pprint_pformat          | 954 ms                                                 | 937 ms: 1.02x faster                                                  |
| generators              | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.5 ms: 1.02x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 72.2 ms: 1.02x faster                                                 |
| async_generators        | 196 ms                                                 | 193 ms: 1.02x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.55 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 159 us                                                 | 157 us: 1.01x faster                                                  |
| json_loads              | 16.1 us                                                | 15.9 us: 1.01x faster                                                 |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| genshi_text             | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| pickle_pure_python      | 201 us                                                 | 199 us: 1.01x faster                                                  |
| async_tree_none         | 286 ms                                                 | 283 ms: 1.01x faster                                                  |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| sympy_expand            | 242 ms                                                 | 241 ms: 1.01x faster                                                  |
| asyncio_tcp             | 651 ms                                                 | 648 ms: 1.01x faster                                                  |
| scimark_sor             | 82.6 ms                                                | 82.2 ms: 1.00x faster                                                 |
| telco                   | 3.41 ms                                                | 3.41 ms: 1.00x slower                                                 |
| mdp                     | 1.55 sec                                               | 1.55 sec: 1.00x slower                                                |
| xml_etree_process       | 35.1 ms                                                | 35.2 ms: 1.00x slower                                                 |
| fannkuch                | 261 ms                                                 | 262 ms: 1.00x slower                                                  |
| 2to3                    | 161 ms                                                 | 162 ms: 1.00x slower                                                  |
| chaos                   | 49.4 ms                                                | 49.7 ms: 1.01x slower                                                 |
| json_dumps              | 7.63 ms                                                | 7.68 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.21 ms: 1.01x slower                                                 |
| nbody                   | 65.6 ms                                                | 66.1 ms: 1.01x slower                                                 |
| django_template         | 21.0 ms                                                | 21.2 ms: 1.01x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 1.93 us: 1.01x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 63.3 ms: 1.01x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 73.4 ms: 1.01x slower                                                 |
| create_gc_cycles        | 716 us                                                 | 724 us: 1.01x slower                                                  |
| richards                | 32.2 ms                                                | 32.6 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 541 ms: 1.01x slower                                                  |
| nqueens                 | 59.8 ms                                                | 60.6 ms: 1.01x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 74.7 ms: 1.02x slower                                                 |
| json                    | 2.78 ms                                                | 2.82 ms: 1.02x slower                                                 |
| pyflate                 | 310 ms                                                 | 316 ms: 1.02x slower                                                  |
| deepcopy                | 223 us                                                 | 227 us: 1.02x slower                                                  |
| unpickle                | 9.67 us                                                | 9.87 us: 1.02x slower                                                 |
| logging_silent          | 68.1 ns                                                | 69.6 ns: 1.02x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.5 ms: 1.02x slower                                                 |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.37 ms: 1.02x slower                                                 |
| raytrace                | 207 ms                                                 | 212 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.9 ms: 1.03x slower                                                 |
| pycparser               | 698 ms                                                 | 717 ms: 1.03x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.88 ms: 1.03x slower                                                 |
| gunicorn                | 1.11 ms                                                | 1.15 ms: 1.04x slower                                                 |
| aiohttp                 | 1.05 ms                                                | 1.09 ms: 1.04x slower                                                 |
| bench_thread_pool       | 474 us                                                 | 499 us: 1.05x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.5 us: 1.08x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 56.5 ms: 1.09x slower                                                 |
| regex_dna               | 152 ms                                                 | 171 ms: 1.13x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.33 ms: 1.19x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.17 ms: 1.22x slower                                                 |
| regex_v8                | 16.1 ms                                                | 19.8 ms: 1.23x slower                                                 |
| mypy2                   | 195 ms                                                 | 251 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (16): bench_mp_pool, float, async_tree_io, dulwich_log, xml_etree_generate, gc_traversal, scimark_fft, pickle_list, unpickle_list, pickle, pidigits, sqlite_synth, flaskblogging, pathlib, tornado_http, pylint
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220405-3.11.0a7-2e49bd0/bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0.json: dask


# HPT report

- Reliability score: 57.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
