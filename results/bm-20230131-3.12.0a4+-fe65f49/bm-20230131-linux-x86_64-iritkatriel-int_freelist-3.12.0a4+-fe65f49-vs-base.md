
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| docutils       | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                              |
| tornado_http   | 94.1 ms                                                                | 94.6 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 192 ms: 1.01x slower                                                |
| float          | 72.3 ms                                                                | 73.8 ms: 1.02x slower                                               |
| nbody          | 94.2 ms                                                                | 98.3 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_dna      | 200 ms                                                                 | 210 ms: 1.05x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.54 ms: 1.05x slower                                               |
| regex_v8       | 21.1 ms                                                                | 22.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| pickle              | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| unpickle_list       | 5.04 us                                                                | 4.93 us: 1.02x faster                                               |
| pickle_list         | 4.26 us                                                                | 4.18 us: 1.02x faster                                               |
| pickle_dict         | 32.2 us                                                                | 31.6 us: 1.02x faster                                               |
| unpickle            | 13.2 us                                                                | 13.3 us: 1.00x slower                                               |
| xml_etree_parse     | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| json_dumps          | 9.37 ms                                                                | 9.47 ms: 1.01x slower                                               |
| json_loads          | 24.3 us                                                                | 25.1 us: 1.03x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.47 ms: 1.00x faster                                               |
| python_startup         | 8.94 ms                                                                | 8.96 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.9 ms                                                                | 32.4 ms: 1.01x faster                                               |
| genshi_text     | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                               |
| genshi_xml      | 46.7 ms                                                                | 47.2 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse     | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| coroutines              | 25.8 ms                                                                | 25.1 ms: 1.03x faster                                               |
| async_tree_memoization  | 651 ms                                                                 | 635 ms: 1.03x faster                                                |
| richards                | 43.9 ms                                                                | 42.9 ms: 1.02x faster                                               |
| pickle                  | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| unpickle_list           | 5.04 us                                                                | 4.93 us: 1.02x faster                                               |
| unpack_sequence         | 43.4 ns                                                                | 42.6 ns: 1.02x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.18 us: 1.02x faster                                               |
| pickle_dict             | 32.2 us                                                                | 31.6 us: 1.02x faster                                               |
| thrift                  | 742 us                                                                 | 731 us: 1.02x faster                                                |
| django_template         | 32.9 ms                                                                | 32.4 ms: 1.01x faster                                               |
| sqlglot_optimize        | 51.3 ms                                                                | 50.6 ms: 1.01x faster                                               |
| deepcopy                | 328 us                                                                 | 325 us: 1.01x faster                                                |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| sympy_sum               | 156 ms                                                                 | 154 ms: 1.01x faster                                                |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| logging_format          | 6.29 us                                                                | 6.23 us: 1.01x faster                                               |
| coverage                | 99.1 ms                                                                | 98.2 ms: 1.01x faster                                               |
| logging_simple          | 5.73 us                                                                | 5.67 us: 1.01x faster                                               |
| sympy_expand            | 458 ms                                                                 | 454 ms: 1.01x faster                                                |
| genshi_text             | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                               |
| sympy_integrate         | 19.8 ms                                                                | 19.6 ms: 1.01x faster                                               |
| pprint_safe_repr        | 679 ms                                                                 | 674 ms: 1.01x faster                                                |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.01x faster                                                |
| aiohttp                 | 1.00 ms                                                                | 1000 us: 1.00x faster                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.47 ms: 1.00x faster                                               |
| python_startup          | 8.94 ms                                                                | 8.96 ms: 1.00x slower                                               |
| unpickle                | 13.2 us                                                                | 13.3 us: 1.00x slower                                               |
| tornado_http            | 94.1 ms                                                                | 94.6 ms: 1.01x slower                                               |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| asyncio_tcp             | 493 ms                                                                 | 497 ms: 1.01x slower                                                |
| docutils                | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                              |
| xml_etree_parse         | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| json_dumps              | 9.37 ms                                                                | 9.47 ms: 1.01x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.2 ms: 1.01x slower                                               |
| pidigits                | 189 ms                                                                 | 192 ms: 1.01x slower                                                |
| raytrace                | 284 ms                                                                 | 288 ms: 1.01x slower                                                |
| hexiom                  | 5.95 ms                                                                | 6.03 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.47 ms: 1.01x slower                                               |
| deltablue               | 3.18 ms                                                                | 3.25 ms: 1.02x slower                                               |
| json                    | 4.63 ms                                                                | 4.73 ms: 1.02x slower                                               |
| float                   | 72.3 ms                                                                | 73.8 ms: 1.02x slower                                               |
| bench_thread_pool       | 780 us                                                                 | 800 us: 1.03x slower                                                |
| dulwich_log             | 62.8 ms                                                                | 64.6 ms: 1.03x slower                                               |
| scimark_lu              | 106 ms                                                                 | 109 ms: 1.03x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 34.6 us: 1.03x slower                                               |
| generators              | 77.0 ms                                                                | 79.5 ms: 1.03x slower                                               |
| nqueens                 | 75.4 ms                                                                | 77.9 ms: 1.03x slower                                               |
| json_loads              | 24.3 us                                                                | 25.1 us: 1.03x slower                                               |
| chaos                   | 64.7 ms                                                                | 66.9 ms: 1.03x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                                | 1.76 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.40 ms                                                                | 1.46 ms: 1.04x slower                                               |
| sqlite_synth            | 2.57 us                                                                | 2.68 us: 1.04x slower                                               |
| go                      | 135 ms                                                                 | 141 ms: 1.04x slower                                                |
| nbody                   | 94.2 ms                                                                | 98.3 ms: 1.04x slower                                               |
| scimark_monte_carlo     | 65.4 ms                                                                | 68.3 ms: 1.05x slower                                               |
| regex_dna               | 200 ms                                                                 | 210 ms: 1.05x slower                                                |
| dask                    | 501 ms                                                                 | 525 ms: 1.05x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.54 ms: 1.05x slower                                               |
| async_generators        | 353 ms                                                                 | 373 ms: 1.06x slower                                                |
| pathlib                 | 17.9 ms                                                                | 19.1 ms: 1.07x slower                                               |
| regex_v8                | 21.1 ms                                                                | 22.5 ms: 1.07x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.17 sec: 1.08x slower                                              |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.71 ms: 1.15x slower                                               |
| pyflate                 | 400 ms                                                                 | 463 ms: 1.16x slower                                                |
| scimark_sor             | 107 ms                                                                 | 125 ms: 1.17x slower                                                |
| gc_traversal            | 3.64 ms                                                                | 4.29 ms: 1.18x slower                                               |
| crypto_pyaes            | 73.3 ms                                                                | 89.3 ms: 1.22x slower                                               |
| scimark_fft             | 304 ms                                                                 | 399 ms: 1.31x slower                                                |
| spectral_norm           | 98.3 ms                                                                | 138 ms: 1.41x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (19): logging_silent, telco, djangocms, mypy, deepcopy_reduce, mdp, bench_mp_pool, chameleon, mako, xml_etree_generate, unpickle_pure_python, xml_etree_process, pickle_pure_python, fannkuch, async_tree_none, meteor_contest, async_tree_io, html5lib, async_tree_cpu_io_mixed
