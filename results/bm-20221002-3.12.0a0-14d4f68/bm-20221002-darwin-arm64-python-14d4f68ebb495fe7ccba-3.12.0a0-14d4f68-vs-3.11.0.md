
# Results vs. 3.11.0

- fork: python
- ref: 14d4f68ebb495fe7ccba
- machine: darwin-arm64
- commit hash: 14d4f68
- commit date: 2022-10-02
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 185 ms: 1.02x slower                                                  |
| chameleon      | 4.61 ms                                                             | 4.69 ms: 1.02x slower                                                 |
| docutils       | 1.46 sec                                                            | 1.47 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                             | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 51.7 ms                                                             | 56.1 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                             | 16.1 ms: 1.03x faster                                                 |
| regex_effbot   | 2.63 ms                                                             | 2.59 ms: 1.02x faster                                                 |
| regex_compile  | 76.3 ms                                                             | 75.4 ms: 1.01x faster                                                 |
| regex_dna      | 151 ms                                                              | 150 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.67 ms                                                             | 6.13 ms: 1.25x faster                                                 |
| xml_etree_parse      | 99.6 ms                                                             | 96.1 ms: 1.04x faster                                                 |
| unpickle_list        | 2.64 us                                                             | 2.56 us: 1.03x faster                                                 |
| xml_etree_generate   | 48.4 ms                                                             | 47.6 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 65.6 ms                                                             | 64.9 ms: 1.01x faster                                                 |
| xml_etree_process    | 35.1 ms                                                             | 34.9 ms: 1.00x faster                                                 |
| json_loads           | 16.1 us                                                             | 16.2 us: 1.00x slower                                                 |
| pickle_dict          | 17.9 us                                                             | 18.0 us: 1.00x slower                                                 |
| unpickle_pure_python | 159 us                                                              | 162 us: 1.02x slower                                                  |
| pickle_pure_python   | 200 us                                                              | 205 us: 1.03x slower                                                  |
| pickle               | 7.21 us                                                             | 7.55 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.02x faster                                                          |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 9.06 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.24 ms                                                             | 7.16 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                               | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.40 ms                                                             | 8.14 ms: 1.03x faster                                                 |
| genshi_xml      | 30.5 ms                                                             | 30.3 ms: 1.01x faster                                                 |
| django_template | 21.1 ms                                                             | 21.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 7.67 ms                                                             | 6.13 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 2.82 ms: 1.13x faster                                                 |
| coverage                | 58.4 ms                                                             | 53.5 ms: 1.09x faster                                                 |
| xml_etree_parse         | 99.6 ms                                                             | 96.1 ms: 1.04x faster                                                 |
| mako                    | 8.40 ms                                                             | 8.14 ms: 1.03x faster                                                 |
| unpickle_list           | 2.64 us                                                             | 2.56 us: 1.03x faster                                                 |
| flaskblogging           | 2.29 ms                                                             | 2.23 ms: 1.03x faster                                                 |
| regex_v8                | 16.5 ms                                                             | 16.1 ms: 1.03x faster                                                 |
| sqlalchemy_imperative   | 7.22 ms                                                             | 7.06 ms: 1.02x faster                                                 |
| sqlalchemy_declarative  | 62.4 ms                                                             | 61.2 ms: 1.02x faster                                                 |
| regex_effbot            | 2.63 ms                                                             | 2.59 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.4 ms                                                             | 47.6 ms: 1.02x faster                                                 |
| python_startup          | 9.19 ms                                                             | 9.06 ms: 1.01x faster                                                 |
| mypy                    | 421 ms                                                              | 415 ms: 1.01x faster                                                  |
| regex_compile           | 76.3 ms                                                             | 75.4 ms: 1.01x faster                                                 |
| python_startup_no_site  | 7.24 ms                                                             | 7.16 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 65.6 ms                                                             | 64.9 ms: 1.01x faster                                                 |
| regex_dna               | 151 ms                                                              | 150 ms: 1.01x faster                                                  |
| scimark_fft             | 201 ms                                                              | 199 ms: 1.01x faster                                                  |
| telco                   | 3.39 ms                                                             | 3.36 ms: 1.01x faster                                                 |
| mdp                     | 1.54 sec                                                            | 1.53 sec: 1.01x faster                                                |
| genshi_xml              | 30.5 ms                                                             | 30.3 ms: 1.01x faster                                                 |
| bench_thread_pool       | 457 us                                                              | 454 us: 1.01x faster                                                  |
| xml_etree_process       | 35.1 ms                                                             | 34.9 ms: 1.00x faster                                                 |
| json_loads              | 16.1 us                                                             | 16.2 us: 1.00x slower                                                 |
| deltablue               | 2.82 ms                                                             | 2.83 ms: 1.00x slower                                                 |
| dulwich_log             | 29.1 ms                                                             | 29.1 ms: 1.00x slower                                                 |
| spectral_norm           | 72.7 ms                                                             | 73.0 ms: 1.00x slower                                                 |
| pickle_dict             | 17.9 us                                                             | 18.0 us: 1.00x slower                                                 |
| sympy_sum               | 85.5 ms                                                             | 85.9 ms: 1.01x slower                                                 |
| docutils                | 1.46 sec                                                            | 1.47 sec: 1.01x slower                                                |
| crypto_pyaes            | 51.7 ms                                                             | 52.2 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                             | 11.6 ms: 1.01x slower                                                 |
| sympy_str               | 151 ms                                                              | 153 ms: 1.01x slower                                                  |
| richards                | 32.7 ms                                                             | 33.2 ms: 1.02x slower                                                 |
| chameleon               | 4.61 ms                                                             | 4.69 ms: 1.02x slower                                                 |
| unpickle_pure_python    | 159 us                                                              | 162 us: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 174 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.3 ms                                                             | 31.9 ms: 1.02x slower                                                 |
| 2to3                    | 181 ms                                                              | 185 ms: 1.02x slower                                                  |
| sympy_expand            | 242 ms                                                              | 248 ms: 1.02x slower                                                  |
| pickle_pure_python      | 200 us                                                              | 205 us: 1.03x slower                                                  |
| async_generators        | 195 ms                                                              | 201 ms: 1.03x slower                                                  |
| pycparser               | 694 ms                                                              | 713 ms: 1.03x slower                                                  |
| unpack_sequence         | 33.1 ns                                                             | 34.1 ns: 1.03x slower                                                 |
| fannkuch                | 262 ms                                                              | 270 ms: 1.03x slower                                                  |
| generators              | 28.4 ms                                                             | 29.2 ms: 1.03x slower                                                 |
| nqueens                 | 59.5 ms                                                             | 61.3 ms: 1.03x slower                                                 |
| chaos                   | 49.3 ms                                                             | 50.9 ms: 1.03x slower                                                 |
| html5lib                | 34.7 ms                                                             | 35.8 ms: 1.03x slower                                                 |
| thrift                  | 429 us                                                              | 446 us: 1.04x slower                                                  |
| django_template         | 21.1 ms                                                             | 21.9 ms: 1.04x slower                                                 |
| raytrace                | 207 ms                                                              | 216 ms: 1.04x slower                                                  |
| hexiom                  | 4.73 ms                                                             | 4.93 ms: 1.04x slower                                                 |
| pickle                  | 7.21 us                                                             | 7.55 us: 1.05x slower                                                 |
| async_tree_io           | 696 ms                                                              | 732 ms: 1.05x slower                                                  |
| sqlglot_transpile       | 1.11 ms                                                             | 1.17 ms: 1.05x slower                                                 |
| pprint_pformat          | 953 ms                                                              | 1.01 sec: 1.06x slower                                                |
| meteor_contest          | 73.9 ms                                                             | 78.1 ms: 1.06x slower                                                 |
| sqlglot_parse           | 948 us                                                              | 1.00 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 467 ms                                                              | 496 ms: 1.06x slower                                                  |
| logging_simple          | 3.47 us                                                             | 3.68 us: 1.06x slower                                                 |
| logging_silent          | 67.4 ns                                                             | 71.7 ns: 1.06x slower                                                 |
| logging_format          | 3.73 us                                                             | 3.97 us: 1.06x slower                                                 |
| go                      | 109 ms                                                              | 118 ms: 1.08x slower                                                  |
| deepcopy                | 222 us                                                              | 240 us: 1.08x slower                                                  |
| float                   | 51.7 ms                                                             | 56.1 ms: 1.09x slower                                                 |
| deepcopy_reduce         | 1.90 us                                                             | 2.06 us: 1.09x slower                                                 |
| deepcopy_memo           | 26.2 us                                                             | 28.5 us: 1.09x slower                                                 |
| coroutines              | 17.8 ms                                                             | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 313 ms                                                              | 353 ms: 1.13x slower                                                  |
| sqlite_synth            | 1.29 us                                                             | 1.46 us: 1.13x slower                                                 |
| scimark_monte_carlo     | 46.9 ms                                                             | 55.4 ms: 1.18x slower                                                 |
| async_tree_memoization  | 317 ms                                                              | 383 ms: 1.21x slower                                                  |
| scimark_sor             | 83.3 ms                                                             | 101 ms: 1.21x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                          |

Benchmark hidden because not significant (13): tornado_http, pathlib, pickle_list, pylint, json, pidigits, nbody, scimark_lu, genshi_text, async_tree_cpu_io_mixed, async_tree_none, unpickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, gunicorn
