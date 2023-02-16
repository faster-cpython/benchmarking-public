
# Results vs. 3.11.0

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| chameleon      | 4.61 ms                                                             | 4.70 ms: 1.02x slower                                                 |
| docutils       | 1.46 sec                                                            | 1.45 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                             | 34.0 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                               | 1.00x faster                                                          |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.2 ms                                                             | 65.6 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                               | 1.00x slower                                                          |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.20 ms: 1.20x faster                                                 |
| regex_compile  | 76.3 ms                                                             | 75.6 ms: 1.01x faster                                                 |
| regex_dna      | 151 ms                                                              | 169 ms: 1.12x slower                                                  |
| regex_v8       | 16.5 ms                                                             | 20.5 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 99.6 ms                                                             | 95.7 ms: 1.04x faster                                                 |
| pickle_list          | 2.86 us                                                             | 2.80 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 65.6 ms                                                             | 64.4 ms: 1.02x faster                                                 |
| unpickle_pure_python | 159 us                                                              | 157 us: 1.01x faster                                                  |
| json_dumps           | 7.67 ms                                                             | 7.58 ms: 1.01x faster                                                 |
| xml_etree_generate   | 48.4 ms                                                             | 47.9 ms: 1.01x faster                                                 |
| unpickle_list        | 2.64 us                                                             | 2.62 us: 1.01x faster                                                 |
| pickle_pure_python   | 200 us                                                              | 200 us: 1.00x faster                                                  |
| json_loads           | 16.1 us                                                             | 16.3 us: 1.01x slower                                                 |
| unpickle             | 9.68 us                                                             | 9.82 us: 1.01x slower                                                 |
| pickle_dict          | 17.9 us                                                             | 19.2 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.24 ms                                                             | 7.18 ms: 1.01x faster                                                 |
| python_startup         | 9.19 ms                                                             | 9.13 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                               | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.40 ms                                                             | 8.21 ms: 1.02x faster                                                 |
| genshi_text     | 15.3 ms                                                             | 15.2 ms: 1.01x faster                                                 |
| django_template | 21.1 ms                                                             | 21.1 ms: 1.00x slower                                                 |
| genshi_xml      | 30.5 ms                                                             | 31.4 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                             | 2.20 ms: 1.20x faster                                                 |
| bench_mp_pool           | 41.4 ms                                                             | 37.1 ms: 1.11x faster                                                 |
| deltablue               | 2.82 ms                                                             | 2.67 ms: 1.06x faster                                                 |
| sympy_sum               | 85.5 ms                                                             | 81.7 ms: 1.05x faster                                                 |
| xml_etree_parse         | 99.6 ms                                                             | 95.7 ms: 1.04x faster                                                 |
| unpack_sequence         | 33.1 ns                                                             | 31.9 ns: 1.04x faster                                                 |
| deepcopy_memo           | 26.2 us                                                             | 25.4 us: 1.03x faster                                                 |
| coroutines              | 17.8 ms                                                             | 17.3 ms: 1.03x faster                                                 |
| sympy_integrate         | 11.5 ms                                                             | 11.2 ms: 1.02x faster                                                 |
| logging_simple          | 3.47 us                                                             | 3.38 us: 1.02x faster                                                 |
| async_generators        | 195 ms                                                              | 191 ms: 1.02x faster                                                  |
| logging_format          | 3.73 us                                                             | 3.65 us: 1.02x faster                                                 |
| sympy_str               | 151 ms                                                              | 147 ms: 1.02x faster                                                  |
| mako                    | 8.40 ms                                                             | 8.21 ms: 1.02x faster                                                 |
| pickle_list             | 2.86 us                                                             | 2.80 us: 1.02x faster                                                 |
| go                      | 109 ms                                                              | 107 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 65.6 ms                                                             | 64.4 ms: 1.02x faster                                                 |
| html5lib                | 34.7 ms                                                             | 34.0 ms: 1.02x faster                                                 |
| richards                | 32.7 ms                                                             | 32.1 ms: 1.02x faster                                                 |
| pprint_safe_repr        | 467 ms                                                              | 460 ms: 1.02x faster                                                  |
| generators              | 28.4 ms                                                             | 27.9 ms: 1.02x faster                                                 |
| pprint_pformat          | 953 ms                                                              | 940 ms: 1.01x faster                                                  |
| unpickle_pure_python    | 159 us                                                              | 157 us: 1.01x faster                                                  |
| json_dumps              | 7.67 ms                                                             | 7.58 ms: 1.01x faster                                                 |
| deepcopy                | 222 us                                                              | 220 us: 1.01x faster                                                  |
| xml_etree_generate      | 48.4 ms                                                             | 47.9 ms: 1.01x faster                                                 |
| regex_compile           | 76.3 ms                                                             | 75.6 ms: 1.01x faster                                                 |
| genshi_text             | 15.3 ms                                                             | 15.2 ms: 1.01x faster                                                 |
| docutils                | 1.46 sec                                                            | 1.45 sec: 1.01x faster                                                |
| python_startup_no_site  | 7.24 ms                                                             | 7.18 ms: 1.01x faster                                                 |
| python_startup          | 9.19 ms                                                             | 9.13 ms: 1.01x faster                                                 |
| sympy_expand            | 242 ms                                                              | 241 ms: 1.01x faster                                                  |
| unpickle_list           | 2.64 us                                                             | 2.62 us: 1.01x faster                                                 |
| async_tree_none         | 281 ms                                                              | 280 ms: 1.00x faster                                                  |
| async_tree_io           | 696 ms                                                              | 693 ms: 1.00x faster                                                  |
| sqlite_synth            | 1.29 us                                                             | 1.29 us: 1.00x faster                                                 |
| fannkuch                | 262 ms                                                              | 262 ms: 1.00x faster                                                  |
| pickle_pure_python      | 200 us                                                              | 200 us: 1.00x faster                                                  |
| scimark_fft             | 201 ms                                                              | 201 ms: 1.00x slower                                                  |
| django_template         | 21.1 ms                                                             | 21.1 ms: 1.00x slower                                                 |
| nbody                   | 65.2 ms                                                             | 65.6 ms: 1.00x slower                                                 |
| scimark_lu              | 72.2 ms                                                             | 72.6 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 3.22 ms: 1.01x slower                                                 |
| sqlglot_normalize       | 171 ms                                                              | 172 ms: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                             | 16.3 us: 1.01x slower                                                 |
| chaos                   | 49.3 ms                                                             | 49.7 ms: 1.01x slower                                                 |
| deepcopy_reduce         | 1.90 us                                                             | 1.91 us: 1.01x slower                                                 |
| raytrace                | 207 ms                                                              | 209 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 528 ms                                                              | 534 ms: 1.01x slower                                                  |
| dulwich_log             | 29.1 ms                                                             | 29.4 ms: 1.01x slower                                                 |
| spectral_norm           | 72.7 ms                                                             | 73.6 ms: 1.01x slower                                                 |
| pathlib                 | 20.6 ms                                                             | 20.9 ms: 1.01x slower                                                 |
| pyflate                 | 313 ms                                                              | 317 ms: 1.01x slower                                                  |
| sqlalchemy_declarative  | 62.4 ms                                                             | 63.2 ms: 1.01x slower                                                 |
| unpickle                | 9.68 us                                                             | 9.82 us: 1.01x slower                                                 |
| scimark_sor             | 83.3 ms                                                             | 84.7 ms: 1.02x slower                                                 |
| meteor_contest          | 73.9 ms                                                             | 75.2 ms: 1.02x slower                                                 |
| nqueens                 | 59.5 ms                                                             | 60.6 ms: 1.02x slower                                                 |
| chameleon               | 4.61 ms                                                             | 4.70 ms: 1.02x slower                                                 |
| sqlglot_optimize        | 31.3 ms                                                             | 31.9 ms: 1.02x slower                                                 |
| sqlalchemy_imperative   | 7.22 ms                                                             | 7.37 ms: 1.02x slower                                                 |
| thrift                  | 429 us                                                              | 439 us: 1.02x slower                                                  |
| pylint                  | 265 ms                                                              | 271 ms: 1.02x slower                                                  |
| logging_silent          | 67.4 ns                                                             | 69.4 ns: 1.03x slower                                                 |
| genshi_xml              | 30.5 ms                                                             | 31.4 ms: 1.03x slower                                                 |
| hexiom                  | 4.73 ms                                                             | 4.87 ms: 1.03x slower                                                 |
| json                    | 2.83 ms                                                             | 2.92 ms: 1.03x slower                                                 |
| pycparser               | 694 ms                                                              | 721 ms: 1.04x slower                                                  |
| bench_thread_pool       | 457 us                                                              | 476 us: 1.04x slower                                                  |
| pickle_dict             | 17.9 us                                                             | 19.2 us: 1.07x slower                                                 |
| mdp                     | 1.54 sec                                                            | 1.66 sec: 1.08x slower                                                |
| crypto_pyaes            | 51.7 ms                                                             | 56.5 ms: 1.09x slower                                                 |
| regex_dna               | 151 ms                                                              | 169 ms: 1.12x slower                                                  |
| sqlglot_transpile       | 1.11 ms                                                             | 1.33 ms: 1.20x slower                                                 |
| sqlglot_parse           | 948 us                                                              | 1.17 ms: 1.23x slower                                                 |
| regex_v8                | 16.5 ms                                                             | 20.5 ms: 1.24x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (13): aiohttp, pickle, tornado_http, float, async_tree_memoization, xml_etree_process, scimark_monte_carlo, 2to3, telco, pidigits, mypy, gunicorn, flaskblogging
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage
