
# Results vs. base

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 250 ms: 1.01x faster                                                       |
| chameleon      | 6.35 ms                                                                | 6.38 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 74.0 ms                                                                | 71.8 ms: 1.03x faster                                                      |
| nbody          | 93.4 ms                                                                | 95.4 ms: 1.02x slower                                                      |
| pidigits       | 192 ms                                                                 | 193 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 127 ms: 1.01x faster                                                       |
| regex_effbot   | 3.50 ms                                                                | 3.54 ms: 1.01x slower                                                      |
| regex_v8       | 21.1 ms                                                                | 21.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 24.1 us                                                                | 24.0 us: 1.01x faster                                                      |
| pickle               | 10.1 us                                                                | 10.0 us: 1.01x faster                                                      |
| pickle_dict          | 30.7 us                                                                | 30.4 us: 1.01x faster                                                      |
| pickle_list          | 4.10 us                                                                | 3.96 us: 1.03x faster                                                      |
| pickle_pure_python   | 285 us                                                                 | 286 us: 1.01x slower                                                       |
| unpickle             | 13.2 us                                                                | 13.0 us: 1.02x faster                                                      |
| unpickle_pure_python | 198 us                                                                 | 196 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 105 ms                                                                 | 103 ms: 1.02x faster                                                       |
| xml_etree_generate   | 78.0 ms                                                                | 78.3 ms: 1.00x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (4): json_dumps, unpickle_list, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.96 ms                                                                | 8.90 ms: 1.01x faster                                                      |
| python_startup_no_site | 6.48 ms                                                                | 6.44 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 20.9 ms                                                                | 21.2 ms: 1.01x slower                                                      |
| genshi_xml     | 46.8 ms                                                                | 47.3 ms: 1.01x slower                                                      |
| mako           | 9.58 ms                                                                | 9.70 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230126-linux-x86_64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3                    | 252 ms                                                                 | 250 ms: 1.01x faster                                                       |
| aiohttp                 | 998 us                                                                 | 993 us: 1.00x faster                                                       |
| async_generators        | 354 ms                                                                 | 351 ms: 1.01x faster                                                       |
| async_tree_io           | 1.33 sec                                                               | 1.30 sec: 1.02x faster                                                     |
| chameleon               | 6.35 ms                                                                | 6.38 ms: 1.01x slower                                                      |
| chaos                   | 64.9 ms                                                                | 64.0 ms: 1.01x faster                                                      |
| bench_thread_pool       | 783 us                                                                 | 779 us: 1.00x faster                                                       |
| coroutines              | 24.8 ms                                                                | 25.2 ms: 1.02x slower                                                      |
| coverage                | 97.6 ms                                                                | 96.1 ms: 1.02x faster                                                      |
| crypto_pyaes            | 72.4 ms                                                                | 72.1 ms: 1.01x faster                                                      |
| deepcopy                | 335 us                                                                 | 327 us: 1.02x faster                                                       |
| deepcopy_memo           | 34.9 us                                                                | 34.3 us: 1.02x faster                                                      |
| deltablue               | 3.20 ms                                                                | 3.22 ms: 1.01x slower                                                      |
| djangocms               | 32.2 us                                                                | 32.8 us: 1.02x slower                                                      |
| fannkuch                | 363 ms                                                                 | 367 ms: 1.01x slower                                                       |
| float                   | 74.0 ms                                                                | 71.8 ms: 1.03x faster                                                      |
| create_gc_cycles        | 1.47 ms                                                                | 1.44 ms: 1.02x faster                                                      |
| gc_traversal            | 4.31 ms                                                                | 3.63 ms: 1.19x faster                                                      |
| generators              | 78.2 ms                                                                | 75.1 ms: 1.04x faster                                                      |
| genshi_text             | 20.9 ms                                                                | 21.2 ms: 1.01x slower                                                      |
| genshi_xml              | 46.8 ms                                                                | 47.3 ms: 1.01x slower                                                      |
| go                      | 133 ms                                                                 | 136 ms: 1.02x slower                                                       |
| gunicorn                | 1.08 ms                                                                | 1.06 ms: 1.01x faster                                                      |
| json_loads              | 24.1 us                                                                | 24.0 us: 1.01x faster                                                      |
| mako                    | 9.58 ms                                                                | 9.70 ms: 1.01x slower                                                      |
| mdp                     | 2.69 sec                                                               | 2.55 sec: 1.06x faster                                                     |
| nbody                   | 93.4 ms                                                                | 95.4 ms: 1.02x slower                                                      |
| nqueens                 | 79.0 ms                                                                | 78.5 ms: 1.01x faster                                                      |
| pickle                  | 10.1 us                                                                | 10.0 us: 1.01x faster                                                      |
| pickle_dict             | 30.7 us                                                                | 30.4 us: 1.01x faster                                                      |
| pickle_list             | 4.10 us                                                                | 3.96 us: 1.03x faster                                                      |
| pickle_pure_python      | 285 us                                                                 | 286 us: 1.01x slower                                                       |
| pidigits                | 192 ms                                                                 | 193 ms: 1.00x slower                                                       |
| pprint_safe_repr        | 679 ms                                                                 | 667 ms: 1.02x faster                                                       |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.02x faster                                                     |
| pyflate                 | 397 ms                                                                 | 399 ms: 1.00x slower                                                       |
| python_startup          | 8.96 ms                                                                | 8.90 ms: 1.01x faster                                                      |
| python_startup_no_site  | 6.48 ms                                                                | 6.44 ms: 1.01x faster                                                      |
| raytrace                | 287 ms                                                                 | 284 ms: 1.01x faster                                                       |
| regex_compile           | 129 ms                                                                 | 127 ms: 1.01x faster                                                       |
| regex_effbot            | 3.50 ms                                                                | 3.54 ms: 1.01x slower                                                      |
| regex_v8                | 21.1 ms                                                                | 21.2 ms: 1.01x slower                                                      |
| richards                | 42.3 ms                                                                | 41.7 ms: 1.01x faster                                                      |
| scimark_fft             | 305 ms                                                                 | 308 ms: 1.01x slower                                                       |
| scimark_lu              | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 66.6 ms                                                                | 65.2 ms: 1.02x faster                                                      |
| scimark_sor             | 107 ms                                                                 | 106 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult | 4.08 ms                                                                | 3.95 ms: 1.03x faster                                                      |
| spectral_norm           | 96.2 ms                                                                | 98.9 ms: 1.03x slower                                                      |
| sqlglot_parse           | 1.43 ms                                                                | 1.42 ms: 1.01x faster                                                      |
| sqlglot_transpile       | 1.72 ms                                                                | 1.70 ms: 1.01x faster                                                      |
| sqlglot_optimize        | 51.2 ms                                                                | 50.7 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                       |
| sqlite_synth            | 2.55 us                                                                | 2.61 us: 1.02x slower                                                      |
| sympy_expand            | 455 ms                                                                 | 451 ms: 1.01x faster                                                       |
| sympy_sum               | 155 ms                                                                 | 155 ms: 1.00x faster                                                       |
| sympy_str               | 271 ms                                                                 | 269 ms: 1.01x faster                                                       |
| telco                   | 6.36 ms                                                                | 6.30 ms: 1.01x faster                                                      |
| thrift                  | 752 us                                                                 | 746 us: 1.01x faster                                                       |
| unpack_sequence         | 43.7 ns                                                                | 41.9 ns: 1.04x faster                                                      |
| unpickle                | 13.2 us                                                                | 13.0 us: 1.02x faster                                                      |
| unpickle_pure_python    | 198 us                                                                 | 196 us: 1.01x faster                                                       |
| xml_etree_iterparse     | 105 ms                                                                 | 103 ms: 1.02x faster                                                       |
| xml_etree_generate      | 78.0 ms                                                                | 78.3 ms: 1.00x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (27): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp, bench_mp_pool, dask, deepcopy_reduce, django_template, docutils, dulwich_log, hexiom, html5lib, json, json_dumps, logging_format, logging_silent, logging_simple, meteor_contest, mypy, pathlib, pycparser, regex_dna, sympy_integrate, tornado_http, unpickle_list, xml_etree_parse, xml_etree_process
