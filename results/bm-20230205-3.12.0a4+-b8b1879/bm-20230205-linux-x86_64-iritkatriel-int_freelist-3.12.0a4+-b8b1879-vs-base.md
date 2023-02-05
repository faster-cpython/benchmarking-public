
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b8b1879
- commit date: 2023-02-05
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| docutils       | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 190 ms: 1.00x slower                                                |
| float          | 72.3 ms                                                                | 72.9 ms: 1.01x slower                                               |
| nbody          | 94.2 ms                                                                | 99.5 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                |
| regex_v8       | 21.1 ms                                                                | 22.4 ms: 1.06x slower                                               |
| regex_dna      | 200 ms                                                                 | 214 ms: 1.07x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.62 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict         | 32.2 us                                                                | 30.1 us: 1.07x faster                                               |
| pickle_list         | 4.26 us                                                                | 4.00 us: 1.07x faster                                               |
| xml_etree_iterparse | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| unpickle_list       | 5.04 us                                                                | 4.84 us: 1.04x faster                                               |
| pickle              | 10.3 us                                                                | 9.98 us: 1.04x faster                                               |
| json_loads          | 24.3 us                                                                | 23.5 us: 1.03x faster                                               |
| xml_etree_process   | 53.4 ms                                                                | 53.7 ms: 1.01x slower                                               |
| xml_etree_generate  | 77.3 ms                                                                | 78.1 ms: 1.01x slower                                               |
| json_dumps          | 9.37 ms                                                                | 9.51 ms: 1.01x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (4): unpickle, pickle_pure_python, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.94 ms                                                                | 8.92 ms: 1.00x faster                                               |
| python_startup_no_site | 6.48 ms                                                                | 6.46 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.77 ms                                                                | 9.62 ms: 1.02x faster                                               |
| django_template | 32.9 ms                                                                | 32.5 ms: 1.01x faster                                               |
| genshi_xml      | 46.7 ms                                                                | 47.7 ms: 1.02x slower                                               |
| genshi_text     | 20.7 ms                                                                | 21.2 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict             | 32.2 us                                                                | 30.1 us: 1.07x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.00 us: 1.07x faster                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 3.92 ms: 1.04x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| unpickle_list           | 5.04 us                                                                | 4.84 us: 1.04x faster                                               |
| coroutines              | 25.8 ms                                                                | 24.9 ms: 1.04x faster                                               |
| mdp                     | 2.58 sec                                                               | 2.49 sec: 1.04x faster                                              |
| pickle                  | 10.3 us                                                                | 9.98 us: 1.04x faster                                               |
| richards                | 43.9 ms                                                                | 42.4 ms: 1.04x faster                                               |
| spectral_norm           | 98.3 ms                                                                | 95.0 ms: 1.03x faster                                               |
| json_loads              | 24.3 us                                                                | 23.5 us: 1.03x faster                                               |
| chaos                   | 64.7 ms                                                                | 63.2 ms: 1.02x faster                                               |
| scimark_sor             | 107 ms                                                                 | 105 ms: 1.02x faster                                                |
| json                    | 4.63 ms                                                                | 4.55 ms: 1.02x faster                                               |
| mako                    | 9.77 ms                                                                | 9.62 ms: 1.02x faster                                               |
| go                      | 135 ms                                                                 | 133 ms: 1.01x faster                                                |
| django_template         | 32.9 ms                                                                | 32.5 ms: 1.01x faster                                               |
| sqlite_synth            | 2.57 us                                                                | 2.55 us: 1.01x faster                                               |
| async_generators        | 353 ms                                                                 | 349 ms: 1.01x faster                                                |
| regex_compile           | 130 ms                                                                 | 129 ms: 1.01x faster                                                |
| dulwich_log             | 62.8 ms                                                                | 62.4 ms: 1.01x faster                                               |
| aiohttp                 | 1.00 ms                                                                | 999 us: 1.01x faster                                                |
| unpack_sequence         | 43.4 ns                                                                | 43.2 ns: 1.01x faster                                               |
| python_startup          | 8.94 ms                                                                | 8.92 ms: 1.00x faster                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.46 ms: 1.00x faster                                               |
| docutils                | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                              |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| pidigits                | 189 ms                                                                 | 190 ms: 1.00x slower                                                |
| hexiom                  | 5.95 ms                                                                | 5.98 ms: 1.01x slower                                               |
| logging_simple          | 5.73 us                                                                | 5.76 us: 1.01x slower                                               |
| xml_etree_process       | 53.4 ms                                                                | 53.7 ms: 1.01x slower                                               |
| raytrace                | 284 ms                                                                 | 287 ms: 1.01x slower                                                |
| float                   | 72.3 ms                                                                | 72.9 ms: 1.01x slower                                               |
| deltablue               | 3.18 ms                                                                | 3.21 ms: 1.01x slower                                               |
| pprint_safe_repr        | 679 ms                                                                 | 686 ms: 1.01x slower                                                |
| xml_etree_generate      | 77.3 ms                                                                | 78.1 ms: 1.01x slower                                               |
| pathlib                 | 17.9 ms                                                                | 18.0 ms: 1.01x slower                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.41 sec: 1.01x slower                                              |
| meteor_contest          | 103 ms                                                                 | 105 ms: 1.01x slower                                                |
| logging_format          | 6.29 us                                                                | 6.38 us: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                              |
| scimark_fft             | 304 ms                                                                 | 309 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 762 ms: 1.01x slower                                                |
| json_dumps              | 9.37 ms                                                                | 9.51 ms: 1.01x slower                                               |
| fannkuch                | 361 ms                                                                 | 367 ms: 1.02x slower                                                |
| deepcopy_reduce         | 2.96 us                                                                | 3.01 us: 1.02x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.7 ms: 1.02x slower                                               |
| nqueens                 | 75.4 ms                                                                | 77.0 ms: 1.02x slower                                               |
| deepcopy                | 328 us                                                                 | 336 us: 1.02x slower                                                |
| genshi_text             | 20.7 ms                                                                | 21.2 ms: 1.03x slower                                               |
| crypto_pyaes            | 73.3 ms                                                                | 75.2 ms: 1.03x slower                                               |
| scimark_lu              | 106 ms                                                                 | 109 ms: 1.03x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 34.7 us: 1.03x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 3.76 ms: 1.03x slower                                               |
| scimark_monte_carlo     | 65.4 ms                                                                | 67.7 ms: 1.04x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.13 sec: 1.04x slower                                              |
| nbody                   | 94.2 ms                                                                | 99.5 ms: 1.06x slower                                               |
| regex_v8                | 21.1 ms                                                                | 22.4 ms: 1.06x slower                                               |
| regex_dna               | 200 ms                                                                 | 214 ms: 1.07x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.62 ms: 1.08x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (31): html5lib, dask, logging_silent, gunicorn, generators, unpickle, coverage, mypy, sympy_expand, chameleon, bench_mp_pool, sqlglot_optimize, thrift, create_gc_cycles, sympy_integrate, sqlglot_normalize, bench_thread_pool, asyncio_tcp, sympy_str, sympy_sum, djangocms, tornado_http, pickle_pure_python, sqlglot_parse, sqlglot_transpile, telco, unpickle_pure_python, pyflate, xml_etree_parse, async_tree_none, async_tree_memoization
