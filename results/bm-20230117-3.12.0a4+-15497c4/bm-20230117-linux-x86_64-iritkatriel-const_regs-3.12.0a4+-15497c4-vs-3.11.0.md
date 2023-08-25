
# Results vs. 3.11.0

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.02x faster \*
- HPT reliability: 97.35%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 258 ms: 1.00x faster                                              |
| chameleon      | 6.47 ms                                                | 6.52 ms: 1.01x slower                                             |
| docutils       | 2.63 sec                                               | 2.60 sec: 1.01x faster                                            |
| html5lib       | 64.5 ms                                                | 60.9 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.5 ms: 1.05x faster                                             |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                              |
| nbody          | 93.1 ms                                                | 95.6 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.60 ms: 1.11x faster                                             |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                              |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.01x slower                                             |
| regex_dna      | 204 ms                                                 | 219 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.59 ms: 1.31x faster                                             |
| unpickle_pure_python | 228 us                                                 | 207 us: 1.10x faster                                              |
| json_loads           | 26.5 us                                                | 24.5 us: 1.08x faster                                             |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| pickle_pure_python   | 306 us                                                 | 295 us: 1.04x faster                                              |
| unpickle             | 13.7 us                                                | 13.3 us: 1.02x faster                                             |
| pickle_list          | 4.11 us                                                | 4.06 us: 1.01x faster                                             |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                             |
| xml_etree_process    | 53.9 ms                                                | 54.7 ms: 1.02x slower                                             |
| xml_etree_generate   | 76.2 ms                                                | 78.3 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.59 ms: 1.01x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 6.10 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.4 ms: 1.07x faster                                             |
| mako            | 10.1 ms                                                | 9.77 ms: 1.03x faster                                             |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                             |
| django_template | 32.6 ms                                                | 33.9 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                              |
| json_dumps              | 12.6 ms                                                | 9.59 ms: 1.31x faster                                             |
| regex_effbot            | 3.99 ms                                                | 3.60 ms: 1.11x faster                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.06 ms: 1.11x faster                                             |
| unpickle_pure_python    | 228 us                                                 | 207 us: 1.10x faster                                              |
| deltablue               | 3.67 ms                                                | 3.38 ms: 1.09x faster                                             |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                              |
| json_loads              | 26.5 us                                                | 24.5 us: 1.08x faster                                             |
| genshi_xml              | 51.8 ms                                                | 48.4 ms: 1.07x faster                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| html5lib                | 64.5 ms                                                | 60.9 ms: 1.06x faster                                             |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                             |
| deepcopy_memo           | 37.0 us                                                | 35.2 us: 1.05x faster                                             |
| float                   | 77.2 ms                                                | 73.5 ms: 1.05x faster                                             |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                            |
| richards                | 45.7 ms                                                | 43.8 ms: 1.04x faster                                             |
| async_generators        | 368 ms                                                 | 353 ms: 1.04x faster                                              |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                              |
| nqueens                 | 83.4 ms                                                | 79.9 ms: 1.04x faster                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.43 ms: 1.04x faster                                             |
| scimark_fft             | 328 ms                                                 | 316 ms: 1.04x faster                                              |
| telco                   | 6.58 ms                                                | 6.35 ms: 1.04x faster                                             |
| pickle_pure_python      | 306 us                                                 | 295 us: 1.04x faster                                              |
| logging_silent          | 101 ns                                                 | 97.7 ns: 1.04x faster                                             |
| mako                    | 10.1 ms                                                | 9.77 ms: 1.03x faster                                             |
| chaos                   | 69.2 ms                                                | 67.2 ms: 1.03x faster                                             |
| bench_thread_pool       | 819 us                                                 | 795 us: 1.03x faster                                              |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                             |
| unpack_sequence         | 43.1 ns                                                | 41.9 ns: 1.03x faster                                             |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                            |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                            |
| unpickle                | 13.7 us                                                | 13.3 us: 1.02x faster                                             |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                              |
| spectral_norm           | 100 ms                                                 | 97.9 ms: 1.02x faster                                             |
| fannkuch                | 388 ms                                                 | 380 ms: 1.02x faster                                              |
| hexiom                  | 6.37 ms                                                | 6.25 ms: 1.02x faster                                             |
| logging_simple          | 6.03 us                                                | 5.92 us: 1.02x faster                                             |
| pyflate                 | 418 ms                                                 | 411 ms: 1.02x faster                                              |
| logging_format          | 6.68 us                                                | 6.59 us: 1.01x faster                                             |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                             |
| pickle_list             | 4.11 us                                                | 4.06 us: 1.01x faster                                             |
| docutils                | 2.63 sec                                               | 2.60 sec: 1.01x faster                                            |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                             |
| pprint_safe_repr        | 701 ms                                                 | 695 ms: 1.01x faster                                              |
| thrift                  | 756 us                                                 | 751 us: 1.01x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                              |
| 2to3                    | 259 ms                                                 | 258 ms: 1.00x faster                                              |
| sympy_str               | 290 ms                                                 | 291 ms: 1.00x slower                                              |
| python_startup          | 8.52 ms                                                | 8.59 ms: 1.01x slower                                             |
| deepcopy                | 342 us                                                 | 345 us: 1.01x slower                                              |
| dulwich_log             | 63.7 ms                                                | 64.1 ms: 1.01x slower                                             |
| chameleon               | 6.47 ms                                                | 6.52 ms: 1.01x slower                                             |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                              |
| raytrace                | 297 ms                                                 | 301 ms: 1.01x slower                                              |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.01x slower                                             |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                             |
| xml_etree_process       | 53.9 ms                                                | 54.7 ms: 1.02x slower                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.10 ms: 1.02x slower                                             |
| sqlglot_normalize       | 108 ms                                                 | 110 ms: 1.02x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                            |
| nbody                   | 93.1 ms                                                | 95.6 ms: 1.03x slower                                             |
| xml_etree_generate      | 76.2 ms                                                | 78.3 ms: 1.03x slower                                             |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                             |
| deepcopy_reduce         | 2.94 us                                                | 3.02 us: 1.03x slower                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 762 ms: 1.03x slower                                              |
| gc_traversal            | 4.02 ms                                                | 4.15 ms: 1.03x slower                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.76 ms: 1.03x slower                                             |
| django_template         | 32.6 ms                                                | 33.9 ms: 1.04x slower                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.46 ms: 1.04x slower                                             |
| coroutines              | 25.5 ms                                                | 26.8 ms: 1.05x slower                                             |
| sympy_integrate         | 21.0 ms                                                | 22.1 ms: 1.05x slower                                             |
| generators              | 73.5 ms                                                | 77.6 ms: 1.06x slower                                             |
| async_tree_memoization  | 627 ms                                                 | 670 ms: 1.07x slower                                              |
| regex_dna               | 204 ms                                                 | 219 ms: 1.08x slower                                              |
| dask                    | 360 ms                                                 | 516 ms: 1.44x slower                                              |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (11): coverage, sqlglot_optimize, bench_mp_pool, crypto_pyaes, sympy_expand, scimark_lu, scimark_monte_carlo, unpickle_list, async_tree_none, meteor_contest, djangocms
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: mypy


# HPT report

- Reliability score: 97.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
