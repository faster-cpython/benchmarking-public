
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1d81198
- commit date: 2023-02-03
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| chameleon      | 6.35 ms                                                                | 6.28 ms: 1.01x faster                                               |
| docutils       | 2.50 sec                                                               | 2.51 sec: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 191 ms: 1.01x slower                                                |
| float          | 72.3 ms                                                                | 73.2 ms: 1.01x slower                                               |
| nbody          | 94.2 ms                                                                | 95.8 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_dna      | 200 ms                                                                 | 209 ms: 1.04x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.51 ms: 1.05x slower                                               |
| regex_v8       | 21.1 ms                                                                | 22.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict         | 32.2 us                                                                | 31.3 us: 1.03x faster                                               |
| xml_etree_iterparse | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| pickle              | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| unpickle            | 13.2 us                                                                | 12.9 us: 1.02x faster                                               |
| json_loads          | 24.3 us                                                                | 23.9 us: 1.01x faster                                               |
| pickle_list         | 4.26 us                                                                | 4.23 us: 1.01x faster                                               |
| xml_etree_parse     | 147 ms                                                                 | 146 ms: 1.01x faster                                                |
| json_dumps          | 9.37 ms                                                                | 9.43 ms: 1.01x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (5): pickle_pure_python, unpickle_pure_python, xml_etree_process, xml_etree_generate, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.47 ms: 1.00x faster                                               |
| python_startup         | 8.94 ms                                                                | 8.93 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.9 ms                                                                | 32.3 ms: 1.02x faster                                               |
| mako            | 9.77 ms                                                                | 9.60 ms: 1.02x faster                                               |
| genshi_text     | 20.7 ms                                                                | 20.3 ms: 1.02x faster                                               |
| genshi_xml      | 46.7 ms                                                                | 47.3 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines              | 25.8 ms                                                                | 24.3 ms: 1.06x faster                                               |
| richards                | 43.9 ms                                                                | 42.0 ms: 1.04x faster                                               |
| pickle_dict             | 32.2 us                                                                | 31.3 us: 1.03x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| coverage                | 99.1 ms                                                                | 96.4 ms: 1.03x faster                                               |
| pickle                  | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.06 ms: 1.02x faster                                               |
| unpickle                | 13.2 us                                                                | 12.9 us: 1.02x faster                                               |
| django_template         | 32.9 ms                                                                | 32.3 ms: 1.02x faster                                               |
| mako                    | 9.77 ms                                                                | 9.60 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.02 ms: 1.02x faster                                               |
| genshi_text             | 20.7 ms                                                                | 20.3 ms: 1.02x faster                                               |
| chaos                   | 64.7 ms                                                                | 63.7 ms: 1.02x faster                                               |
| dask                    | 501 ms                                                                 | 494 ms: 1.01x faster                                                |
| logging_silent          | 93.3 ns                                                                | 91.9 ns: 1.01x faster                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.01x faster                                              |
| json_loads              | 24.3 us                                                                | 23.9 us: 1.01x faster                                               |
| chameleon               | 6.35 ms                                                                | 6.28 ms: 1.01x faster                                               |
| aiohttp                 | 1.00 ms                                                                | 993 us: 1.01x faster                                                |
| pprint_safe_repr        | 679 ms                                                                 | 671 ms: 1.01x faster                                                |
| sqlite_synth            | 2.57 us                                                                | 2.54 us: 1.01x faster                                               |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| dulwich_log             | 62.8 ms                                                                | 62.3 ms: 1.01x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.23 us: 1.01x faster                                               |
| pathlib                 | 17.9 ms                                                                | 17.8 ms: 1.01x faster                                               |
| xml_etree_parse         | 147 ms                                                                 | 146 ms: 1.01x faster                                                |
| sympy_sum               | 156 ms                                                                 | 155 ms: 1.00x faster                                                |
| mdp                     | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                              |
| python_startup_no_site  | 6.48 ms                                                                | 6.47 ms: 1.00x faster                                               |
| python_startup          | 8.94 ms                                                                | 8.93 ms: 1.00x faster                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.45 ms: 1.00x slower                                               |
| bench_thread_pool       | 780 us                                                                 | 782 us: 1.00x slower                                                |
| docutils                | 2.50 sec                                                               | 2.51 sec: 1.00x slower                                              |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| json_dumps              | 9.37 ms                                                                | 9.43 ms: 1.01x slower                                               |
| deepcopy                | 328 us                                                                 | 330 us: 1.01x slower                                                |
| thrift                  | 742 us                                                                 | 747 us: 1.01x slower                                                |
| asyncio_tcp             | 493 ms                                                                 | 496 ms: 1.01x slower                                                |
| pidigits                | 189 ms                                                                 | 191 ms: 1.01x slower                                                |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| sqlglot_normalize       | 106 ms                                                                 | 106 ms: 1.01x slower                                                |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                              |
| float                   | 72.3 ms                                                                | 73.2 ms: 1.01x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.3 ms: 1.01x slower                                               |
| scimark_fft             | 304 ms                                                                 | 308 ms: 1.01x slower                                                |
| unpack_sequence         | 43.4 ns                                                                | 43.9 ns: 1.01x slower                                               |
| deltablue               | 3.18 ms                                                                | 3.22 ms: 1.01x slower                                               |
| scimark_lu              | 106 ms                                                                 | 108 ms: 1.01x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 34.2 us: 1.02x slower                                               |
| raytrace                | 284 ms                                                                 | 289 ms: 1.02x slower                                                |
| nbody                   | 94.2 ms                                                                | 95.8 ms: 1.02x slower                                               |
| fannkuch                | 361 ms                                                                 | 369 ms: 1.02x slower                                                |
| scimark_monte_carlo     | 65.4 ms                                                                | 66.8 ms: 1.02x slower                                               |
| json                    | 4.63 ms                                                                | 4.76 ms: 1.03x slower                                               |
| crypto_pyaes            | 73.3 ms                                                                | 76.0 ms: 1.04x slower                                               |
| pyflate                 | 400 ms                                                                 | 416 ms: 1.04x slower                                                |
| regex_dna               | 200 ms                                                                 | 209 ms: 1.04x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.51 ms: 1.05x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.13 sec: 1.05x slower                                              |
| regex_v8                | 21.1 ms                                                                | 22.5 ms: 1.07x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 4.05 ms: 1.11x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (30): html5lib, async_tree_memoization, telco, tornado_http, scimark_sor, sympy_str, sqlglot_parse, pickle_pure_python, go, unpickle_pure_python, sympy_expand, sqlglot_transpile, spectral_norm, djangocms, bench_mp_pool, async_tree_none, mypy, xml_etree_process, deepcopy_reduce, xml_etree_generate, sympy_integrate, sqlglot_optimize, hexiom, logging_simple, generators, async_generators, async_tree_cpu_io_mixed, unpickle_list, logging_format, nqueens
