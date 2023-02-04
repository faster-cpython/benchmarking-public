
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| chameleon      | 6.35 ms                                                                | 6.26 ms: 1.02x faster                                               |
| html5lib       | 60.8 ms                                                                | 59.6 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 191 ms: 1.01x slower                                                |
| nbody          | 94.2 ms                                                                | 96.5 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_dna      | 200 ms                                                                 | 207 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.48 ms: 1.04x slower                                               |
| regex_v8       | 21.1 ms                                                                | 22.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict         | 32.2 us                                                                | 30.4 us: 1.06x faster                                               |
| xml_etree_iterparse | 106 ms                                                                 | 101 ms: 1.05x faster                                                |
| pickle_list         | 4.26 us                                                                | 4.08 us: 1.05x faster                                               |
| unpickle            | 13.2 us                                                                | 12.7 us: 1.04x faster                                               |
| json_loads          | 24.3 us                                                                | 23.4 us: 1.03x faster                                               |
| pickle              | 10.3 us                                                                | 10.0 us: 1.03x faster                                               |
| pickle_pure_python  | 286 us                                                                 | 281 us: 1.02x faster                                                |
| unpickle_list       | 5.04 us                                                                | 4.96 us: 1.02x faster                                               |
| json_dumps          | 9.37 ms                                                                | 9.27 ms: 1.01x faster                                               |
| xml_etree_generate  | 77.3 ms                                                                | 77.7 ms: 1.00x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                               |
| python_startup_no_site | 6.48 ms                                                                | 6.50 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.77 ms                                                                | 9.48 ms: 1.03x faster                                               |
| django_template | 32.9 ms                                                                | 32.2 ms: 1.02x faster                                               |
| genshi_xml      | 46.7 ms                                                                | 47.3 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict             | 32.2 us                                                                | 30.4 us: 1.06x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 101 ms: 1.05x faster                                                |
| pickle_list             | 4.26 us                                                                | 4.08 us: 1.05x faster                                               |
| unpickle                | 13.2 us                                                                | 12.7 us: 1.04x faster                                               |
| json_loads              | 24.3 us                                                                | 23.4 us: 1.03x faster                                               |
| richards                | 43.9 ms                                                                | 42.5 ms: 1.03x faster                                               |
| coroutines              | 25.8 ms                                                                | 25.0 ms: 1.03x faster                                               |
| mako                    | 9.77 ms                                                                | 9.48 ms: 1.03x faster                                               |
| pickle                  | 10.3 us                                                                | 10.0 us: 1.03x faster                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 3.98 ms: 1.03x faster                                               |
| spectral_norm           | 98.3 ms                                                                | 95.7 ms: 1.03x faster                                               |
| coverage                | 99.1 ms                                                                | 96.7 ms: 1.03x faster                                               |
| django_template         | 32.9 ms                                                                | 32.2 ms: 1.02x faster                                               |
| json                    | 4.63 ms                                                                | 4.54 ms: 1.02x faster                                               |
| html5lib                | 60.8 ms                                                                | 59.6 ms: 1.02x faster                                               |
| logging_silent          | 93.3 ns                                                                | 91.5 ns: 1.02x faster                                               |
| dask                    | 501 ms                                                                 | 492 ms: 1.02x faster                                                |
| pathlib                 | 17.9 ms                                                                | 17.6 ms: 1.02x faster                                               |
| pickle_pure_python      | 286 us                                                                 | 281 us: 1.02x faster                                                |
| scimark_sor             | 107 ms                                                                 | 105 ms: 1.02x faster                                                |
| aiohttp                 | 1.00 ms                                                                | 989 us: 1.02x faster                                                |
| chameleon               | 6.35 ms                                                                | 6.26 ms: 1.02x faster                                               |
| unpickle_list           | 5.04 us                                                                | 4.96 us: 1.02x faster                                               |
| gc_traversal            | 3.64 ms                                                                | 3.58 ms: 1.01x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| sqlite_synth            | 2.57 us                                                                | 2.54 us: 1.01x faster                                               |
| asyncio_tcp             | 493 ms                                                                 | 486 ms: 1.01x faster                                                |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| unpack_sequence         | 43.4 ns                                                                | 42.9 ns: 1.01x faster                                               |
| json_dumps              | 9.37 ms                                                                | 9.27 ms: 1.01x faster                                               |
| sympy_str               | 272 ms                                                                 | 269 ms: 1.01x faster                                                |
| thrift                  | 742 us                                                                 | 736 us: 1.01x faster                                                |
| logging_simple          | 5.73 us                                                                | 5.68 us: 1.01x faster                                               |
| logging_format          | 6.29 us                                                                | 6.24 us: 1.01x faster                                               |
| chaos                   | 64.7 ms                                                                | 64.2 ms: 1.01x faster                                               |
| go                      | 135 ms                                                                 | 134 ms: 1.01x faster                                                |
| pprint_safe_repr        | 679 ms                                                                 | 674 ms: 1.01x faster                                                |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| generators              | 77.0 ms                                                                | 76.5 ms: 1.01x faster                                               |
| pyflate                 | 400 ms                                                                 | 398 ms: 1.01x faster                                                |
| dulwich_log             | 62.8 ms                                                                | 62.6 ms: 1.00x faster                                               |
| sqlglot_optimize        | 51.3 ms                                                                | 51.2 ms: 1.00x faster                                               |
| bench_thread_pool       | 780 us                                                                 | 779 us: 1.00x faster                                                |
| python_startup          | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.50 ms: 1.00x slower                                               |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| xml_etree_generate      | 77.3 ms                                                                | 77.7 ms: 1.00x slower                                               |
| deepcopy_reduce         | 2.96 us                                                                | 2.97 us: 1.01x slower                                               |
| pidigits                | 189 ms                                                                 | 191 ms: 1.01x slower                                                |
| mdp                     | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 759 ms: 1.01x slower                                                |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                              |
| async_generators        | 353 ms                                                                 | 357 ms: 1.01x slower                                                |
| hexiom                  | 5.95 ms                                                                | 6.02 ms: 1.01x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.3 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.47 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 65.4 ms                                                                | 66.5 ms: 1.02x slower                                               |
| deepcopy                | 328 us                                                                 | 335 us: 1.02x slower                                                |
| telco                   | 6.40 ms                                                                | 6.54 ms: 1.02x slower                                               |
| nbody                   | 94.2 ms                                                                | 96.5 ms: 1.02x slower                                               |
| fannkuch                | 361 ms                                                                 | 371 ms: 1.03x slower                                                |
| regex_dna               | 200 ms                                                                 | 207 ms: 1.03x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 34.7 us: 1.03x slower                                               |
| regex_effbot            | 3.36 ms                                                                | 3.48 ms: 1.04x slower                                               |
| nqueens                 | 75.4 ms                                                                | 78.4 ms: 1.04x slower                                               |
| crypto_pyaes            | 73.3 ms                                                                | 76.6 ms: 1.04x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.13 sec: 1.05x slower                                              |
| regex_v8                | 21.1 ms                                                                | 22.5 ms: 1.07x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (23): scimark_fft, genshi_text, tornado_http, sympy_expand, mypy, xml_etree_process, raytrace, sympy_sum, unpickle_pure_python, bench_mp_pool, sympy_integrate, scimark_lu, float, docutils, sqlglot_normalize, deltablue, xml_etree_parse, djangocms, async_tree_memoization, sqlglot_transpile, meteor_contest, sqlglot_parse, async_tree_none
