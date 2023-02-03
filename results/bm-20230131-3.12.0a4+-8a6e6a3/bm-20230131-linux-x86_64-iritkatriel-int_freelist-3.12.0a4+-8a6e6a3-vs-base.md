
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| docutils       | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                              |
| tornado_http   | 94.1 ms                                                                | 95.3 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 192 ms: 1.01x slower                                                |
| float          | 72.3 ms                                                                | 73.8 ms: 1.02x slower                                               |
| nbody          | 94.2 ms                                                                | 96.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 127 ms: 1.02x faster                                                |
| regex_v8       | 21.1 ms                                                                | 21.2 ms: 1.01x slower                                               |
| regex_effbot   | 3.36 ms                                                                | 3.47 ms: 1.03x slower                                               |
| regex_dna      | 200 ms                                                                 | 208 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| unpickle_list       | 5.04 us                                                                | 4.93 us: 1.02x faster                                               |
| pickle              | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| pickle_dict         | 32.2 us                                                                | 31.8 us: 1.01x faster                                               |
| pickle_list         | 4.26 us                                                                | 4.23 us: 1.01x faster                                               |
| xml_etree_process   | 53.4 ms                                                                | 53.6 ms: 1.01x slower                                               |
| json_dumps          | 9.37 ms                                                                | 9.50 ms: 1.01x slower                                               |
| json_loads          | 24.3 us                                                                | 24.7 us: 1.02x slower                                               |
| unpickle            | 13.2 us                                                                | 14.0 us: 1.06x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                               |
| python_startup         | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.9 ms                                                                | 33.1 ms: 1.01x slower                                               |
| genshi_xml      | 46.7 ms                                                                | 47.4 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse     | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| coverage                | 99.1 ms                                                                | 96.1 ms: 1.03x faster                                               |
| regex_compile           | 130 ms                                                                 | 127 ms: 1.02x faster                                                |
| unpickle_list           | 5.04 us                                                                | 4.93 us: 1.02x faster                                               |
| pickle                  | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| coroutines              | 25.8 ms                                                                | 25.3 ms: 1.02x faster                                               |
| mdp                     | 2.58 sec                                                               | 2.53 sec: 1.02x faster                                              |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.02x faster                                              |
| unpack_sequence         | 43.4 ns                                                                | 42.7 ns: 1.02x faster                                               |
| pprint_safe_repr        | 679 ms                                                                 | 669 ms: 1.02x faster                                                |
| pickle_dict             | 32.2 us                                                                | 31.8 us: 1.01x faster                                               |
| sqlglot_normalize       | 106 ms                                                                 | 104 ms: 1.01x faster                                                |
| sqlglot_optimize        | 51.3 ms                                                                | 50.8 ms: 1.01x faster                                               |
| go                      | 135 ms                                                                 | 134 ms: 1.01x faster                                                |
| sympy_integrate         | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.23 us: 1.01x faster                                               |
| chaos                   | 64.7 ms                                                                | 64.4 ms: 1.01x faster                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                               |
| docutils                | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                              |
| python_startup          | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                               |
| hexiom                  | 5.95 ms                                                                | 5.98 ms: 1.00x slower                                               |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| xml_etree_process       | 53.4 ms                                                                | 53.6 ms: 1.01x slower                                               |
| regex_v8                | 21.1 ms                                                                | 21.2 ms: 1.01x slower                                               |
| django_template         | 32.9 ms                                                                | 33.1 ms: 1.01x slower                                               |
| logging_format          | 6.29 us                                                                | 6.35 us: 1.01x slower                                               |
| deepcopy                | 328 us                                                                 | 331 us: 1.01x slower                                                |
| asyncio_tcp             | 493 ms                                                                 | 498 ms: 1.01x slower                                                |
| pidigits                | 189 ms                                                                 | 192 ms: 1.01x slower                                                |
| nqueens                 | 75.4 ms                                                                | 76.2 ms: 1.01x slower                                               |
| logging_simple          | 5.73 us                                                                | 5.79 us: 1.01x slower                                               |
| thrift                  | 742 us                                                                 | 751 us: 1.01x slower                                                |
| tornado_http            | 94.1 ms                                                                | 95.3 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 761 ms: 1.01x slower                                                |
| json                    | 4.63 ms                                                                | 4.69 ms: 1.01x slower                                               |
| json_dumps              | 9.37 ms                                                                | 9.50 ms: 1.01x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.4 ms: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                              |
| scimark_monte_carlo     | 65.4 ms                                                                | 66.4 ms: 1.02x slower                                               |
| json_loads              | 24.3 us                                                                | 24.7 us: 1.02x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.48 ms: 1.02x slower                                               |
| deltablue               | 3.18 ms                                                                | 3.25 ms: 1.02x slower                                               |
| float                   | 72.3 ms                                                                | 73.8 ms: 1.02x slower                                               |
| deepcopy_reduce         | 2.96 us                                                                | 3.02 us: 1.02x slower                                               |
| raytrace                | 284 ms                                                                 | 291 ms: 1.02x slower                                                |
| nbody                   | 94.2 ms                                                                | 96.3 ms: 1.02x slower                                               |
| dulwich_log             | 62.8 ms                                                                | 64.4 ms: 1.03x slower                                               |
| bench_thread_pool       | 780 us                                                                 | 801 us: 1.03x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.47 ms: 1.03x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.12 sec: 1.03x slower                                              |
| regex_dna               | 200 ms                                                                 | 208 ms: 1.04x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 34.9 us: 1.04x slower                                               |
| sqlite_synth            | 2.57 us                                                                | 2.68 us: 1.04x slower                                               |
| async_generators        | 353 ms                                                                 | 369 ms: 1.04x slower                                                |
| gc_traversal            | 3.64 ms                                                                | 3.81 ms: 1.05x slower                                               |
| dask                    | 501 ms                                                                 | 525 ms: 1.05x slower                                                |
| sqlglot_transpile       | 1.70 ms                                                                | 1.78 ms: 1.05x slower                                               |
| sqlglot_parse           | 1.40 ms                                                                | 1.48 ms: 1.05x slower                                               |
| pathlib                 | 17.9 ms                                                                | 18.9 ms: 1.06x slower                                               |
| unpickle                | 13.2 us                                                                | 14.0 us: 1.06x slower                                               |
| generators              | 77.0 ms                                                                | 83.5 ms: 1.08x slower                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.55 ms: 1.11x slower                                               |
| scimark_sor             | 107 ms                                                                 | 123 ms: 1.15x slower                                                |
| pyflate                 | 400 ms                                                                 | 461 ms: 1.15x slower                                                |
| crypto_pyaes            | 73.3 ms                                                                | 90.0 ms: 1.23x slower                                               |
| scimark_fft             | 304 ms                                                                 | 390 ms: 1.28x slower                                                |
| spectral_norm           | 98.3 ms                                                                | 138 ms: 1.40x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (24): richards, logging_silent, fannkuch, gunicorn, mypy, sympy_str, sympy_sum, genshi_text, xml_etree_parse, bench_mp_pool, djangocms, aiohttp, pickle_pure_python, xml_etree_generate, chameleon, unpickle_pure_python, sympy_expand, mako, telco, scimark_lu, meteor_contest, async_tree_none, async_tree_memoization, html5lib
