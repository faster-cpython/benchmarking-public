
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 256 ms: 1.00x faster                                       |
| chameleon      | 6.52 ms                                                             | 6.62 ms: 1.02x slower                                      |
| docutils       | 2.59 sec                                                            | 2.56 sec: 1.01x faster                                     |
| tornado_http   | 96.7 ms                                                             | 94.9 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                               | 1.00x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 92.0 ms: 1.05x faster                                      |
| float          | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                      |
| pidigits       | 197 ms                                                              | 199 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                               | 1.02x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.11 ms: 1.07x faster                                      |
| regex_compile  | 137 ms                                                              | 138 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                               | 1.02x faster                                               |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 26.4 us: 1.17x faster                                      |
| json_loads           | 26.2 us                                                             | 25.0 us: 1.05x faster                                      |
| pickle               | 9.79 us                                                             | 9.44 us: 1.04x faster                                      |
| xml_etree_parse      | 162 ms                                                              | 159 ms: 1.02x faster                                       |
| xml_etree_iterparse  | 108 ms                                                              | 105 ms: 1.02x faster                                       |
| xml_etree_process    | 54.1 ms                                                             | 53.4 ms: 1.01x faster                                      |
| unpickle_pure_python | 228 us                                                              | 227 us: 1.01x faster                                       |
| pickle_pure_python   | 307 us                                                              | 305 us: 1.01x faster                                       |
| xml_etree_generate   | 76.5 ms                                                             | 76.1 ms: 1.01x faster                                      |
| unpickle_list        | 4.96 us                                                             | 5.00 us: 1.01x slower                                      |
| json_dumps           | 12.5 ms                                                             | 12.8 ms: 1.02x slower                                      |
| pickle_list          | 4.03 us                                                             | 4.30 us: 1.07x slower                                      |
| Geometric mean       | (ref)                                                               | 1.02x faster                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.49 ms: 1.00x slower                                      |
| python_startup_no_site | 5.98 ms                                                             | 5.99 ms: 1.00x slower                                      |
| Geometric mean         | (ref)                                                               | 1.00x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                             | 21.5 ms: 1.01x faster                                      |
| django_template | 32.9 ms                                                             | 32.6 ms: 1.01x faster                                      |
| genshi_xml      | 51.8 ms                                                             | 52.4 ms: 1.01x slower                                      |
| mako            | 9.82 ms                                                             | 9.96 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                               | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 26.4 us: 1.17x faster                                      |
| unpack_sequence         | 49.5 ns                                                             | 46.2 ns: 1.07x faster                                      |
| regex_effbot            | 3.32 ms                                                             | 3.11 ms: 1.07x faster                                      |
| logging_simple          | 6.09 us                                                             | 5.74 us: 1.06x faster                                      |
| nbody                   | 96.7 ms                                                             | 92.0 ms: 1.05x faster                                      |
| logging_format          | 6.64 us                                                             | 6.34 us: 1.05x faster                                      |
| json_loads              | 26.2 us                                                             | 25.0 us: 1.05x faster                                      |
| sympy_sum               | 167 ms                                                              | 161 ms: 1.04x faster                                       |
| pickle                  | 9.79 us                                                             | 9.44 us: 1.04x faster                                      |
| hexiom                  | 6.48 ms                                                             | 6.27 ms: 1.03x faster                                      |
| pylint                  | 476 ms                                                              | 462 ms: 1.03x faster                                       |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.0 ms: 1.03x faster                                      |
| richards                | 45.7 ms                                                             | 44.5 ms: 1.03x faster                                      |
| spectral_norm           | 99.5 ms                                                             | 97.3 ms: 1.02x faster                                      |
| json                    | 4.86 ms                                                             | 4.75 ms: 1.02x faster                                      |
| xml_etree_parse         | 162 ms                                                              | 159 ms: 1.02x faster                                       |
| coroutines              | 26.3 ms                                                             | 25.7 ms: 1.02x faster                                      |
| xml_etree_iterparse     | 108 ms                                                              | 105 ms: 1.02x faster                                       |
| thrift                  | 766 us                                                              | 750 us: 1.02x faster                                       |
| async_generators        | 361 ms                                                              | 354 ms: 1.02x faster                                       |
| float                   | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                      |
| raytrace                | 292 ms                                                              | 287 ms: 1.02x faster                                       |
| tornado_http            | 96.7 ms                                                             | 94.9 ms: 1.02x faster                                      |
| sympy_integrate         | 21.0 ms                                                             | 20.7 ms: 1.02x faster                                      |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                       |
| deepcopy_memo           | 36.4 us                                                             | 35.9 us: 1.01x faster                                      |
| xml_etree_process       | 54.1 ms                                                             | 53.4 ms: 1.01x faster                                      |
| genshi_text             | 21.8 ms                                                             | 21.5 ms: 1.01x faster                                      |
| docutils                | 2.59 sec                                                            | 2.56 sec: 1.01x faster                                     |
| sqlalchemy_declarative  | 138 ms                                                              | 137 ms: 1.01x faster                                       |
| sympy_str               | 291 ms                                                              | 288 ms: 1.01x faster                                       |
| bench_thread_pool       | 820 us                                                              | 811 us: 1.01x faster                                       |
| django_template         | 32.9 ms                                                             | 32.6 ms: 1.01x faster                                      |
| chaos                   | 68.0 ms                                                             | 67.3 ms: 1.01x faster                                      |
| dulwich_log             | 63.6 ms                                                             | 63.1 ms: 1.01x faster                                      |
| unpickle_pure_python    | 228 us                                                              | 227 us: 1.01x faster                                       |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                      |
| pickle_pure_python      | 307 us                                                              | 305 us: 1.01x faster                                       |
| xml_etree_generate      | 76.5 ms                                                             | 76.1 ms: 1.01x faster                                      |
| sympy_expand            | 477 ms                                                              | 475 ms: 1.00x faster                                       |
| 2to3                    | 257 ms                                                              | 256 ms: 1.00x faster                                       |
| gunicorn                | 1.13 ms                                                             | 1.13 ms: 1.00x faster                                      |
| python_startup          | 8.49 ms                                                             | 8.49 ms: 1.00x slower                                      |
| asyncio_tcp             | 888 ms                                                              | 890 ms: 1.00x slower                                       |
| python_startup_no_site  | 5.98 ms                                                             | 5.99 ms: 1.00x slower                                      |
| regex_compile           | 137 ms                                                              | 138 ms: 1.01x slower                                       |
| unpickle_list           | 4.96 us                                                             | 5.00 us: 1.01x slower                                      |
| sqlglot_optimize        | 53.4 ms                                                             | 53.9 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.51 ms: 1.01x slower                                      |
| async_tree_cpu_io_mixed | 736 ms                                                              | 743 ms: 1.01x slower                                       |
| pidigits                | 197 ms                                                              | 199 ms: 1.01x slower                                       |
| async_tree_memoization  | 621 ms                                                              | 628 ms: 1.01x slower                                       |
| genshi_xml              | 51.8 ms                                                             | 52.4 ms: 1.01x slower                                      |
| crypto_pyaes            | 73.8 ms                                                             | 74.8 ms: 1.01x slower                                      |
| mdp                     | 2.64 sec                                                            | 2.67 sec: 1.01x slower                                     |
| generators              | 73.4 ms                                                             | 74.4 ms: 1.01x slower                                      |
| mako                    | 9.82 ms                                                             | 9.96 ms: 1.01x slower                                      |
| chameleon               | 6.52 ms                                                             | 6.62 ms: 1.02x slower                                      |
| sqlglot_normalize       | 108 ms                                                              | 110 ms: 1.02x slower                                       |
| json_dumps              | 12.5 ms                                                             | 12.8 ms: 1.02x slower                                      |
| async_tree_io           | 1.28 sec                                                            | 1.31 sec: 1.02x slower                                     |
| create_gc_cycles        | 1.48 ms                                                             | 1.51 ms: 1.02x slower                                      |
| deepcopy_reduce         | 2.96 us                                                             | 3.03 us: 1.02x slower                                      |
| djangocms               | 32.3 us                                                             | 33.5 us: 1.04x slower                                      |
| logging_silent          | 98.7 ns                                                             | 103 ns: 1.04x slower                                       |
| deltablue               | 3.66 ms                                                             | 3.84 ms: 1.05x slower                                      |
| fannkuch                | 384 ms                                                              | 403 ms: 1.05x slower                                       |
| pickle_list             | 4.03 us                                                             | 4.30 us: 1.07x slower                                      |
| gc_traversal            | 3.63 ms                                                             | 4.21 ms: 1.16x slower                                      |
| comprehensions          | 22.2 us                                                             | 26.0 us: 1.17x slower                                      |
| sqlglot_transpile       | 1.65 ms                                                             | 2.05 ms: 1.24x slower                                      |
| sqlglot_parse           | 1.36 ms                                                             | 1.75 ms: 1.29x slower                                      |
| Geometric mean          | (ref)                                                               | 1.00x slower                                               |

Benchmark hidden because not significant (22): sqlalchemy_imperative, telco, mypy2, html5lib, pycparser, pprint_pformat, pprint_safe_repr, dask, pyflate, regex_dna, bench_mp_pool, regex_v8, async_tree_none, scimark_sor, aiohttp, nqueens, deepcopy, go, sqlite_synth, scimark_fft, scimark_lu, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage, flaskblogging
