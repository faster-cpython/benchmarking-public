
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| chameleon      | 6.35 ms                                                                | 6.21 ms: 1.02x faster                                               |
| docutils       | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                              |
| tornado_http   | 94.1 ms                                                                | 93.6 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 190 ms: 1.01x slower                                                |
| float          | 72.3 ms                                                                | 73.1 ms: 1.01x slower                                               |
| nbody          | 94.2 ms                                                                | 96.7 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                |
| regex_v8       | 21.1 ms                                                                | 22.2 ms: 1.05x slower                                               |
| regex_dna      | 200 ms                                                                 | 217 ms: 1.08x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.77 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse | 106 ms                                                                 | 102 ms: 1.05x faster                                                |
| json_loads          | 24.3 us                                                                | 23.4 us: 1.04x faster                                               |
| pickle              | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| pickle_dict         | 32.2 us                                                                | 31.8 us: 1.01x faster                                               |
| pickle_list         | 4.26 us                                                                | 4.22 us: 1.01x faster                                               |
| xml_etree_parse     | 147 ms                                                                 | 145 ms: 1.01x faster                                                |
| pickle_pure_python  | 286 us                                                                 | 284 us: 1.01x faster                                                |
| unpickle            | 13.2 us                                                                | 13.1 us: 1.01x faster                                               |
| xml_etree_generate  | 77.3 ms                                                                | 77.5 ms: 1.00x slower                                               |
| unpickle_list       | 5.04 us                                                                | 5.15 us: 1.02x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, json_dumps

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
| mako            | 9.77 ms                                                                | 9.47 ms: 1.03x faster                                               |
| django_template | 32.9 ms                                                                | 32.1 ms: 1.03x faster                                               |
| genshi_xml      | 46.7 ms                                                                | 47.5 ms: 1.02x slower                                               |
| genshi_text     | 20.7 ms                                                                | 21.3 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines              | 25.8 ms                                                                | 24.1 ms: 1.07x faster                                               |
| richards                | 43.9 ms                                                                | 41.9 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 102 ms: 1.05x faster                                                |
| coverage                | 99.1 ms                                                                | 94.8 ms: 1.05x faster                                               |
| json_loads              | 24.3 us                                                                | 23.4 us: 1.04x faster                                               |
| mako                    | 9.77 ms                                                                | 9.47 ms: 1.03x faster                                               |
| mdp                     | 2.58 sec                                                               | 2.51 sec: 1.03x faster                                              |
| django_template         | 32.9 ms                                                                | 32.1 ms: 1.03x faster                                               |
| chameleon               | 6.35 ms                                                                | 6.21 ms: 1.02x faster                                               |
| go                      | 135 ms                                                                 | 132 ms: 1.02x faster                                                |
| unpack_sequence         | 43.4 ns                                                                | 42.5 ns: 1.02x faster                                               |
| pickle                  | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| spectral_norm           | 98.3 ms                                                                | 96.6 ms: 1.02x faster                                               |
| chaos                   | 64.7 ms                                                                | 63.7 ms: 1.02x faster                                               |
| sqlite_synth            | 2.57 us                                                                | 2.54 us: 1.02x faster                                               |
| dask                    | 501 ms                                                                 | 494 ms: 1.01x faster                                                |
| pickle_dict             | 32.2 us                                                                | 31.8 us: 1.01x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.04 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.96 us                                                                | 2.92 us: 1.01x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.22 us: 1.01x faster                                               |
| logging_simple          | 5.73 us                                                                | 5.67 us: 1.01x faster                                               |
| aiohttp                 | 1.00 ms                                                                | 995 us: 1.01x faster                                                |
| xml_etree_parse         | 147 ms                                                                 | 145 ms: 1.01x faster                                                |
| pickle_pure_python      | 286 us                                                                 | 284 us: 1.01x faster                                                |
| pathlib                 | 17.9 ms                                                                | 17.7 ms: 1.01x faster                                               |
| sympy_expand            | 458 ms                                                                 | 455 ms: 1.01x faster                                                |
| deepcopy                | 328 us                                                                 | 326 us: 1.01x faster                                                |
| regex_compile           | 130 ms                                                                 | 129 ms: 1.01x faster                                                |
| dulwich_log             | 62.8 ms                                                                | 62.4 ms: 1.01x faster                                               |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.01x faster                                                |
| tornado_http            | 94.1 ms                                                                | 93.6 ms: 1.01x faster                                               |
| sqlglot_transpile       | 1.70 ms                                                                | 1.69 ms: 1.01x faster                                               |
| unpickle                | 13.2 us                                                                | 13.1 us: 1.01x faster                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| pprint_safe_repr        | 679 ms                                                                 | 676 ms: 1.00x faster                                                |
| sqlglot_optimize        | 51.3 ms                                                                | 51.1 ms: 1.00x faster                                               |
| bench_thread_pool       | 780 us                                                                 | 777 us: 1.00x faster                                                |
| sympy_integrate         | 19.8 ms                                                                | 19.8 ms: 1.00x faster                                               |
| xml_etree_generate      | 77.3 ms                                                                | 77.5 ms: 1.00x slower                                               |
| docutils                | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                              |
| python_startup          | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.50 ms: 1.00x slower                                               |
| pidigits                | 189 ms                                                                 | 190 ms: 1.01x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 33.9 us: 1.01x slower                                               |
| generators              | 77.0 ms                                                                | 77.7 ms: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                                               | 1.32 sec: 1.01x slower                                              |
| float                   | 72.3 ms                                                                | 73.1 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.47 ms: 1.01x slower                                               |
| scimark_lu              | 106 ms                                                                 | 108 ms: 1.02x slower                                                |
| genshi_xml              | 46.7 ms                                                                | 47.5 ms: 1.02x slower                                               |
| fannkuch                | 361 ms                                                                 | 368 ms: 1.02x slower                                                |
| unpickle_list           | 5.04 us                                                                | 5.15 us: 1.02x slower                                               |
| nqueens                 | 75.4 ms                                                                | 77.2 ms: 1.02x slower                                               |
| pyflate                 | 400 ms                                                                 | 410 ms: 1.02x slower                                                |
| scimark_monte_carlo     | 65.4 ms                                                                | 67.0 ms: 1.02x slower                                               |
| nbody                   | 94.2 ms                                                                | 96.7 ms: 1.03x slower                                               |
| genshi_text             | 20.7 ms                                                                | 21.3 ms: 1.03x slower                                               |
| crypto_pyaes            | 73.3 ms                                                                | 76.1 ms: 1.04x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.14 sec: 1.05x slower                                              |
| regex_v8                | 21.1 ms                                                                | 22.2 ms: 1.05x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 3.93 ms: 1.08x slower                                               |
| regex_dna               | 200 ms                                                                 | 217 ms: 1.08x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.77 ms: 1.12x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (27): html5lib, json, logging_silent, logging_format, mypy, thrift, hexiom, sympy_sum, asyncio_tcp, deltablue, raytrace, scimark_sor, sqlglot_parse, sqlglot_normalize, bench_mp_pool, async_generators, scimark_fft, 2to3, xml_etree_process, unpickle_pure_python, djangocms, telco, json_dumps, meteor_contest, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization
