
# Results vs. 3.11.0

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                                            |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                           |
| html5lib       | 64.5 ms                                                | 60.2 ms: 1.07x faster                                                            |
| tornado_http   | 96.3 ms                                                | 93.4 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                            |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                            |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                             |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                            |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                             |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                                            |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                                            |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.02x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (3): pickle_list, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.57 ms: 1.01x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.13 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                            |
| genshi_text     | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                            |
| mako            | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                            |
| django_template | 32.6 ms                                                | 32.2 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                             |
| json_dumps              | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.01 ms: 1.12x faster                                                            |
| regex_effbot            | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                            |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                            |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                             |
| logging_silent          | 101 ns                                                 | 91.5 ns: 1.11x faster                                                            |
| deepcopy_memo           | 37.0 us                                                | 33.5 us: 1.10x faster                                                            |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                            |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                            |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                            |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.09x faster                                                           |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                             |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                            |
| html5lib                | 64.5 ms                                                | 60.2 ms: 1.07x faster                                                            |
| hexiom                  | 6.37 ms                                                | 5.95 ms: 1.07x faster                                                            |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                           |
| pyflate                 | 418 ms                                                 | 394 ms: 1.06x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                             |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                           |
| gc_traversal            | 4.02 ms                                                | 3.79 ms: 1.06x faster                                                            |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 64.3 ms: 1.06x faster                                                            |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                                            |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.71 us: 1.06x faster                                                            |
| telco                   | 6.58 ms                                                | 6.24 ms: 1.06x faster                                                            |
| pprint_safe_repr        | 701 ms                                                 | 666 ms: 1.05x faster                                                             |
| bench_thread_pool       | 819 us                                                 | 778 us: 1.05x faster                                                             |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                             |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                            |
| nqueens                 | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                            |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                             |
| json                    | 4.94 ms                                                | 4.72 ms: 1.05x faster                                                            |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                             |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                           |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                                            |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                            |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                             |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.04x faster                                                            |
| mako                    | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                            |
| chaos                   | 69.2 ms                                                | 66.9 ms: 1.03x faster                                                            |
| coroutines              | 25.5 ms                                                | 24.7 ms: 1.03x faster                                                            |
| dulwich_log             | 63.7 ms                                                | 61.6 ms: 1.03x faster                                                            |
| raytrace                | 297 ms                                                 | 287 ms: 1.03x faster                                                             |
| tornado_http            | 96.3 ms                                                | 93.4 ms: 1.03x faster                                                            |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                             |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| spectral_norm           | 100 ms                                                 | 97.6 ms: 1.03x faster                                                            |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                             |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                            |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                            |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                             |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                                             |
| chameleon               | 6.47 ms                                                | 6.37 ms: 1.02x faster                                                            |
| deepcopy_reduce         | 2.94 us                                                | 2.89 us: 1.02x faster                                                            |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                                            |
| thrift                  | 756 us                                                 | 746 us: 1.01x faster                                                             |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| django_template         | 32.6 ms                                                | 32.2 ms: 1.01x faster                                                            |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                            |
| crypto_pyaes            | 74.7 ms                                                | 74.3 ms: 1.00x faster                                                            |
| python_startup          | 8.52 ms                                                | 8.57 ms: 1.01x slower                                                            |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.02x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                            |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.13 ms: 1.02x slower                                                            |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                           |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                             |
| generators              | 73.5 ms                                                | 77.2 ms: 1.05x slower                                                            |
| dask                    | 360 ms                                                 | 496 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (11): async_tree_none, coverage, unpack_sequence, pickle_list, xml_etree_process, bench_mp_pool, sqlglot_parse, pickle, nbody, async_tree_cpu_io_mixed, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230113-3.12.0a4+-df06ef8/bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
