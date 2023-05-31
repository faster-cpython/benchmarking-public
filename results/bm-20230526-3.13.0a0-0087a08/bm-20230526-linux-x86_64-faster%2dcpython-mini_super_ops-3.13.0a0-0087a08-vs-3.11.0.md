
# Results vs. 3.11.0

- fork: faster-cpython
- ref: mini_super_ops
- machine: linux-x86_64
- commit hash: 0087a08
- commit date: 2023-05-26
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.7 ms: 1.05x faster                                                     |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                      |
| float          | 77.2 ms                                                | 80.0 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.85 ms: 1.04x faster                                                     |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.91 ms: 1.27x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                                      |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                      |
| tomli_loads          | 2.22 sec                                               | 2.19 sec: 1.01x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                      |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                                     |
| pickle_dict          | 31.1 us                                                | 32.0 us: 1.03x slower                                                     |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                     |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 84.7 ms: 1.11x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.72 us: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 139 us: 3.50x faster                                                      |
| generators               | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| json_dumps               | 12.6 ms                                                | 9.91 ms: 1.27x faster                                                     |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                                      |
| coroutines               | 25.5 ms                                                | 21.8 ms: 1.17x faster                                                     |
| richards_super           | 56.8 ms                                                | 49.6 ms: 1.14x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                                     |
| chaos                    | 69.2 ms                                                | 62.7 ms: 1.10x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                                     |
| hexiom                   | 6.37 ms                                                | 5.92 ms: 1.08x faster                                                     |
| async_tree_none          | 526 ms                                                 | 492 ms: 1.07x faster                                                      |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                                     |
| nqueens                  | 83.4 ms                                                | 78.9 ms: 1.06x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 1.23 sec: 1.05x faster                                                    |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                                     |
| async_tree_memoization   | 627 ms                                                 | 597 ms: 1.05x faster                                                      |
| nbody                    | 93.1 ms                                                | 88.7 ms: 1.05x faster                                                     |
| coverage                 | 100 ms                                                 | 95.4 ms: 1.05x faster                                                     |
| logging_silent           | 101 ns                                                 | 96.8 ns: 1.04x faster                                                     |
| richards                 | 45.7 ms                                                | 43.8 ms: 1.04x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.85 ms: 1.04x faster                                                     |
| mdp                      | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                    |
| meteor_contest           | 107 ms                                                 | 103 ms: 1.03x faster                                                      |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                                      |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| json                     | 4.94 ms                                                | 4.80 ms: 1.03x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                      |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                      |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| scimark_sor              | 118 ms                                                 | 116 ms: 1.01x faster                                                      |
| tomli_loads              | 2.22 sec                                               | 2.19 sec: 1.01x faster                                                    |
| fannkuch                 | 388 ms                                                 | 383 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 52.5 ms: 1.01x faster                                                     |
| raytrace                 | 297 ms                                                 | 294 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                      |
| gc_traversal             | 4.02 ms                                                | 3.99 ms: 1.01x faster                                                     |
| unpickle_list            | 4.91 us                                                | 4.88 us: 1.01x faster                                                     |
| logging_simple           | 6.03 us                                                | 6.00 us: 1.01x faster                                                     |
| deepcopy_memo            | 37.0 us                                                | 36.8 us: 1.00x faster                                                     |
| bench_thread_pool        | 819 us                                                 | 817 us: 1.00x faster                                                      |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| regex_v8                 | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                     |
| deepcopy                 | 342 us                                                 | 345 us: 1.01x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                     |
| docutils                 | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                    |
| dulwich_log              | 63.7 ms                                                | 64.8 ms: 1.02x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 720 ms: 1.03x slower                                                      |
| telco                    | 6.58 ms                                                | 6.77 ms: 1.03x slower                                                     |
| pickle_dict              | 31.1 us                                                | 32.0 us: 1.03x slower                                                     |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| float                    | 77.2 ms                                                | 80.0 ms: 1.04x slower                                                     |
| crypto_pyaes             | 74.7 ms                                                | 77.7 ms: 1.04x slower                                                     |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 71.3 ms: 1.05x slower                                                     |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.10 us: 1.06x slower                                                     |
| regex_dna                | 204 ms                                                 | 216 ms: 1.06x slower                                                      |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                                      |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                                      |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.90 ms: 1.09x slower                                                     |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 84.7 ms: 1.11x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 48.7 ns: 1.13x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.72 us: 1.15x slower                                                     |
| async_generators         | 368 ms                                                 | 444 ms: 1.21x slower                                                      |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, regex_compile, tornado_http, bench_mp_pool, pickle_pure_python
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
