
# Results vs. 3.11.0

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: darwin-arm64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 179 ms: 1.01x faster                                                   |
| chameleon      | 4.61 ms                                                             | 4.28 ms: 1.08x faster                                                  |
| docutils       | 1.46 sec                                                            | 1.44 sec: 1.02x faster                                                 |
| html5lib       | 34.7 ms                                                             | 34.3 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                               | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.2 ms                                                             | 62.8 ms: 1.04x faster                                                  |
| pidigits       | 282 ms                                                              | 283 ms: 1.00x slower                                                   |
| float          | 51.7 ms                                                             | 51.9 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.3 ms                                                             | 72.7 ms: 1.05x faster                                                  |
| regex_v8       | 16.5 ms                                                             | 16.1 ms: 1.03x faster                                                  |
| regex_dna      | 151 ms                                                              | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                             | 2.60 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                               | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.67 ms                                                             | 6.17 ms: 1.24x faster                                                  |
| xml_etree_parse      | 99.6 ms                                                             | 93.1 ms: 1.07x faster                                                  |
| unpickle_pure_python | 159 us                                                              | 152 us: 1.05x faster                                                   |
| xml_etree_generate   | 48.4 ms                                                             | 47.1 ms: 1.03x faster                                                  |
| unpickle_list        | 2.64 us                                                             | 2.58 us: 1.02x faster                                                  |
| xml_etree_process    | 35.1 ms                                                             | 34.4 ms: 1.02x faster                                                  |
| pickle_pure_python   | 200 us                                                              | 196 us: 1.02x faster                                                   |
| pickle_dict          | 17.9 us                                                             | 18.0 us: 1.00x slower                                                  |
| json_loads           | 16.1 us                                                             | 16.3 us: 1.01x slower                                                  |
| pickle               | 7.21 us                                                             | 7.63 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 9.29 ms: 1.01x slower                                                  |
| python_startup_no_site | 7.24 ms                                                             | 7.34 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.40 ms                                                             | 6.88 ms: 1.22x faster                                                  |
| genshi_text     | 15.3 ms                                                             | 14.0 ms: 1.10x faster                                                  |
| genshi_xml      | 30.5 ms                                                             | 28.3 ms: 1.08x faster                                                  |
| django_template | 21.1 ms                                                             | 20.2 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 7.67 ms                                                             | 6.17 ms: 1.24x faster                                                  |
| mako                    | 8.40 ms                                                             | 6.88 ms: 1.22x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 2.78 ms: 1.15x faster                                                  |
| deltablue               | 2.82 ms                                                             | 2.48 ms: 1.14x faster                                                  |
| richards                | 32.7 ms                                                             | 28.9 ms: 1.13x faster                                                  |
| unpack_sequence         | 33.1 ns                                                             | 30.1 ns: 1.10x faster                                                  |
| genshi_text             | 15.3 ms                                                             | 14.0 ms: 1.10x faster                                                  |
| logging_silent          | 67.4 ns                                                             | 62.3 ns: 1.08x faster                                                  |
| chameleon               | 4.61 ms                                                             | 4.28 ms: 1.08x faster                                                  |
| genshi_xml              | 30.5 ms                                                             | 28.3 ms: 1.08x faster                                                  |
| scimark_sor             | 83.3 ms                                                             | 77.5 ms: 1.07x faster                                                  |
| xml_etree_parse         | 99.6 ms                                                             | 93.1 ms: 1.07x faster                                                  |
| coverage                | 58.4 ms                                                             | 55.2 ms: 1.06x faster                                                  |
| regex_compile           | 76.3 ms                                                             | 72.7 ms: 1.05x faster                                                  |
| unpickle_pure_python    | 159 us                                                              | 152 us: 1.05x faster                                                   |
| scimark_lu              | 72.2 ms                                                             | 69.2 ms: 1.04x faster                                                  |
| django_template         | 21.1 ms                                                             | 20.2 ms: 1.04x faster                                                  |
| nbody                   | 65.2 ms                                                             | 62.8 ms: 1.04x faster                                                  |
| pycparser               | 694 ms                                                              | 670 ms: 1.04x faster                                                   |
| bench_thread_pool       | 457 us                                                              | 442 us: 1.03x faster                                                   |
| scimark_fft             | 201 ms                                                              | 194 ms: 1.03x faster                                                   |
| mdp                     | 1.54 sec                                                            | 1.50 sec: 1.03x faster                                                 |
| hexiom                  | 4.73 ms                                                             | 4.59 ms: 1.03x faster                                                  |
| go                      | 109 ms                                                              | 106 ms: 1.03x faster                                                   |
| xml_etree_generate      | 48.4 ms                                                             | 47.1 ms: 1.03x faster                                                  |
| regex_v8                | 16.5 ms                                                             | 16.1 ms: 1.03x faster                                                  |
| mypy                    | 421 ms                                                              | 410 ms: 1.03x faster                                                   |
| fannkuch                | 262 ms                                                              | 256 ms: 1.02x faster                                                   |
| dulwich_log             | 29.1 ms                                                             | 28.4 ms: 1.02x faster                                                  |
| unpickle_list           | 2.64 us                                                             | 2.58 us: 1.02x faster                                                  |
| xml_etree_process       | 35.1 ms                                                             | 34.4 ms: 1.02x faster                                                  |
| pickle_pure_python      | 200 us                                                              | 196 us: 1.02x faster                                                   |
| sqlglot_normalize       | 171 ms                                                              | 168 ms: 1.02x faster                                                   |
| logging_simple          | 3.47 us                                                             | 3.40 us: 1.02x faster                                                  |
| docutils                | 1.46 sec                                                            | 1.44 sec: 1.02x faster                                                 |
| pathlib                 | 20.6 ms                                                             | 20.3 ms: 1.02x faster                                                  |
| regex_dna               | 151 ms                                                              | 149 ms: 1.02x faster                                                   |
| sympy_integrate         | 11.5 ms                                                             | 11.3 ms: 1.01x faster                                                  |
| spectral_norm           | 72.7 ms                                                             | 71.8 ms: 1.01x faster                                                  |
| coroutines              | 17.8 ms                                                             | 17.5 ms: 1.01x faster                                                  |
| telco                   | 3.39 ms                                                             | 3.35 ms: 1.01x faster                                                  |
| 2to3                    | 181 ms                                                              | 179 ms: 1.01x faster                                                   |
| html5lib                | 34.7 ms                                                             | 34.3 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                             | 2.60 ms: 1.01x faster                                                  |
| sqlglot_optimize        | 31.3 ms                                                             | 31.0 ms: 1.01x faster                                                  |
| nqueens                 | 59.5 ms                                                             | 59.0 ms: 1.01x faster                                                  |
| logging_format          | 3.73 us                                                             | 3.71 us: 1.00x faster                                                  |
| sympy_str               | 151 ms                                                              | 150 ms: 1.00x faster                                                   |
| sympy_expand            | 242 ms                                                              | 241 ms: 1.00x faster                                                   |
| chaos                   | 49.3 ms                                                             | 49.2 ms: 1.00x faster                                                  |
| pidigits                | 282 ms                                                              | 283 ms: 1.00x slower                                                   |
| pickle_dict             | 17.9 us                                                             | 18.0 us: 1.00x slower                                                  |
| float                   | 51.7 ms                                                             | 51.9 ms: 1.00x slower                                                  |
| pprint_pformat          | 953 ms                                                              | 960 ms: 1.01x slower                                                   |
| pprint_safe_repr        | 467 ms                                                              | 471 ms: 1.01x slower                                                   |
| python_startup          | 9.19 ms                                                             | 9.29 ms: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                             | 16.3 us: 1.01x slower                                                  |
| async_tree_none         | 281 ms                                                              | 285 ms: 1.01x slower                                                   |
| python_startup_no_site  | 7.24 ms                                                             | 7.34 ms: 1.01x slower                                                  |
| async_generators        | 195 ms                                                              | 198 ms: 1.01x slower                                                   |
| raytrace                | 207 ms                                                              | 211 ms: 1.02x slower                                                   |
| deepcopy_reduce         | 1.90 us                                                             | 1.94 us: 1.02x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                             | 52.9 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 528 ms                                                              | 541 ms: 1.02x slower                                                   |
| bench_mp_pool           | 41.4 ms                                                             | 42.5 ms: 1.03x slower                                                  |
| deepcopy                | 222 us                                                              | 228 us: 1.03x slower                                                   |
| scimark_monte_carlo     | 46.9 ms                                                             | 48.3 ms: 1.03x slower                                                  |
| meteor_contest          | 73.9 ms                                                             | 76.3 ms: 1.03x slower                                                  |
| pyflate                 | 313 ms                                                              | 323 ms: 1.03x slower                                                   |
| async_tree_memoization  | 317 ms                                                              | 329 ms: 1.04x slower                                                   |
| deepcopy_memo           | 26.2 us                                                             | 27.2 us: 1.04x slower                                                  |
| async_tree_io           | 696 ms                                                              | 726 ms: 1.04x slower                                                   |
| pickle                  | 7.21 us                                                             | 7.63 us: 1.06x slower                                                  |
| sqlite_synth            | 1.29 us                                                             | 1.44 us: 1.12x slower                                                  |
| generators              | 28.4 ms                                                             | 32.0 ms: 1.13x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.02x faster                                                           |

Benchmark hidden because not significant (8): sympy_sum, sqlglot_transpile, xml_etree_iterparse, unpickle, thrift, sqlglot_parse, pickle_list, json
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
