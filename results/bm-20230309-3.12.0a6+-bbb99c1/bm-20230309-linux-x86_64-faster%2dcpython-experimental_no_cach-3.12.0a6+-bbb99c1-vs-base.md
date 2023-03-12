
# Results vs. base

- fork: faster-cpython
- ref: experimental_no_cach
- machine: linux-x86_64
- commit hash: bbb99c1
- commit date: 2023-03-09
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 251 ms: 1.01x faster                                                             |
| docutils       | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                           |
| html5lib       | 62.7 ms                                                                | 61.0 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 74.7 ms                                                                | 73.8 ms: 1.01x faster                                                            |
| pidigits       | 190 ms                                                                 | 189 ms: 1.00x faster                                                             |
| nbody          | 88.8 ms                                                                | 95.1 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.43 ms: 1.02x faster                                                            |
| regex_dna      | 209 ms                                                                 | 205 ms: 1.02x faster                                                             |
| regex_compile  | 134 ms                                                                 | 133 ms: 1.01x faster                                                             |
| regex_v8       | 21.9 ms                                                                | 21.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_list          | 4.30 us                                                                | 4.04 us: 1.06x faster                                                            |
| unpickle_pure_python | 206 us                                                                 | 198 us: 1.04x faster                                                             |
| pickle               | 10.4 us                                                                | 10.2 us: 1.02x faster                                                            |
| xml_etree_generate   | 81.9 ms                                                                | 80.7 ms: 1.02x faster                                                            |
| xml_etree_parse      | 150 ms                                                                 | 148 ms: 1.01x faster                                                             |
| pickle_dict          | 31.7 us                                                                | 31.5 us: 1.01x faster                                                            |
| json_loads           | 24.3 us                                                                | 24.1 us: 1.00x faster                                                            |
| xml_etree_process    | 55.9 ms                                                                | 55.7 ms: 1.00x faster                                                            |
| pickle_pure_python   | 286 us                                                                 | 287 us: 1.01x slower                                                             |
| xml_etree_iterparse  | 99.7 ms                                                                | 103 ms: 1.03x slower                                                             |
| unpickle             | 13.4 us                                                                | 14.0 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): json_dumps, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.58 ms                                                                | 6.54 ms: 1.01x faster                                                            |
| python_startup         | 9.07 ms                                                                | 9.02 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 9.86 ms: 1.02x faster                                                            |
| django_template | 33.3 ms                                                                | 33.8 ms: 1.01x slower                                                            |
| genshi_text     | 21.7 ms                                                                | 22.1 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_list             | 4.30 us                                                                | 4.04 us: 1.06x faster                                                            |
| unpickle_pure_python    | 206 us                                                                 | 198 us: 1.04x faster                                                             |
| generators              | 30.7 ms                                                                | 29.8 ms: 1.03x faster                                                            |
| go                      | 138 ms                                                                 | 134 ms: 1.03x faster                                                             |
| chaos                   | 69.5 ms                                                                | 67.5 ms: 1.03x faster                                                            |
| html5lib                | 62.7 ms                                                                | 61.0 ms: 1.03x faster                                                            |
| unpack_sequence         | 43.9 ns                                                                | 42.8 ns: 1.03x faster                                                            |
| scimark_fft             | 325 ms                                                                 | 317 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 68.6 ms                                                                | 67.1 ms: 1.02x faster                                                            |
| mako                    | 10.1 ms                                                                | 9.86 ms: 1.02x faster                                                            |
| regex_effbot            | 3.51 ms                                                                | 3.43 ms: 1.02x faster                                                            |
| regex_dna               | 209 ms                                                                 | 205 ms: 1.02x faster                                                             |
| coverage                | 98.0 ms                                                                | 96.0 ms: 1.02x faster                                                            |
| raytrace                | 289 ms                                                                 | 283 ms: 1.02x faster                                                             |
| sqlglot_transpile       | 1.75 ms                                                                | 1.72 ms: 1.02x faster                                                            |
| coroutines              | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                                            |
| deepcopy                | 339 us                                                                 | 333 us: 1.02x faster                                                             |
| sqlglot_parse           | 1.46 ms                                                                | 1.43 ms: 1.02x faster                                                            |
| pickle                  | 10.4 us                                                                | 10.2 us: 1.02x faster                                                            |
| json                    | 4.68 ms                                                                | 4.60 ms: 1.02x faster                                                            |
| comprehensions          | 24.3 us                                                                | 23.9 us: 1.02x faster                                                            |
| richards                | 43.8 ms                                                                | 43.0 ms: 1.02x faster                                                            |
| pprint_safe_repr        | 691 ms                                                                 | 680 ms: 1.02x faster                                                             |
| logging_format          | 6.37 us                                                                | 6.27 us: 1.02x faster                                                            |
| xml_etree_generate      | 81.9 ms                                                                | 80.7 ms: 1.02x faster                                                            |
| sympy_str               | 288 ms                                                                 | 284 ms: 1.02x faster                                                             |
| deltablue               | 3.27 ms                                                                | 3.22 ms: 1.01x faster                                                            |
| sympy_integrate         | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                            |
| scimark_lu              | 113 ms                                                                 | 111 ms: 1.01x faster                                                             |
| sqlglot_optimize        | 51.3 ms                                                                | 50.6 ms: 1.01x faster                                                            |
| sqlglot_normalize       | 105 ms                                                                 | 103 ms: 1.01x faster                                                             |
| sympy_expand            | 468 ms                                                                 | 462 ms: 1.01x faster                                                             |
| dask                    | 516 ms                                                                 | 509 ms: 1.01x faster                                                             |
| deepcopy_memo           | 34.4 us                                                                | 34.0 us: 1.01x faster                                                            |
| pathlib                 | 17.9 ms                                                                | 17.7 ms: 1.01x faster                                                            |
| xml_etree_parse         | 150 ms                                                                 | 148 ms: 1.01x faster                                                             |
| hexiom                  | 6.23 ms                                                                | 6.16 ms: 1.01x faster                                                            |
| float                   | 74.7 ms                                                                | 73.8 ms: 1.01x faster                                                            |
| pycparser               | 1.16 sec                                                               | 1.15 sec: 1.01x faster                                                           |
| gunicorn                | 1.10 ms                                                                | 1.09 ms: 1.01x faster                                                            |
| aiohttp                 | 1.02 ms                                                                | 1.01 ms: 1.01x faster                                                            |
| sqlalchemy_declarative  | 139 ms                                                                 | 137 ms: 1.01x faster                                                             |
| docutils                | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                           |
| pprint_pformat          | 1.41 sec                                                               | 1.39 sec: 1.01x faster                                                           |
| sympy_sum               | 169 ms                                                                 | 167 ms: 1.01x faster                                                             |
| 2to3                    | 253 ms                                                                 | 251 ms: 1.01x faster                                                             |
| regex_compile           | 134 ms                                                                 | 133 ms: 1.01x faster                                                             |
| bench_thread_pool       | 796 us                                                                 | 789 us: 1.01x faster                                                             |
| scimark_sor             | 108 ms                                                                 | 108 ms: 1.01x faster                                                             |
| asyncio_tcp             | 512 ms                                                                 | 509 ms: 1.01x faster                                                             |
| mypy2                   | 335 ms                                                                 | 333 ms: 1.01x faster                                                             |
| pickle_dict             | 31.7 us                                                                | 31.5 us: 1.01x faster                                                            |
| regex_v8                | 21.9 ms                                                                | 21.8 ms: 1.01x faster                                                            |
| create_gc_cycles        | 1.50 ms                                                                | 1.49 ms: 1.01x faster                                                            |
| logging_simple          | 5.84 us                                                                | 5.81 us: 1.01x faster                                                            |
| python_startup_no_site  | 6.58 ms                                                                | 6.54 ms: 1.01x faster                                                            |
| python_startup          | 9.07 ms                                                                | 9.02 ms: 1.01x faster                                                            |
| thrift                  | 784 us                                                                 | 780 us: 1.00x faster                                                             |
| json_loads              | 24.3 us                                                                | 24.1 us: 1.00x faster                                                            |
| dulwich_log             | 64.2 ms                                                                | 63.9 ms: 1.00x faster                                                            |
| xml_etree_process       | 55.9 ms                                                                | 55.7 ms: 1.00x faster                                                            |
| pidigits                | 190 ms                                                                 | 189 ms: 1.00x faster                                                             |
| mdp                     | 2.40 sec                                                               | 2.42 sec: 1.01x slower                                                           |
| deepcopy_reduce         | 2.97 us                                                                | 2.99 us: 1.01x slower                                                            |
| fannkuch                | 364 ms                                                                 | 366 ms: 1.01x slower                                                             |
| pickle_pure_python      | 286 us                                                                 | 287 us: 1.01x slower                                                             |
| pyflate                 | 406 ms                                                                 | 410 ms: 1.01x slower                                                             |
| spectral_norm           | 95.9 ms                                                                | 96.9 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult | 4.45 ms                                                                | 4.50 ms: 1.01x slower                                                            |
| django_template         | 33.3 ms                                                                | 33.8 ms: 1.01x slower                                                            |
| genshi_text             | 21.7 ms                                                                | 22.1 ms: 1.02x slower                                                            |
| logging_silent          | 95.4 ns                                                                | 98.4 ns: 1.03x slower                                                            |
| xml_etree_iterparse     | 99.7 ms                                                                | 103 ms: 1.03x slower                                                             |
| gc_traversal            | 3.61 ms                                                                | 3.77 ms: 1.04x slower                                                            |
| unpickle                | 13.4 us                                                                | 14.0 us: 1.04x slower                                                            |
| nbody                   | 88.8 ms                                                                | 95.1 ms: 1.07x slower                                                            |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (18): nqueens, telco, json_dumps, async_tree_io, tornado_http, sqlite_synth, async_tree_memoization, bench_mp_pool, async_tree_cpu_io_mixed, meteor_contest, genshi_xml, async_tree_none, crypto_pyaes, unpickle_list, async_generators, chameleon, sqlalchemy_imperative, djangocms
