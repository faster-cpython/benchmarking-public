
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
| 2to3           | 247 ms                                                                | 248 ms: 1.01x slower                                                     |
| chameleon      | 6.50 ms                                                               | 6.46 ms: 1.01x faster                                                    |
| tornado_http   | 93.5 ms                                                               | 92.8 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 72.6 ms                                                               | 72.1 ms: 1.01x faster                                                    |
| pidigits       | 190 ms                                                                | 206 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                               | 3.43 ms: 1.05x faster                                                    |
| regex_compile  | 128 ms                                                                | 127 ms: 1.01x faster                                                     |
| regex_dna      | 207 ms                                                                | 218 ms: 1.05x slower                                                     |
| regex_v8       | 21.1 ms                                                               | 22.3 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 32.0 us                                                               | 31.1 us: 1.03x faster                                                    |
| json_loads           | 23.9 us                                                               | 23.4 us: 1.02x faster                                                    |
| pickle_list          | 4.18 us                                                               | 4.10 us: 1.02x faster                                                    |
| pickle_pure_python   | 290 us                                                                | 287 us: 1.01x faster                                                     |
| xml_etree_parse      | 159 ms                                                                | 158 ms: 1.01x faster                                                     |
| xml_etree_process    | 54.2 ms                                                               | 53.9 ms: 1.01x faster                                                    |
| unpickle_pure_python | 201 us                                                                | 203 us: 1.01x slower                                                     |
| json_dumps           | 9.22 ms                                                               | 9.30 ms: 1.01x slower                                                    |
| pickle               | 10.1 us                                                               | 10.3 us: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (4): unpickle, xml_etree_generate, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.42 ms                                                               | 8.41 ms: 1.00x faster                                                    |
| python_startup_no_site | 5.93 ms                                                               | 5.94 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                               | 20.8 ms: 1.03x faster                                                    |
| genshi_xml      | 49.4 ms                                                               | 49.1 ms: 1.01x faster                                                    |
| django_template | 32.6 ms                                                               | 32.5 ms: 1.00x faster                                                    |
| mako            | 9.59 ms                                                               | 9.89 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221006-linux-x86_64-python-f8edc6ff531bb9885818-3.12.0a0-f8edc6f | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal            | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                    |
| regex_effbot            | 3.61 ms                                                               | 3.43 ms: 1.05x faster                                                    |
| nqueens                 | 82.6 ms                                                               | 78.9 ms: 1.05x faster                                                    |
| richards                | 44.2 ms                                                               | 42.3 ms: 1.04x faster                                                    |
| deltablue               | 3.39 ms                                                               | 3.27 ms: 1.04x faster                                                    |
| pycparser               | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                   |
| deepcopy                | 340 us                                                                | 330 us: 1.03x faster                                                     |
| pickle_dict             | 32.0 us                                                               | 31.1 us: 1.03x faster                                                    |
| scimark_sparse_mat_mult | 4.16 ms                                                               | 4.05 ms: 1.03x faster                                                    |
| sqlite_synth            | 2.63 us                                                               | 2.56 us: 1.03x faster                                                    |
| genshi_text             | 21.3 ms                                                               | 20.8 ms: 1.03x faster                                                    |
| go                      | 134 ms                                                                | 131 ms: 1.02x faster                                                     |
| scimark_fft             | 321 ms                                                                | 315 ms: 1.02x faster                                                     |
| json_loads              | 23.9 us                                                               | 23.4 us: 1.02x faster                                                    |
| pprint_safe_repr        | 683 ms                                                                | 670 ms: 1.02x faster                                                     |
| pprint_pformat          | 1.40 sec                                                              | 1.38 sec: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                               | 17.8 ms: 1.02x faster                                                    |
| scimark_lu              | 112 ms                                                                | 110 ms: 1.02x faster                                                     |
| pickle_list             | 4.18 us                                                               | 4.10 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed | 732 ms                                                                | 724 ms: 1.01x faster                                                     |
| coverage                | 99.3 ms                                                               | 98.3 ms: 1.01x faster                                                    |
| sympy_sum               | 164 ms                                                                | 162 ms: 1.01x faster                                                     |
| sympy_str               | 283 ms                                                                | 280 ms: 1.01x faster                                                     |
| sqlalchemy_declarative  | 134 ms                                                                | 133 ms: 1.01x faster                                                     |
| sqlalchemy_imperative   | 16.9 ms                                                               | 16.7 ms: 1.01x faster                                                    |
| pickle_pure_python      | 290 us                                                                | 287 us: 1.01x faster                                                     |
| tornado_http            | 93.5 ms                                                               | 92.8 ms: 1.01x faster                                                    |
| xml_etree_parse         | 159 ms                                                                | 158 ms: 1.01x faster                                                     |
| fannkuch                | 369 ms                                                                | 366 ms: 1.01x faster                                                     |
| float                   | 72.6 ms                                                               | 72.1 ms: 1.01x faster                                                    |
| sympy_expand            | 456 ms                                                                | 453 ms: 1.01x faster                                                     |
| chameleon               | 6.50 ms                                                               | 6.46 ms: 1.01x faster                                                    |
| genshi_xml              | 49.4 ms                                                               | 49.1 ms: 1.01x faster                                                    |
| xml_etree_process       | 54.2 ms                                                               | 53.9 ms: 1.01x faster                                                    |
| aiohttp                 | 997 us                                                                | 991 us: 1.01x faster                                                     |
| regex_compile           | 128 ms                                                                | 127 ms: 1.01x faster                                                     |
| sqlglot_parse           | 1.35 ms                                                               | 1.34 ms: 1.01x faster                                                    |
| sympy_integrate         | 20.4 ms                                                               | 20.3 ms: 1.00x faster                                                    |
| django_template         | 32.6 ms                                                               | 32.5 ms: 1.00x faster                                                    |
| python_startup          | 8.42 ms                                                               | 8.41 ms: 1.00x faster                                                    |
| python_startup_no_site  | 5.93 ms                                                               | 5.94 ms: 1.00x slower                                                    |
| sqlglot_normalize       | 105 ms                                                                | 105 ms: 1.00x slower                                                     |
| async_generators        | 348 ms                                                                | 349 ms: 1.00x slower                                                     |
| sqlglot_optimize        | 51.3 ms                                                               | 51.5 ms: 1.00x slower                                                    |
| dulwich_log             | 62.5 ms                                                               | 62.8 ms: 1.00x slower                                                    |
| 2to3                    | 247 ms                                                                | 248 ms: 1.01x slower                                                     |
| scimark_monte_carlo     | 65.5 ms                                                               | 65.9 ms: 1.01x slower                                                    |
| hexiom                  | 6.04 ms                                                               | 6.08 ms: 1.01x slower                                                    |
| unpickle_pure_python    | 201 us                                                                | 203 us: 1.01x slower                                                     |
| json_dumps              | 9.22 ms                                                               | 9.30 ms: 1.01x slower                                                    |
| bench_thread_pool       | 774 us                                                                | 782 us: 1.01x slower                                                     |
| pickle                  | 10.1 us                                                               | 10.3 us: 1.01x slower                                                    |
| asyncio_tcp             | 861 ms                                                                | 872 ms: 1.01x slower                                                     |
| async_tree_io           | 1.30 sec                                                              | 1.31 sec: 1.01x slower                                                   |
| pyflate                 | 394 ms                                                                | 400 ms: 1.01x slower                                                     |
| scimark_sor             | 106 ms                                                                | 108 ms: 1.02x slower                                                     |
| telco                   | 6.45 ms                                                               | 6.58 ms: 1.02x slower                                                    |
| mdp                     | 2.54 sec                                                              | 2.59 sec: 1.02x slower                                                   |
| raytrace                | 282 ms                                                                | 290 ms: 1.03x slower                                                     |
| mako                    | 9.59 ms                                                               | 9.89 ms: 1.03x slower                                                    |
| crypto_pyaes            | 73.2 ms                                                               | 75.9 ms: 1.04x slower                                                    |
| generators              | 71.9 ms                                                               | 75.4 ms: 1.05x slower                                                    |
| regex_dna               | 207 ms                                                                | 218 ms: 1.05x slower                                                     |
| regex_v8                | 21.1 ms                                                               | 22.3 ms: 1.06x slower                                                    |
| spectral_norm           | 96.2 ms                                                               | 102 ms: 1.06x slower                                                     |
| pidigits                | 190 ms                                                                | 206 ms: 1.09x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (28): unpickle, async_tree_none, nbody, mypy, sqlglot_transpile, html5lib, djangocms, xml_etree_generate, logging_simple, thrift, logging_format, pylint, docutils, unpack_sequence, gunicorn, bench_mp_pool, logging_silent, json, deepcopy_reduce, chaos, create_gc_cycles, dask, coroutines, xml_etree_iterparse, async_tree_memoization, meteor_contest, deepcopy_memo, unpickle_list
