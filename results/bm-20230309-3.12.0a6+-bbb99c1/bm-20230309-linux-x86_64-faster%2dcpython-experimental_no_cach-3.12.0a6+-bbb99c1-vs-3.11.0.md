
# Results vs. 3.11.0

- fork: faster-cpython
- ref: experimental_no_cach
- machine: linux-x86_64
- commit hash: bbb99c1
- commit date: 2023-03-09
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.54 ms: 1.01x slower                                                            |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| html5lib       | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                            |
| tornado_http   | 96.3 ms                                                | 95.1 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.8 ms: 1.05x faster                                                            |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                             |
| nbody          | 93.1 ms                                                | 95.1 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                            |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| regex_dna      | 204 ms                                                 | 205 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                             |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.06x faster                                                             |
| pickle_list          | 4.11 us                                                | 4.04 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                            |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                            |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                                            |
| xml_etree_process    | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.6 ms: 1.07x faster                                                            |
| mako            | 10.1 ms                                                | 9.86 ms: 1.02x faster                                                            |
| genshi_text     | 21.6 ms                                                | 22.1 ms: 1.03x slower                                                            |
| django_template | 32.6 ms                                                | 33.8 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators             | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                            |
| asyncio_tcp            | 922 ms                                                 | 509 ms: 1.81x faster                                                             |
| json_dumps             | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                            |
| mypy2                  | 420 ms                                                 | 333 ms: 1.26x faster                                                             |
| regex_effbot           | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                            |
| unpickle_pure_python   | 228 us                                                 | 198 us: 1.15x faster                                                             |
| deltablue              | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                            |
| coroutines             | 25.5 ms                                                | 22.8 ms: 1.12x faster                                                            |
| scimark_sor            | 118 ms                                                 | 108 ms: 1.10x faster                                                             |
| json_loads             | 26.5 us                                                | 24.1 us: 1.10x faster                                                            |
| aiohttp                | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                            |
| deepcopy_memo          | 37.0 us                                                | 34.0 us: 1.09x faster                                                            |
| mdp                    | 2.62 sec                                               | 2.42 sec: 1.08x faster                                                           |
| gunicorn               | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                            |
| json                   | 4.94 ms                                                | 4.60 ms: 1.07x faster                                                            |
| xml_etree_parse        | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| gc_traversal           | 4.02 ms                                                | 3.77 ms: 1.07x faster                                                            |
| genshi_xml             | 51.8 ms                                                | 48.6 ms: 1.07x faster                                                            |
| logging_format         | 6.68 us                                                | 6.27 us: 1.07x faster                                                            |
| pickle_pure_python     | 306 us                                                 | 287 us: 1.06x faster                                                             |
| richards               | 45.7 ms                                                | 43.0 ms: 1.06x faster                                                            |
| fannkuch               | 388 ms                                                 | 366 ms: 1.06x faster                                                             |
| html5lib               | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                            |
| sqlglot_optimize       | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                            |
| raytrace               | 297 ms                                                 | 283 ms: 1.05x faster                                                             |
| float                  | 77.2 ms                                                | 73.8 ms: 1.05x faster                                                            |
| go                     | 140 ms                                                 | 134 ms: 1.05x faster                                                             |
| pprint_pformat         | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                           |
| pidigits               | 198 ms                                                 | 189 ms: 1.05x faster                                                             |
| sqlglot_normalize      | 108 ms                                                 | 103 ms: 1.04x faster                                                             |
| coverage               | 100 ms                                                 | 96.0 ms: 1.04x faster                                                            |
| logging_simple         | 6.03 us                                                | 5.81 us: 1.04x faster                                                            |
| regex_compile          | 138 ms                                                 | 133 ms: 1.04x faster                                                             |
| bench_thread_pool      | 819 us                                                 | 789 us: 1.04x faster                                                             |
| scimark_fft            | 328 ms                                                 | 317 ms: 1.04x faster                                                             |
| hexiom                 | 6.37 ms                                                | 6.16 ms: 1.03x faster                                                            |
| spectral_norm          | 100 ms                                                 | 96.9 ms: 1.03x faster                                                            |
| 2to3                   | 259 ms                                                 | 251 ms: 1.03x faster                                                             |
| docutils               | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| pprint_safe_repr       | 701 ms                                                 | 680 ms: 1.03x faster                                                             |
| meteor_contest         | 107 ms                                                 | 104 ms: 1.03x faster                                                             |
| nqueens                | 83.4 ms                                                | 81.0 ms: 1.03x faster                                                            |
| sympy_expand           | 475 ms                                                 | 462 ms: 1.03x faster                                                             |
| pathlib                | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                            |
| deepcopy               | 342 us                                                 | 333 us: 1.03x faster                                                             |
| pycparser              | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                           |
| logging_silent         | 101 ns                                                 | 98.4 ns: 1.03x faster                                                            |
| sympy_integrate        | 21.0 ms                                                | 20.5 ms: 1.03x faster                                                            |
| chaos                  | 69.2 ms                                                | 67.5 ms: 1.02x faster                                                            |
| mako                   | 10.1 ms                                                | 9.86 ms: 1.02x faster                                                            |
| sympy_str              | 290 ms                                                 | 284 ms: 1.02x faster                                                             |
| pyflate                | 418 ms                                                 | 410 ms: 1.02x faster                                                             |
| pickle_list            | 4.11 us                                                | 4.04 us: 1.02x faster                                                            |
| scimark_monte_carlo    | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                            |
| tornado_http           | 96.3 ms                                                | 95.1 ms: 1.01x faster                                                            |
| regex_v8               | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| xml_etree_iterparse    | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| unpack_sequence        | 43.1 ns                                                | 42.8 ns: 1.01x faster                                                            |
| async_tree_io          | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                           |
| crypto_pyaes           | 74.7 ms                                                | 74.3 ms: 1.01x faster                                                            |
| regex_dna              | 204 ms                                                 | 205 ms: 1.00x slower                                                             |
| sympy_sum              | 167 ms                                                 | 167 ms: 1.00x slower                                                             |
| sqlglot_transpile      | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                            |
| pickle                 | 10.1 us                                                | 10.2 us: 1.01x slower                                                            |
| chameleon              | 6.47 ms                                                | 6.54 ms: 1.01x slower                                                            |
| pickle_dict            | 31.1 us                                                | 31.5 us: 1.01x slower                                                            |
| sqlalchemy_imperative  | 17.9 ms                                                | 18.1 ms: 1.01x slower                                                            |
| scimark_lu             | 110 ms                                                 | 111 ms: 1.01x slower                                                             |
| unpickle_list          | 4.91 us                                                | 4.98 us: 1.01x slower                                                            |
| deepcopy_reduce        | 2.94 us                                                | 2.99 us: 1.02x slower                                                            |
| sqlglot_parse          | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                            |
| nbody                  | 93.1 ms                                                | 95.1 ms: 1.02x slower                                                            |
| genshi_text            | 21.6 ms                                                | 22.1 ms: 1.03x slower                                                            |
| thrift                 | 756 us                                                 | 780 us: 1.03x slower                                                             |
| xml_etree_process      | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                            |
| sqlite_synth           | 2.52 us                                                | 2.61 us: 1.04x slower                                                            |
| django_template        | 32.6 ms                                                | 33.8 ms: 1.04x slower                                                            |
| async_tree_memoization | 627 ms                                                 | 657 ms: 1.05x slower                                                             |
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                            |
| xml_etree_generate     | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                            |
| comprehensions         | 22.4 us                                                | 23.9 us: 1.06x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                            |
| async_generators       | 368 ms                                                 | 411 ms: 1.12x slower                                                             |
| dask                   | 360 ms                                                 | 509 ms: 1.41x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (10): sqlalchemy_declarative, async_tree_none, bench_mp_pool, create_gc_cycles, scimark_sparse_mat_mult, telco, dulwich_log, async_tree_cpu_io_mixed, djangocms, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
