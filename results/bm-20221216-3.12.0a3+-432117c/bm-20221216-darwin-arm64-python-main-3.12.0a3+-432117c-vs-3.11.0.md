
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 432117c
- commit date: 2022-12-16
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 184 ms: 1.02x slower                                   |
| chameleon      | 4.61 ms                                                             | 4.29 ms: 1.08x faster                                  |
| docutils       | 1.46 sec                                                            | 1.44 sec: 1.02x faster                                 |
| html5lib       | 34.7 ms                                                             | 33.2 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                               | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.2 ms                                                             | 62.3 ms: 1.05x faster                                  |
| float          | 51.7 ms                                                             | 53.4 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.3 ms                                                             | 72.7 ms: 1.05x faster                                  |
| regex_v8       | 16.5 ms                                                             | 16.0 ms: 1.03x faster                                  |
| regex_dna      | 151 ms                                                              | 149 ms: 1.01x faster                                   |
| regex_effbot   | 2.63 ms                                                             | 2.71 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.67 ms                                                             | 6.16 ms: 1.25x faster                                  |
| xml_etree_parse      | 99.6 ms                                                             | 92.9 ms: 1.07x faster                                  |
| unpickle_pure_python | 159 us                                                              | 151 us: 1.05x faster                                   |
| unpickle_list        | 2.64 us                                                             | 2.56 us: 1.03x faster                                  |
| xml_etree_generate   | 48.4 ms                                                             | 47.0 ms: 1.03x faster                                  |
| xml_etree_process    | 35.1 ms                                                             | 34.4 ms: 1.02x faster                                  |
| pickle_pure_python   | 200 us                                                              | 197 us: 1.01x faster                                   |
| pickle_list          | 2.86 us                                                             | 2.84 us: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                             | 18.0 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                             | 16.3 us: 1.01x slower                                  |
| unpickle             | 9.68 us                                                             | 9.84 us: 1.02x slower                                  |
| pickle               | 7.21 us                                                             | 7.55 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                               | 1.03x faster                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 9.29 ms: 1.01x slower                                  |
| python_startup_no_site | 7.24 ms                                                             | 7.34 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.40 ms                                                             | 6.96 ms: 1.21x faster                                  |
| genshi_text     | 15.3 ms                                                             | 13.9 ms: 1.10x faster                                  |
| genshi_xml      | 30.5 ms                                                             | 28.2 ms: 1.08x faster                                  |
| django_template | 21.1 ms                                                             | 20.7 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                               | 1.10x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 7.67 ms                                                             | 6.16 ms: 1.25x faster                                  |
| mako                    | 8.40 ms                                                             | 6.96 ms: 1.21x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 2.77 ms: 1.16x faster                                  |
| deltablue               | 2.82 ms                                                             | 2.51 ms: 1.12x faster                                  |
| richards                | 32.7 ms                                                             | 29.2 ms: 1.12x faster                                  |
| genshi_text             | 15.3 ms                                                             | 13.9 ms: 1.10x faster                                  |
| unpack_sequence         | 33.1 ns                                                             | 30.4 ns: 1.09x faster                                  |
| genshi_xml              | 30.5 ms                                                             | 28.2 ms: 1.08x faster                                  |
| logging_silent          | 67.4 ns                                                             | 62.7 ns: 1.08x faster                                  |
| chameleon               | 4.61 ms                                                             | 4.29 ms: 1.08x faster                                  |
| xml_etree_parse         | 99.6 ms                                                             | 92.9 ms: 1.07x faster                                  |
| scimark_sor             | 83.3 ms                                                             | 78.1 ms: 1.07x faster                                  |
| coverage                | 58.4 ms                                                             | 54.9 ms: 1.06x faster                                  |
| unpickle_pure_python    | 159 us                                                              | 151 us: 1.05x faster                                   |
| regex_compile           | 76.3 ms                                                             | 72.7 ms: 1.05x faster                                  |
| nbody                   | 65.2 ms                                                             | 62.3 ms: 1.05x faster                                  |
| scimark_lu              | 72.2 ms                                                             | 69.0 ms: 1.05x faster                                  |
| html5lib                | 34.7 ms                                                             | 33.2 ms: 1.04x faster                                  |
| pycparser               | 694 ms                                                              | 665 ms: 1.04x faster                                   |
| scimark_fft             | 201 ms                                                              | 193 ms: 1.04x faster                                   |
| go                      | 109 ms                                                              | 106 ms: 1.03x faster                                   |
| unpickle_list           | 2.64 us                                                             | 2.56 us: 1.03x faster                                  |
| hexiom                  | 4.73 ms                                                             | 4.59 ms: 1.03x faster                                  |
| mdp                     | 1.54 sec                                                            | 1.50 sec: 1.03x faster                                 |
| fannkuch                | 262 ms                                                              | 255 ms: 1.03x faster                                   |
| bench_thread_pool       | 457 us                                                              | 445 us: 1.03x faster                                   |
| regex_v8                | 16.5 ms                                                             | 16.0 ms: 1.03x faster                                  |
| xml_etree_generate      | 48.4 ms                                                             | 47.0 ms: 1.03x faster                                  |
| mypy                    | 421 ms                                                              | 410 ms: 1.03x faster                                   |
| dulwich_log             | 29.1 ms                                                             | 28.4 ms: 1.02x faster                                  |
| sqlglot_normalize       | 171 ms                                                              | 167 ms: 1.02x faster                                   |
| raytrace                | 207 ms                                                              | 203 ms: 1.02x faster                                   |
| xml_etree_process       | 35.1 ms                                                             | 34.4 ms: 1.02x faster                                  |
| django_template         | 21.1 ms                                                             | 20.7 ms: 1.02x faster                                  |
| coroutines              | 17.8 ms                                                             | 17.4 ms: 1.02x faster                                  |
| scimark_monte_carlo     | 46.9 ms                                                             | 46.1 ms: 1.02x faster                                  |
| docutils                | 1.46 sec                                                            | 1.44 sec: 1.02x faster                                 |
| chaos                   | 49.3 ms                                                             | 48.6 ms: 1.02x faster                                  |
| sqlglot_optimize        | 31.3 ms                                                             | 30.8 ms: 1.02x faster                                  |
| spectral_norm           | 72.7 ms                                                             | 71.7 ms: 1.01x faster                                  |
| sympy_integrate         | 11.5 ms                                                             | 11.3 ms: 1.01x faster                                  |
| regex_dna               | 151 ms                                                              | 149 ms: 1.01x faster                                   |
| pickle_pure_python      | 200 us                                                              | 197 us: 1.01x faster                                   |
| pathlib                 | 20.6 ms                                                             | 20.4 ms: 1.01x faster                                  |
| telco                   | 3.39 ms                                                             | 3.35 ms: 1.01x faster                                  |
| logging_simple          | 3.47 us                                                             | 3.44 us: 1.01x faster                                  |
| sympy_str               | 151 ms                                                              | 150 ms: 1.01x faster                                   |
| sympy_expand            | 242 ms                                                              | 240 ms: 1.01x faster                                   |
| pickle_list             | 2.86 us                                                             | 2.84 us: 1.01x faster                                  |
| sympy_sum               | 85.5 ms                                                             | 85.0 ms: 1.01x faster                                  |
| nqueens                 | 59.5 ms                                                             | 59.3 ms: 1.00x faster                                  |
| pprint_pformat          | 953 ms                                                              | 955 ms: 1.00x slower                                   |
| logging_format          | 3.73 us                                                             | 3.74 us: 1.00x slower                                  |
| pickle_dict             | 17.9 us                                                             | 18.0 us: 1.01x slower                                  |
| pprint_safe_repr        | 467 ms                                                              | 470 ms: 1.01x slower                                   |
| thrift                  | 429 us                                                              | 433 us: 1.01x slower                                   |
| json_loads              | 16.1 us                                                             | 16.3 us: 1.01x slower                                  |
| python_startup          | 9.19 ms                                                             | 9.29 ms: 1.01x slower                                  |
| python_startup_no_site  | 7.24 ms                                                             | 7.34 ms: 1.01x slower                                  |
| async_tree_none         | 281 ms                                                              | 285 ms: 1.01x slower                                   |
| unpickle                | 9.68 us                                                             | 9.84 us: 1.02x slower                                  |
| 2to3                    | 181 ms                                                              | 184 ms: 1.02x slower                                   |
| async_tree_cpu_io_mixed | 528 ms                                                              | 538 ms: 1.02x slower                                   |
| meteor_contest          | 73.9 ms                                                             | 75.4 ms: 1.02x slower                                  |
| sqlglot_transpile       | 1.11 ms                                                             | 1.14 ms: 1.02x slower                                  |
| deepcopy                | 222 us                                                              | 227 us: 1.02x slower                                   |
| crypto_pyaes            | 51.7 ms                                                             | 53.0 ms: 1.03x slower                                  |
| async_generators        | 195 ms                                                              | 201 ms: 1.03x slower                                   |
| deepcopy_reduce         | 1.90 us                                                             | 1.95 us: 1.03x slower                                  |
| sqlglot_parse           | 948 us                                                              | 976 us: 1.03x slower                                   |
| regex_effbot            | 2.63 ms                                                             | 2.71 ms: 1.03x slower                                  |
| float                   | 51.7 ms                                                             | 53.4 ms: 1.03x slower                                  |
| pyflate                 | 313 ms                                                              | 324 ms: 1.04x slower                                   |
| async_tree_memoization  | 317 ms                                                              | 330 ms: 1.04x slower                                   |
| deepcopy_memo           | 26.2 us                                                             | 27.4 us: 1.05x slower                                  |
| pickle                  | 7.21 us                                                             | 7.55 us: 1.05x slower                                  |
| async_tree_io           | 696 ms                                                              | 732 ms: 1.05x slower                                   |
| bench_mp_pool           | 41.4 ms                                                             | 43.9 ms: 1.06x slower                                  |
| sqlite_synth            | 1.29 us                                                             | 1.43 us: 1.11x slower                                  |
| generators              | 28.4 ms                                                             | 32.2 ms: 1.13x slower                                  |
| Geometric mean          | (ref)                                                               | 1.02x faster                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, json, pidigits
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
