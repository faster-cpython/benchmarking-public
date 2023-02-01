
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                |
| docutils       | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                              |
| html5lib       | 60.0 ms                                                                | 62.1 ms: 1.03x slower                                               |
| tornado_http   | 93.7 ms                                                                | 95.0 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 199 ms: 1.03x slower                                                |
| nbody          | 93.3 ms                                                                | 97.5 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_v8       | 21.6 ms                                                                | 22.2 ms: 1.03x slower                                               |
| regex_dna      | 202 ms                                                                 | 210 ms: 1.04x slower                                                |
| regex_effbot   | 3.39 ms                                                                | 3.63 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 105 ms                                                                 | 102 ms: 1.03x faster                                                |
| xml_etree_parse      | 149 ms                                                                 | 147 ms: 1.01x faster                                                |
| unpickle_list        | 4.90 us                                                                | 4.85 us: 1.01x faster                                               |
| unpickle_pure_python | 197 us                                                                 | 199 us: 1.01x slower                                                |
| pickle_pure_python   | 282 us                                                                 | 286 us: 1.02x slower                                                |
| json_dumps           | 9.34 ms                                                                | 9.52 ms: 1.02x slower                                               |
| json_loads           | 23.7 us                                                                | 24.9 us: 1.05x slower                                               |
| unpickle             | 13.1 us                                                                | 13.8 us: 1.05x slower                                               |
| pickle_dict          | 30.5 us                                                                | 32.1 us: 1.05x slower                                               |
| pickle_list          | 3.96 us                                                                | 4.30 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (3): pickle, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.44 ms                                                                | 6.44 ms: 1.00x faster                                               |
| python_startup         | 8.89 ms                                                                | 8.91 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 9.75 ms                                                                | 9.82 ms: 1.01x slower                                               |
| genshi_text    | 20.3 ms                                                                | 21.0 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coverage                | 99.0 ms                                                                | 95.6 ms: 1.04x faster                                               |
| xml_etree_iterparse     | 105 ms                                                                 | 102 ms: 1.03x faster                                                |
| nqueens                 | 76.9 ms                                                                | 74.8 ms: 1.03x faster                                               |
| chaos                   | 65.6 ms                                                                | 63.9 ms: 1.03x faster                                               |
| logging_simple          | 5.78 us                                                                | 5.64 us: 1.02x faster                                               |
| pprint_safe_repr        | 677 ms                                                                 | 663 ms: 1.02x faster                                                |
| djangocms               | 32.6 us                                                                | 31.9 us: 1.02x faster                                               |
| meteor_contest          | 105 ms                                                                 | 103 ms: 1.02x faster                                                |
| unpack_sequence         | 42.7 ns                                                                | 42.0 ns: 1.02x faster                                               |
| scimark_lu              | 108 ms                                                                 | 107 ms: 1.02x faster                                                |
| xml_etree_parse         | 149 ms                                                                 | 147 ms: 1.01x faster                                                |
| logging_format          | 6.35 us                                                                | 6.26 us: 1.01x faster                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.01x faster                                              |
| unpickle_list           | 4.90 us                                                                | 4.85 us: 1.01x faster                                               |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.01x faster                                                |
| sympy_str               | 269 ms                                                                 | 268 ms: 1.00x faster                                                |
| sympy_integrate         | 19.7 ms                                                                | 19.6 ms: 1.00x faster                                               |
| python_startup_no_site  | 6.44 ms                                                                | 6.44 ms: 1.00x faster                                               |
| gc_traversal            | 3.82 ms                                                                | 3.82 ms: 1.00x slower                                               |
| python_startup          | 8.89 ms                                                                | 8.91 ms: 1.00x slower                                               |
| sqlglot_optimize        | 50.7 ms                                                                | 51.0 ms: 1.00x slower                                               |
| deltablue               | 3.22 ms                                                                | 3.24 ms: 1.01x slower                                               |
| sympy_expand            | 451 ms                                                                 | 453 ms: 1.01x slower                                                |
| hexiom                  | 5.98 ms                                                                | 6.02 ms: 1.01x slower                                               |
| mako                    | 9.75 ms                                                                | 9.82 ms: 1.01x slower                                               |
| thrift                  | 737 us                                                                 | 743 us: 1.01x slower                                                |
| 2to3                    | 250 ms                                                                 | 252 ms: 1.01x slower                                                |
| unpickle_pure_python    | 197 us                                                                 | 199 us: 1.01x slower                                                |
| aiohttp                 | 992 us                                                                 | 1.00 ms: 1.01x slower                                               |
| asyncio_tcp             | 490 ms                                                                 | 495 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 750 ms                                                                 | 757 ms: 1.01x slower                                                |
| docutils                | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                              |
| telco                   | 6.36 ms                                                                | 6.43 ms: 1.01x slower                                               |
| coroutines              | 25.2 ms                                                                | 25.5 ms: 1.01x slower                                               |
| gunicorn                | 1.06 ms                                                                | 1.08 ms: 1.01x slower                                               |
| tornado_http            | 93.7 ms                                                                | 95.0 ms: 1.01x slower                                               |
| async_tree_io           | 1.29 sec                                                               | 1.31 sec: 1.01x slower                                              |
| pickle_pure_python      | 282 us                                                                 | 286 us: 1.02x slower                                                |
| richards                | 42.9 ms                                                                | 43.6 ms: 1.02x slower                                               |
| json                    | 4.61 ms                                                                | 4.70 ms: 1.02x slower                                               |
| json_dumps              | 9.34 ms                                                                | 9.52 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 65.3 ms                                                                | 66.7 ms: 1.02x slower                                               |
| deepcopy_memo           | 34.3 us                                                                | 35.2 us: 1.02x slower                                               |
| async_tree_memoization  | 628 ms                                                                 | 644 ms: 1.03x slower                                                |
| raytrace                | 283 ms                                                                 | 290 ms: 1.03x slower                                                |
| regex_v8                | 21.6 ms                                                                | 22.2 ms: 1.03x slower                                               |
| dulwich_log             | 62.4 ms                                                                | 64.5 ms: 1.03x slower                                               |
| pidigits                | 192 ms                                                                 | 199 ms: 1.03x slower                                                |
| bench_thread_pool       | 778 us                                                                 | 805 us: 1.03x slower                                                |
| html5lib                | 60.0 ms                                                                | 62.1 ms: 1.03x slower                                               |
| genshi_text             | 20.3 ms                                                                | 21.0 ms: 1.04x slower                                               |
| regex_dna               | 202 ms                                                                 | 210 ms: 1.04x slower                                                |
| sqlglot_transpile       | 1.70 ms                                                                | 1.77 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.41 ms                                                                | 1.47 ms: 1.04x slower                                               |
| nbody                   | 93.3 ms                                                                | 97.5 ms: 1.04x slower                                               |
| sqlite_synth            | 2.55 us                                                                | 2.67 us: 1.05x slower                                               |
| json_loads              | 23.7 us                                                                | 24.9 us: 1.05x slower                                               |
| unpickle                | 13.1 us                                                                | 13.8 us: 1.05x slower                                               |
| pickle_dict             | 30.5 us                                                                | 32.1 us: 1.05x slower                                               |
| async_generators        | 351 ms                                                                 | 371 ms: 1.06x slower                                                |
| dask                    | 495 ms                                                                 | 525 ms: 1.06x slower                                                |
| regex_effbot            | 3.39 ms                                                                | 3.63 ms: 1.07x slower                                               |
| generators              | 76.4 ms                                                                | 82.2 ms: 1.08x slower                                               |
| pathlib                 | 17.6 ms                                                                | 18.9 ms: 1.08x slower                                               |
| pycparser               | 1.09 sec                                                               | 1.18 sec: 1.08x slower                                              |
| pickle_list             | 3.96 us                                                                | 4.30 us: 1.09x slower                                               |
| mdp                     | 2.44 sec                                                               | 2.66 sec: 1.09x slower                                              |
| scimark_sparse_mat_mult | 4.13 ms                                                                | 4.52 ms: 1.09x slower                                               |
| pyflate                 | 406 ms                                                                 | 468 ms: 1.15x slower                                                |
| scimark_sor             | 107 ms                                                                 | 125 ms: 1.16x slower                                                |
| crypto_pyaes            | 73.2 ms                                                                | 89.6 ms: 1.22x slower                                               |
| scimark_fft             | 306 ms                                                                 | 383 ms: 1.25x slower                                                |
| spectral_norm           | 97.0 ms                                                                | 136 ms: 1.40x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (18): pickle, django_template, sympy_sum, float, fannkuch, go, deepcopy_reduce, bench_mp_pool, xml_etree_process, create_gc_cycles, async_tree_none, deepcopy, xml_etree_generate, sqlglot_normalize, genshi_xml, logging_silent, mypy, chameleon
