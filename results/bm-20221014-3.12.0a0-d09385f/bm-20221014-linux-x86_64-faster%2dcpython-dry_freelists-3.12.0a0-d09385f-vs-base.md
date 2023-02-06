
# Results vs. base

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 247 ms                                                                | 246 ms: 1.00x faster                                                     |
| chameleon      | 6.50 ms                                                               | 6.46 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 95.6 ms                                                               | 94.3 ms: 1.01x faster                                                    |
| float          | 72.6 ms                                                               | 71.8 ms: 1.01x faster                                                    |
| pidigits       | 190 ms                                                                | 191 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 207 ms                                                                | 206 ms: 1.01x faster                                                     |
| regex_effbot   | 3.61 ms                                                               | 3.63 ms: 1.01x slower                                                    |
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                                     |
| regex_v8       | 21.1 ms                                                               | 21.8 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 32.0 us                                                               | 30.0 us: 1.07x faster                                                    |
| pickle_list          | 4.18 us                                                               | 3.95 us: 1.06x faster                                                    |
| json_loads           | 23.9 us                                                               | 23.5 us: 1.02x faster                                                    |
| xml_etree_process    | 54.2 ms                                                               | 53.9 ms: 1.01x faster                                                    |
| unpickle_list        | 4.91 us                                                               | 4.88 us: 1.01x faster                                                    |
| unpickle_pure_python | 201 us                                                                | 203 us: 1.01x slower                                                     |
| xml_etree_generate   | 75.8 ms                                                               | 76.4 ms: 1.01x slower                                                    |
| json_dumps           | 9.22 ms                                                               | 9.42 ms: 1.02x slower                                                    |
| xml_etree_iterparse  | 101 ms                                                                | 106 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (4): unpickle, pickle, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.42 ms                                                               | 8.43 ms: 1.00x slower                                                    |
| python_startup_no_site | 5.93 ms                                                               | 5.95 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                               | 20.7 ms: 1.03x faster                                                    |
| genshi_xml      | 49.4 ms                                                               | 48.6 ms: 1.02x faster                                                    |
| django_template | 32.6 ms                                                               | 32.2 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal            | 4.25 ms                                                               | 3.66 ms: 1.16x faster                                                    |
| pickle_dict             | 32.0 us                                                               | 30.0 us: 1.07x faster                                                    |
| pickle_list             | 4.18 us                                                               | 3.95 us: 1.06x faster                                                    |
| nqueens                 | 82.6 ms                                                               | 78.5 ms: 1.05x faster                                                    |
| pycparser               | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                   |
| genshi_text             | 21.3 ms                                                               | 20.7 ms: 1.03x faster                                                    |
| richards                | 44.2 ms                                                               | 42.8 ms: 1.03x faster                                                    |
| deltablue               | 3.39 ms                                                               | 3.29 ms: 1.03x faster                                                    |
| pprint_pformat          | 1.40 sec                                                              | 1.37 sec: 1.03x faster                                                   |
| sqlite_synth            | 2.63 us                                                               | 2.58 us: 1.02x faster                                                    |
| json_loads              | 23.9 us                                                               | 23.5 us: 1.02x faster                                                    |
| logging_simple          | 5.77 us                                                               | 5.67 us: 1.02x faster                                                    |
| genshi_xml              | 49.4 ms                                                               | 48.6 ms: 1.02x faster                                                    |
| go                      | 134 ms                                                                | 132 ms: 1.01x faster                                                     |
| nbody                   | 95.6 ms                                                               | 94.3 ms: 1.01x faster                                                    |
| pprint_safe_repr        | 683 ms                                                                | 674 ms: 1.01x faster                                                     |
| django_template         | 32.6 ms                                                               | 32.2 ms: 1.01x faster                                                    |
| deepcopy                | 340 us                                                                | 336 us: 1.01x faster                                                     |
| float                   | 72.6 ms                                                               | 71.8 ms: 1.01x faster                                                    |
| fannkuch                | 369 ms                                                                | 365 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.92 us                                                               | 2.89 us: 1.01x faster                                                    |
| sympy_sum               | 164 ms                                                                | 163 ms: 1.01x faster                                                     |
| sympy_expand            | 456 ms                                                                | 453 ms: 1.01x faster                                                     |
| telco                   | 6.45 ms                                                               | 6.41 ms: 1.01x faster                                                    |
| chameleon               | 6.50 ms                                                               | 6.46 ms: 1.01x faster                                                    |
| logging_format          | 6.38 us                                                               | 6.34 us: 1.01x faster                                                    |
| xml_etree_process       | 54.2 ms                                                               | 53.9 ms: 1.01x faster                                                    |
| regex_dna               | 207 ms                                                                | 206 ms: 1.01x faster                                                     |
| logging_silent          | 92.4 ns                                                               | 91.9 ns: 1.01x faster                                                    |
| unpickle_list           | 4.91 us                                                               | 4.88 us: 1.01x faster                                                    |
| scimark_fft             | 321 ms                                                                | 320 ms: 1.01x faster                                                     |
| aiohttp                 | 997 us                                                                | 993 us: 1.00x faster                                                     |
| 2to3                    | 247 ms                                                                | 246 ms: 1.00x faster                                                     |
| python_startup          | 8.42 ms                                                               | 8.43 ms: 1.00x slower                                                    |
| python_startup_no_site  | 5.93 ms                                                               | 5.95 ms: 1.00x slower                                                    |
| sqlalchemy_imperative   | 16.9 ms                                                               | 17.0 ms: 1.00x slower                                                    |
| sqlglot_optimize        | 51.3 ms                                                               | 51.6 ms: 1.01x slower                                                    |
| pidigits                | 190 ms                                                                | 191 ms: 1.01x slower                                                     |
| unpickle_pure_python    | 201 us                                                                | 203 us: 1.01x slower                                                     |
| pyflate                 | 394 ms                                                                | 397 ms: 1.01x slower                                                     |
| regex_effbot            | 3.61 ms                                                               | 3.63 ms: 1.01x slower                                                    |
| xml_etree_generate      | 75.8 ms                                                               | 76.4 ms: 1.01x slower                                                    |
| asyncio_tcp             | 861 ms                                                                | 868 ms: 1.01x slower                                                     |
| regex_compile           | 128 ms                                                                | 129 ms: 1.01x slower                                                     |
| create_gc_cycles        | 1.44 ms                                                               | 1.46 ms: 1.01x slower                                                    |
| scimark_monte_carlo     | 65.5 ms                                                               | 66.1 ms: 1.01x slower                                                    |
| bench_thread_pool       | 774 us                                                                | 783 us: 1.01x slower                                                     |
| async_tree_io           | 1.30 sec                                                              | 1.31 sec: 1.01x slower                                                   |
| scimark_sparse_mat_mult | 4.16 ms                                                               | 4.22 ms: 1.02x slower                                                    |
| scimark_sor             | 106 ms                                                                | 107 ms: 1.02x slower                                                     |
| generators              | 71.9 ms                                                               | 73.3 ms: 1.02x slower                                                    |
| async_generators        | 348 ms                                                                | 355 ms: 1.02x slower                                                     |
| json_dumps              | 9.22 ms                                                               | 9.42 ms: 1.02x slower                                                    |
| hexiom                  | 6.04 ms                                                               | 6.18 ms: 1.02x slower                                                    |
| chaos                   | 66.2 ms                                                               | 67.9 ms: 1.03x slower                                                    |
| spectral_norm           | 96.2 ms                                                               | 99.0 ms: 1.03x slower                                                    |
| regex_v8                | 21.1 ms                                                               | 21.8 ms: 1.03x slower                                                    |
| crypto_pyaes            | 73.2 ms                                                               | 76.3 ms: 1.04x slower                                                    |
| xml_etree_iterparse     | 101 ms                                                                | 106 ms: 1.05x slower                                                     |
| coroutines              | 24.4 ms                                                               | 25.7 ms: 1.05x slower                                                    |
| mdp                     | 2.54 sec                                                              | 2.71 sec: 1.07x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (33): unpickle, pathlib, coverage, unpack_sequence, deepcopy_memo, sympy_str, tornado_http, sqlglot_parse, sqlalchemy_declarative, meteor_contest, sqlglot_transpile, mypy, bench_mp_pool, pickle, dulwich_log, sympy_integrate, html5lib, async_tree_memoization, async_tree_none, sqlglot_normalize, mako, docutils, json, raytrace, gunicorn, djangocms, async_tree_cpu_io_mixed, xml_etree_parse, pylint, thrift, pickle_pure_python, dask, scimark_lu
