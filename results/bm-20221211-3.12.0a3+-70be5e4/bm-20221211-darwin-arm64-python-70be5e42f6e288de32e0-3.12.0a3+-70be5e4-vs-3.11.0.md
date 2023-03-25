
# Results vs. 3.11.0

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: darwin-arm64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 161 ms: 1.00x faster                                                   |
| chameleon      | 4.55 ms                                                             | 4.45 ms: 1.02x faster                                                  |
| docutils       | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 64.0 ms: 1.02x faster                                                  |
| float          | 53.0 ms                                                             | 52.5 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.6 ms                                                             | 73.9 ms: 1.04x faster                                                  |
| regex_v8       | 16.1 ms                                                             | 15.7 ms: 1.02x faster                                                  |
| regex_dna      | 151 ms                                                              | 150 ms: 1.01x faster                                                   |
| regex_effbot   | 2.63 ms                                                             | 2.62 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.21 ms: 1.22x faster                                                  |
| xml_etree_parse      | 106 ms                                                              | 96.3 ms: 1.10x faster                                                  |
| unpickle_list        | 2.63 us                                                             | 2.58 us: 1.02x faster                                                  |
| unpickle_pure_python | 158 us                                                              | 156 us: 1.02x faster                                                   |
| xml_etree_generate   | 48.2 ms                                                             | 47.6 ms: 1.01x faster                                                  |
| xml_etree_process    | 35.0 ms                                                             | 34.7 ms: 1.01x faster                                                  |
| pickle_dict          | 17.9 us                                                             | 17.9 us: 1.00x slower                                                  |
| json_loads           | 16.0 us                                                             | 16.3 us: 1.01x slower                                                  |
| pickle               | 7.17 us                                                             | 7.52 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.02x faster                                                           |

