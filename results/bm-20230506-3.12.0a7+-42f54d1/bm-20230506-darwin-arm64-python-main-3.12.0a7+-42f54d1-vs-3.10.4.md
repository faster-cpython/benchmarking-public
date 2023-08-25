
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.16x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 174 ms: 1.16x faster                                   |
| docutils       | 1.78 sec                                               | 1.57 sec: 1.14x faster                                 |
| tornado_http   | 91.9 ms                                                | 69.5 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.4 ms: 1.36x faster                                  |
| float          | 72.3 ms                                                | 59.6 ms: 1.21x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 78.7 ms: 1.23x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.3 ms: 1.08x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.70 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.35x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.95 ms: 1.20x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 40.4 ms: 1.12x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.01x slower                                   |
| xml_etree_iterparse  | 72.6 ms                                                | 75.2 ms: 1.04x slower                                  |
| unpickle             | 9.77 us                                                | 10.1 us: 1.04x slower                                  |
| json_loads           | 16.9 us                                                | 17.8 us: 1.05x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.9 us: 1.06x slower                                  |
| xml_etree_generate   | 54.3 ms                                                | 58.6 ms: 1.08x slower                                  |
| pickle               | 7.36 us                                                | 7.95 us: 1.08x slower                                  |
| pickle_list          | 2.83 us                                                | 3.17 us: 1.12x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.24 us: 1.22x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.73 ms                                                | 10.5 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.79 ms: 1.35x faster                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.47 ms: 2.09x faster                                  |
| logging_silent          | 119 ns                                                 | 69.6 ns: 1.71x faster                                  |
| richards                | 51.4 ms                                                | 32.3 ms: 1.59x faster                                  |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                   |
| sqlglot_parse           | 1.33 ms                                                | 902 us: 1.48x faster                                   |
| scimark_sor             | 127 ms                                                 | 86.6 ms: 1.46x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 461 ms: 1.46x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.33 ms: 1.46x faster                                  |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                   |
| async_tree_memoization  | 493 ms                                                 | 342 ms: 1.44x faster                                   |
| async_tree_io           | 1.02 sec                                               | 716 ms: 1.42x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.08 ms: 1.42x faster                                  |
| async_tree_none         | 402 ms                                                 | 286 ms: 1.40x faster                                   |
| crypto_pyaes            | 78.0 ms                                                | 55.9 ms: 1.40x faster                                  |
| chaos                   | 66.8 ms                                                | 48.0 ms: 1.39x faster                                  |
| unpack_sequence         | 38.7 ns                                                | 28.0 ns: 1.38x faster                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 52.7 ms: 1.37x faster                                  |
| nbody                   | 94.1 ms                                                | 69.4 ms: 1.36x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.35x faster                                   |
| mako                    | 10.5 ms                                                | 7.79 ms: 1.35x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 25.6 us: 1.34x faster                                  |
| scimark_lu              | 110 ms                                                 | 82.2 ms: 1.34x faster                                  |
| generators              | 32.9 ms                                                | 24.9 ms: 1.33x faster                                  |
| tornado_http            | 91.9 ms                                                | 69.5 ms: 1.32x faster                                  |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                   |
| raytrace                | 328 ms                                                 | 250 ms: 1.31x faster                                   |
| pycparser               | 915 ms                                                 | 702 ms: 1.30x faster                                   |
| create_gc_cycles        | 876 us                                                 | 698 us: 1.26x faster                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 538 ms: 1.25x faster                                   |
| logging_format          | 5.01 us                                                | 4.02 us: 1.25x faster                                  |
| logging_simple          | 4.63 us                                                | 3.72 us: 1.24x faster                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.27 ms: 1.24x faster                                  |
| regex_compile           | 96.6 ms                                                | 78.7 ms: 1.23x faster                                  |
| spectral_norm           | 96.4 ms                                                | 79.1 ms: 1.22x faster                                  |
| float                   | 72.3 ms                                                | 59.6 ms: 1.21x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.7 ms: 1.21x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.95 ms: 1.20x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 1.04 sec: 1.20x faster                                 |
| pprint_safe_repr        | 609 ms                                                 | 511 ms: 1.19x faster                                   |
| 2to3                    | 202 ms                                                 | 174 ms: 1.16x faster                                   |
| deepcopy                | 278 us                                                 | 240 us: 1.16x faster                                   |
| mypy2                   | 308 ms                                                 | 267 ms: 1.16x faster                                   |
| fannkuch                | 317 ms                                                 | 276 ms: 1.15x faster                                   |
| docutils                | 1.78 sec                                               | 1.57 sec: 1.14x faster                                 |
| coroutines              | 20.2 ms                                                | 18.0 ms: 1.12x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 40.4 ms: 1.12x faster                                  |
| deepcopy_reduce         | 2.38 us                                                | 2.14 us: 1.11x faster                                  |
| scimark_fft             | 232 ms                                                 | 210 ms: 1.10x faster                                   |
| bench_thread_pool       | 548 us                                                 | 497 us: 1.10x faster                                   |
| sqlalchemy_declarative  | 74.8 ms                                                | 68.6 ms: 1.09x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.3 ms: 1.08x faster                                  |
| meteor_contest          | 78.6 ms                                                | 73.4 ms: 1.07x faster                                  |
| nqueens                 | 68.1 ms                                                | 63.6 ms: 1.07x faster                                  |
| regex_dna               | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| mdp                     | 1.67 sec                                               | 1.57 sec: 1.06x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 36.6 ms: 1.04x faster                                  |
| pathlib                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                  |
| json                    | 3.10 ms                                                | 3.04 ms: 1.02x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.44 ms: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                  |
| comprehensions          | 17.7 us                                                | 17.9 us: 1.01x slower                                  |
| xml_etree_parse         | 107 ms                                                 | 109 ms: 1.01x slower                                   |
| sqlglot_normalize       | 197 ms                                                 | 200 ms: 1.02x slower                                   |
| xml_etree_iterparse     | 72.6 ms                                                | 75.2 ms: 1.04x slower                                  |
| unpickle                | 9.77 us                                                | 10.1 us: 1.04x slower                                  |
| json_loads              | 16.9 us                                                | 17.8 us: 1.05x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.9 us: 1.06x slower                                  |
| sqlite_synth            | 1.47 us                                                | 1.58 us: 1.08x slower                                  |
| xml_etree_generate      | 54.3 ms                                                | 58.6 ms: 1.08x slower                                  |
| pickle                  | 7.36 us                                                | 7.95 us: 1.08x slower                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.5 ms: 1.08x slower                                  |
| telco                   | 3.68 ms                                                | 4.04 ms: 1.10x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.70 ms: 1.10x slower                                  |
| pickle_list             | 2.83 us                                                | 3.17 us: 1.12x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 48.1 ms: 1.17x slower                                  |
| unpickle_list           | 2.66 us                                                | 3.24 us: 1.22x slower                                  |
| dask                    | 258 ms                                                 | 334 ms: 1.29x slower                                   |
| async_generators        | 233 ms                                                 | 316 ms: 1.35x slower                                   |
| coverage                | 40.8 ms                                                | 59.1 ms: 1.45x slower                                  |
| Geometric mean          | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x
