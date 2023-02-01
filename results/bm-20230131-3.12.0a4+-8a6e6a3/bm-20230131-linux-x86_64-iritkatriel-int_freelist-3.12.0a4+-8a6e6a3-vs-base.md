
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                |
| chameleon      | 6.31 ms                                                                | 6.37 ms: 1.01x slower                                               |
| docutils       | 2.49 sec                                                               | 2.50 sec: 1.01x slower                                              |
| html5lib       | 60.0 ms                                                                | 61.6 ms: 1.03x slower                                               |
| tornado_http   | 93.7 ms                                                                | 95.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 192 ms: 1.00x faster                                                |
| float          | 72.2 ms                                                                | 73.8 ms: 1.02x slower                                               |
| nbody          | 93.3 ms                                                                | 96.3 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 127 ms: 1.02x faster                                                |
| regex_v8       | 21.6 ms                                                                | 21.2 ms: 1.02x faster                                               |
| regex_effbot   | 3.39 ms                                                                | 3.47 ms: 1.02x slower                                               |
| regex_dna      | 202 ms                                                                 | 208 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 105 ms                                                                 | 103 ms: 1.02x faster                                                |
| xml_etree_parse      | 149 ms                                                                 | 147 ms: 1.01x faster                                                |
| unpickle_list        | 4.90 us                                                                | 4.93 us: 1.00x slower                                               |
| unpickle_pure_python | 197 us                                                                 | 198 us: 1.01x slower                                                |
| pickle_pure_python   | 282 us                                                                 | 286 us: 1.02x slower                                                |
| json_dumps           | 9.34 ms                                                                | 9.50 ms: 1.02x slower                                               |
| json_loads           | 23.7 us                                                                | 24.7 us: 1.04x slower                                               |
| pickle_dict          | 30.5 us                                                                | 31.8 us: 1.04x slower                                               |
| unpickle             | 13.1 us                                                                | 14.0 us: 1.07x slower                                               |
| pickle_list          | 3.96 us                                                                | 4.23 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (3): pickle, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.44 ms                                                                | 6.49 ms: 1.01x slower                                               |
| python_startup         | 8.89 ms                                                                | 8.97 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.75 ms                                                                | 9.80 ms: 1.00x slower                                               |
| django_template | 32.8 ms                                                                | 33.1 ms: 1.01x slower                                               |
| genshi_xml      | 46.7 ms                                                                | 47.4 ms: 1.01x slower                                               |
| genshi_text     | 20.3 ms                                                                | 20.6 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coverage                | 99.0 ms                                                                | 96.1 ms: 1.03x faster                                               |
| fannkuch                | 369 ms                                                                 | 360 ms: 1.03x faster                                                |
| xml_etree_iterparse     | 105 ms                                                                 | 103 ms: 1.02x faster                                                |
| regex_compile           | 129 ms                                                                 | 127 ms: 1.02x faster                                                |
| regex_v8                | 21.6 ms                                                                | 21.2 ms: 1.02x faster                                               |
| chaos                   | 65.6 ms                                                                | 64.4 ms: 1.02x faster                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.02x faster                                              |
| scimark_lu              | 108 ms                                                                 | 107 ms: 1.02x faster                                                |
| xml_etree_parse         | 149 ms                                                                 | 147 ms: 1.01x faster                                                |
| pprint_safe_repr        | 677 ms                                                                 | 669 ms: 1.01x faster                                                |
| go                      | 135 ms                                                                 | 134 ms: 1.01x faster                                                |
| nqueens                 | 76.9 ms                                                                | 76.2 ms: 1.01x faster                                               |
| pidigits                | 192 ms                                                                 | 192 ms: 1.00x faster                                                |
| gc_traversal            | 3.82 ms                                                                | 3.81 ms: 1.00x faster                                               |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.00x faster                                                |
| mako                    | 9.75 ms                                                                | 9.80 ms: 1.00x slower                                               |
| coroutines              | 25.2 ms                                                                | 25.3 ms: 1.00x slower                                               |
| unpickle_list           | 4.90 us                                                                | 4.93 us: 1.00x slower                                               |
| docutils                | 2.49 sec                                                               | 2.50 sec: 1.01x slower                                              |
| unpickle_pure_python    | 197 us                                                                 | 198 us: 1.01x slower                                                |
| sympy_sum               | 154 ms                                                                 | 156 ms: 1.01x slower                                                |
| django_template         | 32.8 ms                                                                | 33.1 ms: 1.01x slower                                               |
| python_startup_no_site  | 6.44 ms                                                                | 6.49 ms: 1.01x slower                                               |
| sympy_str               | 269 ms                                                                 | 271 ms: 1.01x slower                                                |
| deltablue               | 3.22 ms                                                                | 3.25 ms: 1.01x slower                                               |
| 2to3                    | 250 ms                                                                 | 252 ms: 1.01x slower                                                |
| python_startup          | 8.89 ms                                                                | 8.97 ms: 1.01x slower                                               |
| chameleon               | 6.31 ms                                                                | 6.37 ms: 1.01x slower                                               |
| telco                   | 6.36 ms                                                                | 6.43 ms: 1.01x slower                                               |
| deepcopy_reduce         | 2.98 us                                                                | 3.02 us: 1.01x slower                                               |
| aiohttp                 | 992 us                                                                 | 1.00 ms: 1.01x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.4 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 750 ms                                                                 | 761 ms: 1.01x slower                                                |
| gunicorn                | 1.06 ms                                                                | 1.08 ms: 1.01x slower                                               |
| asyncio_tcp             | 490 ms                                                                 | 498 ms: 1.02x slower                                                |
| tornado_http            | 93.7 ms                                                                | 95.3 ms: 1.02x slower                                               |
| pickle_pure_python      | 282 us                                                                 | 286 us: 1.02x slower                                                |
| json                    | 4.61 ms                                                                | 4.69 ms: 1.02x slower                                               |
| json_dumps              | 9.34 ms                                                                | 9.50 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 65.3 ms                                                                | 66.4 ms: 1.02x slower                                               |
| deepcopy_memo           | 34.3 us                                                                | 34.9 us: 1.02x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.48 ms: 1.02x slower                                               |
| thrift                  | 737 us                                                                 | 751 us: 1.02x slower                                                |
| genshi_text             | 20.3 ms                                                                | 20.6 ms: 1.02x slower                                               |
| sympy_expand            | 451 ms                                                                 | 459 ms: 1.02x slower                                                |
| float                   | 72.2 ms                                                                | 73.8 ms: 1.02x slower                                               |
| logging_silent          | 90.4 ns                                                                | 92.4 ns: 1.02x slower                                               |
| regex_effbot            | 3.39 ms                                                                | 3.47 ms: 1.02x slower                                               |
| html5lib                | 60.0 ms                                                                | 61.6 ms: 1.03x slower                                               |
| regex_dna               | 202 ms                                                                 | 208 ms: 1.03x slower                                                |
| pycparser               | 1.09 sec                                                               | 1.12 sec: 1.03x slower                                              |
| raytrace                | 283 ms                                                                 | 291 ms: 1.03x slower                                                |
| async_tree_io           | 1.29 sec                                                               | 1.33 sec: 1.03x slower                                              |
| bench_thread_pool       | 778 us                                                                 | 801 us: 1.03x slower                                                |
| dulwich_log             | 62.4 ms                                                                | 64.4 ms: 1.03x slower                                               |
| nbody                   | 93.3 ms                                                                | 96.3 ms: 1.03x slower                                               |
| mdp                     | 2.44 sec                                                               | 2.53 sec: 1.04x slower                                              |
| json_loads              | 23.7 us                                                                | 24.7 us: 1.04x slower                                               |
| pickle_dict             | 30.5 us                                                                | 31.8 us: 1.04x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                                | 1.78 ms: 1.05x slower                                               |
| sqlglot_parse           | 1.41 ms                                                                | 1.48 ms: 1.05x slower                                               |
| async_generators        | 351 ms                                                                 | 369 ms: 1.05x slower                                                |
| async_tree_memoization  | 628 ms                                                                 | 659 ms: 1.05x slower                                                |
| sqlite_synth            | 2.55 us                                                                | 2.68 us: 1.05x slower                                               |
| dask                    | 495 ms                                                                 | 525 ms: 1.06x slower                                                |
| unpickle                | 13.1 us                                                                | 14.0 us: 1.07x slower                                               |
| pickle_list             | 3.96 us                                                                | 4.23 us: 1.07x slower                                               |
| pathlib                 | 17.6 ms                                                                | 18.9 ms: 1.08x slower                                               |
| generators              | 76.4 ms                                                                | 83.5 ms: 1.09x slower                                               |
| scimark_sparse_mat_mult | 4.13 ms                                                                | 4.55 ms: 1.10x slower                                               |
| pyflate                 | 406 ms                                                                 | 461 ms: 1.14x slower                                                |
| scimark_sor             | 107 ms                                                                 | 123 ms: 1.15x slower                                                |
| crypto_pyaes            | 73.2 ms                                                                | 90.0 ms: 1.23x slower                                               |
| scimark_fft             | 306 ms                                                                 | 390 ms: 1.27x slower                                                |
| spectral_norm           | 97.0 ms                                                                | 138 ms: 1.42x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (16): pickle, meteor_contest, xml_etree_generate, unpack_sequence, sympy_integrate, hexiom, logging_format, bench_mp_pool, deepcopy, sqlglot_optimize, djangocms, logging_simple, xml_etree_process, mypy, richards, async_tree_none
