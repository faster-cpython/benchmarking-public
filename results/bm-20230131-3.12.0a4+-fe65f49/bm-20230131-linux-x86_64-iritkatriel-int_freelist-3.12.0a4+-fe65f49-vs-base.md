
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
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                                |
| chameleon      | 6.35 ms                                                                | 6.29 ms: 1.01x faster                                               |
| docutils       | 2.50 sec                                                               | 2.51 sec: 1.01x slower                                              |
| html5lib       | 60.8 ms                                                                | 61.9 ms: 1.02x slower                                               |
| tornado_http   | 94.1 ms                                                                | 95.0 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 72.3 ms                                                                | 72.8 ms: 1.01x slower                                               |
| pidigits       | 189 ms                                                                 | 192 ms: 1.01x slower                                                |
| nbody          | 94.2 ms                                                                | 97.9 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_v8       | 21.1 ms                                                                | 21.7 ms: 1.03x slower                                               |
| regex_effbot   | 3.36 ms                                                                | 3.50 ms: 1.04x slower                                               |
| regex_dna      | 200 ms                                                                 | 210 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict          | 32.2 us                                                                | 30.5 us: 1.06x faster                                               |
| pickle_list          | 4.26 us                                                                | 4.09 us: 1.04x faster                                               |
| xml_etree_iterparse  | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| unpickle_list        | 5.04 us                                                                | 4.90 us: 1.03x faster                                               |
| pickle               | 10.3 us                                                                | 10.3 us: 1.00x faster                                               |
| xml_etree_generate   | 77.3 ms                                                                | 77.7 ms: 1.00x slower                                               |
| unpickle_pure_python | 198 us                                                                 | 199 us: 1.00x slower                                                |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| json_loads           | 24.3 us                                                                | 24.6 us: 1.01x slower                                               |
| unpickle             | 13.2 us                                                                | 13.6 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_process, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.47 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 20.7 ms                                                                | 20.2 ms: 1.02x faster                                               |
| django_template | 32.9 ms                                                                | 32.6 ms: 1.01x faster                                               |
| mako            | 9.77 ms                                                                | 9.82 ms: 1.00x slower                                               |
| genshi_xml      | 46.7 ms                                                                | 47.0 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict             | 32.2 us                                                                | 30.5 us: 1.06x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.09 us: 1.04x faster                                               |
| coverage                | 99.1 ms                                                                | 95.1 ms: 1.04x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| unpickle_list           | 5.04 us                                                                | 4.90 us: 1.03x faster                                               |
| async_tree_memoization  | 651 ms                                                                 | 635 ms: 1.03x faster                                                |
| genshi_text             | 20.7 ms                                                                | 20.2 ms: 1.02x faster                                               |
| logging_silent          | 93.3 ns                                                                | 91.3 ns: 1.02x faster                                               |
| sqlglot_normalize       | 106 ms                                                                 | 104 ms: 1.02x faster                                                |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| sqlglot_optimize        | 51.3 ms                                                                | 50.7 ms: 1.01x faster                                               |
| chameleon               | 6.35 ms                                                                | 6.29 ms: 1.01x faster                                               |
| coroutines              | 25.8 ms                                                                | 25.5 ms: 1.01x faster                                               |
| unpack_sequence         | 43.4 ns                                                                | 43.0 ns: 1.01x faster                                               |
| sympy_expand            | 458 ms                                                                 | 453 ms: 1.01x faster                                                |
| thrift                  | 742 us                                                                 | 735 us: 1.01x faster                                                |
| django_template         | 32.9 ms                                                                | 32.6 ms: 1.01x faster                                               |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.00x faster                                                |
| pickle                  | 10.3 us                                                                | 10.3 us: 1.00x faster                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.47 ms: 1.00x faster                                               |
| deepcopy                | 328 us                                                                 | 330 us: 1.00x slower                                                |
| xml_etree_generate      | 77.3 ms                                                                | 77.7 ms: 1.00x slower                                               |
| mako                    | 9.77 ms                                                                | 9.82 ms: 1.00x slower                                               |
| unpickle_pure_python    | 198 us                                                                 | 199 us: 1.00x slower                                                |
| genshi_xml              | 46.7 ms                                                                | 47.0 ms: 1.01x slower                                               |
| hexiom                  | 5.95 ms                                                                | 5.99 ms: 1.01x slower                                               |
| docutils                | 2.50 sec                                                               | 2.51 sec: 1.01x slower                                              |
| float                   | 72.3 ms                                                                | 72.8 ms: 1.01x slower                                               |
| 2to3                    | 251 ms                                                                 | 253 ms: 1.01x slower                                                |
| asyncio_tcp             | 493 ms                                                                 | 496 ms: 1.01x slower                                                |
| scimark_lu              | 106 ms                                                                 | 107 ms: 1.01x slower                                                |
| tornado_http            | 94.1 ms                                                                | 95.0 ms: 1.01x slower                                               |
| json                    | 4.63 ms                                                                | 4.67 ms: 1.01x slower                                               |
| xml_etree_parse         | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| pidigits                | 189 ms                                                                 | 192 ms: 1.01x slower                                                |
| json_loads              | 24.3 us                                                                | 24.6 us: 1.01x slower                                               |
| meteor_contest          | 103 ms                                                                 | 105 ms: 1.02x slower                                                |
| html5lib                | 60.8 ms                                                                | 61.9 ms: 1.02x slower                                               |
| deltablue               | 3.18 ms                                                                | 3.24 ms: 1.02x slower                                               |
| fannkuch                | 361 ms                                                                 | 369 ms: 1.02x slower                                                |
| go                      | 135 ms                                                                 | 138 ms: 1.02x slower                                                |
| dulwich_log             | 62.8 ms                                                                | 64.3 ms: 1.02x slower                                               |
| bench_thread_pool       | 780 us                                                                 | 800 us: 1.03x slower                                                |
| chaos                   | 64.7 ms                                                                | 66.4 ms: 1.03x slower                                               |
| raytrace                | 284 ms                                                                 | 292 ms: 1.03x slower                                                |
| unpickle                | 13.2 us                                                                | 13.6 us: 1.03x slower                                               |
| regex_v8                | 21.1 ms                                                                | 21.7 ms: 1.03x slower                                               |
| deepcopy_memo           | 33.6 us                                                                | 34.7 us: 1.03x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.12 sec: 1.03x slower                                              |
| scimark_monte_carlo     | 65.4 ms                                                                | 67.6 ms: 1.03x slower                                               |
| nbody                   | 94.2 ms                                                                | 97.9 ms: 1.04x slower                                               |
| regex_effbot            | 3.36 ms                                                                | 3.50 ms: 1.04x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                                | 1.78 ms: 1.05x slower                                               |
| regex_dna               | 200 ms                                                                 | 210 ms: 1.05x slower                                                |
| sqlite_synth            | 2.57 us                                                                | 2.70 us: 1.05x slower                                               |
| dask                    | 501 ms                                                                 | 526 ms: 1.05x slower                                                |
| sqlglot_parse           | 1.40 ms                                                                | 1.48 ms: 1.05x slower                                               |
| generators              | 77.0 ms                                                                | 81.0 ms: 1.05x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 3.82 ms: 1.05x slower                                               |
| nqueens                 | 75.4 ms                                                                | 79.3 ms: 1.05x slower                                               |
| async_generators        | 353 ms                                                                 | 372 ms: 1.05x slower                                                |
| mdp                     | 2.58 sec                                                               | 2.72 sec: 1.05x slower                                              |
| pathlib                 | 17.9 ms                                                                | 19.0 ms: 1.06x slower                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.48 ms: 1.10x slower                                               |
| pyflate                 | 400 ms                                                                 | 467 ms: 1.17x slower                                                |
| scimark_sor             | 107 ms                                                                 | 125 ms: 1.17x slower                                                |
| crypto_pyaes            | 73.3 ms                                                                | 89.5 ms: 1.22x slower                                               |
| scimark_fft             | 304 ms                                                                 | 397 ms: 1.30x slower                                                |
| spectral_norm           | 98.3 ms                                                                | 141 ms: 1.44x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (22): gunicorn, telco, sympy_sum, xml_etree_process, pickle_pure_python, json_dumps, logging_simple, richards, async_tree_io, pprint_safe_repr, sympy_integrate, aiohttp, logging_format, create_gc_cycles, python_startup, bench_mp_pool, mypy, async_tree_cpu_io_mixed, pprint_pformat, deepcopy_reduce, async_tree_none, djangocms
