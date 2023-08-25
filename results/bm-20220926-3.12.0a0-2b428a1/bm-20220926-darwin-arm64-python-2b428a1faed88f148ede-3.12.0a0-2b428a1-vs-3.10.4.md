
# Results vs. 3.10.4

- fork: python
- ref: 2b428a1faed88f148ede
- machine: darwin-arm64
- commit hash: 2b428a1
- commit date: 2022-09-26
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 185 ms: 1.10x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.67 ms: 1.25x faster                                                 |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| html5lib       | 44.1 ms                                                | 35.8 ms: 1.23x faster                                                 |
| tornado_http   | 91.9 ms                                                | 69.4 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 64.8 ms: 1.45x faster                                                 |
| float          | 72.3 ms                                                | 56.5 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.6 ms: 1.28x faster                                                 |
| regex_v8       | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                 |
| regex_dna      | 160 ms                                                 | 152 ms: 1.05x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.09 ms: 1.38x faster                                                 |
| xml_etree_process    | 45.1 ms                                                | 35.0 ms: 1.29x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                                  |
| xml_etree_generate   | 54.3 ms                                                | 47.6 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 65.2 ms: 1.11x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 96.6 ms: 1.11x faster                                                 |
| unpickle_list        | 2.66 us                                                | 2.54 us: 1.05x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle_list          | 2.83 us                                                | 2.86 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.55 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.08 ms: 1.39x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 7.15 ms: 1.36x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.16 ms: 1.28x faster                                                 |
| django_template | 27.3 ms                                                | 21.8 ms: 1.25x faster                                                 |
| genshi_xml      | 37.6 ms                                                | 30.2 ms: 1.25x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.83 ms: 1.82x faster                                                 |
| logging_silent          | 119 ns                                                 | 66.2 ns: 1.80x faster                                                 |
| richards                | 51.4 ms                                                | 33.2 ms: 1.55x faster                                                 |
| raytrace                | 328 ms                                                 | 214 ms: 1.53x faster                                                  |
| scimark_lu              | 110 ms                                                 | 72.3 ms: 1.52x faster                                                 |
| crypto_pyaes            | 78.0 ms                                                | 51.8 ms: 1.51x faster                                                 |
| nbody                   | 94.1 ms                                                | 64.8 ms: 1.45x faster                                                 |
| async_tree_none         | 402 ms                                                 | 285 ms: 1.41x faster                                                  |
| go                      | 165 ms                                                 | 118 ms: 1.40x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.40x faster                                                 |
| python_startup          | 12.6 ms                                                | 9.08 ms: 1.39x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.39x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps              | 8.38 ms                                                | 6.09 ms: 1.38x faster                                                 |
| python_startup_no_site  | 9.73 ms                                                | 7.15 ms: 1.36x faster                                                 |
| sqlglot_parse           | 1.33 ms                                                | 1000 us: 1.33x faster                                                 |
| scimark_monte_carlo     | 72.2 ms                                                | 54.3 ms: 1.33x faster                                                 |
| thrift                  | 586 us                                                 | 442 us: 1.32x faster                                                  |
| tornado_http            | 91.9 ms                                                | 69.4 ms: 1.32x faster                                                 |
| spectral_norm           | 96.4 ms                                                | 72.9 ms: 1.32x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.17 ms: 1.32x faster                                                 |
| chaos                   | 66.8 ms                                                | 50.9 ms: 1.31x faster                                                 |
| pyflate                 | 453 ms                                                 | 351 ms: 1.29x faster                                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.00 ms: 1.29x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 35.0 ms: 1.29x faster                                                 |
| async_tree_memoization  | 493 ms                                                 | 383 ms: 1.29x faster                                                  |
| pycparser               | 915 ms                                                 | 713 ms: 1.28x faster                                                  |
| mako                    | 10.5 ms                                                | 8.16 ms: 1.28x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.28x faster                                                 |
| float                   | 72.3 ms                                                | 56.5 ms: 1.28x faster                                                 |
| regex_compile           | 96.6 ms                                                | 75.6 ms: 1.28x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.1 ms: 1.28x faster                                                 |
| logging_format          | 5.01 us                                                | 3.95 us: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 670 ms                                                 | 532 ms: 1.26x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.67 us: 1.26x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.26x faster                                                  |
| django_template         | 27.3 ms                                                | 21.8 ms: 1.25x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.67 ms: 1.25x faster                                                 |
| scimark_sor             | 127 ms                                                 | 102 ms: 1.25x faster                                                  |
| genshi_xml              | 37.6 ms                                                | 30.2 ms: 1.25x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.22 ms: 1.23x faster                                                 |
| pprint_pformat          | 1.24 sec                                               | 1.00 sec: 1.23x faster                                                |
| html5lib                | 44.1 ms                                                | 35.8 ms: 1.23x faster                                                 |
| pprint_safe_repr        | 609 ms                                                 | 495 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.83 ms: 1.23x faster                                                 |
| sqlalchemy_declarative  | 74.8 ms                                                | 61.3 ms: 1.22x faster                                                 |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| bench_thread_pool       | 548 us                                                 | 455 us: 1.21x faster                                                  |
| deepcopy_memo           | 34.5 us                                                | 28.7 us: 1.20x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                 |
| fannkuch                | 317 ms                                                 | 270 ms: 1.18x faster                                                  |
| async_generators        | 233 ms                                                 | 200 ms: 1.17x faster                                                  |
| scimark_fft             | 232 ms                                                 | 199 ms: 1.17x faster                                                  |
| pylint                  | 307 ms                                                 | 264 ms: 1.16x faster                                                  |
| deepcopy                | 278 us                                                 | 241 us: 1.15x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 11.6 ms: 1.15x faster                                                 |
| deepcopy_reduce         | 2.38 us                                                | 2.08 us: 1.15x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 47.6 ms: 1.14x faster                                                 |
| unpack_sequence         | 38.7 ns                                                | 34.1 ns: 1.13x faster                                                 |
| generators              | 32.9 ms                                                | 29.2 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 197 ms                                                 | 174 ms: 1.13x faster                                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 65.2 ms: 1.11x faster                                                 |
| nqueens                 | 68.1 ms                                                | 61.2 ms: 1.11x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 96.6 ms: 1.11x faster                                                 |
| sympy_expand            | 276 ms                                                 | 248 ms: 1.11x faster                                                  |
| sympy_str               | 169 ms                                                 | 153 ms: 1.10x faster                                                  |
| json                    | 3.10 ms                                                | 2.81 ms: 1.10x faster                                                 |
| sympy_sum               | 94.3 ms                                                | 85.9 ms: 1.10x faster                                                 |
| mdp                     | 1.67 sec                                               | 1.52 sec: 1.10x faster                                                |
| 2to3                    | 202 ms                                                 | 185 ms: 1.10x faster                                                  |
| telco                   | 3.68 ms                                                | 3.36 ms: 1.10x faster                                                 |
| regex_v8                | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                 |
| regex_dna               | 160 ms                                                 | 152 ms: 1.05x faster                                                  |
| unpickle_list           | 2.66 us                                                | 2.54 us: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.5 ms: 1.03x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.46 us: 1.01x faster                                                 |
| meteor_contest          | 78.6 ms                                                | 78.2 ms: 1.01x faster                                                 |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle_list             | 2.83 us                                                | 2.86 us: 1.01x slower                                                 |
| pickle                  | 7.36 us                                                | 7.55 us: 1.03x slower                                                 |
| regex_effbot            | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                 |
| coverage                | 40.8 ms                                                | 53.7 ms: 1.32x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (3): unpickle, pidigits, bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220926-3.12.0a0-2b428a1/bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x
