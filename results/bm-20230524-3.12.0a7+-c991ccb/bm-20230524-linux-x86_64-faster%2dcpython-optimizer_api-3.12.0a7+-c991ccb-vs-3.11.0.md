
# Results vs. 3.11.0

- fork: faster-cpython
- ref: optimizer_api
- machine: linux-x86_64
- commit hash: c991ccb
- commit date: 2023-05-24
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 271 ms: 1.05x slower                                                      |
| docutils       | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                    |
| tornado_http   | 96.3 ms                                                | 99.4 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.4 ms: 1.02x faster                                                     |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                      |
| float          | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.83 ms: 1.04x faster                                                     |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                     |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.82 ms: 1.28x faster                                                     |
| json_loads           | 26.5 us                                                | 24.7 us: 1.07x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 315 us: 1.03x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                     |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                                     |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                     |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 85.7 ms: 1.12x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.34 ms: 1.10x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.79 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 141 us: 3.44x faster                                                      |
| generators               | 73.5 ms                                                | 32.1 ms: 2.29x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| json_dumps               | 12.6 ms                                                | 9.82 ms: 1.28x faster                                                     |
| async_tree_none          | 526 ms                                                 | 466 ms: 1.13x faster                                                      |
| coroutines               | 25.5 ms                                                | 22.6 ms: 1.13x faster                                                     |
| richards_super           | 56.8 ms                                                | 50.7 ms: 1.12x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 1.17 sec: 1.11x faster                                                    |
| async_tree_memoization   | 627 ms                                                 | 569 ms: 1.10x faster                                                      |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                                     |
| json_loads               | 26.5 us                                                | 24.7 us: 1.07x faster                                                     |
| chaos                    | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.49 ms: 1.05x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.82 ms: 1.05x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 707 ms: 1.05x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.83 ms: 1.04x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                      |
| coverage                 | 100 ms                                                 | 96.7 ms: 1.04x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.17 ms: 1.03x faster                                                     |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                                     |
| richards                 | 45.7 ms                                                | 44.8 ms: 1.02x faster                                                     |
| nbody                    | 93.1 ms                                                | 91.4 ms: 1.02x faster                                                     |
| go                       | 140 ms                                                 | 138 ms: 1.02x faster                                                      |
| logging_silent           | 101 ns                                                 | 99.8 ns: 1.01x faster                                                     |
| nqueens                  | 83.4 ms                                                | 82.6 ms: 1.01x faster                                                     |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                      |
| bench_thread_pool        | 819 us                                                 | 828 us: 1.01x slower                                                      |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                     |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                     |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.01x slower                                                    |
| regex_v8                 | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                     |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                                     |
| mdp                      | 2.62 sec                                               | 2.67 sec: 1.02x slower                                                    |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| pickle_pure_python       | 306 us                                                 | 315 us: 1.03x slower                                                      |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| tornado_http             | 96.3 ms                                                | 99.4 ms: 1.03x slower                                                     |
| deepcopy_memo            | 37.0 us                                                | 38.4 us: 1.04x slower                                                     |
| unpickle_list            | 4.91 us                                                | 5.09 us: 1.04x slower                                                     |
| telco                    | 6.58 ms                                                | 6.83 ms: 1.04x slower                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                                    |
| docutils                 | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                    |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.7 ms: 1.04x slower                                                     |
| crypto_pyaes             | 74.7 ms                                                | 78.1 ms: 1.05x slower                                                     |
| pickle_dict              | 31.1 us                                                | 32.6 us: 1.05x slower                                                     |
| deepcopy                 | 342 us                                                 | 358 us: 1.05x slower                                                      |
| 2to3                     | 259 ms                                                 | 271 ms: 1.05x slower                                                      |
| logging_format           | 6.68 us                                                | 7.01 us: 1.05x slower                                                     |
| logging_simple           | 6.03 us                                                | 6.33 us: 1.05x slower                                                     |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                                      |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 741 ms: 1.06x slower                                                      |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.06x slower                                                      |
| sqlalchemy_declarative   | 138 ms                                                 | 147 ms: 1.06x slower                                                      |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 72.3 ms: 1.06x slower                                                     |
| float                    | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 68.2 ms: 1.07x slower                                                     |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                     |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                                     |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                                      |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.34 ms: 1.10x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.94 ms: 1.10x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 85.7 ms: 1.12x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.79 ms: 1.13x slower                                                     |
| async_generators         | 368 ms                                                 | 452 ms: 1.23x slower                                                      |
| unpack_sequence          | 43.1 ns                                                | 59.7 ns: 1.38x slower                                                     |
| dask                     | 360 ms                                                 | 539 ms: 1.50x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (7): xml_etree_iterparse, meteor_contest, tomli_loads, fannkuch, bench_mp_pool, raytrace, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
