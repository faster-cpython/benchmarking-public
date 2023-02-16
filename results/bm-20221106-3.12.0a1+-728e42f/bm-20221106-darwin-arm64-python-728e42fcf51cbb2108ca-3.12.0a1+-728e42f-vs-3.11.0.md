
# Results vs. 3.11.0

- fork: python
- ref: 728e42fcf51cbb2108ca
- machine: darwin-arm64
- commit hash: 728e42f
- commit date: 2022-11-06
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 187 ms: 1.03x slower                                                   |
| chameleon      | 4.61 ms                                                             | 5.13 ms: 1.11x slower                                                  |
| docutils       | 1.46 sec                                                            | 1.50 sec: 1.03x slower                                                 |
| html5lib       | 34.7 ms                                                             | 37.5 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                              | 282 ms: 1.00x slower                                                   |
| nbody          | 65.2 ms                                                             | 65.9 ms: 1.01x slower                                                  |
| float          | 51.7 ms                                                             | 57.3 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                             | 16.1 ms: 1.02x faster                                                  |
| regex_dna      | 151 ms                                                              | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                             | 2.63 ms: 1.00x slower                                                  |
| regex_compile  | 76.3 ms                                                             | 77.7 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.67 ms                                                             | 6.15 ms: 1.25x faster                                                  |
| xml_etree_parse      | 99.6 ms                                                             | 93.3 ms: 1.07x faster                                                  |
| unpickle_list        | 2.64 us                                                             | 2.60 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 65.6 ms                                                             | 65.0 ms: 1.01x faster                                                  |
| pickle_list          | 2.86 us                                                             | 2.88 us: 1.01x slower                                                  |
| json_loads           | 16.1 us                                                             | 16.4 us: 1.02x slower                                                  |
| unpickle             | 9.68 us                                                             | 9.86 us: 1.02x slower                                                  |
| xml_etree_generate   | 48.4 ms                                                             | 50.5 ms: 1.04x slower                                                  |
| unpickle_pure_python | 159 us                                                              | 167 us: 1.05x slower                                                   |
| pickle               | 7.21 us                                                             | 7.55 us: 1.05x slower                                                  |
| xml_etree_process    | 35.1 ms                                                             | 36.8 ms: 1.05x slower                                                  |
| pickle_pure_python   | 200 us                                                              | 222 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 9.32 ms: 1.01x slower                                                  |
| python_startup_no_site | 7.24 ms                                                             | 7.38 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.40 ms                                                             | 8.59 ms: 1.02x slower                                                  |
| django_template | 21.1 ms                                                             | 22.2 ms: 1.05x slower                                                  |
| genshi_text     | 15.3 ms                                                             | 16.2 ms: 1.06x slower                                                  |
| genshi_xml      | 30.5 ms                                                             | 32.4 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 7.67 ms                                                             | 6.15 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 2.76 ms: 1.16x faster                                                  |
| coverage                | 58.4 ms                                                             | 53.1 ms: 1.10x faster                                                  |
| xml_etree_parse         | 99.6 ms                                                             | 93.3 ms: 1.07x faster                                                  |
| pylint                  | 265 ms                                                              | 257 ms: 1.03x faster                                                   |
| logging_silent          | 67.4 ns                                                             | 65.6 ns: 1.03x faster                                                  |
| regex_v8                | 16.5 ms                                                             | 16.1 ms: 1.02x faster                                                  |
| richards                | 32.7 ms                                                             | 32.0 ms: 1.02x faster                                                  |
| regex_dna               | 151 ms                                                              | 149 ms: 1.02x faster                                                   |
| unpickle_list           | 2.64 us                                                             | 2.60 us: 1.02x faster                                                  |
| scimark_lu              | 72.2 ms                                                             | 71.2 ms: 1.01x faster                                                  |
| spectral_norm           | 72.7 ms                                                             | 71.9 ms: 1.01x faster                                                  |
| generators              | 28.4 ms                                                             | 28.1 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 65.6 ms                                                             | 65.0 ms: 1.01x faster                                                  |
| scimark_fft             | 201 ms                                                              | 200 ms: 1.00x faster                                                   |
| nqueens                 | 59.5 ms                                                             | 59.3 ms: 1.00x faster                                                  |
| regex_effbot            | 2.63 ms                                                             | 2.63 ms: 1.00x slower                                                  |
| pidigits                | 282 ms                                                              | 282 ms: 1.00x slower                                                   |
| pickle_list             | 2.86 us                                                             | 2.88 us: 1.01x slower                                                  |
| mdp                     | 1.54 sec                                                            | 1.55 sec: 1.01x slower                                                 |
| nbody                   | 65.2 ms                                                             | 65.9 ms: 1.01x slower                                                  |
| deltablue               | 2.82 ms                                                             | 2.85 ms: 1.01x slower                                                  |
| bench_thread_pool       | 457 us                                                              | 463 us: 1.01x slower                                                   |
| json                    | 2.83 ms                                                             | 2.86 ms: 1.01x slower                                                  |
| python_startup          | 9.19 ms                                                             | 9.32 ms: 1.01x slower                                                  |
| telco                   | 3.39 ms                                                             | 3.44 ms: 1.02x slower                                                  |
| json_loads              | 16.1 us                                                             | 16.4 us: 1.02x slower                                                  |
| regex_compile           | 76.3 ms                                                             | 77.7 ms: 1.02x slower                                                  |
| unpickle                | 9.68 us                                                             | 9.86 us: 1.02x slower                                                  |
| python_startup_no_site  | 7.24 ms                                                             | 7.38 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 175 ms: 1.02x slower                                                   |
| dulwich_log             | 29.1 ms                                                             | 29.7 ms: 1.02x slower                                                  |
| mako                    | 8.40 ms                                                             | 8.59 ms: 1.02x slower                                                  |
| pycparser               | 694 ms                                                              | 711 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 31.3 ms                                                             | 32.0 ms: 1.02x slower                                                  |
| docutils                | 1.46 sec                                                            | 1.50 sec: 1.03x slower                                                 |
| sympy_sum               | 85.5 ms                                                             | 88.0 ms: 1.03x slower                                                  |
| thrift                  | 429 us                                                              | 443 us: 1.03x slower                                                   |
| fannkuch                | 262 ms                                                              | 270 ms: 1.03x slower                                                   |
| async_generators        | 195 ms                                                              | 202 ms: 1.03x slower                                                   |
| 2to3                    | 181 ms                                                              | 187 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed | 528 ms                                                              | 547 ms: 1.03x slower                                                   |
| bench_mp_pool           | 41.4 ms                                                             | 42.8 ms: 1.04x slower                                                  |
| raytrace                | 207 ms                                                              | 215 ms: 1.04x slower                                                   |
| hexiom                  | 4.73 ms                                                             | 4.91 ms: 1.04x slower                                                  |
| xml_etree_generate      | 48.4 ms                                                             | 50.5 ms: 1.04x slower                                                  |
| async_tree_none         | 281 ms                                                              | 294 ms: 1.04x slower                                                   |
| chaos                   | 49.3 ms                                                             | 51.6 ms: 1.05x slower                                                  |
| unpickle_pure_python    | 159 us                                                              | 167 us: 1.05x slower                                                   |
| pickle                  | 7.21 us                                                             | 7.55 us: 1.05x slower                                                  |
| xml_etree_process       | 35.1 ms                                                             | 36.8 ms: 1.05x slower                                                  |
| sympy_expand            | 242 ms                                                              | 255 ms: 1.05x slower                                                   |
| django_template         | 21.1 ms                                                             | 22.2 ms: 1.05x slower                                                  |
| sympy_str               | 151 ms                                                              | 159 ms: 1.05x slower                                                   |
| sympy_integrate         | 11.5 ms                                                             | 12.1 ms: 1.05x slower                                                  |
| async_tree_memoization  | 317 ms                                                              | 335 ms: 1.06x slower                                                   |
| async_tree_io           | 696 ms                                                              | 736 ms: 1.06x slower                                                   |
| genshi_text             | 15.3 ms                                                             | 16.2 ms: 1.06x slower                                                  |
| genshi_xml              | 30.5 ms                                                             | 32.4 ms: 1.06x slower                                                  |
| sqlglot_transpile       | 1.11 ms                                                             | 1.19 ms: 1.07x slower                                                  |
| sqlglot_parse           | 948 us                                                              | 1.01 ms: 1.07x slower                                                  |
| coroutines              | 17.8 ms                                                             | 19.1 ms: 1.07x slower                                                  |
| html5lib                | 34.7 ms                                                             | 37.5 ms: 1.08x slower                                                  |
| logging_simple          | 3.47 us                                                             | 3.77 us: 1.09x slower                                                  |
| meteor_contest          | 73.9 ms                                                             | 80.5 ms: 1.09x slower                                                  |
| logging_format          | 3.73 us                                                             | 4.09 us: 1.10x slower                                                  |
| pprint_safe_repr        | 467 ms                                                              | 514 ms: 1.10x slower                                                   |
| pprint_pformat          | 953 ms                                                              | 1.05 sec: 1.10x slower                                                 |
| go                      | 109 ms                                                              | 121 ms: 1.10x slower                                                   |
| float                   | 51.7 ms                                                             | 57.3 ms: 1.11x slower                                                  |
| pickle_pure_python      | 200 us                                                              | 222 us: 1.11x slower                                                   |
| chameleon               | 4.61 ms                                                             | 5.13 ms: 1.11x slower                                                  |
| sqlite_synth            | 1.29 us                                                             | 1.45 us: 1.12x slower                                                  |
| pyflate                 | 313 ms                                                              | 355 ms: 1.14x slower                                                   |
| scimark_monte_carlo     | 46.9 ms                                                             | 54.9 ms: 1.17x slower                                                  |
| deepcopy                | 222 us                                                              | 263 us: 1.18x slower                                                   |
| deepcopy_reduce         | 1.90 us                                                             | 2.28 us: 1.20x slower                                                  |
| deepcopy_memo           | 26.2 us                                                             | 32.1 us: 1.23x slower                                                  |
| scimark_sor             | 83.3 ms                                                             | 103 ms: 1.24x slower                                                   |
| unpack_sequence         | 33.1 ns                                                             | 52.1 ns: 1.57x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.04x slower                                                           |

Benchmark hidden because not significant (5): tornado_http, crypto_pyaes, pickle_dict, pathlib, mypy
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
