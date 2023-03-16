
# Results vs. base

- fork: faster-cpython
- ref: allow_non_python_fra
- machine: linux-x86_64
- commit hash: 3e2c3ab
- commit date: 2023-03-15
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 252 ms: 1.00x faster                                                             |
| chameleon      | 6.49 ms                                                                | 6.42 ms: 1.01x faster                                                            |
| docutils       | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 88.8 ms                                                                | 95.6 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                     |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.36 ms: 1.04x faster                                                            |
| regex_dna      | 209 ms                                                                 | 203 ms: 1.03x faster                                                             |
| regex_v8       | 21.9 ms                                                                | 21.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_list          | 4.30 us                                                                | 4.12 us: 1.04x faster                                                            |
| unpickle_pure_python | 206 us                                                                 | 201 us: 1.02x faster                                                             |
| pickle_dict          | 31.7 us                                                                | 31.1 us: 1.02x faster                                                            |
| pickle               | 10.4 us                                                                | 10.2 us: 1.01x faster                                                            |
| xml_etree_parse      | 150 ms                                                                 | 148 ms: 1.01x faster                                                             |
| xml_etree_process    | 55.9 ms                                                                | 55.2 ms: 1.01x faster                                                            |
| xml_etree_generate   | 81.9 ms                                                                | 81.0 ms: 1.01x faster                                                            |
| json_loads           | 24.3 us                                                                | 24.4 us: 1.01x slower                                                            |
| unpickle_list        | 4.96 us                                                                | 5.05 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_pure_python, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.58 ms                                                                | 6.54 ms: 1.01x faster                                                            |
| python_startup         | 9.07 ms                                                                | 9.02 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 48.4 ms                                                                | 47.7 ms: 1.02x faster                                                            |
| genshi_text     | 21.7 ms                                                                | 21.5 ms: 1.01x faster                                                            |
| mako            | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                            |
| django_template | 33.3 ms                                                                | 33.5 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 30.7 ms                                                                | 29.3 ms: 1.05x faster                                                            |
| coverage                | 98.0 ms                                                                | 93.6 ms: 1.05x faster                                                            |
| pickle_list             | 4.30 us                                                                | 4.12 us: 1.04x faster                                                            |
| regex_effbot            | 3.51 ms                                                                | 3.36 ms: 1.04x faster                                                            |
| regex_dna               | 209 ms                                                                 | 203 ms: 1.03x faster                                                             |
| pycparser               | 1.16 sec                                                               | 1.13 sec: 1.03x faster                                                           |
| chaos                   | 69.5 ms                                                                | 67.9 ms: 1.02x faster                                                            |
| unpickle_pure_python    | 206 us                                                                 | 201 us: 1.02x faster                                                             |
| comprehensions          | 24.3 us                                                                | 23.8 us: 1.02x faster                                                            |
| pickle_dict             | 31.7 us                                                                | 31.1 us: 1.02x faster                                                            |
| deltablue               | 3.27 ms                                                                | 3.21 ms: 1.02x faster                                                            |
| scimark_sor             | 108 ms                                                                 | 107 ms: 1.02x faster                                                             |
| coroutines              | 23.2 ms                                                                | 22.9 ms: 1.02x faster                                                            |
| scimark_fft             | 325 ms                                                                 | 319 ms: 1.02x faster                                                             |
| genshi_xml              | 48.4 ms                                                                | 47.7 ms: 1.02x faster                                                            |
| telco                   | 6.62 ms                                                                | 6.52 ms: 1.02x faster                                                            |
| sqlglot_transpile       | 1.75 ms                                                                | 1.72 ms: 1.02x faster                                                            |
| sqlglot_parse           | 1.46 ms                                                                | 1.44 ms: 1.01x faster                                                            |
| pickle                  | 10.4 us                                                                | 10.2 us: 1.01x faster                                                            |
| deepcopy                | 339 us                                                                 | 335 us: 1.01x faster                                                             |
| dask                    | 516 ms                                                                 | 509 ms: 1.01x faster                                                             |
| xml_etree_parse         | 150 ms                                                                 | 148 ms: 1.01x faster                                                             |
| xml_etree_process       | 55.9 ms                                                                | 55.2 ms: 1.01x faster                                                            |
| xml_etree_generate      | 81.9 ms                                                                | 81.0 ms: 1.01x faster                                                            |
| sympy_expand            | 468 ms                                                                 | 462 ms: 1.01x faster                                                             |
| genshi_text             | 21.7 ms                                                                | 21.5 ms: 1.01x faster                                                            |
| pprint_safe_repr        | 691 ms                                                                 | 683 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 68.6 ms                                                                | 67.8 ms: 1.01x faster                                                            |
| aiohttp                 | 1.02 ms                                                                | 1.01 ms: 1.01x faster                                                            |
| chameleon               | 6.49 ms                                                                | 6.42 ms: 1.01x faster                                                            |
| sympy_integrate         | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                            |
| sympy_str               | 288 ms                                                                 | 285 ms: 1.01x faster                                                             |
| sqlglot_optimize        | 51.3 ms                                                                | 50.8 ms: 1.01x faster                                                            |
| go                      | 138 ms                                                                 | 137 ms: 1.01x faster                                                             |
| json                    | 4.68 ms                                                                | 4.64 ms: 1.01x faster                                                            |
| docutils                | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                           |
| pprint_pformat          | 1.41 sec                                                               | 1.39 sec: 1.01x faster                                                           |
| pathlib                 | 17.9 ms                                                                | 17.8 ms: 1.01x faster                                                            |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                             |
| mako                    | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                            |
| raytrace                | 289 ms                                                                 | 287 ms: 1.01x faster                                                             |
| python_startup_no_site  | 6.58 ms                                                                | 6.54 ms: 1.01x faster                                                            |
| dulwich_log             | 64.2 ms                                                                | 63.8 ms: 1.01x faster                                                            |
| python_startup          | 9.07 ms                                                                | 9.02 ms: 1.01x faster                                                            |
| regex_v8                | 21.9 ms                                                                | 21.8 ms: 1.01x faster                                                            |
| 2to3                    | 253 ms                                                                 | 252 ms: 1.00x faster                                                             |
| sympy_sum               | 169 ms                                                                 | 168 ms: 1.00x faster                                                             |
| bench_thread_pool       | 796 us                                                                 | 793 us: 1.00x faster                                                             |
| richards                | 43.8 ms                                                                | 44.0 ms: 1.00x slower                                                            |
| django_template         | 33.3 ms                                                                | 33.5 ms: 1.01x slower                                                            |
| asyncio_tcp             | 512 ms                                                                 | 515 ms: 1.01x slower                                                             |
| logging_format          | 6.37 us                                                                | 6.41 us: 1.01x slower                                                            |
| hexiom                  | 6.23 ms                                                                | 6.27 ms: 1.01x slower                                                            |
| pyflate                 | 406 ms                                                                 | 409 ms: 1.01x slower                                                             |
| json_loads              | 24.3 us                                                                | 24.4 us: 1.01x slower                                                            |
| logging_silent          | 95.4 ns                                                                | 96.1 ns: 1.01x slower                                                            |
| async_generators        | 409 ms                                                                 | 413 ms: 1.01x slower                                                             |
| async_tree_io           | 1.29 sec                                                               | 1.30 sec: 1.01x slower                                                           |
| sqlite_synth            | 2.61 us                                                                | 2.65 us: 1.01x slower                                                            |
| thrift                  | 784 us                                                                 | 796 us: 1.02x slower                                                             |
| unpickle_list           | 4.96 us                                                                | 5.05 us: 1.02x slower                                                            |
| djangocms               | 32.3 us                                                                | 32.9 us: 1.02x slower                                                            |
| spectral_norm           | 95.9 ms                                                                | 97.8 ms: 1.02x slower                                                            |
| fannkuch                | 364 ms                                                                 | 371 ms: 1.02x slower                                                             |
| scimark_sparse_mat_mult | 4.45 ms                                                                | 4.68 ms: 1.05x slower                                                            |
| nbody                   | 88.8 ms                                                                | 95.6 ms: 1.08x slower                                                            |
| gc_traversal            | 3.61 ms                                                                | 3.93 ms: 1.09x slower                                                            |
| mdp                     | 2.40 sec                                                               | 2.63 sec: 1.10x slower                                                           |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (26): html5lib, scimark_lu, sqlalchemy_declarative, deepcopy_reduce, nqueens, unpack_sequence, xml_etree_iterparse, deepcopy_memo, gunicorn, tornado_http, pidigits, sqlalchemy_imperative, mypy2, regex_compile, pickle_pure_python, bench_mp_pool, json_dumps, create_gc_cycles, crypto_pyaes, async_tree_cpu_io_mixed, logging_simple, async_tree_none, async_tree_memoization, meteor_contest, float, unpickle
