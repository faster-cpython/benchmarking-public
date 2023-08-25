
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.02x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| chameleon      | 6.47 ms                                                | 6.57 ms: 1.01x slower                                 |
| html5lib       | 64.5 ms                                                | 60.1 ms: 1.07x faster                                 |
| tornado_http   | 96.3 ms                                                | 94.6 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 77.2 ms                                                | 72.5 ms: 1.06x faster                                 |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 2.93 ms: 1.36x faster                                 |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                  |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 25.6 us: 1.21x faster                                 |
| pickle               | 10.1 us                                                | 9.56 us: 1.05x faster                                 |
| json_loads           | 26.5 us                                                | 25.4 us: 1.04x faster                                 |
| unpickle             | 13.7 us                                                | 13.4 us: 1.02x faster                                 |
| json_dumps           | 12.6 ms                                                | 12.4 ms: 1.02x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 157 ms: 1.01x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.6 ms: 1.01x faster                                 |
| unpickle_pure_python | 228 us                                                 | 229 us: 1.00x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                 |
| xml_etree_iterparse  | 104 ms                                                 | 104 ms: 1.00x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                 |
| pickle_list          | 4.11 us                                                | 4.26 us: 1.03x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.25 ms: 1.03x faster                                 |
| python_startup_no_site | 6.01 ms                                                | 6.16 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.88 ms: 1.02x faster                                 |
| django_template | 32.6 ms                                                | 32.8 ms: 1.01x slower                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 2.93 ms: 1.36x faster                                 |
| pickle_dict             | 31.1 us                                                | 25.6 us: 1.21x faster                                 |
| html5lib                | 64.5 ms                                                | 60.1 ms: 1.07x faster                                 |
| float                   | 77.2 ms                                                | 72.5 ms: 1.06x faster                                 |
| pickle                  | 10.1 us                                                | 9.56 us: 1.05x faster                                 |
| json_loads              | 26.5 us                                                | 25.4 us: 1.04x faster                                 |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                  |
| logging_format          | 6.68 us                                                | 6.44 us: 1.04x faster                                 |
| sympy_sum               | 167 ms                                                 | 161 ms: 1.04x faster                                  |
| python_startup          | 8.52 ms                                                | 8.25 ms: 1.03x faster                                 |
| scimark_sor             | 118 ms                                                 | 115 ms: 1.03x faster                                  |
| logging_silent          | 101 ns                                                 | 98.2 ns: 1.03x faster                                 |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                  |
| regex_compile           | 138 ms                                                 | 135 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.03x faster                                 |
| spectral_norm           | 100 ms                                                 | 97.6 ms: 1.03x faster                                 |
| logging_simple          | 6.03 us                                                | 5.89 us: 1.02x faster                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 66.5 ms: 1.02x faster                                 |
| unpickle                | 13.7 us                                                | 13.4 us: 1.02x faster                                 |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                  |
| mako                    | 10.1 ms                                                | 9.88 ms: 1.02x faster                                 |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                 |
| thrift                  | 756 us                                                 | 741 us: 1.02x faster                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                 |
| json_dumps              | 12.6 ms                                                | 12.4 ms: 1.02x faster                                 |
| pyflate                 | 418 ms                                                 | 411 ms: 1.02x faster                                  |
| deltablue               | 3.67 ms                                                | 3.61 ms: 1.02x faster                                 |
| tornado_http            | 96.3 ms                                                | 94.6 ms: 1.02x faster                                 |
| sympy_expand            | 475 ms                                                 | 468 ms: 1.02x faster                                  |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                 |
| hexiom                  | 6.37 ms                                                | 6.29 ms: 1.01x faster                                 |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| scimark_fft             | 328 ms                                                 | 325 ms: 1.01x faster                                  |
| raytrace                | 297 ms                                                 | 294 ms: 1.01x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 157 ms: 1.01x faster                                  |
| chaos                   | 69.2 ms                                                | 68.6 ms: 1.01x faster                                 |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                  |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.3 ms: 1.01x faster                                 |
| xml_etree_process       | 53.9 ms                                                | 53.6 ms: 1.01x faster                                 |
| unpickle_pure_python    | 228 us                                                 | 229 us: 1.00x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                 |
| xml_etree_iterparse     | 104 ms                                                 | 104 ms: 1.00x slower                                  |
| django_template         | 32.6 ms                                                | 32.8 ms: 1.01x slower                                 |
| chameleon               | 6.47 ms                                                | 6.57 ms: 1.01x slower                                 |
| richards                | 45.7 ms                                                | 46.4 ms: 1.01x slower                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.57 ms: 1.02x slower                                 |
| nqueens                 | 83.4 ms                                                | 84.7 ms: 1.02x slower                                 |
| python_startup_no_site  | 6.01 ms                                                | 6.16 ms: 1.02x slower                                 |
| unpack_sequence         | 43.1 ns                                                | 44.3 ns: 1.03x slower                                 |
| unpickle_list           | 4.91 us                                                | 5.05 us: 1.03x slower                                 |
| pickle_list             | 4.11 us                                                | 4.26 us: 1.03x slower                                 |
| telco                   | 6.58 ms                                                | 6.84 ms: 1.04x slower                                 |
| Geometric mean          | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (6): json, pickle_pure_python, nbody, regex_dna, sqlite_synth, pycparser
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