Benchmark hidden because not significant (4): pickle_list, pickle_pure_python, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.2 ms: 1.01x faster                                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.3 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 7.99 ms: 1.05x faster                                                  |
| genshi_xml      | 29.9 ms                                                             | 28.7 ms: 1.04x faster                                                  |
| genshi_text     | 15.3 ms                                                             | 15.0 ms: 1.02x faster                                                  |
| django_template | 21.1 ms                                                             | 20.8 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 7.59 ms                                                             | 6.21 ms: 1.22x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 2.79 ms: 1.14x faster                                                  |
| deltablue               | 2.81 ms                                                             | 2.55 ms: 1.10x faster                                                  |
| richards                | 32.2 ms                                                             | 29.3 ms: 1.10x faster                                                  |
| xml_etree_parse         | 106 ms                                                              | 96.3 ms: 1.10x faster                                                  |
| logging_silent          | 68.0 ns                                                             | 63.3 ns: 1.07x faster                                                  |
| scimark_sor             | 82.9 ms                                                             | 78.2 ms: 1.06x faster                                                  |
| mako                    | 8.42 ms                                                             | 7.99 ms: 1.05x faster                                                  |
| create_gc_cycles        | 722 us                                                              | 692 us: 1.04x faster                                                   |
| genshi_xml              | 29.9 ms                                                             | 28.7 ms: 1.04x faster                                                  |
| regex_compile           | 76.6 ms                                                             | 73.9 ms: 1.04x faster                                                  |
| pycparser               | 695 ms                                                              | 672 ms: 1.03x faster                                                   |
| bench_thread_pool       | 474 us                                                              | 458 us: 1.03x faster                                                   |
| nqueens                 | 62.4 ms                                                             | 60.4 ms: 1.03x faster                                                  |
| pathlib                 | 28.3 ms                                                             | 27.5 ms: 1.03x faster                                                  |
| scimark_fft             | 200 ms                                                              | 194 ms: 1.03x faster                                                   |
| chameleon               | 4.55 ms                                                             | 4.45 ms: 1.02x faster                                                  |
| regex_v8                | 16.1 ms                                                             | 15.7 ms: 1.02x faster                                                  |
| nbody                   | 65.5 ms                                                             | 64.0 ms: 1.02x faster                                                  |
| unpack_sequence         | 33.5 ns                                                             | 32.8 ns: 1.02x faster                                                  |
| genshi_text             | 15.3 ms                                                             | 15.0 ms: 1.02x faster                                                  |
| mdp                     | 1.54 sec                                                            | 1.51 sec: 1.02x faster                                                 |
| unpickle_list           | 2.63 us                                                             | 2.58 us: 1.02x faster                                                  |
| unpickle_pure_python    | 158 us                                                              | 156 us: 1.02x faster                                                   |
| raytrace                | 207 ms                                                              | 204 ms: 1.02x faster                                                   |
| logging_simple          | 3.49 us                                                             | 3.44 us: 1.02x faster                                                  |
| hexiom                  | 4.73 ms                                                             | 4.68 ms: 1.01x faster                                                  |
| django_template         | 21.1 ms                                                             | 20.8 ms: 1.01x faster                                                  |
| xml_etree_generate      | 48.2 ms                                                             | 47.6 ms: 1.01x faster                                                  |
| scimark_lu              | 72.2 ms                                                             | 71.3 ms: 1.01x faster                                                  |
| regex_dna               | 151 ms                                                              | 150 ms: 1.01x faster                                                   |
| float                   | 53.0 ms                                                             | 52.5 ms: 1.01x faster                                                  |
| go                      | 109 ms                                                              | 108 ms: 1.01x faster                                                   |
| xml_etree_process       | 35.0 ms                                                             | 34.7 ms: 1.01x faster                                                  |
| logging_format          | 3.77 us                                                             | 3.74 us: 1.01x faster                                                  |
| docutils                | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                                 |
| python_startup          | 12.3 ms                                                             | 12.2 ms: 1.01x faster                                                  |
| fannkuch                | 260 ms                                                              | 259 ms: 1.01x faster                                                   |
| sqlglot_parse           | 956 us                                                              | 951 us: 1.00x faster                                                   |
| 2to3                    | 161 ms                                                              | 161 ms: 1.00x faster                                                   |
| regex_effbot            | 2.63 ms                                                             | 2.62 ms: 1.00x faster                                                  |
| gc_traversal            | 2.41 ms                                                             | 2.41 ms: 1.00x slower                                                  |
| thrift                  | 431 us                                                              | 433 us: 1.00x slower                                                   |
| sympy_expand            | 243 ms                                                              | 244 ms: 1.00x slower                                                   |
| pickle_dict             | 17.9 us                                                             | 17.9 us: 1.00x slower                                                  |
| chaos                   | 49.4 ms                                                             | 49.6 ms: 1.00x slower                                                  |
| sympy_str               | 151 ms                                                              | 152 ms: 1.00x slower                                                   |
| telco                   | 3.40 ms                                                             | 3.42 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 172 ms: 1.01x slower                                                   |
| sympy_sum               | 86.0 ms                                                             | 86.6 ms: 1.01x slower                                                  |
| json                    | 2.77 ms                                                             | 2.80 ms: 1.01x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                             | 31.6 ms: 1.01x slower                                                  |
| json_loads              | 16.0 us                                                             | 16.3 us: 1.01x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                             | 47.2 ms: 1.01x slower                                                  |
| crypto_pyaes            | 51.8 ms                                                             | 52.7 ms: 1.02x slower                                                  |
| asyncio_tcp             | 651 ms                                                              | 665 ms: 1.02x slower                                                   |
| python_startup_no_site  | 10.1 ms                                                             | 10.3 ms: 1.02x slower                                                  |
| async_tree_none         | 285 ms                                                              | 291 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed | 534 ms                                                              | 547 ms: 1.02x slower                                                   |
| async_generators        | 195 ms                                                              | 201 ms: 1.03x slower                                                   |
| pprint_pformat          | 946 ms                                                              | 978 ms: 1.03x slower                                                   |
| comprehensions          | 16.1 us                                                             | 16.6 us: 1.03x slower                                                  |
| coroutines              | 17.7 ms                                                             | 18.4 ms: 1.04x slower                                                  |
| pprint_safe_repr        | 463 ms                                                              | 480 ms: 1.04x slower                                                   |
| deepcopy                | 224 us                                                              | 232 us: 1.04x slower                                                   |
| meteor_contest          | 73.3 ms                                                             | 76.4 ms: 1.04x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                             | 1.99 us: 1.04x slower                                                  |
| pickle                  | 7.17 us                                                             | 7.52 us: 1.05x slower                                                  |
| async_tree_io           | 707 ms                                                              | 747 ms: 1.06x slower                                                   |
| pyflate                 | 309 ms                                                              | 327 ms: 1.06x slower                                                   |
| deepcopy_memo           | 26.3 us                                                             | 28.0 us: 1.07x slower                                                  |
| sqlite_synth            | 1.28 us                                                             | 1.44 us: 1.12x slower                                                  |
| generators              | 28.6 ms                                                             | 32.7 ms: 1.15x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.00x faster                                                           |

Benchmark hidden because not significant (15): async_tree_memoization, html5lib, dask, pickle_list, sqlglot_transpile, dulwich_log, pickle_pure_python, sympy_integrate, xml_etree_iterparse, pidigits, spectral_norm, unpickle, coverage, bench_mp_pool, mypy2
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
