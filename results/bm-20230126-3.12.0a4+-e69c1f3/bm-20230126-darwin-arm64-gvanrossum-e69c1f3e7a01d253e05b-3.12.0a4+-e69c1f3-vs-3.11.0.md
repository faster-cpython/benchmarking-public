
# Results vs. 3.11.0

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: darwin-arm64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.00x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| chameleon      | 4.61 ms                                                             | 4.58 ms: 1.01x faster                                                      |
| docutils       | 1.46 sec                                                            | 1.45 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                               | 1.00x faster                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 51.7 ms                                                             | 52.4 ms: 1.01x slower                                                      |
| nbody          | 65.2 ms                                                             | 64.4 ms: 1.01x faster                                                      |
| pidigits       | 282 ms                                                              | 283 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                               | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 76.3 ms                                                             | 73.6 ms: 1.04x faster                                                      |
| regex_dna      | 151 ms                                                              | 150 ms: 1.01x faster                                                       |
| regex_effbot   | 2.63 ms                                                             | 2.61 ms: 1.01x faster                                                      |
| regex_v8       | 16.5 ms                                                             | 16.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                               | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.67 ms                                                             | 6.15 ms: 1.25x faster                                                      |
| json_loads           | 16.1 us                                                             | 16.3 us: 1.01x slower                                                      |
| pickle               | 7.21 us                                                             | 7.55 us: 1.05x slower                                                      |
| pickle_list          | 2.86 us                                                             | 2.84 us: 1.01x faster                                                      |
| pickle_pure_python   | 200 us                                                              | 194 us: 1.03x faster                                                       |
| unpickle             | 9.68 us                                                             | 9.87 us: 1.02x slower                                                      |
| unpickle_list        | 2.64 us                                                             | 2.71 us: 1.03x slower                                                      |
| unpickle_pure_python | 159 us                                                              | 145 us: 1.10x faster                                                       |
| xml_etree_parse      | 99.6 ms                                                             | 94.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.6 ms                                                             | 68.3 ms: 1.04x slower                                                      |
| xml_etree_generate   | 48.4 ms                                                             | 49.3 ms: 1.02x slower                                                      |
| xml_etree_process    | 35.1 ms                                                             | 35.4 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                               | 1.02x faster                                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 9.40 ms: 1.02x slower                                                      |
| python_startup_no_site | 7.24 ms                                                             | 7.38 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.1 ms                                                             | 21.1 ms: 1.00x slower                                                      |
| genshi_text     | 15.3 ms                                                             | 14.8 ms: 1.04x faster                                                      |
| genshi_xml      | 30.5 ms                                                             | 28.9 ms: 1.05x faster                                                      |
| mako            | 8.40 ms                                                             | 7.29 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                               | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators        | 195 ms                                                              | 200 ms: 1.03x slower                                                       |
| async_tree_none         | 281 ms                                                              | 288 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 528 ms                                                              | 544 ms: 1.03x slower                                                       |
| async_tree_io           | 696 ms                                                              | 743 ms: 1.07x slower                                                       |
| async_tree_memoization  | 317 ms                                                              | 332 ms: 1.05x slower                                                       |
| chameleon               | 4.61 ms                                                             | 4.58 ms: 1.01x faster                                                      |
| chaos                   | 49.3 ms                                                             | 48.1 ms: 1.03x faster                                                      |
| bench_mp_pool           | 41.4 ms                                                             | 42.5 ms: 1.03x slower                                                      |
| bench_thread_pool       | 457 us                                                              | 447 us: 1.02x faster                                                       |
| coroutines              | 17.8 ms                                                             | 18.6 ms: 1.05x slower                                                      |
| coverage                | 58.4 ms                                                             | 57.4 ms: 1.02x faster                                                      |
| crypto_pyaes            | 51.7 ms                                                             | 52.1 ms: 1.01x slower                                                      |
| deepcopy                | 222 us                                                              | 220 us: 1.01x faster                                                       |
| deepcopy_reduce         | 1.90 us                                                             | 1.92 us: 1.01x slower                                                      |
| deltablue               | 2.82 ms                                                             | 2.59 ms: 1.09x faster                                                      |
| django_template         | 21.1 ms                                                             | 21.1 ms: 1.00x slower                                                      |
| docutils                | 1.46 sec                                                            | 1.45 sec: 1.01x faster                                                     |
| dulwich_log             | 29.1 ms                                                             | 28.5 ms: 1.02x faster                                                      |
| fannkuch                | 262 ms                                                              | 255 ms: 1.03x faster                                                       |
| float                   | 51.7 ms                                                             | 52.4 ms: 1.01x slower                                                      |
| generators              | 28.4 ms                                                             | 34.4 ms: 1.21x slower                                                      |
| genshi_text             | 15.3 ms                                                             | 14.8 ms: 1.04x faster                                                      |
| genshi_xml              | 30.5 ms                                                             | 28.9 ms: 1.05x faster                                                      |
| go                      | 109 ms                                                              | 109 ms: 1.00x faster                                                       |
| hexiom                  | 4.73 ms                                                             | 4.71 ms: 1.01x faster                                                      |
| json_dumps              | 7.67 ms                                                             | 6.15 ms: 1.25x faster                                                      |
| json_loads              | 16.1 us                                                             | 16.3 us: 1.01x slower                                                      |
| logging_format          | 3.73 us                                                             | 3.87 us: 1.04x slower                                                      |
| logging_silent          | 67.4 ns                                                             | 66.0 ns: 1.02x faster                                                      |
| logging_simple          | 3.47 us                                                             | 3.60 us: 1.04x slower                                                      |
| mako                    | 8.40 ms                                                             | 7.29 ms: 1.15x faster                                                      |
| mdp                     | 1.54 sec                                                            | 1.52 sec: 1.01x faster                                                     |
| meteor_contest          | 73.9 ms                                                             | 73.0 ms: 1.01x faster                                                      |
| mypy                    | 421 ms                                                              | 414 ms: 1.01x faster                                                       |
| nbody                   | 65.2 ms                                                             | 64.4 ms: 1.01x faster                                                      |
| nqueens                 | 59.5 ms                                                             | 59.7 ms: 1.00x slower                                                      |
| pathlib                 | 20.6 ms                                                             | 20.8 ms: 1.01x slower                                                      |
| pickle                  | 7.21 us                                                             | 7.55 us: 1.05x slower                                                      |
| pickle_list             | 2.86 us                                                             | 2.84 us: 1.01x faster                                                      |
| pickle_pure_python      | 200 us                                                              | 194 us: 1.03x faster                                                       |
| pidigits                | 282 ms                                                              | 283 ms: 1.00x slower                                                       |
| pprint_safe_repr        | 467 ms                                                              | 462 ms: 1.01x faster                                                       |
| pprint_pformat          | 953 ms                                                              | 941 ms: 1.01x faster                                                       |
| pycparser               | 694 ms                                                              | 680 ms: 1.02x faster                                                       |
| pyflate                 | 313 ms                                                              | 322 ms: 1.03x slower                                                       |
| python_startup          | 9.19 ms                                                             | 9.40 ms: 1.02x slower                                                      |
| python_startup_no_site  | 7.24 ms                                                             | 7.38 ms: 1.02x slower                                                      |
| raytrace                | 207 ms                                                              | 210 ms: 1.01x slower                                                       |
| regex_compile           | 76.3 ms                                                             | 73.6 ms: 1.04x faster                                                      |
| regex_dna               | 151 ms                                                              | 150 ms: 1.01x faster                                                       |
| regex_effbot            | 2.63 ms                                                             | 2.61 ms: 1.01x faster                                                      |
| regex_v8                | 16.5 ms                                                             | 16.1 ms: 1.02x faster                                                      |
| richards                | 32.7 ms                                                             | 30.7 ms: 1.07x faster                                                      |
| scimark_fft             | 201 ms                                                              | 193 ms: 1.04x faster                                                       |
| scimark_lu              | 72.2 ms                                                             | 71.5 ms: 1.01x faster                                                      |
| scimark_monte_carlo     | 46.9 ms                                                             | 45.7 ms: 1.03x faster                                                      |
| scimark_sor             | 83.3 ms                                                             | 85.2 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 2.83 ms: 1.13x faster                                                      |
| sqlglot_parse           | 948 us                                                              | 1.01 ms: 1.07x slower                                                      |
| sqlglot_transpile       | 1.11 ms                                                             | 1.18 ms: 1.06x slower                                                      |
| sqlglot_optimize        | 31.3 ms                                                             | 31.7 ms: 1.01x slower                                                      |
| sqlglot_normalize       | 171 ms                                                              | 174 ms: 1.02x slower                                                       |
| sqlite_synth            | 1.29 us                                                             | 1.36 us: 1.05x slower                                                      |
| sympy_expand            | 242 ms                                                              | 241 ms: 1.01x faster                                                       |
| sympy_integrate         | 11.5 ms                                                             | 11.2 ms: 1.03x faster                                                      |
| sympy_sum               | 85.5 ms                                                             | 82.0 ms: 1.04x faster                                                      |
| sympy_str               | 151 ms                                                              | 145 ms: 1.04x faster                                                       |
| thrift                  | 429 us                                                              | 444 us: 1.04x slower                                                       |
| unpack_sequence         | 33.1 ns                                                             | 33.6 ns: 1.01x slower                                                      |
| unpickle                | 9.68 us                                                             | 9.87 us: 1.02x slower                                                      |
| unpickle_list           | 2.64 us                                                             | 2.71 us: 1.03x slower                                                      |
| unpickle_pure_python    | 159 us                                                              | 145 us: 1.10x faster                                                       |
| xml_etree_parse         | 99.6 ms                                                             | 94.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse     | 65.6 ms                                                             | 68.3 ms: 1.04x slower                                                      |
| xml_etree_generate      | 48.4 ms                                                             | 49.3 ms: 1.02x slower                                                      |
| xml_etree_process       | 35.1 ms                                                             | 35.4 ms: 1.01x slower                                                      |
| Geometric mean          | (ref)                                                               | 1.00x faster                                                               |

Benchmark hidden because not significant (8): 2to3, deepcopy_memo, html5lib, json, pickle_dict, spectral_norm, telco, tornado_http
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: asyncio_tcp, create_gc_cycles, dask, gc_traversal
