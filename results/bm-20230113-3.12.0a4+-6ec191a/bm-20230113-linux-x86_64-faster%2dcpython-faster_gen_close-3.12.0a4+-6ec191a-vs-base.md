
# Results vs. base

- fork: faster-cpython
- ref: faster_gen_close
- machine: linux-x86_64
- commit hash: 6ec191a
- commit date: 2023-01-13
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.00x faster                                                         |
| docutils       | 2.49 sec                                                               | 2.52 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.0 ms                                                                | 71.3 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_dna      | 207 ms                                                                 | 215 ms: 1.04x slower                                                         |
| regex_effbot   | 3.55 ms                                                                | 3.69 ms: 1.04x slower                                                        |
| regex_v8       | 22.5 ms                                                                | 22.4 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 9.60 ms                                                                | 9.40 ms: 1.02x faster                                                        |
| pickle_dict          | 30.8 us                                                                | 31.2 us: 1.01x slower                                                        |
| pickle_list          | 4.02 us                                                                | 4.23 us: 1.05x slower                                                        |
| pickle_pure_python   | 280 us                                                                 | 284 us: 1.02x slower                                                         |
| unpickle             | 12.9 us                                                                | 13.2 us: 1.02x slower                                                        |
| unpickle_list        | 5.03 us                                                                | 4.98 us: 1.01x faster                                                        |
| unpickle_pure_python | 197 us                                                                 | 198 us: 1.00x slower                                                         |
| xml_etree_iterparse  | 106 ms                                                                 | 103 ms: 1.03x faster                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): json_loads, pickle, xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.55 ms                                                                | 8.52 ms: 1.00x faster                                                        |
| python_startup_no_site | 6.11 ms                                                                | 6.09 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 32.4 ms                                                                | 32.7 ms: 1.01x slower                                                        |
| genshi_text     | 21.0 ms                                                                | 20.5 ms: 1.03x faster                                                        |
| genshi_xml      | 46.5 ms                                                                | 47.0 ms: 1.01x slower                                                        |
| mako            | 9.59 ms                                                                | 9.79 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230112-linux-x86_64-python-94fc7706b7bc3d57cdd6-3.12.0a4+-94fc770 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3                    | 251 ms                                                                 | 250 ms: 1.00x faster                                                         |
| async_tree_memoization  | 621 ms                                                                 | 635 ms: 1.02x slower                                                         |
| asyncio_tcp             | 503 ms                                                                 | 501 ms: 1.01x faster                                                         |
| coroutines              | 24.4 ms                                                                | 25.3 ms: 1.04x slower                                                        |
| coverage                | 99.5 ms                                                                | 97.5 ms: 1.02x faster                                                        |
| crypto_pyaes            | 74.9 ms                                                                | 76.9 ms: 1.03x slower                                                        |
| deepcopy_reduce         | 2.95 us                                                                | 2.89 us: 1.02x faster                                                        |
| deepcopy_memo           | 33.1 us                                                                | 33.4 us: 1.01x slower                                                        |
| django_template         | 32.4 ms                                                                | 32.7 ms: 1.01x slower                                                        |
| docutils                | 2.49 sec                                                               | 2.52 sec: 1.01x slower                                                       |
| fannkuch                | 359 ms                                                                 | 371 ms: 1.03x slower                                                         |
| float                   | 72.0 ms                                                                | 71.3 ms: 1.01x faster                                                        |
| gc_traversal            | 4.05 ms                                                                | 3.63 ms: 1.12x faster                                                        |
| generators              | 73.9 ms                                                                | 76.6 ms: 1.04x slower                                                        |
| genshi_text             | 21.0 ms                                                                | 20.5 ms: 1.03x faster                                                        |
| genshi_xml              | 46.5 ms                                                                | 47.0 ms: 1.01x slower                                                        |
| go                      | 136 ms                                                                 | 136 ms: 1.00x slower                                                         |
| hexiom                  | 6.14 ms                                                                | 6.12 ms: 1.00x faster                                                        |
| json                    | 4.71 ms                                                                | 4.66 ms: 1.01x faster                                                        |
| json_dumps              | 9.60 ms                                                                | 9.40 ms: 1.02x faster                                                        |
| logging_format          | 6.37 us                                                                | 6.34 us: 1.01x faster                                                        |
| logging_silent          | 93.8 ns                                                                | 92.7 ns: 1.01x faster                                                        |
| logging_simple          | 5.65 us                                                                | 5.74 us: 1.02x slower                                                        |
| mako                    | 9.59 ms                                                                | 9.79 ms: 1.02x slower                                                        |
| mdp                     | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                                       |
| nqueens                 | 78.3 ms                                                                | 80.8 ms: 1.03x slower                                                        |
| pickle_dict             | 30.8 us                                                                | 31.2 us: 1.01x slower                                                        |
| pickle_list             | 4.02 us                                                                | 4.23 us: 1.05x slower                                                        |
| pickle_pure_python      | 280 us                                                                 | 284 us: 1.02x slower                                                         |
| pprint_safe_repr        | 674 ms                                                                 | 670 ms: 1.01x faster                                                         |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                       |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                                       |
| pyflate                 | 397 ms                                                                 | 395 ms: 1.00x faster                                                         |
| python_startup          | 8.55 ms                                                                | 8.52 ms: 1.00x faster                                                        |
| python_startup_no_site  | 6.11 ms                                                                | 6.09 ms: 1.00x faster                                                        |
| raytrace                | 281 ms                                                                 | 283 ms: 1.01x slower                                                         |
| regex_compile           | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_dna               | 207 ms                                                                 | 215 ms: 1.04x slower                                                         |
| regex_effbot            | 3.55 ms                                                                | 3.69 ms: 1.04x slower                                                        |
| regex_v8                | 22.5 ms                                                                | 22.4 ms: 1.00x faster                                                        |
| richards                | 41.1 ms                                                                | 42.9 ms: 1.04x slower                                                        |
| scimark_fft             | 311 ms                                                                 | 313 ms: 1.01x slower                                                         |
| scimark_monte_carlo     | 64.7 ms                                                                | 64.4 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult | 4.10 ms                                                                | 4.22 ms: 1.03x slower                                                        |
| spectral_norm           | 98.2 ms                                                                | 95.3 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 50.5 ms                                                                | 51.1 ms: 1.01x slower                                                        |
| sqlglot_normalize       | 104 ms                                                                 | 106 ms: 1.02x slower                                                         |
| sqlite_synth            | 2.56 us                                                                | 2.59 us: 1.01x slower                                                        |
| sympy_integrate         | 20.3 ms                                                                | 19.9 ms: 1.02x faster                                                        |
| sympy_sum               | 163 ms                                                                 | 156 ms: 1.04x faster                                                         |
| sympy_str               | 281 ms                                                                 | 269 ms: 1.04x faster                                                         |
| telco                   | 6.17 ms                                                                | 6.25 ms: 1.01x slower                                                        |
| thrift                  | 735 us                                                                 | 752 us: 1.02x slower                                                         |
| unpack_sequence         | 41.3 ns                                                                | 41.8 ns: 1.01x slower                                                        |
| unpickle                | 12.9 us                                                                | 13.2 us: 1.02x slower                                                        |
| unpickle_list           | 5.03 us                                                                | 4.98 us: 1.01x faster                                                        |
| unpickle_pure_python    | 197 us                                                                 | 198 us: 1.00x slower                                                         |
| xml_etree_iterparse     | 106 ms                                                                 | 103 ms: 1.03x faster                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (30): async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, chameleon, chaos, bench_mp_pool, bench_thread_pool, dask, deepcopy, deltablue, djangocms, dulwich_log, create_gc_cycles, html5lib, json_loads, meteor_contest, mypy, nbody, pathlib, pickle, pidigits, scimark_lu, scimark_sor, sqlglot_parse, sqlglot_transpile, sympy_expand, xml_etree_parse, xml_etree_generate, xml_etree_process
