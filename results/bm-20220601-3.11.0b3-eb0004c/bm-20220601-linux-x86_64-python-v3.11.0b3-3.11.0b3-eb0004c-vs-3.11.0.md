
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 256 ms: 1.00x faster                                       |
| chameleon      | 6.52 ms                                                             | 6.42 ms: 1.02x faster                                      |
| docutils       | 2.59 sec                                                            | 2.56 sec: 1.01x faster                                     |
| html5lib       | 64.0 ms                                                             | 62.8 ms: 1.02x faster                                      |
| tornado_http   | 96.7 ms                                                             | 94.7 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                               | 1.01x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 76.0 ms                                                             | 73.9 ms: 1.03x faster                                      |
| nbody          | 96.7 ms                                                             | 94.9 ms: 1.02x faster                                      |
| pidigits       | 197 ms                                                              | 194 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                               | 1.02x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 2.92 ms: 1.14x faster                                      |
| regex_v8       | 22.0 ms                                                             | 21.4 ms: 1.02x faster                                      |
| regex_dna      | 196 ms                                                              | 194 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                               | 1.04x faster                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 26.0 us: 1.19x faster                                      |
| json_loads           | 26.2 us                                                             | 24.9 us: 1.05x faster                                      |
| pickle               | 9.79 us                                                             | 9.37 us: 1.04x faster                                      |
| xml_etree_parse      | 162 ms                                                              | 158 ms: 1.02x faster                                       |
| pickle_pure_python   | 307 us                                                              | 301 us: 1.02x faster                                       |
| xml_etree_process    | 54.1 ms                                                             | 53.6 ms: 1.01x faster                                      |
| unpickle_pure_python | 228 us                                                              | 227 us: 1.00x faster                                       |
| json_dumps           | 12.5 ms                                                             | 12.7 ms: 1.01x slower                                      |
| pickle_list          | 4.03 us                                                             | 4.27 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                               | 1.02x faster                                               |

