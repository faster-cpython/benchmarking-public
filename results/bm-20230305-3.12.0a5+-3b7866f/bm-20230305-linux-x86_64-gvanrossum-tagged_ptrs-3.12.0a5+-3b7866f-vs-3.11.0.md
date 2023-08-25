
# Results vs. 3.11.0

- fork: gvanrossum
- ref: tagged_ptrs
- machine: linux-x86_64
- commit hash: 3b7866f
- commit date: 2023-03-05
- overall geometric mean: 1.01x faster \*
- HPT reliability: 75.43%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.01x faster                                              |
| chameleon      | 6.47 ms                                                | 6.64 ms: 1.03x slower                                             |
| docutils       | 2.63 sec                                               | 2.59 sec: 1.01x faster                                            |
| html5lib       | 64.5 ms                                                | 63.2 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                              |
| float          | 77.2 ms                                                | 76.0 ms: 1.02x faster                                             |
| nbody          | 93.1 ms                                                | 101 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.36 ms: 1.19x faster                                             |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                              |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.58 ms: 1.31x faster                                             |
| json_loads           | 26.5 us                                                | 23.7 us: 1.11x faster                                             |
| unpickle_pure_python | 228 us                                                 | 208 us: 1.10x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| pickle_pure_python   | 306 us                                                 | 297 us: 1.03x faster                                              |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                              |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                             |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                             |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                             |
| xml_etree_process    | 53.9 ms                                                | 57.4 ms: 1.07x slower                                             |
| xml_etree_generate   | 76.2 ms                                                | 83.1 ms: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.7 ms: 1.04x faster                                             |
| genshi_text     | 21.6 ms                                                | 22.0 ms: 1.02x slower                                             |
| mako            | 10.1 ms                                                | 10.5 ms: 1.04x slower                                             |
| django_template | 32.6 ms                                                | 34.3 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.3 ms: 2.34x faster                                             |
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.83x faster                                              |
| json_dumps              | 12.6 ms                                                | 9.58 ms: 1.31x faster                                             |
| mypy2                   | 420 ms                                                 | 340 ms: 1.24x faster                                              |
| regex_effbot            | 3.99 ms                                                | 3.36 ms: 1.19x faster                                             |
| json_loads              | 26.5 us                                                | 23.7 us: 1.11x faster                                             |
| deltablue               | 3.67 ms                                                | 3.34 ms: 1.10x faster                                             |
| unpickle_pure_python    | 228 us                                                 | 208 us: 1.10x faster                                              |
| json                    | 4.94 ms                                                | 4.56 ms: 1.08x faster                                             |
| aiohttp                 | 1.10 ms                                                | 1.02 ms: 1.08x faster                                             |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| coroutines              | 25.5 ms                                                | 24.0 ms: 1.06x faster                                             |
| genshi_xml              | 51.8 ms                                                | 49.7 ms: 1.04x faster                                             |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                            |
| logging_format          | 6.68 us                                                | 6.46 us: 1.03x faster                                             |
| coverage                | 100 ms                                                 | 97.0 ms: 1.03x faster                                             |
| richards                | 45.7 ms                                                | 44.3 ms: 1.03x faster                                             |
| pickle_pure_python      | 306 us                                                 | 297 us: 1.03x faster                                              |
| scimark_sor             | 118 ms                                                 | 115 ms: 1.03x faster                                              |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                              |
| logging_silent          | 101 ns                                                 | 98.7 ns: 1.02x faster                                             |
| html5lib                | 64.5 ms                                                | 63.2 ms: 1.02x faster                                             |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                              |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                             |
| logging_simple          | 6.03 us                                                | 5.92 us: 1.02x faster                                             |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                              |
| float                   | 77.2 ms                                                | 76.0 ms: 1.02x faster                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                             |
| 2to3                    | 259 ms                                                 | 255 ms: 1.01x faster                                              |
| docutils                | 2.63 sec                                               | 2.59 sec: 1.01x faster                                            |
| bench_thread_pool       | 819 us                                                 | 808 us: 1.01x faster                                              |
| sqlglot_optimize        | 53.1 ms                                                | 52.6 ms: 1.01x faster                                             |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.00x faster                                            |
| sympy_integrate         | 21.0 ms                                                | 20.9 ms: 1.00x faster                                             |
| pyflate                 | 418 ms                                                 | 420 ms: 1.00x slower                                              |
| pickle_dict             | 31.1 us                                                | 31.3 us: 1.01x slower                                             |
| raytrace                | 297 ms                                                 | 299 ms: 1.01x slower                                              |
| dulwich_log             | 63.7 ms                                                | 64.3 ms: 1.01x slower                                             |
| sqlalchemy_declarative  | 138 ms                                                 | 140 ms: 1.01x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                            |
| gc_traversal            | 4.02 ms                                                | 4.07 ms: 1.01x slower                                             |
| pprint_safe_repr        | 701 ms                                                 | 710 ms: 1.01x slower                                              |
| deepcopy                | 342 us                                                 | 346 us: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.01x slower                                              |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                            |
| crypto_pyaes            | 74.7 ms                                                | 75.9 ms: 1.02x slower                                             |
| sympy_sum               | 167 ms                                                 | 169 ms: 1.02x slower                                              |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                              |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                             |
| hexiom                  | 6.37 ms                                                | 6.49 ms: 1.02x slower                                             |
| genshi_text             | 21.6 ms                                                | 22.0 ms: 1.02x slower                                             |
| spectral_norm           | 100 ms                                                 | 102 ms: 1.02x slower                                              |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.3 ms: 1.02x slower                                             |
| chaos                   | 69.2 ms                                                | 70.7 ms: 1.02x slower                                             |
| chameleon               | 6.47 ms                                                | 6.64 ms: 1.03x slower                                             |
| scimark_fft             | 328 ms                                                 | 337 ms: 1.03x slower                                              |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                             |
| thrift                  | 756 us                                                 | 783 us: 1.04x slower                                              |
| mako                    | 10.1 ms                                                | 10.5 ms: 1.04x slower                                             |
| unpack_sequence         | 43.1 ns                                                | 44.8 ns: 1.04x slower                                             |
| nqueens                 | 83.4 ms                                                | 86.7 ms: 1.04x slower                                             |
| unpickle_list           | 4.91 us                                                | 5.11 us: 1.04x slower                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 70.9 ms: 1.04x slower                                             |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                             |
| scimark_lu              | 110 ms                                                 | 115 ms: 1.05x slower                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.78 ms: 1.05x slower                                             |
| django_template         | 32.6 ms                                                | 34.3 ms: 1.05x slower                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.48 ms: 1.06x slower                                             |
| python_startup          | 8.52 ms                                                | 9.02 ms: 1.06x slower                                             |
| deepcopy_reduce         | 2.94 us                                                | 3.12 us: 1.06x slower                                             |
| xml_etree_process       | 53.9 ms                                                | 57.4 ms: 1.07x slower                                             |
| async_tree_memoization  | 627 ms                                                 | 670 ms: 1.07x slower                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.86 ms: 1.08x slower                                             |
| nbody                   | 93.1 ms                                                | 101 ms: 1.08x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                             |
| xml_etree_generate      | 76.2 ms                                                | 83.1 ms: 1.09x slower                                             |
| comprehensions          | 22.4 us                                                | 25.2 us: 1.12x slower                                             |
| async_generators        | 368 ms                                                 | 423 ms: 1.15x slower                                              |
| dask                    | 360 ms                                                 | 517 ms: 1.44x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (12): deepcopy_memo, tornado_http, sqlglot_normalize, regex_compile, bench_mp_pool, go, unpickle, telco, sympy_str, async_tree_none, pickle, djangocms
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 75.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
