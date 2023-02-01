
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 253 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (4): chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                                | 95.5 ms: 1.02x slower                                               |
| pidigits       | 192 ms                                                                 | 199 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_v8       | 21.6 ms                                                                | 21.7 ms: 1.01x slower                                               |
| regex_dna      | 202 ms                                                                 | 209 ms: 1.03x slower                                                |
| regex_effbot   | 3.39 ms                                                                | 3.63 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse | 105 ms                                                                 | 103 ms: 1.03x faster                                                |
| pickle_pure_python  | 282 us                                                                 | 287 us: 1.02x slower                                                |
| json_loads          | 23.7 us                                                                | 24.2 us: 1.02x slower                                               |
| pickle_dict         | 30.5 us                                                                | 31.2 us: 1.02x slower                                               |
| json_dumps          | 9.34 ms                                                                | 9.58 ms: 1.03x slower                                               |
| pickle_list         | 3.96 us                                                                | 4.24 us: 1.07x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (7): pickle, unpickle_list, xml_etree_process, xml_etree_generate, unpickle_pure_python, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.44 ms                                                                | 6.49 ms: 1.01x slower                                               |
| python_startup         | 8.89 ms                                                                | 8.98 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.8 ms                                                                | 33.1 ms: 1.01x slower                                               |
| mako            | 9.75 ms                                                                | 9.87 ms: 1.01x slower                                               |
| genshi_xml      | 46.7 ms                                                                | 47.6 ms: 1.02x slower                                               |
| genshi_text     | 20.3 ms                                                                | 21.0 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| richards                | 42.9 ms                                                                | 41.6 ms: 1.03x faster                                               |
| coverage                | 99.0 ms                                                                | 96.0 ms: 1.03x faster                                               |
| fannkuch                | 369 ms                                                                 | 358 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult | 4.13 ms                                                                | 4.02 ms: 1.03x faster                                               |
| chaos                   | 65.6 ms                                                                | 63.9 ms: 1.03x faster                                               |
| pyflate                 | 406 ms                                                                 | 396 ms: 1.03x faster                                                |
| xml_etree_iterparse     | 105 ms                                                                 | 103 ms: 1.03x faster                                                |
| scimark_lu              | 108 ms                                                                 | 106 ms: 1.02x faster                                                |
| logging_simple          | 5.78 us                                                                | 5.68 us: 1.02x faster                                               |
| deepcopy_reduce         | 2.98 us                                                                | 2.94 us: 1.02x faster                                               |
| pprint_safe_repr        | 677 ms                                                                 | 669 ms: 1.01x faster                                                |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.01x faster                                                |
| logging_format          | 6.35 us                                                                | 6.30 us: 1.01x faster                                               |
| deltablue               | 3.22 ms                                                                | 3.20 ms: 1.01x faster                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| go                      | 135 ms                                                                 | 134 ms: 1.01x faster                                                |
| sympy_integrate         | 19.7 ms                                                                | 19.8 ms: 1.00x slower                                               |
| aiohttp                 | 992 us                                                                 | 997 us: 1.01x slower                                                |
| sqlglot_transpile       | 1.70 ms                                                                | 1.71 ms: 1.01x slower                                               |
| async_generators        | 351 ms                                                                 | 353 ms: 1.01x slower                                                |
| dulwich_log             | 62.4 ms                                                                | 62.8 ms: 1.01x slower                                               |
| sympy_expand            | 451 ms                                                                 | 453 ms: 1.01x slower                                                |
| regex_v8                | 21.6 ms                                                                | 21.7 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                               |
| thrift                  | 737 us                                                                 | 742 us: 1.01x slower                                                |
| asyncio_tcp             | 490 ms                                                                 | 494 ms: 1.01x slower                                                |
| sympy_sum               | 154 ms                                                                 | 156 ms: 1.01x slower                                                |
| gunicorn                | 1.06 ms                                                                | 1.07 ms: 1.01x slower                                               |
| python_startup_no_site  | 6.44 ms                                                                | 6.49 ms: 1.01x slower                                               |
| sqlglot_optimize        | 50.7 ms                                                                | 51.2 ms: 1.01x slower                                               |
| django_template         | 32.8 ms                                                                | 33.1 ms: 1.01x slower                                               |
| deepcopy_memo           | 34.3 us                                                                | 34.6 us: 1.01x slower                                               |
| sqlglot_normalize       | 105 ms                                                                 | 105 ms: 1.01x slower                                                |
| python_startup          | 8.89 ms                                                                | 8.98 ms: 1.01x slower                                               |
| mako                    | 9.75 ms                                                                | 9.87 ms: 1.01x slower                                               |
| unpack_sequence         | 42.7 ns                                                                | 43.3 ns: 1.01x slower                                               |
| json                    | 4.61 ms                                                                | 4.67 ms: 1.01x slower                                               |
| 2to3                    | 250 ms                                                                 | 253 ms: 1.01x slower                                                |
| scimark_fft             | 306 ms                                                                 | 311 ms: 1.01x slower                                                |
| bench_thread_pool       | 778 us                                                                 | 790 us: 1.02x slower                                                |
| pathlib                 | 17.6 ms                                                                | 17.8 ms: 1.02x slower                                               |
| async_tree_io           | 1.29 sec                                                               | 1.31 sec: 1.02x slower                                              |
| genshi_xml              | 46.7 ms                                                                | 47.6 ms: 1.02x slower                                               |
| logging_silent          | 90.4 ns                                                                | 92.2 ns: 1.02x slower                                               |
| scimark_monte_carlo     | 65.3 ms                                                                | 66.7 ms: 1.02x slower                                               |
| pickle_pure_python      | 282 us                                                                 | 287 us: 1.02x slower                                                |
| generators              | 76.4 ms                                                                | 78.0 ms: 1.02x slower                                               |
| json_loads              | 23.7 us                                                                | 24.2 us: 1.02x slower                                               |
| raytrace                | 283 ms                                                                 | 289 ms: 1.02x slower                                                |
| meteor_contest          | 105 ms                                                                 | 107 ms: 1.02x slower                                                |
| sqlite_synth            | 2.55 us                                                                | 2.60 us: 1.02x slower                                               |
| nbody                   | 93.3 ms                                                                | 95.5 ms: 1.02x slower                                               |
| pickle_dict             | 30.5 us                                                                | 31.2 us: 1.02x slower                                               |
| pycparser               | 1.09 sec                                                               | 1.12 sec: 1.02x slower                                              |
| json_dumps              | 9.34 ms                                                                | 9.58 ms: 1.03x slower                                               |
| regex_dna               | 202 ms                                                                 | 209 ms: 1.03x slower                                                |
| pidigits                | 192 ms                                                                 | 199 ms: 1.03x slower                                                |
| genshi_text             | 20.3 ms                                                                | 21.0 ms: 1.03x slower                                               |
| nqueens                 | 76.9 ms                                                                | 79.5 ms: 1.03x slower                                               |
| scimark_sor             | 107 ms                                                                 | 111 ms: 1.03x slower                                                |
| crypto_pyaes            | 73.2 ms                                                                | 76.0 ms: 1.04x slower                                               |
| async_tree_memoization  | 628 ms                                                                 | 658 ms: 1.05x slower                                                |
| regex_effbot            | 3.39 ms                                                                | 3.63 ms: 1.07x slower                                               |
| pickle_list             | 3.96 us                                                                | 4.24 us: 1.07x slower                                               |
| mdp                     | 2.44 sec                                                               | 2.62 sec: 1.07x slower                                              |
| spectral_norm           | 97.0 ms                                                                | 105 ms: 1.08x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (25): djangocms, pickle, deepcopy, unpickle_list, hexiom, coroutines, float, sqlglot_parse, gc_traversal, chameleon, xml_etree_process, xml_etree_generate, unpickle_pure_python, bench_mp_pool, xml_etree_parse, unpickle, docutils, tornado_http, async_tree_cpu_io_mixed, sympy_str, telco, dask, html5lib, async_tree_none, mypy