Benchmark hidden because not significant (4): unpickle_list, xml_etree_iterparse, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.51 ms: 1.00x slower                                      |
| python_startup_no_site | 5.98 ms                                                             | 6.01 ms: 1.00x slower                                      |
| Geometric mean         | (ref)                                                               | 1.00x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 32.9 ms                                                             | 33.0 ms: 1.00x slower                                      |
| genshi_text     | 21.8 ms                                                             | 22.0 ms: 1.01x slower                                      |
| genshi_xml      | 51.8 ms                                                             | 52.3 ms: 1.01x slower                                      |
| mako            | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                               | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 26.0 us: 1.19x faster                                      |
| regex_effbot            | 3.32 ms                                                             | 2.92 ms: 1.14x faster                                      |
| json_loads              | 26.2 us                                                             | 24.9 us: 1.05x faster                                      |
| logging_simple          | 6.09 us                                                             | 5.82 us: 1.05x faster                                      |
| logging_format          | 6.64 us                                                             | 6.35 us: 1.04x faster                                      |
| pickle                  | 9.79 us                                                             | 9.37 us: 1.04x faster                                      |
| sympy_sum               | 167 ms                                                              | 162 ms: 1.03x faster                                       |
| unpack_sequence         | 49.5 ns                                                             | 48.0 ns: 1.03x faster                                      |
| float                   | 76.0 ms                                                             | 73.9 ms: 1.03x faster                                      |
| xml_etree_parse         | 162 ms                                                              | 158 ms: 1.02x faster                                       |
| regex_v8                | 22.0 ms                                                             | 21.4 ms: 1.02x faster                                      |
| json                    | 4.86 ms                                                             | 4.74 ms: 1.02x faster                                      |
| pylint                  | 476 ms                                                              | 465 ms: 1.02x faster                                       |
| sympy_str               | 291 ms                                                              | 285 ms: 1.02x faster                                       |
| tornado_http            | 96.7 ms                                                             | 94.7 ms: 1.02x faster                                      |
| spectral_norm           | 99.5 ms                                                             | 97.5 ms: 1.02x faster                                      |
| pickle_pure_python      | 307 us                                                              | 301 us: 1.02x faster                                       |
| html5lib                | 64.0 ms                                                             | 62.8 ms: 1.02x faster                                      |
| nbody                   | 96.7 ms                                                             | 94.9 ms: 1.02x faster                                      |
| hexiom                  | 6.48 ms                                                             | 6.36 ms: 1.02x faster                                      |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.6 ms: 1.02x faster                                      |
| sympy_expand            | 477 ms                                                              | 469 ms: 1.02x faster                                       |
| async_generators        | 361 ms                                                              | 356 ms: 1.02x faster                                       |
| sympy_integrate         | 21.0 ms                                                             | 20.7 ms: 1.02x faster                                      |
| pidigits                | 197 ms                                                              | 194 ms: 1.02x faster                                       |
| chameleon               | 6.52 ms                                                             | 6.42 ms: 1.02x faster                                      |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.01x faster                                       |
| regex_dna               | 196 ms                                                              | 194 ms: 1.01x faster                                       |
| sqlalchemy_declarative  | 138 ms                                                              | 137 ms: 1.01x faster                                       |
| pyflate                 | 414 ms                                                              | 409 ms: 1.01x faster                                       |
| docutils                | 2.59 sec                                                            | 2.56 sec: 1.01x faster                                     |
| pprint_safe_repr        | 701 ms                                                              | 694 ms: 1.01x faster                                       |
| dulwich_log             | 63.6 ms                                                             | 63.0 ms: 1.01x faster                                      |
| xml_etree_process       | 54.1 ms                                                             | 53.6 ms: 1.01x faster                                      |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.01x faster                                       |
| coroutines              | 26.3 ms                                                             | 26.0 ms: 1.01x faster                                      |
| flaskblogging           | 7.09 ms                                                             | 7.04 ms: 1.01x faster                                      |
| unpickle_pure_python    | 228 us                                                              | 227 us: 1.00x faster                                       |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.00x faster                                      |
| gunicorn                | 1.13 ms                                                             | 1.12 ms: 1.00x faster                                      |
| bench_thread_pool       | 820 us                                                              | 816 us: 1.00x faster                                       |
| 2to3                    | 257 ms                                                              | 256 ms: 1.00x faster                                       |
| python_startup          | 8.49 ms                                                             | 8.51 ms: 1.00x slower                                      |
| deepcopy                | 339 us                                                              | 340 us: 1.00x slower                                       |
| django_template         | 32.9 ms                                                             | 33.0 ms: 1.00x slower                                      |
| generators              | 73.4 ms                                                             | 73.8 ms: 1.00x slower                                      |
| python_startup_no_site  | 5.98 ms                                                             | 6.01 ms: 1.00x slower                                      |
| aiohttp                 | 1.05 ms                                                             | 1.06 ms: 1.01x slower                                      |
| go                      | 138 ms                                                              | 139 ms: 1.01x slower                                       |
| sqlglot_normalize       | 108 ms                                                              | 109 ms: 1.01x slower                                       |
| sqlite_synth            | 2.51 us                                                             | 2.53 us: 1.01x slower                                      |
| deepcopy_reduce         | 2.96 us                                                             | 2.98 us: 1.01x slower                                      |
| json_dumps              | 12.5 ms                                                             | 12.7 ms: 1.01x slower                                      |
| genshi_text             | 21.8 ms                                                             | 22.0 ms: 1.01x slower                                      |
| genshi_xml              | 51.8 ms                                                             | 52.3 ms: 1.01x slower                                      |
| sqlglot_optimize        | 53.4 ms                                                             | 54.0 ms: 1.01x slower                                      |
| deepcopy_memo           | 36.4 us                                                             | 36.9 us: 1.01x slower                                      |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.02x slower                                     |
| mako                    | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                      |
| create_gc_cycles        | 1.48 ms                                                             | 1.51 ms: 1.02x slower                                      |
| mdp                     | 2.64 sec                                                            | 2.69 sec: 1.02x slower                                     |
| fannkuch                | 384 ms                                                              | 393 ms: 1.02x slower                                       |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.57 ms: 1.02x slower                                      |
| async_tree_memoization  | 621 ms                                                              | 636 ms: 1.02x slower                                       |
| logging_silent          | 98.7 ns                                                             | 101 ns: 1.03x slower                                       |
| pycparser               | 1.14 sec                                                            | 1.18 sec: 1.03x slower                                     |
| djangocms               | 32.3 us                                                             | 33.2 us: 1.03x slower                                      |
| gc_traversal            | 3.63 ms                                                             | 3.79 ms: 1.05x slower                                      |
| pickle_list             | 4.03 us                                                             | 4.27 us: 1.06x slower                                      |
| comprehensions          | 22.2 us                                                             | 25.9 us: 1.17x slower                                      |
| sqlglot_transpile       | 1.65 ms                                                             | 2.04 ms: 1.23x slower                                      |
| sqlglot_parse           | 1.36 ms                                                             | 1.75 ms: 1.29x slower                                      |
| Geometric mean          | (ref)                                                               | 1.00x faster                                               |

Benchmark hidden because not significant (23): sqlalchemy_imperative, richards, mypy2, thrift, scimark_sor, pprint_pformat, regex_compile, deltablue, nqueens, crypto_pyaes, dask, bench_mp_pool, unpickle_list, async_tree_cpu_io_mixed, xml_etree_iterparse, raytrace, asyncio_tcp, async_tree_none, telco, scimark_fft, xml_etree_generate, chaos, unpickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage
