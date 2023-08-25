
# Results vs. 3.11.0

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                                     |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                   |
| html5lib       | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                    |
| tornado_http   | 96.3 ms                                                | 92.8 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.1 ms: 1.07x faster                                                    |
| nbody          | 93.1 ms                                                | 95.2 ms: 1.02x slower                                                    |
| pidigits       | 198 ms                                                 | 206 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                    |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                                     |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                    |
| regex_dna      | 204 ms                                                 | 218 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.30 ms: 1.35x faster                                                    |
| json_loads           | 26.5 us                                                | 23.4 us: 1.13x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                     |
| unpickle             | 13.7 us                                                | 13.1 us: 1.05x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                     |
| xml_etree_generate   | 76.2 ms                                                | 75.6 ms: 1.01x faster                                                    |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_list, pickle_dict, xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.41 ms: 1.01x faster                                                    |
| python_startup_no_site | 6.01 ms                                                | 5.94 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 49.1 ms: 1.05x faster                                                    |
| genshi_text    | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                    |
| mako           | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.30 ms: 1.35x faster                                                    |
| regex_effbot            | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                    |
| json_loads              | 26.5 us                                                | 23.4 us: 1.13x faster                                                    |
| deltablue               | 3.67 ms                                                | 3.27 ms: 1.12x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.12x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.05 ms: 1.11x faster                                                    |
| aiohttp                 | 1.10 ms                                                | 991 us: 1.11x faster                                                     |
| json                    | 4.94 ms                                                | 4.48 ms: 1.10x faster                                                    |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                    |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                                     |
| logging_silent          | 101 ns                                                 | 92.5 ns: 1.09x faster                                                    |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                                     |
| html5lib                | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                    |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                    |
| float                   | 77.2 ms                                                | 72.1 ms: 1.07x faster                                                    |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                                     |
| sqlalchemy_imperative   | 17.9 ms                                                | 16.7 ms: 1.07x faster                                                    |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                     |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                   |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                     |
| nqueens                 | 83.4 ms                                                | 78.9 ms: 1.06x faster                                                    |
| asyncio_tcp             | 922 ms                                                 | 872 ms: 1.06x faster                                                     |
| async_generators        | 368 ms                                                 | 349 ms: 1.06x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 49.1 ms: 1.05x faster                                                    |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                   |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                                    |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.76 us: 1.05x faster                                                    |
| bench_thread_pool       | 819 us                                                 | 782 us: 1.05x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                     |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                                     |
| unpickle                | 13.7 us                                                | 13.1 us: 1.05x faster                                                    |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.04x faster                                                    |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.04x faster                                                    |
| scimark_fft             | 328 ms                                                 | 315 ms: 1.04x faster                                                     |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.04x faster                                                    |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 133 ms: 1.04x faster                                                     |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                                    |
| tornado_http            | 96.3 ms                                                | 92.8 ms: 1.04x faster                                                    |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                     |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                    |
| sympy_str               | 290 ms                                                 | 280 ms: 1.04x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 65.9 ms: 1.03x faster                                                    |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                                    |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                    |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                                     |
| pylint                  | 465 ms                                                 | 453 ms: 1.03x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                     |
| async_tree_none         | 526 ms                                                 | 514 ms: 1.02x faster                                                     |
| raytrace                | 297 ms                                                 | 290 ms: 1.02x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed | 739 ms                                                 | 724 ms: 1.02x faster                                                     |
| thrift                  | 756 us                                                 | 742 us: 1.02x faster                                                     |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                     |
| coverage                | 100 ms                                                 | 98.3 ms: 1.02x faster                                                    |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                     |
| python_startup          | 8.52 ms                                                | 8.41 ms: 1.01x faster                                                    |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                    |
| python_startup_no_site  | 6.01 ms                                                | 5.94 ms: 1.01x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                   |
| xml_etree_generate      | 76.2 ms                                                | 75.6 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                    |
| gc_traversal            | 4.02 ms                                                | 4.03 ms: 1.00x slower                                                    |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                    |
| async_tree_memoization  | 627 ms                                                 | 636 ms: 1.01x slower                                                     |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                   |
| crypto_pyaes            | 74.7 ms                                                | 75.9 ms: 1.02x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                                    |
| spectral_norm           | 100 ms                                                 | 102 ms: 1.02x slower                                                     |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                    |
| unpack_sequence         | 43.1 ns                                                | 44.0 ns: 1.02x slower                                                    |
| nbody                   | 93.1 ms                                                | 95.2 ms: 1.02x slower                                                    |
| generators              | 73.5 ms                                                | 75.4 ms: 1.03x slower                                                    |
| pidigits                | 198 ms                                                 | 206 ms: 1.04x slower                                                     |
| regex_dna               | 204 ms                                                 | 218 ms: 1.07x slower                                                     |
| dask                    | 360 ms                                                 | 496 ms: 1.38x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (11): xml_etree_parse, django_template, pickle_list, chameleon, scimark_lu, pickle_dict, telco, bench_mp_pool, xml_etree_process, djangocms, unpickle_list
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
