
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c4e4b91
- commit date: 2022-02-03
- overall geometric mean: 1.04x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 267 ms: 1.04x slower                                  |
| chameleon      | 6.52 ms                                                             | 6.95 ms: 1.07x slower                                 |
| html5lib       | 64.0 ms                                                             | 67.9 ms: 1.06x slower                                 |
| tornado_http   | 96.7 ms                                                             | 106 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 197 ms                                                              | 190 ms: 1.04x faster                                  |
| nbody          | 96.7 ms                                                             | 94.7 ms: 1.02x faster                                 |
| float          | 76.0 ms                                                             | 77.5 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                               | 1.01x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.14 ms: 1.06x faster                                 |
| regex_compile  | 137 ms                                                              | 140 ms: 1.03x slower                                  |
| regex_dna      | 196 ms                                                              | 213 ms: 1.08x slower                                  |
| regex_v8       | 22.0 ms                                                             | 24.0 ms: 1.09x slower                                 |
| Geometric mean | (ref)                                                               | 1.04x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 28.1 us: 1.10x faster                                 |
| xml_etree_parse      | 162 ms                                                              | 153 ms: 1.06x faster                                  |
| json_dumps           | 12.5 ms                                                             | 12.2 ms: 1.03x faster                                 |
| xml_etree_iterparse  | 108 ms                                                              | 106 ms: 1.01x faster                                  |
| pickle               | 9.79 us                                                             | 9.93 us: 1.01x slower                                 |
| unpickle             | 13.2 us                                                             | 13.4 us: 1.02x slower                                 |
| json_loads           | 26.2 us                                                             | 26.7 us: 1.02x slower                                 |
| xml_etree_generate   | 76.5 ms                                                             | 79.6 ms: 1.04x slower                                 |
| xml_etree_process    | 54.1 ms                                                             | 57.0 ms: 1.05x slower                                 |
| unpickle_list        | 4.96 us                                                             | 5.26 us: 1.06x slower                                 |
| pickle_pure_python   | 307 us                                                              | 334 us: 1.09x slower                                  |
| unpickle_pure_python | 228 us                                                              | 249 us: 1.09x slower                                  |
| pickle_list          | 4.03 us                                                             | 4.47 us: 1.11x slower                                 |
| Geometric mean       | (ref)                                                               | 1.02x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.13 ms: 1.04x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 5.92 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                               | 1.03x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.82 ms                                                             | 10.5 ms: 1.07x slower                                 |
| django_template | 32.9 ms                                                             | 35.4 ms: 1.08x slower                                 |
| Geometric mean  | (ref)                                                               | 1.07x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 28.1 us: 1.10x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 46.0 ns: 1.07x faster                                 |
| xml_etree_parse         | 162 ms                                                              | 153 ms: 1.06x faster                                  |
| regex_effbot            | 3.32 ms                                                             | 3.14 ms: 1.06x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.13 ms: 1.04x faster                                 |
| logging_simple          | 6.09 us                                                             | 5.84 us: 1.04x faster                                 |
| logging_format          | 6.64 us                                                             | 6.37 us: 1.04x faster                                 |
| pidigits                | 197 ms                                                              | 190 ms: 1.04x faster                                  |
| json_dumps              | 12.5 ms                                                             | 12.2 ms: 1.03x faster                                 |
| nbody                   | 96.7 ms                                                             | 94.7 ms: 1.02x faster                                 |
| xml_etree_iterparse     | 108 ms                                                              | 106 ms: 1.01x faster                                  |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.01x faster                                  |
| python_startup_no_site  | 5.98 ms                                                             | 5.92 ms: 1.01x faster                                 |
| sympy_integrate         | 21.0 ms                                                             | 21.3 ms: 1.01x slower                                 |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                 |
| pickle                  | 9.79 us                                                             | 9.93 us: 1.01x slower                                 |
| sympy_sum               | 167 ms                                                              | 170 ms: 1.01x slower                                  |
| telco                   | 6.59 ms                                                             | 6.70 ms: 1.02x slower                                 |
| unpickle                | 13.2 us                                                             | 13.4 us: 1.02x slower                                 |
| json_loads              | 26.2 us                                                             | 26.7 us: 1.02x slower                                 |
| float                   | 76.0 ms                                                             | 77.5 ms: 1.02x slower                                 |
| regex_compile           | 137 ms                                                              | 140 ms: 1.03x slower                                  |
| dulwich_log             | 63.6 ms                                                             | 65.7 ms: 1.03x slower                                 |
| nqueens                 | 84.0 ms                                                             | 87.2 ms: 1.04x slower                                 |
| 2to3                    | 257 ms                                                              | 267 ms: 1.04x slower                                  |
| xml_etree_generate      | 76.5 ms                                                             | 79.6 ms: 1.04x slower                                 |
| pycparser               | 1.14 sec                                                            | 1.19 sec: 1.04x slower                                |
| fannkuch                | 384 ms                                                              | 400 ms: 1.04x slower                                  |
| hexiom                  | 6.48 ms                                                             | 6.76 ms: 1.04x slower                                 |
| sympy_str               | 291 ms                                                              | 304 ms: 1.04x slower                                  |
| spectral_norm           | 99.5 ms                                                             | 104 ms: 1.05x slower                                  |
| xml_etree_process       | 54.1 ms                                                             | 57.0 ms: 1.05x slower                                 |
| sympy_expand            | 477 ms                                                              | 503 ms: 1.06x slower                                  |
| scimark_fft             | 328 ms                                                              | 347 ms: 1.06x slower                                  |
| html5lib                | 64.0 ms                                                             | 67.9 ms: 1.06x slower                                 |
| unpickle_list           | 4.96 us                                                             | 5.26 us: 1.06x slower                                 |
| thrift                  | 766 us                                                              | 815 us: 1.06x slower                                  |
| go                      | 138 ms                                                              | 147 ms: 1.07x slower                                  |
| chameleon               | 6.52 ms                                                             | 6.95 ms: 1.07x slower                                 |
| mako                    | 9.82 ms                                                             | 10.5 ms: 1.07x slower                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.6 ms: 1.07x slower                                 |
| django_template         | 32.9 ms                                                             | 35.4 ms: 1.08x slower                                 |
| sqlite_synth            | 2.51 us                                                             | 2.71 us: 1.08x slower                                 |
| regex_dna               | 196 ms                                                              | 213 ms: 1.08x slower                                  |
| pickle_pure_python      | 307 us                                                              | 334 us: 1.09x slower                                  |
| unpickle_pure_python    | 228 us                                                              | 249 us: 1.09x slower                                  |
| tornado_http            | 96.7 ms                                                             | 106 ms: 1.09x slower                                  |
| regex_v8                | 22.0 ms                                                             | 24.0 ms: 1.09x slower                                 |
| raytrace                | 292 ms                                                              | 321 ms: 1.10x slower                                  |
| chaos                   | 68.0 ms                                                             | 74.9 ms: 1.10x slower                                 |
| scimark_lu              | 108 ms                                                              | 120 ms: 1.11x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.47 us: 1.11x slower                                 |
| pyflate                 | 414 ms                                                              | 459 ms: 1.11x slower                                  |
| richards                | 45.7 ms                                                             | 50.8 ms: 1.11x slower                                 |
| scimark_sor             | 115 ms                                                              | 129 ms: 1.12x slower                                  |
| deltablue               | 3.66 ms                                                             | 4.13 ms: 1.13x slower                                 |
| crypto_pyaes            | 73.8 ms                                                             | 83.8 ms: 1.14x slower                                 |
| logging_silent          | 98.7 ns                                                             | 113 ns: 1.14x slower                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 5.14 ms: 1.15x slower                                 |
| Geometric mean          | (ref)                                                               | 1.04x slower                                          |

Benchmark hidden because not significant (1): json
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
